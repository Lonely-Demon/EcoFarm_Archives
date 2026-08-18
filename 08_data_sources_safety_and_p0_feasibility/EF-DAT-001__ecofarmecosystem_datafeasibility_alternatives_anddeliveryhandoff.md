# EcoFarm Ecosystem, Data Feasibility, Alternatives, and Delivery Handoff

**Geography:** Namakkal / Kongu belt, Tamil Nadu, India  
**Research date:** 13 August 2026  
**Author:** Manus AI  
**Evidence posture:** Current desk research with an explicit field-verification agenda.

## 1. Executive answer

The most credible near-term opportunity is **not another generic weather, mandi-price, or crop-advisory channel**. Those functions already exist through the Namakkal Agriculture Department, ATMA, KVK Namakkal, TNAU, IMD/TNAU agrometeorological services, Agmarknet/data.gov.in, eNAM, mKisan, and private advisory platforms.[1] [2] [3] [4] [5] [6] [7] The defensible opportunity is a **transparent, localized decision workflow** that helps a farmer compare a small number of crop or action options against explicitly entered constraints, while showing source, date, location, confidence, missing data, and an escalation path.

This conclusion is a **supported inference**, not proof of farmer demand. Namakkal’s official agriculture page documents substantial rainfed and irrigated cultivation, multiple agricultural extension centres, soil-testing infrastructure, ATMA, farmer training, and crops including groundnut, pulses, maize, sorghum, cotton, paddy, and sugarcane.[1] These are strong ecosystem conditions for validation. They do not prove current reach, digital adoption, willingness to pay, or partnership availability.

The first pilot should therefore test three bounded workflows: **constraint-aware crop-option comparison**, **source-labelled weather-to-action alerts**, and **current market-observation plus choice/outcome logging**. Each must remain descriptive or decision-support oriented. EcoFarm should not predict profitability or future prices, issue autonomous high-stakes agronomic prescriptions, or imply that public institutions will distribute or endorse the product.

The main constraints are practical. Public data is often available without being sufficiently localized, stable, complete, or legally reusable for automated recommendations. Farmer-level soil and water context is more decision-relevant than district averages but may require consent, institutional access, or new field collection. KVK and department webpages document capabilities, but several pages are old or do not demonstrate current farmer reach. IMD’s API gateway requires account/access verification before implementation. Mandi data is suitable for current observations, but missingness, market relevance, quality/variety matching, and freshness must be surfaced rather than hidden.

### Decision summary

| Area | Finding | Evidence label | Pilot implication |
|---|---|---|---|
| Local ecosystem | Namakkal has a documented agriculture department, 15 block-level Agricultural Extension Centres, ATMA, soil-testing facilities, farmer training, KVK, and regulated markets. | Verified fact | Use these as context, validation, escalation, and possible field-access channels; do not assume partnership. |
| Weather | Official IMD APIs and TNAU/IMD advisories exist, including forecasts, warnings, and agromet bulletins. | Verified fact | Test ingestion and local action translation; retain source timestamp and forecast horizon. |
| Market prices | data.gov.in publishes a daily mandi-price resource sourced from Agmarknet; Tamil Nadu maintains regulated-market infrastructure. | Verified fact | Show observed min/max/modal prices by market, commodity, variety, and date; do not forecast. |
| Agronomy | TNAU publishes crop-production guidance and KVK Namakkal lists crop, soil, weather, training, trials, and demonstrations. | Verified fact | Use as referenced education with crop/region/date metadata and human escalation. |
| Farmer-level soil/water | Local testing exists, but farmer-specific digital access and current groundwater resolution are not established. | Unknown / verification required | Do not build automated recommendations on district averages or unconsented farmer records. |
| Competitive position | Public, institutional, broadcast, marketplace, input-linked, and informal channels already serve overlapping jobs. | Supported inference | EcoFarm must win on transparent synthesis and decision logging, not information volume. |

## 2. Ecosystem map

