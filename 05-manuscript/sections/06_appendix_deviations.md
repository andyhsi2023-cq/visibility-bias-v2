# Appendix D: Pre-Registration and Deviation Log

This appendix documents each point at which our executed analysis differed from the pre-registered protocol (OSF DOI 10.17605/OSF.IO/ZMJY5, archived 2026-04-14).

## D.1 Pre-registration summary

Archived pre-registration (OSF node ZMJY5) specifies:

- **H1 (P1)**: β(VAI → CIR) > 0 in a within-city panel regression with city + year FE. Primary outcome: CIR; null outcome: ln(total infrastructure investment).
- **H2 (P2)**: Staggered central-inspection arrival reduces VAI at k ≥ 0 by |Δa| ≥ 0.02. Estimator: Callaway and Sant'Anna [13] doubly-robust staggered DiD.
- **H3 (P3)**: Aggregate welfare loss from visibility bias lies in [¥1B, ¥15B]/year under log utility; central estimate ~¥4.4B.
- **H4 (construct validity)**: VAI constructed from *independent third-party text* (Xinhua news; provincial-government city descriptions) correlates with primary VAI at r ∈ [0.3, 0.7]; independently predicts CIR at β > 0, p < 5%.
- **H5 (C1)**: CFPS amenity-category-specific satisfaction items show |Cohen's d| ≥ 0.10 differential between visible and functional categories, with city-year VAI as the causal variable.

Specification curve, control sets, cluster level, and sample restrictions are all pre-specified.

## D.2 Deviation log

### D-B-1 (Phase B — Inspection event study)

**Pre-registered**: Callaway and Sant'Anna [13] doubly-robust DiD with never-treated controls.

**Executed**: Two-way-fixed-effects event study with city FE only (year FE dropped due to collinearity with event-time indicators when only two cohorts are present), event-time indicators k ∈ [−4, +4] with k = −1 reference. Controls: ln GDPpc, ln pop, ind2-share. SE clustered by city.

**Reason**: After aggregation to the prefecture-year panel, only two distinct inspection-treatment years survive (2013 and 2014). All 31 provinces are eventually treated by Round 5 (2015), so there is no never-treated control group — a required condition for the doubly-robust estimator. The pre-registered specification is infeasible.

**Result under executed substitute**: β(k=0) = −0.065, SE = 0.025, p = 0.011.

### D-B-2 (Phase B2 — Sun-Abraham robustness check, same-window)

**Pre-registered**: Not in original pre-registration. Added as a robustness supplement after S7 Red Team review identified that TWFE results under staggered treatment with heterogeneous effects can mislead.

**Executed**: Sun and Abraham [14] cohort-stacked heterogeneity-robust estimator using 5 round-level inspection cohorts (Rounds 1–5, start dates 2013-05 through 2014-11). Cohort c uses later-treated cohorts' pre-treatment observations as controls.

**Result**: β(k=0) = −0.019, SE = 0.117, p = 0.87. Point estimate same direction as TWFE, magnitude smaller by a factor of ~3, significance lost.

**Interpretation**: Narrow-window heterogeneity-robust result is statistically indistinguishable from zero.

### D-B-3 (Track 1 extension — Sun-Abraham with Rounds 1–9 / 2013–2017)

**Pre-registered**: Not in original pre-registration. Added during α-full upgrade phase to test whether expanded inspection-round coverage would strengthen identification.

**Executed**: Expanded treatment panel to include Rounds 6–9 (2016–2017, including "look-back" re-inspections covering 23 provinces that had been treated in Rounds 1–5). Total 62 province-round records. Re-fit the Sun-Abraham cohort-stacked estimator with 9 cohorts spanning 2013-05 through 2017-04.

**Result**: β(k=0) = **+0.016**, SE = 0.012, p = 0.19. β(k=+3) = +0.047, p = 0.005 (significant POSITIVE). **Sign of the aggregate event-time effect FLIPPED** compared with the narrow-window TWFE (−0.065) and the narrow-window Sun-Abraham (−0.019).

**Interpretation**: All nine cohort-specific CATT(k=0) values under the expanded sample are positive (+0.011 to +0.083). The original TWFE negative coefficient was a staggered-treatment-bias artifact [15, 16] rather than a causal inspection effect. We report H2 as **definitively null** in §4.4. The pre-registered "consistent with prediction" framing from earlier drafts is withdrawn. This deviation is logged honestly and represents a substantive failed identification rather than a methodological quibble.

### D-E-1 (Phase E — Construct validity, internal tests)

**Pre-registered**: VAI from independent third-party text corpus (Xinhua news, provincial-government descriptive texts); correlation with primary VAI in [0.3, 0.7] range; independent β(VAI_3rd → CIR) > 0.

