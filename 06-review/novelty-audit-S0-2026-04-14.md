# Novelty Audit: Visibility Bias v2 (Stage 0 Gate)

**Audit date**: 2026-04-14
**Stage**: S0 (Idea Vetting gate)
**Current target journal**: TBD (to be determined by this audit)
**Auditor**: novelty-audit agent (independent)
**Input read**: `idea-vetting-v2.md`, `red-team-report-visibility-bias.md`, SOP §2 Stage 0/4, agent role file.
**Input NOT read**: v1 manuscript, v1 supplementary, any empirical results files.

---

## Part 1: Per-Criterion Evaluation

| # | Criterion | Score | Evidence |
|---|-----------|:----:|----------|
| 1 | **New fact** | **0** | Author claims the novel fact is: "central anti-corruption inspections cause VAI to fall → cosmetic-to-functional reallocation." This is a *proposed* chain the paper intends to estimate; the DV (CIR reallocation) and the shock (2013–2016 inspections) are both well-studied in isolation. Chen & Kung (2019, QJE), Wang-Zheng-Wang and numerous follow-ups have exploited inspection timing for local-government outcomes; Bai-Hsieh-Song (BPEA 2016) and Chen-Henderson-Cai (2017) have documented cosmetic-vs-functional distortions. Combining a known shock with a known reallocation, mediated by an index the author built, is application work, not a new first-order fact. The idea-vetting document itself notes the "fact" remains conditional on Phase B–E surviving (Risks 1–4). A new fact cannot be scored on a promise to find one. |
| 2 | **New method** | **0** | VAI is a dictionary-based text index — the exact family of methods the Red Team criticized (Gentzkow-Kelly-Taddy 2019) and that Cao-Lindo-Zhong 2023 / Hassan et al. 2019 / Qin-Strömberg-Wu 2018 have all deployed in variants. The "third-party VAI" fix in Phase E is triangulation, not a new estimator. The inspection-DiD design is a standard staggered-adoption event study (Callaway-Sant'Anna, de Chaisemartin-D'Haultfoeuille are the off-the-shelf tools). No new identification strategy, no new measurement theory. |
| 3 | **New data** | **0** | Work reports are publicly scraped; CFPS is a public survey; central inspections are a public policy timeline; MOHURD/NBS investment data are public. Even if the author's *assembled* panel is not previously published in this exact form, that is compilation, not exclusivity. No proprietary or restricted data source is claimed in the idea-vetting document. |
| 4 | **Formal model** | **0** | Idea-vetting references a "structural welfare calculation" in Phase D and a model sketch the Red Team expert demanded (D3: "half a page and generate comparative statics"), but the idea-vetting document contains **no equations, no utility function, no FOC, no equilibrium condition**. The section on welfare explicitly labels current numbers "BOE, not a structural welfare calculation." Promises do not earn points per the SOP honesty rule. **Score 0 until the model is written.** |
| 5 | **Welfare / counterfactual** | **0** | The ¥55B/year central estimate is *verbal multiplication*: take v1's 9.5pp reallocation coefficient × aggregate investment × an externally-cited damage function (Chen et al. 2021 NatSus). This is the canonical "back-of-envelope that might dissolve" case the audit prompt flagged. Three reasons to withhold the point: (a) it re-uses v1's β=−9.5pp, which may not survive Phase E re-estimation under the very controls the Red Team demanded (document length, boilerplate, province-year FE); (b) it assumes the reallocation is causal, which is what the whole paper is supposed to establish — circular; (c) a genuine welfare number needs a counterfactual allocation rule (social planner? Pareto frontier?), none specified. The author even concedes this: "Phase D will convert this into a model-consistent number." Until converted, score 0. |
| 6 | **Policy # with magnitude** | **0** | The policy anchor section compares the BOE to Wu 2015 and Li-Zhou 2005 aggregates but offers **no specific policy lever with a magnitude**. Candidate levers (redesign cadre evaluation weights? mandate functional-infra minimum shares? publish VAI rankings?) are absent. "Visibility bias costs 1% of urban GDP" is a descriptive magnitude, not a policy lever paired with an estimated response. |
| 7 | **External validity** | **0** | Single country (China), single institutional setting (prefecture-level municipal work reports 2002–2024). No second country, no second era, no out-of-sample subsample comparison promised. The backup Smart-City-pilots design is still Chinese. Fails the ≥2 independent settings bar. |
| 8 | **Micro-foundation** | **0** | The idea-vetting document mentions "matching CFPS respondents to city-year VAI" as Phase F (D7-fix) and flags match quality as unknown (Risk 4). Even if matched, CFPS → city VAI is individual-to-aggregate *correlation*, not a micro-founded behavioral model (no individual utility function, no choice experiment, no decision model of the cadre). Individual-level *data* is not the same as a *micro-foundation*. Score 0. |
| 9 | **Pre-registration** | **0** | No OSF / AEA / AsPredicted link in the idea-vetting document. Phase G promises pre-registration *after* Phase B feasibility. Per the SOP and the prompt's explicit instruction, promises don't count. Score 0 until a live registry link exists. |
| 10 | **Top-20 coauthor** | **0** | Single-authored. The idea-vetting document names no coauthor, lists no outreach plan, and no specific Top-20 scholar is identified. The memory index confirms the user is based at Chongqing Survey Institute, non-elite institution. Score 0. |