### 2.1 Documented actors and likely relationship types

| Actor / channel | Documented role and geography | Farmer segment / decision moment | Delivery and language | Practical limitation evidenced or requiring verification | EcoFarm relationship |
|---|---|---|---|---|---|
| Namakkal District Agriculture Department | District programmes, seed and input oversight, soil-health activities, IPM/INM, crop diversification, farmer training, ATMA, 15 block AECs, and soil-testing facilities.[1] | Farmers seeking schemes, inputs, soil testing, crop support, and extension at block level. | Offices, extension centres, training, field services; Tamil access should be confirmed. | The page documents infrastructure and functions, not current service levels or digital reach. | Validation source, escalation channel, possible field-access route; not assumed partner. |
| ATMA Namakkal | Research–extension–farmer linkage through demonstrations, training, and exposure visits.[1] | Farmers needing technology transfer and group-based learning. | Demonstrations, training, exposure visits; current schedule and language to verify. | Active programme calendar, contactability, and current farmer reach are unknown. | Human validation and field-access hypothesis. |
| KVK Namakkal / TANUVAS | KVK started in 2004; page lists crop production/protection, soil, water, seed, training, trials, demonstrations, market information, and ICT/media links.[2] | Farmers seeking applied technical advice, demonstrations, and training. | In-person campus/outreach and linked digital/media channels; language and current schedule to verify. | Portal has 2013 copyright and references a 2010–11 annual report; current operations must be reconfirmed. | Technical validation and escalation; possible intermediary only after conversation. |
| TNAU Agritech and crop guides | Crop, pest, disease, weather, soil, water, market, and advisory content; TNAU Crop Production Guide is an authoritative agronomic reference.[8] [9] | Farmers, extension staff, and advisers needing general crop guidance. | Web and institutional outreach; Tamil localization and comprehension require testing. | General guidance can be over-generalized to plot-level action. | Source library and validation reference; preserve original attribution and version. |
| IMD / TNAU agromet services | IMD provides forecasts, observations, warnings, and specialized bulletins through its API gateway; TNAU hosts agromet bulletins and TAWN references block-level services.[3] [10] [11] | Farmers making weather-sensitive sowing, spraying, irrigation, and harvest decisions. | Web, apps, bulletins, and possible API delivery; local-language action wording requires testing. | API registration/terms, forecast resolution, outages, and advisory applicability must be verified. | Source aggregation and alert presentation, not replacement of official warnings. |
| Tamil Nadu Department of Agricultural Marketing / regulated markets | Regulated markets support buying/selling and market infrastructure; TNAU lists Namakkal markets including Namakkal, Namagiripettai, and Kolli Hills entries.[12] [13] | Farmers deciding where/when to observe or sell produce. | Physical markets plus online price information; local market practices require interviews. | A listed market is not proof of active trading for every commodity or farmer access. | Market-context source; no buyer assurance. |
| Agmarknet / data.gov.in | Daily mandi-price resource; OGD metadata identifies DMI/Department of Agriculture and a variety-wise market-price web service.[4] [14] | Farmers and advisers seeking observed prices. | API/web dataset; farmer-facing explanation needed. | Missingness, quality/variety matching, delayed updates, and source-market relevance need monitoring. | Read-only observation layer with freshness and missing-data flags. |
| eNAM | Pan-India electronic trading portal linking APMC mandis into a national market.[5] | Farmers, traders, and FPOs participating in price discovery or trading. | Web/app and mandi-linked operations. | Access, registration, commodity/market coverage, and transaction execution are distinct from simply viewing prices. | Adjacent alternative; do not imply EcoFarm offers transactions. |
| mKisan / Kisan Suvidha | Government mobile/SMS channels provide weather, agro-advisory, market and related information.[6] [7] | Farmers who accept broadcast or mobile information. | SMS/app; registration, handset, language, and notification tolerance matter. | Broadcast information is not a plot-specific, interactive decision record. | Complement by synthesizing and logging a named decision. |
| Private advisory and input-linked platforms | DeHaat describes farmer app services including crop reminders, advisories, and weather; IFFCO Kisan describes weather, mandi, and advisory features.[15] [16] | Digitally reachable farmers and input-linked users. | App, call centre, input network, and local agents. | Marketing claims do not establish Namakkal adoption, accuracy, or independence from input sales. | Adjacent alternatives; field-verify local usage and trust. |
| FPOs, cooperatives, traders, input dealers, and local advisers | Namakkal has documented collective-farming/FPO policy context and FPO studies; individual actor activity and trust must be verified.[1] [17] | Farmer groups needing aggregation, input access, market access, or practical advice. | In-person, WhatsApp/phone, meetings, and transactions; Tamil is likely important but must be tested. | Commercial incentives and advice quality vary; no actor should be labelled trusted without evidence. | Potential distribution or human-escalation route after interviews. |

