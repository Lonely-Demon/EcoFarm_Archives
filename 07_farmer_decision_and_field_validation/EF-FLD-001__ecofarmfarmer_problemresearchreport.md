# EcoFarm Farmer-Problem Research Report

**Geography:** Namakkal / Kongu belt, Tamil Nadu, India  
**Initial segment hypothesis:** Small- and medium-holding farmers, with groundnut as a starting hypothesis rather than a conclusion  
**Research status:** Desk research plus field-research design; no first-party EcoFarm farmer validation has been completed  
**Prepared by:** Manus AI  
**Access date:** 13 August 2026

> **Decision brief:** For small, predominantly rainfed Namakkal farmers who make groundnut or comparable dryland crop decisions, EcoFarm should test support for the **sowing and early-season response decision** because local agriculture is materially exposed to rainfall and water variability, the decision has a short and observable action window, and the district already contains overlapping information channels whose gap may be translation, timing, trust, and feasibility rather than simple information absence. The bounded workflow should compare a few feasible actions, show source and uncertainty, record the farmer’s actual choice, and measure whether the decision becomes more timely and better explained—not whether EcoFarm predicts profit.

## 1. Executive answer

The desk evidence does not justify launching a generic “AI farming app,” a broad agricultural operating system, a guaranteed-procurement service, or a profit-prediction product. Namakkal has formal agriculture, KVK, weather, regulated-market, e-NAM, insurance, dealer, trader, and farmer-to-farmer channels. The strategic question is therefore narrower: **does a defined farmer segment face a recurring decision where existing information is too late, too general, too difficult to compare, or insufficiently trusted to support action?**

Three candidate problems are credible enough to take into fieldwork. The first is **rainfed crop establishment and early-season response**, especially whether to sow, wait, re-sow, or adjust after uncertain rainfall. The district administration reports approximately 80,598 hectares of rainfed cultivated area against about 60,939 hectares irrigated, with normal annual rainfall of 716.54 mm.[^1] The Statistical Handbook also shows a very large number of small operational holdings: 120,087 holdings up to 0.5 hectares, 53,265 between 0.5 and 1 hectare, and 45,067 between 1 and 2 hectares in its provisional Agricultural Census table.[^2] These facts support a segment hypothesis, not a conclusion about unmet demand.

The second is **in-season response to pest, disease, weed, or crop-moisture signals**. This decision is potentially more frequent and more measurable than crop choice, but it has a greater safety burden. Incorrect diagnosis can cause unnecessary chemical use, crop damage, resistance, health risk, and financial loss. KVK Namakkal already lists integrated crop management, groundnut activities, drought mitigation, and ICT-enabled farm advisories.[^3] EcoFarm should therefore test whether it can improve triage, evidence capture, and escalation—not provide autonomous pesticide prescriptions.

The third is **harvest, storage, and sale timing**. This is financially consequential, but market decisions are constrained by cash needs, quality, transport, storage, buyer relationships, debt, and existing regulated-market channels. Tamil Nadu’s e-NAM programme supports electronic trading, assaying, market access, and SMS dissemination, while the Namakkal handbook lists six regulated-market locations and multiple crop categories.[^4] TNAU also publishes crop-price advisories, including a 2024 groundnut note that explicitly states that its harvest-price estimate is subject to arrivals and monsoon conditions.[^5] EcoFarm should test transparent market observation and comparison, not price prediction.

### Ranked candidates

| Rank | Candidate decision problem | Desk score / 40 | Recommendation | Principal caveat |
|---:|---|---:|---|---|
| 1 | Rainfed crop establishment and early-season response | 32 | Primary field hypothesis | Existing weather/advisory services may already be sufficient; local farmer use and trust are unknown. |
| 2 | In-season pest/disease/weed/moisture response | 32 | Parallel field hypothesis | Highest safety burden; requires expert escalation and conservative boundaries. |
| 3 | Harvest/sale timing and market routing | 30 | Secondary comparison | Liquidity, storage, quality, and buyer power may dominate information effects. |

