# Pre-Registration: Visibility Bias and the Composition of Urban Investment in China (v2)

**Platform**: Open Science Framework (OSF)
**Template**: OSF Pre-registration v2 (adapted with AsPredicted 9-question core)
**Status**: DRAFT — user must create OSF account at https://osf.io, upload this document, and archive the DOI before running any Phase B–F regressions.
**Author (to appear on OSF)**: Hongyang Xi — Chongqing Survey Institute Co., Ltd.
**Project root**: `~/Desktop/Research/visibility-bias-v2/`
**Model reference**: `03-analysis/model.md`

---

## A. Metadata

| Field | Value |
|---|---|
| Title | Visibility Bias in Chinese Urban Governance: Model, Measurement, Identification |
| Acronym | VBIAS-V2 |
| Pre-reg date (to fill) | YYYY-MM-DD (the day OSF stamps the DOI) |
| Data access date | 2026-04-14 (main v1 panel); Phase B shock data extraction TBD |
| Proposed study type | Observational with quasi-experimental identification |
| Has data been accessed by author? | Yes for v1 panel (used to motivate v2 design); **no** for Phase B shock outcomes, Phase E third-party VAI corpus, Phase F CFPS matched subsample |

## B. Hypotheses

Derived from `03-analysis/model.md` Propositions 1–3:

- **H1 (P1 — compositional substitution)**: In city-year observations, a one-standard-deviation increase in Visibility Attention Index (VAI) raises the Cosmetic Investment Ratio (CIR) by β > 0, without increasing total infrastructure investment. Pre-registered sign: β > 0 for CIR; coefficient on ln(total) statistically indistinguishable from zero.

- **H2 (P2 — exogenous attenuation)**: Central anti-corruption inspections (staggered 2013–2016, assignment-timing exogenous conditional on pre-inspection covariates) causally *reduce* VAI and *raise* the functional-investment share. The reduction in VAI and the reduction in CIR will have **matching signs and approximately matching magnitudes** (scaled by the visibility-legibility wedge $\phi$ and fiscal capacity $B$).

- **H3 (P3 — structural welfare)**: The quadratic welfare-loss specification implied by the Cobb-Douglas model [$W_i = \tfrac{1}{2} \tfrac{(a^*_i - a^{SO})^2}{a^{SO}(1-a^{SO})}$] yields an aggregate annual welfare loss in the range **¥1–¥15 billion** under log-utility, central parameter values $a^{SO} = 0.45$; plausible range under sensitivity is ¥0.1–¥11B/year. The headline central estimate is **¥4.4 billion/year**.

- **H4 (third-party validation — D1 fix)**: A Visibility Attention Index constructed from independent third-party text (Xinhua news, provincial-gov descriptions of the city) will correlate with the primary VAI at $r \in [0.3, 0.7]$ and will independently predict CIR with $β > 0$ (at the 5% level) in the same direction as the primary measure.

- **H5 (micro-foundation — D7 fix)**: In CFPS individual-level data, residents in high-VAI city-years will report *higher* satisfaction with visible amenities (parks, roads, streetscapes) and *lower* satisfaction with functional amenities (water, heating, flood resilience). Effect sizes: at least |Cohen's d| = 0.10 at the city-year level.

## C. Data

### C.1 Primary sources (known)
- 6,294 municipal government work reports (GWR), 282 cities, 2002–2024 (extracted)
- MOHURD *Urban Construction Statistical Yearbook*, 2005–2015, 9-category investment (extracted)
- CPED v1.0 + hand-compiled officer panel (extracted)
- China Land Market Network 2000–2022 (extracted)
- CEADs carbon, PM2.5, CFPS 2010–2022, CSMAR regional (extracted)

### C.2 Data to be acquired for Phase B
- **Anti-corruption inspection timing**: ChinaFile China Dashboard + Harvard Dataverse replication archive (Chen-Kung 2019); city-year treatment assignments 2013–2016.
- **Smart-city pilot designations**: MOHURD announcements 2012–2016 (backup instrument).

