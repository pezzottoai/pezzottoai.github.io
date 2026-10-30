# pezzotto.ai

> **pezzotto** /pe'tsɔt.to/ — Neapolitan. A knock-off. The bootleg CD on a blanket
> outside the station. Also: something patched together from pieces that mostly works.

A street stall of vibecoded clones of closed-source apps, and the workshop that makes them.

This repository is the site at **https://pezzotto.ai** and the catalog it serves.

## Two halves

1. **'O bancariello — the catalog.** A curated index of open-source, vibecoded clones of
   closed-source apps. Each entry names the original, links the clone, records license,
   stack, feature coverage and maintenance status, and assigns a *pezzotto grade*
   (A: fools you at arm's length … D: you'd have to be told). See [`catalog/`](catalog/).
2. **'A fraveca — the harness.** A tool that drives a coding agent from a closed-source
   target to a working clone: `spec` the original from public behaviour, `build` it feature
   by feature, `grade` the result, and emit the catalog entry (`stall`). The harness lives
   in its own repository under the [pezzottoai](https://github.com/pezzottoai) organization.

3. **'O guaglione — the launcher.** The [pezzotto.ai launcher](https://github.com/pezzottoai/launcher)
   installs and launches open-source apps, including the clones on the blanket, on Linux,
   Windows and macOS. Its own app manifests live in
   [launcher-catalog](https://github.com/pezzottoai/launcher-catalog).

## This repo

```
index.html            the site, static, no build step
catalog/clones.json   the stall: a JSON array of entries
catalog/README.md     entry format, grade scale, rules
```

The page fetches `catalog/clones.json` at load and renders cards with search and status
filter. It is in English, Italian and Neapolitan: the English text is the HTML itself, the
other two live in the `I18N` table in the page script (`data-i18n` keys), and the switcher
in the nav remembers the choice. `?lang=it` or `?lang=nap` picks one directly. Open `index.html` through any static server to preview (`python3 -m http.server`).

## Add a clone

1. Fork this repo.
2. Append an entry to `catalog/clones.json` following [`catalog/README.md`](catalog/README.md).
   Any clone qualifies, yours or someone else's, as long as it is open source and the
   original is closed source.
3. Open a pull request. A human checks the clone actually runs, then grades it.

## License

Site and code: [MIT](LICENSE). Catalog data (`catalog/clones.json`): CC0.

No affiliation with any of the originals. That's the point.
