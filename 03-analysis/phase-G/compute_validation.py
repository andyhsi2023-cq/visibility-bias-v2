#!/usr/bin/env python3
"""compute_validation.py — confusion matrix + precision/recall/F1 (+ Cohen's kappa)
for the VAI passage-level validation (Phase G).

Dictionary label (`dict_label`) is the PREDICTION; a human/pilot column is GROUND TRUTH.

    python3 compute_validation.py --sheet passage_coding_sheet.csv --truth adjudicated --coder2 coder2
    python3 compute_validation.py --sheet passage_coding_sheet_pilot.csv --truth coder_llm   # pilot
"""
import argparse, csv, json, math
from collections import defaultdict, Counter
from pathlib import Path

LABELS = ["visible", "functional", "mixed", "irrelevant"]

def norm(x):
    x = (x or "").strip().lower()
    for L in LABELS:
        if x == L or x.startswith(L[:4]):
            return L
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", required=True)
    ap.add_argument("--truth", default="adjudicated", help="ground-truth column (human consensus)")
    ap.add_argument("--pred", default="dict_label", help="prediction column")
    ap.add_argument("--coder2", default=None, help="second coder column for kappa vs --truth")
    a = ap.parse_args()

    rows = list(csv.DictReader(open(a.sheet, encoding="utf-8-sig")))
    if not rows:
        print("empty sheet"); return
    def col(name):
        for c in rows[0].keys():
            if c == name or c.startswith(name):
                return c
        return name
    tcol, pcol = col(a.truth), col(a.pred)
    pairs = [(norm(r.get(pcol)), norm(r.get(tcol))) for r in rows]
    pairs = [(p, t) for p, t in pairs if p and t]
    n = len(pairs)
    print(f"[validation] {n} labeled rows  (pred={pcol} vs truth={tcol})")
    if not n:
        print("No labeled rows — fill the truth column first."); return

    cm = defaultdict(Counter)
    for p, t in pairs:
        cm[t][p] += 1
    print("\nConfusion (rows = truth, cols = dict prediction):")
    print("            " + "".join(f"{L[:5]:>9}" for L in LABELS))
    for t in LABELS:
        print(f"{t:>11} " + "".join(f"{cm[t][p]:>9}" for p in LABELS))

    print("\nPer-class:")
    out = {}
    for L in LABELS:
        tp = cm[L][L]
        fp = sum(cm[t][L] for t in LABELS if t != L)
        fn = sum(cm[L][p] for p in LABELS if p != L)
        prec = tp / (tp + fp) if tp + fp else float("nan")
        rec = tp / (tp + fn) if tp + fn else float("nan")
        f1 = (2 * prec * rec / (prec + rec)) if (prec and rec and prec + rec
              and not math.isnan(prec) and not math.isnan(rec)) else float("nan")
        out[L] = {"precision": round(prec, 3), "recall": round(rec, 3),
                  "f1": round(f1, 3), "n_truth": sum(cm[L].values())}
        print(f"  {L:>11}: precision={prec:.3f}  recall={rec:.3f}  f1={f1:.3f}  (n_truth={sum(cm[L].values())})")
    acc = sum(cm[L][L] for L in LABELS) / n
    print(f"\nOverall accuracy: {acc:.3f}")

    if a.coder2:
        c2 = col(a.coder2)
        kp = [(norm(r.get(tcol)), norm(r.get(c2))) for r in rows]
        kp = [(x, y) for x, y in kp if x and y]
        if kp:
            po = sum(1 for x, y in kp if x == y) / len(kp)
            mx = Counter(x for x, _ in kp); my = Counter(y for _, y in kp); m = len(kp)
            pe = sum((mx[L] / m) * (my[L] / m) for L in LABELS)
            kappa = (po - pe) / (1 - pe) if pe < 1 else float("nan")
            print(f"Cohen's kappa ({tcol} vs {c2}): {kappa:.3f}  (n={len(kp)})")
            out["kappa"] = round(kappa, 3)

    Path(a.sheet).with_suffix(".validation.json").write_text(
        json.dumps({"n": n, "accuracy": round(acc, 3), "per_class": out}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    print(f"[write] {Path(a.sheet).with_suffix('.validation.json')}")

if __name__ == "__main__":
    main()