### C.3 Data to be acquired for Phase E (third-party VAI)
- Xinhua news archive (Xinhua News Agency, 2002–2024): city-level coverage
- Provincial-government annual reports mentioning prefecture-level cities
- Estimated corpus: ~50 GB text across 282 cities × 23 years

### C.4 Data to be acquired for Phase F (micro-foundation)
- CFPS individual satisfaction items: `qm401`–`qm406` (2010, 2012, 2014, 2016, 2018, 2020)
- Match to city-year VAI via `provcd` + `countyid` → `city_std`

### C.5 Exclusion rules (pre-specified)

City-years with missing VAI (fewer than 50 characters of renewal-relevant GWR text) will be excluded. City-years with missing CIR (all 9 MOHURD investment categories zero) will be excluded. The post-exclusion main-analysis panel is expected to be ≥2,700 city-years for H1 and ≥1,500 city-years for H2.

## D. Analyses

### D.1 Baseline (H1)

$$\text{CIR}_{i,t} = \beta \cdot \text{VAI}_{i,t} + \gamma' X_{i,t} + \mu_i + \tau_t + \epsilon_{i,t}$$

Controls $X$: ln(GDP per capita), ln(population), secondary-industry share, officer tenure, officer age.
Fixed effects: city $\mu_i$ and year $\tau_t$. Standard errors clustered by city.
Pre-registered prediction: $\beta > 0$, significant at 5%.

### D.2 Specification curve (H1 robustness — pre-registered "defensible set")

Cartesian product of:
- VAI variant (4): Baseline, Extended, Contextual, Composite
- Fixed-effect structure (4): city only; year only; city + year; city + province-by-year
- Control set (4): {none, economic, officer, both}
- Sample (3): full; excluding provincial-level municipalities; balanced panel
- Clustering (2): city; province

Total: 384 specifications. Pre-registered acceptance criterion: **≥70% statistically significant at 5% with positive sign**. The 96-spec-curve subset used in v1 is a consistent projection of this design.

### D.3 Anti-corruption inspection event study (H2)

$$\text{VAI}_{i,t} = \sum_{k = -3, k \ne -1}^{+3} \theta_k \mathbb{1}[\text{years since inspection} = k] + \mu_i + \tau_t + \nu_{i,t}$$

Estimated with Callaway-Sant'Anna (2021) doubly-robust DiD. Analogous specification for CIR.
Pre-registered prediction: $\theta_k < 0$ for $k \ge 0$ in VAI regression, and magnitudes ≥ 0.02.
Phase B will run power analysis **before** looking at post-treatment outcomes.

### D.4 Third-party VAI (H4)

Construct VAI_ext from Xinhua corpus using same dictionary. Estimate:
$$\text{CIR}_{i,t} = \beta_1 \cdot \text{VAI}_{i,t} + \beta_2 \cdot \text{VAI}^{ext}_{i,t} + \ldots$$
Pre-registered acceptance: $\beta_2 > 0$ at 10% level.

### D.5 Welfare calculation (H3)

Compute per-city $W_i = \tfrac{1}{2}(a^*_i - a^{SO})^2 / [a^{SO}(1-a^{SO})]$ using $a^* = $ observed CIR, $a^{SO} \in \{0.40, 0.42, 0.44, 0.45, 0.46, 0.48, 0.50, 0.52, 0.55\}$. Aggregate using annual service flow = 0.08 × ¥3.5T municipal construction expenditure.

### D.6 CFPS micro (H5)

City-year mean of individual satisfaction scores on visible vs functional amenities; regress on VAI with province × year FE and individual controls.

## E. Outcome neutral

The primary outcome is a **compositional effect** (visible share up, functional share down, total unchanged). Our model **predicts null effects on total investment, housing prices, total emissions, and aggregate health** (see model.md §4; these are the v1 Null Table boundary conditions). These null predictions are **pre-registered as predictions**, not as post-hoc interpretations.

**Rescue clause**: If any of these predicted nulls come up statistically significant in Phase E/F re-runs, we will report it as a finding **against** the model, not attempt to reinterpret.

