# Minecraft pack handbook

A Markdown reference for a developing Minecraft 1.21.1 / NeoForge 21.1.250 pack. The same reviewed pages feed a human GitHub Pages site and LLM-readable text exports. This checkout is not a pack download and contains no mod JARs, worlds or private configuration.

## Status

Development snapshot with partial tutorial coverage. [Read the handbook](https://faizsaifulnizam.github.io/minecraft-pack-wiki/) or give your chosen LLM the [combined text edition](https://faizsaifulnizam.github.io/minecraft-pack-wiki/llms-full.txt). If your model cannot open URLs, download that text file and attach it. Complete-pack gameplay, tutorial completion, multiplayer and performance remain unverified.

Read [the overview](index.md), [pack map](pack-map.md) and [evidence contract](sources.md).

## Checks and exports

Python 3.11 or newer; standard library only. Run from this directory:

```sh
python tests/check_wiki.py
python tools/wiki.py export --site-url https://faizsaifulnizam.github.io --base-path "/minecraft-pack-wiki"
python tools/wiki.py check --site-url https://faizsaifulnizam.github.io --base-path "/minecraft-pack-wiki"
```

Exports are `llms.txt`, `llms-full.txt` and one Markdown copy per page under `text/`. They omit frontmatter and rewrite relative page links to the explicit supplied address. The combined text is a fallback attachment for models that cannot browse the site. An `llms.txt` file does not ensure that every model will fetch or follow it.

The checker verifies the fixed public-file allowlist, frozen snapshot digest (including exact hashes and identity versions), ordinary inline Markdown links/heading anchors, required guide sections, selected private-path/token patterns and exact export parity. Page metadata and prospective text exports are checked before writing. Corrected sources can replace stale exports. It is not a general Markdown parser, secret detector, external-link checker, Jekyll renderer or runtime mod validator. Use the reviewed page conventions; do not add raw HTML, reference-style links or new content paths without extending tests and the allowlist.

## Human rendering

GitHub Pages/Jekyll consumes `_config.yml`, `_layouts/default.html` and `assets/style.css`. The supported `jekyll-relative-links` plugin is required to rewrite source Markdown links to their page permalinks. Before publishing, set the approved public `url` and `baseurl` in `_config.yml` and export with the same values. A project-site base path is not interchangeable with the domain root.

Ruby/Jekyll was not available in the initial local environment, so this edition does not claim a real local Jekyll render or browser layout test. Source checks and serving `.txt` are not substitutes. Require a successful authorized Jekyll/Pages build and fetch the actual human pages, nested guide, stylesheet and text exports before marking deployment ready.

## Updating

The safe snapshot is `_data/baseline.json`. Private extraction and source receipts are deliberately outside this repository. Recheck the instance privately after approved changes, compare exact identities and selected settings, then review affected prose. Do not automatically rewrite guides or silently loosen the frozen baseline tests. Update the baseline, evidence dates and tests together after review, then regenerate the text exports.

Keep starter instructions tied to shipped evidence and mark runtime checks separately. Do not infer a progression gate from an advancement parent, a power bridge from co-installed mods or a working recipe from a filename.

## Publication boundary

Public source is maintained at `faizsaifulnizam/minecraft-pack-wiki`, with GitHub Pages publishing from `main`. Only curated documentation and its checks belong here. No site backend, paid AI API, tracking or remote font is required. Do not redistribute bundled mod documentation or binaries wholesale.
