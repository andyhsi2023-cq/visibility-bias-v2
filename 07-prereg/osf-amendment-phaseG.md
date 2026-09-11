# OSF Amendment to ZMJY5 — Phase G: Passage-Level Construct Validation

**Parent pre-registration**: OSF DOI 10.17605/OSF.IO/ZMJY5 (archived 2026-04-14)
**Amendment date**: 2026-06-18
**Reason**: Responding to JCSO-D-26-00240 Reviewer #1 (Comment 3), we add a direct passage-level human validation of the VAI dictionary. This amendment is filed **before** coding; the sample is drawn deterministically from a fixed seed so the draw is itself pre-committed.

## What we will do
Compare the VAI dictionary's sentence-level classification against independent human coding.

- **Frame**: all sentences in the 6,294-report GWR corpus (282 prefectures, 2002–2024).
- **Sample**: n = 500 sentences, stratified by dictionary hit-type × era (`passage_sample.py`, seed = 20260618). Quota: visible-only 150, functional-only 150, mixed(both) 50, none 150; split evenly early(<2013)/late(≥2013). (Strata populations recorded in `passage_sample_manifest.json`.)
- **Coding scheme**: each sentence labeled `visible` / `functional` / `mixed` / `irrelevant` per `coding_manual.md`.
- **Coders**: two independent human coders, blind to the dictionary label and to each other; disagreements adjudicated by a third pass.
- **Metrics** (`compute_validation.py`): full confusion matrix; per-class precision, recall, F1; false-positive/negative exemplars; an error taxonomy; intercoder agreement (Cohen's/Krippendorff's κ).

## Pre-set success criteria (committed before seeing results)
- Per-class precision **and** recall for `visible` and `functional` ≥ 0.75 → instrument well-validated; report.
- 0.50–0.75 → report honestly with error taxonomy; soften the measurement claims accordingly.
- < 0.50 on a core class → disclose as a dictionary limitation (cautionary measurement note).

## Note on the automated pilot
Prior to human coding we ran an LLM-as-annotator **pilot** (`annotate_pilot.py`) to estimate likely precision/recall and de-risk the validation. The pilot is **provisional and does not substitute** for the pre-registered human coding above; its only role is feasibility/triage. Pilot results are reported as such.

## Materials (in `03-analysis/phase-G/`)
`passage_sample.py` (sampler) · `passage_sample_manifest.json` (seed + strata) · `passage_coding_sheet.csv` (blind sheet) · `coding_manual.md` · `compute_validation.py` (scorer) · `annotate_pilot.py` (pilot).
