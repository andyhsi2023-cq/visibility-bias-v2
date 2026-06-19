#!/usr/bin/env python3
"""score_anchor.py — score the human anchor against the dictionary and the model ensemble.

    python3 score_anchor.py anchor_human_labels.csv               # 1 coder
    python3 score_anchor.py coder_andy.csv coder_two.csv          # 2 coders -> human intercoder kappa

Reports, with the human label as ground truth:
  • dictionary precision/recall/F1 per class (the reviewer's core ask)
  • ensemble-majority vs human agreement + Cohen's kappa (licenses scaling to the full 500)
  • human1 vs human2 Cohen's kappa, if a second coder file is given (the human intercoder kappa)
"""
import csv, sys, math
from collections import defaultdict, Counter
from pathlib import Path

LABELS = ["visible", "functional", "mixed", "irrelevant"]

def norm(x):
    x = (x or "").strip().lower()
    for L in LABELS:
        if x.startswith(L[:4]):
            return L
    return None

def load_labels(path):
    d = {}
    for r in csv.DictReader(open(path, encoding="utf-8-sig")):
        lab = norm(r.get("human_label") or r.get("label"))
        if lab:
            d[r["sample_id"]] = lab
    return d

def kappa(pairs):
    pairs = [(a, b) for a, b in pairs if a and b]
    if not pairs:
        return float("nan"), 0
    po = sum(1 for a, b in pairs if a == b) / len(pairs)
    ca = Counter(a for a, _ in pairs); cb = Counter(b for _, b in pairs); m = len(pairs)
    pe = sum((ca[L] / m) * (cb[L] / m) for L in LABELS)
    return ((po - pe) / (1 - pe) if pe < 1 else float("nan")), len(pairs)

def prf(pred_truth):  # list of (pred, truth)
    cm = defaultdict(Counter)
    for p, t in pred_truth:
        cm[t][p] += 1
    print("            " + "".join(f"{L[:5]:>9}" for L in LABELS) + "   (cols=dict pred, rows=human)")
    for t in LABELS:
        print(f"{t:>11} " + "".join(f"{cm[t][p]:>9}" for p in LABELS))
    for L in LABELS:
        tp = cm[L][L]; fp = sum(cm[t][L] for t in LABELS if t != L); fn = sum(cm[L][p] for p in LABELS if p != L)
        prec = tp / (tp + fp) if tp + fp else float("nan")
        rec = tp / (tp + fn) if tp + fn else float("nan")
        f1 = 2 * prec * rec / (prec + rec) if (prec and rec and prec + rec and not math.isnan(prec) and not math.isnan(rec)) else float("nan")
        print(f"  {L:>11}: precision={prec:.3f}  recall={rec:.3f}  f1={f1:.3f}  (n_human={sum(cm[L].values())})")

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    key = {r["sample_id"]: r for r in csv.DictReader(open("anchor_key.csv", encoding="utf-8-sig"))}
    h1 = load_labels(sys.argv[1])
    print(f"[anchor] human coder 1: {len(h1)} labels")

    common = [sid for sid in h1 if sid in key]
    print(f"\n=== Dictionary vs human (n={len(common)}) ===")
    prf([(norm(key[s]["dict_label"]), h1[s]) for s in common])

    k_he, n_he = kappa([(key[s]["ensemble_majority"] and norm(key[s]["ensemble_majority"]), h1[s]) for s in common])
    print(f"\n=== Ensemble-majority vs human ===\nCohen's kappa = {k_he:.3f}  (n={n_he})  "
          f"agreement={sum(1 for s in common if norm(key[s]['ensemble_majority'])==h1[s])/max(1,n_he):.3f}")

    if len(sys.argv) > 2:
        h2 = load_labels(sys.argv[2])
        k_hh, n_hh = kappa([(h1[s], h2[s]) for s in h1 if s in h2])
        print(f"\n=== Human intercoder (coder1 vs coder2) ===\nCohen's kappa = {k_hh:.3f}  (n={n_hh})")
    else:
        print("\n(Provide a 2nd coder file for the human intercoder kappa the reviewer asks for.)")

if __name__ == "__main__":
    main()
