# 5. Discussion

## 5.1 What the paper establishes

Taking the rungs together, the paper delivers a *validated* measure of compositional policy attention and an honest account of how far each validation move carries. A naive dictionary fails at the passage level (visible precision 0.10); a concrete, salience-based lexicon raises precision to 0.50–0.60 but meets a polysemy ceiling near 0.60–0.64; an LLM ensemble clears the ceiling (0.84 accuracy, Fleiss κ = 0.835); and — decisively — the valid concrete measure co-moves with real cosmetic investment under an exogenous, retirement-driven incentive shock (+0.010, p = 0.01, clean pre-trend), while the naive measure does not (+0.002, p = 0.54). The construct is real in behavior, and the right text measure tracks it.

## 5.2 Methodological lessons

Within this single-country case (Chinese municipal GWRs), three lessons emerge that may transfer — offered to be tested elsewhere, not assumed.

**Lesson 1 — Dictionary precision is bounded by polysemy, not by effort.** For compositional constructs carried by everyday words, a non-trivial share of keyword occurrences are metaphorical or categorical (道路 as "the *path* of industrialization"; 轨道交通 as the rail-transit *industry*). Because these words are genuinely on-construct in the majority of uses, pruning them to raise precision destroys recall, so a precision ceiling is reached that no amount of curation breaks. Reporting this ceiling — rather than tuning a lexicon until an aggregate correlation looks acceptable — should be standard practice. The diagnostic is cheap: a few hundred human-coded passages and a per-class confusion matrix reveal it immediately.

**Lesson 2 — Behavioral co-movement is the decisive validity test for measures of strategic attention.** Internal reliability (E-A, r = 0.93) and aggregate cross-source correlation (E-D, r = 0.24) are routinely offered as "validation," but our naive measure is internally reliable and still behaviorally inert. What separates a valid measure from a stable-but-empty one is whether it *moves with real behavior under an exogenous shock*. Where an incentive shock and an accounting outcome are available, criterion validity of this kind should outrank passage precision and internal reliability in the hierarchy of evidence.

**Lesson 3 — Use LLM-ensemble classification where the dictionary ceiling binds, and report inter-model agreement.** When high passage precision is required, a multi-family LLM ensemble is the practical route (0.84 here) — consistent with a fast-growing literature showing LLMs match or surpass human and crowd annotation of political text [5, 20, 21] — and inter-model agreement (Fleiss κ) is the natural reliability statistic to report alongside accuracy. The transparency cost is real, so the choice is a genuine trade-off: dictionaries for transparent, reproducible aggregate indices with attenuating error; LLM ensembles for precision-critical passage-level work.

## 5.3 Limitations

We are explicit about what the paper does not establish.

- **Intercoder agreement is substantial but not perfect.** Two independent human coders reach Cohen κ = 0.70 on the 120-sentence gold set; residual disagreement concentrates on the visible-versus-mixed boundary — itself a manifestation of the polysemy the paper documents — so passage-level precision/recall carry a few points of coder-judgment uncertainty.
- **The procurement check is provincial.** It covers Zhejiang only; project frequency *and* investment amount both corroborate the tilt, but a "project" is proxied by the deduplicated award record, so the count comparison remains sensitive to how works are packaged. National generalization is untested.
- **Causal identification of drivers is not achieved.** The inspection event study fails under heterogeneity-robust estimation; the retirement-turnover design supports *measurement* validity, not a causal theory of what produces visibility bias.
- **No welfare claim.** The structural welfare figure is assumption-dependent and demoted; we attach no policy magnitude to it.
- **External (non-governance) validity is not established.** The Wikipedia null bounds the measure to governance rhetoric; an appropriate policy-rhetoric third-party validation (e.g., Xinhua local-policy news, CNKI key-newspaper coverage) remains future work.

## 5.4 Portability

The validation protocol — seed a dictionary, validate at the passage level, *report the ceiling*, escalate to LLM classification where needed, and anchor validity behaviorally against an accounting outcome under an exogenous shock — could plausibly transfer to other settings where bureaucratic agents produce structured, consequential annual documents (e.g., EU National Reform Programmes; Indian state budget speeches; Mexican municipal *Plan de Desarrollo* documents), though we have not tested it outside China. What is *not* portable is the specific lexicon and the institutional observability-asymmetry parameters, which require re-derivation in each context. The transferable contribution is the validation discipline, not the keyword list.

