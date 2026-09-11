# S7-3 Red Team Report

**Manuscript**: Visibility Bias in Chinese Urban Governance (v1, 2026-04-14)
**Target tier**: Second Tier (RSUE / JHE / CER)
**Novelty**: 4.6/10
**Reviewer**: peer-reviewer agent, three-persona simulation
**Date**: 2026-04-14

---

## Persona 1: Hostile Referee

### Fatal flaws identified

**F1. The Wikipedia null (Phase E2, r = −0.15) is buried, not disclosed.**
Section 3.2.5 (Table 1) does not report Phase E2 at all. The only mention of third-party validation appears in §6.3 Limitation 2 as "Phase E2 construction of a true third-party VAI is *deferred to future work*" — which is flatly false. Phase E2 **was executed** (2.4M char Wikipedia-zh corpus, 282 cities) and **failed** (r = −0.15, CI crosses zero; CIR replication β = +0.02, p = 0.57). The memo (phase-E2-results-memo.md §5) explicitly says "This is a pre-registered null. It goes into the manuscript's deviation/null-results log." The manuscript omits it. This is not transparency — this is **selective non-reporting of a pre-registered test**. A hostile referee would call this out as potentially sanctionable under pre-registration norms. **This alone is desk-reject material at RSUE.**

**F2. The r = 0.93 "independent dictionary" test is circular.**
§3.2.5 acknowledges r = 0.93 overshoots the pre-registered [0.3, 0.7] band, then spins this as "upper bound because same-genre". But the expanded lexicon was built *by the same coder team* from *GWRs not in the training sample* — this is not an independent dictionary; it is a bootstrap within the same corpus and same author's coding intuition. Combine with E-C (bootstrap half-halves r = 0.18) and you have a measure that (i) agrees with itself when you keep the source and coder fixed, (ii) disagrees with itself when you randomly shuffle the lexicon, and (iii) does not correlate with Wikipedia. The most parsimonious interpretation: **VAI is a writing-style artifact of a small number of high-leverage keywords** used consistently by a cohort of municipal speechwriters, not a measure of governance substance.

**F3. Sun-Abraham attenuation (Phase B2) is a methodological smoking gun for Phase B.**
§4.2 reports the TWFE β(k=0) = −0.065, p = 0.011. Phase B2 memo shows the Sun-Abraham robust estimator yields β = **−0.019, p = 0.87** — a 3.4× attenuation and total loss of significance. The manuscript buries this in §6.3 Limitation 1 with language like "significance attenuates in the robust alternative." A hostile referee reads this as: **the pre-registered estimator returns null; the author substituted a discredited estimator (TWFE under staggered treatment) and called it a positive result.** Goodman-Bacon (2021) and Sun-Abraham (2021) have established that TWFE is biased when the pre-registered design is infeasible; the correct conclusion is that P2 is not identified, not that P2 is supported at the 1% level.

**F4. CFPS "theory-consistent null" is post-hoc rationalization.**
The OSF pre-registration (D.1 H5) explicitly predicted **|Cohen's d| ≥ 0.10** in the positive direction with a **differential signature** between visible and functional amenities. The executed result is d ≤ 0.011 with *inverted* sign on Y1. The manuscript (§4.3, §2.5 Corollary C1) rebrands this as a "distinguishing prediction" that the *null itself* affirms the supervisor-signaling channel. But the pre-registration did not say "null affirms theory"; it said "positive d ≥ 0.10 confirms theory." This is a **textbook case of HARK-ing** (Hypothesizing After Results are Known). The Corollary C1 framing was added after Phase F returned null. A referee with access to the OSF timestamp will catch this.

**F5. Welfare calibration is circular and order-of-magnitude unreliable.**
§5 calibrates W = ¥4.4B/yr using (a_i* − a_i^SO)² / [a^SO(1−a^SO)]. But a_i* comes from MOHURD CIR (observed), and a_i^SO is assumed ∈ [0.40, 0.50] based on "MOHURD Urban Construction Design Code" and "OECD averages." The latter two citations are **unverifiable as stated** (the MOHURD code does not specify a fiscal allocation ratio; OECD does not publish a comparable metric). The BOE "¥55B/yr" upper bound uses "replacement cost of deferred functional investment" without any derivation. The 13× range between central and upper estimate is not sensitivity analysis — it is an admission that the calibration is undisciplined. Policy NPV claims (¥50–60B over 10 years) inherit this uncertainty and should be stricken.

**F6. No external validity beyond China, yet the Broader Implications section claims global relevance.**
§6.4 asserts "The policy levers we discuss in §5.4 are not specific to China." The entire identification rests on a Chinese bureaucratic supervision structure (cadre evaluation, CCDI inspection). Not a single non-China data point is offered. The claim that asymmetric observability is "a first-order determinant" in "many real-world public-goods provision problems" is unsupported. Cut this paragraph or the whole paper drifts from "RSUE China paper" to "we claim generalizability we cannot defend."

### Recommended verdict
**Reject.** If forced into revision categories: **major revision with high probability of subsequent rejection**. The Wikipedia omission (F1) and the Sun-Abraham framing (F3) individually justify desk reject at a Second Tier journal that takes pre-registration seriously.

