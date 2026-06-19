# Gap Verification v2 — Visibility Bias in Chinese Urban Governance

**Stage**: 1 (Gap Verification) of the Stage-Gate SOP
**Date**: 2026-04-14
**Author of this diagnosis**: Literature Specialist (adversarial posture)
**Decision to be reached**: proceed / downgrade / kill

---

## Why this redo matters

The v1 Visibility Bias paper was desk-rejected at Habitat International on 2026-04-13 for "lack of sufficient novelty," and the subsequent 3-role Red Team (2026-04-14) confirmed that the novelty problem is not cosmetic. Five published papers — Hassan et al. 2019 QJE, Qin-Strömberg-Wu 2018 AER, Bai-Hsieh-Song 2020 JPubE, Cao-Lindo-Zhong 2023 JUE, and Persson-Zhuravskaya 2016 AEJ:Applied — each cover a piece of what v1 claimed as its own contribution. If v2 cannot articulate a sharp, first-order departure from each, then the reframe is ornamental and the paper will be desk-rejected again. The purpose of this document is *diagnosis, not defense*: for each opponent, I ask whether v2's incremental move is a genuinely new empirical or conceptual object, or whether it is a subset / variant / minor extension of what the opponent already did. One manufactured departure is worse than one honest admission.

---

### Hassan, Hollander, van Lent, Tahoun (2019) *Quarterly Journal of Economics* — "Firm-Level Political Risk: Measurement and Effects"

**What they did** (specific):
- Built a firm-level, quarter-level measure of political risk from conference-call transcripts by counting bigrams within 10 words of risk-synonyms, weighted by a trained political/non-political classifier based on a political-science textbook versus a non-political corpus.
- Validated the measure against earnings-call topic shares, audit-fee loadings, hedging behavior, lobbying, and campaign contributions; showed that firm political risk comoves with aggregate measures (EPU) but has overwhelming idiosyncratic variance (≈91%).
- Showed downstream: high-political-risk firms reduce investment, hire less, lobby more, and donate more to politicians. Released the measure as a public dataset, which has become a de facto standard.

**What they did NOT do / limitations in their coverage**:
- (a) Their object is a *firm-level risk* measure — a variance-type object (exposure to political uncertainty) — not an *attentional composition* object (which of several possible things a government is choosing to emphasize). These are different statistical primitives: risk is about dispersion, attention is about mixture weights.
- (b) Their text corpus is produced by firms describing their environment; it is not produced by the political actor whose behavior is under study. In Chinese municipal work reports, the speaker IS the actor whose capital-allocation behavior is being predicted, which creates a different (and harder) endogeneity structure than HHVT face.
- (c) They do not study capital composition — visible vs. buried, cosmetic vs. functional. The outcome space is private-firm investment, hiring, and political activity; it is not public-sector reallocation across infrastructure categories.

**Our specific departure from them**:

We depart by constructing a *compositional* (mixture-weight) text measure on the *speaker-equals-actor* side of the political economy — where the text is written by the government whose reallocation we study — which their firm-level risk-exposure framework cannot produce because they measure how private agents perceive political uncertainty, not how political principals allocate attention across policy categories.

**Is this departure first-order or auxiliary?**

**AUXILIARY.** The move from "risk exposure" to "attention composition" is a meaningful conceptual shift, but the underlying methodological machinery is the same family: dictionary / bigram / keyword counts over a structured text corpus, validated against hand coding, used as a regressor in a panel. A sophisticated referee will read our VAI construction and say "this is HHVT with a different dictionary and a different corpus," and on the method side they will be essentially correct. The conceptual departure (composition vs. risk) is real but is expressible in one sentence, which is the hallmark of an auxiliary contribution. To elevate this to first-order we would need either (a) a new validation technique not in the HHVT toolkit (e.g., LLM-based semantic embedding comparison with out-of-domain benchmarks) or (b) a structural interpretation of the index that HHVT lack (e.g., derivation from a cadre-utility model).

**Shared-fate risk** — single strongest counter if a referee calls us a minor extension:

Our measure predicts a *compositional* reallocation pattern — specifically, that visible categories go up and functional categories go down *by similar magnitudes*, with total investment unchanged. HHVT's measure cannot in principle generate a compositional prediction because political risk is a scalar exposure, not a mixture. If the referee accepts that "visible vs. functional" is an economically meaningful partition, the compositional prediction is not something HHVT could have produced. This is a real counter but it is narrow.

---

### Qin, Strömberg, Wu (2018) *American Economic Review* — "Media Bias in China"

**What they did** (specific):
- Digitized content from 117 Chinese daily newspapers 1981–2011, measured propaganda-vs-commercial orientation using a supervised classifier on article topics and language, and showed that commercial papers cover corruption and disasters more and propaganda papers cover leaders more.
- Linked bias scores to readership, advertising revenue, and subsequent coverage of political events (anti-corruption drives, protests).
- Established that text content in Chinese official/semi-official documents is (i) measurable at scale, (ii) systematically varies with local political-commercial conditions, and (iii) predicts downstream behavior including local government responsiveness.