The scores are **analytical judgments**, not scientific facts. The primary recommendation is to run a 30-day field programme that compares the first two workflows before building software. If product leadership requires one wedge immediately, test **rainfed sowing and early-season response among small groundnut farmers**, but include a small comparison group growing maize, sorghum, tapioca, or another locally material crop system. Groundnut is a promising entry hypothesis because it is listed as a major Namakkal crop, KVK Namakkal has crop-specific groundnut and drought activities, and recent research has directly studied rainfed groundnut farmers in the district.[^1] [^3] [^6] It is not yet a validated product segment.

## 2. What the evidence establishes—and what it does not

The official district agriculture page establishes that Namakkal is a mixed crop environment with both irrigated and rainfed agriculture, multiple soil and water conditions, and crops including paddy, sorghum, groundnut, pulses, maize, cotton, and sugarcane.[^1] The handbook adds operational holding, regulated-market, crop-insurance, irrigation-by-crop, and crop-list detail.[^2] These sources support segmentation by **crop system, holding size, and water situation** rather than treating “Namakkal farmers” as a single customer.

The evidence also establishes that the advice ecosystem is populated. KVK Namakkal describes regular advisory services, on-farm testing, demonstrations, need-based training, ICT/media advisories, and groundnut and drought-mitigation activities.[^3] IMD exposes district-level forecasts, agromet bulletins, local-language bulletins, KALP location-specific weather prediction, and SANKALP-related advisory infrastructure.[^7] Tamil Nadu’s e-NAM page describes electronic trading, assaying, SMS market information, and regulated-market integration.[^4] Consequently, **“farmers lack information” is not a defensible problem statement**.

> The more defensible gap hypothesis is that information may be **available but not sufficiently localized, timely, comparable, trusted, or translated into a feasible action** for a specific farmer and crop stage.

The evidence does not establish that Namakkal farmers prefer an app, that they trust AI, that they will share farm data, that they will pay, or that any advice feature will be adopted repeatedly. The supplied EcoFarm archive is a hypothesis repository, not independent customer evidence. The current report therefore uses “product hypothesis” and “field validation required” labels deliberately.

## 3. Segment map

### 3.1 Practical segment dimensions

The first segmentation should combine five dimensions: crop system, operational holding size, water exposure, market route, and advisory access. These dimensions are more useful than generic labels such as “small farmer” or “digital farmer.” The handbook’s provisional Agricultural Census table records 244,347 operational holdings and a large concentration in the smallest holding classes.[^2] However, an operational holding is not automatically a household, income unit, or decision-maker. Field sampling must therefore record both holding size and household decision authority.

| Segment | Working definition for fieldwork | Why relevant | Initial priority |
|---|---|---|---|
| Rainfed small groundnut farmer | Up to approximately 2 ha, groundnut in the last two seasons, little or no dependable irrigation, relies on monsoon or stored soil moisture | Strong exposure to sowing-window and early-season uncertainty; direct fit with EcoFarm’s starting hypothesis | High |
| Rainfed mixed dryland farmer | Up to approximately 2 ha, rotates or compares groundnut, maize, sorghum, pulses, or other dryland crops | Tests whether groundnut is truly the best wedge or merely founder familiarity | High comparison |
| Irrigated small/medium crop farmer | Approximately 1–5 ha with borewell, canal, tank, lift, or open-well access; crops may include tapioca, vegetables, paddy, jowar, or groundnut | Different decision cadence, water constraints, and crop economics; prevents overgeneralizing rainfed needs | Medium |
| Market-exposed farmer | Sells through trader, regulated market, FPO, processor, or e-NAM-linked route; may store or sell immediately | Tests harvest/sale workflow and whether information changes action despite cash constraints | Medium |
| High-advice-access farmer | Regular contact with KVK, agricultural officer, FPO, progressive farmer, dealer, or WhatsApp group | Tests whether EcoFarm complements or duplicates existing advice | Medium comparison |
| Low-advice-access farmer | Relies mainly on experience, family, neighbors, or dealer and has limited institutional contact | Tests whether the problem is access, trust, literacy, timing, or relevance | High comparison |

