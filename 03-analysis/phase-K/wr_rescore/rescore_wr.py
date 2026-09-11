# -*- coding: utf-8 -*-
"""R2 measure unification, step 1: re-score passage samples with the recommended
wr_visibility dictionary (FACADE 20 / LIZI 16, verbatim from
phase-J/build_workreport_text.py) and compare against
(a) the 120-sentence human gold standard (C.8a replacement), and
(b) the 499-sentence LLM-ensemble majority (C.8c replacement)."""
import csv, json
from collections import defaultdict, Counter
from pathlib import Path

K = Path("/Users/andy/Desktop/Research/visibility-bias-v2/03-analysis/phase-K")
OUT = K / "wr_rescore"

FACADE = ['绿化','园林','景观','亮化','公园','绿地','美化','广场','风貌','绿道','街景','花园','道路','路网','桥梁','立交','轨道','地铁','大道','景观带']
LIZI   = ['排水','排涝','管网','管道','防洪','地下管','污水','供水','管廊','内涝','下水道','排污','给排水','防汛','地下空间','雨水']

def wr_label(txt):
    fc = sum(txt.count(w) for w in FACADE)
    lc = sum(txt.count(w) for w in LIZI)
    if fc > 0 and lc > 0: return "mixed"
    if fc > 0: return "visible"
    if lc > 0: return "functional"
    return "irrelevant"

LABELS = ["visible", "functional", "mixed", "irrelevant"]
def kappa(pairs):
    pairs = [(a, b) for a, b in pairs if a and b]
    if not pairs: return float("nan"), 0
    po = sum(1 for a, b in pairs if a == b) / len(pairs)
    ca = Counter(a for a, _ in pairs); cb = Counter(b for _, b in pairs); m = len(pairs)
    pe = sum((ca[L] / m) * (cb[L] / m) for L in LABELS)
    return ((po - pe) / (1 - pe) if pe < 1 else float("nan")), len(pairs)

def prf(pred_truth, name):
    cm = defaultdict(Counter)
    for p, t in pred_truth: cm[t][p] += 1
    print(f"\n{name} (rows = truth, cols = wr prediction)")
    print("            " + "".join(f"{L[:5]:>9}" for L in LABELS))
    for t in LABELS:
        print(f"{t:>11} " + "".join(f"{cm[t][p]:>9}" for p in LABELS))
    out = {}
    for L in LABELS:
        tp = cm[L][L]; fp = sum(cm[t][L] for t in LABELS if t != L); fn = sum(cm[L][p] for p in LABELS if p != L)
        prec = tp / (tp + fp) if tp + fp else float("nan")
        rec  = tp / (tp + fn) if tp + fn else float("nan")
        f1 = 2*prec*rec/(prec+rec) if (prec and rec) else float("nan")
        out[L] = {"precision": round(prec,3), "recall": round(rec,3), "f1": round(f1,3), "n_truth": sum(cm[L].values())}
        print(f"  {L:>11}: precision={prec:.3f}  recall={rec:.3f}  f1={f1:.3f}  (n={sum(cm[L].values())})")
    n = sum(sum(cm[t].values()) for t in LABELS)
    acc = sum(cm[L][L] for L in LABELS) / n
    print(f"  overall accuracy = {acc:.3f} ({sum(cm[L][L] for L in LABELS)}/{n})")
    return out, round(acc,3)

# ---- (a) 120-sentence human gold ----
key = {r["sample_id"]: r for r in csv.DictReader(open(K/"anchor_key.csv", encoding="utf-8-sig"))}
human = {}
for r in csv.DictReader(open(K/"anchor_human_labels.csv", encoding="utf-8-sig")):
    human[r["sample_id"]] = r["human_label"].strip().lower()

rows = []
for sid, lab in human.items():
    sent = key.get(sid, {}).get("sentence", "")
    rows.append((wr_label(sent), lab, sid, sent))
n_h = len(rows)
print(f"human gold: {n_h} sentences scored with wr dictionary")
prf([(p, t) for p, t, *_ in rows], "wr dictionary vs human gold (n=120)")
k_h, n_hh = kappa([(p, t) for p, t, *_ in rows])
print(f"wr-dict vs human Cohen kappa = {k_h:.3f} (n={n_hh})")

# also wr vs ensemble on the 120
pairs_e120 = []
for sid, lab in human.items():
    ens = key.get(sid, {}).get("ensemble_majority", "").strip().lower()
    if ens: pairs_e120.append((wr_label(key.get(sid, {}).get("sentence", "")), ens))
k_e120, n_e120 = kappa(pairs_e120)
print(f"wr-dict vs ensemble (on the 120 anchors) kappa = {k_e120:.3f} (n={n_e120})")

# ---- (b) 499-sentence ensemble sample ----
sheet = list(csv.DictReader(open(K/"passage_coding_sheet_ensemble.csv", encoding="utf-8-sig")))
pairs_499 = []
for r in sheet:
    ens = (r.get("ensemble_majority") or "").strip().lower()
    if not ens: continue
    pairs_499.append((wr_label(r.get("sentence", "")), ens))
print(f"\nensemble sample scored: {len(pairs_499)}")
out499, acc499 = prf(pairs_499, "wr dictionary vs LLM-ensemble majority (n=499)")
k_499, n_499 = kappa(pairs_499)
print(f"wr-dict vs ensemble kappa = {k_499:.3f} (n={n_499})")

json.dump({"n": len(pairs_499), "accuracy": acc499, "per_class": out499,
           "kappa_dict_vs_ensemble": round(k_499,3),
           "n_120_human_gold": n_h,
           "kappa_dict_vs_human_120": round(k_h,3),
           "kappa_dict_vs_ensemble_120": round(k_e120,3)},
          open(OUT/"wr_rescore_summary.json", "w"), indent=1, ensure_ascii=False)
# dump per-sentence labels for the archive
with open(OUT/"anchor_wr_labels.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["sample_id","wr_label","human_label","sentence"])
    for p, t, sid, sent in rows: w.writerow([sid, p, t, sent])
with open(OUT/"ensemble_wr_labels.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["sample_id","wr_label","ensemble_majority"])
    for r in sheet:
        ens = (r.get("ensemble_majority") or "").strip().lower()
        if ens: w.writerow([r["sample_id"], wr_label(r.get("sentence","")), ens])
print("\nsaved:", OUT)
