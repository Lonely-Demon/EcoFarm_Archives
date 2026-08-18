# EcoFarm Field and Partner Verification Questions

**Purpose:** Resolve the unknowns that desk research cannot establish before selecting a pilot workflow or committing to integrations. Questions should be asked in Tamil or the respondent’s preferred language, recorded with consent, and tagged by source and date.

## 1. Questions for farmers

| Theme | Questions | Evidence to record |
|---|---|---|
| Decision | What is the most important crop decision you make before sowing, during the crop, and at sale? Which decision creates the most uncertainty or loss? | Named decision, timing, crop, and consequence. |
| Existing advice | Whom do you ask first: family, neighbour, dealer, trader, FPO, extension officer, KVK, app, SMS, or WhatsApp group? Why? | Actor, trust reason, response time, and whether advice is followed. |
| Weather | Which weather information do you receive? By what channel and language? What action did it change recently? | Source, channel, forecast horizon, action, and comprehension. |
| Prices | Which market and commodity/variety do you follow? Do you compare min/max/modal prices, trader quotes, or actual sale prices? | Market, unit, quality/variety, transport cost, and sale outcome. |
| Soil/water | Do you have a soil-health card or lab report? When was it issued? How do you assess irrigation reliability and water quality? | Report availability, date, fields, consent to share, and farmer interpretation. |
| Inputs and constraints | What constraints matter most: water, labour, cash, seed, input access, timing, risk tolerance, or buyer access? | Ranked constraints and whether they are stable or seasonal. |
| Digital use | What phone do you use? Can you receive SMS, voice, WhatsApp, or app content? Is connectivity reliable in the field? | Device, channel preference, network failures, shared-device issue. |
| Language and assisted use | Which Tamil terms are clear? Would you prefer voice, a person helping, or a simple comparison card? | Comprehension test and preferred assisted-use pattern. |
| Trust and safety | What would make you distrust an agriculture tool? When would you insist on a human adviser? | Trust triggers, escalation threshold, and prohibited claims. |
| Outcome logging | Would you record what you chose and what happened later? What information would feel too personal? | Consent boundary, minimum log fields, and follow-up feasibility. |

## 2. Questions for Namakkal Agriculture Department and ATMA

1. Which blocks, crops, and farmer segments currently receive the most active extension support? Please provide the current programme calendar and contacts.
2. Are the 15 Agricultural Extension Centres currently staffed and reachable? What are typical response times and service hours?
3. What soil-testing services are currently operational at Namakkal and through the Tiruchengode mobile unit? What are sample routes, fees, turnaround times, report fields, and farmer consent rules?
4. Are soil-health card records available to farmers digitally or only as printed reports? Is any API, export, or referral process available to an authorized pilot?
5. Which ATMA demonstrations, trainings, or exposure visits are active in the target blocks? Can EcoFarm observe without implying endorsement?
6. Which crops and crop stages generate the most repeated farmer questions? Which questions must always be escalated to an officer?
7. How are official weather and pest/disease advisories received, adapted, and distributed locally? Which source is considered authoritative when advisories conflict?
8. Which local-language formats work best: in-person, pamphlet, voice, SMS, WhatsApp, or app?
9. Would the department review a prototype’s disclaimers and escalation language? What attribution and non-endorsement wording is required?
10. What data may be publicly reused, what requires permission, and what must remain within department systems?

## 3. Questions for KVK Namakkal / TANUVAS / TNAU

1. What are the KVK’s current major thrust areas, crops, active trials, demonstrations, training calendar, and farmer coverage in Namakkal?
2. Which TNAU recommendations are crop-, region-, soil-, or season-specific for the target belt, and which are general references only?
3. What is the recommended human escalation path for pest/disease images, pesticide questions, crop failure, and uncertain diagnosis?
4. Are current bulletins, crop guides, training materials, or advisories available for reuse in a farmer-facing tool? What attribution, versioning, and language review are required?
5. Can the KVK validate a small set of conservative crop-option comparison rules without becoming the product’s implied endorser?
6. Which data can be shared, which can only be viewed, and which requires a formal agreement?
7. What farmer communication channels are actually active and trusted: visits, phone, WhatsApp, radio, video, or app?
8. Which claims or recommendations would the KVK consider unsafe or too generalized for automated delivery?

