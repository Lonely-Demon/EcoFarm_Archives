> **Curated citation system:** Each `EF-*` citation links to the canonical reviewed file in the public EcoFarm archive. Legacy `SRC-*` identifiers remain available through the archive crosswalk for historical traceability. A cited source may still be historical, exploratory, or unvalidated; its source status governs interpretation.

# EcoFarm Master Knowledge Base

> **Document posture:** This is a preserved, non-final, evidence-aware knowledge base. It is designed to retain the reasoning needed to revisit EcoFarm’s choices; it is not a pitch deck, a final product requirements document, a statement of validated customer demand, or a promise that every historical idea will be built.

| Field | Current value |
|---|---|
| **Working purpose** | Preserve EcoFarm’s vision, conceptual mechanics, research, technical thinking, decision history, alternatives, and unresolved questions so future decisions can be remade from context. |
| **Primary forms** | This human-readable Markdown document; a structured LLM retrieval corpus; and a navigable HTML knowledge site. |
| **Archive baseline** | 390 preserved source files, including historical task artifacts, current uploads, shared project research, research-agent work, visual assets, and canonical conversation records. |
| **Source system** | `SRC-xxxx` identifiers resolve through the preserved source manifest and LLM corpus. |
| **Current product posture** | Broad long-term ecosystem vision; narrow, human-supervised, evidence-constrained field/P0 exploration. |
| **Core rule** | Do not convert a historical design, a plan, a desk-research inference, or an AI/agent synthesis into proof that a feature works, that farmers want it, or that it is currently approved. |

## Table of Contents

