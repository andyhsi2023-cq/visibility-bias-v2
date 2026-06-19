# 5. Discussion

## 5.1 What the paper establishes methodologically

The paper's contribution is the Visibility Attention Index, a pre-registered, replicable instrument for the visible-versus-functional composition of infrastructure language. It is now validated more rigorously than in the original draft, and honestly bounded:

- Direct passage-level validation (§3.2.0): the naive appearance-word dictionary fails (visible precision 0.10); the concrete, salience-based VAI reaches 0.50–0.60 but meets a polysemy ceiling near 0.60–0.64; an LLM ensemble clears it (0.84 accuracy, Fleiss κ = 0.835). Human intercoder agreement is Cohen κ = 0.70.
- Behavioral criterion validity (§3.2.7) is the test that does the work. Under an exogenous, retirement-driven turnover shock the concrete VAI co-moves with real cosmetic investment (+0.010, p = 0.01; clean pre-trend), while the naive measure does not (+0.002, p = 0.54). The construct is real in behavior, and the right measure tracks it.
- A cross-source accounting correlation (E-D, r = 0.24) provides independent external evidence, modest in magnitude. An independent-dictionary replication (E-A, r = 0.93) is a reliability check rather than a validation. And an independent procurement corroboration (§4.3) shows a ≈2:1 visible-over-functional tilt in 97 of 108 Zhejiang localities, with a visible-dominated spending tail.

One pre-registered test, applying the lexicon to Chinese Wikipedia, fails (r = −0.15 against a [0.3, 0.7] criterion). We report it plainly as a domain mismatch that bounds the instrument to governance rhetoric.

## 5.2 What substantively follows (conditional on the instrument)

Within cities, VAI tracks the accounting-based Cosmetic Investment Ratio (P1, β = +0.111) with no accompanying change in total investment. The association is therefore compositional rather than expansionary, and under the turnover shock both rise together. We read these as evidence that the measure captures strategic compositional attention. We do not offer a headline welfare figure, because the model-based calibration (§4.4) is too assumption-dependent to support one.

## 5.3 What we cannot establish

- Causal identification of drivers is not achieved. The inspection event study fails under heterogeneity-robust estimation (§4.5); the retirement-turnover design supports *measurement* (criterion) validity, not a causal theory of what produces visibility bias.
- External (non-governance) validity is bounded. The Wikipedia null scopes the measure to governance rhetoric, and an appropriate policy-rhetoric third-party validation (e.g., Xinhua local-policy news, CNKI key-newspaper coverage) remains future work.
- Intercoder agreement is substantial but not perfect. Two human coders reach Cohen κ = 0.70 on the 120-sentence gold set. Residual disagreement concentrates on the visible-versus-mixed boundary, itself a manifestation of the polysemy the paper documents, so passage-level precision/recall carry a few points of coder-judgment uncertainty.
- The procurement corroboration is provincial. It covers Zhejiang, and although frequency and amount both corroborate the tilt, a "project" is proxied by the deduplicated award record, so the count comparison is sensitive to packaging. National generalization is untested.
- No welfare claim. The structural welfare figure is assumption-dependent and demoted, and we attach no policy magnitude to it.

## 5.4 Portability to non-Chinese settings

The construction-and-validation protocol has a fixed shape: seed a dictionary, validate at the passage level, *report the ceiling*, escalate to LLM classification where needed, and anchor validity behaviorally against an accounting outcome under an exogenous shock. In principle this protocol ports to other settings where bureaucratic agents produce structured, consequential annual documents (EU National Reform Programmes; Indian state budget speeches; Mexican municipal *Plan de Desarrollo* documents), though we have not tested it outside China. What is *not* portable is the specific lexicon and the institutional observability-asymmetry parameters, which require re-derivation in each context. What transfers is the validation discipline, not the keyword list.

## 5.5 Policy implications (conditional on the cadre-attention model)

Suppose the cadre-attention model is substantively correct. It is theoretically motivated and now behaviorally supported (§3.2.7), though not cleanly identified causally. Three levers then follow. (1) Increase the observability of functional categories, reducing the legibility asymmetry, through real-time pipe-pressure telemetry, open waterworks dashboards, and mandatory structural-safety reporting. (2) Introduce functional output targets in cadre evaluation, raising the social-motivation weight. (3) Build citizen-audit portals as supplementary, informational pressure, given the §4.5 individual-level null. Because these follow from the model rather than from identified causal estimates, we offer them as model-implied possibilities rather than forecasts, and attach no net-present-value figure.

