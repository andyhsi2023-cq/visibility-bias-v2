# 4. Substantive Applications

Section 3 established that the concrete VAI is a validated measure of the visible-versus-functional composition of Chinese municipal governance rhetoric. It was passage-validated against human coding (§3.2.0) and behaviorally anchored to real cosmetic investment under an exogenous incentive shock (§3.2.7). This section presents what the validated instrument *descriptively* reveals: a compositional-substitution association in accounting data (§4.1), a suggestive within-document pattern (§4.2), and an independent large-scale corroboration in public-procurement data (§4.3). Three exercises that a previous draft foregrounded are demoted and reported transparently (§4.4–§4.5). We make no causal claim about *what drives* visibility bias; the criterion-validity evidence (§3.2.7) supports the measure rather than a causal theory.

## 4.1 Application I: Compositional substitution in accounting data (P1)

Our pre-registered H1 holds that within-city variation in VAI positively predicts the accounting-based Cosmetic Investment Ratio (CIR) while leaving total infrastructure investment unchanged. We estimate

$$\text{CIR}_{it} = \beta\,\text{VAI}_{it} + \gamma' X_{it} + \mu_i + \tau_t + \epsilon_{it},$$

with city ($\mu_i$) and year ($\tau_t$) fixed effects, controls $X_{it}=\{\ln\text{GDPpc}, \ln\text{pop}, \text{ind2-share}\}$, and city-clustered SE; sample 2,751 city-years across 261 cities, 2005–2015 (MOHURD CIR coverage).

**Table 2. P1 — Compositional substitution (CIR ~ VAI)**

| Specification | β(VAI) | SE | p | N |
|---|---:|---:|---:|---:|
| (1) Primary VAI | **+0.113** | 0.037 | **0.002** | 2,751 |
| (2) Reconstructed lexicon (robustness) | +0.111 | 0.036 | 0.002 | 2,751 |
| (3) Independent lexicon | +0.111 | 0.043 | 0.011 | 2,751 |
| (4) No city FE | +0.089 | 0.042 | 0.035 | 2,751 |
| (5) No year FE | +0.184 | 0.055 | 0.001 | 2,751 |
| (6) IV = VAI(t−1) | +0.142 | 0.051 | 0.005 | 2,489 |

All specifications give β > 0 at conventional significance. The null on total investment (ln total urban-construction investment on VAI: β = −0.008, p = 0.71) is consistent with *composition, not expansion*. Horse races against GDP-growth, urbanization stage, and leader tenure leave β(VAI) essentially unchanged (Online Appendix C.2). A pre-registered 24-permutation specification curve gives median β = +0.107 with 24/24 positive and 22/24 significant (Online Appendix B.1). We read this as a descriptive compositional-substitution association, conditional on the instrument's validity, and stop short of a causal claim.

## 4.2 Application II: The within-document review-vs-plan differential (suggestive)

Exploiting the temporal structure of GWRs (a retrospective past-year review and a prospective next-year plan), we partition each report at the first plan marker after character 2000 and compute VAI on each section (N = 4,330 successful splits).

**Table 3. Within-document retrospective-vs-prospective VAI differential**

| Metric | Value |
|---|---:|
| Mean VAI(review) | 0.615 |
| Mean VAI(plan) | 0.591 |
| Mean Δ (review − plan) | **+0.0245** |
| Paired t | **8.40** |
| Two-tailed p | **6.2 × 10⁻¹⁷** |

The differential is positive and highly significant. It cannot arise from lexicon-selection (same lexicon), from author-style (the same author writes both sections), or from report-length (VAI is a ratio). We nonetheless report it as suggestive corroboration rather than a behavioral signature, since, as in R1, genre differences between retrospective and prospective sections could produce the same pattern (§4.2.1). With the criterion-validity test of §3.2.7 now carrying the behavioral argument, the within-document differential is a secondary, measurement-level fact about how reports are written.

### 4.2.1 What this does and does not tell us

The differential is compatible with the upward-signaling mechanism but is not a unique diagnostic. Downstream-facing rhetoric, lexical-availability bias, and selection on what gets completed-versus-planned would also predict it. Robustness to alternative split markers and to long-document/single-tenure subsamples is in Online Appendix C.3.

