#!/usr/bin/env python3
"""dump_fp_examples.py — print actual irrelevant-labeled sentences for REVIEW-tier terms,
so we can design context constraints (and document why we did/did not gate them)."""
import csv, sys
from pathlib import Path

PROJ = Path("/Users/andy/Desktop/Research/visibility-bias-v2")
ENSEMBLE = PROJ / "03-analysis/phase-G/passage_coding_sheet_ensemble.csv"

TERMS = ["示范", "文明城市", "展示", "美丽", "形象", "样板", "整洁", "门户", "装饰"]

rows = list(csv.DictReader(open(ENSEMBLE, encoding="utf-8-sig")))
for term in TERMS:
    print(f"\n========== {term} : sentences ensemble-judged IRRELEVANT ==========")
    hits = [r for r in rows if term in r["sentence"]
            and r.get("ensemble_majority", "").strip().lower() == "irrelevant"]
    for r in hits[:8]:
        print(f"  [{r['sample_id']}] {r['sentence'][:160]}")
    print(f"\n========== {term} : sentences ensemble-judged VISIBLE (anchor uses) ==========")
    hits_v = [r for r in rows if term in r["sentence"]
              and r.get("ensemble_majority", "").strip().lower() == "visible"]
    for r in hits_v[:5]:
        print(f"  [{r['sample_id']}] {r['sentence'][:160]}")