### 3.2 Why groundnut must remain a hypothesis

Groundnut is not a random choice. Namakkal’s official crop list includes it; KVK Namakkal lists groundnut-specific integrated crop management, seed production, drought mitigation, and moisture-conservation work; a recent Namakkal study directly examined 120 rainfed groundnut farmers; and a broader Tamil Nadu study sampled groundnut farmers in Namakkal blocks including Tiruchengode and Rasipuram.[^1] [^3] [^6] [^8] These facts make groundnut practical for initial access and comparison.

However, the handbook’s irrigated crop table shows substantial area in jowar, tapioca, sugarcrops, vegetables, paddy, coconut, and other systems in addition to groundnut.[^2] The crop with the most tractable decision workflow may not be the crop with the strongest founder familiarity. The field programme must therefore include a non-relative comparison village and at least one non-groundnut crop system.

## 4. Decision journeys

### 4.1 Candidate 1: rainfed crop establishment and early-season response

The workflow begins before sowing. The farmer considers rainfall expectation, soil moisture, seed availability, labour, input cost, crop price expectations, and household cash constraints. The decision may be influenced by family members, experienced neighbors, input dealers, traders, agricultural officers, KVK staff, or a local WhatsApp network. The relevant question is not “what information exists?” but **what was actually consulted before the last sowing decision, how contradictory advice was resolved, and what happened after the choice?**

The action window is likely short: the farmer may need to wait, sow, re-sow, or change the crop within days. A weak decision can generate wasted seed, labour and land-preparation cost, poor establishment, or a missed seasonal window. The recent Namakkal groundnut study reports a significant association between farm size and sowing season and identifies land-preparation cost as a major operating-cost factor in its sample of 120 farmers.[^6] This supports testing the decision, but does not establish that a digital workflow caused better outcomes.

EcoFarm could credibly support a structured comparison of a few feasible options: sow now, wait for a defined observation, inspect soil moisture, or escalate to a local adviser. It could show the source and age of weather information, identify missing facts, record the farmer’s actual action, and follow up. It cannot guarantee rain, yield, soil condition, labour, seed quality, credit, or market price.

### 4.2 Candidate 2: in-season crop-risk response

The trigger may be a pest, disease, weed, nutrient, or moisture symptom. This decision recurs during the crop cycle and often has a narrow action window. Existing workarounds include visual inspection, a neighbor, an input dealer, an agricultural officer, KVK, a WhatsApp group, a YouTube video, or prior experience. The farmer may receive several conflicting recommendations and choose the one that is nearest, most familiar, available on credit, or believed to have worked previously.

This workflow is attractive because the event, advice, action, and outcome can be recorded. It is dangerous because the system may be wrong. The Tamil Nadu information-search study documented both the importance of input dealers and concerns that dealers may use time pressure to push products; it also documented complaints about inconsistent or selective extension contact.[^9] Those findings are not current Namakkal groundnut validation, but they show why trust and commercial neutrality must be tested.

The first pilot should be limited to **triage and escalation**. It may ask for crop, stage, location, recent weather, symptom timing, and a photograph where feasible; present uncertainty; advise inspection or human review; and record what happened. It should not prescribe a chemical, recommend a brand, diagnose from a weak image, or imply that an untreated crop will be safe.

### 4.3 Candidate 3: harvest, storage, and sale timing

