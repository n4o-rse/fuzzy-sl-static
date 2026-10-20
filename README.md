# fuzzy-sl-static

Static, read-only copy of the Wikibase <https://fuzzy-sl.wikibase.cloud>, built with
[wikibase-static](https://github.com/n4o-rse/wikibase-static).

**State:** the items and properties of the source are archived in `data/raw/`
(`manifest.json` and one JSON file per entity, as the Wikibase API delivers them).
The pages are not built yet; the work plan is `PRIMER.md` in `wikibase-static`.

## Use

Python 3.10 or later.

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py harvest --probe
python main.py harvest
```

`harvest` reads the source address from `data/raw/manifest.json` and downloads only
what changed since the last run (`0 changed` when nothing did). If the Wikibase
answers with a bot challenge, the step stops and does not try to get around it.

## Data

The entities in `data/raw/` were published by the operators of the source Wikibase.
The licence of the source data is not recorded yet; it is an open point in the work plan of `wikibase-static`.