**Novelty Score: 0 / 10**

Even granting the most charitable reading of the reframe — where Phase B inspection data exists, VAI survives Phase E controls, and CFPS matches cleanly — the idea-vetting document **as it currently stands** does not provide concrete evidence for any of the ten criteria. Each criterion is either (a) a promise of future work (4, 5, 9), (b) not attempted (7, 10), (c) explicitly conceded as not-yet-done (5 "BOE, not structural"; 4 "will write in Phase C"), or (d) a combination of known elements that does not clear the "new fact / new method / new data" bar (1, 2, 3, 6, 8).

---

## Part 2: Tier Matching

- **Computed tier**: **0–2 → Working paper / do not submit** (per SOP §2 Stage 4 table).
- **Current target**: The idea-vetting document is ambiguous; the memory index and red-team report reveal v1 was aimed at Habitat International, with the reframe's ambition pointed toward **Nature Human Behaviour (NHB)** per `project_visibility_bias.md` ("目标 NHB"). NHB is a Flagship-tier outlet on the SOP table.
- **Gap**: Flagship target vs. computed 0/10 → **+4 tier overreach** (worst-case observed in the SOP).
- **Verdict**: 🚫 **Overreach is extreme.** Even by the most generous scoring — granting provisional credit for criteria 4, 5, and 9 if Phases C, D, G execute successfully — the ceiling is 3/10, still Third-Tier. The gap between the ambition (NHB) and the currently earned novelty is four full tiers. **Must return to S0.**

This is not a close call. The SOP permits overreach by **one** tier with explicit PI + Red Team endorsement; four tiers is outside any sanctioned override.

---

## Part 3: Upgrade Paths

Three most-feasible paths to gain points, ranked by feasibility:

1. **Write the formal model now, not in Phase C (+1, criterion 4).** Half a page: cadre utility U = α·V + (1−α)·F subject to budget B, where V = visible output, F = functional output, α shifts with political scrutiny. Derive FOC, show comparative statics wrt α, derive a testable reduced-form elasticity that maps to the CIR ratio. This is a one-afternoon task; the Red Team methodology expert explicitly said it "could be done in half a page." No reason to defer.

2. **Convert BOE to a counterfactual welfare calculation inside the model (+1, criterion 5).** Once criterion 4 is done, compute welfare as distance from the planner's α* allocation. Requires (a) calibrating α from observed CIR, (b) picking a damage function from Chen et al. 2021 NatSus, (c) integrating. Two to three days of work. Turns a verbal multiplication into a model-consistent number that critics cannot dismiss as circular.

3. **Pre-register before Phase B execution, not after (+1, criterion 9).** Post an AEA-RCT-Registry or OSF pre-analysis plan containing the main inspection-DiD spec, the mediator regression (inspection → VAI → CIR), the seven null outcomes with power calculations, and the spec-curve choice set. One day of work. Directly disarms the Red Team's R3 ("nulls reinterpreted post-hoc") and the methodology expert's D1.

Completing 1–3 in the next week would raise the score to **3/10 → Third-Tier** (China Econ Letters, IJUS, CER in principle). Further upgrades require (a) finding a Top-20 coauthor (criterion 10; structural barrier flagged in SOP §6) and/or (b) adding a second institutional setting — e.g., replicating on Vietnamese or Indonesian municipal documents — to earn criterion 7. Neither is in the idea-vetting plan. Without them, 5/10 (Second Tier) is the realistic ceiling for a successfully-executed reframe; Top Field (JUE / Nature Cities) and Flagship (NHB) remain structurally out of reach.

---

## Part 4: Bottom Line

**Return to S0.** The reframed idea, as written, earns **0/10 Novelty Score**. Every criterion is either promised-for-later, not-attempted, or already-done-elsewhere. The ¥55B welfare BOE is circular (uses v1's contested coefficient); the formal model is a promise; pre-registration is a promise; no Top-20 coauthor exists; external validity is single-country. NHB is four tiers out of reach — the reframe does not make NHB plausible, it makes the old fit (CER / JCE / IJUS) survivable. Before proceeding to Phase B, execute the three upgrade paths above (model, counterfactual, pre-registration) to reach a defensible 3/10, then re-audit. Do not let the emotional weight of a recent desk reject push this paper toward a higher tier than it has earned.