A sale decision is made when the farmer weighs crop maturity, expected price, quality, storage, transport, household cash needs, debt, and buyer relationship. The existence of regulated markets and e-NAM does not remove these constraints. The Namakkal handbook lists six regulated markets and multiple crop categories, while Tamil Nadu’s e-NAM page describes electronic trading, assaying, unified licensing, and SMS market-price dissemination.[^2] [^4]

TNAU’s groundnut price note is an important caution. It provides a price estimate based on historical prices and market survey but explicitly says the estimate may change with arrivals and monsoon conditions.[^5] EcoFarm should therefore test whether a farmer can use a transparent market comparison that includes quality, location, transport, and timing. It should not provide a single “best price,” guarantee a buyer, predict price with certainty, or encourage delayed sale without checking storage, liquidity, and quality risk.

## 5. Current workaround and trust map

Farmers should be understood as using a **stack of alternatives**, not a single service. The stack may include own experience, family, neighbors, progressive farmers, input dealers, traders, agricultural officers, KVK, FPOs, WhatsApp, video, television, SMS, IMD, e-NAM, regulated markets, insurance documents, and non-action. The most important competitor for EcoFarm may be a trusted person or familiar habit.

| Alternative | What it does well | Demonstrable limitation to test | EcoFarm relationship |
|---|---|---|---|
| Own experience and family | Fast, local, available, low cost | May not transfer across unusual weather, crop, or disease events | Coordinate and make assumptions explicit |
| Neighbors/progressive farmers | Field-visible comparison and social proof | Can propagate local errors or unsuitable practices | Make peer comparison visible but not authoritative |
| Input dealer | Immediate access to products, local presence, sometimes credit | Potential product conflict, limited comparison, commercial incentives | Never silently replace; disclose commercial neutrality and escalate |
| Agricultural officer / KVK | Institutional legitimacy, training, demonstrations, location-specific work | Reach, timing, staffing, and follow-up may vary | Complement, refer, and record source |
| IMD / agromet | Official forecasts and advisories | Forecast credibility, locality, timing, and translation into action may be insufficient | Translate cautiously; cite source and uncertainty |
| WhatsApp / video / TV | Easy sharing, language and peer access, repeated exposure | Misinformation, generic advice, weak accountability | Treat as current workaround to understand, not automatically displace |
| Trader / buyer | Immediate liquidity and practical market information | Bargaining asymmetry, opaque deductions, relationship dependence | Show observations, never guarantee price or buyer |
| Regulated market / e-NAM | Formal price discovery, assaying, market access | Transport, grading, waiting, registration, liquidity, and usage barriers | Compare feasible routes, not merely nominal prices |
| Non-action | Avoids cost and uncertainty when advice is weak | Delays may increase crop or price risk | Measure explicitly rather than assuming willingness to act |

A useful trust test is to reconstruct the **last advice conflict**. Ask who gave each recommendation, what evidence they offered, whether the farmer had time to compare, and whether the advice was later judged correct. Interest in a new source is weak evidence; repeated verified action after a consequential event is stronger evidence.

## 6. Problem scoring

Scores are analytical judgments using a 1–5 scale. They are not survey results.

| Candidate | Frequency | Consequence | Urgency | Addressability | Trust burden | Data feasibility | Measurability | Field access | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rainfed sowing and early-season response | 3 | 5 | 4 | 4 | 4 | 3 | 4 | 5 | 32 |
| In-season pest/disease/weed/moisture response | 4 | 4 | 5 | 3 | 5 | 3 | 4 | 4 | 32 |
| Harvest/sale timing and market routing | 2 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 30 |

The first candidate is recommended because it is bounded, consequential, locally accessible, and safer to test than autonomous crop diagnosis or price prediction. The second should be tested in parallel because it may have greater frequency and stronger observable-event measurement. The third should remain in the research programme but not become the first product unless field evidence shows that market timing is the dominant unresolved decision.

## 7. Recommended initial hypothesis and strict product boundary

### Recommended hypothesis

