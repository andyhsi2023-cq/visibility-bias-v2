# Phase B Results Memo: Central Anti-Corruption Inspection Shock on VAI

**Project**: Visibility Bias v2
**Phase**: B (H2 test from OSF pre-registration zmjy5)
**Date**: 2026-04-14
**Analyst**: main session
**Stage Gate**: post-α-min, within α-full

---

## 1. Executive verdict

**H2 pre-registered prediction**: staggered central-inspection arrival causes VAI to decline at event time k ≥ 0, with |Δa| ≥ 0.02.

**Empirical verdict**: **PARTIAL SUPPORT**. The observed immediate effect at k=0 is negative (β between −0.04 and −0.07), consistent with the pre-registered direction, and the magnitude exceeds the 0.02 threshold. The observed coefficient is marginally statistically significant (p ∈ [0.01, 0.08] depending on specification detail). Pre-registered parallel-trends test passes jointly, but k=−2 shows an individual pre-trend violation (β=−0.073, p=0.019). The close pre-era placebo (fake treatment 2011/2012) returns a clean null (β=+0.001, p=0.98), which is the strongest single piece of supporting evidence. Far-era placebos (+4, +6 years) return significant coefficients, suggesting post-2015 VAI dynamics are partly driven by secular trends not specific to the inspection treatment.

**We report H2 as "consistent with model prediction but not decisively established."**

---

## 2. Data and design

### Sample
- VAI panel: 282 prefecture-level cities, 2002–2024 (from v1 project, reused).
- Inspection cohort assignment: compiled from publicly known Round 1–5 province-level treatment (2013–2015). See `02-data/processed/ccdi_inspection_rounds.csv`. Only 2 distinct treatment years survive after annual aggregation (2013 and 2014).
- Analysis window: 2009–2018, giving k ∈ [−4, +4] around each cohort.
- Post-match sample: 2,725 city-years in descriptive panel; 128 city-years in main regression (controls drop non-matched entries).

### Specification (deviation from pre-registration)

The pre-registration specified Callaway-Sant'Anna (2021) doubly-robust DiD. Because the inspection-cohort variation collapses to 2 treatment years (2013, 2014) and all 31 provinces are eventually treated by 2015, the full Callaway-Sant'Anna estimator with never-treated controls is not well-identified. We fall back to:

- **Specification**: two-way-fixed-effects event study with event-time indicators k ∈ [−4, +4] (k = −1 reference), city fixed effects only, controls (ln GDPpc, ln pop, secondary-industry share), city-clustered standard errors.
- **Year fixed effects dropped** because with only 2 cohorts they are collinear with event-time dummies.

**This deviation is logged here and will be documented in the manuscript's "Pre-registration and Deviations" section per our OSF §I commitment**. The pre-registered estimator was infeasible given the data structure; the TWFE approximation is a first-order diagnostic.

### Outcomes

Primary: VAI. CIR was planned but the overlap with MOHURD Yearbook (2005–2015) and the inspection window yields only n=89 for CIR, below the sample-size floor.

---

## 3. Results

### 3.1 Main event-study coefficients (Model 2, with controls, city FE only)

| k | β | SE | p | 95% CI |
|---|---:|---:|---:|---|
| −4 | −0.039 | 0.061 | 0.52 | [−0.160, 0.082] |
| −3 | −0.012 | 0.047 | 0.81 | [−0.105, 0.082] |
| **−2** | **−0.050** | 0.032 | **0.12** (but see alternate spec: p=0.019) | [−0.114, 0.013] |
| −1 | 0 | — | reference | — |
| **0** | **−0.065** | 0.025 | **0.011** | [−0.115, −0.016] |
| +1 | −0.031 | 0.047 | 0.51 | [−0.123, 0.062] |
| +2 | −0.061 | 0.037 | 0.10 | [−0.135, 0.012] |
| +3 | −0.058 | 0.054 | 0.28 | [−0.165, 0.048] |
| +4 | −0.078 | 0.061 | 0.20 | [−0.198, 0.042] |

### 3.2 Joint tests

- **Pre-trend test (H0: k ∈ [−4, −3, −2] all zero)**: F = 0.89, p = 0.447. **Pre-trends not jointly rejected.** ✅
- **Post-treatment joint test (H0: k ∈ [0, +4] all zero)**: F = 1.80, p = 0.119. Not jointly rejected — but all five point estimates are negative.
- **Post-treatment mean β**: −0.059 (consistent with pre-registered direction).

### 3.3 Placebo: close pre-era shift (most informative)

With fake treatment shifted to 2011/2012 (2 years before real inspections), re-running the same specification:
- **β(k=0) = +0.001, p = 0.98** — clean null.

This supports that the observed ~−0.065 effect is not simply a pre-existing VAI decline that would appear under any treatment-timing shift.

### 3.4 Placebo: far-era shifts

Shifting fake treatment by +4 yrs (2017/2018) or +6 yrs (2019/2020):
- +4 yr shift: β(k=0) = +0.023, p = 0.0003 (significant positive)
- +6 yr shift: β(k=0) = −0.025, p = 0.001 (significant negative)

Interpretation: post-2015 VAI has non-trivial secular dynamics unrelated to the inspection treatment. This is a concerning but honest finding — it means our design cannot cleanly separate the 2013–2015 inspection effect from broader post-Xi-Congress shifts in municipal discourse.

### 3.5 Random-assignment placebo (500 iterations)

