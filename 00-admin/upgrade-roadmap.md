# Visibility Bias v2 — Full Upgrade Roadmap

**Established**: 2026-04-14
**Predecessor**: `~/Desktop/Research/visibility-bias-upgrade/` (v1, target JUE, Red-Teamed and found non-ready)
**Framework**: Stage-Gate SOP v1.0 (`~/Desktop/Research/_meta/research-sop.md`)
**Ambition**: Novelty Score 3/10 → **6–8/10**
**Total timeline**: **8–14 weeks** (B1 path: 8–10 wk; B2 path: +4 wk for coauthor)

---

## The 7 architectural defects identified by the 2026-04-14 Red Team

Every upgrade below maps to a specific defect.

| # | Defect (from `_meta/red-team-report-visibility-bias.md`) | Severity |
|---|---|---|
| D1 | Text-outcome common-source bias (VAI and CIR both from same city) | **Fatal** |
| D2 | Officer transfers not exogenous (Persson-Zhuravskaya 2016) | **Fatal** |
| D3 | No formal model, no comparative statics, no welfare calc | **Fatal** |
| D4 | Post-hoc null reinterpretation without pre-registration or power analysis | Major |
| D5 | VAI dictionary not length/boilerplate-controlled; segment selection endogenous | Major |
| D6 | Overlap with Hassan et al. 2019, Qin-Strömberg-Wu 2018, Bai-Hsieh-Song 2020 not addressed | Major |
| D7 | No individual-level / micro-foundation | Major |
| D8 | Single-author + non-elite institution (structural, not content) | Major |

---

## Two upgrade tracks

### Track B1 — Full AI-doable upgrade (Novelty target 6/10 → RSUE / CER / JHE)

Addresses D1–D7 (all non-structural defects). Projected duration **8–10 weeks**.

### Track B2 — B1 + real-human coauthor (Novelty target 7-8/10 → JUE / JPubE)

Adds D8 fix. User must recruit a real top-20 economist. Projected duration **12–14 weeks**.

---

## Phase-by-Phase Plan (Track B1)

### Phase A. Reframe (Week 1)

**Stage 0 — Idea Vetting (redo)**
- Sharpen the one-sentence finding. Current: "visibility bias exists and is institutional." Needs: a *causal* sentence with magnitude.
- Draft: *"Exogenous shocks to official career incentives (e.g., anti-corruption inspection) shift city-level Visibility Attention Index by β, but the persistent cross-city VAI gap is 4× as large, implying that visibility bias is primarily a fiscal-institutional property rather than a career-incentive response."*

**Stage 1 — Gap Verification (redo)**
- For each of Hassan et al. 2019 (firm 10-K text), Qin-Strömberg-Wu 2018 (media coverage), Bai-Hsieh-Song 2020 (land politics), Cao-Lindo-Zhong 2023 (local gov social media), Persson-Zhuravskaya 2016 (provincial GDP promotion), write:
  - (a) exactly what they did
  - (b) exactly what we do that they didn't
  - (c) whether (b) is first-order or auxiliary
- Expected outcome: either a sharp 1-sentence departure per paper, or we downgrade the ambition.

**Deliverables:**
- `00-admin/idea-vetting-v2.md`
- `01-literature/gap-verification-v2.md`
- Gate decision: proceed to Phase B, or downgrade to Second Tier without further upgrade.

### Phase B. Exogenous Variation (Weeks 2–4)

**D2 fix**: find a genuine exogenous shock to municipal governance that plausibly affects visibility attention.

Candidate shocks (ranked by feasibility given our existing data):

| Shock | Data source | Identification strategy | Expected VAI effect |
|---|---|---|---|
| **Xi anti-corruption inspections (central 中央巡视组)** | ChinaFile + Harvard Dataverse; 2013–2016 timing | Staggered DiD, 31 provinces | -10 to -15% in VAI (defensive) |
| **2014 new-style urbanization policy** | State Council doc | Interrupted time series | Mixed |
| **Cadre age-limit reform (65→60 for subnational)** | CPED | Age-cutoff RDD + event study | Channel-specific |
| **Smart-city pilot designation** | MOHURD | Staggered DiD | Visible ↑ |
| **Local debt cap (2015 新预算法)** | CBRC | Pre/post | Visible ↓ (constrained) |

**Action plan:**
1. Data-analyst agent runs feasibility check on each: (a) shock assignment independence; (b) pre-trends; (c) power given N=282 cities.
2. Pick top 2 candidates.
3. Run event-study on VAI around shock date.
4. Evaluate: do shock-induced VAI movements predict downstream composition changes (CIR) in the same direction?

**Deliverables:**
- `03-analysis/exogenous-shock-feasibility.md`
- `03-analysis/shock-event-studies/` (Python scripts)
- `04-figures/shock-event-study.pdf`

### Phase C. Formal Model (Week 5)

**D3 fix**: minimal model that yields testable predictions.

**Two-period model sketch:**
- Officials choose investment allocation $a \in \{V, F\}$ (visible vs functional)
- Supervisor observes a noisy signal of output. Signal precision: $\sigma_V < \sigma_F$ (visible is more legible)
- Cities differ in exogenous fiscal capacity $\theta_i$ (land finance channel)
- **Proposition 1**: Optimal visible share $a_V^* = f(\sigma_F/\sigma_V, \theta_i)$, increasing in $\theta_i$
- **Proposition 2**: Welfare loss $W = g(a_V^* - a_V^{social})$, scales with $\theta_i$