**For small, primarily rainfed farmers in Namakkal who grow groundnut or a comparable dryland crop, EcoFarm should test support for the decision to sow, wait, re-sow, or adjust during the establishment window because rainfall and water uncertainty can compress the action window and interact with seed, labour, cost, and crop-choice constraints. The bounded workflow should present a small number of feasible options, cite the weather or agronomic source, show uncertainty, identify missing facts, record the farmer’s actual action, and measure decision timeliness, confidence, and crop-establishment outcome.**

### Product boundary

The first pilot is not a crop-profit optimizer, AI agronomist, buyer marketplace, insurance product, pesticide recommender, guaranteed weather service, yield predictor, hardware system, or farmer social network. It is a **human-supervised, localized decision-recording and comparison workflow** for one defined event.

The workflow should refuse or escalate when key facts are missing. It should distinguish observation from forecast, forecast from interpretation, and interpretation from recommendation. It should expose alternatives and uncertainty rather than create false precision. It should store the farmer’s actual choice and outcome so the team can learn whether the support changed behavior or merely generated interest.

## 8. Thirty-day field-validation plan

### 8.1 Sampling plan

Recruit 24–30 farmers across two villages. The first village may be familiar to the founder, but the second must be non-relative and operationally independent. Use purposeful quotas rather than convenience alone.

| Dimension | Minimum comparison |
|---|---|
| Crop | At least 12 groundnut farmers; at least 8 maize, sorghum, tapioca, pulse, or comparable dryland/irrigated comparison farmers |
| Water | Rainfed or highly uncertain water; dependable borewell/canal/tank/open-well access |
| Holding | Up to 2 ha; 2–5 ha where available |
| Advice access | Low institutional/digital access; frequent KVK/extension/dealer/WhatsApp access |
| Technology comfort | Assisted phone use; independent smartphone use; basic phone or low-digital-use participant |
| Decision authority | Main decision-maker; spouse or family influencer; hired manager/worker where relevant |
| Market route | Local trader; regulated market/e-NAM-linked route; FPO/processor/storage where available |

A family-network sample is useful for learning language, decision vocabulary, and access logistics. It is insufficient to prove transferability. At least one-third of interviews should be conducted with non-relatives or through an independent local facilitator.

### 8.2 Sequence

| Days | Activity | Evidence produced |
|---:|---|---|
| 1–4 | Recruit, consent, and conduct 8–10 past-cycle interviews | Decision timelines and initial segment map |
| 5–8 | Conduct 8–10 comparison interviews in the second village | Transferability and contradiction evidence |
| 9–12 | Conduct 4–6 adviser/dealer/KVK/market interviews, clearly separated from farmer evidence | Alternative and trust map |
| 13–20 | Observe or follow live sowing, crop-risk, or sale events; use paper or spreadsheet workflow manually | Trigger-to-action records and outcome observations |
| 21–26 | Recontact participants after action; verify what they did and what happened | Repeat-use and verified-action evidence |
| 27–30 | Synthesize, score, and decide continue/change/stop | Product decision memo and next experiment |

### 8.3 Continue / change / stop signals

| Signal | Continue if | Change if | Stop or defer if |
|---|---|---|---|
| Recurrence | At least several independent farmers describe the same decision in the current or latest crop cycle | Decision recurs but differs by crop/water/market segment | No common decision emerges after purposeful sampling |
| Pain | Farmers can identify a specific cost, delay, loss, or dependence | Pain is real but structural and not information-addressable | Pain is only generic dissatisfaction or hypothetical concern |
| Workaround gap | Existing sources are too late, generic, conflicting, or difficult to compare | One trusted adviser already solves it for the segment | Existing service is timely, trusted, and actionably sufficient |
| Actionability | A farmer can take a feasible action within the window | Advice requires missing data or external resources | Information cannot change the outcome once the trigger occurs |
| Trust | Farmer can explain why the source is credible and verifies it | Trust depends on a local person EcoFarm must coordinate with | Participants reject support or see it as commercial input selling |
| Outcome | Action, timing, confidence, and consequence can be recorded | Outcome needs longer crop-cycle follow-up | No credible pre/post or comparison measure is available |
| Safety | Workflow can stay within cautious comparison and escalation | Human review or agronomist partnership is required | Wrong advice could cause material harm without reliable safeguards |

