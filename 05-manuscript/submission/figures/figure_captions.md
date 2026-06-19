# Figure Captions (JCSS Format)

JCSS format: caption begins with **Fig. N** (bold). No punctuation after the number. No period at the end of the caption.

---

## R2 MAIN-TEXT FIGURES (new; `04-figures/fig1_precision_ladder.*`, `fig2_comovement.*`)

**Fig. 1** Lexicon precision ladder. Visible-class precision against the human gold standard (n = 120) for the naive dictionary (0.10), a concrete salience-based lexicon (0.50), its targeted refinement (0.60), the same plus above-ground landmarks (0.64), and a three-model LLM ensemble (0.84). The shaded band marks the dictionary polysemy ceiling (~0.60–0.64) that curation cannot break; the LLM ensemble clears it. Recall is noted for the naive (0.43) and concrete (0.79) lexicons

**Fig. 2** Behavioral criterion validity: co-movement under quasi-exogenous, retirement-driven secretary turnover (two-way city + year fixed effects; city-clustered 95% CIs). The one-year-lag turnover effect (filled markers) is positive and significant for real cosmetic investment (CIR, +0.025) and the concrete/valid text measure (+0.010) but null for the naive text measure (+0.002, n.s.); the future-turnover placebo (hollow markers) is ~0 for all three (clean pre-trends)

---

*[EM-upload note: the four captions below — the former main Fig. 1–4 — depict analyses the R2 demotes (construct battery, Wikipedia null, inspection event study, welfare calibration); relabel them as ESM / Online-Resource figures, and keep the procurement figure (`fig_bidding_by_city`) as ESM-6.]*

**ESM (was Fig. 1)** Construct-validity battery (three panels). **a** Internal-replication test E-A: VAI computed from the original 80-term lexicon plotted against VAI computed from an independent 150-term expanded lexicon, across 5,686 city-year reports (Pearson r = 0.93). **b** Within-document behavioral signature E-B: paired histogram of the retrospective-vs-prospective VAI differential within each report (N = 4,330 reports with cleanly-separable past-year review and next-year plan sections; Δ = +0.025, paired t = 8.4, p < 10⁻¹⁶). **c** Random half-lexicon bootstrap stability test E-C: distribution of the Pearson r between VAI computed from a random 40-term half-lexicon and the full 80-term VAI, across 1,000 bootstrap iterations (mean r = 0.18, indicating that the full 80-term lexicon is the minimum stable measurement unit)

**Fig. 2** Third-party cross-source validation E-F (Wikipedia null). Scatter plot of governance-rhetoric VAI (computed from 6,294 government work reports) versus encyclopedic-description VAI (computed from Chinese Wikipedia city descriptions for 282 prefectures, restricted to N = 139 cities with at least 3 lexicon hits in the Wikipedia text). The Pearson r = −0.15 (95% CI [−0.31, +0.02]) is statistically null. The interpretation is that the instrument is valid within the governance-rhetoric domain but does not extrapolate to encyclopedic-description text — a scope finding rather than evidence of invalid measurement

**Fig. 3** P2 inspection event study (three specifications). **a** Two-way fixed-effects (TWFE) event study around CCDI Round-1–5 inspections (2013–2014 cohorts, narrow window 2010–2015), point estimate at k = 0 is β = −0.065 (significant). **b** Sun-Abraham heterogeneity-robust estimator on the same 5-cohort narrow window. **c** Sun-Abraham extended-window estimator using all 9 CCDI rounds (2013–2017 including 回头看 re-inspections), point estimate at k = 0 is β = +0.016 (not significant). The sign reversal between panels **a** and **c** is the key transparently-reported pre-registered null

**Fig. 4** Welfare calibration sensitivity. Per-yuan welfare loss across the parameter space {*a*ᴿᴼ ∈ [0.40, 0.50], utility form ∈ {log, CRRA(γ=2), back-of-envelope replacement-cost}}. The central estimate (log utility, *a*ᴿᴼ = 0.45) yields ¥4.4 billion per year of compositionally-misallocated urban infrastructure investment. The defensible range across log-utility specifications is ¥1–15 billion per year; the back-of-envelope shadow-pricing ceiling is ¥55 billion per year

---

# Online Resource 1 — Supplementary Figure Captions

(For figures appearing in the Online Appendix [Supplementary Information])

**Online Resource 1 Fig. S1** Phase B baseline TWFE event study. Point-estimate plot of VAI around CCDI Round-1–5 inspection events on the narrow 2010–2015 window. Pre-trend coefficients k = −3 to k = −1 are statistically null; post-treatment coefficient at k = 0 is β = −0.065 with 95% CI excluding zero

**Online Resource 1 Fig. S2** Random-assignment placebo distribution. Distribution of placebo-treatment effects from 500 iterations in which inspection cohorts are reshuffled at random across the 282-prefecture sample. The observed treatment effect (β = −0.065) falls inside the placebo distribution (5th–95th percentile range [−0.043, +0.076]), indicating that the narrow-window finding is underpowered with only two real cohorts

**Online Resource 1 Fig. S3** Pre-/post-era shift placebos. Two placebo specifications shift the treatment date by ±4 years and ±6 years from the actual 2013/2014 cohort years. The +4 and +6 shift placebos return statistically significant effects (β = +0.023, p = 0.0003 and β = −0.025, p = 0.001 respectively), flagging secular-trend contamination of the narrow-window TWFE specification

**Online Resource 1 Fig. S4** Phase B2 Sun-Abraham 5-cohort narrow-window estimator. Same 5-cohort (Rounds 1–5) sample as Fig. 3a, with the Sun-Abraham heterogeneity-robust estimator. Point estimate at k = 0 is closer to zero than the TWFE specification, foreshadowing the sign reversal in the extended-window specification (Fig. 3c)

**Online Resource 1 Fig. S5** Phase F CFPS individual-level null (coefficient forest). Coefficient estimates with 95% confidence intervals from 18 individual-level regressions in the China Family Panel Studies (2010–2022 biennial waves), regressing diverse satisfaction measures on city-level VAI. None of the 18 coefficients reach statistical significance; the largest absolute standardized effect is |d| = 0.011, providing a tight upper bound on the citizen-level satisfaction channel
