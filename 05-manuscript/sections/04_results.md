# 4. Behavioral Criterion Validity

Passage precision (§3) establishes that the concrete measure classifies the right *sentences*. It does not establish that the measure captures *strategic attention* rather than genre, template, or ritual language — the central concern of Reviewer #1, and the reason a precise text measure can still be substantively empty. This section supplies the decisive test: does the text measure co-move with **real, accounting-based** behavior under a plausibly exogenous shift in career incentives? It does, and only the valid measure does. We then add a supplementary procurement-frequency check (§4.3) and report transparently the exercises that do *not* support causal or welfare claims (§4.4).

## 4.1 Identification: retirement-driven secretary turnover as an incentive shock

The arrival of a new municipal party secretary is an incentive shock: an incoming secretary with promotion ambitions has heightened reason to produce *observable* achievements within a short evaluation window. If the visibility construct is behaviorally real, a turnover should raise both real cosmetic investment and the (valid) text measure, and should do so *after* the turnover, not before.

Plain turnover may be endogenous — under-performing cities may receive new leadership. We therefore isolate **retirement-driven turnover** (secretary departure at or above the mandatory-retirement age threshold), which is driven by the official's age rather than by local infrastructure conditions and is thus plausibly exogenous to a city's cosmetic-investment demand. For each outcome $y_{it}$ we estimate two-way fixed-effects regressions on the merged 2002–2024 city panel,

$$y_{it} = \beta\,\text{Turnover}_{i,t-1} + \mu_i + \tau_t + \varepsilon_{it},$$

with city ($\mu_i$) and year ($\tau_t$) fixed effects and standard errors clustered by city. We report the one-year-lag effect (turnover last year → outcome this year), a **future-turnover lead** as a pre-trend/placebo test (which should be ≈ 0 under clean identification), and the retirement-exogenous lag. The three outcomes are: real cosmetic investment (CIR, the MOHURD accounting series), the **concrete/valid** text measure (`wr_visibility`), and the **naive** text measure (`vai_composite`). This analysis is an independent re-estimation; code and outputs are in `03-analysis/phase-J-criterion-validity/` (`verify_comovement_master.py` → `verify_results_master.csv`).

## 4.2 The co-movement result

**Table 2. Co-movement under secretary turnover (two-way FE, city-clustered SE)**

| Outcome | Turnover (t−1) | Future turnover (lead) | Retirement-exogenous (t−1) |
|---|---:|---:|---:|
| Real cosmetic investment (CIR) | **+0.025** (p < 0.001) | −0.009 (p = 0.26) ✓ clean | +0.024 (p = 0.04) |
| **Concrete / valid text** (`wr_visibility`) | **+0.0103** (p = 0.01) | +0.001 (p = 0.84) ✓ clean | +0.016 (p = 0.01) |
| **Naive text** (`vai_composite`) | +0.002 (p = 0.54) ✗ | +0.003 (p = 0.29) | +0.004 (p = 0.39) ✗ |

*n ≈ 3,082 (CIR), 5,005 (concrete), 5,011 (naive) city-years.*

The pattern (Figure 2) is exactly what behavioral validity requires and is the paper's central result:

1. **Real cosmetic investment rises** in the year after turnover (+0.025, p < 0.001), with a clean pre-trend (the future-turnover lead is negative and insignificant). The same holds under the retirement-exogenous shock (+0.024, p = 0.04). The construct is real in money, not only in words.
2. **The valid text measure rises in lockstep** (+0.010, p = 0.01; retirement-exogenous +0.016, p = 0.01), again with a clean lead. The concrete measure tracks real behavior under an exogenous incentive shift.
3. **The naive measure does not respond at all** (+0.002, p = 0.54; retirement-exogenous +0.004, p = 0.39). It is internally stable (§3.5, E-A r = 0.93) yet behaviorally inert.

A genre or template artifact would not co-move with real expenditure under an exogenous shock; a strategic-attention measure does. The contrast between the valid and naive measures is the crux: passage validation tells us *which* measure to trust, and the behavioral test confirms that the trusted measure — and only it — captures attention that moves resources. This is the decisive answer to the rhetoric-versus-strategy question. It also reframes what validity means for measures of this kind: **behavioral co-movement, not internal reliability or aggregate cross-source correlation, is the test that separates a valid measure from a stable-but-empty one.** (The behavioral test uses the concrete dictionary at its 0.50-precision construction — a conservative choice; classical measurement error attenuates toward zero, so the true co-movement is, if anything, stronger.)

## 4.3 Supplementary check: procurement frequency