### 2.2 Ecosystem interpretation

The ecosystem is **dense rather than empty**. Farmers may receive advice from departments, KVKs, dealers, traders, peers, WhatsApp groups, television/radio, mobile apps, SMS, and market contacts. The practical job is not merely finding information; it is deciding which information applies, what is uncertain, and what action is safe. EcoFarm should route to authoritative sources and human help where uncertainty is material. A product that simply republishes weather, prices, or crop tips is likely to duplicate existing channels.

## 3. Data-feasibility matrix

| Candidate source / category | Fields and resolution | Freshness / history | Access and terms | Known gaps / safety issue | Classification |
|---|---|---|---|---|---|
| IMD API Management Platform | Observations, forecasts, warnings, specialized bulletins; exact endpoint fields and spatial granularity require account inspection.[3] | Real-time and forecast products are advertised; historical access is not established from the landing page. | Official portal with registration/login and Explore APIs; confirm credentials, quotas, attribution, and redistribution terms. | Forecast error, local microclimate, outages, and generic wording. Never convert to guaranteed crop outcome. | Available but insufficient alone until access and resolution are tested. |
| IMD/TNAU agromet bulletins and TAWN | District/block-oriented forecast/advisory content; bulletin date, forecast period, crop/action text.[10] [11] | Bulletin periods are explicit; historical archive stability needs testing. | Public webpages; confirm scraping/redistribution terms and language. | A bulletin may be stale, generic, or not fit a farmer’s crop stage. | Available and pilot-usable for source-labelled alerts, with caveats. |
| Agmarknet via data.gov.in | Market, commodity, variety, date, min/max/modal price, and likely arrivals depending on endpoint.[4] [14] | Daily granularity; resource page showed update on 13 Aug 2026 at research time.[4] | OGD API/resource; Government Open Data License–India applies to published datasets/metadata, but endpoint limits and downstream presentation should be reviewed.[4] | Market/variety mismatch, missing days, delayed entries, price units, and no future-price validity. | Available and pilot-usable for observations. |
| Tamil Nadu regulated-market listings | Market names, locations, contacts, infrastructure; current commodity activity requires direct check.[12] [13] | Static directory plus current departmental price pages; update cadence varies. | Public webpages; verify reuse terms. | Directory inclusion does not prove active local relevance or farmer access. | Available but insufficient alone. |
| TNAU Crop Production Guide | Crop, season, land preparation, nutrient, irrigation, pest/disease, and harvest guidance.[8] [9] | Guidance publication date/version; not a real-time feed. | Public university publication; preserve attribution and version. | General recommendations may not match local soil, water, cultivar, or stage. | Available and pilot-usable as referenced education. |
| Namakkal soil testing / Soil Health Card | Soil sample and laboratory results, soil-health indicators, recommendations; district page confirms local lab/mobile-lab workflow.[1] [18] | Test date is important; farmer records may be stale. | Farmer-facing departmental process; digital/API access and consent requirements unknown. | Grid samples are not plot-specific; farmer records require consent; lab interpretation is not a full crop-profit recommendation. | Requires permission or partnership for automated use; otherwise use farmer-held report entry. |
| CGWB groundwater resources and quality | Aquifer/groundwater resource and quality reports, typically district/block or monitoring-point scale.[19] [20] | Annual/periodic reports; monitoring dates vary. | Public reports and India-WRIS; direct data access and reuse should be checked. | Spatial scale and staleness are unsuitable for asserting a particular borewell’s status; do not claim local depletion rates without primary scoped data. | Available but insufficient alone. |
| Farmer-entered data | Village/location, plot area, soil-test date/results, irrigation type, crop history, crop stage, constraints, preferred language, and chosen option. | User-entered and event-based; validate and timestamp each field. | Consent-based collection; data minimization, deletion, access, and purpose notice required. | Recall error, language burden, privacy sensitivity, missingness, and false precision. | Available and pilot-usable only for a named workflow. |
| Satellite / remote sensing | Vegetation indices, land-cover signals, rainfall proxies, and temporal imagery; exact field inference depends on resolution and cloud cover.[21] [22] | Periodic revisit, cloud-dependent; historical access varies. | Public or commercial APIs; terms, cost, attribution, and derived-product rights require verification. | Cannot reliably diagnose crop, disease, yield, irrigation need, or farmer intent for a small pilot without ground truth. | Not appropriate as a primary initial recommendation input; optional validation signal. |
| Pest/disease sources | Crop-specific symptoms, integrated pest management, preventive actions, and escalation contacts from TNAU/KVK/department.[1] [2] [8] | Publication/advisory date varies; outbreak status may change rapidly. | Public institutional materials; confirm reuse and current advisories. | Image/symptom ambiguity and false certainty can cause crop or health harm; pesticide advice requires label and expert escalation. | Available but insufficient alone; education plus escalation only. |