**What they did NOT do / limitations in their coverage**:
- (a) Their object is *newspaper content*, produced by media firms with commercial incentives, not *municipal work reports*, produced by local governments as direct political self-reports. The two corpora differ in authorship incentive: newspapers optimize for readers, work reports optimize for superiors.
- (b) Their outcome is *media coverage patterns and readership*, not *physical capital allocation*. They do not link text to infrastructure investment composition. The crossing from "what media say" to "what cities build" is not in their paper.
- (c) Their measurement is calibrated on propaganda vs. commercial — a one-dimensional political-orientation axis — not on cosmetic vs. functional investment priority, which is a policy-composition axis orthogonal to political orientation.

**Our specific departure from them**:

We depart by linking a within-government text measure to a within-government capital-allocation outcome at the prefecture-year level, which their framework cannot produce because their text is produced by commercial/propaganda media firms and their outcomes are media-market variables — not the government's own budget composition.

**Is this departure first-order or auxiliary?**

**FIRST-ORDER**, but contingent. QSW's paper established that Chinese text-at-scale predicts political behavior; we are in the post-QSW world, and the fact that work-report text predicts *something* is no longer novel. Our first-order claim must be that the specific thing it predicts — the *composition* of infrastructure capital — is an economically consequential object that QSW cannot address because their corpus and outcome space do not overlap with this question. This is a first-order claim *if* we can show the compositional reallocation has real welfare or efficiency consequences (which requires a quantified welfare calculation, which v1 did not have). Without the welfare number, this downgrades to auxiliary. Rating this FIRST-ORDER is therefore conditional on v2 delivering the Hsieh-Klenow-style calculation that v1 lacked.

**Shared-fate risk** — single strongest counter:

QSW measure media-firm outputs; we measure government self-reports. The endogeneity structure is fundamentally different: a newspaper reporting on corruption is reporting *about* a government; a work report reporting on greening is reporting *as* a government. The speaker-equals-actor structure changes the identification problem entirely. If a referee argues we are an extension of QSW, the counter is: "QSW cannot study government self-attention because their corpus is not produced by governments." This is a clean counter.

---

### Bai, Hsieh, Song (2020) *Journal of Public Economics* — "Special Deals with Chinese Characteristics"

**What they did** (specific):
- Documented that Chinese local governments make "special deals" with favored firms — tax concessions, subsidized land, regulatory forbearance — and that these deals are concentrated on visible, politically salient projects (industrial parks, showcase developments).
- Built a firm-panel from tax records and showed that special-deal firms receive systematically larger land allocations, lower effective tax rates, and more subsidies; connected these to political-promotion incentives of local leaders.
- Established quantitatively that Chinese cities *do* distort toward visible construction and that the distortion has measurable efficiency costs in TFP terms.

**What they did NOT do / limitations in their coverage**:
- (a) Their unit of analysis is the *firm-deal*, not the *city-year attentional allocation*. They study which firms get which deals; they do not measure the city government's overall attentional composition across the portfolio of infrastructure types.
- (b) They do not distinguish *visible cosmetic* from *visible productive*. Their "visible" is politically salient production (industrial parks that show up in GDP figures); our "visible" is cosmetic finish (greening, façades, road surface) that does not correspond to productive output. These are different sets of projects.
- (c) Their identification is through firm-level variation in political connections; they cannot separate "institutional city-level bias" from "personal connection-driven bias" because their design conflates them.

**Our specific departure from them**:

We depart by studying the *within-city, across-infrastructure-category* allocation between cosmetic-visible (greening, façades) and functional-buried (drainage, water, gas) public investment, which their firm-deal framework cannot produce because their unit is the firm and their visible category is politically-connected production, not publicly-funded cosmetic finish.

**Is this departure first-order or auxiliary?**

**AUXILIARY, leaning toward FIRST-ORDER.** BHS already established the general claim that Chinese cities distort toward visibility. The referee's mental shortcut will be: "Bai-Hsieh-Song already showed this." Our departure is narrower than our pitch suggests — we are studying a different *flavor* of visibility bias (cosmetic public infrastructure rather than politically-connected private investment) within the same general phenomenon that BHS characterized. This is a refinement, not a new phenomenon. For v2 to make this first-order, we would need to show that the cosmetic-vs-functional distinction has consequences BHS cannot see — specifically, a welfare decomposition showing that the cosmetic bias has *larger* efficiency costs per dollar than the industrial-park bias BHS studied, or a policy counterfactual where fixing cosmetic bias requires different instruments than fixing connection bias. Absent that, we are a subset of BHS.

