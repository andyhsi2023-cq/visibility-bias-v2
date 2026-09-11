# R2 Responsiveness Audit — JCSO-D-26-00240 (Reviewer #1)

**Date**: 2026-06-19 · **Against**: `05-manuscript/manuscript_compiled_R2.md` + `06-submission/response-to-reviewers-R1.md`
**Verdict in one line**: 5/5 major comments substantively addressed in the *text*; **two items still genuinely open, both requiring Andy (not text)** — the **human intercoder κ (C3)** and the **working reproducibility links (C5)**.

Legend: ✅ fully addressed in R2 · 🟡 addressed but with a residual gap · ⛔ not yet resolved (action required).

---

## C1 — Construct validity (distinguish the three claims; "rhetoric" unless stronger evidence)

**Reviewer's three-claim ladder**: (a) VAI measures visible/functional *language* [strongest]; (b) language reflects *attention* [weaker]; (c) attention reflects *strategic* response to observability/career incentives [insufficient]. Alternatives — actually built more, central campaigns, development needs, fiscal capacity, templates, genre — don't imply strategic bias.

**R2**: ✅ **Fully addressed — this is the strongest part of the revision.**
- §1 states the ladder explicitly and supplies the demanded *stronger evidence* for claim (c): the **behavioral co-movement** (§4). Under retirement-*exogenous* secretary turnover, real cosmetic investment (+0.025) and the valid concrete text measure (+0.0103, p=0.01) rise together with clean pre-trends, while the naive measure does not (+0.002, p=0.54).
- Why this answers the reviewer's specific alternatives: an *exogenous* incentive shock (a new secretary's career horizon) does not change a city's underlying development needs, central campaigns, or templates overnight — so co-movement of *money and text* under that shock isolates the incentive channel. "A genre/template artifact would not co-move with money under an exogenous shock" (§4.2).
- §2 defines "visible" by **salience to the evaluating audience** (not surface); §3.6 is explicit that "text alone identifies *what* is emphasized; the strategic interpretation rests on the behavioral evidence."
- **Caveat for us**: this claim is now load-bearing, so its data must be deposited and airtight (see C5 / R-3). It reproduces exactly (`verify_comovement_master.py`).

## C2 — Institutional premise (who drafts/reviews; cadre evaluation; "visible to whom")

