#!/usr/bin/env python3
"""Generate the pezzotto.ai logo files as self-contained SVG (glyphs outlined from Archivo Black).

usage: make_logo.py FONT.ttf OUT_DIR
"""
import pathlib
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT, OUT = sys.argv[1], pathlib.Path(sys.argv[2])
font = TTFont(FONT)
UPM = font["head"].unitsPerEm
GS = font.getGlyphSet()
CMAP = font.getBestCmap()

LIGHT = {"ink": "#161412", "paper": "#f3eee2", "tarp": "#1f4fd8", "stamp": "#c8312b"}
DARK = {"ink": "#f0e9d8", "paper": "#17150f", "tarp": "#6f93ff", "stamp": "#ff6a5f"}


def text_paths(text, size, x, y):
    """[(char, svg path d)] for `text` drawn at font size `size`, baseline origin (x, y)."""
    s = size / UPM
    out = []
    for ch in text:
        g = GS[CMAP[ord(ch)]]
        pen = SVGPathPen(GS)
        g.draw(TransformPen(pen, (s, 0, 0, -s, x, y)))
        out.append((ch, pen.getCommands()))
        x += g.width * s
    return out, x


def text_bounds(text, size, x, y):
    s = size / UPM
    xmin = ymin = float("inf")
    xmax = ymax = float("-inf")
    for ch in text:
        g = GS[CMAP[ord(ch)]]
        bp = BoundsPen(GS)
        g.draw(TransformPen(bp, (s, 0, 0, -s, x, y)))
        if bp.bounds:
            a, b, c, d = bp.bounds
            xmin, ymin, xmax, ymax = min(xmin, a), min(ymin, b), max(xmax, c), max(ymax, d)
        x += g.width * s
    return xmin, ymin, xmax, ymax


def fmt(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def paths_svg(paths, pal, extra=""):
    """Wordmark colouring: letters in ink, the dot in tarp blue."""
    parts = []
    for ch, d in paths:
        color = pal["tarp"] if ch == "." else pal["ink"]
        parts.append(f'<path fill="{color}"{extra} d="{d}"/>')
    return "\n".join(parts)


def mark_svg(pal, size=512):
    """Square mark: a paper tile with 'p.' and a red misprinted ghost behind it (a bootleg print)."""
    fs = size * 0.70
    bx0, by0, bx1, by1 = text_bounds("p.", fs, 0, 0)
    w, h = bx1 - bx0, by1 - by0
    # centre the "p." box in the tile, nudged up a little so the descender doesn't drag it down
    x = (size - w) / 2 - bx0
    y = (size - h) / 2 - by0 - size * 0.015
    paths, _ = text_paths("p.", fs, x, y)
    off = size * 0.03
    r = size * 0.21
    inset = size * 0.02
    stroke = size * 0.035
    body = "\n".join([
        f'<rect x="{fmt(inset)}" y="{fmt(inset)}" width="{fmt(size - 2 * inset)}" height="{fmt(size - 2 * inset)}" rx="{fmt(r)}" fill="{pal["paper"]}" stroke="{pal["ink"]}" stroke-width="{fmt(stroke)}"/>',
        f'<g transform="translate({fmt(off)} {fmt(off * 0.8)})">',
        "\n".join(f'<path fill="{pal["stamp"]}" d="{d}"/>' for _, d in paths),
        "</g>",
        paths_svg(paths, pal),
    ])
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" role="img" aria-label="pezzotto.ai">\n{body}\n</svg>\n', (x, y, fs)


def wordmark_svg(pal, fs=100, pad=6):
    bx0, by0, bx1, by1 = text_bounds("pezzotto.ai", fs, 0, 0)
    x, y = pad - bx0, pad - by0
    paths, _ = text_paths("pezzotto.ai", fs, x, y)
    w, h = bx1 - bx0 + 2 * pad, by1 - by0 + 2 * pad
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {fmt(w)} {fmt(h)}" role="img" aria-label="pezzotto.ai">\n'
            f"{paths_svg(paths, pal)}\n</svg>\n")


def logo_svg(pal, fs=100, pad=8, gap=0.26):
    """Mark + wordmark, the mark as tall as the text block (ascender to descender)."""
    bx0, by0, bx1, by1 = text_bounds("pezzotto.ai", fs, 0, 0)
    th = by1 - by0
    mark_size = th * 1.08
    mark_svg_text, _ = mark_svg(pal, 512)
    inner = mark_svg_text.split(">\n", 1)[1].rsplit("</svg>", 1)[0]
    tx = pad + mark_size + fs * gap - bx0
    ty = pad + (mark_size - th) / 2 - by0
    paths, _ = text_paths("pezzotto.ai", fs, tx, ty)
    w = tx + bx1 + pad
    h = mark_size + 2 * pad
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {fmt(w)} {fmt(h)}" role="img" aria-label="pezzotto.ai">\n'
            f'<g transform="translate({fmt(pad)} {fmt(pad)}) scale({mark_size / 512:.5f})">\n{inner}</g>\n'
            f"{paths_svg(paths, pal)}\n</svg>\n")


OUT.mkdir(parents=True, exist_ok=True)
(OUT / "mark.svg").write_text(mark_svg(LIGHT)[0])
(OUT / "wordmark.svg").write_text(wordmark_svg(LIGHT))
(OUT / "wordmark-dark.svg").write_text(wordmark_svg(DARK))
(OUT / "logo.svg").write_text(logo_svg(LIGHT))
(OUT / "logo-dark.svg").write_text(logo_svg(DARK))
for p in sorted(OUT.glob("*.svg")):
    print(p, p.stat().st_size, "bytes")
