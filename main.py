#!/usr/bin/env python3
"""Entry point of this site repository (thin wrapper around the wikibase-static package).

    python main.py harvest              back up the Wikibase named in data/raw/manifest.json (network)
    python main.py harvest --probe      one test request, writes nothing
    python main.py                      all other steps in order (build, search, rdf, sparql)
    python main.py --list               print the steps and exit

Everything is done by the installed package ``wikibase-static``; this file only
points it at this repository (WBS_ROOT) and starts the steps. It will be replaced
by the command line of the package once the template repository exists
(PRIMER.md of wikibase-static, S9). Any further arguments are passed to the step.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# (name, module, in the default run). harvest is the only step that uses the network.
STEPS = [
    ("harvest", "step_harvest", False),
    ("from-csv", "step_from_csv", True),
    ("build", "step_build", True),
    ("search", "step_search", True),
    ("rdf", "step_rdf", True),
    ("sparql", "step_sparql", True),
]


def run(module: str, extra: list[str]) -> int:
    env = dict(os.environ, WBS_ROOT=str(ROOT), PYTHONIOENCODING="utf-8")
    return subprocess.call([sys.executable, "-m", f"wikibase_static.{module}", *extra], cwd=ROOT, env=env)


def main(argv: list[str]) -> int:
    if argv[:1] == ["--list"]:
        for name, _module, default in STEPS:
            print(f"{name:9} {'default' if default else 'verb'}")
        return 0
    names = [name for name, _m, _d in STEPS]
    if argv and argv[0] in names:
        module = next(m for n, m, _d in STEPS if n == argv[0])
        return run(module, argv[1:])
    if argv:
        print(f"unknown step {argv[0]!r}; use --list", file=sys.stderr)
        return 2
    for name, module, default in STEPS:
        if default:
            print(f"[{name}]")
            code = run(module, [])
            if code:
                return code
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
