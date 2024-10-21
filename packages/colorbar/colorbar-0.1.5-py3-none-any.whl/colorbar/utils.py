import math
import cairo
import numpy as np
import importlib.resources
from cmap import Colormap
from cmap._color import ALL_COLORS
from PIL import Image, ImageDraw, ImageFont
DATA_PATH = str(importlib.resources.files('colorbar')) + '/data'
FONT = ImageFont.truetype(f'{DATA_PATH}/DejaVuSans.ttf')


class CMap:
    def __init__(self, cmap='gray', vmin=0, vmax=1, n=256, gamma=1.):
        colormap = Colormap(cmap)
        lut = colormap.lut(N=n, gamma=gamma)
        self.name = colormap.name
        self.lut = (lut * 255).astype(np.uint8)
        self.vmin = vmin
        self.vmax = vmax

    def __call__(self, x, vmin=None, vmax=None):
        self.vmin = x.min() if self.vmin is None else self.vmin
        self.vmax = x.max() if self.vmax is None else self.vmax
        x = (x - self.vmin) / (self.vmax - self.vmin)
        x = (x * len(self.lut)).astype(np.int16)
        return self.lut.take(x, axis=0, mode='clip')


def get_color_values(color, n_channels=4):
    assert 0 <= n_channels <= 4, 'n_channels must be between 0 and 4'
    values = ALL_COLORS[color] if isinstance(color, str) else color
    alpha = 255 if len(values) < 4 else values[3]
    values = list(values) if n_channels > 2 else [sum(values[:3]) // 3]
    return values[0] if n_channels == 0 else tuple((values + [alpha])[:n_channels])


def tick_values(vmin, vmax, num_ticks=5, steps=(1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10)):#(1, 2, 5, 10):
    raw_step = (vmax - vmin) / (num_ticks - 1)
    scale = 10 ** (math.log10(raw_step) // 1)
    good_tick_values, n_ticks = [], []
    for s in steps:
        vmin_scaled = round((vmin / scale) / s) * s
        vmax_scaled = round((vmax / scale) / s) * s
        tick_values = np.arange(vmin_scaled * scale, (vmax_scaled + s) * scale, s * scale)
        tick_values = tick_values[tick_values <= vmax]
        good_tick_values.append(tick_values)
        n_ticks.append(len(tick_values))
    idx_best = np.abs(np.array(n_ticks) - num_ticks).argmin()
    return good_tick_values[idx_best]


def draw(im, rectangle=None, lines=None, texts=None, font=FONT, linecolor='white', asarray=False):
    lines = lines or []
    texts = texts or []
    fonts = {text['fontsize']: font.font_variant(size=text['fontsize']) for text in texts}
    fill = get_color_values(linecolor, len(im.mode))
    draw = ImageDraw.Draw(im)
    if rectangle is not None:
        draw.rectangle(**rectangle, outline=fill)
    for line in lines:
        draw.line(**line) if 'fill' in line else draw.line(**line, fill=fill)
    for text in texts:
        text_kwargs = {}#'stroke_width': 1, 'stroke_fill': 'white' if linecolor == 'black' else 'black'}
        for k, v in text.items():
            if k != 'fontsize':
                text_kwargs.update({k: v})
        draw.text(fill=fill, font=fonts[text['fontsize']], **text_kwargs)
    return to_numpy(im) if asarray else im


def to_numpy(im):  # Taken from https://uploadcare.com/blog/fast-import-of-pillow-images-to-numpy-opencv-arrays/
    im.load()
    e = Image._getencoder(im.mode, 'raw', im.mode)
    e.setimage(im.im)
    shape, typestr = Image._conv_type_shape(im)
    data = np.empty(shape, dtype=np.dtype(typestr))
    mem = data.data.cast('B', (data.data.nbytes,))
    bufsize, s, offset = 65536, 0, 0
    while not s:
        l, s, d = e.encode(bufsize)
        mem[offset:offset + len(d)] = d
        offset += len(d)
    if s < 0:
        raise RuntimeError('encoder error %d in tobytes' % s)
    return data


def from_pil(im):
    arr = bytearray((im if im.mode == 'RGBA' else im.convert('RGBA')).tobytes('raw', 'BGRa'))
    return cairo.ImageSurface.create_for_data(arr, cairo.FORMAT_ARGB32, im.width, im.height)


def get_surface_class(filetype='pdf'):
    return {'svg': cairo.SVGSurface, 'eps': cairo.PSSurface, 'ps': cairo.PSSurface, 'pdf': cairo.PDFSurface}[filetype]


def get_source_rgba(color):
    rgba = get_color_values([color, color, color] if isinstance(color, int) else color, n_channels=4)
    return [c / 255 for c in rgba]


def draw_objects(ctx, patches=None, rectangles=None, lines=None, texts=None, linecolor='white', box=(0, 0)):
    ctx.set_source_rgba(*get_source_rgba(linecolor))
    if rectangles is not None:
        for rectangle in rectangles:
            draw_rectangle(ctx, box=box, **rectangle)
    if lines is not None:
        for line in lines:
            draw_line(ctx, box=box, **line)
    if texts is not None:
        for text in texts:
            draw_text(ctx, box=box, **text)
    if patches is not None:
        for patch in patches:
            draw_patch(ctx, box=box, **patch)


def draw_rectangle(ctx, xy, width, box=(0, 0), fill=None):
    if fill is not None:
        ctx_fill = ctx.get_source().get_rgba()
        ctx.set_source_rgba(*get_source_rgba(fill))
    ctx.set_line_width(max(width, 1.3))
    ctx.rectangle(xy[0] + width / 2 + box[0], xy[1] + width / 2 + box[1],
                  xy[2] - xy[0] - width + 1, xy[3] - xy[1] - width + 1)
    #ctx.stroke()
    if fill is not None:
        ctx.set_source_rgba(*ctx_fill)


def draw_line(ctx, xy, width, box=(0, 0), fill=None):
    if fill is not None:
        ctx_fill = ctx.get_source().get_rgba()
        ctx.set_source_rgba(*get_source_rgba(fill))
    ctx.set_line_width(max(width, 1.3))
    d = min(width / 2, 1)
    ctx.move_to(xy[0] + d + box[0], xy[1] + d + box[1])
    ctx.line_to(xy[2] + d + box[0], xy[3] + d + box[1])
    ctx.stroke()
    if fill is not None:
        ctx.set_source_rgba(*ctx_fill)


def draw_text(ctx, text, xy, fontsize, box=(0, 0), fill=None, **kwargs):
    if fill is not None:
        ctx_fill = ctx.get_source().get_rgba()
        ctx.set_source_rgba(*get_source_rgba(fill))
    ctx.select_font_face('DejaVuSans', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(fontsize)
    xbearing, ybearing, width, height, dx, dy = ctx.text_extents(text)
    anchor = kwargs['anchor'] if 'anchor' in kwargs else 'lt'
    dx = {'r': -dx, 'm': -.5 * dx, 'l': 0}[anchor[0]]
    dy = {'a': 1.25 * height, 't': height, 'm': .5 * height, 'b': 0, 'd': -.25 * height}[anchor[1]]
    ctx.move_to(xy[0] + dx + box[0], xy[1] + dy + box[1])
    ctx.show_text(text)
    if fill is not None:
        ctx.set_source_rgba(*ctx_fill)


def draw_patch(ctx, im, xy, box=(0, 0)):
    ctx.stroke()
    ctx.set_source_surface(from_pil(im.convert('RGBA')), xy[0] + box[0], xy[1] + box[1])
    ctx.paint()
