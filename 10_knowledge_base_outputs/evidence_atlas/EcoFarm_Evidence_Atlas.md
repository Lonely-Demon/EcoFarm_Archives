# EcoFarm Evidence Atlas

## Status, Purpose, and Reading Rule

The Evidence Atlas is an **archive-only trace layer** for EcoFarm. It is designed to make the project’s accumulated reasoning inspectable and reusable without converting historical intent, secondary research, field instruments, visuals, or product hypotheses into verified fact. It does not select a product wedge, recommend an investment, or declare a product or pilot validated.

The Atlas is now based on a completed mandatory review stage: **113 of 113 curated canonical sources were individually read in full before classification, relationship reconciliation, or trace mapping.** The procedural record is available in the [Full-File Review Completion Record](full_file_review/EcoFarm_Full_File_Review_Completion_Record.md), while source-specific treatment remains in the [Full-File Review Ledger](full_file_review/EcoFarm_Full_File_Review_Ledger.json).

> **How to read an Atlas statement:** First identify its evidence label, scope, limitation, source ID, chunk ID, and current-use designation. A statement with an eloquent historical source is still only historical intent unless the cited evidence supports more.

## Evidence Architecture

| Layer | What it contributes | Permitted Atlas use | Prohibited upgrade |
|---|---|---|---|
| Current governance | Founder instructions, archive boundaries, and programme controls. [1] [2] | Governing constraints. | Treating policy/process direction as agricultural or market proof. |
| Historical vision, PRD, technical, and design sources | Intent, feature mechanics, alternatives, interaction models, and historical communication context. [3] [4] [5] | Historical context and candidate requirements. | Treating a described capability as built, safe, current, or useful. |
| Research syntheses and local notes | Context, research leads, comparison logic, and hypotheses. | Candidate inputs and revalidation targets. | Treating secondary repetition as corroborated primary evidence. |
| Field instruments and protocols | A method for generating attributable evidence. | Research-design controls. | Treating an interview guide, consent pack, or cohort plan as an observed result. |
| P0 data/safety records | Provenance, consent, source semantics, escalation, feasibility, and observability controls. [6] | Governing constraints for data-enabled work. | Treating a test snapshot or framework as universal readiness. |
| Historical visuals and pitches | Design and narrative lineage. | Historical/design context only. | Treating a mockup, chart, or deck as factual, numeric, or outcome evidence. |

The family-level relationship analysis is available in both [human-readable](EcoFarm_Source_Family_Reconciliation.md) and [machine-readable](EcoFarm_Source_Family_Reconciliation.json) forms.

## Evidence Labels

| Label | Meaning in this Atlas |
|---|---|
| `verified_fact` | Reserved for a statement directly established by an attributable, scoped primary source. It is deliberately rare. |
| `supported_inference` | A bounded inference from a source or test whose method/scope is known; its limitation remains mandatory. |
| `historical_intent` | What the project historically planned, preferred, or described. |
| `product_hypothesis` | A proposed feature, benefit, mechanism, or impact that has not been demonstrated. |
| `secondary_synthesis` | A report or consolidation that preserves reasoning and source leads but does not become primary proof. |
| `research_design_only` | A plan, instrument, protocol, consent pack, or evaluation method with no result implied. |
| `needs_revalidation` | A dated, dynamic, institutional, or external assertion that needs a fresh primary source for present use. |
| `unknown` | The archive does not contain sufficient provenance, method, scope, or evidence. |

## Core Trace Map

The `EVA-CORE-*` dataset is a compact cross-source map. Each entry includes recovery chunk IDs, durable GitHub source URLs, scope, confidence, relationships, and a limitation note in [EVA Core Trace Records](EVA_Core_Trace_Records.jsonl).

