# JCSO-D-26-00240 — R1 Revision Handoff

**Date**: 2026-06-18 · **Decision**: Major Revisions (Reviewer #1) · **Due**: 2026-07-30
**Strategy**: Plan A — reframe to a *validated measurement instrument + descriptive evidence*; demote causal/welfare. (Plan B ruled out 2026-06-18: no defensible causal identification available — see `rejection-log.yaml` entry.)
**Authoritative artifact**: `05-manuscript/manuscript_compiled_R1.md` (recompiled from `sections/`; contiguous §1–§6 + appendices). Response: `06-submission/response-to-reviewers-R1-DRAFT.md`.

---

## What is done (autonomous pass)

| Reviewer comment | Status | Where |
|---|---|---|
| **C1** construct-validity ladder; "rhetoric" not "strategic bias" | ✅ reframed | abstract, §1, §2, §3.2 |
| **C2** institutional grounding of GWRs | ✅ new subsection | §3.1.0 (drafting/approval, target-responsibility evaluation, audiences) |
| **C3** passage-level human validation | ⚙️ **set up + piloted; needs human coding** | §3.2.0 + `03-analysis/phase-G/` |
| **C4** demote causal / CFPS / welfare | ✅ done | §4.3 welfare (no headline #), §4.4 nulls condensed, full detail in App A/C.7/D |
| **C5** positioning vs Grimmer; narrow; fix links | ✅ positioning + refs; ⚠️ links pending | §3.0 Table 0, §1.1, refs [2,18,19] |
| internal consistency | ✅ renumbered §3→§5 gap closed; deviation-log de-duped; cross-refs fixed | all sections |

---

## ⛔ THE GATING ITEM — visible-lexicon refinement (your decision; Plan A depends on it)

The Phase-G **automated pilot** (DeepSeek over the 500-sentence sample) found the visible lexicon has **low precision (~0.32)**: one term, **示范** ("demonstration/model"), drives ~70% of false positives (示范区/示范项目/改革示范 — non-infrastructure). As-is, the dictionary would **not** clear the pre-registered 0.75 precision bar under human coding either. Details + diagnostic: `03-analysis/phase-G/PILOT-FINDINGS.md`.

This is good news handled right (it *is* the false-positive analysis the reviewer asked for), but it is a real dependency:

1. **Refine the visible lexicon** — drop/disambiguate `示范` first; review 文明城市, 展示, 美丽, 形象. (Surgical, not wholesale — blanket pruning tanks recall.)
2. **Re-derive VAI** on the full corpus → **re-run all downstream**: descriptive stats, E-A/E-D correlations, the β=+0.111 P1 result, the spec curve. *(Every VAI number in the paper depends on the lexicon.)*
3. **Human double-code** the 500 sentences (`coding_manual.md`) → final precision/recall/κ → fill the 3 `[TODO]`s (abstract, §3.2.0, §4.1 + Table 1).

Toolchain is ready: edit `02-data/processed/lexicon_visible.txt` → re-run `passage_sample.py` → `annotate_pilot.py` (fast re-check) → human coding → `compute_validation.py`.

---

## Your remaining actions (in order)

1. **Decide + run the lexicon refinement above** (the gating item).
2. **Recruit a 2nd human coder** (~1 day) for the passage validation — longest human lead time, start now.
3. **Re-deposit + verify every reproducibility link resolves** — the reviewer said none worked. The three anchors, used in the text:
   - OSF `10.17605/OSF.IO/ZMJY5` (×11) — and **file the Phase-G amendment** `07-prereg/osf-amendment-phaseG.md`
   - Zenodo `10.5281/zenodo.19569979` (×6) — set reviewer token / make public on acceptance
   - GitHub `andyhsi2023-cq/visibility-bias-v2` (×2)
4. **Final EM upload** by **2026-07-30** — editable source only (Word/Tex, no PDF). Convert `manuscript_compiled_R1.md` → DOCX.

## Minor polish (low priority)
- Verify the 2 added ref DOIs (Grimmer & Stewart 2013 `mps028`; Osnabrügge–Ash–Morelli `pan.2021.37`) — marked `[verify]` in `08_references.md`.
- Add real citations for the two `[ref]` markers in §3.1.0 (China cadre-evaluation literature).
- Appendix ordering quirk: "Appendix D" (deviation log) precedes "Online Appendix" (A/B/C/E) — optional reshuffle.
- Recompile (`manuscript_compiled_R1.md`) after the lexicon re-run so numbers refresh.

## Artifact index
- Manuscript: `05-manuscript/sections/*.md` → `manuscript_compiled_R1.md`
- Response: `06-submission/response-to-reviewers-R1-DRAFT.md`
- Reviewer PDF: `06-submission/JCSO_review.pdf`
- Validation: `03-analysis/phase-G/` (sampler, manual, scorer, pilot, PILOT-FINDINGS, coding sheet)
- OSF amendment: `07-prereg/osf-amendment-phaseG.md`
- Plan-B feasibility + decision log: `_meta/rejection-log.yaml`
