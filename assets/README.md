# pezzotto.ai logo

| file | use |
|---|---|
| `mark.svg` | square mark: the "p." tile with its misprinted red ghost. Favicon, app icon, avatar |
| `wordmark.svg`, `wordmark-dark.svg` | "pezzotto.ai" alone, for light and dark backgrounds |
| `logo.svg`, `logo-dark.svg` | mark + wordmark, for light and dark backgrounds |
| `icon-192.png`, `icon-512.png`, `apple-touch-icon.png` | PNG favicons |
| `card.png` | 1200×630 social card |

Colours are the site's: paper `#f3eee2`, ink `#161412`, tarp blue `#1f4fd8`, stamp red `#c8312b`.
The glyphs are outlines of Archivo Black (Omnibus-Type, SIL Open Font License 1.1), so the SVGs
need no font. `src/make_logo.py` regenerates everything:

```sh
pip install fonttools
curl -LO https://github.com/google/fonts/raw/main/ofl/archivoblack/ArchivoBlack-Regular.ttf
python src/make_logo.py ArchivoBlack-Regular.ttf .
```

Use the logo to refer to pezzotto.ai; don't use it to suggest an endorsement.
