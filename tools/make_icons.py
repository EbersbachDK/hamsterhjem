"""Tegner app-ikonerne til PWA'en: spillets logo (hvidt hamsterhoved på orange baggrund).
Kør fra hamsterhjem/:  py tools/make_icons.py   ->  icons/*.png"""
import os
from PIL import Image, ImageDraw

ACCENT = (238, 154, 47)
INK = (27, 31, 44)
NOSE = (238, 136, 136)
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'icons')


def icon(size, scale=1.0):
    S = 1024  # tegnes stort og skaleres ned (kantudglatning)
    im = Image.new('RGB', (S, S), ACCENT)
    d = ImageDraw.Draw(im)
    # logoet er tegnet i et 30x30-net som SVG'en i index.html
    k = S / 30 * 0.82 * scale
    ox = oy = S / 2 - 15 * k

    def P(x, y):
        return ox + x * k, oy + y * k

    def ell(cx, cy, rx, ry, fill):
        x0, y0 = P(cx - rx, cy - ry); x1, y1 = P(cx + rx, cy + ry)
        d.ellipse([x0, y0, x1, y1], fill=fill)

    ell(15, 18, 11, 8.5, 'white')
    ell(9, 10, 3.4, 3.4, 'white'); ell(20, 10, 3.4, 3.4, 'white')
    ell(9, 10, 1.8, 1.8, (242, 169, 178)); ell(20, 10, 1.8, 1.8, (242, 169, 178))
    ell(11.5, 16.5, 1.3, 1.3, INK); ell(18.5, 16.5, 1.3, 1.3, INK)
    ell(15, 19.5, 1.2, 1.2, NOSE)
    return im.resize((size, size), Image.LANCZOS)


def main():
    os.makedirs(OUT, exist_ok=True)
    icon(180).save(os.path.join(OUT, 'apple-touch-icon.png'))
    icon(192).save(os.path.join(OUT, 'icon-192.png'))
    icon(512).save(os.path.join(OUT, 'icon-512.png'))
    icon(512, 0.72).save(os.path.join(OUT, 'icon-512-maskable.png'))  # holdes inden for sikker zone
    print('Ikoner skrevet til', OUT)


if __name__ == '__main__':
    main()