| Topic | Evidence label | What the archive supports | What remains explicitly open |
|---|---|---|---|
| Archive purpose | `historical_intent` / governing | EcoFarm must be preserved as a non-final knowledge base rather than converted into a pitch-led summary. [1] [2] | The archive rule says nothing about a market, product, or agricultural outcome. |
| Integrated ecosystem vision | `historical_intent` | Historical onboarding sources describe a hardware-plus-software ecosystem with a farmer-facing app, data, and assisted operations. [3] [4] [5] | No delivery, adoption, safety, or benefit has been established. |
| Software-first MVP | `historical_intent` | Several historical sources preferred API-enabled utility while proprietary hardware was unavailable. [4] [5] | Current data availability, farmer utility, and scope priority require validation. |
| Recommendation boundary | `product_hypothesis` | The historical record itself warns that regional inputs cannot stand in for farm-specific conditions. [4] [5] | Recommendation accuracy, agronomic appropriateness, and safe operationalisation are unproven. |
| Irrigation automation | `historical_intent` | Historical designs specify farmer confirmation or override before consequential watering. [4] [5] | Confirmation alone is not an end-to-end control-system safety case. |
| Technical direction | `historical_intent` | Flutter/FastAPI/PostgreSQL-plus-spatial/time-series/cloud was a historical preference; Node/React Native was considered. [4] [5] | There is no current architecture, security, cost, component, or delivery decision established by this record. |
| National/global problem context | `secondary_synthesis` | The archive preserves broad agricultural-problem framing and source leads. | National/global context does not prove local need or product-market fit. |
| Regional selection reasoning | `secondary_synthesis` | Comparative microcosm records preserve historical Kongu/Namakkal decision logic. | They do not settle an entry geography without attributable local evidence. |
| Field programme | `research_design_only` | Field records define how decision authority, consent, seasonality, and outcomes should be observed. | No field guide, recruitment pack, or dashboard is itself a field result. |
| P0 source controls | `supported_inference` / governing | P0 records require provenance, source semantics, consent, observability, escalation, and bounded testing. [6] | A source-control framework does not prove every provider, endpoint, or feature is ready. |
| Historical visuals | `historical_intent` | Visuals preserve past communication and workflow context. | They do not establish numerical claims, current design direction, or user evidence. |

## Feature-to-Evidence Map

The full structured record is [EVA Feature Evidence Map](EVA_Feature_Evidence_Map.json). This table preserves the relationship between product imagination and evidence boundaries without making a prioritisation recommendation.

| Historical feature family | Primary historical source family | Governing qualification | Evidence boundary |
|---|---|---|---|
| Weather information and alerts | `EF-VSN-*`, `EF-PRD-007` | `EF-DAT-002`, `012`, `013`, `020` | A public weather/advisory service exists, but each use case still needs source semantics, freshness, and failure-state checks. |
| Farm mapping and sectorization | `EF-VSN-*`, `EF-PRD-001`–`002` | Data/consent mechanics and field decision-model work | Historical workflow only; local usability and spatial-data quality are untested. |
| Planting recommendations | `EF-VSN-*`, `EF-PRD-006` | P0 feasibility and source hierarchy | A product hypothesis; regional estimates must not be presented as farm-specific agronomy. |
| Crop lifecycle guidance | `EF-VSN-*`, `EF-PRD-005` | Referral, source, and field-claim controls | Localization, provenance, clinical/agronomic boundaries, and user utility remain open. |
| Disease diagnosis and pest alerts | `EF-VSN-*`, `EF-TEC-003` | P0 safety, escalation, and observability | No training data, model evaluation, confidence calibration, or field accuracy evidence is established. |
| Irrigation automation | `EF-VSN-*`, `EF-TEC-005`–`006` | P0 feasibility, escalation, and fail-closed controls | Historical intent includes override/confirmation; deployment and hazard controls remain unresolved. |
| Records, calendars, tasks, and inventory | `EF-VSN-*`, `EF-PRD-*` | Data and field-attribution protocols | Actual data-entry burden and farmer utility remain to be tested. |
| Market-price information | `EF-VSN-*`, `EF-PRD-007` | Source semantics and provider tests | Market/commodity/variety/grade/date/update state must be explicit; no forecast or benefit follows from a displayed price. |
| Financial, marketplace, labour, and community features | `EF-VSN-*`, `EF-PRD-*` | Consent, referral, data, and ecosystem controls | Historical MVP scope differs across versions; network effects, trust, compliance, and demand are unresolved. |
| Sensors, drone, sustainability, and blockchain extensions | `EF-VSN-*`, `EF-TEC-*` | P0 feasibility, observability, safety | These remain later-phase historical concepts with no current hardware qualification or impact proof. |

## Decision-to-Assumption Map

The [EVA Decision Assumption Map](EVA_Decision_Assumption_Map.json) records the assumption that each historical decision depends upon. It prevents a retained decision from becoming a silent conclusion.

