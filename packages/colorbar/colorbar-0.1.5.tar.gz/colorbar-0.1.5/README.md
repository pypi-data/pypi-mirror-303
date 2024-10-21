# colorbar
Add a colorbar to an image in milliseconds (faster than `plt.imshow`+`plt.colorbar`) 💨

`colorbar` achieves its speed by avoiding [`matplotlib`](https://github.com/matplotlib/matplotlib) and instead using [`numpy`](https://github.com/numpy/numpy), [`pillow`](https://github.com/python-pillow/Pillow), [`cmap`](https://github.com/tlambert03/cmap) and [`pycairo`](https://github.com/pygobject/pycairo)!

🛠️ Install via: `pip install colorbar` (+ if pycairo causes trouble try `conda install anaconda::pycairo`)
## Usage 💡
```python
import numpy as np
from colorbar import CBar

shape = (400, 800)
im = np.linspace(0, 1, shape[0] * shape[1]).reshape(*shape)  # dummy image
cbar = CBar(cmap='gray',    # see https://cmap-docs.readthedocs.io/en/latest/catalog/
            vmin=im.min(),  # pixels <= vmin become first color of cmap
            vmax=im.max())  # pixels >= vmax become last color of cmap
im_cbar = cbar.draw(im)  # draw colorbar!
im_cbar.show()
```
![cbar](https://github.com/user-attachments/assets/fdfc61f8-6aeb-4895-9050-f349037675c6)

`draw()` returns a [`PIL.Image`](https://pillow.readthedocs.io/en/stable/reference/Image.html) that is shown via [`show()`](https://pillow.readthedocs.io/en/stable/reference/ImageShow.html) and saved via [`save()`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save)
```python
im_cbar.save('cbar.png')
```

Use `cbar.save()` instead of `im=cbar.draw()`+`im.save()` to save the image as a vector graphic
```python
...
cbar.save('cbar.pdf', im)  # .pdf, .svg, .ps or .eps
```
To customize the colorbar, `draw()` and `save()` take the arguments:
- `vertical`: If True, colorbar is vertical. Default: `True`
- `pad`: Added pixel rows on the colorbar-side of the image. Default: `0`
- `pad_color`: [Color-string](https://cmap-docs.readthedocs.io/en/latest/colors/) of added pixels. Default: `'k'`(=black) 
- `x`: Position of the colorbar center relative to image in width-direction. Default: `.9`
- `y`: Position of the colorbar center relative to image in length-direction. Default: `.5`
- `width`: Size of the colorbar relative to image. Default: `.05`
- `length`: Size of the colorbar relative to image. Default: `.8`
- `label`: Label above the colorbar. Default: `None`
- `ticks`: List (e.g. `[0, 1]`) or dict (e.g. `{0: 'low', 1: 'high'}`) of ticks. Default: `None`
- `fontsize`: Fontsize of labels and ticks. Default: `20`
- `linecolor`: Color of the lines and the font used to write labels and ticks. Default: `w`(=white) 
- `linewidth`: Width of ticklines and outlines. Default: `2`
- `tick_len`: Length of ticklines. Default: `2`

Finally, if you want `draw()` to return a `numpy` array use `asarray=True`
```python
im_cbar = cbar.draw(im, asarray=True)
```
to e.g. plot it with [`matplotlib`](https://matplotlib.org/stable/tutorials/images.html#sphx-glr-tutorials-images-py) via `plt.imshow(im_cbar)`.