## 4. Questions for IMD, TNAU weather owners, and API/data owners

1. What exact IMD API products cover Namakkal and at what spatial resolution? Are block-level forecasts available through the API or only through bulletins?
2. What are the forecast horizons, update times, historical endpoints, quality flags, rate limits, uptime expectations, and authentication requirements?
3. What are the permitted uses, attribution rules, redistribution limits, and restrictions on commercial or derived alerts?
4. How should missing, delayed, contradictory, or revised forecasts be represented?
5. Can EcoFarm store source snapshots or only references? How should source version/time be recorded?
6. Which advisory wording may be reproduced verbatim, and what transformation requires review?
7. Which Tamil terms and channels are recommended for weather-sensitive actions?

## 5. Questions for Agmarknet, data.gov.in, regulated markets, and eNAM stakeholders

1. Which Namakkal/Kongu markets, commodities, varieties, grades, and units are covered consistently?
2. What are the exact meanings of min, max, modal, arrivals, and date fields? Are prices updated on the same day or later?
3. How often are records missing, corrected, duplicated, or reported under inconsistent commodity/variety names?
4. What API keys, rate limits, licensing, attribution, and redistribution rules apply to the resource and any derived display?
5. Is there a recommended market identifier or official mapping for Namakkal, Namagiripettai, Kolli Hills, and nearby comparison markets?
6. Can a market committee validate whether a displayed observation is locally meaningful for a farmer’s commodity and quality grade?
7. For eNAM, which local markets and commodities are active, and what must a farmer or FPO do to participate in a transaction?
8. How should EcoFarm avoid suggesting that an observed price is a guaranteed sale price?

## 6. Questions for FPOs, cooperatives, farmer groups, and local intermediaries

1. Which crops, villages, and farmer segments do you actively serve today? How many members are active rather than merely registered?
2. What decisions do farmers ask you to help with, and at what time in the crop cycle?
3. Which channels do members actually use and understand: meetings, phone, WhatsApp, SMS, app, or printed material?
4. Would a staff member assist farmers with a decision packet? What training, time, and liability boundaries would be needed?
5. What market, buyer, quality, transport, and input information is available directly to the group, and what cannot be shared?
6. Which claims would make farmers distrust EcoFarm or interpret it as a buyer, lender, insurer, or government service?
7. What would a safe referral or escalation process look like when the tool is uncertain?

## 7. Questions for input dealers and traders

1. Which crop problems and market questions do farmers bring most often? Which are commonly misunderstood?
2. What information do you rely on for advice or price quotes, and how current is it?
3. Which incentives or commercial relationships could affect the advice given?
4. What fields distinguish a reliable price comparison: commodity, variety, grade, moisture, quantity, market, transport, and buyer terms?
5. When should a farmer be referred to an agriculture officer, KVK, plant-protection expert, or laboratory?
6. Would you participate as an identified human channel, and what disclosure would be necessary?

## 8. Questions for legal, privacy, and data-governance review

1. Does each source permit API retrieval, storage, transformation, caching, and farmer-facing redistribution?
2. What consent is required for farmer location, soil reports, crop history, choices, and outcomes?
3. What minimum fields are necessary for each workflow, and which proposed fields should be removed?
4. What retention, deletion, access, correction, and breach procedures are required?
5. How will the product document source version, freshness, missing-data state, recommendation version, farmer rejection, and escalation?
6. What wording clearly distinguishes information, constrained decision support, professional advice, price observation, and transaction assurance?
7. Which workflows require a named human reviewer or a local institutional escalation agreement before pilot release?

## 9. Evidence capture template

For each interview or partner conversation, record: respondent role; institution/organization; date and location; language; consent status; exact claim; supporting document or data sample; geography; currentness; contradiction; confidence; requested follow-up; and whether the respondent authorized any public attribution. Do not record a conversation as a partnership, integration, endorsement, or data right without a written agreement.
