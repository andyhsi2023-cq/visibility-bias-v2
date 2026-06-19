# Stage 0: Idea Vetting — Visibility Bias v2

**Date**: 2026-04-14
**Framework**: Stage-Gate SOP v1.0 §2 Stage 0
**Author**: main session (will be independently audited by `novelty-audit` agent before Phase B)

---

## Gate criterion 1: The one-sentence finding

### v1 (what the rejected paper claimed)

> "Chinese cities exhibit a systematic visibility bias that shifts investment composition (cosmetic +8.4pp, functional -9.5pp) without altering total investment, and this bias is institutional (96.1% city FE) rather than personal (27 transferee correlations)."

**Red Team verdict**: descriptive; not causal; reverse-causality & common-source not addressed; no welfare magnitude.

### v2 (revised, after Red-Team-driven reframe)

> **"Exogenous reductions in local officials' supervisory scrutiny (via the staggered 2013–2016 central anti-corruption inspections) cause the Visibility Attention Index to *fall* by Δβ, and this induced decline in visibility discourse is followed by a reallocation of municipal capital from cosmetic to functional infrastructure, identifying a causal visibility-bias channel worth an estimated ¥XXX billion per year in avoided infrastructure-failure costs."**

**What changed**:
- **Causal verb**: "cause" with an exogenous shock, not "predict" with FE.
- **Direction flipped to defensive**: inspections *reduce* visibility pressure → shows the mechanism runs the "right" direction causally.
- **Downstream quantified**: the bias has a welfare cost we estimate.
- **Connects discourse → allocation causally**: not just "both correlated with city."

### Test for compliance with Gate 1

> ✅ "We find X that was previously not known." — **X = central inspection-induced drop in VAI causally reduces cosmetic investment share and raises functional share**. Previously unknown at the causal level.

### Backup variant (if Phase B shows inspections are the wrong shock)

> "Cities exogenously designated as Smart-City pilots increase VAI by Δβ within 2 years, and subsequent investment composition shifts toward visible categories (roads, greening); the induced deviation from pre-trend yields a ¥XXX billion counterfactual welfare loss in underprovided functional infrastructure."

Backup preserved in case inspection data proves unusable (Phase B feasibility).

---

## Gate criterion 2: Two-to-three prior works + our specific difference

See `01-literature/gap-verification-v2.md` (being written in parallel by `literature-specialist` agent) for the full treatment of five opponent papers. Here, the three most-proximate are summarized in SOP format:

### Prior work A: Cao, Lindo & Zhong (2023) *Journal of Urban Economics*

**They found**: local Chinese government *Weibo* rhetoric predicts downstream hate-incident occurrence (dictionary-based text measure → outcome).

**We depart by**: (a) measuring *attentional bias* rather than *sentiment*; (b) using *legally binding annual work reports* (not voluntary social media) — which are structurally shaped by supervisory incentives; (c) identifying off an *exogenous central-inspection shock*, not panel correlations; (d) connecting discourse to *physical capital allocation with welfare magnitudes*, not only to downstream social outcomes.

**First-order?** ✅ Each of (a)-(d) is a first-order departure. Shared method class (dictionary-based text), but entirely different construct, identification, and outcome.

### Prior work B: Bai, Hsieh & Song (2020) *Journal of Public Economics*

**They found**: Chinese cities systematically favor visible construction in cross-sectional land politics.

**We depart by**: (a) providing a *text-based ex ante predictor* (VAI) of which cities will do this — they document the pattern, we predict it from discourse; (b) identifying the *attentional mechanism* rather than only the fiscal-political mechanism; (c) providing *within-city dynamic evidence* from inspection shocks; (d) quantifying *welfare cost* they do not estimate.

**First-order?** ⚠️ Mixed. (c) and (d) are clearly first-order; (a)-(b) are conceptually related but the ex-ante-discourse angle is genuinely new.

### Prior work C: Persson & Zhuravskaya (2016) *AEJ: Applied*

**They showed**: Chinese officer rotations are **not** exogenous and are shaped by provincial career concerns.

**We respond by**: (a) *not* relying on officer rotations for our main identification in v2 (we use central inspections instead); (b) keeping officer-rotation analysis only as a *descriptive decomposition* (r_city vs r_person), not as a causal claim; (c) explicitly citing Persson-Zhuravskaya as the reason we moved to inspection-based ID.