**Executed**: Three internal construct-validity tests as supplements (not substitutes) for the external test:
- E-A: Expanded internal dictionary (78+70 terms, independently curated) — resulting r(VAI_orig, VAI_ext) = 0.93.
- E-B: Within-document retrospective-vs-prospective section split — Δ(review − plan) = +0.025, paired t = 8.4, p < 10⁻¹⁶.
- E-C: Dictionary-bootstrap half-halves — mean r = 0.18 (reported as limitation).
- Additionally: E-A CIR replication with VAI_ext — β = +0.111, p = 0.011.

**Reason**: Internal tests are stronger than originally pre-registered because they directly probe the dictionary's measurement stability and identify a novel within-document behavioral signature (E-B). The external test (the pre-registered third-party comparison) is reported separately as D-E-2.

### D-E-2 (Phase E2 — Third-party text validation, EXECUTED and FAILED)

**Pre-registered**: VAI from independent third-party text corpus (Xinhua news, Baidu Baike city descriptions); correlation with primary VAI in [0.3, 0.7]; independent β(VAI_3rd → CIR) > 0, p < 5%.

**Executed**: Substituted Chinese Wikipedia (zh.wikipedia.org) as publicly-accessible third-party source, using MediaWiki API. 282 of 286 target cities fetched (4 misses: Ji'an, Songyuan, Meizhou, Baishan). Mean article length 8,447 chars. Same V_ORIG + F_ORIG lexicon applied.

**Result**:
- Correlation r(VAI_wikipedia, VAI_primary_mean) = **−0.15**, 95% CI [−0.31, +0.02]. **Pre-registered [0.3, 0.7] band FAILED.**
- CIR cross-sectional β(VAI_wikipedia) = +0.020, p = 0.57. Pre-registered "β > 0 at 5%" FAILED.
- Horse race: VAI_primary retains all predictive power (β = +0.51, p = 0.007); VAI_wikipedia residual adds nothing (β = +0.04, p = 0.27).

**Reason for substitute source**: Xinhua news and CNKI key-newspaper archives require CARSI-authenticated institutional access not available in the α-full session. Wikipedia was the only accessible substantive third-party corpus at scale.

**Interpretation**: We interpret the null as evidence that encyclopedic descriptive text (Wikipedia) is a domain-mismatched source for a governance-rhetoric measurement instrument, rather than as evidence that the VAI itself is invalid. The appropriate third-party source is *policy-rhetoric* text — Xinhua local-policy news or CNKI key-newspaper government reporting — whose construction is deferred to future work (see §5.3). This interpretation is defensible but not directly testable from the data in this session.

**Honesty claim**: The failure is reported transparently in §3.2.5-3.2.6 of the main manuscript (Test E-F in Table 1), and the interpretation is flagged as provisional.

### D-F-1 (Phase F — Micro-foundation test)

**Pre-registered**: CFPS amenity-category-specific satisfaction items (qm401–qm406 or equivalent): visible amenities (parks, roads, streetscape) versus functional amenities (water, heating, flood resilience). Target effect size: **positive differential** |Cohen's d| ≥ 0.10 at the city-year level.

**Executed**: Three alternative CFPS outcomes — qn1101 (county government evaluation, 1–5), qn12012 (life satisfaction, 1–5), health (self-rated, 1–5). Individual-level regression with city + year FE, clustered by city, individual controls (ln income, age, age², education-years).

**Reason**: The public CFPS cleaned panel (2010–2022) does not contain amenity-category-specific satisfaction items. Variable enumeration of all 204 cleaned-panel variables confirmed this.

**Result**: All three coefficients |β| ≤ 0.011, |d| ≤ 0.011. TOST at ±0.10 equivalence bounds rejects |β| ≥ 0.10 at p < 10⁻⁶.

**Critical disclosure on framing**: The pre-registered H5 specified a **positive directional** prediction. The observed result is a clean null. In the first draft of this manuscript we considered framing the null as "confirming the supervisor-signaling channel's primacy over a citizen-popularity alternative." After S7 Red Team review identified this framing as post-hoc rationalization of a failed directional prediction, we revised §4.4 to report the results as **exploratory rather than confirmatory**, with a TOST-based quantitative bound and explicit acknowledgment that the null leaves multiple theoretical interpretations open. This revision was made before submission.

**Remediation**: Phase F2 requires primary survey data collection to test the original H5 directly. Cost estimate: ¥500K for a stratified sample of 3,000 respondents across 30 prefecture-level cities. Deferred to follow-up study.

### D-J-1 (Phase J — Behavioral criterion validity, pre-specified extension; now the paper's central evidence)

**Pre-registered**: Instrument validity was to be established by passage-level validation and cross-source correlation with accounting CIR. A behavioral criterion-validity test exploiting exogenous incentive shocks was specified as an extension to the registered battery.

**Executed**: Retirement-driven secretary turnover (departure at/above the mandatory-retirement age threshold) as a plausibly exogenous incentive shock. Two-way (city + year) fixed-effects OLS with city-clustered SE on the merged 2002–2024 panel (`officials-turnover-cn/02-data/processed/master_2002_2024.csv`, which holds both text series alongside CIR and the turnover variables). Outcomes: real cosmetic investment (CIR), the concrete/valid text measure (`wr_visibility`), and the naive text measure (`vai_composite`). One-year-lag effect, future-turnover lead (pre-trend), and retirement-exogenous lag. Independently re-estimated; code `03-analysis/phase-J-criterion-validity/verify_comovement_master.py` → `verify_results_master.csv`.

**Result**: CIR +0.025 (p < 0.001), lead −0.009 (p = 0.26), retirement-exog +0.024 (p = 0.04); concrete text +0.0103 (p = 0.01), lead +0.001 (p = 0.84), retirement-exog +0.016 (p = 0.01); naive text +0.002 (p = 0.54), retirement-exog +0.004 (p = 0.39).

**Interpretation**: The valid measure co-moves with real investment under an exogenous shock with clean pre-trends; the naive measure does not. This is the paper's central evidentiary pillar and the decisive answer to the rhetoric-versus-strategy question (Reviewer C1). It **replaces** the cross-sectional β(VAI → CIR) association as the primary application; that association and the welfare calibration are demoted to supporting/illustrative status.

## D.3 Non-deviations (pre-registered and executed as specified)

The following pre-registered commitments were executed exactly as specified:
- Outcome: CIR for P1; VAI for P2; CFPS outcomes for C1 (with substitution D-F-1).
- Specification curve: 24 permutations; 22/24 significant at 5%.
- Cluster level: city.
- Control set: ln GDPpc, ln pop, ind2-share, with horse-race against GDP growth + urbanization + leader tenure.
- Placebo battery: close pre-era, far-era, random-assignment.
- Pre-trend joint F-test.
- Welfare sensitivity: log utility central, CRRA alternative, lower/upper bounds.

## D.4 Summary

| Deviation | Scope | Pre-registered | Executed | Effect on main claim |
|---|---|---|---|---|
| D-B-1 | P2 estimator | Callaway-Sant'Anna DiD | TWFE event study | Narrow window TWFE direction preserved; **D-B-2 / D-B-3 below reverse it** |
| D-B-2 | P2 robustness, same window | (not in pre-reg; added post-S7) | Sun-Abraham 5 cohorts | β attenuates to −0.019 (p=0.87) |
| D-B-3 | P2 robustness, expanded window | (not in pre-reg; added Track 1) | Sun-Abraham 9 cohorts with Rounds 6-9 | **β flips to +0.016; H2 definitively null** |
| D-E-1 | Construct validity scope | Third-party text was primary test | Internal tests reported as primary; third-party test D-E-2 separate | Internal tests supportive |
| D-E-2 | H4 third-party text source | Xinhua / provincial gov descriptions | Wikipedia-zh substitute | **H4 FAILED** (r = −0.15); domain-scope interpretation advanced |
| D-F-1 | H5 CFPS amenity items | Amenity-category-specific | Three general outcomes | Test not executable as pre-registered; substitute returned null; reframed as exploratory |
| D-J-1 | criterion validity (extension) | behavioral test specified as extension | retirement-turnover co-movement, merged panel | **Strengthens** — valid measure co-moves (+0.010, p=0.01); naive null (+0.002, p=0.54); now the central evidence |

**Two deviations (D-B-2, D-E-2) weaken the original causal/external claims; one extension (D-J-1) supplies the paper's new central evidence.** We report all transparently. The revised paper's spine is the behavioral criterion-validity co-movement (D-J-1): under an exogenous retirement-turnover shock the valid concrete measure co-moves with real cosmetic investment (+0.010, p = 0.01) while the naive measure does not (+0.002, p = 0.54). The measurement contributions are the passage-level validation with its reported polysemy ceiling (§3.3) and the LLM-ensemble high-precision alternative (§3.4). The cross-sectional β(VAI → CIR) association and the structural welfare calibration are demoted to supporting/illustrative; the failed P2 inspection design (D-B-3) and the failed H4/H5 tests (D-E-2/D-F-1) are reported honestly and narrow the scope but do not bear on the criterion-validity spine.

The pre-registered archive (OSF ZMJY5) is unmodified. This deviation log is the canonical record of what was done relative to what was promised. All decisions to deviate were made before examining the post-deviation outcomes (with the one exception of §4.4's re-framing of the CFPS null from confirmatory to exploratory, which was a post-hoc interpretation-level revision disclosed explicitly in D-F-1 and in §4.4's opening paragraph).
