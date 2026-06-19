# S7-2 Independent Novelty Audit

**Manuscript**: Visibility Bias in Chinese Urban Governance: Model, Measurement, Identification
**Auditor role**: Independent adversarial scorer (no loyalty to prior internal estimates)
**Date**: 2026-04-14
**Prior internal estimate**: 4.6 / 10
**This audit's verdict**: **3.5 / 10**

---

## Score Summary

| Criterion | Score | Justification |
|---|---:|---|
| 1. New fact | **0.5** | Within-document Review>Plan differential (Δ=0.025, paired t=8.4) is a genuinely new, replicable empirical pattern not previously documented. The headline CIR~VAI cross-sectional correlation (β=+0.113) is evolutionary, not new; it restates the v1 Habitat-International finding in event form. Half-credit for the within-document fact only. |
| 2. New mechanism | **0.5** | The Cobb-Douglas cadre-attention model with observability asymmetry ω_V²<ω_F² is a clean formalization but not a conceptual breakthrough — Holmström (1979), Dewatripont-Jewitt-Tirole (1999), and recent Chinese-cadre literature (Jia, Kudamatsu, Seim 2015; Lei-Zhou 2022) already contain the relevant multi-task/legibility logic. The paper formalizes a specific compositional margin; that is incremental refinement, not new mechanism. |
| 3. New data | **0.5** | 6,294 GWRs (2002–2024) is a sizeable corpus but Chinese work-report corpora already exist in the literature (Hanlon 2022; Qian-Wen 2024). The lexicon (42+38 terms) is hand-curated and small. The Wikipedia-zh corpus added in Phase E2 **failed its pre-registered validation** (r=−0.15) and is therefore a liability, not a data contribution. Half-credit for corpus scale + public release; zero for novelty of source. |
| 4. New measurement/method | **0.5** | VAI as a simple count-ratio index is methodologically light — no embedding, no LLM classification, no structural topic model. The within-document Review-vs-Plan split (E-B) is the one methodological innovation and is worth half a point. The "specification-curve" framing is not new (Simonsohn-Simmons-Nelson 2020). |
| 5. Clean identification | **0.0** | **This is the paper's fatal weakness.** (a) P1 is cross-sectional within-city correlation — no exogenous variation in VAI; reverse causality and omitted-variable bias are wide open. (b) P2's TWFE estimate (β=−0.065, p=0.011) **does not survive Sun-Abraham heterogeneity-robust re-estimation** (β=−0.019, p=0.87, Phase B2). (c) Far-era placebos return significant coefficients — the design cannot separate the inspection shock from post-2015 secular trends. (d) Only 2 distinct treatment years with universal eventual treatment. Zero credit. |
| 6. Robustness | **0.5** | The paper does run many checks (dictionary expansion r=0.93, 24-way specification curve, close pre-era placebo null). Partial credit. **Major penalty**: Phase E2 failed, Phase B2 attenuated to null, Phase F null on pre-registered direction. When the robustness matrix is this mixed, the honest score is 0.5 not 1.0. An adversarial referee reads "5 of 10 tests passed, 3 failed, 2 ambiguous" as "the effect is fragile." |
| 7. Clean falsification | **0.5** | Three pre-registered tests with failable predictions were executed. The CFPS citizen-popularity null (C1) is the strongest — it's a genuine bet-against-alternative-hypothesis. However, the null was reinterpreted *post hoc* into "supervisor-channel primacy," which is classic HARKing-adjacent behavior. SOP rule: "A null pre-registered result counts as +0.5 max unless it falsifies an important alternative." The citizen-popularity alternative is not a heavily-defended alternative in the literature — nobody seriously claimed Chinese cadres over-provide lamp-posts to win citizen votes — so the falsification is of a straw man. Half credit. |
| 8. Micro-foundation | **0.0** | **The micro-foundation test produced a null (|d|≤0.011, p>0.3 on all three outcomes).** The paper spins this as "confirming" the upward-signaling model, but operationally the paper has no individual-level positive evidence. No supervisor-level data (no promotion outcomes, no evaluation scores, no inspection grades) is used. The theoretical model is about supervisors; the micro data is about citizens; they don't connect. Zero credit. |
| 9. Policy relevance | **0.5** | Three policy levers are discussed and a ¥50–60B 10-year NPV is given, but the welfare calculation (¥4.4B/yr central estimate, ¥1–15B range) is a structural calibration off a Cobb-Douglas model with assumed α∈[0.40,0.50] — the range is 15× wide and the point estimate depends on a non-identified parameter. Order-of-magnitude only. Half credit. |
| 10. Replication-ready | **0.5** | OSF pre-registration (zmjy5) exists; GitHub repo named; Zenodo DOI "pending." CFPS and MOHURD data are restricted — reviewers cannot fully replicate. Wikipedia corpus is released. Code pipeline appears complete. Half credit — a true "1" requires DOI minted and all data (or detailed access protocols) in one archive at submission time. |
| **TOTAL** | **3.5 / 10** | |