**R2**: ✅ **Fully addressed.** §3.1.0 documents drafting (政府研究室 under the mayor), approval (municipal People's Congress vote), the link to cadre evaluation (目标责任制), the audiences (superior / NPC / public-media), and answers **"visible to whom" = the upward principal**, with the citizen channel reported as a bounded null. The only sub-question not *demonstrated* (vs documented) is whether citizens actually *use* the reports — honestly handled by reporting the citizen channel as a null rather than asserting it.

## C3 — Validation weaker than advertised; provide passage-level validation

| Reviewer sub-ask | R2 | Status |
|---|---|---|
| Alt-dictionary corr = *reliability*, not validity | §3.5 relabels E-A as "internal reliability, not validity" | ✅ |
| Review-vs-plan = genre, not diagnostic | §3.5 demotes E-B to "suggestive… may reflect genre" | ✅ |
| MOHURD = strongest external but modest | §3.5 "modest external check," r=0.24; behavioral is decisive | ✅ |
| Wikipedia = plainly failed; why preregistered? | §3.5 "failed external validation… a poorly-chosen source" | ✅ |
| **Passage-level validation**: random sample coded visible/functional/mixed/irrelevant; precision, recall, FP, FN, **intercoder agreement**, ambiguous cases | §3.3 + Online Appendix C.8: stratified sample, confusion matrix, per-class P/R, **示范 FP taxonomy**, polysemy-ceiling ambiguous cases | 🟡 |

**The residual gap (🟡 → ⛔):** every sub-item of the passage validation is delivered **except intercoder agreement**. The manuscript currently reports human↔ensemble κ = 0.66 and marks the *human* intercoder κ as "pending a second coder."

> **Finding (2026-06-19):** the two coding files in `~/Downloads` (`anchor_human_labels.csv` 06-18 22:39; `anchor_human_labels-2.csv` 06-19 08:10) **do not form a valid intercoder pair.** Both drew 120 sentences from the 500-pool but coded *different* subsets (only **26 shared IDs**), and on those 26 they agree just **6/26** (Cohen κ = **−0.032**, chance-level). The HTML coder evidently serves a different batch per session (coverage, not double-coding); `passage_coding_sheet.csv`'s coder1/coder2 columns are empty. So this does **not** discharge C3's intercoder ask. Coder-2 (08:10) is the gold behind the 0.50 precision; coder-1 (22:39) looks like a rough first pass (it calls clearly-visible 大道/公园 sentences irrelevant). I did **not** report κ=−0.03 — it would falsely say the construct is unreliable.
>
> **Fix prepared**: `03-analysis/phase-K/second_coder_sheet_LOCKED.csv` — the **same 120 gold sentences**, blank labels, dict/ensemble labels hidden. A second coder fills `human_label`, then `score_anchor.py coder2_labels.csv <filled>.csv` returns the real intercoder κ on the same sentences. **This is the one substantive thing standing between R2 and a clean C3.**

## C4 — Inspection event study / CFPS / welfare overextend

**R2**: ✅ **Fully addressed.** §4.4 demotes all three, transparently: inspection = "definitively null" (sign reverses under Sun–Abraham; staggered-treatment artifact); CFPS = bounded null (broad outcomes don't measure the mechanism); welfare = "assumption-dependent, **no headline number**." Full detail in Appendix D (deviation log D-B-1/2/3, D-F-1) and Online Appendix A/C.7. Matches the reviewer's "move to appendix or remove" exactly.

## C5 — Narrow the contribution; fix Table 0 positioning; **fix reproducibility links**

| Reviewer sub-ask | R2 | Status |
|---|---|---|
| Table 0 overstates novelty vs expressed-agendas/attention/cross-domain work | §3.0 Table 0 recast (compares on passage-validation + behavioral-validity, not "we're new"); §1/§3.0 position as "domain-specific application within the tradition," cite Grimmer [2], cross-domain [19] | ✅ |
| "Too many papers" → define VAI, institutional importance, validate via human coding + accounting, review-plan as suggestive; failed causal/CFPS/welfare to appendix | R2 is exactly this single measurement-validation identity; model→appendix; DiD/CFPS/welfare→§4.4/appendix; review-plan→suggestive | ✅ |
| **"None of the links provided actually work or are accessible"** — PAP, code, lexicons, data doc, deviation log must be reviewer-accessible | text still cites OSF `ZMJY5` / Zenodo `19569979` / GitHub; **resolving the links is a deposit action, not a text edit** | ⛔ |

**The residual gap:** the reviewer flagged broken links as a "serious reviewability problem," and it is **not fixed by the rewrite.** It requires Andy to (i) make the OSF Phase-G/J amendment public, (ii) set the Zenodo reviewer token / verify resolution, (iii) confirm the GitHub mirror is reachable, and (iv) **ensure the deposit actually contains** `master_2002_2024.csv` + `build_workreport_text.py` + `verify_comovement_master.py` (the behavioral pillar lives there) and the passage-validation toolchain. This is R-3.

---

## Bottom line

**Substantively, R2 responds to all five major comments** — and C1 (the make-or-break one) is answered with genuinely new, verified behavioral evidence, exactly the "stronger evidence" the reviewer demanded. **Two things are not yet done, neither fixable by writing:**

1. **⛔ Human intercoder κ (C3)** — the second coding on disk is unusable (different sample, chance-level agreement). Needs one clean double-coding of the locked 120-sentence sheet. *Highest priority — it is a specific, named reviewer ask and the gold's 0.50 precision rests on a single coder.*
2. **⛔ Working reproducibility links + complete deposit (C5)** — Andy deposit/verify action (R-3); the reviewer called broken links a "serious" problem.

Everything else (C1 behavioral evidence, C2 institutions, C3 passage validation, C4 demotions, C5 positioning/narrowing) is in the R2 text and traces to verified numbers.
