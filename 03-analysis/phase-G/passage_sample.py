#!/usr/bin/env python3
"""
phase-G/passage_sample.py — stratified sentence sampler for VAI passage-level validation.

Produces the to-be-human-coded sample requested by JCSO-D-26-00240 Reviewer #1, Comment 3
(precision/recall/intercoder against human labels). Design: see
`03-analysis/phase-G-passage-validation-plan.md`.

What it does:
  1. Streams the GWR corpus (one UTF-8 .txt per city-year), segments Chinese sentences.
  2. Applies the visible / functional lexicons to each sentence and assigns a *dictionary
     hit-type* stratum: visible-only / functional-only / both(mixed) / none.
  3. Reservoir-samples a fixed quota per (hit-type x era) stratum in a single streaming pass
     (no full corpus held in memory — respects the repo compute rules), with a fixed seed.
  4. Writes a blind coding sheet (coder1/coder2 columns empty) + a reproducible manifest.

Reproducibility: deterministic given (seed, corpus, lexicons). Seed + per-stratum counts are
written to the manifest and should be filed with the OSF amendment BEFORE coding begins.

Run:
    python3 passage_sample.py            # uses CONFIG below
    python3 passage_sample.py --dry-run  # report strata counts only, write nothing
"""
from __future__ import annotations
import argparse, csv, json, os, random, re, sys
from pathlib import Path

# ----------------------------------------------------------------------------- CONFIG
PROJ = Path("/Users/andy/Desktop/Research/visibility-bias-v2")
CONFIG = {
    # Corpus: directory of GWR .txt files. Filenames must encode city + year; adjust
    # FILENAME_RE if your convention differs (default matches e.g. "重庆_2014.txt"
    # or "500100_2014.txt"). The corpus lives on P1 per data-catalog; set the real path.
    "corpus_dir": "/Volumes/P1/城市研究/工作报告汇总/extracted/zf工作报告汇总/地级市工作报告2002-2024年",
    "filename_re": r"^(?P<city>.+?)(?P<year>(?:19|20)\d{2})$",   # e.g. 七台河市2003.txt
    # Lexicons: one term per line, UTF-8. Point these at the v1 replication lexicon files
    # (Online Appendix A.1). If missing, the script aborts (no silent fallback).
    "visible_lexicon": str(PROJ / "02-data/processed/lexicon_visible.txt"),
    "functional_lexicon": str(PROJ / "02-data/processed/lexicon_functional.txt"),
    "out_dir": str(PROJ / "03-analysis/phase-G"),
    "seed": 20260618,                       # pass via OSF amendment; do NOT change post-hoc
    "era_cut": 2013,                        # early = year < era_cut ; late = year >= era_cut
    "min_sentence_chars": 8,                # drop boilerplate fragments shorter than this
    # Quota per dictionary hit-type, split evenly across the two eras. Total = 500.
    "quota": {"visible": 150, "functional": 150, "mixed": 50, "none": 150},
}

SENT_SPLIT = re.compile(r"[。！？；!?;]+")
HAN = re.compile(r"[一-鿿]")
LABELS = "visible | functional | mixed | irrelevant"   # the human coding scheme


def load_lexicon(path: str) -> set[str]:
    p = Path(path)
    if not p.exists():
        sys.exit(f"[FATAL] lexicon not found: {path}\n"
                 f"        Point CONFIG at the v1 replication lexicon (Online Appendix A.1), "
                 f"one term per line.")
    terms = {ln.strip() for ln in p.read_text(encoding="utf-8").splitlines()
             if ln.strip() and not ln.startswith("#")}
    return terms


def iter_documents(corpus_dir: str, fn_re: str):
    """Yield (city, year, text) for each corpus file. Streaming — one file at a time."""
    rx = re.compile(fn_re)
    root = Path(corpus_dir)
    if not root.exists():
        sys.exit(f"[FATAL] corpus_dir not found: {corpus_dir}")
    for fp in sorted(root.rglob("*.txt")):
        m = rx.search(fp.stem)
        if not m:
            continue
        try:
            year = int(m.group("year"))
        except (ValueError, IndexError):
            continue
        city = m.group("city").strip()
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        yield city, year, text


