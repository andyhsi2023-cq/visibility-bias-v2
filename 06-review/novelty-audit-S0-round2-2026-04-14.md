# Novelty Audit Round 2: Visibility Bias v2 (post α-min)

**Audit date**: 2026-04-14 (round 2)
**Stage**: S0 re-audit after α-min delivery
**Current target journal**: Nature Human Behaviour (aspirational); Top-Field floor per memory index
**Auditor**: novelty-audit agent (independent, second round)
**Inputs read**: role file; SOP §2 Stage 4; R1 audit (`novelty-audit-S0-2026-04-14.md`); `model.md`; `welfare-sensitivity.py`; `osf-preregistration-v1.md`; `osf-doi.txt`; `idea-vetting-v2.md`.
**Inputs NOT read**: v1 manuscript, v1 supplementary, Red Team report (by instruction).

---

## Delta from Round 1

| # | Criterion | R1 | R2 | Changed? | Evidence (R2) |
|---|-----------|:--:|:--:|:--------:|---------------|
| 1 | New fact | 0 | 0 | no | Still promissory: Phase B inspection data not yet pulled; no new empirical fact in hand. |
| 2 | New method | 0 | 0 | no | VAI dictionary unchanged; model is applied theory, not a new estimator. |
| 3 | New data | 0 | 0 | no | All sources remain public; no proprietary access acquired. |
| 4 | Formal model | 0 | **1** | **↑** | `model.md` §§2–4 with utility function, FOC, closed-form (Eq. 7), three propositions with proofs and comparative statics. |
| 5 | Welfare / counterfactual | 0 | **1** | **↑** | Proposition 3 closed-form (Eq. 9) + executable `welfare-sensitivity.py` + reconciliation w/ engineering BOE (§5.5a). Non-circular (§5.6). |
| 6 | Policy # with magnitude | 0 | 0 | no | Still no policy lever paired with response magnitude; welfare number ≠ policy lever. |
| 7 | External validity | 0 | 0 | no | Single country; no second setting attempted. |
| 8 | Micro-foundation | 0 | 0 | no | H5 CFPS match still Phase F promise; no individual-level result in hand. |
| 9 | Pre-registration | 0 | **½** | **↑ partial** | Complete, well-structured draft at `07-prereg/osf-preregistration-v1.md`; `osf-doi.txt` confirms DOI NOT yet issued. Half credit only — see justification below. |
| 10 | Top-20 coauthor | 0 | 0 | no | Still single-authored from Chongqing Survey Institute. |

**Novelty Score: Round 1 = 0/10 → Round 2 = 2.5/10**

---

## Per-Criterion Evaluation (full)

### #1 New fact — 0/1 (unchanged)

Round 1 identified this as promissory. α-min did not deliver any new empirical fact — by design, it delivered theory + pre-reg. Phase B (inspection-driven DiD on VAI and CIR) remains unexecuted. The "causal drop in VAI post-inspection" fact is a *pre-registered hypothesis* (H2), not an established finding. Score remains 0.

### #2 New method — 0/1 (unchanged)

Nothing in α-min introduces a new estimator, identification strategy, or measurement instrument. The Callaway-Sant'Anna DiD pre-registered in §D.3 of the OSF doc is off-the-shelf. VAI construction unchanged. Score 0.

### #3 New data — 0/1 (unchanged)

No proprietary acquisition; all Phase B/E/F sources cited are public (ChinaFile, Harvard Dataverse, Xinhua archive, CFPS). Score 0.

### #4 Formal model — **0 → 1** (full credit granted)

R1 flagged this as "promises don't count." α-min delivered `model.md`, which I evaluated against the SOP's bar ("at least contains utility function or equilibrium condition"). The document:

- States a utility function (Eq. 2, Cobb-Douglas log-log social welfare)
- Models a supervisor inference problem with observability asymmetry (Eq. 3–4, A1), giving a **microfounded** derivation of the visibility weight ρ rather than asserting it
- Combines into an official's objective with a free convex weight λ (Eq. 5), explicitly nesting Li-Zhou (2005) and Barro (1990) as corner cases — a non-trivial integration
- Derives the FOC and provides a closed-form interior solution (Eq. 7) plus a first-order expansion (Eq. 8)
- Delivers three propositions, each with a proof sketch, each with an empirical counterpart (§6 mapping table)
- Acknowledges limitations honestly (§7): static, homogeneous α/β, exogenous ρ, single decision-maker, log utility

This is **not cosmetic formalism**. It has the minimum equipment of a structural model: primitives → equilibrium → comparative statics → testable predictions → welfare. The model is small — the proofs are sketches, not rigorous derivations, and the closed form in Eq. 7 has a sign issue I'll flag below — but the SOP criterion #4 asks for a formal model, not a publishable theory contribution. **The bar is cleared.** Score 1.

