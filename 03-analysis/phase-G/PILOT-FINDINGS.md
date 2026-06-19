# Phase G — Automated Pilot Findings (DE-RISK; provisional)

**Date**: 2026-06-18 · **Run**: `annotate_pilot.py` (DeepSeek as a stand-in second coder over the 500-sentence sample) → `compute_validation.py`.
**Status**: PROVISIONAL (silver standard). Now **confirmed by a 3-model ensemble** (Fleiss κ = 0.77) — see "Ensemble confirmation" below. Still not the pre-registered human gold; exact numbers will move under human coding, but the **qualitative finding is robust across independent model families**.

## Headline: the visible lexicon has a precision problem

Dictionary label vs LLM coder, n = 500:

| class | precision | recall | f1 |
|---|---:|---:|---:|
| visible | **0.32** | 0.73 | 0.44 |
| functional | 0.55 | 0.74 | 0.63 |
| mixed | 0.66 | 0.52 | 0.58 |
| irrelevant | 0.85 | 0.49 | 0.63 |
overall accuracy = 0.58

**Read**: the *visible* dictionary over-fires. Of 150 sentences the dict calls visible, the LLM judges 86 to be **not about physical infrastructure at all**. Recall is fine (0.73) — the dict isn't missing visible content; it's producing false positives.

## Ensemble confirmation (3 model families — robust)

Re-run with a **3-family ensemble** (Gemini 3.1 Pro + ChatGPT 5.5 + DeepSeek; `annotate_ensemble.py`). Inter-model **Fleiss κ = 0.77** (substantial agreement). Dictionary vs the 3-model majority (n = 470 with a majority):

| class | precision | recall |
|---|---:|---:|
| visible | **0.37** | 0.88 |
| functional | 0.56 | 0.83 |
| mixed | 0.79 | 0.59 |
| irrelevant | 0.89 | 0.50 |

The visible-precision problem **replicates across three independent model families** (overall accuracy 0.63), and `示范` is again the dominant driver — **61 of 84** visible→irrelevant false positives. Coverage: Gemini & DeepSeek 500/500, ChatGPT 375/500 (its proxy dropped ~125 batches; the majority is anchored by the two full raters). This is a *silver* standard: it does not replace the human-coded subset, but it shows the finding is not a single-model artifact.

## Cause: one term dominates

False-positive drivers (dict=visible but LLM=irrelevant):

| term | FP count |
|---|---:|
| **示范** (demonstration/model) | **60** |
| 文明城市 | 7 |
| 展示 | 6 |
| 美丽 | 5 |
| 形象 | 4 |
| (others ≤2 each) | — |

`示范` is pervasive in GWRs in non-infrastructure senses (示范区, 示范项目, 改革示范, 示范带动). It alone accounts for ~70% of the visible false positives.

## Fix is surgical, not wholesale

Pruning 13 polysemous terms blindly: visible precision 0.32 → 0.585 but **recall 0.73 → 0.47** (over-corrects — terms like 风貌/面貌/门面 are often legitimately visible). So the fix is to disambiguate/drop a **small** set led by `示范` (and context-gate 文明城市/美丽/展示), not to gut the lexicon.

## Implication for Plan A (needs Andy's decision)

Plan A (reframe to a *validated measurement instrument*) is **viable but now has a hard dependency**: the dictionary must actually pass passage-level validation, and as-is the visible lexicon would not clear the pre-registered 0.75 precision bar. This is exactly the false-positive issue Reviewer #1 (Comment 3) asked us to surface — handled well, it *strengthens* the paper (validate → find FPs → refine → re-validate).

**Recommended sequence (Andy to approve — it changes the instrument and every downstream VAI number):**
1. Refine the visible lexicon: drop/disambiguate `示范` first; review 文明城市, 展示, 美丽, 形象 with context rules.
2. Re-derive VAI on the full corpus with the refined lexicon; **re-run all downstream** (descriptive stats, E-A/E-D correlations, the β=+0.111 P1 application, spec curve).
3. Human double-code the 500-sentence sample (`coding_manual.md`) for the **final** precision/recall/κ that go into §3.2.0 / Table 1.

Toolchain is ready: refine `02-data/processed/lexicon_visible.txt`, re-run `passage_sample.py` (new seed or same), `annotate_pilot.py` for a fast re-check, then human coding + `compute_validation.py`.

*Files: `passage_coding_sheet_pilot.csv`, `passage_coding_sheet_pilot.validation.json`.*