---

# 6. Conclusion

We set out to measure visibility bias in Chinese municipal government work reports and, in doing so, to take seriously the question applied dictionary work usually skips: does the measure capture the construct? The answer is a ladder. A naive dictionary fails (visible precision 0.10) because abstract appearance words are polysemous; a concrete, salience-based lexicon improves greatly (0.50–0.60) but hits a polysemy ceiling near 0.60–0.64; an LLM ensemble clears it (0.84, Fleiss κ = 0.835); and the valid measure — unlike the naive one — co-moves with real cosmetic investment under an exogenous, retirement-driven incentive shock. The contribution is methodological: a rigorously validated, behaviorally anchored procedure for measuring compositional policy attention in bureaucratic text, with an honest map of its limits and a high-precision alternative where the dictionary stops.

Two points may outlast this one-country case and invite testing elsewhere. First, polysemy imposes a precision ceiling on dictionary measures of everyday-word constructs that curation cannot break, and that ceiling should be reported, not hidden. Second, for measures of strategic attention the decisive validity test is behavioral co-movement under an exogenous shock — not internal reliability, and not passage precision alone. We invite extension along three lines: a policy-rhetoric third-party corpus to strengthen external validity; additional exogenous incentive shocks to widen the criterion-validity base; and application of the validate-report-the-ceiling-then-escalate protocol to bureaucratic text in other institutional settings.

Pre-registration: OSF DOI 10.17605/OSF.IO/ZMJY5. Replication archive: Zenodo DOI 10.5281/zenodo.19569978; GitHub: andyhsi2023-cq/visibility-bias-v2.

---

# Statements and Declarations

**Competing Interests.** The authors declare no competing financial or non-financial interests related to this work.

**Funding.** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. The work was conducted as part of the authors' professional research activities.

**Authors' Contributions.** Hongyang Xi and Liu Can contributed equally and are co-first authors. Hongyang Xi (corresponding author) conceived the study, constructed the lexicons and the LLM-ensemble classification, performed the data collection and statistical analysis, drafted the manuscript, and prepared the replication archive. Liu Can constructed and verified the public-procurement (bidding) evidence (§4.3), contributing urban- and rural-planning domain expertise to the visible-versus-functional classification of construction projects. Zhihui Li independently performed the second passage-level coding of the validation sample for the intercoder-reliability assessment (§3.3). All authors contributed to the critical revision of the manuscript, reviewed and approved the final version, and are accountable for the integrity of the work.

**Data Availability.** All data, lexicons, code, and intermediate outputs supporting the findings are archived at Zenodo (DOI [10.5281/zenodo.19569978](https://doi.org/10.5281/zenodo.19569978)) and mirrored on GitHub (`andyhsi2023-cq/visibility-bias-v2`). The Zenodo record is Restricted during peer review; reviewer access is provided via the token in the cover letter and will be flipped to Public upon acceptance. Source government work reports are scraped from publicly accessible municipal government websites; CFPS individual data are obtained from the Institute of Social Science Survey at Peking University under their public data-use agreement; the MOHURD Urban Construction Statistical Yearbook (2005–2015) and Zhejiang public-procurement records are publicly archived.

**Code Availability.** All analysis scripts (Python; pandas, statsmodels) and the passage-validation toolchain are archived in the Zenodo replication record.

**Pre-registration.** This study is pre-registered at the Open Science Framework (DOI [10.17605/OSF.IO/ZMJY5](https://doi.org/10.17605/OSF.IO/ZMJY5), archived 2026-04-14); the passage-level human/LLM validation and the behavioral criterion-validity analyses are pre-specified extensions. All deviations are logged in Appendix D.

**Ethics Approval.** Not applicable. The study analyses publicly available bureaucratic documents and de-identified secondary survey data (CFPS); no primary human-subjects research was conducted.

**Consent for Publication.** Not applicable.

**Use of Generative AI.** Large-language-model classification is an *object of study and a measurement tool* in this paper (the three-family ensemble of §3.4), documented and reproducible. Separately, the authors used an LLM for copy-editing of draft prose (readability, grammar, consistency); all substantive content, analysis, and interpretation are the authors' own.