1. [How to use this knowledge base](#1-how-to-use-this-knowledge-base)
2. [EcoFarm’s mental universe](#2-ecofarms-mental-universe)
3. [Historical evolution of the EcoFarm thesis](#3-historical-evolution-of-the-ecofarm-thesis)
4. [Problem landscape and research knowledge](#4-problem-landscape-and-research-knowledge)
5. [Conceptual system models](#5-conceptual-system-models)
6. [Feature and capability dossiers](#6-feature-and-capability-dossiers)
7. [Technical and data-system archive](#7-technical-and-data-system-archive)
8. [Trust, safety, consent, and governance](#8-trust-safety-consent-and-governance)
9. [Field validation and operating memory](#9-field-validation-and-operating-memory)
10. [Current working map without forced finality](#10-current-working-map-without-forced-finality)
11. [Commercial and investor material as secondary archive](#11-commercial-and-investor-material-as-secondary-archive)
12. [Knowledge registers and appendices](#12-knowledge-registers-and-appendices)

---

## 1. How to use this knowledge base

### 1.1 What this document preserves

EcoFarm has accumulated several kinds of knowledge that should not be flattened into one confident story. Its records include the founder’s original vision of an integrated agricultural technology company; broad product, hardware, software, sensor, and marketplace concepts; regional agricultural research; historical technical-stack choices; design flows; field-research protocols; direct source tests; and recent safety constraints. The correct use of this document is therefore **reconstruction before decision**.

When considering a feature, an outside reader should be able to locate five things: the problem it was meant to solve; the mental model that made it seem useful; the intended mechanism; the evidence and assumptions that supported it at the time; and the later information that narrowed, deferred, or challenged it. The fact that an idea is historical does not make it worthless. It means only that its authority and conditions must be visible.

### 1.2 Evidence and temporal labels

The source archive uses a two-part label: an **evidence-status code** and a **temporal status**. The most important codes are `FI` for a founder instruction or intent, `HV` for a historical vision, `PD` for a proposed design, `RH` for a research hypothesis, `SR` for secondary research/cited context, `DO` for a direct operational artifact, `OP` for an operating safety policy, `DA` for a deferred or rejected path, `UQ` for an unresolved question, and `AS` for an analytical or agent synthesis. Full definitions are preserved in the evidence-status taxonomy. [EF-GOV-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/00_governance_and_archive/EF-GOV-001__ecofarm_current_main_conversation_canonical_capture_2026_08_18.md "Current main conversation canonical capture; legacy SRC-0134") [EF-GOV-002](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/00_governance_and_archive/EF-GOV-002__ecofarm_current_session_approvals_and_requirements_2026_08_18.md "Current session approvals and requirements; legacy SRC-0135")

| Example | Correct interpretation | Incorrect interpretation |
|---|---|---|
| A 2025 onboarding document describes remote irrigation control. | Historical product and technical intent; a detailed idea worth preserving. | A deployed feature or current P0 commitment. |
| A field-launch kit contains a consent form and follow-up sequence. | Planned validation method and governance design. | Proof that all interviews or field events occurred. |
| A current test memo captures an HTTP 200 page that lacks Namakkal coverage. | Direct, bounded evidence that the tested source path failed target-locality checks. | Evidence that all official weather sources are unusable. |
| A founder statement describes a data-driven farming ecosystem. | Authoritative expression of intent. | Proof of market demand, feasibility, or regulatory approval. |

### 1.3 Reopening an old decision

This knowledge base is intentionally designed to make old decisions reopenable. A decision should not be reopened by reading only its conclusion. The reader should retrieve its source record, alternatives, assumptions, operating environment, and subsequent evidence. A historical marketplace idea, for example, may become sensible only if later field evidence demonstrates that price transparency or buyer access is the binding farmer problem; it should not be rejected merely because the first P0 is narrower.

### 1.4 Source conventions

The human-readable document uses internal references such as `[EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")`. They identify the source in the preserved corpus and should be read together with the source map. Where a source contains external primary references, those are retained in the relevant research entries. The LLM corpus exposes every canonical source in provenance-bearing chunks, making it possible to retrieve the exact source text rather than relying on this synthesis alone.

---

## 2. EcoFarm’s mental universe

### 2.1 The originating intuition

EcoFarm began as an intuition that farming decisions are not merely agricultural calculations. They are made under uncertainty, incomplete information, physical distance, labour constraints, financial pressure, changing weather, local advice, and unequal access to technology. The initial ambition was correspondingly broad: combine field hardware, sensor information, remote control, weather, crop intelligence, market awareness, farm management, community, and access to people or services into a single agricultural technology ecosystem. `[Private preservation trace; no public link]` [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

The early conceptual mistake to avoid is assuming that EcoFarm’s essence was a list of modules. The deeper thesis was that a farmer should not have to navigate every uncertainty through disconnected tools, physical visits, implicit local knowledge, or opaque commercial relationships. The envisioned system would make farm conditions and choices visible, connect them to relevant information, and give the farmer more control over both operations and decisions.

### 2.2 The original integrated-ecosystem model

The historical onboarding documents describe EcoFarm as an integrated hardware-and-software ecosystem. In that model, sensors, farm equipment, external data, human knowledge, and a mobile interface were not independent products. They were intended to form a feedback loop:

1. **Observe the farm and its context.** Gather sensor readings, weather, satellite or map context, crop-stage information, farmer-entered constraints, market observations, and historical records.
2. **Interpret the information.** Use rules, analytics, or later AI to identify meaningful conditions, compare options, detect risk, or show relevant guidance.
3. **Support or automate action.** Help a farmer decide, alert them, connect them to a source, schedule an operation, or remotely operate an enabled device.
4. **Record the action and outcome.** Preserve what the farmer did, why, and what happened so future decisions are not made without memory.
5. **Learn or improve.** Use the accumulated record carefully to improve explanation, contextual relevance, or future support without claiming causal certainty merely because data exists.

This loop remains essential as an **architectural mental model**, even though the current P0 should not assume the availability, accuracy, legality, or safety of every input or automation route. [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039") [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354")

### 2.3 The farmer is a decision-maker inside a system, not a generic app user

EcoFarm’s current research reframes the farmer from a generic “customer” into a decision-maker embedded in a household, farm, village, information network, market route, and environmental situation. A decision may be shaped by a spouse, parent, labourer, field manager, neighbour, input dealer, trader, agricultural officer, KVK, WhatsApp group, and the farmer’s own experience. The system must therefore avoid an individualistic model in which a single phone user receives a supposedly optimal answer and acts immediately. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

This implies several recurring mental models:

| Mental model | Intended meaning | Practical consequence |
|---|---|---|
| **Decision companion, not oracle** | EcoFarm should make constraints, options, reasons, sources, and uncertainty easier to understand. | Avoid a single unexplained “best” recommendation. |
| **Evidence layer, not information flood** | The value is often in making existing information comparable, timely, and attributable. | Do not duplicate weather pages or mandi tables without contextual value. |
| **Human-supervised system, not autonomous agronomist** | High-stakes decisions need source visibility, caveats, and escalation. | Fail closed when critical facts or authority are absent. |
| **Farm record with memory, not merely a dashboard** | Decisions and outcomes should become inspectable over time. | Log inputs, source time, rule/version, farmer action, change, rejection, and outcome. |
| **Ecosystem complement, not institutional replacement** | Existing officers, KVKs, markets, FPOs, dealers, peers, and public services matter. | Route, cite, and compare rather than claim to replace or partner with them. |
| **Local context before generic intelligence** | A technically correct statement can be wrong for a farmer’s crop stage, water situation, market, or objective. | Ask for context, show missing facts, and suppress inappropriate actions. |

### 2.4 The long-term ambition and the current wedge can coexist

The broad vision includes decision support, farm sensing, irrigation control, crop health, market access, financial awareness, community, resource sharing, and supply-chain concepts. The current research does **not** invalidate that imagination. It says that the first credible proof point should be far narrower: a human-supervised workflow around a repeated, consequential, information-addressable decision, beginning as a hypothesis with rainfed sowing and early-season response in Namakkal/Kongu. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

The relationship between the two is not “vision versus reality.” It is **architecture versus entry point**. The long-term vision describes what a connected agricultural operating system might eventually make possible. The current wedge asks what minimal, safe, observable intervention can establish whether EcoFarm adds useful value in a real decision moment.

### 2.5 Non-negotiable conceptual principles

The following principles recur across the current research and should be treated as foundational unless consciously reopened:

1. **No false precision.** The system should distinguish observation, forecast, interpretation, and recommendation.
2. **No silent substitution.** A nearby district, old bulletin, generic price, district average, or guessed value should not quietly replace missing local data.
3. **No hidden source authority.** The publisher, time, geographic basis, freshness, transformation, and limitation of a source should be inspectable.
4. **No automatic proof of demand.** An available data source, a historical feature, or farmer interest in a conversation does not establish repeated adoption.
5. **No unearned partnership language.** An institution may be a source or public contact without being an EcoFarm partner, reviewer, or distributor.
6. **No conversion of a plan into an outcome.** A research design, safety card, or test plan remains a plan until an event record demonstrates execution.
7. **No punishment for non-action.** A farmer’s rejection, change, or deferral is a meaningful result, not a failure to be hidden.

---

## 3. Historical evolution of the EcoFarm thesis

### 3.1 Phase A — Broad AI-enabled Agri-Tech company and mobile app

The earliest retained founder request described an AI-powered farming company with physical products and a mobile application. The physical side included remotely controllable motor starters, gate valves for water flow, drip-irrigation systems, sensor kits for soil conditions, and AI-enabled cameras for crop monitoring. The mobile side was intended to make these devices usable while also addressing weather, crop selection, crop management, farm mapping, budgeting, community, labour, equipment rental, direct/wholesale sale, market prices, disease diagnosis, and more. `[Private preservation trace; no public link]`

The important historical insight is not the number of features. It is that the initial model treated farm operations, agronomy, information, commerce, and social coordination as interconnected. Remote irrigation control without sensing or crop context was incomplete; crop advice without weather, budget, or market context was incomplete; market access without quality, logistics, labour, and farmer records was incomplete.

### 3.2 Phase B — Early product requirements, flows, and stack exploration

The first formal product material translated the broad vision into requirements, flows, wireframes, and technology choices. It introduced dashboards for sensor monitoring and alerts; mapped farm sectors; planning and recommendation flows; remote control; market and community screens; and feature-level technical decisions. [EF-PRD-002](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/02_product_concept_and_feature_mechanics/EF-PRD-002__mvp_screens_flows.md "MVP user flows and key screens outline; legacy SRC-0005") [EF-PRD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/02_product_concept_and_feature_mechanics/EF-PRD-001__prd_draft.md "Historical product requirements document; legacy SRC-0006") [EF-PRD-003](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/02_product_concept_and_feature_mechanics/EF-PRD-003__wireframes_part1.md "Low-fidelity wireframes part 1; legacy SRC-0023") [EF-PRD-004](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/02_product_concept_and_feature_mechanics/EF-PRD-004__wireframes_part2.md "Low-fidelity wireframes part 2; legacy SRC-0024")

The technical architecture at that stage proposed a cross-platform mobile application, backend services, cloud/IoT integration, databases, machine-learning frameworks, and long-range sensor communications. These documents are useful because they retain why certain categories were considered—not because their tools or framework choices should be adopted unchanged. The technology was selected around cross-platform access, telemetry, scalability, remote control, data storage, and the possibility of later analytics. [EF-TEC-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/03_technical_architecture_hardware_ai/EF-TEC-001__tech_stack_alternatives.md "Technology stack alternatives and trade-offs; legacy SRC-0008")–[EF-TEC-004](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/03_technical_architecture_hardware_ai/EF-TEC-004__tech_stack_research_hosting.md "Cloud hosting and scalability research; legacy SRC-0015")

### 3.3 Phase C — Hardware and sensor reasoning

Later onboarding work deepened the hardware argument. Soil moisture, pH, EC/NPK proxy signals, temperature, humidity, actuators, microcontrollers, gateways, and communications were considered not as isolated gadgets but as inputs to irrigation, nutrient, and crop-management support. The archive compares resistance, capacitance, FDR, TDR, glass-electrode, ISFET, electrical-conductivity, ion-selective, and optical sensing approaches. [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039") [EF-TEC-005](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/03_technical_architecture_hardware_ai/EF-TEC-005__grok_ecofarm_module_sensor_research.md "Preferred parseable Grok sensor-research export; legacy SRC-0025") [EF-TEC-005](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/03_technical_architecture_hardware_ai/EF-TEC-005__grok_ecofarm_module_sensor_research.md "Preferred parseable Grok sensor-research export; legacy SRC-0026") [EF-TEC-005](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/03_technical_architecture_hardware_ai/EF-TEC-005__grok_ecofarm_module_sensor_research.md "Preferred parseable Grok sensor-research export; legacy SRC-0029") [EF-TEC-005](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/03_technical_architecture_hardware_ai/EF-TEC-005__grok_ecofarm_module_sensor_research.md "Preferred parseable Grok sensor-research export; legacy SRC-0036")

The historical selection logic is still valuable:

- A sensor must be evaluated against accuracy, reliability, cost, durability, calibration burden, integration complexity, power, environmental conditions, and farmer-maintenance burden.
- Moisture sensing was treated as central because irrigation decisions depend on soil water, but the sources recognize soil-specific calibration and installation issues.
- pH sensing was treated as potentially useful for soil-health context, but calibration, fragility, and maintenance are material operating conditions.
- EC was treated as a lower-cost proxy for dissolved salts/nutrient context, not a direct, complete N-P-K measurement. This distinction is essential: an EC reading cannot safely be translated into a precise fertilizer prescription without calibration, local context, and other evidence.

### 3.4 Phase D — Comprehensive ecosystem and innovation framing

The EcoFarm/Smart Farming Ecosystem materials later expanded and reorganized the idea into an integrated company narrative, master-document architecture, proposal content, and innovation/hackathon framing. The project was positioned against resource scarcity, climate volatility, crop health risk, information asymmetry, market access, operational inefficiency, accessibility barriers, sustainability concerns, finance, loss, and extension gaps. [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039") [EF-DSN-008](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-008__smartfarmingecosystem_amasterdocumentforcom.pdf "Smart Farming Ecosystem master document; legacy SRC-0044") [EF-DSN-009](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-009__content_plan.md "ComSoc HackX content plan; legacy SRC-0048")–[EF-DSN-011](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-011__title_slide.html "Historical title-slide artifact; legacy SRC-0062")

These materials preserve a useful **problem-to-capability map**, but they should be read cautiously. They often rely on national/global figures, general sources, or forward-looking claims. They describe why an integrated platform might matter; they do not prove that an integrated platform is the first intervention farmers in Namakkal need.

### 3.5 Phase E — Regionalization, microcosms, and operational difficulty research

The current project workspace shifted attention from generic agriculture to differentiated contexts. It assembled national agricultural-crisis material, Tamil Nadu and Kongu analysis, Punjab comparison, microcosm profiles, and recommendation work. The resulting view is that agricultural problems vary by crop system, water regime, holding size, market structure, weather exposure, labour, institutional access, and local practice. [EF-REG-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/05_regional_microcosm_and_namakkal_research/EF-REG-001__all_microcosms_detailed_profiles.md "All agricultural microcosms detailed profiles; legacy SRC-0274") [EF-REG-002](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/05_regional_microcosm_and_namakkal_research/EF-REG-002__comparative_difficulties_kongu_vs_punjab.md "Kongu versus Punjab operational difficulties; legacy SRC-0285") [EF-REG-003](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/05_regional_microcosm_and_namakkal_research/EF-REG-003__comparative_microcosm_analysis_recommendation.md "Comparative microcosm analysis and recommendation; legacy SRC-0286") [EF-REG-004](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/05_regional_microcosm_and_namakkal_research/EF-REG-004__kongu_belt_operational_difficulties_detailed.md "Kongu Belt operational difficulties; legacy SRC-0300") [EF-REG-005](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/05_regional_microcosm_and_namakkal_research/EF-REG-005__kongu_belt_regional_analysis.md "Kongu Belt regional analysis; legacy SRC-0301") [EF-REG-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/05_regional_microcosm_and_namakkal_research/EF-REG-007__namakkal_kongu_belt_agricultural_problems.md "Namakkal and Kongu Belt agricultural problems; legacy SRC-0309") [EF-REG-009](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/05_regional_microcosm_and_namakkal_research/EF-REG-009__punjab_operational_difficulties_detailed.md "Punjab operational difficulties; legacy SRC-0314") [EF-REG-010](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/05_regional_microcosm_and_namakkal_research/EF-REG-010__tamil_nadu_agriculture_specific_analysis.md "Tamil Nadu agriculture-specific analysis; legacy SRC-0315")

The conceptual change is substantial: EcoFarm cannot sensibly begin with a universal “farmer” model. It needs a specific microcosm and a narrow decision context whose inputs, constraints, and outcomes can be understood.

### 3.6 Phase F — Current farmer-decision, ecosystem, and P0 safety work

Research Agent 1 and Research Agent 2 introduced the current discipline: treat farmers’ actual decisions, alternatives, information channels, data rights, provenance, safety, and operational failure states as primary design constraints. The resulting P0 is no longer defined by a broad app feature list. It is a candidate decision packet whose value must be established before expansion. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357") [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354") [EF-DAT-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-007__ecofarmp0operationaltestresultsmemo.md "P0 operational test results memo; legacy SRC-0370")

The most important evolution is from **“What can EcoFarm contain?”** to **“What repeated decision can EcoFarm safely help a particular farmer make better than the existing workaround?”**

---

## 4. Problem landscape and research knowledge

### 4.1 The layered problem map

The EcoFarm archive identifies several overlapping problem layers. They should not be treated as one undifferentiated “agriculture crisis.” A farmer may experience water uncertainty, input cost, disease risk, weather volatility, market opacity, labour scarcity, debt, access barriers, and information problems at once. Yet the binding constraint at a specific moment may be one of these, and software may not change all of them.

| Layer | Historical concern | EcoFarm’s intended relevance | Current caution |
|---|---|---|---|
| Natural resources | Water scarcity, inefficient irrigation, soil degradation, nutrient imbalance. | Monitoring, irrigation planning, soil context, efficiency. | Field-level data and calibration are required; district averages are insufficient. |
| Climate and weather | Rainfall uncertainty, extreme events, changing seasons. | Weather-linked decision support and alerts. | Forecasts may lack locality, freshness, rights, or action relevance. |
| Crop health | Pests, diseases, weeds, stress, late detection. | Observation, triage, education, escalation, later vision-based support. | Autonomous diagnosis or chemical advice is unsafe in P0. |
| Farm operations | Manual control, labour dependence, record gaps. | Remote control, schedules, tasking, and operating history. | Hardware and automation require separate field reliability, safety, and economic validation. |
| Markets | Price volatility, intermediaries, post-harvest loss, buyer asymmetry. | Observed market information, comparability, decision/outcome logging, later marketplace concepts. | No price prediction, buyer guarantee, or marketplace claim in initial work. |
| Knowledge and access | Generic advice, extension reach limits, digital divide, information overload. | Translation of evidence into a feasible local decision. | Existing channels are dense; the gap may be relevance/trust rather than absence. |
| Finance and risk | Cost pressure, credit, insurance, investment constraints. | Budgeting, cost visibility, risk-aware decisions, later services. | These structural constraints may not be addressable through information alone. |

### 4.2 Namakkal/Kongu as a starting context

Namakkal/Kongu is not selected because the archive proves it is the highest-value agricultural market. It is selected as a **practical microcosm hypothesis**: the founder has access; the region contains mixed crop systems and both rainfed and irrigated farming; desk research identifies substantial rainfed area and many smaller operational holdings; and public extension, weather, market, and institutional channels provide a rich environment in which to test duplication versus complementarity. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

The sources explicitly resist the claim that Namakkal farmers lack information. Formal agriculture departments, AECs, ATMA, KVK Namakkal, TNAU content, IMD/agromet services, market infrastructure, e-NAM, dealers, traders, peers, WhatsApp, and public/private apps all exist. The defensible gap hypothesis is narrower: **information may exist but be too generic, late, hard to compare, not trusted, or infeasible to act on in the farmer’s particular decision moment.** [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357") [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354")

### 4.3 Candidate farmer decision problems

The current farmer-problem report identifies three candidates. Their prioritization is an analytical judgment, not a survey result.

| Candidate decision | Why it matters | EcoFarm’s possible role | Boundary / risk |
|---|---|---|---|
| **Rainfed sowing and early-season response** | Rainfall and water uncertainty can compress the sow/wait/re-sow/adjust window; wrong timing can waste seed, labour, and preparation cost. | Compare a small number of feasible actions, show weather source/age, identify missing facts, record decision and follow-up. | Cannot guarantee rain, establishment, yield, seed quality, labour, credit, or price. |
| **In-season pest/disease/weed/moisture response** | Recurrent, urgent, and recordable events; farmers may receive conflicting advice. | Triage, contextual evidence capture, uncertainty display, and qualified human escalation. | No autonomous diagnosis, pesticide prescription, product brand, or dose recommendation from weak evidence. |
| **Harvest/storage/sale timing** | Financially consequential but entangled with quality, transport, storage, liquidity, debt, and buyer relationships. | Transparent market observation/comparison and decision/outcome record. | No “best price,” price forecast, buyer guarantee, or delayed-sale instruction without constraints. |

The research recommends testing rainfed sowing/early-season response as the primary field hypothesis, while retaining the second workflow as a close comparator and the third as a secondary research candidate. It does **not** establish that groundnut is the definitive segment, that farmers prefer an app, or that a paid product exists. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

### 4.4 Workarounds are part of the product environment

EcoFarm’s relevant competitors are not only software products. A farmer may use experience, family, neighbours, progressive farmers, dealers, traders, agricultural officers, KVK staff, FPOs, WhatsApp, video, television, SMS, IMD, e-NAM, regulated markets, insurance documents, or non-action. The product should therefore analyze the **advice stack** behind a past decision: what sources were consulted, what conflicted, why one was trusted, what constraints ruled out options, and what happened afterward. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

This changes the meaning of “trust.” Trust is not a brand-impression metric. It is the farmer’s ability to understand why a source should matter, what it does not know, whether it fits local conditions, and when a human source is more appropriate.

### 4.5 Research evidence boundaries

The current archive contains valuable desk research and detailed field methods, but it is not a substitute for completed customer discovery. The following remain unresolved: repeated decision frequency across independent farmers; current use and trust of advisory channels; household decision authority; local language and assisted-use preference; willingness to share information; willingness to act; and the extent to which a software workflow can alter an outcome constrained by rainfall, labour, credit, storage, land, or buyer power. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357") [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354")

The correct research posture is therefore: **record rich hypotheses, test them against real decisions, preserve negative evidence, and change or stop the product hypothesis when the decision is not repeated, addressable, or safely measurable.**

---

## 5. Conceptual system models

This section describes EcoFarm as a collection of interacting models. These are not implementation commitments. They are the conceptual machinery needed to understand why individual features existed and how they were expected to relate to one another.

### 5.1 Farmer context and decision-authority model

**Purpose.** Represent the conditions that make an action feasible for a particular farm and decision-maker. The model is not a generic profile page. It is an evolving record of the facts necessary to avoid irrelevant guidance.

**Intended inputs.** Location or village/block; field identifier; crop and variety if known; crop stage; sowing date/window; holding and water context; soil-test date/value if available; recent weather observation; seed, labour, cash, storage, transport, and input constraints; objective; existing advice sources; language and assisted-use needs; and the person or household members who influence the decision. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

**Conceptual working.** EcoFarm would begin a named decision by asking only for the context essential to that decision. It would validate whether a crop stage, location scope, source date, or constraint is missing. The system would not infer missing facts from district averages or an old profile. If a critical condition is absent, the system should ask a clarifying question, narrow the output, or refer the user rather than generate a plausible-looking answer.

**Mental model.** A farmer context is an *evidence envelope* around an action. It defines the boundaries within which external sources, historical records, and rules may be considered relevant. A decision is unsafe when the envelope is too incomplete.

**Current status.** `PD` / `current_working` for the P0 data dictionary and consent map; broader historical profile concepts remain `HV`. [EF-DAT-003](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-003__ecofarmp0decision_packetdatadictionaryandconsentmap.md "P0 decision-packet data dictionary and consent map; legacy SRC-0366") [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

### 5.2 Farm, crop, and production-state model

**Purpose.** Represent the farm not just as acreage but as fields, sectors, crop cycles, stages, water access, inputs, activities, and observations. Historical materials imagined field mapping and crop-sector views; current work narrows this to the minimum state required to interpret an event. [EF-PRD-002](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/02_product_concept_and_feature_mechanics/EF-PRD-002__mvp_screens_flows.md "MVP user flows and key screens outline; legacy SRC-0005") [EF-PRD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/02_product_concept_and_feature_mechanics/EF-PRD-001__prd_draft.md "Historical product requirements document; legacy SRC-0006") [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

**Conceptual working.** A field can have one or more crop cycles. A crop cycle has a crop, dates, stage, water regime, relevant observations, planned activities, and events. The system should avoid turning a static crop name into a generic treatment: crop stage and recent conditions determine whether a statement has timing relevance. Over time, the model could support comparisons among fields or seasons, but an early pilot should use it only to anchor a named decision.

**Mental model.** A farm is a *time-varying operational system*, not a pin on a map. A field map, satellite view, or dashboard is useful only when it helps someone connect an observation to an actionable context.

### 5.3 Decision-support and option-comparison model

**Purpose.** Make a farmer’s decision space inspectable without claiming omniscience. This is the central current product model.

**Conceptual working.** The workflow receives a trigger—for example, an approaching sowing window, a field symptom, or a sale decision—and constructs a small set of feasible options. Each option should expose its assumptions, supporting sources, timing, constraints, missing facts, and the reasons it may not be feasible. The output is not “the best crop” or “the correct action.” It is a comparison that enables the farmer and, where relevant, a human adviser to reason more clearly.

The system should record the farmer’s actual choice, any change from the initial choice, the reason for the choice, and later observations. That record is the bridge between an attractive suggestion and a testable product hypothesis. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357") [EF-FLD-003](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-003__ecofarmdecision_journeytables.md "Decision journey tables; legacy SRC-0351") [EF-FLD-004](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-004__ecofarmdecisionoperationalizationsheets.md "Decision operationalization sheets; legacy SRC-0352") [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354")

**Mental model.** A decision packet is a *transparent case file*. It contains farmer context, source records, transformation rules, alternatives, unknowns, action, and outcome. It is not merely a recommendation card.

### 5.4 Risk, uncertainty, and failure-state model

**Purpose.** Prevent the interface from turning uncertain inputs into certainty.

**Conceptual working.** Every source-dependent output must carry information about source, time, geography, validity period, freshness, scope, and transformations. If the source is stale, empty, malformed, unauthorized, geographically mismatched, semantically non-comparable, conflicting, or not approved for transformation, the relevant action prompt must be suppressed. The safe output should explain what is unavailable and offer a neutral next action, not manufacture a substitute. [EF-DAT-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-007__ecofarmp0operationaltestresultsmemo.md "P0 operational test results memo; legacy SRC-0370") [EF-DAT-010](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-010__ecofarmsource_failureandprovenanceobservabilityplan.md "Source-failure and provenance observability plan; legacy SRC-0377") [EF-DAT-013](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-013__ecofarmweatherandadvisorysourcehierarchy.md "Weather and advisory source hierarchy; legacy SRC-0380") [EF-DAT-016](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-016__observability_simulated_failure_records.jsonl "Observability simulated failure records; legacy SRC-0386")

**Mental model.** Uncertainty is not a score to hide behind. It is an *operating state*. A state change—from current to stale, comparable to non-comparable, or source-aligned to source-conflicted—changes what the system is permitted to say.

### 5.5 Evidence, provenance, and transformation model

**Purpose.** Preserve the path from an original fact to a farmer-facing statement.

**Conceptual working.** A source record should retain publisher, URL or source identifier, retrieval time, issue time, validity period, target geography, relevant crop/action scope, version or ETag where available, rights/terms status, raw text or reference, and freshness classification. A transformation from source to action wording must be documented and deterministic. For example, a forecast indicating rain might support a cautious prompt to inspect whether a spray can be delayed; it must not become a guaranteed recommendation to sow on a given date. [EF-DAT-013](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-013__ecofarmweatherandadvisorysourcehierarchy.md "Weather and advisory source hierarchy; legacy SRC-0380")

**Mental model.** Provenance is a *chain of accountability*: input → source → transformation → output → farmer action. A source visible on the internet is not automatically a source permitted for automated storage, transformation, or redistribution.

### 5.6 Human-advice, referral, and ecosystem model

**Purpose.** Clarify where automation ends and human or institutional support begins.

**Conceptual working.** EcoFarm may identify a public contact, source, or possible escalation route only with neutral wording and source/date provenance. It should not claim institutional endorsement, response-time commitments, data-sharing arrangements, or case acceptance without agreement. For material uncertainty, unsafe symptoms, or source conflicts, the workflow should downgrade to information, caution, or referral. [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354") [EF-DAT-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-007__ecofarmp0operationaltestresultsmemo.md "P0 operational test results memo; legacy SRC-0370") [EF-DAT-009](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-009__ecofarmsafereferralandescalationdesign.md "Safe referral and escalation design; legacy SRC-0374")

**Mental model.** The product is a *router and evidence organizer*, not a substitute for a local officer, KVK, agronomist, dealer, trader, or household decision process.

### 5.7 Outcome-learning and memory model

**Purpose.** Learn from actual decision journeys without exaggerating causal knowledge.

**Conceptual working.** Preserve the initial context, source records, recommendation/option display, actual action, user modification or rejection, follow-up observation, and escalation event. Over many cases, the data might show patterns, recurring missing data, friction points, or branches that farmers reject. It cannot by itself prove that EcoFarm caused yield, profit, or better outcomes because crop, weather, quality, labour, and market conditions confound the record. [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354") [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

**Mental model.** An outcome log is a *learning ledger*, not a performance-marketing engine.

### 5.8 Trust, localization, and assisted-use model

**Purpose.** Make the system usable in environments where language, literacy, connectivity, household authority, and local practice affect whether a decision aid is meaningful.

**Conceptual working.** The system should support Tamil-first and assisted use, low-bandwidth or offline-safe review where relevant, plain-language explanation of what is observed versus forecast, easy correction of inputs, and comparison with existing trusted sources. The goal is not to remove human judgement; it is to make assumptions and trade-offs visible enough for a farmer to evaluate with their own network. [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354") [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

**Mental model.** Trust is built through *legibility and restraint*: show where the information came from, what it does not know, and when it is inappropriate to act.

---

## 6. Feature and capability dossiers

Each dossier records a concept’s original intention, its intended mechanics, dependencies, current interpretation, and unanswered questions. Status labels are deliberately reversible.

### 6.1 Crop-option comparison and crop recommendation

| Field | Knowledge record |
|---|---|
| **Historical intent** | Help a farmer decide what crop to plant using soil conditions, weather until harvest, market demand, budget, and preference. `[Private preservation trace; no public link]` |
| **Underlying intuition** | Crop choice is a consequential decision made under multiple constraints; an answer should not be based on a single factor such as price or weather. |
| **Conceptual working** | Collect season, location, water reliability, crop history, available inputs/labour, soil-test availability, farmer objective, and constraints. Compare a small set of feasible crop options against explicit assumptions, source-labelled context, trade-offs, and unknowns. Present questions for a human adviser when information is insufficient. |
| **Required data** | Location, season, water category, crop/land context, labour/input/cash constraint, farmer objective, and ideally current soil/test evidence. |
| **Trust mechanism** | Explain why an option is shown, which inputs matter, which are missing, and why it is not a profitability guarantee. |
| **Failure behaviour** | No ranking when critical facts are missing; do not silently substitute district averages; refer when local agronomic conditions cannot be supported. |
| **Current interpretation** | `RH` / `PD`. A candidate workflow for field validation, not an approved autonomous recommendation engine. [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354") |
| **Open questions** | Which crop decision recurs often enough? Are the relevant constraints recordable? Does a transparent comparison outperform existing human advice or merely add complexity? |

### 6.2 Weather-linked decision support

| Field | Knowledge record |
|---|---|
| **Historical intent** | Provide accurate weather data, localized forecasts, adverse-weather alerts, and weather-informed planting, irrigation, and crop-care guidance. `[Private preservation trace; no public link]` [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039") |
| **Underlying intuition** | Weather alters the timing and risk of farm operations; a farmer needs actionable context rather than a raw number. |
| **Conceptual working** | Match a target-location forecast/advisory and validity period to a named crop-stage decision. Preserve source, time, location, freshness, forecast/observation distinction, and transformation rule. Produce only information, caution, or referral states. |
| **Required data** | Approved target-relevant source, rights/terms status, issue/retrieval/validity time, location scope, crop stage, intended action window. |
| **Trust mechanism** | Show publisher, source type, geographic scope, time, period, caveat, and original link/reference. |
| **Failure behaviour** | Suppress output if stale, absent, mismatched, malformed, conflicting, rate-limited, or transformation-unverified. |
| **Current interpretation** | `DA` for the tested automated TNAU district bulletin path in first P0; `PD` / `UQ` for the wider concept pending separate source approval. [EF-DAT-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-007__ecofarmp0operationaltestresultsmemo.md "P0 operational test results memo; legacy SRC-0370") [EF-DAT-013](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-013__ecofarmweatherandadvisorysourcehierarchy.md "Weather and advisory source hierarchy; legacy SRC-0380") |
| **Open questions** | What official target-local source has usable rights, stable coverage, action relevance, and failure semantics? How should farmers interpret forecast uncertainty in a local decision? |

### 6.3 Market observation, price context, and sale decision support

| Field | Knowledge record |
|---|---|
| **Historical intent** | Show market prices near the farm, help farmers negotiate or decide where/when to sell, connect to buyers, and later reduce intermediary dependence. `[Private preservation trace; no public link]` [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039") |
| **Underlying intuition** | Farmers may make sales under asymmetric information and may benefit from clearer observations, comparisons, and memory of prior decisions. |
| **Conceptual working** | Capture commodity, variety, grade where available, market, date, unit, observed min/max/modal price, and farmer constraints such as transport, storage, cash needs, quality, and buyer relationship. Display only comparable observations and log the actual route/decision/outcome. |
| **Required data** | Decision-relevant crop/market selection, source rights, freshness, unit/variety/grade semantics, transport/storage/liquidity context. |
| **Trust mechanism** | Label prices as observed, show market/date/unit/variety, disclose gaps, and never represent an observation as a forecast. |
| **Failure behaviour** | Hide non-comparable, missing, stale, or semantically mismatched records; do not interpolate or promise a buyer. |
| **Current interpretation** | `RH` / `PD`; market context is excluded from the presently constrained P0 until a specific crop/market semantic test exists. [EF-DAT-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-007__ecofarmp0operationaltestresultsmemo.md "P0 operational test results memo; legacy SRC-0370") |
| **Open questions** | Does information change action once liquidity, debt, quality, and buyer relations are accounted for? Which local crops and markets are meaningful? |

### 6.4 Farm mapping, field sectors, satellite context, and land observation

**Historical intent.** Let a farmer map farmland, divide it into crop sectors, obtain satellite views, and later identify stressed areas or overall field performance. `[Private preservation trace; no public link]` [EF-PRD-002](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/02_product_concept_and_feature_mechanics/EF-PRD-002__mvp_screens_flows.md "MVP user flows and key screens outline; legacy SRC-0005") [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

**Conceptual working.** A field map would associate a physical area with crop cycle, sensor placement, water zone, activity history, and observations. Satellite imagery or remote sensing could later provide a coarse contextual signal. The map is valuable when it helps link observations and actions to the correct field, rather than being a decorative visualization.

**Boundary.** Satellite or remote signals cannot by themselves reliably diagnose crop health, disease, yield, irrigation need, or farmer intent in a small pilot. They are therefore historical/future context or a later validation signal, not a primary early recommendation input. [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354")

### 6.5 Soil, water, sensor, and field-condition intelligence

**Historical intent.** Provide continuous awareness of soil moisture, pH, nutrient context, temperature, humidity, and other relevant conditions so that irrigation, fertilizer, and crop-management decisions can be less blind. [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

**Conceptual working.** Sensors or farmer-held test records produce observations. Those observations must be timestamped, associated with a field/zone, checked for calibration and plausibility, and interpreted in relation to crop stage, soil type, water source, and weather. Historical system designs connect this context to alerts, trends, irrigation schedules, and nutrient guidance.

**Key mental model.** A reading is not a recommendation. Soil moisture, pH, EC, or an estimated NPK-related value becomes useful only after questions of calibration, sensor placement, maintenance, environmental conditions, local baseline, and decision relevance are answered.

| Sub-capability | Historical conceptual mechanism | Key limitation to preserve |
|---|---|---|
| Soil moisture | Capacitance/FDR/TDR/resistance approaches signal water content or related condition for irrigation decisions. | Soil-specific calibration, salinity/temperature effects, installation, durability, and the difference between signal and crop need. |
| Soil pH | Glass, ISFET, or other probes estimate acidity/alkalinity relevant to nutrient availability. | Calibration, cleaning, temperature effects, fragility, drift, and representativeness. |
| Nutrient context | EC may provide a proxy for dissolved salts/nutrient context; ISE/optical options were also considered. | EC does not directly differentiate N, P, and K; it must not be converted into a precise fertilizer prescription without ground-truth and expert context. |
| Temperature/humidity | Ambient or field conditions support crop/alert interpretation. | Sensor quality, placement, contamination, drift, and whether the reading represents the crop microclimate. |
| Farmer-held soil test | A date-stamped laboratory report can serve as context. | Consent, age, units, spatial representativeness, and no silent substitution with district averages. |

**Current interpretation.** `HV` and `PD` for the long-term hardware system; `UQ` / permission-dependent for farmer-specific soil/water data in P0. [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039") [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354") [EF-DAT-003](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-003__ecofarmp0decision_packetdatadictionaryandconsentmap.md "P0 decision-packet data dictionary and consent map; legacy SRC-0366")

### 6.6 Irrigation control, automation, and remote operation

**Historical intent.** Allow farmers to remotely control motor starters, pumps, valves, irrigation zones, and later automated schedules; connect control to soil and weather information. `[Private preservation trace; no public link]` [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

**Conceptual working.** A farmer or authorized operator sees a status, chooses a manual action or approved schedule, and sends a command through a gateway/actuator system. The system should acknowledge command state, report actual device status rather than only desired state, log who acted and when, and surface safety or connectivity failures. Longer-term automation would require conservative rules, overrides, water/resource context, and owner control.

**Mental model.** Remote control is a *safety-critical operating interface*, not a convenience toggle. The difference between a command sent, command received, and valve/pump actually changed is material.

**Current interpretation.** `HV` / future hypothesis. Current decision-packet P0 explicitly does not include hardware control. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357") [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354")

### 6.7 Nutrient management and fertilizer support

**Historical intent.** Use soil/nutrient information, crop type, and growth stage to guide fertilizer choice, timing, and quantity. [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

**Conceptual working.** A safe version would begin from a documented soil/test context, crop/stage, known constraints, and an authoritative, versioned guideline. It would distinguish a general education reference from a location-specific prescription and surface missing facts or an escalation path.

**Boundary.** Current P0 safety rules prohibit pesticide, fertilizer, or disease-treatment instructions when crop, stage, symptom, product, dose, or local regulatory facts are insufficient. The long-term concept remains preserved, but no automatic nutrient recommendation should be inferred from sensor data alone. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

### 6.8 Crop health, pest, disease, and image-based support

**Historical intent.** Combine user-uploaded photos, AI-enabled cameras, monitoring, early detection, and localized management guidance to help identify disease, pest, and crop-health issues. `[Private preservation trace; no public link]` [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

**Conceptual working.** A symptom event would collect crop, stage, location, timing, visible symptoms, recent weather, treatment history, and possibly photographs. The system could classify the evidence as insufficient, suggest basic observation or a safe educational reference, compare possible categories, or route it to human review. A future image model might add an evidence signal, but it must retain confidence, quality, and provenance rather than replace context.

**Boundary.** One photograph, generic symptom description, or weak model output cannot establish a treatment. The current bounded concept is triage and escalation; no autonomous pesticide prescription, product brand recommendation, diagnosis claim, or assurance of safety. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357") [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354")

### 6.9 Growth tracking, yield estimation, and crop-calendar support

**Historical intent.** Track crop stages, guide pre-planting through harvest, show timely activities, predict yield, and connect activity timing to weather, sensors, and field observations. `[Private preservation trace; no public link]` [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

**Conceptual working.** A crop cycle contains stage and event milestones. A calendar or workflow should identify what activity is relevant, what source/guide supports it, and what variables make timing conditional. Historical yield estimation would combine history, sensors, crop conditions, and models; current thinking recognizes that this is a future hypothesis requiring ground truth and careful communication.

**Boundary.** Calendar guidance is not a guarantee that a crop will perform as planned. Yield estimates are not profit promises and should not be presented as precise without validated local models and data quality controls.

### 6.10 Farm logs, tasks, budget, and seasonal planning

**Historical intent.** Give farmers a way to record tasks, plan a budget for a season, monitor use of resources, track expenses/revenue, and create operational memory. `[Private preservation trace; no public link]` [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

**Conceptual working.** A farmer or assisted operator creates activities, costs, inputs, events, actions, and outcomes. These records may later support budget views, historical patterns, or decision review. In the current narrow model, the most important logging function is not general productivity tracking; it is recording the input, choice, reason, and outcome of a named decision.

**Current interpretation.** The broad farm-management suite is `HV` / future candidate. Decision and outcome logging is `PD` / current working candidate because it is necessary to test whether EcoFarm changes behavior. [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354") [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

### 6.11 Community, peer exchange, labour, equipment rental, and marketplace concepts

**Historical intent.** Enable farmer communities, peer knowledge sharing, equipment rental, labour/harvesting access, fertilizer-shop discovery, direct retail/wholesale sale, and marketplace relationships. `[Private preservation trace; no public link]` [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

**Underlying intuition.** Many farm constraints are social and operational, not merely informational. Farmers may need trusted people, tools, labour, markets, and exchange channels as much as they need a forecast.

**Conceptual working.** A future community/resource system would need identity, listing, availability, location, permissions, pricing/terms, reputation or verification, dispute boundaries, logistics, and safety controls. A marketplace would need quality, grade, inventory, transport, payment, buyer eligibility, and regulatory/legal design. These mechanisms are substantially more complex than an information feature.

**Current interpretation.** Preserve as `HV` / long-term ecosystem concepts. They are explicitly outside the narrow current P0 because no local need, trust model, transaction process, safety approach, or business logic has yet been validated. [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354")

### 6.12 Financial, insurance, buyer-access, and supply-chain concepts

Historical documents include budget planning, expense/revenue tracking, market access, direct buyer connection, financial services, insurance context, and later possible supply-chain transparency. These ideas share a common intuition: crop decisions are financial decisions, and a farmer’s ability to act depends on cash, credit, risk, quality, logistics, and buyer power. [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

The current research preserves them as context but warns that neither a price display nor a digital record solves liquidity, debt, storage, grading, transport, or relationship constraints. These capabilities require future evidence and, in several cases, regulated partnerships or transaction infrastructure. They should remain visible in the long-term map without being smuggled into the first product wedge.

---

## 7. Technical and data-system archive

### 7.1 Historical architecture intent

Historical EcoFarm designs proposed an interconnected mobile, backend, cloud, IoT, analytics, and hardware stack. The named technologies changed across documents, but the responsibilities were relatively stable: mobile/assisted interaction; application services; data storage; device/gateway connection; external-source adapters; analytics/AI; notifications; and hardware control. [EF-TEC-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/03_technical_architecture_hardware_ai/EF-TEC-001__tech_stack_alternatives.md "Technology stack alternatives and trade-offs; legacy SRC-0008")–[EF-TEC-004](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/03_technical_architecture_hardware_ai/EF-TEC-004__tech_stack_research_hosting.md "Cloud hosting and scalability research; legacy SRC-0015") [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

This should be preserved as an **architecture of responsibilities**, not as a frozen technical stack. A current implementation may use different frameworks, databases, or managed services without abandoning the original conceptual model.

| Architectural layer | Historical intended responsibility | Relevance to current knowledge base |
|---|---|---|
| Farmer-facing interface | Show context, field state, sensor readings, choices, alerts, tasks, market/knowledge views, and controls. | Current P0 requires only an assisted, transparent decision packet and safe source states. |
| Core application/service layer | Manage identities, farm/crop records, decisions, logs, permissions, source adapters, notifications, and workflows. | Decision records, consent, source metadata, and immutable logging remain central. |
| Data layer | Store user/farm records, observations, sensor data, source records, actions, and outcomes. | Must distinguish personal/farm data from public source data; retain deletion and provenance policies. |
| Integration layer | Connect weather, market, advisory, map, satellite, device, and institutional sources. | Every integration must pass rights, locality, freshness, semantics, provenance, and failure-behaviour gates. |
| IoT/gateway layer | Relay sensor readings and device commands across field connectivity constraints. | Long-term; needs command acknowledgement, offline behaviour, calibration, and physical safety. |
| Intelligence layer | Apply deterministic rules, analysis, future ML, or image models. | Begin with documented conservative rules; preserve inputs/rule version; no unexplained high-stakes automation. |
| Audit/observability layer | Track source state, data flow, output, user action, errors, overrides, and escalation. | A current non-negotiable P0 control. |

### 7.2 The minimum technical contract for a decision packet

The current data-feasibility and P0 documents converge on a small but rigorous technical contract. A decision-support system should not start with a model. It should start with a record that can be inspected after the event.

| Record / component | Required conceptual contents | Why it matters |
|---|---|---|
| **Farmer context record** | Purpose-specific consent, language, location/block, crop, stage, intended timing, water category, constraints, and objective. | Establishes relevance and protects against overbroad data collection. |
| **Source record** | Publisher, URL/ID, retrieval time, issue/validity time, geography, raw/source reference, version, rights state, freshness and completeness state. | Allows a reader to see what the system relied on. |
| **Transformation record** | Deterministic rule/version that converted source/context into an informational, caution, or referral state. | Prevents opaque leap from data to advice. |
| **Packet/output record** | Options, assumptions, unknowns, display state, source references, explanation, and any escalation trigger. | Makes the output reviewable. |
| **Decision/action record** | Farmer acceptance, rejection, modification, reason, timing, and any human consultation. | Separates viewed content from actual behaviour. |
| **Follow-up/outcome record** | Later observation, unresolved issue, or outcome context. | Supports learning without pretending to establish causality. |
| **Observability record** | Source failure, parser/error state, suppression, logs, and recovery status. | Ensures a failure is visible rather than silently converted into bad advice. |

### 7.3 Source-adapter gate

An external source must not be treated as usable merely because it has a public webpage, a logo, an HTTP success, or a data-looking response. The P0 work defines a more stringent gate:

1. **Access:** Can the intended system legally and technically retrieve the source?
2. **Rights:** Are automated retrieval, caching, transformation, translation, storage, and farmer-facing redistribution permitted?
3. **Freshness:** Are source time and validity period sufficient for the decision moment?
4. **Locality:** Does the source explicitly cover the farmer’s relevant geography and condition?
5. **Semantics:** Do the source fields mean what the workflow assumes—commodity/variety/unit, forecast period, crop stage, and so on?
6. **Provenance:** Can the raw/source record and version be retained and shown?
7. **Failure behaviour:** Can the system recognize and safely handle empty, stale, malformed, unauthorized, conflicting, or out-of-area responses?

Only then can a source become a candidate for a specific farmer-facing transformation. [EF-DAT-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-007__ecofarmp0operationaltestresultsmemo.md "P0 operational test results memo; legacy SRC-0370") [EF-DAT-010](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-010__ecofarmsource_failureandprovenanceobservabilityplan.md "Source-failure and provenance observability plan; legacy SRC-0377") [EF-DAT-013](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-013__ecofarmweatherandadvisorysourcehierarchy.md "Weather and advisory source hierarchy; legacy SRC-0380")

### 7.4 The TNAU weather-path test as a design lesson

The P0 operational test is important because it demonstrates the difference between *technical availability* and *decision readiness*. The selected TNAU public district Agro-Met Advisory Bulletin page returned public HTTP responses and had a visible publication period. However, the tested page stated that Namakkal district weather details were unavailable, and the page showed an “All Rights” notice without identified permission for EcoFarm’s proposed automated reuse, transformation, storage, or redistribution. [EF-DAT-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-007__ecofarmp0operationaltestresultsmemo.md "P0 operational test results memo; legacy SRC-0370")

The result is not “TNAU is bad” or “weather support is impossible.” The precise result is that the **tested automated path was rejected for the first P0 workflow** because it failed target-locality and rights checks. The appropriate user state is not a substitute forecast. It is: *no current Namakkal decision-ready weather advisory is available from this source; EcoFarm is not using an older, general, or substitute value.* [EF-DAT-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-007__ecofarmp0operationaltestresultsmemo.md "P0 operational test results memo; legacy SRC-0370")

This is a core EcoFarm mental model: a system earns trust by refusing to fill an evidence gap with confidence.

### 7.5 Data-source hierarchy for weather/advisory material

The intended hierarchy for a weather/advisory decision packet is as follows. It is a proposed operating model, not a claim that each source is currently approved. [EF-DAT-013](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-013__ecofarmweatherandadvisorysourcehierarchy.md "Weather and advisory source hierarchy; legacy SRC-0380")

| Priority | Source class | Permitted conceptual role | Core restriction |
|---:|---|---|---|
| 1 | Target-relevant official warning/forecast via approved API or current official page | Raw warning/forecast and cautious source-labelled prompt. | Must identify target geography and valid period. |
| 2 | Target-covered current IMD/TNAU agromet bulletin | Human-reviewed advisory reference; later automated display only after rights test. | Never label district/block guidance as plot-specific. |
| 3 | Target-block local weather record | Corroboration/local context after validation. | Must retain timestamp and expected update interval. |
| 4 | Secondary public provider | Internal comparison or outage diagnostic. | Not a first-P0 farmer-facing authority without separate approval. |
| 5 | Farmer/local observation | Explicitly labelled context or clarifying input. | Never replace official warning/forecast. |

### 7.6 Historical IoT and hardware control implications

The original architecture imagined STM32-class microcontrollers, gateways, LoRaWAN or Wi-Fi/GSM connectivity, sensor nodes, relays, motor starters, and valves. These choices encode several operational concerns: field range, power consumption, intermittent connectivity, low-level device integration, and remote-control needs. [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039")

A future hardware system would need to preserve at least the following distinctions:

- **Measurement versus state.** A sensor reading may be stale, noisy, or uncalibrated; a device’s commanded state may differ from actual state.
- **Request versus acknowledgement.** “Turn on” is not proof that a pump switched; the system needs command, acknowledgement, confirmation, timeout, and override events.
- **Automation suggestion versus automation execution.** An irrigation schedule based on a general rule is not a safe actuation authority without hardware safeguards, owner permission, and local constraint checks.
- **Device ownership versus user access.** Household or farm ownership, operator authorization, shared infrastructure, and emergency overrides are distinct.
- **Remote availability versus safe fallback.** Connectivity loss must leave physical systems in a predictable, locally controllable state.

### 7.7 AI, rules, and explainability

EcoFarm’s historical vision includes AI for crop choice, crop management, yield estimation, disease detection, image analysis, market insight, and predictive analytics. The current P0 work introduces a more disciplined ordering: first establish source quality, local relevance, consent, safe failure states, and decision recording; then use documented deterministic transformations; only later consider higher-complexity models where validation and accountability support them. [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039") [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354")

| Level | Intended role | Evidence/accountability requirement |
|---|---|---|
| **Reference retrieval** | Show official guidance, public source, or farmer-entered record with attribution. | Source, date/version, scope, and rights. |
| **Deterministic rule** | Map explicit conditions to informational/caution/refer output. | Rule version, required inputs, exceptions, and testable failure handling. |
| **Analytical comparison** | Compare options against explicit constraints. | Assumptions, missing data, trade-offs, and human review trigger. |
| **Predictive/ML system** | Estimate future condition or recognize a pattern. | Local validation, input quality, uncertainty calibration, monitoring, override, and non-harm boundaries. |
| **Autonomous action** | Trigger an operation or high-stakes recommendation. | Strongest controls: authorization, physical safety, real-world validation, audits, and emergency fallback. |

No level should impersonate the authority of a higher one. A market observation is not a price forecast; a weather forecast is not a crop outcome; an image similarity is not a diagnosis; a suggestion is not a command; an automation proposal is not a safe actuator state.

---

## 8. Trust, safety, consent, and governance

### 8.1 Core safety posture

The current operating principle is **fail closed, explain why, preserve human control**. A system should suppress or narrow an output when critical data is missing or unreliable, rather than reward itself for always producing an answer. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357") [EF-DAT-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-007__ecofarmp0operationaltestresultsmemo.md "P0 operational test results memo; legacy SRC-0370") [EF-DAT-013](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-013__ecofarmweatherandadvisorysourcehierarchy.md "Weather and advisory source hierarchy; legacy SRC-0380")

### 8.2 Explicit non-claims and red lines

EcoFarm should not claim or imply that it guarantees yield, profit, rainfall, buyer access, price, insurance settlement, crop health, or farmer outcome. It should not represent public institutions as partners, reviewers, distributors, or committed case handlers without written evidence. It should not make autonomous pesticide, fertilizer, disease-treatment, or high-stakes irrigation claims from insufficient context. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357") [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354") [EF-DAT-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-007__ecofarmp0operationaltestresultsmemo.md "P0 operational test results memo; legacy SRC-0370")

| Domain | Safe statement | Unsafe statement |
|---|---|---|
| Weather | “A source indicates rain for the stated location and period; confirm local conditions.” | “Rain will ensure crop establishment.” |
| Market | “Observed modal price for this market/date/variety is shown.” | “This is the best price; wait for higher returns.” |
| Crop health | “Information is insufficient; capture context or consult a qualified source.” | “This photo proves the disease; apply this product.” |
| Institutions | “Public contact information for independent verification.” | “KVK/department will review or endorses your case.” |
| Recommendation | “This option appears feasible under listed assumptions.” | “This is the correct or most profitable action.” |

### 8.3 Consent and data minimization

Farmer data should be collected only for a named purpose. At a minimum, the person should be able to understand why information is requested, what the output requires, who can access the record, how to correct it, and how to request deletion. The field set must be proportionate to the decision: collecting a detailed farm profile “just in case” conflicts with the current safety posture. [EF-FLD-006](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-006__ecofarmattributionandfield_dataqualityprotocol.md "Attribution and field-data quality protocol; legacy SRC-0342") [EF-DAT-003](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-003__ecofarmp0decision_packetdatadictionaryandconsentmap.md "P0 decision-packet data dictionary and consent map; legacy SRC-0366") [EF-FLD-013](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-013__ecofarmprimarypilotcohortanddecision_authorityprotocol.md "Primary pilot cohort and decision authority protocol; legacy SRC-0372") [EF-FLD-014](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-014__ecofarmrecruitmentandconsentpack.md "Recruitment and consent pack; legacy SRC-0373")

The consent model must distinguish three categories:

1. **Farmer-entered decision context:** purpose-specific and removable, subject to validation.
2. **Public source references:** public visibility does not automatically create transformation/redistribution rights.
3. **Partner or institutional records:** require a documented agreement and, where relevant, farmer authorization before case data is sent.

### 8.4 Source-failure states

The current design artifact simulates eight failure states. These simulations are not live-integration approval, but they establish the intended fail-closed behaviour. [EF-DAT-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-007__ecofarmp0operationaltestresultsmemo.md "P0 operational test results memo; legacy SRC-0370") [EF-DAT-016](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-016__observability_simulated_failure_records.jsonl "Observability simulated failure records; legacy SRC-0386")

| State | Required safe response |
|---|---|
| Stale | “No current decision-ready information”; suppress action prompt. |
| Empty | “No comparable record found”; do not substitute zero or a nearby record. |
| Malformed | “Source temporarily unavailable”; suppress and log parser error. |
| Unauthorized | “Source not available for this packet”; classify as permission-dependent. |
| Geography mismatch | “Not available for your area”; do not create local action prompt. |
| Semantic mismatch | “Market record not comparable”; hide price number or invalid comparison. |
| Conflict | “Sources conflict”; preserve both, suppress action, and refer. |
| Transformation unverified | “Reference only, not a recommendation”; require human review. |

### 8.5 Trust as interaction design, not marketing language

The current research suggests that trust should be tested by reconstructing a real advice conflict rather than asking whether someone “likes AI.” The relevant questions are: who gave the advice, what evidence they offered, whether the farmer had time to compare it, which constraints decided the action, and whether the advice was later judged useful. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

This means the interface and operating process should make the following visible: source identity; date and location; whether information is an observation, forecast, interpretation, or recommendation; what is missing; what alternatives exist; whether a commercial party has an interest; and where human confirmation can be sought.

---

## 9. Field validation and operating memory

### 9.1 What has and has not happened

The archive contains detailed recruitment, consent, field-selection, interview, event, safety, follow-up, tie-break, and evidence-governance artifacts. These are important operating knowledge. However, they must be classified as field-method and launch-kit material unless accompanied by actual participant/event records. The farmer-problem report explicitly states that no first-party EcoFarm farmer validation has been completed. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357") [EF-FLD-008](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-008__ecofarmfieldlaunchkit_governanceindex.md "Field launch governance index; legacy SRC-0360") [EF-FLD-013](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-013__ecofarmprimarypilotcohortanddecision_authorityprotocol.md "Primary pilot cohort and decision authority protocol; legacy SRC-0372") [EF-FLD-017](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-017__ecofarmweeklyeventregisterandevidencedashboard.md "Weekly event register and evidence dashboard; legacy SRC-0381")

### 9.2 Intended field programme

The proposed 30-day programme seeks 24–30 participants across at least two villages, including non-relative or independently recruited participants. It compares crop, water, holding, advice access, technology comfort, household authority, and market route rather than treating a familiar founder network as representative. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

| Stage | Intended activity | Evidence that should exist if completed |
|---|---|---|
| Recruitment and consent | Recruit purposeful sample; explain purpose and consent. | Consent and participant eligibility records. |
| Past-cycle interviews | Reconstruct recent decisions, sources, constraints, advice conflicts, and outcomes. | Interview/decision-timeline records. |
| Comparison interviews | Test transferability across village, crop, water, and advice-access differences. | Comparison evidence and contradiction log. |
| Adviser/dealer/KVK/market interviews | Map alternatives and ecosystem, separate from farmer evidence. | Source-specific interview notes. |
| Live-event observation | Use manual/paper/spreadsheet workflow during sowing, risk, or sale events. | Trigger-to-action record with sources, decision, and observed action. |
| Follow-up | Verify what was done and what happened. | Outcome/follow-up record; no inferred action from message views. |
| Decision review | Continue/change/stop based on evidence. | Decision memo identifying source, limits, and next test. |

### 9.3 Continue/change/stop logic

The field programme should not measure generic “interest.” It should ask whether a repeated, consequential, information-addressable decision exists; whether the current workaround has a demonstrable gap; whether a feasible action can be taken in the time window; whether trust can be earned without safety overreach; and whether an action/outcome can be recorded. [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

| Decision condition | Continue signal | Change signal | Stop/defer signal |
|---|---|---|---|
| Recurrence | Several independent farmers describe the same current/recent decision. | Decision varies meaningfully by segment/crop/water context. | No common decision after purposeful sampling. |
| Pain | Specific cost, delay, risk, or dependence can be described. | Pain is real but appears structural rather than information-addressable. | Only generic/hypothetical dissatisfaction. |
| Workaround gap | Existing sources are late, generic, conflicting, or hard to compare. | A gap exists only for a narrower segment or delivery mode. | A trusted service is timely, sufficient, and already fits the decision. |
| Actionability | A farmer can act within the decision window. | Advice requires more local evidence or human review. | Information cannot alter the outcome once the trigger occurs. |
| Safety | Workflow stays within comparison, education, and escalation boundaries. | Needs formal agronomist/institutional review. | High harm remains possible without a reliable safeguard. |

### 9.4 Measurement philosophy

Success should be measured through comprehension, source understanding, decision timeliness, ability to explain the reason for an option, recognition of contradictions, actual action, appropriate escalation, repeat engagement where relevant, and quality of outcome records. It should not be measured through clicks alone, self-reported enthusiasm alone, or ungrounded claims of profit/yield improvement. [EF-DAT-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-001__ecofarmecosystem_datafeasibility_alternatives_anddeliveryhandoff.md "Ecosystem, data feasibility, alternatives, and delivery handoff; legacy SRC-0354") [EF-FLD-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/07_farmer_decision_and_field_validation/EF-FLD-001__ecofarmfarmer_problemresearchreport.md "Farmer problem research report; legacy SRC-0357")

---

## 10. Current working map without forced finality

### 10.1 Current positions

| Area | Current working interpretation | Status |
|---|---|---|
| Long-term EcoFarm vision | Integrated agricultural technology ecosystem spanning information, decisions, records, hardware, operations, markets, and human networks. | `HV` / enduring founder vision; not a current build scope. |
| Primary research geography | Namakkal/Kongu as a practical field-entry hypothesis. | `RH` / current working. |
| Initial farmer segment | Small, primarily rainfed groundnut or comparable dryland-crop farmers. | `RH`; field validation required. |
| First decision wedge | Sowing/wait/re-sow/early-season response. | `RH` + `PD`; primary field hypothesis. |
| Close comparator | In-season crop-risk triage/escalation. | `RH` + `PD`; high safety burden. |
| Secondary comparator | Market observation plus decision/outcome logging. | `RH`; specific crop/market semantics required. |
| P0 operational form | Human-reviewed packet using consented farmer context and manual references. | Conditional `PD` / `OP`. |
| Automated weather source | Tested TNAU bulletin path blocked in first P0. | `DA` for the tested path, not all future paths. |
| Market feed | Excluded until decision-relevant crop/market and semantic sample are established. | `UQ` / blocked in P0. |
| Referral directory | Public links/contacts may be shown with neutral wording and recheck dates. | Conditional `OP`; not partnership. |
| Hardware/IoT control | Retained long-term concept, not P0. | `HV` / future hypothesis. |
| Marketplace/community/finance | Retained long-term concepts, not current P0. | `HV` / future hypothesis. |

### 10.2 Explicit current blockers

1. First-party evidence that a repeated decision gap exists among independent farmers.
2. A field-proven target segment, crop comparison, and decision vocabulary.
3. Purpose-specific consent, data minimization, deletion/access mechanics, and human review workflow.
4. A source pathway with rights, target locality, semantics, freshness, provenance, and failure behaviour sufficient for the intended transformation.
5. Local-language/assisted-use validation and proof that participants understand observed versus expected information.
6. A named escalation route that does not misrepresent institutions or disclose cases without agreement.
7. An outcome-recording method that can distinguish actual action from interest and acknowledge confounding factors.

### 10.3 Reopening conditions for deferred concepts

| Deferred concept | What would justify reopening it |
|---|---|
| Automated weather-to-action output | A target-covered, rights-cleared, semantically stable source passes a documented source gate and the transformation rule is reviewed. |
| Market observation in P0 | Fieldwork names the crop/market decision, and a source sample passes freshness, comparability, unit/variety, and failure tests. |
| Crop recommendation/ranking | Repeated decision evidence, locally valid constraints, transparent rules, expert review path, and a safe way to handle missing data. |
| Image disease support | Ground-truthed local data, confidence/quality controls, expert escalation, and explicit non-prescription boundary. |
| Sensor/automation MVP | Field evidence of operational value plus calibration, maintenance, connectivity, safety, ownership, and economic viability design. |
| Marketplace/community/finance | Evidence of the relevant local transaction or coordination problem, trust/governance model, and legal/operating plan. |

---

## 11. Commercial and investor material as secondary archive

EcoFarm’s commercial, pitch, market-access, and investor materials are preserved because they contain part of the project’s imagination. They should be read as **business hypotheses and historical narrative artifacts**, not as the organizing centre of the knowledge base.

### 11.1 Commercial logic historically present in EcoFarm

The historical archive contains several commercial ideas:

- Help farmers improve yields, reduce resource waste, and improve operational efficiency.
- Improve market awareness and possibly direct buyer access.
- Reduce intermediary dependence through transparent prices, marketplace functions, or supply-chain connectivity.
- Support seasonal budgeting, expenses, revenue, and eventually financial/insurance context.
- Use hardware, software, data, and services as mutually reinforcing parts of an Agri-Tech company.
- Present an innovation narrative around precision agriculture, automation, sustainability, AI, and rural empowerment. [EF-VSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "Extended EcoFarm onboarding document; legacy SRC-0039") [EF-DSN-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-007__skylabstechpreneurpitch.pdf "SkyLabs TechPreneur pitch; legacy SRC-0043") [EF-DSN-008](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-008__smartfarmingecosystem_amasterdocumentforcom.pdf "Smart Farming Ecosystem master document; legacy SRC-0044") [EF-DSN-009](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-009__content_plan.md "ComSoc HackX content plan; legacy SRC-0048")–[EF-DSN-011](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-011__title_slide.html "Historical title-slide artifact; legacy SRC-0062")

These ideas remain useful as a map of possible value capture and impact mechanisms. The current knowledge base deliberately refuses to infer a business model or investability conclusion from them.

### 11.2 What must not be overstated

The archive does not yet establish farmers’ willingness to pay, repeat usage, customer-acquisition economics, source-integration rights, hardware unit economics, partner commitments, validated price/profit outcomes, or a reliable path from pilot to scale. A strong product insight may still lack a viable business model; conversely, a broad historical business narrative might later become useful once a narrow decision wedge is proven.

### 11.3 How future commercial work should use this archive

Future commercialization work should begin from the evidence registers in this document: what decision is recurrent, who feels it, what alternatives exist, what portion of value is information-addressable, what human/operational work is required, and what outcomes can be credibly measured. Any future pitch should cite the specific evidence status of its claims and avoid converting intended impact into traction.

---

## 12. Knowledge registers and appendices

### Appendix A — Core research and evidence register

This register groups unique information that should remain available for future reasoning. It is not a claim that every entry has equal evidentiary weight.

| Knowledge object | What the archive currently says | Evidence status | Key source(s) | Decision relevance |
|---|---|---|---|---|
| Namakkal agricultural context | Mixed rainfed and irrigated agriculture; multiple crop systems; official extension and market infrastructure. | `SR` | `SRC-0357`, `SRC-0354`, `SRC-0301`, `SRC-0309` | Supports segmentation and field selection; does not prove demand. |
| Smallholding/segment hypothesis | Desk research identifies many smaller operational holdings and supports differentiating crop, water, and holding context. | `SR` + `RH` | `SRC-0357` | Do not treat holding records as proof of household decision authority. |
| Groundnut entry hypothesis | Groundnut is locally documented and has relevant KVK/research context. | `SR` + `RH` | `SRC-0357` | Practical starting hypothesis, not validated wedge. |
| Information-gap hypothesis | Existing information channels are dense; the gap may be timeliness, comparability, trust, localization, or feasible-action translation. | `AS` / `RH` | `SRC-0357`, `SRC-0354` | Central testable thesis; avoid “farmers lack information” claim. |
| Advice stack | Farmers may combine peers, family, dealers, traders, public officers, KVK, WhatsApp, media, public apps, and non-action. | `SR` + `RH` | `SRC-0357`, `SRC-0354` | Defines alternatives and trust research. |
| Rainfed establishment decision | Sowing/wait/re-sow/adjust may be consequential, time-bound, and measurable. | `RH` + `AS` | `SRC-0357`, `SRC-0351`, `SRC-0352` | Primary candidate for field validation. |
| Crop-risk triage decision | Symptom events can recur but carry high safety burden. | `RH` + `PD` | `SRC-0357` | Test escalation and evidence capture, not autonomous treatment. |
| Sale/market decision | Market information must be interpreted alongside quality, transport, storage, liquidity, debt, and buyer relations. | `RH` + `SR` | `SRC-0357`, `SRC-0354` | Requires specific crop/market semantic test. |
| Official weather/advisory sources | Official IMD/TNAU/TAWN ecosystems exist. | `SR` | `SRC-0354`, `SRC-0380` | Availability does not equal automation approval. |
| Tested TNAU bulletin result | Tested page was public/current at statewide level but lacked Namakkal details and clear automated reuse rights. | `DO` + `DA` | `SRC-0370` | Automated use of this selected path blocked for first P0. |
| Market data source | Agmarknet/data.gov.in may provide observed market values with market/date/variety/unit context. | `SR` + `UQ` | `SRC-0354`, `SRC-0370` | P0 excluded until selected decision and semantics pass test. |
| Institutional ecosystem | Department, ATMA, KVK, markets, FPOs, and others may be sources, validation channels, or escalation routes. | `SR` + `UQ` | `SRC-0354`, `SRC-0355` | No partnership may be implied. |
| Public referral contacts | District Agriculture Department and KVK Namakkal public entries were verified on the recorded test date. | `DO` + `OP` | `SRC-0370` | Public-link/contact-only; recheck and neutral wording required. |
| Farmer data | Farmer-entered crop/stage/location/constraint data is relevant but purpose-dependent. | `PD` + `OP` | `SRC-0354`, `SRC-0366`, `SRC-0372` | Consent, minimization, validation, and deletion gate. |
| Satellite signals | Potential future context for crop/field observation. | `HV` + `UQ` | `SRC-0039`, `SRC-0354` | Not primary initial recommendation input. |
| Sensors and hardware | Long-term system components with substantial calibration, maintenance, cost, and safety requirements. | `HV` + `PD` | `SRC-0039`, `SRC-0025`, `SRC-0026`, `SRC-0029`, `SRC-0036` | Preserve as architecture; require separate validation. |

### Appendix B — Feature status register

| Feature / capability | Historical role | Current status | Reopening or progression condition |
|---|---|---|---|
| Constraint-aware crop comparison | Core decision-support aspiration. | `RH` / current field candidate. | Evidence of repeated decision, viable input set, safe comparison rules, and human review path. |
| Weather source card / cautious prompt | Historical weather functionality. | Tested path blocked; broader concept unresolved. | Rights-cleared, target-covered, fresh, stable source and documented transformation rules. |
| Market observation | Historical market transparency. | Secondary candidate, not P0 now. | Crop/market selection, semantic sample, farmer relevance, and source tests. |
| Decision and outcome log | Historical farm recordkeeping; current learning core. | Current working candidate. | Consent/field design, actual event capture, and appropriate retention. |
| Crop-risk triage | Historical disease/crop-health intelligence. | Parallel field hypothesis. | Safe evidence capture, expert escalation, no-prescription boundary, and field need evidence. |
| Agronomy education | Historical guidance layer. | Human-reviewed reference candidate. | Version/region/crop-stage matching and rights/attribution handling. |
| Soil-test context | Historical soil intelligence. | Permission-dependent. | Farmer-held/authorized data, freshness and units, consent, no district-average substitution. |
| Sensors | Core hardware vision. | Long-term historical concept. | Calibration, field durability, economics, maintenance, and decision-value evidence. |
| Irrigation control | Core hardware/operations vision. | Long-term historical concept. | Device safety, authority/ownership, reliability, command confirmation, and field value. |
| Pest/disease image support | Historical AI vision. | Future hypothesis. | Ground-truth, quality/calibration, safe escalation and clear non-prescription scope. |
| Yield prediction | Historical analytics vision. | Future hypothesis. | Local validated data/model and conservative communication. |
| Community/peer network | Historical ecosystem vision. | Future hypothesis. | Local use, governance, trust, moderation, safety, and value evidence. |
| Equipment/labour marketplace | Historical coordination vision. | Future hypothesis. | Local transaction demand, availability, payment/dispute/logistics model. |
| Buyer marketplace | Historical market-access vision. | Future hypothesis. | Supply quality, buyer operations, logistics, compliance, and farmer protection model. |
| Budget/finance/insurance support | Historical financial resilience vision. | Contextual future concept. | Evidence of decision value, regulated/partner path, and privacy/safety design. |

### Appendix C — Decision-history ledger

| Historical or current decision | Reasoning preserved | Status / reopening condition | Source(s) |
|---|---|---|---|
| Treat EcoFarm as integrated hardware/software ecosystem | Original vision connected sensing, automation, data, decisions, market, and community. | Historical architecture remains preserved. | `SRC-0130`, `SRC-0039` |
| Start with a mobile interface | The app was imagined as the farmer’s central interaction point with farm data, recommendations, controls, and networks. | Historical product decision; future interfaces may include assisted/voice/other modes. | `SRC-0039`, `SRC-0005` |
| Consider sensors rather than only software | Sensor data was intended to improve irrigation, soil, and crop context. | Historical; hardware needs separate evidence. | `SRC-0039`, `SRC-0025`–`SRC-0036` |
| Prefer a microcosm / Namakkal entry | Local access, mixed systems, rainfed exposure, and visible institution/data ecosystem. | Current field hypothesis, not market conclusion. | `SRC-0286`, `SRC-0357` |
| Treat groundnut as starting hypothesis | Local crop relevance and research/extension context. | Must be compared against other crop systems. | `SRC-0357` |
| Narrow from broad app to named decision | Existing channels and safety constraints make generic information aggregation weak. | Current working posture. | `SRC-0354`, `SRC-0357` |
| Choose sowing/early-season decision for initial test | Consequential, bounded, local, potentially observable, safer than autonomous diagnosis/price prediction. | Field validation required. | `SRC-0357` |
| Do not use tested TNAU bulletin in automated P0 | Target-locality and rights failure documented. | Reopen only with a separately approved source path. | `SRC-0370` |
| Use public referral directory only with neutral wording | Contacts are sources, not partners or guaranteed responders. | Recheck dates and no case sharing without agreement. | `SRC-0370` |

### Appendix D — Unresolved-question register

1. Which exact farmer decision repeats across independent Namakkal/Kongu participants, and in which crop/water segments?
2. Is the most consequential gap information absence, poor timing, poor localization, conflicting advice, trust, lack of feasible action, or something structural that software cannot change?
3. Who actually makes or vetoes the relevant decision inside the household or farm operation?
4. How do farmers currently receive, interpret, verify, ignore, or act on weather/advisory/market information?
5. Which language, delivery, assisted-use, and connectivity patterns are usable in the target segment?
6. Which weather/advisory source can meet rights, locality, freshness, semantics, provenance, and failure requirements for a named action?
7. Which market/crop/variety/unit records are actually comparable for a farmer’s sale decision?
8. What source transformations are safe enough to be automated, and where must a human review remain mandatory?
9. What data will farmers consent to provide for a decision packet, and what retention/deletion expectations do they have?
10. Can a decision packet change comprehension, timing, confidence calibration, or escalation behaviour without creating false certainty?
11. What outcomes can be measured credibly without claiming that EcoFarm caused yield or profit changes?
12. Which institutional actors are reachable, current, appropriate, and willing to act as a validation or escalation channel?
13. What hardware problem, if any, is economically and operationally worth solving after a software/decision wedge is validated?
14. Which marketplace, community, finance, or supply-chain concepts represent actual local coordination gaps rather than attractive but duplicative platform features?
15. What would make EcoFarm trusted enough to become part of a farmer’s advice stack rather than another ignored channel?

### Appendix E — Historical visual and design asset index

The corpus preserves wireframes, high-fidelity mockups, charts, slide artifacts, and an early video. These assets are retained because they encode historical product imagination and research context. Detailed pixel-level UI specification is intentionally outside the main knowledge base.

| Asset class | Preserved examples | Intended archival use |
|---|---|---|
| Historical product wireframes | Field overview, home dashboard, marketplace feed, MVP flow/wireframe documents. [EF-PRD-002](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/02_product_concept_and_feature_mechanics/EF-PRD-002__mvp_screens_flows.md "MVP user flows and key screens outline; legacy SRC-0005") [EF-DSN-004](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-004__wireframe_fields_overview.png "Field overview wireframe; legacy SRC-0020")–[EF-PRD-004](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/02_product_concept_and_feature_mechanics/EF-PRD-004__wireframes_part2.md "Low-fidelity wireframes part 2; legacy SRC-0024") | Recover earlier workflow and module relationships. |
| Historical high-fidelity mockups | Home/dashboard and field-overview mockups. [EF-DSN-001](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-001__mockup_fields_overview_hf.png "Field overview high-fidelity mockup; legacy SRC-0003") [EF-DSN-002](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-002__mockup_home_dashboard_hf.png "Home dashboard high-fidelity mockup; legacy SRC-0004") | Understand visual hierarchy and intended data/control views. |
| Agricultural research charts | Water, soil, farm-size, income, labour, food loss, regional cluster, and crisis charts. [EF-DSN-012](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-012__ag_rd_spending.png "Agricultural R&D spending chart; legacy SRC-0319")–[EF-DSN-018](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-018__water_disputes.png "Water disputes chart; legacy SRC-0338") | Trace source-era research communication; verify underlying figures before reuse. |
| Presentations and pitch visuals | Proposal, HackX, pitch, and slide-content artifacts. [EF-DSN-007](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-007__skylabstechpreneurpitch.pdf "SkyLabs TechPreneur pitch; legacy SRC-0043") [EF-DSN-009](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-009__content_plan.md "ComSoc HackX content plan; legacy SRC-0048")–[EF-DSN-011](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-011__title_slide.html "Historical title-slide artifact; legacy SRC-0062") | Preserve historical commercial/innovation framing. |
| Video artifact | Early AI farming UI video. [EF-DSN-003](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/09_historical_design_pitch_and_media/EF-DSN-003__aifarmingui3_2.mov "Early AI farming UI video; legacy SRC-0001") | Retain as historical design reference only. |

### Appendix F — Full preservation system

The single human-readable document is intentionally paired with a full evidence archive rather than pretending a finite narrative can contain every raw source verbatim.

| Artifact | Location / role |
|---|---|
| Raw preserved archive | `/home/ubuntu/ecofarm_source_archive/` — all retrieved and copied artifacts, conversations, current-session captures, and visual assets. |
| Source manifest | `manifest/EcoFarm_Source_Manifest.json` and `.csv` — stable IDs, source group, file metadata, SHA-256, and exact-duplicate relations. |
| Evidence taxonomy | `knowledge_mapping/EcoFarm_Evidence_Status_Taxonomy.md` — rules for interpreting status. |
| Core source map | `knowledge_mapping/EcoFarm_Core_Source_Map.md` — high-value sources and cautions. |
| Normalized text | `extracted_text/` — text copies and PDF text extraction, plus document index. |
| LLM corpus | `llm_knowledge_corpus/` — 181 documents and 957 canonical provenance-bearing chunks with retrieval topics. |
| Partial atomic extraction | `gemini_structured_extraction/` — source-grounded compact records for processed priority material; partial by design due external quota boundary. |

### Appendix G — Maintenance protocol

When new EcoFarm research, product thinking, technical work, field evidence, or decisions appear, update the system in this order:

1. Preserve the raw artifact and origin/date before summarizing it.
2. Add it to the source manifest and calculate its hash; record exact duplicates without deleting versions.
3. Assign an evidence-status and temporal-status label.
4. Update the relevant concept/feature dossier with what changed, what remains true, and what is now unresolved.
5. Add or revise decision-history and open-question records rather than silently rewriting old conclusions.
6. Regenerate the LLM chunk corpus so external models can retrieve the new source with provenance.
7. Update the HTML knowledge site index and topic page links.
8. Treat any field plan, design, or test methodology as unexecuted until an actual evidence artifact proves execution.

---

## Reference sources for the current field/P0 evidence

The following primary sources are retained in the current research material and should be preferred when revalidating time-sensitive facts:

[1]: https://namakkal.nic.in/departments/agriculture/ "Namakkal District Agriculture Department"
[2]: https://namakkal.nic.in/document/statistical-handbook-2023-2024/ "Namakkal District Statistical Handbook 2023–24"
[3]: https://www.tanuvas.ac.in/kvk_namakkal.php "ICAR-Krishi Vigyan Kendra, Namakkal / TANUVAS"
[4]: https://www.agrimark.tn.gov.in/index.php/scheme/view/4 "Tamil Nadu e-NAM scheme"
[5]: https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi "data.gov.in daily mandi-price resource"
[6]: https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php "India Meteorological Department Agromet Advisory Services"
[7]: https://api.imd.gov.in/ "India Meteorological Department API Management Platform"
[8]: https://tnau.ac.in/site/research/crop-production-guide/ "Tamil Nadu Agricultural University Crop Production Guide"
[9]: https://agritech.tnau.ac.in/agrometeorologicaladvisory/agro_meteorological_advisory_tnau_district.html "TNAU district Agro-Meteorological Advisory Bulletin"