Map propositions to our empirical:
- Prop 1 → baseline β and its heterogeneity in $\theta$ (land-dependence)
- Prop 2 → welfare calculation in Phase D

**Deliverables:**
- `03-analysis/model.md` with derivations
- `04-figures/model-comparative-statics.pdf`

### Phase D. Welfare Calculation (Week 6)

**D3 fix (part 2)**: counterfactual welfare estimate.

Approach:
1. Estimate the "visibility premium" — how much more a unit of VAI raises visible vs functional investment.
2. Take engineering estimates of functional-infrastructure depreciation costs (e.g., urban flooding damage estimates, sewer overflow costs from EPA / IWA benchmarks).
3. Back-of-envelope: if visibility bias causes a 5-10% underprovision of functional infrastructure nationally, what's the present-value damage?

Candidate reference: Chen-Xi 2020 (*Nature Sustainability*) on Chinese flood damage; or Han-Kung 2015 on fiscal inefficiency.

**Target output**: "Visibility bias in Chinese municipal capital allocation implies approximately ¥XXX billion (or 0.YY% of municipal GDP) in avoidable infrastructure-failure costs annually."

**Deliverables:**
- `03-analysis/welfare-calc.md`
- Sensitivity analysis in `03-analysis/welfare-sensitivity.py`

### Phase E. VAI Re-construction with Controls (Weeks 4–6, parallel)

**D5 fix**: 
- Control for document length, boilerplate density, section-length
- Validate against independent text source (e.g., Xinhua news coverage of the city, or provincial government descriptions of the city)
- Placebo lexicons (expanded set) + cross-lexicon correlation matrix

**D1 fix (partial)**: build a **third-party VAI** — measure visibility attention *about* the city, from outside (media, social media, provincial docs). If third-party VAI also predicts CIR, the common-source bias concern weakens.

**Deliverables:**
- `02-data/processed/vai_v2_panel.csv` with new controls
- `03-analysis/vai-v2-validation.md`
- Third-party VAI from Xinhua / Weibo corpus

### Phase F. Individual-Level Evidence (Weeks 7–8)

**D7 fix**: micro-foundation.

Option 1 — **CFPS individual perception**:
- CFPS 2014+ has questions on resident satisfaction with infrastructure
- Match residents in high-VAI vs low-VAI cities
- Test: are visible-infra satisfaction scores higher in high-VAI cities? And functional-infra satisfaction lower?

Option 2 — **Officer behavior traces**:
- Hand-collect or use existing data on officers' site-visit reports (inspection itineraries)
- Test: do officers from high-VAI cities visit more visible sites?

Option 3 — **Media coverage of officer achievements**:
- Xinhua / People's Daily local-government coverage
- Content-code achievements into visible/functional
- Test: officer from high-VAI city gets relatively more visible-coverage

**Deliverables:**
- Pick 1 of 3 (CFPS is cheapest).
- `03-analysis/micro-evidence.md`
- `04-figures/micro-evidence.pdf`

### Phase G. Pre-Registration (Week 2, front-loaded)

**D4 fix**: register spec-curve design before running Phase E–F.

- Draft OSF pre-registration document
- Specify: hypothesis, data, all "defensible specifications" for spec curve, analysis plan
- **User action**: submit to OSF and save DOI

**Deliverable**: `07-prereg/osf-draft-v1.md` + `07-prereg/osf-doi.txt` (after user submission)

### Phase H. Rewrite Manuscript (Weeks 9–10)

- Stage 6 per SOP
- New title reflecting causal frame
- Sections restructured: Intro → Background → Data → **Model** → Strategy → Results → **Welfare** → **Micro** → Robustness → Conclusion
- Word target: 10,000–11,500 (Second Tier expected)

**Deliverable**: `05-manuscript/manuscript_v2.md`

### Phase I. S7 Audit (Week 11)

4-layer audit: format + novelty-audit + hostile-referee + editor-simulation.

**Gate**: only submit if all 4 pass. If any fail, return to Phase B-H as needed.

### Phase J. Submit (Week 12+)

Target (pending novelty-audit result):
- If Novelty ≥ 7 (unlikely without coauthor): JUE / JPubE
- If Novelty 5–6: RSUE / China Economic Review
- If Novelty 4: JHE / Cities

Log in `_meta/rejection-log.yaml`.

---

## What I'll do in **this** conversation

Stage 0 and Stage 1 — the reframe. Everything else requires deeper work that I'll pick up in future sessions.

This conversation's output:
1. `00-admin/idea-vetting-v2.md` — sharpened one-sentence finding + welfare BOE
2. `01-literature/gap-verification-v2.md` — literal 1-sentence departures from all 5 opponent papers
3. `00-admin/task-board.md` — tracks the 8-week plan

Then you decide: proceed with Phase B, or first try to find a coauthor (which makes the upgrade 12-week, B2 track)?

---

## Parking items (require user action, not AI)

| Item | Who | When |
|---|---|---|
| OSF account + pre-registration submission | User | After Phase G draft |
| Top-20 coauthor outreach | User | Anytime; ideally before Phase H |
| Mendeley Data replication upload | User | After conditional acceptance |

---

*End of roadmap v1.0*