**Shared-fate risk** — single strongest counter:

BHS's visible category is GDP-productive (industrial parks produce output); ours is GDP-cosmetic (greening produces no output). These are economically distinct distortions: BHS describe *whom* cities favor within productive investment; we describe *how cities trade off* between productive and non-productive capital. The latter has different welfare implications (pure waste vs. misdirected productivity) and requires different policy responses (budget restraint vs. connection severance). The counter is: "BHS study capture; we study vanity." Whether the referee accepts this hinges on whether we can quantify the welfare gap, which v1 did not do.

---

### Cao, Lindo, Zhong (2023) *Journal of Urban Economics* — "Social Media Rhetoric and Hate Incidents: Evidence from Chinese Local Government Discourse"

**What they did** (specific):
- Constructed a dictionary-based measure of anti-foreign / nationalist rhetoric in Chinese local-government Weibo posts, 2013–2019, and linked it to downstream anti-foreign incidents and hate-crime proxies at the city level.
- Used dictionary methodology (keyword counts with inter-coder validation) on government-produced Chinese-language text.
- Published in *exactly our target venue*, establishing JUE's methodological precedent for dictionary-text measures of local-government discourse predicting downstream city-level behavior.

**What they did NOT do / limitations in their coverage**:
- (a) Their outcome is social behavior (hate incidents); ours is capital allocation (infrastructure composition). The mechanisms linking text to outcome are different: rhetoric-to-mob-violence versus rhetoric-to-budget-line-items.
- (b) Their corpus is Weibo (fast, reactive, short-form); ours is annual work reports (slow, formal, long-form, vetted). These are different text objects with different production technologies.
- (c) They do not address the cadre-transfer or institutional-vs-personal question; the paper is about *what local governments say* and downstream effects, not about whether the saying reflects the city or the officer.

**Our specific departure from them**:

We depart by applying government-text-dictionary methodology to *public capital allocation composition* rather than to *social-violence outcomes*, and by adding an institutional-vs-personal decomposition via cadre transfers — which their framework could in principle accommodate but did not attempt, so the combination of outcome-space and identification-design is new.

**Is this departure first-order or auxiliary?**

**AUXILIARY.** This is the most dangerous opponent. CLZ sit in the target venue (JUE) using methodologically identical machinery (dictionary counts over local-government Chinese text). A JUE editor reading our submission will immediately see CLZ and categorize us as "another CLZ-style dictionary paper on Chinese local governments." The only substantive difference is the outcome (capital composition vs. hate incidents) and the identification design (cadre transfers vs. their approach, which I recall uses leader characteristics or timing). Neither is a methodological advance; both are applications of their template to a different outcome. To elevate to first-order we would need either (a) a measurement innovation CLZ lack — e.g., LLM-based embedding validation, or a semantic topic-decomposition that dictionary methods cannot do — or (b) an identification innovation CLZ lack, and the cadre-transfer design is precisely the one the Red Team flagged as non-exogenous (Persson-Zhuravskaya). We do not currently have either.

**Shared-fate risk** — single strongest counter:

The strongest counter is outcome novelty: CLZ study social behavior downstream of rhetoric; we study fiscal behavior downstream of attention. If a JUE editor groups us with CLZ because of shared method, our counter is "CLZ cannot produce compositional fiscal predictions because their outcome space does not include capital categories." This is true but feels thin — the editor may reply "then your contribution is applying a known method to a new outcome," which is auxiliary by definition in top field journals. This is our weakest first-order position of the five.

---

### Persson, Zhuravskaya (2016) *AEJ: Applied* — "The Limits of Career Concerns in Federalism: Evidence from China"

**What they did** (specific):
- Analyzed the Chinese cadre promotion system and showed that local officials' career trajectories depend on factional ties and patronage networks, not just on objective GDP performance; in particular, officials with stronger central patronage are promoted regardless of local growth.
- Documented that officer placement across cities is *not* exogenous: officers are sorted to cities on factional, developmental-priority, and timing dimensions.
- Directly attacks the validity of "cadre transfer as natural experiment" designs by showing the assignment mechanism is selection-driven.

**What they did NOT do / limitations in their coverage**:
- (a) They do not study capital *composition*; they study promotion outcomes and growth. They cannot say anything about whether officials sorted to a city shift its fiscal mix.
- (b) They do not use text measures; their data are promotion records and biographies.
- (c) They focus on the *promotion function* (what predicts advancement), not on the *behavioral function* (what cities do differently when they get a different officer). Their result is about careers; it does not directly identify how officer traits map to city policy choices.

**Our specific departure from them**:

We depart by... (intended claim) shifting the identification from officer-transfer exogeneity to within-city persistence, arguing that even if officer assignment is endogenous (as PZ show), the dominance of city fixed effects in explaining VAI variance demonstrates that *the city, not the officer, carries the bias* — which is an argument PZ cannot rebut because they do not decompose behavioral variance into city and officer components using text measures.

