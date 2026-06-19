# Phase G — Passage-Level Construct Validation of VAI (minimal plan)

**Project**: Visibility Bias v2
**Trigger**: JCSO-D-26-00240 Reviewer #1, Comment 3 — the manuscript lacks an independent passage-level validation of the dictionary; reviewer wants a random sample coded visible/functional/mixed/irrelevant with **precision, recall, FP, FN, intercoder agreement, and ambiguous-case examples**.
**Role in revision**: this is the **only substantive new analysis** in the Plan-A revision. Everything else is restructuring. Plug into manuscript §3 as the headline validation table.
**Date**: 2026-06-18

---

## 1. Goal (one sentence)

Show that the VAI dictionary, applied at the sentence/passage level, actually classifies *visible* vs *functional* infrastructure language the way a human reader would — and report where it fails — so VAI's construct validity rests on direct evidence, not on dictionary-vs-dictionary reliability.

## 2. Unit, sampling, sample size

- **Unit**: sentence (primary) — the level at which the dictionary scores text. Optionally a paragraph-level robustness pass.
- **Frame**: all sentences in the 6,294-report GWR corpus (2002–2024, 282 cities).
- **Sample**: **n ≈ 500 sentences**, stratified to guarantee signal in every cell:
  - **By dictionary hit**: ~150 visible-term hits, ~150 functional-term hits, ~200 no-hit (to estimate false negatives — the no-hit stratum is where missed visible/functional content hides).
  - **Spread across** city tier (provincial-capital / ordinary prefecture) and era (≤2012 / ≥2013) so validity isn't an artifact of one regime.
  - n=500 gives ±~4–6pp 95% CIs on per-class precision/recall — adequate for a validation table; can extend to 800 if a class CI is too wide.
- **Sampling is scripted and seeded** (reproducible); the sampling script + seed go to OSF.

## 3. Coding scheme (4 mutually exclusive labels)

| Label | Definition | Example cues |
|---|---|---|
| **Visible** | Infrastructure salient to an external observer (superior/inspector/media/citizen) without specialist access | 道路, 绿化, 亮化, 广场, 立面, 市容, 景观 |
| **Functional** | Infrastructure whose quality is not externally legible without inspection/records | 排水, 供热, 燃气, 管网, 污水, 防洪, 管廊, 结构安全 |
| **Mixed** | Both in the same unit, or genuinely dual-purpose | "改造老旧小区道路与地下管网" |
| **Irrelevant** | Not about physical infrastructure (fiscal, personnel, slogans, social policy) | "加强党风廉政建设" |

- A **2–3 page coding manual** with ≥5 worked examples per label and decision rules for hard cases (e.g., 公园 vs 地下综合管廊; greening vs ecological-restoration). Manual → OSF.

## 4. Coders & procedure (the intercoder requirement)

Reviewer wants **intercoder agreement**, which needs ≥2 independent coders. Single-author constraint → two options:

- **Option A (preferred, cleanest)**: recruit **one second human coder** (an RA / grad student) for ~1 day of coding. Two humans code all 500 blind; disagreements adjudicated by a third pass or discussion; report Cohen's/Krippendorff's κ on the two-human labels. This is what reviewers expect and is unimpeachable.
- **Option B (fallback, must disclose)**: Andy + a **frozen LLM coder** as the second annotator, with **all human–LLM disagreements adjudicated by Andy**, and κ reported for the human–LLM pair *with explicit disclosure* that one annotator is an LLM. Acceptable in computational-social-science venues if transparent, but weaker than Option A for this particular reviewer (who is already wary of overclaiming). Use only if a human RA is infeasible before 2026-07-30.

> Recommendation: **Option A.** It's one day of one person's time and removes a line of attack.

## 5. Metrics to report (the table)

Treat **dictionary label = prediction**, **human consensus label = ground truth**:
- Full **4×4 confusion matrix**.
- **Precision, recall, F1 per class** (visible / functional / mixed / irrelevant).
- **False-positive and false-negative exemplars** (≥3 each for visible and functional) — verbatim sentences, as the reviewer explicitly asked.
- **Intercoder agreement** (κ) on the human(s).
- A short **error taxonomy** (e.g., metaphorical 道路, negated mentions, list-template boilerplate) — turns the validation into a methods contribution.

## 6. Pre-registration hygiene

- This is a **new analysis not in OSF zmjy5** → file an **OSF amendment / addendum** (allowed) BEFORE coding, stating sample size, strata, scheme, and metrics. Keeps the "transparent deviations" claim intact (and directly answers Comment 5's reproducibility point).
- Lock the coding manual + sampling seed in the amendment so the validation is itself preregistered.

## 7. Effort & sequence

| Step | Owner | Effort |
|---|---|---|
| Sampling script (stratified, seeded) | AI | 1–2 h |
| Coding manual + examples | AI draft → Andy approve | 2–3 h |
| OSF amendment filed | Andy | 0.5 h |
| Coding (2 coders × 500) | Andy + RA (Option A) | ~1 day each |
| Adjudication + metrics + table/figure | AI | 2–3 h |
| Write §3 validation subsection | AI draft → Andy | 2–3 h |

**Critical path** = recruiting/scheduling the second coder. Start that now given the 2026-07-30 deadline.

## 8. Success criterion (honest, pre-set)

- If per-class precision/recall for visible & functional are **≥ ~0.75**: VAI is well-validated; report and proceed.
- If **0.5–0.75**: report honestly, add the error taxonomy, and soften VAI's claims accordingly (still publishable as an honest measurement paper).
- If **< 0.5** for a core class: that is itself a finding about dictionary limits — disclose, and the paper becomes a cautionary measurement note. (Pre-committing this rule keeps us from post-hoc rationalizing.)

---

*Plan ends. This is the lone Stage-1 task in the revision; the rest is Stage-2 rewrite + Stage-3 link fixes.*
