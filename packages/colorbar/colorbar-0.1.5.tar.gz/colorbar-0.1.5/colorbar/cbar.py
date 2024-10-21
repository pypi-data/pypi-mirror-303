import numpy as np
from PIL import Image
from cairo import Context
from colorbar.utils import FONT, draw, from_pil, tick_values, draw_objects, get_color_values, get_surface_class, CMap
VERTICAL = True
PAD, PAD_COLOR = 0, 'k'
X, Y = .9, .5
WIDTH, LENGTH = .05, .8


class CBar:
    def __init__(self, cmap=None, vmin=0, vmax=1, font=FONT):
        self.cmap = CMap(cmap, vmin, vmax) if isinstance(cmap, str) else cmap
        self.vmin = vmin
        self.vmax = vmax
        self.font = font
        self._bar = None
        self._bar_box = None
        self._rectangle = None
        self._lines = []
        self._texts = []

    def save(self, filepath, im, apply_cmap=True, vertical=VERTICAL, pad=PAD, pad_color=PAD_COLOR, x=X, y=Y,
             width=WIDTH, length=LENGTH, label=None, ticks=None, fontsize=20, linecolor='w', linewidth=2, tick_len=2):
        im = Image.fromarray(self.cmap(im) if apply_cmap else im)
        im = add_padding(im, vertical, pad, pad_color, x)
        SurfaceClass = get_surface_class(filepath.split('.')[-1])
        with SurfaceClass(filepath, im.size[0], im.size[1]) as surface:
            ctx = Context(surface)
            ctx = draw_background(ctx, pad_color)
            ctx.set_source_surface(from_pil(im.convert('RGBA')))
            ctx.paint()
            self.set_draw_objects(im.size, vertical, x, y, width, length, ticks, label, fontsize, tick_len, linewidth)
            lw = max(linewidth, 1.3)
            patches = [{'xy': [self._rectangle['xy'][0] + lw, self._rectangle['xy'][1] + lw],
                        'im': self._bar.crop((lw + 1, lw + 1, self._bar.size[0], self._bar.size[1]))}]
            draw_objects(ctx, patches, [self._rectangle], self._lines, self._texts, linecolor)
            surface.finish()

    def draw(self, im, apply_cmap=True, vertical=VERTICAL, pad=PAD, pad_color=PAD_COLOR, x=X, y=Y, width=WIDTH,
             length=LENGTH, label=None, ticks=None, fontsize=20, linecolor='w', linewidth=2, tick_len=2, asarray=False):
        im = Image.fromarray(self.cmap(im) if apply_cmap else im)
        im = add_padding(im, vertical, pad, pad_color, x)
        self.set_draw_objects(im.size, vertical, x, y, width, length, ticks, label, fontsize, tick_len, linewidth)
        im.paste(self._bar, self._bar_box)
        return draw(im, self._rectangle, self._lines, self._texts, self.font, linecolor, asarray)

    def get_bar(self, im_size, vmin, vmax, vertical, width, length):
        im_size = im_size if vertical else [im_size[1], im_size[0]]
        shape = (int(round(im_size[0] * width)), int(round(im_size[1] * length)))
        shape = (max(1, shape[0]), max(1, shape[1]))
        value_range = (vmax, vmin) if vertical else (vmin, vmax)
        bar = np.linspace(*value_range, max(shape[1], 1))
        bar = bar[:, None].repeat(max(shape[0], 1), axis=1)
        bar = bar if vertical else bar.swapaxes(0, 1)
        return Image.fromarray(self.cmap(bar))

    def get_tick_positions(self, ticks, vmin, vmax, bar_box, vertical):
        ticks = tick_values(self.vmin, self.vmax) if ticks is None else ticks
        tick_dict = ticks if isinstance(ticks, dict) else {v: f'{v:.4g}' for v in ticks}
        tick_positions = {}
        for value, label in tick_dict.items():
            if vmin <= value <= vmax:
                position = self.get_tick_position(value, vmin, vmax, bar_box, vertical)
                tick_positions.update({label: position})
        return tick_positions

    def set_draw_objects(self, im_size, vertical, x, y, width, length, ticks, label, fontsize, tick_len, linewidth):
        self._bar = self.get_bar(im_size, self.vmin, self.vmax, vertical, width, length)
        self._bar_box = self.get_bar_box(im_size, self._bar.size, vertical, x, y)
        tick_positions = self.get_tick_positions(ticks, self.vmin, self.vmax, self._bar_box, vertical)
        self._rectangle = self.get_bar_frame(self._bar_box, linewidth)
        self._lines = self.get_tick_lines(tick_positions, vertical, tick_len, linewidth)
        texts = self.get_tick_texts(tick_positions, vertical, int(.8 * fontsize), tick_len, linewidth)
        if label is not None:
            texts.append(self.get_label_text(label, self._bar_box, fontsize))
        self._texts = texts

    @staticmethod
    def get_tick_texts(ticks, vertical, fontsize, tick_len, linewidth):
        texts = []
        for text, pos in ticks.items():
            xy = pos
            xy[1 - vertical] += tick_len + linewidth + fontsize // 2
            texts.append({'xy': xy, 'text': text, 'anchor': 'lm' if vertical else 'mt', 'fontsize': fontsize})
        return texts

    @staticmethod
    def get_label_text(label, bar_box, fontsize):
        return {'xy': ((bar_box[0] + bar_box[2]) // 2, bar_box[1] - fontsize), 'text': label,
                'anchor': 'mb', 'fontsize': fontsize}

    @staticmethod
    def get_bar_frame(bar_box, linewidth):
        margin = (linewidth - 1) // 2
        return {'xy': (bar_box[0] - margin, bar_box[1] - margin, bar_box[2] + margin, bar_box[3] + margin),
                'width': linewidth}

    @staticmethod
    def get_tick_lines(ticks, vertical, tick_len, linewidth):
        lines = []
        for pos in ticks.values():
            line = [pos[0], pos[1], pos[0], pos[1]]
            line[3 - vertical] += tick_len + linewidth
            lines.append({'xy': tuple(line), 'width': linewidth})
        return lines

    @staticmethod
    def get_tick_position(value, vmin, vmax, bar_box, vertical):
        start = bar_box[1 if vertical else 0]
        end = bar_box[3 if vertical else 2]
        len_pos = (value - vmin) / (vmax - vmin)
        len_pos = 1 - len_pos if vertical else len_pos
        len_pos = int(round(len_pos * (end - start) + start))
        len_pos = max(start, min(len_pos, end - 1))
        #len_pos = int(len_pos * (end - start) + start)
        return [bar_box[2], len_pos] if vertical else [len_pos, bar_box[3]]

    @staticmethod
    def get_bar_box(im_size, bar_size, vertical, x, y):
        x0 = int(round(im_size[0] * (x if vertical else y) - bar_size[0] / 2))
        y0 = int(round(im_size[1] * (y if vertical else x) - bar_size[1] / 2))
        return x0, y0, x0 + bar_size[0], y0 + bar_size[1]


def add_padding(im, vertical=VERTICAL, pad=PAD, pad_color=PAD_COLOR, x=X, **kwargs):
    if pad > 0:
        color_value = get_color_values(pad_color, len(im.mode))
        size = (im.size[0] + pad, im.size[1]) if vertical else (im.size[0], im.size[1] + pad)
        pad_im = Image.new(im.mode, size, color_value)
        pad_im.paste(im, box=(0, 0) if x > .5 else (pad, 0) if vertical else (0, pad))
        return pad_im
    else:
        return im


def draw_background(ctx, pad_color=PAD_COLOR, **kwargs):
    color = get_color_values(color=pad_color, n_channels=4)  # len(im.mode))
    color = [c / 255 for c in color]
    ctx.set_source_rgba(*color)
    ctx.paint()
    return ctx


def get_pad_box(vertical=VERTICAL, pad=PAD, x=X, **kwargs):
    return pad if vertical and x < .5 else 0, pad if not vertical and x < .5 else 0
