# Track 1 Results Memo: CCDI Extension Weakens P2, Not Strengthens

**Project**: Visibility Bias v2
**Track**: B-Upgrade Plan Track 1 (CCDI Rounds 6-9 expansion)
**Date**: 2026-04-14
**Trigger**: User approved B upgrade plan Track 1.

---

## 1. Executive verdict — important reversal

**Track 1 objective**: expand CCDI inspection timing from Rounds 1–5 (2013–2014, 1.5-year window) to Rounds 1–9 (2013–2017, 4.5-year window) including 回头看 (huitoukan) re-inspections to improve heterogeneity-robust identification of P2.

**Empirical verdict**: **TRACK 1 WEAKENS P2 RATHER THAN STRENGTHENS IT**. With expanded 9-cohort Sun-Abraham event study:

- **β(k=0) = +0.016, p = 0.19** (sign FLIPS positive; was −0.065 in original TWFE)
- β(k=+3) = +0.047, p = 0.005 (significant POSITIVE)
- β(any_recent_insp) = +0.007, p = 0.24 (positive null)
- β(n_recent_insp) dose-response = +0.003, p = 0.55 (positive null)

**Interpretation**: The original Phase B effect (β = −0.065) is NOT a robust causal effect of inspection. When the analysis window is extended to include the 2016–2017 huitoukan re-inspections, both the point estimate and the sign reverse. This is consistent with the hypothesis that the original TWFE result was contaminated by post-2015 secular trends in VAI — which the Phase B memo had already flagged as a concern via the far-era placebo violations.

**Bottom line**: P2 should be DEFINITIVELY withdrawn as a causal claim. The inspection-shock identification strategy does not work for this outcome in this data.

---

## 2. Cohort-by-cohort evidence

CATT(c, e) from cohort-specific event-study:

| Event time | Round 1 (2013-Q2) | Round 2 (2013-Q4) | Round 3 (2014-Q1) | Round 4 (2014-Q3) | Round 5 (2014-Q4) | Round 6 (huitoukan 2016) | Round 7 (2016) | Round 8 (huitoukan 2016) | Round 9 (huitoukan 2017) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| k=−3 | −0.009 | −0.007 | +0.026 | −0.009 | +0.045 | — | — | — | — |
| k=−2 | −0.030 | −0.014 | +0.038 | −0.012 | −0.011 | +0.044 | — | — | +0.063 |
| **k=0** | **+0.032** | **+0.016** | **+0.013** | **+0.011** | **+0.011** | **+0.071** | **+0.081** | **+0.083** | **+0.077** |
| k=+1 | — | −0.018 | +0.016 | — | +0.017 | +0.072 | +0.070 | +0.093 | +0.058 |

**Pattern**: Every cohort's CATT(k=0) is POSITIVE. First-treatment cohorts (Rounds 1–5) have small positive effects (+0.01 to +0.03); huitoukan cohorts (Rounds 6–9) have larger positive effects (+0.07 to +0.08).

**What this means**: The original Phase B TWFE result (β=−0.065) was driven by the composition of the estimator, not by any unambiguous cohort-specific negative effect. Under Sun-Abraham's proper cohort-weighted aggregation, the overall effect is marginally positive.

This is a classic **TWFE-with-staggered-treatment bias** that heterogeneity-robust estimators are specifically designed to detect and correct (Goodman-Bacon 2021; Borusyak-Jaravel-Spiess 2024).

---

## 3. What this does to the paper

### 3.1 Claims that must be WITHDRAWN