| Historical decision or control | Key assumption that must remain visible | Present treatment |
|---|---|---|
| Preserve a knowledge base rather than a pitch | Historical reasoning, alternatives, and uncertainty are useful future decision inputs. | Governing archive decision. |
| Build software/API utility before hardware | Reliable relevant inputs and daily user value can exist before proprietary sensing/control. | Historical reasoning; requires current source and field validation. |
| Use regional data in early guidance | Regional data can offer bounded value when limitations are stated. | Constrained hypothesis; not farm-specific advice. |
| Request confirmation before irrigation automation | Human confirmation improves control and trust. | Historical safety intent; incomplete without full hazard analysis. |
| Choose an AI/spatial/time-series stack | The preference fits actual team, cost, operations, security, integration, and safety needs. | Historical technical preference. |
| Focus historical research on Namakkal/Kongu | Desktop comparison captures decision-relevant local conditions. | Historical logic; field evidence required. |
| Run attributed, consented field research | The proposed cohort/method can capture relevant decision evidence. | Research design, not outcome. |
| Require P0 provenance/semantics/escalation controls | The controls can safely bound named data-source failures at the relevant stage. | Governing P0 constraint; test scope remains bounded. |

## Contradictions and Open Questions

The [Contradiction and Open Question Register](EVA_Contradiction_Open_Question_Register.json) deliberately retains tensions instead of silently replacing them.

| Item | Status |
|---|---|
| Historical MVP scope differs, especially for community and marketplace features. | **Unresolved version variation.** Preserve both models; make a current priority decision only with new evidence. |
| Ambitious historical hardware/AI automation coexists with later P0 limits. | **Qualified by current controls.** Do not convert vision into a deployment claim. |
| Broad national/global problem framing exceeds bounded local evidence. | **Unresolved.** Do not extrapolate. |
| Historical stack preference has no current tested architecture decision. | **Open engineering decision.** |
| Target decision, farmer segment, locality, crop/system context, and first validation moment remain unsettled. | **Open research-design/field-evidence question.** |
| Valid, decision-fit weather, advisory, and market sources remain use-case-specific. | **Open revalidation question.** |
| Confidence, escalation, liability, and human oversight for agronomic AI remain unresolved. | **Open safety/model-governance question.** |
| Hardware calibration, maintenance, connectivity, actuation, and failure controls remain unresolved. | **Open engineering/field-validation question.** |
| Marketplace/community trust, density, moderation, and compliance remain unresolved. | **Open ecosystem-validation question.** |
| Underlying data/methods for historical charts remain partly unrecovered. | **Open provenance question.** |

## Primary-Source Revalidation Findings

The detailed log is in [EVA Revalidation Findings](EVA_Revalidation_Findings.md) and the machine ledger is [EVA Revalidation Ledger](EVA_Revalidation_Ledger.json). These checks narrow evidence boundaries; they do not validate a product feature.

| Topic | Primary-source result | Atlas consequence |
|---|---|---|
| IMD agricultural weather and advisory context | Official IMD pages publicly present agricultural meteorology/advisory material, state and district bulletins, district-level forecasts, and Tamil Nadu in the state-bulletin selector. [7] [8] | Service existence is a **candidate input**, not proof of data interface, freshness, local accuracy, advisory suitability, or feature feasibility. |
| Namakkal local institutional context | The official district Agriculture page presents departmental objectives, stated district context, crops, infrastructure, schemes, extension structure, and contacts; the official directory lists the Joint Director role. [9] [10] | Treat as official page content with its page/date scope. It does not establish farmer demand, intervention effect, or a longitudinal local dataset. |
| Price and arrival information | AGMARKNET publicly presents price-and-arrival reporting with geography, commodity, variety, grade, and daily-report filters; the report interaction was CAPTCHA-gated when checked. [11] [12] | Preserve commodity, variety/grade, market, date, freeze/update state, and field semantics. Do not infer API access, completeness, “real time” suitability, or price-prediction value. |
| Pests and diseases | FAO states that up to 40% of global crop production is lost each year due to plant pests and diseases. [13] | This is **global context** only; it does not quantify crop loss in India, Tamil Nadu, Namakkal, a crop, or an EcoFarm user segment. |
| Agricultural water withdrawal | FAO AQUASTAT states global sectoral withdrawal ratios of 69% agricultural, 12% municipal, and 19% industrial, while noting methodological and regional-variation caveats. [14] | This is **global method-bounded context**, not a local water-demand, irrigation-efficiency, or product-effect claim. |

