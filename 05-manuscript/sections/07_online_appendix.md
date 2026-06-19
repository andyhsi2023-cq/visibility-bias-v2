# Online Appendix

**Manuscript**: *When Dictionaries Hit a Polysemy Ceiling: Validating a Measure of Visibility Bias with LLMs and Behavioral Evidence*

**Authors**: Hongyang Xi (Chongqing Survey Institute)†, Liu Can (Guangzhou College of Applied Science and Technology)†, Zhihui Li (Chongqing Survey Institute) · †co-first authors
**Pre-registration**: OSF DOI 10.17605/OSF.IO/ZMJY5
**Replication**: Zenodo DOI 10.5281/zenodo.19569978

---

## Appendix A: The Full Cadre-Attention Model

The main text (§2) gives an intuitive summary of the cadre-attention model. This appendix provides the full derivation.

### A.1 Setup

A local official in city $i$ allocates a municipal capital budget $B_i$ between visible capital $V_i$ and functional capital $F_i$ subject to $V_i + F_i = B_i$. Social welfare is Cobb-Douglas:

$$U^S(V_i, F_i) = \alpha \ln V_i + \beta \ln F_i, \quad \alpha + \beta = 1.$$

The supervisor observes both categories with Gaussian noise with variances $\omega_V^2 < \omega_F^2$ (assumption A1, observability asymmetry). The Bayesian posterior on the official's performance is the precision-weighted sum:

$$\pi_i = \rho V_i + (1-\rho) F_i, \quad \rho = \frac{\omega_V^{-2}}{\omega_V^{-2} + \omega_F^{-2}} \in (1/2, 1).$$

### A.2 Official's objective and FOC

The official maximizes a convex combination of social welfare and career value:

$$U^O = \lambda_i \left[\alpha \ln(a_i B_i) + \beta \ln((1-a_i) B_i)\right] + (1-\lambda_i) B_i \left[\rho a_i + (1-\rho)(1-a_i)\right]$$

where $a_i = V_i/B_i \in (0, 1)$ and $\lambda_i \in [0, 1]$ is the social-motivation weight. The first-order condition yields the cadre-attention equation:

$$\frac{\alpha}{a_i^*} - \frac{\beta}{1-a_i^*} = -\frac{1-\lambda_i}{\lambda_i} \phi B_i, \quad \phi \equiv 2\rho - 1 > 0.$$

### A.3 Closed-form and welfare loss

A Taylor expansion around $\delta_i \equiv (1-\lambda_i)/\lambda_i \cdot \phi B_i = 0$ gives:

$$a_i^* \approx a_i^{SO} + a_i^{SO}(1-a_i^{SO}) \delta_i.$$

The welfare loss expressed as a fraction of first-best utility is:

$$W_i = \frac{1}{2} \cdot \frac{(a_i^* - a_i^{SO})^2}{a_i^{SO}(1-a_i^{SO})}.$$

This quadratic form permits calibration from observed $a_i^*$ and a standard social-optimum benchmark $a_i^{SO}$.

## Appendix B: Specification Curve (P1 Robustness — demoted)

*This appendix supports the cross-sectional VAI→CIR association, which the revised paper demotes to a "modest external check" (§3.5, E-D); it is not part of the main evidentiary spine (the behavioral co-movement of §4). [Archive note: the pruned 24-permutation output file and the path `phase-A/specification_curve_v2.py` must be reconciled with the 96-spec full run before final deposit — see the pre-submission blockers memo.]*

### B.1 24-permutation specification curve

Following Simonsohn et al. [17], we ran a pre-registered specification curve combining:
- Lexicon thresholds: denominator requirement {≥3, ≥5, ≥10 total hits}
- Control-set subsets: {all controls, drop ln_pop, drop ind2_share, no controls}
- Panel windows: {2005-2015 full, 2008-2015 post-GFC, 2012-2015 post-Xi}
- FE structure: {city + year FE, city FE only}

Total: 3 × 4 × 3 × 2 / redundant = 24 non-redundant permutations.

**Results**: Median β = +0.107. All 24 coefficients positive. 22/24 significant at the 5% level; 2 marginally significant (p = 0.06–0.10). Full specification curve table in `03-analysis/phase-A/specification_curve_v2.py`.

## Appendix C: Further Robustness and Sensitivity

### C.1 Dictionary details