Shuffling the 2013/2014 treatment-year assignment across the 31 provinces 500 times:
- Observed β(k=0) = −0.065 (from main) or −0.043 (from placebo-script replication)
- Placebo distribution: mean = −0.001, SD = 0.056, 5–95% range [−0.043, +0.076]
- Empirical two-tailed p: 1.00 (observed is not extreme vs placebo distribution)

Because treatment is binary between 2013 and 2014 (only 2 distinct values), random permutation has limited variation. This placebo is underpowered to falsify; its null result should not be over-weighted. The close pre-era placebo (§3.3) is a stronger falsification test.

---

## 4. Pre-registration compliance record

| Pre-registered commitment | Status | Notes |
|---|---|---|
| Sign of β(k=0) < 0 | ✅ Met (−0.043 to −0.065) | |
| |Δa| ≥ 0.02 | ✅ Met | All specifications exceed threshold |
| Callaway-Sant'Anna estimator | ❌ **Deviation** | Infeasible with 2 cohorts; TWFE approximation used |
| Parallel-trends diagnostic | ✅ Partial | Joint F passes (p=0.447); individual k=−2 borderline |
| Pre-specified null predictions | Not tested in this memo | Will be in Phase B2 extension |
| Report null/sign-opposite findings transparently | ✅ | See §3.4 far-placebo results |

### Deviation log

**D-B-1 (2026-04-14)**: Substituted Callaway-Sant'Anna doubly-robust DiD with TWFE event-study (city FE only, no year FE). Reason: only 2 treatment cohorts (2013, 2014) with all units eventually treated by Round 5 (2015); no never-treated control group. Planned remediation: Phase B2 will compile more-detailed sub-annual timing (using inspection month + round) and apply a proper heterogeneity-robust estimator (de Chaisemartin-D'Haultfœuille 2020) on the expanded timing variation.

---

## 5. Honest assessment against Novelty Score criterion #1 ("new fact")

The novelty-audit criterion reads: *"A finding not previously known."*

What Phase B establishes:
- An event-study coefficient of approximately −0.04 to −0.07 on VAI at the year of central-inspection arrival, in a first-cut TWFE approximation.
- A close pre-era placebo that is clean null, which argues *against* the effect being a generic post-2012 trend.
- Multiple placebo and pre-trend diagnostics that do NOT rule out secular-trend contamination.

What Phase B does NOT establish:
- A decisively significant causal effect under rigorous identification.
- Robustness to far-era placebos (which show their own significant coefficients).
- The full Callaway-Sant'Anna specification the pre-registration committed to.

**My honest self-assessment**: criterion #1 earns approximately **+0.5 point** (not the +1 I projected earlier). The result is consistent with the model but not independently compelling. A referee could reasonably demand Phase B2 (proper heterogeneity-robust DiD + more-granular timing) before giving full credit.

**Projected Novelty Score**: 3.0 + 0.5 = **3.5 / 10**. Still in Third Tier; Second Tier still requires Phase E (third-party VAI) and Phase F (CFPS micro).

---

## 6. What could strengthen Phase B

Ranked by feasibility:

1. **Use month-level inspection timing** (not just year) — expands cohorts from 2 to 5 (Round 1/2/3/4/5). Requires verifying exact start/end months for all 31 provinces against CCDI archives (2–3 hours).
2. **Apply de Chaisemartin-D'Haultfœuille (2020) estimator** — handles staggered treatment without "bad controls" bias from contaminated control group. Requires the `DIDmultiplegt` Python port (available).
3. **Instrument for inspection assignment** — use distance to Beijing, political-connection strength, or 2012 corruption prosecution density. Weak-instrument risk.
4. **Extend to "回头看" re-inspections (Round 8, 2016)** — introduces a new treatment that is plausibly exogenous conditional on pre-2016 trajectory. Adds genuine timing variation.
5. **Verify original data against Chen & Kung (2019 REStat) replication archive** — definitively resolve which provinces got Round 1 vs Round 2.

Any of items 1, 2, 4, 5 would strengthen criterion #1 from 0.5 toward 1.0. Items 2 and 4 together would be close to decisive.

---

## 7. Recommendation

**Proceed to Phase F (CFPS micro)** — data already available, faster turnaround, addresses a different novelty criterion (#8, micro-foundation). Phase B upgrade items listed in §6 are better revisited after the full Phase E+F results are in, because the marginal value of strengthening B depends on whether E and F both pass.

If E and F both pass (+2 net novelty points), Phase B as currently reported is sufficient — we would have Novelty 5.5/10 and target Second Tier (RSUE). If E or F fails, we should circle back to Phase B improvements because we need the evidence mass.

---

## 8. Files produced

- `03-analysis/phase-B/ccdi_inspection_rounds.csv` → `02-data/processed/`
- `03-analysis/phase-B/event_study.py` (v1; obsolete)
- `03-analysis/phase-B/event_study_v2.py` (preferred spec)
- `03-analysis/phase-B/event_study_vai.csv` (Model 2 coefficients)
- `03-analysis/phase-B/placebo.py` (random-assignment placebo)
- `03-analysis/phase-B/placebo_distribution.csv`
- `03-analysis/phase-B/placebo_preera.py` (pre/post-era shift placebo)
- `03-analysis/phase-B/placebo_preera.csv`
- `04-figures/phase-B-event-study.pdf` / `.png`
- `04-figures/phase-B-placebo.pdf` / `.png`
- `04-figures/phase-B-placebo-preera.pdf` / `.png`

---

*End of Phase B memo. Task board updated; proceeding to Phase F per §7 recommendation.*
