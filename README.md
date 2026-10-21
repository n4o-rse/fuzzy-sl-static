# fuzzy-sl-static

Static, read-only copy of the Wikibase <https://fuzzy-sl.wikibase.cloud>, built with
[wikibase-static](https://github.com/n4o-rse/wikibase-static). 

**State:** the items and properties of the source are archived in `data/raw/`
(`manifest.json` and one JSON file per entity, as the Wikibase API delivers them).
`python main.py build` renders them into `docs/` (one page per item and property, a start page,
a language switch, a search box, maps for coordinates, the logo top left, laid out like the Wikibase itself);
`site.yaml` holds title, languages, source, the logo (`assets/logo.jpg`) and, if you want one,
a licence other than CC0.
The search box finds an entity by label, alias or Q-/P-id (`python main.py search` writes its index,
`docs/assets/search-index.js`; the default run does).
The data is also published as RDF in the data model of Wikibase: `dist/fuzzy-sl.wikibase.cloud.ttl` (everything, described with DCAT 3),
`docs/ttl/Q1.ttl` and `docs/json/Q1.json` (one file per entity), and `docs/sparql.html` lets you query it in the browser
(`python main.py rdf`, `python main.py sparql`; the default run does both). The work plan is `PRIMER.md` in `wikibase-static`.

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
number of pages and a link check; run it twice and `git status` stays clean. The search box needs
`wikibase-static` 0.2.0 or later, the RDF export and the query page 0.3.0 or later; after a new release run `pip install --upgrade -r requirements.txt`
(pip keeps an installed package of the same version, so a branch that does not change the version number
needs `--force-reinstall --no-deps`).
`python main.py --strict` does the same and treats every `WARN` line (a dead internal link, an entity that
does not load) as an error.

## Publishing

`.github/workflows/site.yml` runs on every push and pull request: `python main.py --strict` twice, with
`git status` required to be clean after each run (so the committed `docs/` is what a fresh build makes),
and, on `main`, publishes `docs/` to GitHub Pages. Set Settings, Pages, Source to "GitHub Actions" once.
After a harvest or a change to `site.yaml`, run `python main.py` and commit `data/` and `docs/` together.

## Data

The entities in `data/raw/` were published by the operators of the source Wikibase.
The pages state the licence CC0 1.0 (Public Domain) in their footer, which is the default of
`wikibase-static`. If the operators name another licence, write it as `license` in `site.yaml`.