---

## Tier Assignment (per SOP §2 Stage 4)

3.5 falls at the **Third Tier / Second Tier low-end boundary**, with the tiebreak going to **Third Tier** given the criterion-5 failure.

- **Third Tier (0–3.5)**: China Economic Review, Cities, Habitat International, Journal of Urban Management
- Second Tier requires ≥ 3.5 *and* clean identification; this paper has 3.5 but fails on identification

---

## Verdict

**Recommended target journal**: **China Economic Review** (Third Tier). Secondary acceptable: *Cities* (already tried a sister-title Habitat International, desk rejected on novelty grounds 2026-04-13).

**Do NOT target**: RSUE, JHE, JUE, or any Nature-family. The Sun-Abraham attenuation and Wikipedia validation failure would both be caught by any competent referee at these venues. Expected desk reject or first-round reject with probability > 70%.

**Do NOT re-target Habitat International**. Same editorial board already rejected v1 on novelty grounds; resubmitting a paper that has *more* null results is a waste of a submission slot.

---

## Weaknesses That Most Pull Down the Score

1. **Identification failure (criterion 5 = 0)**. The P2 event study is the paper's only claim to causal identification, and it does not survive heterogeneity-robust estimation. The author's own Phase B2 memo concedes "cannot be fixed without compiling additional rounds." An adversarial referee treats this as disqualifying for any Second Tier venue.

2. **Third-party validation failed (criterion 3 penalty)**. The Wikipedia-zh correlation was −0.15, not the pre-registered [0.3, 0.7]. The "domain mismatch" explanation is plausible but post-hoc. A strict referee reads this as: the construct does not generalize outside the author-curated text source. This directly undermines the measurement-contribution claim.

3. **Micro-foundation null spun as confirmation (criterion 8 = 0)**. The pre-registration (OSF zmjy5) predicted positive differential; the null is reframed as supporting an upward-signaling model that was not the pre-registered primary model. This is a soft version of HARKing. Sophisticated referees notice.

4. **No supervisor-level data**. The theory is about how supervisors evaluate cadres. Zero evidence in the manuscript uses promotion outcomes, inspection grades, or provincial-superior assessments. The "upward-signaling" label is attached without being tested.

5. **Sole-author single-institution paper targeting an international audience**. Per SOP, Top Field and above require top-30 institutional coauthors. Chongqing Survey Institute is not such an institution. This is a structural barrier the Novelty Score does not directly capture but editors absolutely consider.

---

## How to Move from 3.5 to Next Tier (Second Tier, 5.0+)

Additive improvements required (each must be executed, not merely planned):

1. **Compile Rounds 6–12 CCDI inspections (2016–2020)** to expand treatment-cohort variation from 2 to ~12. Re-run Sun-Abraham; if β(k=0) now survives at p<0.05, criterion 5 moves from 0 to 0.5 and criterion 6 from 0.5 to 1.0. **Effort: 40–60 hours** (archival work + recode).

2. **Build the Xinhua / CNKI 重要报纸 policy-rhetoric third-party corpus** that Phase E2 deferred. The Wikipedia null needs to be counterbalanced by a corpus in the correct domain. If r(VAI_primary, VAI_Xinhua) ∈ [0.3, 0.7], criterion 3 moves from 0.5 to 1.0. **Effort: 20–30 hours** (CARSI scraping + computation).

3. **Add a supervisor-side outcome**. Merge city-year VAI with provincial-level promotion data (Li-Zhou style) or with CCDI discipline-action counts. A single positive β(VAI → next-period promotion probability) would legitimize "upward-signaling" and move criterion 8 from 0 to 0.5 and criterion 2 from 0.5 to 1.0. **Effort: 30–50 hours**.

4. **Find a top-30-institution collaborator**. PKU-NSD, Tsinghua-SPPM, or HKUST-ECON. This is a structural requirement for any Second Tier submission in Chinese political economy, independent of Novelty Score. **Effort: 2–6 weeks** (outreach + integration).

**Realistic ceiling after all four**: 6.0–6.5. That puts RSUE / JHE / JPubE in play but not JUE or higher.

**Minimum viable path to submission at current score (3.5)**: Submit to China Economic Review as-is, with the current manuscript, after a 2-day cleanup of the Phase E2 failure disclosure. Expected outcome: desk-reject probability ~30%, review probability ~70%, conditional accept probability ~25% — reasonable for a Third Tier venue.

---

## Disagreement with Prior Internal Estimate (4.6)

The prior internal estimate of 4.6/10 **double-counted** the Review-vs-Plan finding (once under criterion 1, once under criterion 4, once under criterion 6), **did not penalize** the Phase B2 Sun-Abraham attenuation sharply enough on criterion 5, and **gave full rather than half credit** for the pre-registered null on criterion 7.

Corrected adversarial total: **3.5/10**, a one-tier downgrade. The author should treat this as binding pending successful remediation on at least two of the four items above.

---

*End of S7-2 audit. Pass to research-director for S7 integrated verdict.*