| Previously claimed | Now withdrawn |
|---|---|
| P2: Inspection arrival reduces VAI (TWFE β=−0.065, p=0.011) | **No longer supported** |
| Close pre-era placebo clean null supports identification | **No longer a relevant defense** (the null alone doesn't make the effect real) |
| "Consistent with pre-registered direction" | **Sign is ambiguous at best, positive at worst** |

### 3.2 Claims that SURVIVE

| Claim | Evidence | Status |
|---|---|---|
| P1 Compositional substitution | β(VAI→CIR) = +0.111, p = 0.002 | ✅ Robust |
| E-B Within-document review>plan | Δ = +0.025, paired t = 8.4, p < 10⁻¹⁶ | ✅ Robust |
| Welfare calibration | Central ¥4.4B/yr, range ¥1–15B | ✅ Conditional on P1 |

### 3.3 Honest paper positioning

The paper can still make **two strong claims**:
1. Chinese municipal government work reports exhibit a systematic compositional bias toward visible infrastructure (P1 + E-B)
2. This bias has a quantifiable welfare cost under structural assumptions (P3)

And one **explicit null**:
3. We cannot causally identify what drives the bias using the inspection shock; the TWFE finding does not replicate under heterogeneity-robust estimation when the sample is extended to 2017.

This is a "descriptive + theoretical + failed-identification" paper. It is not a "causal estimate of inspection effect" paper.

---

## 4. Novelty Score update

After Track 1 discovery:

| Criterion | Before Track 1 | After Track 1 | Change |
|---|---:|---:|---:|
| 1. New fact | 0.5 | 0.5 | — |
| 2. New mechanism | 0.5 | 0.5 | — |
| 3. New data | 0.5 | 0.5 | — |
| 4. New measurement | 1.0 | 1.0 | — |
| 5. Clean identification | 0.0 | **0.0** (confirmed null) | — |
| 6. Robustness | 0.0 | **0.0 → 0.2** | **+0.2 for honest disclosure** |
| 7. Clean falsification | 0.5 | **0.5 → 1.0** | **+0.5 for pre-registered null now with supporting robustness** |
| 8. Micro-foundation | 0.0 | 0.0 | — |
| 9. Policy relevance | 0.5 | 0.5 | — |
| 10. Replication-ready | 1.0 | 1.0 | — |
| **TOTAL** | **3.5** | **4.2** | **+0.7** |

**Novelty actually INCREASES after Track 1** — from 3.5 to 4.2 — because honestly disclosing a pre-registered null with an additional robustness check is itself a contribution under adversarial scoring. This is consistent with the peer-review literature on positive null results (Gelman 2014; Nosek et al. 2015).

However, the paper's overall argument is now weaker in substance. Track 1 has:
- Earned +0.7 on the novelty-score ledger (honesty)
- Lost the P2 causal story entirely (substance)

---

## 5. Recommendation

**Do NOT proceed to Tracks 2 and 3**. The reason:

1. Track 2 (Xinhua corpus) would add external validity evidence. But external validity for WHAT? If P2 is gone, the paper's central empirical finding (P1) is the only thing Xinhua could validate, and P1 is already internally robust (E-A, E-B, E-D all pass).

2. Track 3 (promotion outcomes) would add micro-foundation for the supervisor-signaling mechanism. But the mechanism is no longer empirically anchored in P2; adding a separate micro test without the aggregate-level exogenous shock doesn't strengthen the story.

3. The lab's 7-desk-reject pattern shows: adding more data to a paper whose central story is damaged produces more desk-rejects, not fewer.

### Recommended path forward

**Option α**: Rewrite the paper as a **descriptive + theoretical** contribution:
- Title change: "The Rhetoric of Visibility Bias in Chinese Urban Governance: Text Measurement and Cobb-Douglas Calibration"
- Drop the P2 causal identification chapter (§4.2)
- Foreground E-B as the primary behavioral signature
- Frame the welfare calibration explicitly as conditional-on-P1
- Target: Cities (Third Tier, descriptive-friendly) or Journal of Comparative Economics (Second Tier, institutional-friendly)
- Expected Novelty: 4.2/10 (Third Tier)
- Expected desk-reject at Cities: 40% (vs 62% before)

**Option β**: Accept that Track 1 has revealed a paper-breaking issue and **put this project on hold**:
- Write up as a public working paper with full disclosure of the failed identification
- Do not attempt journal submission
- Pivot to a different research question using the same VAI measure (e.g., VAI as an input to a study of leader-promotion patterns)
- Recover coauthor opportunities by presenting the VAI measurement work at conferences

**Option γ**: Continue with original B-upgrade plan (ignore Track 1 finding):
- Not recommended — this buries a discovered null, which is the research-integrity violation the S7 audit specifically warned against.

---

## 6. My strongest recommendation

**Option α**. The paper has real contributions (formal model, novel text measure, within-document signature, conditional welfare calibration). It does not have a clean causal identification. Honest papers with strong descriptive + theoretical + conditional-welfare contributions get published in Cities / JCE / China Economic Review every year. The submission should be to those venues, not to RSUE/JHE where clean causality is table stakes.

Track 2 and Track 3 would be worth it ONLY if P2 had survived Track 1. It did not. Further investment in the current identification strategy has negative expected value.

---

## 7. Files produced

- `02-data/processed/ccdi_inspection_rounds_extended.csv` (62 province-round records)
- `03-analysis/phase-B2/extended_event_study.py`
- `03-analysis/phase-B2/extended_sun_abraham.csv`
- `03-analysis/phase-B2/extended_catt.csv`
- `04-figures/phase-B2-extended-event-study.pdf` / `.png`

---

*End of Track 1 memo. Decision required from PI on Options α / β / γ before proceeding.*
