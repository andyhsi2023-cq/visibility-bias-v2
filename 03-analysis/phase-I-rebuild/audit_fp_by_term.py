#!/usr/bin/env python3
"""audit_fp_by_term.py — per-term FP audit for the V_ORIG lexicon.

For each visible term, count over the 500-sentence Phase-G ensemble sample:
  • N_hit              sentences where the term occurs AND the dictionary fires visible/mixed
  • N_irrelevant       sentences where (term ∈ sentence) AND ensemble_majority == irrelevant
  • N_visible          sentences where (term ∈ sentence) AND ensemble_majority == visible
  • N_mixed/functional ... similarly
  • FP_rate            N_irrelevant / N_hit  (the headline diagnostic — "non-infrastructure rate")

Also computes the same against the 120-row human anchor (subset of the 500).

Outputs:
  phase-I-rebuild/per_term_fp_audit.csv         (one row per visible term)
  phase-I-rebuild/per_term_fp_audit.json        (machine-readable summary)

This drives the lexicon_visible_v2 decisions; no term gets dropped without numbers here.
"""
from __future__ import annotations
import csv, json
from collections import Counter, defaultdict
from pathlib import Path

PROJ = Path("/Users/andy/Desktop/Research/visibility-bias-v2")
ENSEMBLE = PROJ / "03-analysis/phase-G/passage_coding_sheet_ensemble.csv"
HUMAN = PROJ / "03-analysis/phase-G/anchor_human_labels.csv"
ANCHOR_KEY = PROJ / "03-analysis/phase-G/anchor_key.csv"
LEX_VIS = PROJ / "02-data/processed/lexicon_visible.txt"
OUT = PROJ / "03-analysis/phase-I-rebuild"
OUT.mkdir(parents=True, exist_ok=True)


def load_terms(p: Path) -> list[str]:
    return [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.startswith("#")]


def load_ensemble(p: Path) -> list[dict]:
    return list(csv.DictReader(open(p, encoding="utf-8-sig")))


def load_human(p_human: Path, p_key: Path) -> list[dict]:
    """Merge human anchor labels with the key (which carries the sentence + dict_label)."""
    key = {r["sample_id"]: r for r in csv.DictReader(open(p_key, encoding="utf-8-sig"))}
    out = []
    for r in csv.DictReader(open(p_human, encoding="utf-8-sig")):
        sid = r["sample_id"]
        if sid not in key:
            continue
        rec = dict(key[sid])
        rec["human_label"] = r["human_label"].strip()
        out.append(rec)
    return out


def per_term_stats(rows: list[dict], truth_col: str, terms: list[str]) -> dict:
    """For each term, scan all rows. Count occurrences and breakdown by truth label."""
    counts = {t: Counter() for t in terms}
    total = {t: 0 for t in terms}
    for r in rows:
        sent = r.get("sentence", "")
        truth = (r.get(truth_col) or "").strip().lower()
        if not truth:
            continue
        for t in terms:
            if t in sent:
                counts[t][truth] += 1
                total[t] += 1
    rows_out = []
    for t in terms:
        c = counts[t]
        n = total[t]
        if n == 0:
            rows_out.append({"term": t, "n_hits": 0, "fp_irrelevant": 0,
                             "fp_rate": None,
                             "by_label": {}, "verdict": "ZERO_HITS"})
            continue
        irr = c.get("irrelevant", 0)
        vis = c.get("visible", 0)
        mix = c.get("mixed", 0)
        fun = c.get("functional", 0)
        rows_out.append({
            "term": t,
            "n_hits": n,
            "fp_irrelevant": irr,
            "fp_rate": round(irr / n, 3),
            "by_label": {"visible": vis, "mixed": mix, "functional": fun, "irrelevant": irr},
        })
    return rows_out