## Machine-Readable Trace Corpus

| Artifact | Coverage | Use |
|---|---:|---|
| [EVA Source Review Records](EVA_Source_Review_Records.jsonl) | 113 records | One stable source-coverage record per individually reviewed canonical source, including limitation note, source chunk, and durable GitHub URL. |
| [EVA Core Trace Records](EVA_Core_Trace_Records.jsonl) | 23 records | Cross-source constraints, historical intent, contradictions, and open questions. |
| [EVA Feature Evidence Map](EVA_Feature_Evidence_Map.json) | 12 feature families | Historical feature intent linked to evidence and P0/field qualifications. |
| [EVA Claim Source Map](EVA_Claim_Source_Map.json) | 11 claim families | Claim source sets, evidence label, revalidation priority, and use boundary. |
| [EVA Decision Assumption Map](EVA_Decision_Assumption_Map.json) | 8 records | Historical decision logic and its visible assumptions. |
| [EVA Contradiction/Open Question Register](EVA_Contradiction_Open_Question_Register.json) | 10 records | Preserved contradictions, uncertainty, and explicit next evidence needs. |
| [EVA Revalidation Ledger](EVA_Revalidation_Ledger.json) | 5 themes | Primary-source revalidation status and bounded results. |
| [EVA Trace Dataset Manifest](EVA_Trace_Dataset_Manifest.json) | Dataset inventory | Record counts and full canonical-source coverage list. |

## Citation and Retrieval Convention

Every atomic `EVA-*` record carries one or more `EF-*` source IDs, one or more retrieval chunk IDs where normalized text exists, a source excerpt/heading cue, scope, confidence, limitation note, relationship type, current-use designation, and canonical GitHub source URL. Visual/binary sources without normalized text still retain a durable canonical source URL and their individual-review record.

The canonical public source path follows this form:

> `https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/<canonical-relative-path>`

This Atlas should be extended through **new trace records**, not by overwriting uncertainty or treating a family-level label as a claim-level citation.

## References

[1]: https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/00_governance_and_archive/EF-GOV-001__ecofarm_current_main_conversation_canonical_capture_2026_08_18.md "EF-GOV-001 — Current main conversation canonical capture"
[2]: https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/00_governance_and_archive/EF-GOV-003__ecofarm_master_document_reworked_architecture.md "EF-GOV-003 — Master document reworked architecture"
[3]: https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-001__project_onboarding_document.md "EF-VSN-001 — Extended EcoFarm onboarding document"
[4]: https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-004__project_onboarding_document.md%20(title:%20%22project%20onboarding%20document:%20smart%20farming%20ecosystem%22) "EF-VSN-004 — Historical EcoFarm-2 onboarding document"
[5]: https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/01_founder_vision_and_evolution/EF-VSN-005__project_onboarding_document_old.txt "EF-VSN-005 — Historical EcoFarm onboarding document source text"
[6]: https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/08_data_sources_safety_and_p0_feasibility/EF-DAT-005__p0_feasibility_decision_memo.md "EF-DAT-005 — P0 feasibility decision memo"
[7]: https://imdagrimet.gov.in/ "India Meteorological Department — Agricultural Meteorology Division"
[8]: https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php "India Meteorological Department — Agromet Advisory Services"
[9]: https://namakkal.nic.in/departments/agriculture/ "Namakkal District, Government of Tamil Nadu — Agriculture"
[10]: https://namakkal.nic.in/directory/joint-director-agriculturenamakkal/ "Namakkal District, Government of Tamil Nadu — Joint Director (Agriculture)"
[11]: https://agmarknet.gov.in/home "Government of India — AGMARKNET 2.0"
[12]: https://agmarknet.gov.in/daily-price-and-arrival-report "Government of India — AGMARKNET Daily Price and Arrival Report"
[13]: https://www.fao.org/plant-production-protection/about/en "FAO — About Plant Production and Protection"
[14]: https://www.fao.org/aquastat/en/overview/methodology/water-use/ "FAO AQUASTAT — Water Use Methodology"