### 3.1 Three data-supported candidate workflows

| Workflow | Minimum input and transformation | Output | Strongest reason it may fail | Alternative to complement/outperform | Trust proposition |
|---|---|---|---|---|---|
| Constraint-aware crop-option comparison | Village/block, season, water/irrigation constraint, soil-test availability, land size, labour/input constraint, and farmer objective. Join TNAU crop guidance with non-predictive water/soil context and explicit unknowns. | A short comparison of feasible options, assumptions, trade-offs, and questions for a human adviser. | Inputs may be incomplete or inaccurate; agronomic suitability is not profitability and district averages can mislead. | Department/ATMA/KVK advice, local agronomist, input dealer, and farmer experience. | “We show why an option appears feasible, what we do not know, and when to ask a person.” |
| Weather-to-action alert | Location, crop, crop stage, source bulletin/forecast, forecast period, and action rule. | Source-labelled alert such as “consider delaying spray if rain is forecast; confirm locally,” with timestamp and confidence. | Forecast resolution and generic advisory wording may not support plot-specific action. | IMD/TNAU official alert channels and local adviser. | “Official source and time are visible; alert is not a guarantee.” |
| Market-observation and outcome log | Commodity/variety, market, date, unit, observed min/max/modal price, farmer’s choice, and later outcome. | Current observation table, change over time, and private decision/outcome history; no price prophecy. | Data may be missing or non-comparable; logged outcomes are confounded by quality, timing, transport, and buyer terms. | Agmarknet/data.gov.in, eNAM, regulated market, trader/FPO. | “Observed price is labelled as observed; farmer choice remains the farmer’s.” |

## 4. Existing alternatives and competitive reality