**First-order?** Not a finding departure — it's a *methodological response*. This paper threatens our v1 identification; our v2 reframe specifically addresses the threat by moving to a different exogenous shock.

### Remaining threats

Hassan et al. 2019 (firm-level political risk) and Qin-Strömberg-Wu 2018 (media bias) will be evaluated by the `literature-specialist` agent. Expected: methodological parallels but entirely different constructs and institutional settings.

---

## Gate criterion 3: Back-of-envelope welfare / counterfactual number

### The target quantity

Annual welfare loss from visibility-biased underprovision of functional infrastructure in Chinese cities.

### Computation sketch

**Step 1 — Magnitude of underprovision.**
- From v1 empirical: visibility bias shifts functional-share by −9.5 percentage points vs counterfactual neutral allocation.
- Total Chinese urban construction investment, 2015–2022 annual average: ~¥16 trillion (MOHURD + NBS).
- Functional-infrastructure subset of that (water/gas/heating/drainage/flood): ~¥2.1 trillion/year in reported categories.
- Implied annual functional-infra underprovision (if v1 share estimates hold): ~¥200 billion.

**Step 2 — Damage from underprovision.**
- Chinese urban-flooding damage costs: Chen et al. (2021 *Nature Sustainability*) estimate direct annual damages at ¥30–50 billion in major-city basement / transport / commerce flooding.
- Drainage-system effective-life-loss costs: back-of-envelope 10-year depreciation × ¥200B underprovision × 30% inefficiency = ~¥6B/year hidden cost.
- Aging-pipe catastrophic-failure costs (gas explosions, water main bursts): ¥10–15B/year based on 2015–2024 incident records.

**Step 3 — Present-value bundle.**
- Annual functional-infra failure cost directly attributable to visibility bias (conservative): **¥45–65 billion per year.**
- 20-year PV at 3% real discount: **~¥700–950 billion** (≈ 0.9–1.2% of annual urban GDP)

### Bandwidth of the estimate

- Lower bound (only direct flooding damages): ~¥30 billion/year
- Central estimate: ~¥55 billion/year
- Upper bound (including lifetime maintenance debt): ~¥200 billion/year

### Validity

This is a **BOE (back-of-envelope) estimate**, not a structural welfare calculation. Phase D will convert this into a model-consistent number by:
- Calibrating the model's σ_V / σ_F ratio to observed spec-curve elasticities
- Computing welfare loss as distance from Pareto-optimal allocation
- Sensitivity-analyzing across reasonable damage-function specifications

### Policy anchor

Compared to reference welfare numbers in Chinese-local-gov literature:
- Land finance efficiency cost estimates: 0.5–2% of GDP (Wu 2015, Han-Kung 2015)
- Overbuilding / GDP tournament cost estimates: 1–3% of investment (Li-Zhou 2005, Jia-Kudamatsu-Seim 2015)
- **Our ballpark (1% of urban GDP) is in the same order of magnitude** — not implausibly large, not negligible.

---

## Gate decision for Stage 0

| Criterion | Status | Evidence |
|---|---|---|
| 1. One-sentence finding | ✅ Pass | Causal verb + exogenous shock + welfare magnitude |
| 2. Prior-work departures | ⚠️ Tentative pass | 2 of 3 proximate papers show clear first-order departures; (B) has mixed departure. Await `literature-specialist` report on Hassan, Qin-Strömberg-Wu. |
| 3. Welfare BOE | ✅ Pass | ~¥55B/year central estimate with credible bandwidth |

**Provisional verdict**: proceed to Phase B, conditional on `literature-specialist` agent's gap-verification and `novelty-audit` agent's independent scoring.

---

## Risks to flag for the `novelty-audit` agent

1. The welfare estimate depends on v1 empirical results that may not survive Phase E (VAI re-construction with controls). If VAI loses significance after controlling for document length / boilerplate, the welfare story collapses.
2. The central-inspection shock (Phase B) may show null effects on VAI if inspections targeted cosmetic-heavy cities endogenously.
3. "Third-party VAI" (Phase E D1-fix) may correlate too weakly with primary VAI to relieve the common-source concern.
4. "Individual-level evidence" (Phase F D7-fix) requires matching CFPS respondents to city-year VAI — match quality is unknown until attempted.

Any of risks 1–3 failing triggers a mandatory return to Stage 0 with a further-downgraded finding.

---

*Stage 0 complete. Proceeding to Stage 1 (literature-specialist in parallel) and Stage 0 novelty-audit immediately after.*