---

## Persona 2: Methodological Expert

### Statistical / identification concerns

**M1. Pre-registration discipline is partial.** Three deviations (D-B-1, D-E-1, D-F-1) are logged, but the post-E2 deviation is missing entirely from the manuscript. Appendix D.2 D-E-1 still says "Phase E2 extension will construct a true third-party VAI from CNKI... Expected timeline: within the R1 revision cycle" — but Phase E2 has already been executed and failed. This is a factually incorrect deviation log submitted to a journal. **Must be corrected before submission.**

**M2. Callaway–Sant'Anna → TWFE substitution is defensible but the reported p-value is not.** With 2 cohorts and all-units-eventually-treated, CS is indeed infeasible. TWFE as a "first-order diagnostic" is acceptable, but the p = 0.011 should be reported alongside Sun-Abraham's p = 0.87 in the **same table in the main text**, not relegated to a limitations discussion. The honest summary is: point estimate negative across estimators; statistical significance depends on estimator choice; causal identification is weak.

**M3. SE clustering is under-specified.** Section 4 says "clustered at the city level" but with 282 cities, 23 years, staggered treatment, and spatial correlation across provinces (inspection rounds are assigned at the province level), the correct clustering is at minimum **two-way city × province-year** or wild cluster bootstrap with G = 31 provinces. Conventional city-clustered SE under-states uncertainty for the P2 event study, where treatment is province-assigned.

**M4. Multiple-testing burden is not addressed.** Across Phases B, E, E2, F, and the specification curve (24 permutations), the manuscript reports at least 7 primary hypothesis tests. Family-wise error rate correction (Bonferroni, Romano-Wolf, or Anderson q-values) is not applied. At α = 0.05 with 7 tests, the probability of at least one false positive is 30%. The only surviving significant results after correction would be P1 (p = 0.002, passes any correction) and the E-B within-document differential (p = 6×10⁻¹⁷, overwhelmingly passes). **P2 (p = 0.011 uncorrected) does not survive Bonferroni at α = 0.05/7 = 0.007.**

**M5. Specification-curve is partially data-mined.** §4.1 says "pre-registered specification curve with 24 permutations." But Appendix D does not list the pre-registered permutations (lexicon thresholds, control subsets, panel restrictions). Without the OSF-archived specification list with timestamps, a referee cannot verify the curve was not optimized post-hoc to produce "24/24 positive, 22/24 significant." The OSF archive must be cited with the exact node containing this specification list.

**M6. Power analysis for the CFPS null is missing.** Claiming an "informative null" requires a power calculation: given N = 62,139 person-years and the realized SE ≈ 0.011, what is the minimum detectable effect size at 80% power? If MDE = 0.02 of an outcome-SD, then the null bounds d < 0.02, which is indeed informative. But the manuscript claims "bounds the maximum possible citizen-popularity effect at roughly 1% of an outcome-SD" without formal power derivation. The equivalence-test (TOST) p < 10⁻⁶ reported in §4.3 is computed against ±0.10 bounds, which is a choice made **after seeing the data** and is larger than the conventional Cohen's d = 0.10 small-effect threshold.

### Recommended verdict
**Major revision.** Methodology is salvageable but requires: (i) honest main-text reporting of both TWFE and Sun-Abraham side-by-side, (ii) multiple-testing correction, (iii) Phase E2 integration, (iv) pre-specified specification-curve audit, (v) formal TOST with d = 0.05 as well as d = 0.10 bounds.

---

## Persona 3: Sympathetic Editor

### What to keep
1. **P1 compositional-substitution result (β = +0.111, p = 0.002; total-invest null p = 0.71).** This is the strongest claim in the paper and survives all robustness checks. It is publishable on its own.
2. **E-B within-document retrospective-vs-prospective differential (Δ = +0.025, t = 8.4, p < 10⁻¹⁶).** Genuinely novel behavioral signature; no plausible alternative explanation; does not depend on external text. This is the paper's most defensible innovation.
3. **The formal cadre-attention model (§2).** Clean Cobb-Douglas derivation, closed-form welfare expression — a useful theoretical contribution even if the calibration is soft.
4. **The pre-registration protocol and transparent deviation log** (after it is corrected to include Phase E2).

### What to cut or rewrite
1. **Cut Corollary C1 as a "distinguishing prediction."** Reframe CFPS as an **exploratory** supplementary analysis, not a theory-affirming null. The OSF-registered H5 predicted d ≥ 0.10 positive; it failed. Do not reverse-engineer a success narrative.
2. **Cut or radically downsize §5 welfare calibration.** The ¥4.4B / ¥55B range is not defensible. Report the compositional distortion (a* − a^SO) = 0.088 with CI; let readers do the calibration.
3. **Cut §5.4 policy levers and §6.4 Broader Implications.** Neither is supported by the identification.
4. **Rewrite §4.2 and §6.3 Limitation 1** to report TWFE and Sun-Abraham side-by-side in the main text. Concede that P2 is "suggestive, not identified."
5. **Add §3.2.6** transparently reporting the Phase E2 Wikipedia null with the domain-mismatch interpretation. Hiding it is the single largest submission risk.