| Alternative | Job served | Strength | Documented or material limitation | EcoFarm relationship |
|---|---|---|---|---|
| District department / ATMA / KVK | Technical advice, schemes, training, demonstrations, soil testing, and escalation. | Institutional authority, local presence, and human accountability. | Access is episodic; webpages do not establish response time, personalized availability, or digital workflow. | Complement and route to, never replace. |
| IMD/TNAU advisories | Weather-sensitive action guidance. | Official meteorology and agricultural interpretation. | Forecast uncertainty, limited plot-level specificity, and potential alert overload. | Make provenance and action context visible. |
| Agmarknet/data.gov.in | Current market observation. | Broad official market-price source and API route. | Missingness, market/variety mismatch, and no future-price guarantee. | Normalize, compare, and explain; never predict. |
| eNAM | Market access and electronic trading. | Trading/price-discovery network, not just an information page. | Registration, market participation, grading, logistics, and buyer availability remain operational. | Adjacent; do not become a marketplace in pilot. |
| mKisan/Kisan Suvidha | Broadcast weather, advisory, and market information. | Low-friction public channel and SMS/app reach. | Broadcast content is not a persistent, individualized decision record. | Complement with narrow workflow and logging. |
| Private advisory/input-linked apps | Reminders, weather, crop advice, inputs, and services. | Convenience, bundled support, and potentially local agents. | Independence, local adoption, recommendation quality, and commercial incentives require verification. | Compete only on transparency and decision traceability where evidence supports it. |
| Input dealers/traders/FPOs | Immediate practical advice, inputs, aggregation, or sale. | High-frequency local relationships and transaction knowledge. | Incentive conflicts, variable expertise, and undocumented advice quality. | Human channel and reality check; display commercial context. |
| Peer/WhatsApp/telephone advice | Fast, socially trusted problem-solving. | Familiar, accessible, and language-aligned. | Rumour propagation, outdated content, and no provenance. | Design for assisted use and source checking, not displacement. |
| Status quo | Farmer combines experience, family, dealer, weather, prices, and institutional advice. | No new onboarding or technology burden. | High cognitive load; contradictions and implicit assumptions remain invisible. | EcoFarm must reduce decision friction enough to change behaviour. |

## 5. Complement-versus-duplicate analysis

EcoFarm should **aggregate and explain**, not broadcast more of the same. A useful product boundary is a “decision packet” containing the farmer’s stated constraints, the selected sources, timestamps, the transformation applied, the unknowns, the options compared, and the human escalation route. This is meaningfully different from a portal that merely displays a weather number or a mandi table.

The product should not duplicate official alerts in a way that creates competing authority. It should link to the original alert, state whether its wording is directly reproduced or transformed, show the forecast period and location, and suppress or downgrade output when the source is stale or incomplete. For prices, it should aggregate observations only where commodity, variety, unit, market, and date are comparable.

## 6. Delivery and trust feasibility

Desk evidence confirms institutional and digital channels but is weak on actual farmer reach. Connectivity, smartphone ownership, digital literacy, Tamil terminology, notification tolerance, and assisted-use patterns must therefore be treated as **unknown / verification required** rather than inferred from app availability. The pilot should support Tamil-first assisted use, low-bandwidth or offline-safe review, and a human fallback through a local adviser, FPO, or extension intermediary. A phone-based interview should test whether farmers prefer voice, WhatsApp, SMS, or in-person review; the answer must not be assumed.

The minimum trust proposition is operational rather than cosmetic: source and time are visible; the system distinguishes observation from inference; missing data is shown; a farmer can reject or change a suggestion; no guaranteed profit or buyer outcome is claimed; and a named human escalation path exists. The product should collect only fields required by the selected workflow.

## 7. Safety and governance constraints