## 9. UI/UX handoff constraints

1. The interface must support **assisted use** and local-language delivery; smartphone ownership or literacy must never be assumed.
2. Every output must show the **date, location basis, source, and uncertainty** of weather, market, or agronomic information.
3. Present a small set of feasible options with constraints, not a single “best crop,” “best action,” or profit ranking.
4. Capture the farmer’s actual decision, reason, and follow-up outcome; do not treat a viewed message as action.
5. Make it easy to compare the recommendation with the farmer’s existing adviser, dealer, neighbor, or institutional source.

## 10. Product safety and trust constraints

1. Do not guarantee yield, profit, rainfall, buyer access, price, insurance settlement, or crop outcome.
2. Do not issue pesticide, fertilizer, or disease-treatment instructions when crop, stage, symptom, product, dose, or local regulatory facts are insufficient; escalate to a qualified human source.
3. Distinguish observed data, forecast, interpretation, and recommendation in both internal records and farmer-facing output.
4. Disclose uncertainty, missing inputs, data age, and the conditions under which the advice should not be followed.
5. Preserve farmer control and consent: collect only necessary data, avoid undisclosed commercial ranking, and record disagreement or non-action as valid outcomes.

## 11. Inputs required from the farmer

| Input | Why necessary |
|---|---|
| Village/location and field identifier | To avoid applying district-wide information to the wrong micro-context and to compare local events. |
| Crop, variety if known, sowing date, and crop stage | Crop-stage relevance determines whether an action is timely and safe. |
| Water source and current availability | Irrigation and rainfed exposure materially change feasible options. |
| Soil moisture or recent field observation | Establishment and water-response decisions cannot be inferred from rainfall alone. |
| Recent rainfall/forecast received and source | Allows comparison between available information and the farmer’s actual interpretation. |
| Seed, labour, input, storage, transport, and cash constraints | A theoretically optimal option may be operationally impossible. |
| Current symptom/event description and timing | Needed for conservative triage and escalation; absence makes diagnosis unsafe. |
| Advice sources consulted and recommendation received | Reveals the existing workaround and trust hierarchy. |
| Actual action and time taken | Separates understanding or interest from verified behavior. |
| Outcome or follow-up observation | Enables measurable learning without claiming causality prematurely. |

## 12. Facts insufficient for a safe recommendation

The following are insufficient on their own: a district-level weather forecast without field location or timing; a crop name without crop stage; a photograph without symptom history and field context; a market price without quality, market, date, deductions, and transport; a farmer’s stated interest without observed action; a single neighbor’s success; a generic crop-profit ranking; a forecast without uncertainty; and a recommendation that ignores labour, liquidity, storage, water, or input availability.

## 13. Unknowns and risks

The principal unknown is whether the same unresolved decision appears across independent farmers outside the founder’s network. Other unknowns include the true crop-cycle timing, the role of women and other household members in decisions, current dealer and trader influence, the practical use of KVK and IMD channels, Tamil-language and assisted-use needs, willingness to share farm information, and whether a farmer can act on advice within the available window.

The principal product risks are duplication, false precision, unsafe agronomic advice, commercial conflict, overgeneralization from a family sample, and confusing stated interest with repeat verified action. The principal business risk is that the problem is painful but not addressable by software because the binding constraint is rainfall, labour, credit, storage, buyer power, or land access.

## 14. Conclusion

