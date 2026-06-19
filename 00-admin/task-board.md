# Task Board — Visibility Bias v2

**Last updated**: 2026-04-14 (Stage 0 in progress)
**Roadmap**: `00-admin/upgrade-roadmap.md`

---

## Phase A — Reframe (Week 1)

| Task | Owner | Stage gate | Status | Date |
|---|---|---|---|---|
| A1. Sharpen one-sentence finding + welfare BOE | main session | S0 | ✅ Done | 2026-04-14 |
| A2. Gap verification against 5 opponent papers | literature-specialist | S1 | 🔄 In progress | 2026-04-14 |
| A3. Independent novelty-audit on reframe | novelty-audit agent | S0 gate | 🔄 In progress | 2026-04-14 |
| **A-Gate decision** | user | Proceed / Downgrade / Kill | ⏳ Pending A2+A3 | — |

## Phase B — Exogenous Variation (Weeks 2–4)

| Task | Owner | Stage gate | Status |
|---|---|---|---|
| B1. Shock-feasibility evaluation (inspections / smart-city / debt-cap / age-cutoff) | data-analyst | — | ⏳ Blocked by A-Gate |
| B2. Event-study on VAI around top-2 shocks | data-analyst | — | ⏳ |
| B3. Downstream CIR test under shocks | data-analyst | — | ⏳ |

## Phase C — Formal Model (Week 5)

| Task | Owner | Stage gate | Status |
|---|---|---|---|
| C1. 2-equation model with σ_V / σ_F and θ_i | main session | — | ⏳ |
| C2. Comparative statics + propositions | main session | — | ⏳ |
| C3. Map propositions to empirical regressions | main session | — | ⏳ |

## Phase D — Welfare Calculation (Week 6)

| Task | Owner | Stage gate | Status |
|---|---|---|---|
| D1. Structural welfare calc from calibrated model | data-analyst | — | ⏳ |
| D2. Sensitivity analysis | data-analyst | — | ⏳ |

## Phase E — VAI v2 Reconstruction (Weeks 4–6 parallel)

| Task | Owner | Stage gate | Status |
|---|---|---|---|
| E1. Length / boilerplate / selection controls | data-analyst | — | ⏳ |
| E2. Third-party VAI from Xinhua / Weibo | data-analyst | — | ⏳ |
| E3. Placebo-lexicon battery expanded | data-analyst | — | ⏳ |
| E4. Validation report | data-analyst | — | ⏳ |

## Phase F — Individual-Level Evidence (Weeks 7–8)

| Task | Owner | Stage gate | Status |
|---|---|---|---|
| F1. CFPS match to VAI city-years | data-analyst | — | ⏳ |
| F2. Visible vs functional satisfaction regression | data-analyst | — | ⏳ |
| F3. Validation / alternative channels | data-analyst | — | ⏳ |

## Phase G — Pre-registration (Week 2, front-loaded)

| Task | Owner | Stage gate | Status |
|---|---|---|---|
| G1. OSF pre-registration draft (AsPredicted format) | main session | — | ⏳ |
| **G2. USER submits to OSF, records DOI** | **user** | — | ⏳ |

## Phase H — Rewrite Manuscript (Weeks 9–10)

| Task | Owner | Stage gate | Status |
|---|---|---|---|
| H1. New manuscript structure draft | manuscript-writer | S6 | ⏳ |
| H2. Integrate model + welfare + micro | manuscript-writer | S6 | ⏳ |
| H3. Tables & figures v2 | figure-designer | S6 | ⏳ |

## Phase I — S7 Audit (Week 11)

| Task | Owner | Stage gate | Status |
|---|---|---|---|
| I1. Format compliance | peer-reviewer | S7.1 | ⏳ |
| I2. Novelty audit (final) | novelty-audit | S7.2 | ⏳ |
| I3. Red Team final | hostile-referee | S7.3 | ⏳ |
| I4. Editor simulation | hostile-referee | S7.4 | ⏳ |
| **I-Gate** | all four must pass | — | ⏳ |

## Phase J — Submission (Week 12+)

| Task | Owner | Stage gate | Status |
|---|---|---|---|
| J1. Target journal determined by I2 novelty score | user + main | S8 | ⏳ |
| J2. Log in `_meta/rejection-log.yaml` | main | — | ⏳ |
| J3. Monitor for outcome | — | — | ⏳ |

---

## Parked for user-action

| Item | Reason parked |
|---|---|
| Top-20 coauthor outreach | AI cannot do this; user must reach out (B2 track) |
| OSF account creation | User action |
| OSF pre-reg actual submission | User click to submit |

---

## Gate log

| Gate | Date | Verdict | Evidence |
|---|---|---|---|
| **A-Gate round 1** | 2026-04-14 11:10 | **FAIL** | lit-spec 1/5 FIRST-ORDER; novelty-audit 0/10 |
| User decision | 2026-04-14 | execute α-min then α-full | logged in rejection-log.yaml |
| α-min Phase C (model) | 2026-04-14 | ✅ delivered | `03-analysis/model.md` Props 1–3 |
| α-min Phase D (welfare) | 2026-04-14 | ✅ delivered | `03-analysis/welfare-sensitivity.py` + §5 of model.md, central ¥4.4B/yr |
| α-min Phase G (pre-reg draft) | 2026-04-14 | ✅ delivered | `07-prereg/osf-preregistration-v1.md` awaiting user upload for DOI |
| **A-Gate round 2** | 2026-04-14 | **⚠️ PARTIAL PASS** | 2.5/10 (model 1, welfare 1, prereg 0.5); proceed under scrutiny |
| +Phase 6 (policy lever) | 2026-04-14 | ✅ delivered | `03-analysis/policy-levers.md`, ¥50-60B PV package, +1 → 3.5/10 |
| Phase B feasibility | 2026-04-14 | ✅ planned | `03-analysis/phase-B-shock-feasibility.md`; execution blocked on OSF DOI |
| **USER ACTION**: OSF DOI | ✅ 2026-04-14 | DONE | Registration ID zmjy5; DOI 10.17605/OSF.IO/ZMJY5; public immediately; Novelty #9 → 1.0 |
| Projected Novelty Score | 2026-04-14 | **3.0/10** (Third Tier) | Post α-min + policy-lever + DOI; α-full Phase B unblocked |