def assign_verdict(stats_ensemble: list[dict], stats_human: list[dict]) -> list[dict]:
    """Combine the two evidence streams into a recommendation per term.

    Rule (conservative, evidence-driven):
      • DROP   : FP rate ≥ 0.60 in ensemble AND n_hits ≥ 5 (high enough to trust)
      • DROP-H : FP rate ≥ 0.50 in human anchor AND n_hits_human ≥ 3 (smaller threshold for the gold subset)
      • REVIEW : 0.30 ≤ FP < 0.60 OR insufficient evidence (n < 5 in ensemble, n < 3 in human)
      • KEEP   : FP < 0.30 in ensemble (and human doesn't disagree)
      • NO_HITS: 0 hits in the 500-row sample (cannot judge — keep for now)
    """
    h_lookup = {s["term"]: s for s in stats_human}
    merged = []
    for s in stats_ensemble:
        t = s["term"]
        h = h_lookup.get(t, {})
        n_e = s["n_hits"]
        fp_e = s["fp_rate"]
        n_h = h.get("n_hits", 0)
        fp_h = h.get("fp_rate")

        if n_e == 0 and n_h == 0:
            verdict = "NO_HITS_KEEP"
            note = "No evidence in 500-row sample; keep until larger sample available."
        elif fp_e is not None and fp_e >= 0.60 and n_e >= 5:
            verdict = "DROP"
            note = f"Ensemble FP={fp_e:.2f} over {n_e} hits — over fires on non-infrastructure."
        elif fp_h is not None and fp_h >= 0.50 and n_h >= 3:
            verdict = "DROP"
            note = f"Human anchor FP={fp_h:.2f} over {n_h} hits — confirmed FP problem."
        elif fp_e is not None and fp_e >= 0.30:
            verdict = "REVIEW"
            note = f"Ensemble FP={fp_e:.2f} over {n_e} hits; marginal — needs context constraint."
        elif n_e < 5 and n_h < 3:
            verdict = "REVIEW_LOW_N"
            note = f"Only {n_e} ensemble hits, {n_h} human hits — too few to judge."
        else:
            verdict = "KEEP"
            fp_e_str = f"{fp_e:.2f}" if fp_e is not None else "NA"
            note = f"Ensemble FP={fp_e_str} over {n_e} hits — clean."

        merged.append({
            "term": t,
            "n_hits_ensemble": n_e,
            "fp_rate_ensemble": fp_e,
            "ensemble_breakdown": s["by_label"],
            "n_hits_human": n_h,
            "fp_rate_human": fp_h,
            "human_breakdown": h.get("by_label", {}),
            "verdict": verdict,
            "note": note,
        })
    return merged


def main():
    terms = load_terms(LEX_VIS)
    print(f"[load] {len(terms)} visible terms")

    ens = load_ensemble(ENSEMBLE)
    print(f"[load] {len(ens)} ensemble rows ({ENSEMBLE.name})")

    hum = load_human(HUMAN, ANCHOR_KEY)
    print(f"[load] {len(hum)} human-anchor rows ({HUMAN.name} ⨝ {ANCHOR_KEY.name})")

    # ensemble: use ensemble_majority as truth, drop 'tie'
    ens_truthy = [r for r in ens if r.get("ensemble_majority", "").strip()
                  and r["ensemble_majority"].strip().lower() != "tie"]
    print(f"[scope] {len(ens_truthy)} ensemble rows with a non-tie majority")

    stats_e = per_term_stats(ens_truthy, "ensemble_majority", terms)
    stats_h = per_term_stats(hum, "human_label", terms)

    merged = assign_verdict(stats_e, stats_h)
    merged.sort(key=lambda x: (x["fp_rate_ensemble"] is None, -(x["fp_rate_ensemble"] or 0), -x["n_hits_ensemble"]))

    csv_out = OUT / "per_term_fp_audit.csv"
    with csv_out.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["term", "n_hits_ensemble", "fp_rate_ensemble",
                    "ens_visible", "ens_mixed", "ens_functional", "ens_irrelevant",
                    "n_hits_human", "fp_rate_human",
                    "hum_visible", "hum_mixed", "hum_functional", "hum_irrelevant",
                    "verdict", "note"])
        for m in merged:
            eb = m["ensemble_breakdown"] or {}
            hb = m["human_breakdown"] or {}
            w.writerow([
                m["term"], m["n_hits_ensemble"], m["fp_rate_ensemble"],
                eb.get("visible", 0), eb.get("mixed", 0), eb.get("functional", 0), eb.get("irrelevant", 0),
                m["n_hits_human"], m["fp_rate_human"],
                hb.get("visible", 0), hb.get("mixed", 0), hb.get("functional", 0), hb.get("irrelevant", 0),
                m["verdict"], m["note"],
            ])
    print(f"[write] {csv_out}")

    json_out = OUT / "per_term_fp_audit.json"
    json_out.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[write] {json_out}")

    print("\n--- TOP-15 by ensemble FP rate (min 5 hits) ---")
    print(f"{'term':<12} {'n_e':>5} {'fp_e':>6} {'n_h':>5} {'fp_h':>6}  verdict")
    for m in merged:
        if (m["n_hits_ensemble"] or 0) >= 5:
            fp_e = m["fp_rate_ensemble"]
            fp_h = m["fp_rate_human"]
            print(f"  {m['term']:<10} {m['n_hits_ensemble']:>5} "
                  f"{(f'{fp_e:.2f}' if fp_e is not None else '   --'):>6} "
                  f"{m['n_hits_human']:>5} "
                  f"{(f'{fp_h:.2f}' if fp_h is not None else '   --'):>6}  {m['verdict']}")

    print("\n--- Verdict tally ---")
    tally = Counter(m["verdict"] for m in merged)
    for v, n in tally.most_common():
        print(f"  {v:<15} {n}")


if __name__ == "__main__":
    main()