## F. What is NOT pre-registered

- Exploratory analyses of heterogeneity across coastal/inland, high-land-finance/low-land-finance, etc., will be clearly labeled as exploratory.
- We pre-commit that we will **not** drop data to improve fit.
- Any new dictionary construction (beyond the four variants listed) will be post-hoc and labeled.

## G. The 9 AsPredicted questions

1. **Have any data been collected yet?** Yes for v1 panel. No for Phase B inspection outcomes, Phase E third-party corpus, Phase F CFPS satisfaction items.
2. **What's the main question?** Does a causal shock to local officials' attention (anti-corruption inspection) shift the compositional allocation of urban infrastructure from visible to functional categories, and does this reallocation represent a welfare improvement?
3. **Describe the key dependent variable(s).** Cosmetic Investment Ratio (CIR); category-level log investment; CFPS satisfaction items.
4. **How will you manipulate the key variable?** Staggered treatment from anti-corruption inspection assignments 2013–2016 (exogenous timing conditional on pre-inspection covariates).
5. **Describe your analysis.** Event-study DiD (Callaway-Sant'Anna), specification-curve analysis across 384 defensible specifications, structural welfare calculation per Proposition 3.
6. **Sample size and stopping rule.** Full panel of 282 prefecture-level cities × 2002–2024 where data are available; **no interim look, no stopping rule — analyze full panel once assembled**.
7. **Rules for excluding observations.** Missing VAI (low GWR text) or missing CIR (zero in all categories) — see §C.5.
8. **Anything else?** Power analysis will be conducted on simulated data before running post-treatment Phase B regressions; welfare calculation is a pre-specified sensitivity grid.
9. **Have results been obtained for any of the planned analyses?** Yes for v1 baseline (β = 0.118) and v1 spec-curve (95.8% significant). **No** for Phase B causal shocks, Phase E third-party VAI, Phase F CFPS micro. Those are the analyses this pre-reg controls for forking paths.

## H. Honest caveats

1. **V1 is not pre-registered** and has already informed the design of V2. V2's contribution on any outcome already tested in V1 is therefore a **replication**, not a novel pre-registered test. The novel pre-registered tests are H2, H3, H4, H5.
2. **H3 welfare magnitude (¥4.4B/year central)** is substantially smaller than the idea-vetting BOE (¥45–65B/year) because log utility misses non-convex catastrophic damages. This is acknowledged up front, not buried.
3. **Anti-corruption inspection assignment** has been argued to have some endogenous components (Chen-Kung 2019 find discretion in which cities are inspected first). Our H2 identification is conditional on pre-inspection covariates; we will run robustness that tests for pre-trend violations (Roth 2022).

## I. Deviations clause

If, during Phase B–F analysis, the data force a deviation from this pre-reg (e.g., inspection assignment turns out to be too correlated with pre-inspection visibility trends to support the design), we commit to:
- Logging the deviation in an `amendments/` folder with timestamp
- Reporting any deviation transparently in the manuscript's "Pre-registration and Deviations" section
- Treating any post-deviation test as **exploratory** rather than confirmatory

## J. Permanent URL and archiving

Upon user submission to OSF:
- Pre-reg DOI: *(user to paste here once archived)*
- Archived version of `model.md`: *(OSF link once attached)*
- Code archive (Python + data derivation scripts): Zenodo archive to be created at manuscript submission time.

---

## NEXT STEP FOR USER

To complete criterion #9 (pre-registration), the author should:

1. Create (or log into) an OSF account at https://osf.io
2. Create a new project titled "Visibility Bias and the Composition of Urban Investment in China (v2)"
3. Go to the "Registrations" tab → "New Registration" → choose **"OSF Preregistration"** template (or **"AsPredicted"** for minimal version)
4. Copy the relevant sections from this document into the OSF form
5. Check "Release registration immediately" (not embargo)
6. Record the resulting DOI in `07-prereg/osf-doi.txt`

**This is the one action in α-min that AI cannot complete for you.** Estimated time: 20–30 minutes.