Full lists of V_ORIG (42 terms), F_ORIG (38 terms), V_EXT (+36 new terms, 78 total), F_EXT (+32 new terms, 70 total) are in `03-analysis/phase-E/construct_validity.py`. Coder-agreement statistics from the inter-coder validation protocol (Cohen's κ):
- Visible-term marking: κ = 0.87
- Functional-term marking: κ = 0.84
- Overall orientation (1–5 Likert): ICC = 0.79

### C.2 Horse races against alternative explanations (main text §4.1)

| Alternative | Specification | β(VAI) | p |
|---|---|---:|---:|
| Baseline P1 | City FE + year FE + 3 controls | +0.113 | 0.002 |
| + GDP growth control | Added annual GDP growth | +0.109 | 0.003 |
| + urbanization² control | Added urbanization rate and its square | +0.111 | 0.002 |
| + leader-tenure control | Added party-secretary + mayor tenure | +0.110 | 0.003 |
| All four jointly | All three above | +0.108 | 0.004 |

### C.3 P2 placebo battery (main text §4.4.1)

**Table C.3.** Placebo tests for the inspection event study.

| Placebo | β(k=0) | p | Interpretation |
|---|---:|---:|---|
| Close pre-era shift (fake 2011/2012) | +0.001 | 0.98 | Clean null — supports narrow-window TWFE |
| Far-era shift +4 yr (fake 2017/2018) | +0.023 | 0.0003 | Significant — flags secular-trend contamination |
| Far-era shift +6 yr (fake 2019/2020) | −0.025 | 0.001 | Significant — flags secular-trend contamination |
| Random-assignment (500 iters) | Observed −0.065 vs placebo [−0.043, +0.076] | 1.00 | Underpowered (only 2 cohorts) |

### C.4 Evidence for observability asymmetry (A1)

Three independent proxies for $\omega_V/\omega_F$:

1. **Inspection frequency**: Municipal Transparency Report audits per year of visible vs functional categories. Ratio 3.2:1 in favor of visible.
2. **Media reporting intensity**: Xinhua local news mentions per month. Ratio 2.8:1 in favor of visible.
3. **Accident-record visibility**: Ministry of Emergency Management major-accident reports by category. Only visible-category accidents (street collapse, façade fall) receive consistent national news coverage; functional failures (pipe rupture, flooding) are usually reported only as aggregate statistics.

All three support A1 at $p < 0.05$ (separately and jointly).

### C.5 Tenure-cycle dynamics (supplementary evidence)

Event-study around scheduled leadership transition (mayor + party-secretary tenure-end year):

| Event time | β(VAI) | p |
|---:|---:|---:|
| k = −2 (pre-transition −2 years) | +0.008 | 0.52 |
| k = −1 (year before transition) | **+0.031** | **0.021** |
| k = 0 (transition year) | −0.009 | 0.58 |
| k = +1 | +0.004 | 0.78 |

**Interpretation**: VAI spikes in the year before a scheduled leadership transition, when career-concern intensity $(1-\lambda)/\lambda$ is theoretically highest. This is consistent with P2's exogenous-attenuation logic in reverse (career-concern spikes → VAI spikes). We treat this as *supplementary* evidence because the identification relies on transitions being partially exogenous, which is weaker than our pre-registered design. Results replicate under city + year FE and are insensitive to controls.

### C.6 Heterogeneity by fiscal capacity

Equation $(\star)$ from §2.4 predicts that the visibility-bias distortion increases in $B_i$. We split the sample by above/below-median per-capita fiscal revenue:

| Subsample | β(VAI) on CIR | p | N |
|---|---:|---:|---:|
| Above-median fiscal revenue | +0.184 | 0.001 | 1,378 |
| Below-median fiscal revenue | +0.068 | 0.071 | 1,373 |
| Interaction (above × VAI) | +0.116 | **0.024** | 2,751 |

The high-revenue subsample's coefficient is substantially larger and more significant. The interaction is statistically distinguishable (p = 0.024).

### C.7 Welfare sensitivity (main text §4.3)

Full sensitivity across $a^{SO} \in [0.40, 0.50]$, utility forms, and shadow-pricing assumptions:

| $a^{SO}$ | Utility | $W$ per ¥1000B renewal | Scaled to ¥3.5T/yr × 8% renewal share |
|---:|---|---:|---:|
| 0.50 | Log | 0.06% | ¥0.2B/yr |
| 0.45 | Log (central) | 1.56% | **¥4.4B/yr** |
| 0.40 | Log | 3.94% | ¥11.0B/yr |
| 0.45 | CRRA(γ=2) | 3.12% | ¥8.8B/yr |
| 0.45 | BOE (replacement cost) | ~20% | ¥55B/yr |

**Defensible range**: ¥1–15B/yr under log utility and $a^{SO} \in [0.40, 0.50]$. The ¥55B BOE is a ceiling. (This calibration is demoted; the main text attaches no headline welfare figure — §4.4.)

### C.8 Passage-validation confusion matrix and error taxonomy (main text §3.2–§3.3)

Human gold standard: 120 sentences, four-class coding (visible / functional / mixed / irrelevant). Source: `03-analysis/phase-K/` (`anchor_human_labels.csv`, `score_anchor.py`).

**Table C.8a. Concrete (salience-based) dictionary vs human coding, n = 120.** Rows = human label, columns = dictionary prediction.

| human ↓ / dict → | visible | functional | mixed | irrelevant |
|---|---:|---:|---:|---:|
| visible | 15 | 1 | 1 | 2 |
| functional | 0 | 18 | 1 | 1 |
| mixed | 9 | 7 | 24 | 0 |
| irrelevant | 6 | 4 | 4 | 27 |

Per class: visible P = 0.500, R = 0.789, F1 = 0.61; functional P = 0.600, R = 0.900; mixed P = 0.800, R = 0.600; irrelevant P = 0.900, R = 0.659. Overall four-class accuracy = 0.74.

**Table C.8b. Visible-class false-positive taxonomy (naive dictionary).** Of 84 naive visible-class false positives (dictionary = visible, human/ensemble = not infrastructure), the drivers are:

| term | false positives | typical non-infrastructure use |
|---|---:|---|
| 示范 (model/demonstration) | 60–61 | 示范区, 示范项目, 改革示范 |
| 文明城市 (civilized city) | 7 | award/campaign title |
| 展示 (display/showcase) | 6 | "display achievements" |
| 美丽 (beautiful) | 5 | 美丽乡村 slogan |
| 形象 (image) | 4 | "government image" |

`示范` alone accounts for ~70% of visible false positives — the single-cause failure motivating the move to a concrete, salience-based lexicon (§3.2.2). Blanket-pruning the 13 most polysemous terms raises visible precision to 0.59 but collapses recall to 0.47, so the fix is surgical.

**Human intercoder agreement.** The 120-sentence gold standard was independently double-coded by two coders on the identical locked sentence set (`03-analysis/phase-K/second_coder_sheet_LOCKED.csv`, with dictionary and ensemble labels hidden). The **human intercoder agreement is Cohen κ = 0.70** (substantial; n = 120). Agreement is highest on the irrelevant and functional classes; the residual disagreement concentrates on the visible-versus-mixed boundary, consistent with the polysemy difficulty documented in §3.2–§3.3 (and itself part of why high passage precision favors the LLM ensemble). Human↔ensemble agreement is Cohen κ = 0.66.

**Figure ESM-6 (procurement, §4.3).** `04-figures/fig_bidding_by_city.{pdf,png}` — visible:functional project-count ratio across Zhejiang localities (2.96M procurement records, 2019–2026; v2 domain-verified lexicon). Panel A: distribution over 108 localities (median 1.8; 97 of 108 above 1:1 parity). Panel B: top 15 localities by procurement volume (near-parity county exceptions in red). Source: `03-analysis/phase-L-bidding/` (`classify_bidding.py`, `bidding_lexicon.py` v2, `by_city.csv`).

**Table C.8c. LLM-ensemble (Gemini 3.1 Pro + ChatGPT 5.5 + DeepSeek) vs human, n = 499.** Majority label; inter-model Fleiss κ = 0.835; overall accuracy 0.842; human↔ensemble Cohen κ = 0.66. Source: `passage_coding_sheet_ensemble.validation.json`.

| class | precision | recall |
|---|---:|---:|
| visible | 0.793 | 0.96 |
| functional | 0.813 | 0.897 |
| mixed | 0.857 | 0.609 |
| irrelevant | 0.913 | 0.806 |

## Appendix D: Pre-Registration and Deviation Log

(In main text as §6 Appendix D. See Deviations D-B-1 through D-F-1.)

## Appendix E: Replication Architecture

Full directory layout (Zenodo record 19569978):

```
visibility-bias-v2/
├── 00-admin/           Research plan, upgrade roadmap, outreach drafts
├── 03-analysis/        Python analysis by phase:
│                         G/K  passage validation (human gold + 3-model LLM ensemble)
│                         J    behavioral criterion validity (turnover co-movement)
│                         L    Zhejiang procurement-frequency check
│                         B/B2/E/E2/F  demoted inspection / construct / micro tests
├── 04-figures/         PDF and PNG figures for all main-text exhibits
├── 05-manuscript/      Manuscript sections + compiled R2 + submission package
├── 06-review/          S7 audit reports + phase memos
├── 07-prereg/          OSF pre-registration archive + Zenodo DOI record
├── 01-literature/      references.bib
└── 02-data/processed/  text panels (naive + concrete lexicons), CCDI rounds
```

The criterion-validity panel `master_2002_2024.csv` (merged from the absorbed `officials-turnover-cn` materials; holds both the naive `vai_composite` and concrete `wr_visibility` series alongside CIR and turnover variables) and the lexicon-build script `build_workreport_text.py` are included in the Zenodo record. Running instructions in `README.md` at the record root.

*Note: the absorbed `officials-turnover-cn` project is not published separately; its retirement-exogenous identification and `wr_visibility` measure are folded into this paper, so there is no double-publication and no citation of unpublished work.*
