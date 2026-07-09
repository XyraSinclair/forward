#!/usr/bin/env python3
"""Validate .forward/ ledgers against docs/ledger-schema.md.

Usage: validate-ledgers.py [repo-root]     (default: cwd)
Exit codes: 0 = valid, 1 = violations found, 2 = no .forward/ directory.
Distinguishes "no ledgers" from "invalid ledgers" — never collapses them.
"""
import json
import re
import sys
from pathlib import Path

LENSES = {"correctness", "duplication", "drift", "dead-code", "efficiency",
          "interfaces", "invariants", "error-paths", "spot-audit"}
VERDICTS = {"loved", "fine", "shrug", "disliked"}
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}([T ]\d{2}:\d{2}(:\d{2})?(\.\d+)?Z?)?$")

def fail(errs, where, msg):
    errs.append(f"{where}: {msg}")

def check_ts(errs, where, o):
    ts = o.get("ts", "MISSING")
    if ts == "MISSING":
        fail(errs, where, "missing ts field")
    elif ts is None:
        if not o.get("ts_note"):
            fail(errs, where, "ts null without ts_note explaining why")
    elif not (isinstance(ts, str) and ISO.match(ts)):
        fail(errs, where, f"ts not ISO-8601: {ts!r}")

def validate_hunt(path, errs):
    for i, line in enumerate(path.read_text().splitlines(), 1):
        where = f"{path.name}:{i}"
        try:
            o = json.loads(line)
        except json.JSONDecodeError as e:
            fail(errs, where, f"invalid JSON: {e}"); continue
        check_ts(errs, where, o)
        area = o.get("area", "")
        if not area or not isinstance(area, str):
            fail(errs, where, "missing area")
        elif "+" in area:
            fail(errs, where, f"compound area {area!r} (must be atomic)")
        if o.get("lens") not in LENSES:
            fail(errs, where, f"lens {o.get('lens')!r} not in vocabulary {sorted(LENSES)}")
        finds, issues = o.get("finds"), o.get("issues", [])
        if not isinstance(finds, int) or finds < 0:
            fail(errs, where, f"finds must be a non-negative int, got {finds!r}")
        elif finds != len(issues):
            fail(errs, where, f"finds={finds} but {len(issues)} issue strings")
        if not o.get("head"):
            fail(errs, where, "missing head (git provenance)")

def validate_worth(path, errs):
    for i, line in enumerate(path.read_text().splitlines(), 1):
        where = f"{path.name}:{i}"
        try:
            o = json.loads(line)
        except json.JSONDecodeError as e:
            fail(errs, where, f"invalid JSON: {e}"); continue
        check_ts(errs, where, o)
        if o.get("verdict") not in VERDICTS:
            fail(errs, where, f"verdict {o.get('verdict')!r} not in {sorted(VERDICTS)}")
        commits = o.get("commits")
        if not commits or not isinstance(commits, list):
            fail(errs, where, "missing commits list")
        elif any(c == "pending" for c in commits):
            fail(errs, where, 'commits contains "pending" (backfill before committing)')
        for field in ("area", "finds_addressed", "probes_spent", "worth_probes", "appraiser"):
            if field not in o:
                fail(errs, where, f"missing {field}")

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    fwd = root / ".forward"
    if not fwd.is_dir():
        print(f"no .forward/ at {root.resolve()} — nothing to validate (exit 2, distinct from valid)")
        return 2
    errs = []
    hunt, worth = fwd / "hunt.jsonl", fwd / "worth.jsonl"
    checked = []
    if hunt.exists():
        validate_hunt(hunt, errs); checked.append(hunt.name)
    if worth.exists():
        validate_worth(worth, errs); checked.append(worth.name)
    if not checked:
        print("`.forward/` exists but has no JSONL ledgers to validate (exit 2)")
        return 2
    if errs:
        print(f"INVALID — {len(errs)} violation(s) in {', '.join(checked)}:")
        for e in errs:
            print(f"  {e}")
        return 1
    print(f"valid: {', '.join(checked)} ({sum(1 for f in (hunt, worth) if f.exists())} files)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