**Is this departure first-order or auxiliary?**

**AUXILIARY, and the Red Team already flagged why.** PZ established that officer assignment is non-exogenous; this is a *blocking* result against the v1 identification, not a departure point. The v1 response — "city FE absorbs 96.1% of variance, so the city dominates" — is exactly the wrong inference under endogenous matching. If officers are sorted to cities whose priorities match theirs, you would expect city FE to absorb most of the variance *precisely because the matching is endogenous*, and this absorption is evidence *for* PZ's selection story, not against it. The v1 "institutional not personal" claim is therefore not a departure from PZ; it is an artifact that PZ's framework predicts. To genuinely depart from PZ, v2 would need a mobility-exogeneity test (AKM-style in Card-Heining-Kline 2013 or Bonhomme-Lamadon-Manresa 2019), or an exogenous shock to officer assignment (e.g., a centrally-mandated rotation reform). Without either, we are not above PZ; we are *refuted by* PZ.

**Shared-fate risk** — single strongest counter:

Honestly, we do not have a strong counter. If a referee cites PZ and says "your cadre-transfer design is refuted before it starts," the single best response is to *abandon the transfer design* and re-anchor the institutional-vs-personal claim on a different source of variation (e.g., persistence across officer turnovers, pre-period correlation of city VAI with pre-period officer traits, or an instrument for officer assignment). The counter is not a defense of the current design; it is a concession that the current design needs to be replaced. This is honest and it is also an admission that one of the five departures does not hold.

---

## Final synthesis (400 words)

**Count of FIRST-ORDER vs AUXILIARY departures:**
- Hassan et al. 2019 (QJE): **AUXILIARY**
- Qin-Strömberg-Wu 2018 (AER): **FIRST-ORDER**, conditional on a welfare calculation being delivered in v2
- Bai-Hsieh-Song 2020 (JPubE): **AUXILIARY** (leaning first-order only with welfare quantification)
- Cao-Lindo-Zhong 2023 (JUE): **AUXILIARY**
- Persson-Zhuravskaya 2016 (AEJ:Applied): **AUXILIARY** (in fact worse — they partially refute us)

Score: **1 FIRST-ORDER (conditional) vs 4 AUXILIARY.** Failing threshold is ≥3 auxiliary; we are at 4.

**Strongest threat:** Cao-Lindo-Zhong 2023 JUE. They sit in our target journal using essentially the same methodological machinery (dictionary counts over Chinese local-government text, validated with inter-coder agreement, used in a panel regression). A JUE editor reading our v2 submission will have CLZ on the top of their mental stack and will categorize us as a CLZ-style paper applied to a new outcome. Applied-to-a-new-outcome is an auxiliary contribution at a top field journal, not a first-order one. This is the paper whose shadow we cannot escape by rhetoric alone; we can only escape it by introducing methodological innovation that CLZ lack (LLM embedding validation, supervised classifier benchmarking, structural derivation of the index from a cadre utility model) or by an identification strategy CLZ did not attempt and that survives the PZ critique.

**Secondary threat:** Persson-Zhuravskaya 2016. They do not compete with us on outcome; they *refute* one of our identification strategies. The v1 "cadre transfer natural experiment" is not just weak relative to PZ — it is predicted-away by PZ's selection result. This is not a shared-fate risk; it is an active attack that we walk into.

**Is the gap-verification passable?** No. The SOP threshold is ≥3 of 5 clearly FIRST-ORDER; we have 1 (conditional). Four are AUXILIARY, and one of those four actively undermines an identification strategy we rely on. If we proceed to Phase B with this gap structure, we will produce a paper that a JUE editor can desk-reject in six minutes by citing Cao-Lindo-Zhong and Persson-Zhuravskaya. Habitat International already did the rhetorical version of this; JUE will do the formal version.

**Single recommendation: DOWNGRADE AMBITION TO RSUE.** Do not kill the reframe — the puzzle (cosmetic-vs-functional public capital, with a compositional reallocation result) is real and worth publishing. But it is not a JUE paper as currently positioned. A *Regional Science and Urban Economics* submission, with honest positioning as an empirical refinement of the Bai-Hsieh-Song visibility-distortion literature using text methodology of the Cao-Lindo-Zhong type, extended to public infrastructure composition, is defensible and publishable. A JUE submission is not. Alternatively, if the author insists on JUE, the prerequisite is not more robustness checks; it is (a) a welfare quantification (Hsieh-Klenow style) that lets us make a first-order claim against QSW and BHS, and (b) replacement of the cadre-transfer design with something that survives PZ — which is a six-month re-execution, not a revision. Proceeding to Phase B without one of these is a third desk rejection in a row.
