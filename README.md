# fuzzy-sl-static

Static, read-only copy of the Wikibase <https://fuzzy-sl.wikibase.cloud>, built with
[wikibase-static](https://github.com/n4o-rse/wikibase-static).

**State:** the items and properties of the source are archived in `data/raw/`
(`manifest.json` and one JSON file per entity, as the Wikibase API delivers them).
`python main.py build` renders them into `docs/` (one page per item and property, a start page,
a language switch, maps for coordinates, the logo top left, laid out like the Wikibase itself);
`site.yaml` holds title, languages, source, the logo (`assets/logo.jpg`) and, if you want one,
a licence other than CC0.
Search and the SPARQL page are not built yet; the work plan is `PRIMER.md` in `wikibase-static`.

## Use

Python 3.10 or later.

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py harvest --probe
python main.py harvest
python main.py build
```

`harvest` reads the source address from `data/raw/manifest.json` and downloads only
what changed since the last run (`0 changed` when nothing did). If the Wikibase
answers with a bot challenge, the step stops and does not try to get around it.

`build` needs no network. It reads `data/raw/` and `site.yaml`, writes `docs/` and reports the
number of pages and a link check; run it twice and `git status` stays clean. To publish, serve
`docs/` with GitHub Pages (Settings, Pages, branch `main`, folder `/docs`).

## Data

The entities in `data/raw/` were published by the operators of the source Wikibase.
The pages state the licence CC0 1.0 (Public Domain) in their footer, which is the default of
`wikibase-static`. If the operators name another licence, write it as `license` in `site.yaml`.