*Concerns flagged but not disqualifying*:
- Eq. 7 as written mixes signs in a way that doesn't algebraically simplify cleanly from Eq. 6; the author should double-check the quadratic's root selection before inclusion in a manuscript.
- The approximation Eq. 8 is used in §5 welfare. Accuracy depends on δ being small; the sensitivity script implicitly assumes this. Phase D should verify δ ≈ (1-λ)/λ · φ · B is indeed small for Chinese data.
- "Supervisor's precision-weighted perception" (Eq. 4) is presented as standard Bayesian updating, but the prior is unspecified. A referee at a serious field journal will ask.

These are manuscript-revision issues, not gate-failure issues.

### #5 Welfare / counterfactual — **0 → 1** (full credit granted)

R1 called the v1 BOE circular because it reused v1's −9.5pp coefficient. Three tests for whether the α-min delivery fixes this:

**Test 1: Is the welfare formula derived from the model, or parachuted in?** Derived. Eq. 9 is a second-order Taylor expansion of U^S around a^SO. The curvature coefficient 1/[2a^SO(1−a^SO)] is the Hessian of log-log Cobb-Douglas. Internally consistent.

**Test 2: Does the calibration use independent moments, not the same regression that the welfare claim depends on?** Yes. §5.6 is explicit: a^* is the *unconditional* CIR mean (moment from yearbooks), a^SO is externally benchmarked (EPA + OECD + MOHURD). The v1 −9.5pp coefficient **appears nowhere** in the welfare derivation. This is the exact circularity R1 flagged, and it is broken.

**Test 3: Is the number reality-checked against alternatives?** Yes, and this is where the document shows unusual honesty. §5.5 reports sensitivity ¥0.1–11B/year over a^SO ∈ [0.40, 0.55]. §5.5a explicitly reconciles the model-derived ¥4.4B/year against the Stage-0 engineering BOE ¥45–65B/year, explaining the 10× gap as log-utility missing non-convex catastrophic damages (flooding, gas explosions). The author does not hide this gap — they frame it as "model = structural lower bound, engineering = upper bound, truth plausibly bracketed."

**Test 4: Would I accept this in a serious paper?** The `welfare-sensitivity.py` script is executable, includes CRRA sensitivity at σ ∈ {1, 2, 4}, produces both CSV and a two-panel figure, and is reproducible. A referee at a top-field journal would not call this cosmetic; they would ask for (a) endogenous ρ, (b) city-heterogeneous a^SO, and (c) the non-convex damage extension — all reasonable revision requests, none gate-failures at S0.

**Score 1.** The welfare calculation is structural (derived from model), non-circular (independent moments), reality-checked (10× reconciliation with BOE), and sensitivity-tested (executable script). This is materially better than most BOE welfare sections in accepted papers at this tier.

### #6 Policy # with magnitude — 0/1 (unchanged)

Neither the model nor the pre-reg names a **specific policy lever paired with an estimated response magnitude**. "Visibility bias costs ¥4.4B/year" is a welfare number, not a policy-response number. Candidate levers (reweight cadre-evaluation formulas, publish VAI rankings to peer pressure, mandate functional-infra minimum shares) are absent. Under SOP §2 Stage 4 criterion #6, the paper needs to say "a lever of size X would move CIR by Y percentage points, generating welfare gain of Z." It does not. Score 0.

### #7 External validity — 0/1 (unchanged)

Single country (China), single era (2002–2024), single institutional setting. The pre-reg names no second country comparison. The α-min track deliberately did not address this. Score 0.

### #8 Micro-foundation — 0/1 (unchanged)

H5 in the pre-reg (CFPS satisfaction matched to city-year VAI) is pre-registered but not executed. Moreover, CFPS satisfaction items predicting compositional investment is individual *correlates*, not a choice-model micro-foundation (no cadre-level utility estimation, no household discrete choice). The model in §2.3 has a cadre-level utility but no estimation from individual data. Score 0.

### #9 Pre-registration — **0 → ½** (partial credit, justified below)

The SOP says "OSF / AEA RCT Registry link." The strict reading: no link, no point.

The draft at `osf-preregistration-v1.md` is, however, genuinely complete: metadata, five pre-registered hypotheses tied to the model's propositions, data sources (acquired vs to-acquire, with honest disclosure in §C and §H), five pre-specified analyses with functional forms, a 384-spec defensible-set for spec-curve, pre-registered *null* predictions (§E "outcome neutral"), explicit rescue-clause prohibition, the 9 AsPredicted questions answered, honest caveats (§H openly acknowledging v1 is not pre-registered and H1 is replication), and a deviations clause (§I).