The evidence supports a **narrow field experiment**, not a broad product build. Namakkal is a defensible starting geography because it combines founder access with mixed crop systems, substantial rainfed agriculture, many small operational holdings, established advisory institutions, regulated markets, and visible weather and market information infrastructure.[^1] [^2] [^3] [^4] The same evidence makes overclaiming dangerous: EcoFarm is entering an environment with existing people, institutions, and services.

The best first test is therefore a human-supervised workflow around **rainfed sowing and early-season response**, with in-season crop-risk response as a close comparison. The test should be event-based, local-language capable, transparent about uncertainty, and measured by verified behavior and outcome records. If the fieldwork does not reveal a repeated, consequential, information-addressable decision that existing channels fail to support, EcoFarm should change or stop the software hypothesis rather than expanding the platform.

## References

[^1]: [Namakkal District Agriculture Department, Government of Tamil Nadu](https://namakkal.nic.in/departments/agriculture/).
[^2]: [Namakkal District Statistical Handbook 2023-24, District Administration](https://namakkal.nic.in/document/statistical-handbook-2023-2024/); [official PDF](https://cdn.s3waas.gov.in/s3b9228e0962a78b84f3d5d92f4faa000b/uploads/2025/05/2025051243.pdf).
[^3]: [ICAR-Krishi Vigyan Kendra, Namakkal / TANUVAS](https://www.tanuvas.ac.in/kvk_namakkal.php).
[^4]: [Department of Agricultural Marketing and Agri Business, Tamil Nadu, e-NAM scheme](https://www.agrimark.tn.gov.in/index.php/scheme/view/4).
[^5]: [Tamil Nadu Agricultural University, Price Forecast for Groundnut](https://agritech.tnau.ac.in/tnaupressnotes/pdf/2024/Price%20Forecast%20for%20G.%20nut.pdf).
[^6]: [Jayashree, K.V. and Saravanan, K., “An Empirical Study on Groundnut Cultivation Practices in Rainfed Zones of Namakkal District, Tamil Nadu,” South India Journal of Social Sciences, 2026](https://journal.sijss.com/index.php/home/article/view/2297).
[^7]: [India Meteorological Department, Agromet Advisory Services](https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php).
[^8]: [Muthuswamy et al., “Weather-driven groundnut price forecasting and profitability assessment of cropping patterns in Tamil Nadu using boosting algorithms,” Scientific Reports, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12484663/).
[^9]: [Babu et al., “Farmers’ Information Needs and Search Behaviors: Case Study in Tamil Nadu, India,” IFPRI Discussion Paper 01165, 2012](https://ageconsearch.umn.edu/record/126226/files/Farmers%20information%20needs%20and%20search%20behaviour%20case%20study%20in%20Tamil%20Nadu%20India.pdf).
[^10]: [Rohit et al., “Exploring farmers’ communication pattern and satisfaction regarding the adoption of Agromet advisory services in semi-arid regions of southern India,” Frontiers in Sustainable Food Systems, 2024](https://www.frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2023.1284880/full).
[^11]: [Kumar et al., “Role of Information in Farmers’ Response to Weather and Water Related Stresses in the Lower Bengal Delta, Bangladesh,” Sustainability, 2020](https://www.mdpi.com/2071-1050/12/16/6598).
[^12]: [Tamil Nadu Department of Economics and Statistics, Season and Crop Report 2024-25](https://www.tn.gov.in/crop/stat.htm).

## Handoff summary

The next product and field-validation stages must test five exact hypotheses: **(1)** rainfed smallholders experience a repeated sow/wait/re-sow or early-season response decision with a short action window; **(2)** the current workaround stack leaves a demonstrable gap in timing, locality, comparison, or trust; **(3)** a bounded, uncertainty-labelled workflow changes an observable action or decision confidence; **(4)** the workflow can be delivered through assisted and local-language use without requiring high digital literacy; and **(5)** the workflow can operate safely without guarantees, autonomous chemical advice, unsupported price predictions, or claims of replacing existing advisers.
