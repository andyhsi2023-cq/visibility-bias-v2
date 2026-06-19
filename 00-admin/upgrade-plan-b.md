# B-Upgrade Plan: Path from Novelty 3.5 → Second Tier (5.5–6.5)

**Project**: Visibility Bias v2
**Plan date**: 2026-04-14
**Trigger**: S7-2 Novelty audit returned 3.5/10 (adversarial); S7-4 Editor simulation recommended CER Third Tier as realistic target with current state.
**Goal**: reach Novelty 5.5–6.5 to enable legitimate RSUE/JHE submission.
**Estimated timeline**: 4–6 weeks of intensive work + 2–6 weeks of coauthor outreach (overlapping).

---

## Constraint: Why current state blocks Second Tier

The three specific weaknesses from S7-2 Novelty audit:

1. **Criterion 5 (clean identification) = 0.0**. P2 inspection shock attenuates under Sun-Abraham heterogeneity-robust estimator. Only 5 cohorts spanning 1.5 years.
2. **Criterion 3 (new data) = 0.5**. Wikipedia-zh third-party validation FAILED; true policy-rhetoric corpus (Xinhua/CNKI) not yet built.
3. **Criterion 8 (micro-foundation) = 0.0**. CFPS amenity-specific items unavailable; substitute null reframed as exploratory.

Any credible plan to move to Second Tier must fix at least two of these three and add institutional credibility.

---

## Four Upgrade Tracks

### TRACK 1 — Expand CCDI rounds to 6–12 (2016–2020)

**Novelty impact**: +1.0 on Criterion 5 (clean identification); +0.3 on Criterion 6 (robustness).

**Scope**:
- Compile Rounds 6 through 12 inspection assignments (2016–2020), each covering provinces + SOEs.
- Additional 7 rounds × 5-12 provinces each ≈ 50-80 new province-round observations.
- Reach approximately 10 distinct cohorts spanning 2013-06 through 2020-12 — a 7-year window rather than 1.5 years.

**Expected outcomes**:
- Sun-Abraham estimator becomes identifiable with wide temporal variation.
- Callaway-Sant'Anna (pre-registered original estimator) becomes feasible again because never-yet-treated cohorts provide controls through 2020.
- Event-study dynamic effects can be estimated to k=+5 with adequate precision.

**Effort estimate**: 15–25 hours
- CCDI press release scraping: 6 hours (public data)
- Harvard Dataverse cross-validation with Chen-Kung (2024) replication: 3 hours
- Panel construction: 4 hours
- Re-running all DiD specifications: 4 hours
- Writing updated §4.2: 4 hours
- Robustness battery: 4 hours

**Risk**: Low. Data is publicly available. Main risk is that expanded sample attenuates effect further rather than strengthening it. Contingency: if expanded effect is still insignificant under robust estimators, report it transparently and position P2 as definitively null, which still updates the field's understanding.

**Deliverable**: Updated `03-analysis/phase-B/` with 2013-2020 panel; revised Table 3; new §4.2 paragraph; updated deviation log D-B-1.

---

### TRACK 2 — Build Xinhua local-policy news corpus

**Novelty impact**: +1.0 on Criterion 3 (new data); +0.5 on Criterion 4 (new measurement).

**Scope**:
- Target: 282 cities × 2010–2024 window, Xinhua News local sections or People's Daily local bureau news.
- Approach A (preferred): CARSI-authenticated access to CNKI 重要报纸 database (万方/CNKI). Search by city name in "政务" or "新闻" sections.
- Approach B (fallback): Xinhua News online archive via web scraping with explicit User-Agent identification as academic research.

**Expected corpus**: 2,000–5,000 articles per city × 15 years ≈ 800K–1.5M total articles. Manageable storage.

**Validation test**:
- Compute VAI_news on the Xinhua corpus using same V_ORIG + F_ORIG.
- Expected correlation with VAI_primary: r ∈ [0.30, 0.60] (the pre-registered band).
- Expected CIR replication: β(VAI_news → CIR) > 0, p < 5%.
- If correlation is in band: H4 succeeds; criterion 3 earns +1.0.
- If correlation is null/negative: H4 fails again; criterion 3 earns -0.2 (worse than current 0.5).

**Effort estimate**: 25–40 hours
- CARSI authentication + database navigation: 4 hours
- Scraping infrastructure (respecting rate limits): 10 hours
- Text cleaning and city-name disambiguation: 6 hours
- VAI computation: 2 hours
- Correlation and replication tests: 4 hours
- Writing updated §3.2 and Appendix: 6 hours

**Risk**: Medium. CARSI access may have usage limits; CNKI may throttle aggressive scrapers. Contingency: if CARSI blocks, switch to People's Daily online archive (public, slower). Worst case: build a smaller corpus of 50 representative cities rather than all 282.

**Deliverable**: Updated `02-data/raw/xinhua_news/` and `03-analysis/phase-E3/`; revised §3.2 construct-validity table; new figure; updated Appendix D-E-2 (success or second-failure disclosure).

---

### TRACK 3 — Add supervisor-side promotion outcome

**Novelty impact**: +0.5 on Criterion 2 (new mechanism, supervisor channel is the theoretical claim but not yet empirically demonstrated); +0.5 on Criterion 8 (micro-foundation, at the supervisor level).

**Scope**:
- Link prefectural party-secretary and mayor panels (CPED + hand-compiled) to subsequent promotion outcomes (1-year, 3-year, 5-year post-tenure-end).
- Test: within-city variation in VAI during leader tenure predicts leader's subsequent promotion.
- Positive β would confirm the upward-signaling channel of the theoretical model (visibility rhetoric → supervisor reward).