| Risk | Required control |
|---|---|
| Stale or missing source | Store source timestamp/version, check freshness, show “last updated,” and fail closed to “no current data” rather than inventing a value. |
| False agronomic certainty | Use educational and constrained decision-support language; show assumptions and uncertainty; escalate disease, pesticide, irrigation, and crop-failure cases. |
| Price overclaim | Label min/max/modal as observed prices, include market/date/variety/unit, and prohibit future-price or buyer-assurance language. |
| Unconsented farmer data | Obtain purpose-specific consent; collect minimum fields; provide deletion/access path; avoid collecting data “just in case.” |
| Source rights and redistribution | Maintain a source register with terms, attribution, endpoint permissions, and fallback; do not assume public visibility equals unrestricted API redistribution. |
| Conflicting advice | Preserve each source, explain the conflict, prefer authoritative/current material, and route material disagreement to a human. |
| Pesticide or disease harm | Do not diagnose from one photo or symptom; provide safe educational content and escalation; never conceal label, dosage, or protective-equipment requirements. |
| Recommendation accountability | Log input state, source version/time, rule/model version, output, farmer acceptance/rejection/change, and escalation event. |
| Institutional misrepresentation | Refer to institutions as sources or possible channels until a documented conversation or agreement exists. |

## 8. Pilot operating implications

A safe pilot needs one named decision, not a broad platform. The minimum technical contract should include: a source adapter; normalized source timestamp and location; a completeness/freshness state; a transparent transformation layer; a human-readable explanation; and an immutable recommendation/decision log. The system should retain raw source references but avoid retaining unnecessary personal data.

The pilot should begin with a small set of crops and villages chosen after Agent 1 and fieldwork identify a repeated decision. The first test should compare EcoFarm’s decision packet with the farmer’s existing process, not merely measure app clicks. Success measures should include comprehension, trust calibration, whether the farmer can explain why an option was shown, whether contradictory advice is recognized, and whether escalation occurs appropriately.

### Prioritized development data contract

| Priority | Input | Source | Transformation | Output | Update pattern | Failure behavior |
|---|---|---|---|---|---|---|
| P0 | Location, crop/season/stage, constraints, source metadata | Farmer + official source | Validate, timestamp, classify missingness | Decision packet | At decision time | No recommendation if critical fields missing; offer questions/escalation. |
| P0 | Market, commodity, variety, date, min/max/modal price | data.gov.in/Agmarknet | Normalize units and comparability | Read-only price observation | Daily or on demand | Show stale/missing; never interpolate without label. |
| P0 | Forecast/advisory, period, location | IMD/TNAU | Map only to conservative action rules | Alert with source and caveat | Bulletin/forecast update | Link to official source and suppress if stale. |
| P1 | Soil test values/date, irrigation type | Farmer-held report or authorized department process | Validate date and units; do not infer missing nutrients | Constraint input / comparison factor | Per test or farmer update | Treat as unknown; do not substitute district average silently. |
| P1 | Crop guide and pest-risk education | TNAU/KVK/department | Version and region tag | Referenced education | Versioned content updates | Keep prior version and escalate uncertain cases. |
| P2 | Satellite signal | Public/commercial imagery | Cloud/quality screening and ground-truth check | Optional context only | Periodic | Do not use as primary recommendation input. |

## 9. Open questions and field/partner verification plan

The central unknown is not whether sources exist; it is whether they are current, reachable, understood, and useful at the decision moment. The verification agenda in `field_partner_verification_questions.md` should be completed before implementation decisions.

Priority questions include: Which crop decision recurs often enough to matter? Which block and farmer segment should be tested? Which source does the farmer currently trust? How are weather and price updates received and acted upon? Can the farmer access or share a soil-health card? What are the local names, units, varieties, and market practices? When do farmers seek a human adviser? Which official pages or APIs can be reused, at what rate, and with what attribution? Will any institution permit observation, referral, or data access? What happens when sources disagree or fail?

## 10. Product, UI/UX, and development handoff

### Product handoff

The three candidate workflows are the crop-option comparison, weather-to-action alert, and market-observation/outcome log. The strongest failure mode for all three is **false relevance**: a technically correct source may still be wrong for the farmer’s crop stage, location, variety, water condition, or objective. Each workflow must complement the relevant department/KVK/IMD/market channel and offer a minimum trust proposition of transparent provenance, explicit uncertainty, farmer control, and human escalation.

### UI/UX handoff

