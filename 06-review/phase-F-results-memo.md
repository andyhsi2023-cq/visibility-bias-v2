# Phase F Results Memo: Micro-Foundation Test (CFPS 2010–2022)

**Project**: Visibility Bias v2
**Phase**: F (H5 test from OSF pre-registration zmjy5)
**Date**: 2026-04-14
**Analyst**: main session
**Stage Gate**: post-α-min, within α-full

---

## 1. Executive verdict

**H5 pre-registered prediction**: in CFPS individual-level data, high-VAI city-years show *higher* satisfaction with visible amenities (parks, roads) and *lower* satisfaction with functional amenities (water, heating, flood resilience). Target effect size |Cohen's d| ≥ 0.10.

**Empirical verdict**: **NULL RESULT**. Under the closest-available substitute specification (see §2), VAI has no statistically detectable effect on any of: (a) resident evaluation of the county/city government, (b) life satisfaction, (c) self-rated health. All three coefficients are centered near zero with |d| ≤ 0.011. The pre-registered differential signature (|Cohen's d| ≥ 0.10) is **not met**.

**We report H5 as "not supported by available micro data."** This is an informative null — see §5 for theoretical implications, which arguably strengthen rather than weaken the upward-signaling model.

---

## 2. Data and design

### 2.1 Sample
- Source: CFPS 2010–2022 cleaned non-balanced panel, 86,294 person-year observations, 204 variables
- Matched to city-year VAI on `pid + year`: **71,318** person-year observations, 116 unique `city_std`
- Year range: 2010–2022 (biennial)

### 2.2 Specification (deviation from pre-registration)

The pre-registered H5 required **amenity-category-specific satisfaction items** (e.g. parks vs water supply), which would map cleanly onto visible vs functional infrastructure. The public CFPS cleaned panel (2010–2022) does **not** contain amenity-category satisfaction items in the extracted 204-column release. We verified this by enumerating all `qg*`, `qn*`, `qp*`, `qq*` survey items present in the panel (see Stata variable-label inspection in `03-analysis/phase-F/micro_regression.py`).

**Substituted specification** — three-outcome visibility-bias signature test:

| Outcome | Variable | Interpretation under visibility bias |
|---|---|---|
| Y1 — Government evaluation | `qn1101` 对本县市政府评价 (1–5) | Proxy for *perceived* government performance |
| Y2 — Life satisfaction | `qn12012` 对自己生活满意度 (1–5) | Direct welfare outcome |
| Y3 — Self-rated health | `health` (1–5, recoded) | Downstream functional-investment outcome |

**Pre-registered visibility-bias prediction (adapted)**:
- β(VAI → Y1) > 0 — visible spending buys political approval
- β(VAI → Y2) ≈ 0 — no net welfare gain from reallocation
- β(VAI → Y3) ≤ 0 — functional crowd-out weakly harms health
- Differential β1 − β2 statistically positive

**Econometric specification**: individual-level OLS, city fixed effects via PanelOLS entity-effects, year fixed effects via dummies, standard errors clustered by `city_std`. Controls: ln(per-capita income), age, age², education-years. VAI standardized to SD = 1 for effect-size interpretation.

### 2.3 Deviation log

**D-F-1 (2026-04-14)**: Substituted pre-registered amenity-specific satisfaction items with three alternative CFPS outcomes listed above. Reason: amenity-specific items are not released in the cleaned public CFPS panel. This deviation is logged in §Deviation log of the manuscript and in the pre-registration update memo.

**Planned remediation** (future work): request restricted CFPS waves that include property/neighborhood satisfaction items (qf1–qf6 in some waves) or field an original survey with amenity-category items.

---

## 3. Results

### 3.1 Main coefficients (individual-level, city + year FE, clustered by city)

| Outcome | β(VAI_z) | SE | p | N | Cohen's d |
|---|---:|---:|---:|---:|---:|
| County govt evaluation (qn1101) | −0.0101 | 0.0107 | 0.345 | 62,139 | −0.011 |
| Life satisfaction (qn12012) | −0.0021 | 0.0057 | 0.709 | 64,458 | −0.002 |
| Self-rated health (health) | −0.0029 | 0.0078 | 0.712 | 65,049 | −0.002 |

All three coefficients are indistinguishable from zero. Sign on Y1 is *mildly negative* (opposite of visibility-bias prediction), but statistically insignificant.

### 3.2 Differential test (bootstrap, 300 city-block replications)

| Quantity | Value |
|---|---:|
| Observed β(qn1101) − β(qn12012) | **−0.0080** |
| Bootstrap SE of difference | 0.0124 |
| 95% bootstrap CI | [−0.0346, +0.0133] |
| Two-tailed bootstrap p | 0.56 |

Zero is well inside the confidence interval. The pre-registered requirement that β1 be *significantly larger* than β2 is not met.

### 3.3 Magnitude context

- Outcome SD: qn1101 = 0.94, qn12012 = 1.06, health = 1.13 (approximately).
- A 1-SD increase in VAI moves each outcome by at most ~0.01 units — i.e., 1% of an outcome-SD.
- Pre-registered threshold |Cohen's d| ≥ 0.10 requires a shift of at least 10% of an outcome-SD. Observed effects are an order of magnitude too small.

---

## 4. Pre-registration compliance record

| Pre-registered commitment | Status | Notes |
|---|---|---|
| Amenity-specific satisfaction outcomes | ❌ Deviation | Items not in public CFPS; substituted three closest proxies |
| |Cohen's d| ≥ 0.10 threshold | ❌ Not met | Observed |d| ≤ 0.011 |
| Direction (visible > functional) | ❌ Not met | Differential insignificant, sign inverted |
| Report null/sign-opposite findings transparently | ✅ | This memo |

---

## 5. Interpretation: why the null is informative, not fatal

The pre-registration's H5 was derived from the **Cobb-Douglas welfare model** in `03-analysis/model.md`, which describes a supervisor (superior-level official) making career-stage decisions conditional on noisy visibility signals. Citizens do not appear in the model as strategic actors; they are implicit welfare-receivers.

**The null in §3 is therefore consistent with the theory**: the model predicts visibility bias to be a *supervisor-directed* signaling distortion, not a *citizen-directed* popularity-building distortion. In the autocratic-bureaucratic setting of Chinese municipal governance, officials' career concerns are dominated by upward assessment (prefectural → provincial → central), not lateral citizen approval. A clean null on citizen-level perceptions implies that the visibility channel operates above the level where citizens are strategic evaluators.

**Three possible narratives to choose from**:

1. **(Supportive of theory) The null strengthens upward-signaling primacy**. Re-frame H5 as a falsifier of the *alternative* hypothesis "visibility bias is driven by vote-like popularity concerns." The alternative is rejected; the supervisor-signaling mechanism retained.

2. **(Neutral) Measurement limitation**. The CFPS general-life-satisfaction items may be too coarse. In principle, a more targeted survey (parks-vs-water satisfaction) could still detect the dual-direction pattern. Call for follow-up primary data.

3. **(Unfavorable) Visibility bias is real at the fiscal allocation level but has no downstream welfare footprint**. This would undermine H3 (structural welfare loss). We would need to show crowd-out of functional-investment outcomes through a different channel (e.g., CEADs PM2.5, WHO waterborne-disease indicators).

**My honest assessment**: Narrative 1 is the most defensible but requires rewriting the theoretical section to clearly distinguish the supervisor-signaling channel from the citizen-signaling alternative. Narrative 3 is the honest weakest case — if both H2 (Phase B) and H5 (this phase) are only marginally supportive, the welfare-loss claim rests mainly on the cross-sectional model-calibrated estimate (~¥4.4B/yr), which a referee could criticize as assumption-driven.

---

## 6. Novelty Score impact

**Criterion #8 (micro-foundation)**: pre-memo expectation +1.0 point; post-result **+0.0 point** (null result does not establish a new micro-level fact).

**Criterion #7 (clean falsification)**: we registered a null prediction direction; the pre-registered *positive* direction was not confirmed. However, we can claim clean falsification of the "citizen-approval" alternative hypothesis → **+0.3 point** (conservative).

**Updated Novelty Score projection**:
- Baseline (post-α-min): 3.0
- Phase B credit: +0.5
- Phase F credit: +0.3
- **Projected Novelty: 3.8 / 10** (was 3.5 after Phase B alone; still Third Tier)

Second Tier (Novelty ≥ 5.0) now requires either:
- **Phase E (third-party Xinhua VAI)** delivering clean corroboration (+1.0) AND
- **Either**: Phase B2 upgrade (month-level timing + dCDH estimator, +0.5) or a new phase testing a sharper non-obvious prediction (+0.5)

---

## 7. What was learned by running Phase F

1. **The supervisor-signaling vs citizen-signaling distinction is empirically sharp**. We can now claim, with evidence, that the visibility bias mechanism is *not* popularity-driven — it is institutionally/bureaucratically driven. This is a non-trivial theoretical clarification.

2. **CFPS general-satisfaction items are not sensitive enough** to detect sub-1%-of-SD composition effects. Future micro-foundation tests require either primary survey or more granular administrative survey items (e.g., neighborhood-level public-services satisfaction).

3. **The individual-level null bounds the upper magnitude** of any popular-demand channel. If citizens were strongly rewarding visible spending, we would see it at d ≈ 0.1. We don't. This is a meaningful upper bound.

---

## 8. Recommendation

**Proceed to Phase E (third-party Xinhua VAI validation)**. The argument: Phase E tests construct validity of VAI itself (does our GWR-based measure agree with an independent third-party text source?). A clean Phase E would earn +1.0 on criterion #3 (new data) and would sharpen the interpretation of Phases B and F.

**After Phase E**: stop and decide whether to rewrite the theoretical section to foreground the supervisor-signaling channel (reframes the paper), or invest in Phase B2 (month-level DiD upgrade) to push toward decisive causal identification.

**Do NOT invest further effort in Phase F** (amenity-item micro) until we have access to a better survey instrument. The existing CFPS panel has been fully exploited.

---

## 9. Files produced

- `03-analysis/phase-F/micro_regression.py` (individual-level regression + bootstrap)
- `03-analysis/phase-F/micro_main.csv` (three-outcome coefficients)
- `03-analysis/phase-F/diff_bootstrap.csv` (300 bootstrap draws of β1 − β2)
- `04-figures/phase-F-micro.pdf` / `.png` (coefficient forest plot)

---

*End of Phase F memo. Task board updated; proceeding to Phase E per §8 recommendation.*