def hit_type(sentence: str, vis: set[str], fun: set[str]) -> tuple[str, int, int]:
    v = sum(sentence.count(t) for t in vis)
    f = sum(sentence.count(t) for t in fun)
    if v and not f:
        return "visible", v, f
    if f and not v:
        return "functional", v, f
    if v and f:
        return "mixed", v, f
    return "none", v, f


def dict_predicted_label(ht: str) -> str:
    return {"visible": "visible", "functional": "functional",
            "mixed": "mixed", "none": "irrelevant"}[ht]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="report strata counts, write nothing")
    args = ap.parse_args()

    rng = random.Random(CONFIG["seed"])
    vis = load_lexicon(CONFIG["visible_lexicon"])
    fun = load_lexicon(CONFIG["functional_lexicon"])
    print(f"[lexicon] {len(vis)} visible terms, {len(fun)} functional terms")

    # per-stratum reservoir: key = (hit_type, era) ; era in {'early','late'}
    quota = CONFIG["quota"]
    per_era = {ht: q // 2 for ht, q in quota.items()}          # half to each era
    reservoir: dict[tuple, list] = {}
    seen: dict[tuple, int] = {}
    for ht in quota:
        for era in ("early", "late"):
            reservoir[(ht, era)] = []
            seen[(ht, era)] = 0

    n_docs = n_sents = 0
    for city, year, text in iter_documents(CONFIG["corpus_dir"], CONFIG["filename_re"]):
        n_docs += 1
        era = "early" if year < CONFIG["era_cut"] else "late"
        for raw in SENT_SPLIT.split(text):
            s = raw.strip()
            if len(s) < CONFIG["min_sentence_chars"] or not HAN.search(s):
                continue
            n_sents += 1
            ht, v, f = hit_type(s, vis, fun)
            key = (ht, era)
            cap = per_era[ht]
            seen[key] += 1
            res = reservoir[key]
            rec = {"city": city, "year": year, "stratum": f"{ht}:{era}",
                   "sentence": s, "dict_visible_hits": v, "dict_functional_hits": f,
                   "dict_label": dict_predicted_label(ht)}
            if len(res) < cap:                       # reservoir sampling (Algorithm R)
                res.append(rec)
            else:
                j = rng.randint(0, seen[key] - 1)
                if j < cap:
                    res[j] = rec

    print(f"[scan] {n_docs} documents, {n_sents:,} sentences")
    print("[strata] sampled / target  (population seen):")
    sample = []
    for ht in quota:
        for era in ("early", "late"):
            key = (ht, era)
            got, tgt, pop = len(reservoir[key]), per_era[ht], seen[key]
            flag = "" if got >= tgt else "  <-- UNDERFILLED (population too small)"
            print(f"   {ht:10} {era:5}: {got:3}/{tgt:<3} ({pop:,}){flag}")
            sample.extend(reservoir[key])

    if args.dry_run:
        print("[dry-run] no files written.")
        return

    rng.shuffle(sample)                              # randomize coding order (blind to stratum)
    out = Path(CONFIG["out_dir"]); out.mkdir(parents=True, exist_ok=True)
    sheet = out / "passage_coding_sheet.csv"
    with sheet.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["sample_id", "city", "year", "stratum", "sentence",
                    "dict_visible_hits", "dict_functional_hits", "dict_label",
                    f"coder1 ({LABELS})", f"coder2 ({LABELS})", "adjudicated", "notes"])
        for i, r in enumerate(sample, 1):
            w.writerow([f"S{i:04d}", r["city"], r["year"], r["stratum"], r["sentence"],
                        r["dict_visible_hits"], r["dict_functional_hits"], r["dict_label"],
                        "", "", "", ""])
    manifest = out / "passage_sample_manifest.json"
    manifest.write_text(json.dumps({
        "seed": CONFIG["seed"], "era_cut": CONFIG["era_cut"], "quota": quota,
        "n_documents": n_docs, "n_sentences": n_sents,
        "n_visible_terms": len(vis), "n_functional_terms": len(fun),
        "sampled": len(sample),
        "strata_population": {f"{k[0]}:{k[1]}": seen[k] for k in seen},
        "coding_scheme": LABELS,
        "note": "File this manifest with the OSF amendment BEFORE coding begins.",
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[write] {sheet}  ({len(sample)} rows)")
    print(f"[write] {manifest}")
    print("Next: file OSF amendment with this manifest, then two coders fill coder1/coder2 blind.")


if __name__ == "__main__":
    main()