Every user-facing source card should show source name, publisher, location or market, date/time, freshness, forecast period or observation date, confidence/quality state, limitations, and a link or reference to the original. Inputs that cannot be assumed include soil test values, irrigation reliability, crop stage, land area, farmer objective, market access, willingness to sell, and tolerance for labour or input risk. Prototype testing must examine Tamil labels, voice or assisted entry, low connectivity, error correction, and whether farmers understand “observed price” versus “expected price.”

### Development handoff

Read-only information should include raw prices, official forecasts, official warnings, and referenced agronomy. Constrained recommendations may include option comparison and conservative action prompts only when required inputs are present and the rule is documented. Required logs are source version, source time, location/market, recommendation or rule version, missing-data state, farmer change/rejection, and escalation event. Explicit blockers before implementation are IMD API terms/access, source redistribution rights, farmer-data consent, local-language content review, source-failure handling, and named human escalation.

## 11. Overall recommendation

Proceed to **field validation and a narrow, read-only or constrained decision-support prototype**, not a broad agricultural operating system. The first implementation should prefer a source-labelled market observation or weather action workflow if fieldwork confirms a repeated decision, while crop-option comparison should remain bounded and advisory rather than predictive. Do not build marketplace, future-price prediction, autonomous agronomy, hardware control, or institution-branded distribution until evidence and governance are materially stronger.

## References

[1]: https://namakkal.nic.in/departments/agriculture/ "Government of Tamil Nadu, Namakkal District Agriculture Department"
[2]: https://agritech.tnau.ac.in/kvk/kvk_namakal.html "TNAU Agritech Portal, KVK Namakkal"
[3]: https://api.imd.gov.in/ "India Meteorological Department API Management Platform"
[4]: https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi "data.gov.in, Current Daily Price of Various Commodities from Various Markets"
[5]: https://enam.gov.in/ "National Agriculture Market (eNAM)"
[6]: https://mkisan.gov.in/ "mKisan Portal"
[7]: https://mkisan.gov.in/Home/Downloads "mKisan Downloads and Kisan Suvidha information"
[8]: https://tnau.ac.in/site/research/crop-production-guide/ "Tamil Nadu Agricultural University Crop Production Guide"
[9]: https://agritech.tnau.ac.in/pdf/HORTICULTURE.pdf "TNAU Crop Production Guide: Horticulture Crops"
[10]: https://agritech.tnau.ac.in/agrometeorologicaladvisory/agro_meteorological_advisory_tnau_district.html "TNAU Weather Watch Group / District Agro-Meteorological Advisory"
[11]: http://tawn.tnau.ac.in/ "Tamil Nadu Agriculture Weather Network"
[12]: https://www.agrimark.tn.gov.in/ "Tamil Nadu Department of Agricultural Marketing and Agri Business"
[13]: https://agritech.tnau.ac.in/agricultural_marketing/agrimark_Regulated%20markets_list.html "TNAU Agricultural Marketing: Regulated Market List"
[14]: https://www.data.gov.in/apis "data.gov.in APIs"
[15]: https://agrevolution.in/solution-for-farmers "DeHaat Farmer App and Services"
[16]: https://poultry.proultry.com/products/iffco-kisan "IFFCO Kisan service description"
[17]: https://ageconsearch.umn.edu/record/367751/files/Sasikanth41102023AJAEES107623.pdf "Study of Farmer Producer Organizations with special reference to Namakkal District"
[18]: https://soilhealth.dac.gov.in/ "Government of India Soil Health Card Portal"
[19]: https://cgwb.gov.in/cgwbpnm/public/uploads/documents/17096271421048841089file.pdf "CGWB State Report on Groundwater Quality in Tamil Nadu and Puducherry"
[20]: https://indiawris.gov.in/wiki/doku.php?id=cgwb_ground_water_resources "India-WRIS / CGWB Groundwater Resources"
[21]: https://www.isro.gov.in/ "Indian Space Research Organisation"
[22]: https://developers.google.com/earth-engine/datasets "Google Earth Engine Data Catalog and usage documentation"