---

# 6. Conclusion

We set out to measure visibility bias in Chinese municipal government work reports and to take seriously the question applied dictionary work usually skips: does the measure capture the construct? The Visibility Attention Index, built from 6,294 GWRs, is validated directly at the passage level. We report that validation honestly, including the naive dictionary's failure (precision 0.10), the concrete lexicon's polysemy ceiling (~0.60), and an LLM ensemble that clears it (0.84). The behavioral test settles the question: under an exogenous retirement-turnover shock the valid measure co-moves with real cosmetic investment while the naive one does not. Descriptively, VAI tracks the accounting Cosmetic Investment Ratio and is corroborated by an independent procurement corpus, where visible projects run ≈2:1 over functional and own the high-value tail. One pre-registered third-party test failed and is reported plainly. An inspection event study, a CFPS micro-foundation, and a welfare calibration are demoted as non-robust or assumption-dependent.

The contribution is methodological: a pre-registered, passage-validated, behaviorally-anchored instrument for measuring compositional infrastructure rhetoric, with an honest map of its limits and a high-precision LLM alternative where the dictionary stops. Two points may carry beyond this one-country case and invite testing elsewhere. First, polysemy imposes a precision ceiling on dictionary measures of everyday-word constructs that curation cannot break, and that ceiling should be reported rather than hidden. Second, for measures of strategic attention the validity test that decides the matter is behavioral co-movement under an exogenous shock, not internal reliability or passage precision alone. We invite extension via a policy-rhetoric third-party corpus, further exogenous shocks, and application to bureaucratic text in other institutional settings.

Pre-registration: OSF DOI 10.17605/OSF.IO/ZMJY5. Replication archive: Zenodo DOI 10.5281/zenodo.19569978; GitHub: andyhsi2023-cq/visibility-bias-v2.

---

# Statements and Declarations

**Competing Interests.** The authors declare no competing financial or non-financial interests related to this work.

**Funding.** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. The work was conducted as part of the authors' professional research activities.

**Authors' Contributions.** Hongyang Xi and Liu Can contributed equally and are co-first authors. Hongyang Xi (corresponding author) conceived the study, constructed the lexicons and the LLM-ensemble classification, performed the data collection and statistical analysis (including the behavioral criterion-validity test), drafted the manuscript, and prepared the replication archive. Liu Can constructed and verified the public-procurement (bidding) evidence (§4.3), contributing urban- and rural-planning domain expertise to the visible-versus-functional classification of construction projects. Zhihui Li independently performed the second passage-level coding of the validation sample for the intercoder-reliability assessment (§3.2.0). All authors critically revised the manuscript, approved the final version, and are accountable for the integrity of the work.

**Data Availability.** All data, lexicons, code, and intermediate outputs are archived at Zenodo (DOI [10.5281/zenodo.19569978](https://doi.org/10.5281/zenodo.19569978)) and mirrored on GitHub (`andyhsi2023-cq/visibility-bias-v2`). The Zenodo record is open access (CC-BY-4.0). Source government work reports are scraped from publicly accessible municipal government websites; CFPS individual data are obtained from the Institute of Social Science Survey at Peking University under their public data-use agreement; the China Urban Construction Statistical Yearbook (Ministry of Construction / MOHURD, 2005–2015) and Zhejiang public-procurement records are publicly archived.

**Code Availability.** All analysis scripts (Python; pandas, statsmodels) and the passage-validation and re-pull toolchains are archived in the Zenodo record.

**Pre-registration.** Pre-registered at the Open Science Framework (DOI [10.17605/OSF.IO/ZMJY5](https://doi.org/10.17605/OSF.IO/ZMJY5), archived 2026-04-14); the passage-level human/LLM validation and the behavioral criterion-validity analyses are pre-specified extensions. All deviations are logged in Appendix D.

**Ethics Approval.** Not applicable. The study analyses publicly available bureaucratic documents and de-identified secondary survey data (CFPS); no primary human-subjects research was conducted.

**Consent for Publication.** Not applicable.

**Use of Generative AI.** Large-language-model classification is an *object of study and a measurement tool* in this paper (the three-family ensemble of §3.2.0), documented and reproducible. Separately, the authors used an LLM for copy-editing of draft prose; all substantive content, analysis, and interpretation are the authors' own.