### Minimum viable submission plan
**Option A (recommended): Split into a methods paper.**
Title: *"Measuring Rhetorical Visibility Bias in Chinese Municipal Government Work Reports: A Text-Based Instrument with Within-Document Validation."*
Target: *Journal of Chinese Economic and Business Studies* or *China Economic Review* methods-track.
Content: §2 (model, abbreviated), §3 (VAI construction), E-A/E-B/E-C/E-D + honest Phase E2 reporting, §4.1 (P1 only), §4.4.1 (E-B behavioral signature). Drop P2, P3, C1, welfare calibration.
Novelty: ~5.0/10 (measurement contribution is concrete and novel).
Desk-reject probability: ~30%.

**Option B: Keep the full paper but demote target tier.**
Target: *China Economic Review* or *Journal of Comparative Economics*.
Required revisions: F1 (Phase E2 disclosure), F3 (side-by-side B/B2 reporting), F4 (drop C1 Corollary framing), F5 (strip welfare quantification to qualitative discussion), F6 (cut §6.4).
Novelty: stays ~4.6/10.
Desk-reject probability at CER: ~45%. At JCE: ~55%.

**Option C (discouraged): Submit as-is to RSUE/JHE.**
Desk-reject probability: **75–85%**. Editors at RSUE read pre-registration OSF records; they will find the E2 null. JHE has limited appetite for China-only text-analysis papers.

### Realistic target journal given current state
**China Economic Review** (after Option B revisions). CER has published text-analysis papers on Chinese policy corpora, accepts China-only identification, and has a 3–4 month review cycle. Back-up: *Journal of Chinese Economic and Business Studies*, *Journal of Asian Economics*. Do **not** submit to RSUE, JHE, or JUE with current state.

### Projected desk-reject probability
- RSUE as-is: **80%**
- JHE as-is: **75%**
- CER as-is: **55%**
- CER after Option B fixes: **25–30%**
- Methods split (Option A) at JCEBS/CER-methods: **20–25%**

---

## Synthesis: what MUST be fixed before submission

### P0 — Blockers (submission is unethical/reckless without these)

1. **Integrate Phase E2 Wikipedia null into §3.2 and update Appendix D D-E-1.** The current manuscript falsely states the test was deferred. Without this, submission risks a pre-registration-integrity complaint. **Effort: 4 hours.**

2. **Correct Appendix D D-E-1 remediation language** (Phase E2 was executed, not planned). **Effort: 30 minutes.**

3. **Report TWFE and Sun-Abraham side-by-side in §4.2 Table 3, main text.** Rewrite §4.2 closing paragraph to concede P2 is "suggestive, not decisively identified." **Effort: 3 hours.**

### P1 — High priority (desk-reject risk if missed)

4. **Drop Corollary C1 framing.** Reframe CFPS as exploratory supplementary analysis. Remove the claim "null affirms theory." Present as "visibility bias mechanism does not detectably reach citizens at d ≥ 0.10 bounds." **Effort: 4 hours (rewrites in §2.5, §4.3, §6.1).**

5. **Apply multiple-testing correction** (Romano-Wolf or Bonferroni) across P1/P2/C1/E-B and report corrected p-values. Add to Table 6. **Effort: 2 hours.**

6. **Two-way or province-clustered SE for Phase B event study.** Add row to Table 3 with robust SE alternative. **Effort: 3 hours.**

7. **Formal power / MDE calculation for CFPS null.** Add paragraph to §4.3 with MDE derivation. **Effort: 2 hours.**

### P2 — Medium priority (reviewer-response quality)

8. **Downsize welfare calibration (§5).** Keep the compositional distortion estimate; report welfare loss as a single sensitivity figure with a ±10× uncertainty band; remove the ¥50–60B policy NPV claim. **Effort: 6 hours.**

9. **Cut §6.4 Broader Implications** or restrict to one sentence. **Effort: 1 hour.**

10. **Archive the exact 24-permutation specification list on OSF with timestamp verification.** Cite the specific OSF node in §4.1. **Effort: 2 hours.**

### P3 — Nice to have

11. Rewrite abstract to lead with P1 + E-B (strongest evidence), demote P2 and C1. **Effort: 2 hours.**

12. Decide Option A (split) vs Option B (demote tier) vs wait for CARSI Xinhua access. **Effort: PI decision, 1 hour.**

### Total effort for safe submission (P0 + P1)
**~18 hours of focused revision**, followed by novelty-audit re-scoring before S7-4.

### Final recommendation
**HOLD submission.** Current rejection log (7 desk rejects in 30 days) indicates a pattern of submitting before P0 blockers are resolved. Completing P0 + P1 and demoting the target to CER (Option B) brings desk-reject probability from ~80% to ~25–30%. This is the only defensible path. Submitting to RSUE/JHE with the E2 Wikipedia null hidden would be the 8th rejection, and would materially damage the pre-registration track record of future submissions from this lab.

---

*End of S7-3 Red Team Report. Word count: ~2,450.*