**Pre-registration addendum required**: This is a new test not in OSF ZMJY5. Must file an amendment (allowable per OSF platform) or add as explicitly exploratory with clear disclosure.

**Effort estimate**: 20–30 hours
- CPED cross-linking with existing mayor/secretary panels: 6 hours
- Promotion outcome construction (position-tier coding): 4 hours
- Within-city within-tenure panel construction: 4 hours
- Regression specifications: 4 hours
- Robustness (control for observable ability via prior tenure length, city-stage FE): 6 hours
- Writing updated §4 results and §6.1 strong-claim upgrade: 6 hours

**Risk**: Medium. Promotion outcomes can be noisy; direction of the effect may go either way. Contingency: null result here would NOT force paper rejection but would make the "supervisor channel" claim less convincing. Plan for publication under either outcome with appropriate framing.

**Deliverable**: New `03-analysis/phase-G/promotion_outcomes.py`; new Table in §4 with promotion regression; revised Corollary C1 framing to incorporate supervisor-side evidence.

---

### TRACK 4 — Institutional collaborator / co-author

**Novelty impact**: +0.5–1.0 on perceived credibility (not a formal Novelty criterion but strongly affects desk-review outcome at Second Tier).

**Scope**:
- Identify 1–2 potential collaborators from top-30 Chinese institutions (Peking, Tsinghua, Fudan, Shanghai Jiao Tong, Zhejiang, CUHK, HKUST) with prior work on Chinese urban political economy.
- Preferred candidates: authors of Li-Zhou (2005), Yao-Zhang (2015), Lei-Zhou (2022), or Jiang (2018).
- Outreach strategy: send current manuscript with specific ask — "Would you be interested in providing critical feedback or serving as co-author given our interest in [specific research question]?"

**Effort estimate**: 2–6 weeks of outreach cycle (asynchronous).

**Risk**: High variance. May receive no response. Contingency: even a declined-coauthor-but-willing-to-provide-feedback arrangement adds credibility; acknowledge in Acknowledgments section.

**Deliverable**: Either a co-author listed on title page, or credited reviewer in Acknowledgments with institutional affiliation.

---

## Integrated Upgrade Sequence (optimal order)

**Phase 1 (Week 1–2): Low-risk high-value tracks in parallel**
- Track 1 CCDI expansion (publicly available data, can start immediately)
- Track 4 collaborator outreach (asynchronous; send 3–5 emails in first week)

**Phase 2 (Week 2–4): Data-access-dependent tracks**
- Track 3 supervisor-promotion outcomes (start once Track 1 panel is ready)
- Track 2 Xinhua corpus (requires CARSI; start when authenticated)

**Phase 3 (Week 4–5): Integration and rewrite**
- Update manuscript with new findings
- Re-run S7 full audit cycle
- Revise target-journal decision based on new Novelty score

**Phase 4 (Week 5–6): Submission**
- If Novelty ≥ 5.5: submit to RSUE / JHE (Second Tier)
- If Novelty still < 5.5 after best-effort upgrade: submit to CER (Third Tier, de-risked)

---

## Projected Novelty After Upgrade

| Scenario | Tracks completed | Projected Novelty |
|---|---|---:|
| Track 1 only (CCDI expansion) | Partial B upgrade | 4.0–4.5 (still Third Tier) |
| Track 1 + Track 3 (promotion) | Both internal tracks | 4.5–5.0 (CER/Cities high end) |
| Track 1 + Track 2 (Xinhua success) | Causal + external validity | 5.5–6.0 (RSUE / JHE feasible) |
| Track 1 + Track 2 + Track 3 | All internal tracks | **6.0–6.5** (RSUE / JHE strong) |
| All four + strong coauthor | Full upgrade | **6.5–7.0** (top of Second Tier; JUE possible) |

**Decision rule**: do not submit to a Second Tier journal until Novelty ≥ 5.5 under adversarial re-scoring by independent Novelty audit agent.

---

## What to do in the meantime

**Do NOT submit manuscript v2 (with P0 fixes) immediately**, even though it is now format-ready and deviation-honest. The current state (Novelty ~3.8 under adversarial scoring after P0 fixes) means:
- CER: ~28% desk-reject probability (acceptable for a deliberate "consume-a-slot" decision, not for a strategic advance)
- Anywhere else Second Tier: >60% desk-reject

**Instead**: invest the next 4–6 weeks in the upgrade plan above. This is consistent with SOP §S0 Stage 0 Idea Vetting's principle that a properly-scoped paper is worth delaying for.

**Monitoring**: file weekly progress memos in `00-admin/upgrade-progress-YYYY-MM-DD.md` so that the decision to submit or further delay can be made on defensible evidence.

---

## Reject-this-plan decision criteria

Do NOT pursue this B-Upgrade path if:
- Any of the following happen in the first week:
  - No coauthor reply from top-30 institution after 8 outreach emails
  - CCDI Rounds 6–12 data is corrupt or incomplete (unlikely)
  - Track 2 fails again on Xinhua with r < 0.20 (would mean the lexicon is truly source-specific and the paper's scope claim is fatally narrow)

If any of these triggers: revert to submitting v2 to CER immediately, accept the 28% desk-reject probability, and treat the paper as a published data-construction paper rather than a Second Tier contribution.

---

*End of plan. Task board will track progress per week.*