## 4.3 Application III: Independent corroboration in public-procurement data (new)

As an entirely separate, large-scale corroboration we classify the universe of Zhejiang public-procurement announcements (≈2,957,789 records, predominantly 2019–2026, national `ggzy.gov.cn` platform) by the same visible-versus-functional construction distinction. Visible-type projects outnumber functional ones by roughly 2-to-1 overall (2.1-to-1 among first-stage tender notices, the cleanest one-per-project proxy), and the tilt is pervasive rather than local: visible exceeds functional in 97 of 108 localities with sufficient volume (median city ratio 1.8; the exceptions are small county-level units; Online Appendix Figure ESM-6). Going beyond counts, we recover each project's investment amount from the tender briefs (16,794 award-stage projects, 2023–2024). Visible and functional projects are of broadly similar typical size (median ¥5.8M vs ¥4.7M), but the visible category owns the high-value tail. Its 99th percentile (¥0.90B vs ¥0.20B) and maximum (¥11.5B, the Hangzhou Metro Line 7 contract, vs ¥1.07B) are several times larger, because the biggest construction outlays (metro/rail, arterial roads, landmark parks) are visible-salient while concealed-utility works top out an order of magnitude lower. Visible construction thus predominates on both frequency and the high-value tail. The visible/functional classification was refined by LLM-assisted adjudication with domain-expert (urban- and rural-planning) sign-off (Authors' Contributions); the lexicon, re-pull and analysis code, per-city table, and amount distribution are deposited (`03-analysis/phase-L-bidding/`). One caveat is that a "project" is proxied by the deduplicated award record, so the count comparison (less so the amount comparison) is sensitive to how works are packaged; the accounting CIR (§4.1, §3.2.7) supplies the independent expenditure-share corroboration.

## 4.4 Structural welfare calibration (illustrative; demoted)

The cadre-attention model yields a closed-form welfare-loss expression. Calibrated with the observed compositional share, an assumed social optimum $a^{SO} \in [0.40, 0.50]$, and an aggregate renewal-expenditure base, it produces figures on the order of single-digit ¥ billions per year. We deliberately do not headline this number. It depends on strong assumptions that we have not independently validated: the Cobb-Douglas welfare function, the social-optimum benchmark, and the text-to-spending mapping. The derivation and sensitivity table are in Online Appendix A and C.7, and we attach no policy weight to the magnitude.

## 4.5 Demoted exercises: transparent reporting of failed/null tests

Two pre-registered tests are demoted from the main evidentiary structure (full detail in Appendix C.3 and Appendix D):

**Null 1, central-inspection event study (H2): definitively null.** A narrow-window TWFE specification gave the predicted sign (β(k=0) = −0.065, p = 0.011), but a heterogeneity-robust Sun–Abraham estimator attenuates it to insignificance and, extending to Rounds 6–9 (2016–2017), reverses the sign (β = +0.016). The narrow-window result is a staggered-treatment-heterogeneity artifact [14, 15, 16] rather than a causal inspection effect (deviations D-B-1/2/3).

**Null 2, individual-level CFPS micro-foundation (H5): bounded null.** Amenity-category-specific satisfaction items are absent from the public CFPS panel; substituted general outcomes show no effect above |d| = 0.011 (TOST rejects |d| ≥ 0.10 at p < 10⁻⁶). This bounds a citizen-popularity channel but does not test the pre-registered mechanism, and is reported as exploratory (deviation D-F-1).

## 4.6 Summary

The validated VAI tracks an external accounting measure of investment composition (P1, β = +0.111, with no effect on total investment). It co-moves with real cosmetic investment under an exogenous turnover shock while the naive measure does not (§3.2.7). In an entirely independent procurement corpus it is corroborated by a ≈2:1 visible-over-functional tilt across 97 of 108 localities and a visible-dominated spending tail (§4.3), and it shows a suggestive within-document differential (§4.2). The inspection event study, the CFPS micro-foundation, and the welfare calibration are demoted and reported transparently; they limit, rather than support, the causal and welfare claims the instrument can carry.
