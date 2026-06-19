# Phase B Feasibility Assessment: Exogenous Shocks to Cadre Attention

**Project**: Visibility Bias v2 — α-full
**Stage**: Phase B planning (blocked on OSF DOI per SOP; plan is pre-DOI; execution is post-DOI)
**Date**: 2026-04-14

---

## 1. Purpose

Model Proposition 2 (see `model.md`) predicts that exogenous reductions in career-concern intensity $\kappa = (1-\lambda)/\lambda$ cause the visible share $a^*$ to decline. Phase B seeks a credible exogenous shock to $\lambda$ and tests P2 empirically.

This document evaluates candidate shocks for (a) **timing exogeneity**, (b) **data availability**, (c) **sample coverage**, (d) **power**. It recommends a primary + backup design and defers execution to post-DOI Phase B proper.

---

## 2. Candidate shock inventory

| # | Shock | Variation | Years | Exogeneity | Existing data? |
|---|---|---|---|---|---|
| 1 | Central inspection rounds (巡视组 staggered) | Province-round × year | 2013–2017 | High (conditional on pre-inspection covariates) | **No** — need to compile from `中央纪委监察部网站` press releases |
| 2 | First "Tiger" in province (Xi-era onset of prosecution intensity) | Province × year | 2012–2014 | Moderate (province salience endogenous to pre-Xi rent levels) | Yes (Harvard Corruption Dataset) |
| 3 | Prosecution intensity (# corruption cases per city-year) | City × year, continuous | 2004–2016 | Low (prosecutions endogenous) | Yes (Harvard, 16,169 cases, 295 cities) |
| 4 | 2013 Cadre Evaluation Reform (Organization Dept Notice) | National one-shot | 2013 | High but no cross-section | Treatment date only |
| 5 | 2014 New-Type Urbanization Plan | National one-shot | 2014 | Moderate | Treatment date only |
| 6 | Smart-City pilot designations | City × year | 2012–2016 | Low (cities lobbied for designation) | Yes (MOHURD) |
| 7 | 2015 New Budget Law (land-finance cap) | National one-shot | 2015 | High but no cross-section | Treatment date only |

---

## 3. Detailed evaluation

### 3.1 Shock 1 — Central inspection rounds (preferred)

**Design**:
- Each central inspection team enters a province on a known date; reports and announcements are public.
- 8 rounds of inspections 2013–2017 cover all 31 provincial-level units + some central SOEs.
- Identification: provinces are ordered roughly by political priority but **within-round assignment of 10 provinces** per round has a quasi-random component.

**Why preferred**: This is the identification strategy used by Chen & Kung (2019 *REStat*), Li & Zhou (2019 *China Q*), and Campbell & Liu (2019 *AJPS*). It is the **accepted exogeneity benchmark** for this literature.

**Data gap**: The inspection-round data must be hand-compiled from CCDI (中央纪委监察部) press releases or acquired from Chen-Kung's replication archive. Estimated effort: 3–4 hours.

**Power**: 282 cities × 15 years × known round dates → sufficient for Callaway-Sant'Anna (2021) staggered DiD with event-time bins.

**Pre-registered endpoint** (H2): event-time $\theta_k$ on VAI < 0 for $k \in [0, 3]$, magnitude ≥ 0.02.

### 3.2 Shock 2 — First "Tiger" in province (backup)

**Design**: Define treatment as the year province $p$ sees its first tiger-rank corruption prosecution post-2012. Use Harvard data.

**From data inspection** (`03-analysis/phase-B-shock-feasibility.md` source data):
- 31 provinces; 16 first-tiger in 2012, 13 in 2013, 2 in 2014
- Variation window: 3 years only

**Why backup, not primary**: 
- Limited time variation (all 31 within 3 years)
- "First tiger" timing is correlated with pre-Xi rent extraction (endogenous)
- Useful as a *robustness check* on Shock 1, not as primary identification.

**Power**: Adequate for provincial-level tests; weak at city level.

### 3.3 Shock 3 — Prosecution intensity (NOT recommended)

**Design**: Treat # city-year prosecutions as treatment.

**Why not**: Prosecutions are endogenous to the very behavior we study (high-visibility cities may attract more prosecutions because of asset-stripping opportunities). Regressing VAI on prosecution intensity is a regression of one outcome on another, not a causal identification.

**Possible use**: as a *control variable* in Shock 1/2 designs, or as a descriptive heterogeneity check.

### 3.4 Shocks 4–5, 7 — National one-shot reforms

**Why limited**: No cross-section, no placebo cities. An interrupted-time-series design is possible but weak. Can be used for *supplementary* evidence but not primary identification.

### 3.5 Shock 6 — Smart-City pilot designation

**Why low preferences**: Treatment assignment is substantially endogenous (cities applied and were selected). Bai-Hsieh-Song (2020) note this explicitly. Can be used as a *heterogeneity* dimension but not as causal shock.

---

## 4. Recommended identification package

**Primary (H2 test)**: Shock 1 — Central inspection rounds, staggered DiD (Callaway-Sant'Anna) with province × round as treatment unit.

**Robustness / triangulation**:
- Shock 2 (first tiger) — provincial-level event study
- Shock 4 (2013 cadre reform) — interrupted time series on national VAI mean

**Not used for causal claim**:
- Shock 3 — prosecution intensity (used only as control)
- Shock 6 — Smart-City — used only for heterogeneity tests

---

## 5. Pre-execution checklist (gated on OSF DOI)

Before running any Phase B regressions:

1. ✅ Model derived (Proposition 2 specifies sign + magnitude prediction)
2. ✅ Dataset inventory completed (this document)
3. ✅ Pre-registration drafted (`07-prereg/osf-preregistration-v1.md`)
4. ⏳ **OSF DOI issued** (user action — currently pending; hard blocker per `novelty-audit-S0-round2`)
5. ⏳ Central inspection dataset compiled (3–4 hrs AI-doable once DOI exists)
6. ⏳ Power analysis on simulated data (1 hr AI-doable)
7. ⏳ Parallel-trends pre-checks (1 hr AI-doable)

Total AI time to complete Phase B data prep + full event study: **~1 working day** once DOI exists.

---

## 6. Expected contribution to Novelty Score

If Phase B delivers the pre-registered P2 sign + magnitude and passes parallel-trends checks:

| Criterion | Before B | After B | Comment |
|---|---|---|---|
| #1 New fact (causal inspection→VAI→CIR) | 0 | **+1** | Novel within-province causal finding |
| #5 Structural welfare (already 1) | 1 | 1 | Unchanged (but the welfare *interpretation* strengthens) |
| Other criteria | — | — | — |

Projected post-B Novelty Score: **3.5 → 4.5/10** (with OSF DOI in place: 5.0/10).

**Second Tier (RSUE / CER) becomes feasible at 5/10**. Third Tier (Cities / IJUS / CEL) is already feasible at 3.5/10.

---

## 7. Deviation clause

If the inspection data reveal (a) parallel-trend violations, (b) small treatment-effect magnitude below the pre-registered threshold (|Δa| < 0.02), or (c) sign contradictions with P2:

- Report the null/sign-opposite result in the manuscript
- Treat this as **evidence against** the model, not as a fatal flaw of the project
- Robustness: try Shock 2 and Shock 4 as complementary designs

**The pre-reg's §I "deviations clause" protects us**: transparent reporting of null/contrary findings is a feature of good pre-registered empirical work, not a bug.

---

## 8. Next actions

**USER ACTION (CRITICAL)**:
1. Create OSF account + submit pre-reg → obtain DOI (20–30 min)
2. Record DOI in `07-prereg/osf-doi.txt`

**AI ACTIONS (post-DOI)**:
3. Compile central inspection dataset from CCDI press releases (3–4 hrs)
4. Power analysis + parallel-trend checks (1 hr)
5. Execute event-study per pre-reg specifications (2–3 hrs)
6. Write Phase B results memo

Total calendar time from OSF submission to Phase B complete: **~1 working day** (AI) + **20 min** (user) = ~1 day.

---

*End of Phase B feasibility document. Execution is held at this step until user provides OSF DOI.*