As an independent behavioral angle we classify the universe of Zhejiang public-procurement announcements (**2,957,789 records**, predominantly 2019–2026, from the national `ggzy.gov.cn` platform) by the same visible-versus-functional construction distinction. **Visible-type projects outnumber functional ones by roughly 2-to-1 overall** (2.1-to-1 among first-stage tender notices, the cleanest one-per-project proxy), and the tilt is pervasive rather than local: visible exceeds functional in **97 of 108** Zhejiang localities with sufficient volume (median city ratio 1.8; the few exceptions are small county-level units; Online Appendix Figure ESM-6). This corroborates the compositional tilt in an entirely separate, large-scale data source. Going beyond counts, we recover each project's **investment amount** from the tender briefs themselves (16,794 award-stage projects, 2023–2024). Visible and functional projects are of **broadly similar typical size** (median ¥5.8M vs ¥4.7M), but the visible category owns the high-value tail: its 99th percentile (¥0.90B vs ¥0.20B) and maximum (¥11.5B — the Hangzhou Metro Line 7 contract — vs ¥1.07B) are several times larger, because the biggest construction outlays (metro/rail, arterial roads, landmark parks) are visible-salient while concealed-utility works top out an order of magnitude lower. Visible construction therefore predominates on both **frequency** (≈2:1 by count) and the **high-value tail** — not merely because visible projects are small and numerous. The visible/functional keyword classification was refined by LLM-assisted adjudication with **domain-expert (urban- and rural-planning) sign-off** (Authors' Contributions); the lexicon, re-pull and analysis code, per-city table, and amount distribution are deposited (`03-analysis/phase-L-bidding/`). One caveat remains: a "project" is proxied by the deduplicated award record, so the *count* comparison (less so the amount comparison) is sensitive to how works are packaged; the accounting-based CIR (§4.2) supplies the independent expenditure-share corroboration.

## 4.4 Demoted exercises: transparent reporting of failed / assumption-dependent tests

Three exercises an earlier draft treated as contributions are demoted to supporting material and reported transparently; none is part of the main evidentiary structure.

**Causal inspection event study — definitively null.** The pre-registered prediction that central anti-corruption inspections reduce visibility attention does not survive: a narrow-window TWFE estimate has the predicted sign (β = −0.065, p = 0.01) but a heterogeneity-robust Sun–Abraham estimator attenuates it to insignificance, and extending the sample to the 2016–2017 rounds **reverses the sign** (β = +0.016; all nine cohort effects positive). The narrow-window result is a staggered-treatment-heterogeneity artifact [14, 15, 16], not a causal effect (Appendix D, deviations D-B-1/2/3). Note that the retirement-turnover design of §4.2 serves a *different* purpose — measurement (criterion) validity, not a causal welfare magnitude — and is methodologically distinct from this failed design.

**Physical-stock external anchor — null.** We also tested whether the text measure tracks *physical* infrastructure stocks (greening rate, pipe-network density, and similar yearbook series) as an external anchor. These stocks carry essentially no within-city signal over the period (a flow-versus-stock mismatch: annual rhetoric and investment are flows, accumulated stocks are not), so the anchor fails at the within-city level and is not used; the accounting-based CIR (a flow) is the appropriate external series.

**Individual-level micro-foundation — bounded null.** Amenity-category-specific satisfaction items are absent from the public CFPS panel; substituted general outcomes (government evaluation, life satisfaction, self-rated health) show no effect above |d| = 0.011 (TOST rejects |d| ≥ 0.10). This bounds a citizen-popularity channel but does not test the upward-signaling mechanism; we report it as exploratory (Appendix D, D-F-1).

**Structural welfare calibration — assumption-dependent, no headline.** The §2 model yields a closed-form welfare-loss expression; calibrating it with the observed compositional share and an assumed social optimum produces single-digit ¥-billion figures. **We deliberately attach no headline number.** The estimate depends on the Cobb–Douglas form, the social-optimum benchmark, and the text-to-spending mapping — assumptions stronger than the evidence warrants. Full derivation and sensitivity are in Online Appendix A and C.7; we treat it only as an illustration of what the model implies.

## 4.5 Summary

The paper's evidentiary spine is the behavioral co-movement of §4.2: under an exogenous, retirement-driven incentive shock, real cosmetic investment and the *valid* concrete text measure rise together with clean pre-trends, while the *naive* measure does not move. Procurement frequency corroborates the compositional tilt in an independent source. Causal identification of *what drives* visibility bias (the inspection design) fails and is reported as such; the citizen-channel and welfare exercises are bounded or assumption-dependent and demoted. What the paper establishes is a *validated measure* of compositional attention whose validity is anchored in real behavior — not a causal or welfare result.