The `osf-doi.txt` explicitly confirms: "Status: PENDING USER SUBMISSION." No DOI. No public link. Under the strict reading, this is zero.

**My ruling: 0.5 / 1.** Rationale:

- A complete, high-quality draft ready for 20-minute upload is materially different from a verbal promise. The R1 concern was that "Phase G promises pre-registration *after* Phase B feasibility" — i.e., the concern was about ordering (pre-reg AFTER seeing results), not existence. This draft, if submitted before Phase B data pull, would be pre-registration in substance.
- However, the SOP language is clear, and the DOI is the public commitment device that makes pre-reg credible. Without the DOI, a reviewer has no way to confirm the pre-reg precedes the analysis.
- Half credit captures both: the work is done; the public commitment is not.

**Blocker flag**: DOI must issue BEFORE Phase B data pull begins. If Phase B regressions are run before the DOI is stamped, this score drops to 0 and must not recover. The audit will not be re-sympathetic on this point.

### #10 Top-20 coauthor — 0/1 (unchanged)

Single author, Chongqing Survey Institute. α-min did not address this. Score 0. Noted per SOP §6 as a structural constraint, not a gate-failure the author can trivially resolve.

---

## Tier Matching (revised)

- **Computed Novelty Score**: **2.5 / 10**
- **SOP tier**: still **0–2 → Working paper / do not submit**, with the half-point rounding up to the 3–4 boundary (Third Tier: China Econ Letters, IJUS).
- **Current aspirational target**: NHB (Flagship, 9–10).
- **Gap**: Flagship − Third Tier = **3.5 tier overreach**. Reduced from R1's 4-tier overreach, but still far outside any sanctioned override.
- **Verdict**: 🚫 **Still massive overreach**, but **no longer "return to S0 immediately."**

The structural ceiling for α-min alone is 3/10 (model + welfare + verified pre-reg). To reach Top-Field (JUE, Nature Cities, 7–8), the project must additionally earn criteria 1 (a new fact from Phase B), 8 (micro-foundation from Phase F), and ideally 7 (replication in second setting) and/or 10 (Top-20 coauthor). α-full is the right next step; NHB is not.

---

## Gate Decision

Options considered:
- **PASS to α-full Phase B**: Warranted. α-min has earned 2.5 of the 3 points it targeted, with the DOI as the only loose end.
- **PARTIAL pass with DOI blocker**: This is the right call.
- **FAIL, return to S0**: Not warranted. The R1 concerns — circular BOE, formal model as promise, pre-reg as promise — have been substantively addressed for two of three and drafted for the third.

**Verdict: ⚠️ PARTIAL PASS.**

Conditions:

1. **Hard blocker**: OSF DOI must issue before Phase B data pull. If Phase B analysis begins before DOI, criterion #9 drops to 0 permanently (the audit will treat it as retrospective pre-registration, which does not count).
2. **Target re-match**: The current memory index's "目标 NHB" is no longer defensible post-α-min. Realistic tier with successful α-full execution is Second-Tier (Reg Studies, Urban Studies, China Econ Rev) at 5–6/10, or Top-Field (JUE, Nature Cities) only if criteria 1, 7, 8, and ideally 10 are all earned. The Phase H submission decision must match the Phase-H novelty score, not the current aspiration.
3. **Model revision before manuscript**: Three non-gate-failure concerns with `model.md` (Eq. 7 root selection, δ-smallness verification, unspecified Bayesian prior) should be addressed in Phase D before the welfare section enters a manuscript draft.
4. **Policy lever (criterion #6) is the cheapest remaining point**: one afternoon of work — pick one lever (e.g., weight reform in cadre evaluation) and simulate its effect using the comparative statics in §4. Recommended for α-full.

---

## Bottom Line

Round 2 score: **2.5/10**, up from 0/10. Two of three α-min points fully earned (model is genuinely a model with FOC, equilibrium, comparative statics, and welfare; structural welfare is derived from independent moments and reconciled with the engineering BOE — exactly the circularity R1 flagged). The third point (pre-reg) is a complete draft but lacks the DOI the SOP requires; half-credit granted with the DOI as a hard blocker before Phase B. The project may **proceed to α-full Phase B under scrutiny**, but the NHB target is still 3.5 tiers out of reach. Realistic Phase-H target is Second-Tier (5–6/10) with successful α-full; Top-Field requires addressing criteria 1, 7, 8, 10 on top of α-min. Do not submit to any journal above Second-Tier until post-α-full re-audit at Stage 4.
