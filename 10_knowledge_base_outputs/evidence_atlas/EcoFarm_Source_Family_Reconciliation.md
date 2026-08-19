# EcoFarm Evidence Atlas — Source-Family Relationship and Evidence-Treatment Reconciliation

## Purpose and Boundary

This reconciliation translates the completed individual full-file reviews into an explicit family-level map. It determines **how source families relate**, **what their records can evidence**, **how they should be retained**, and **which sources govern current use**. It does not decide EcoFarm’s product wedge, recommend an action, validate a historical feature, or convert a research plan into field evidence.

The complete source-level assessments remain authoritative in the [Full-File Review Ledger](full_file_review/EcoFarm_Full_File_Review_Ledger.json). This document preserves their common structure so that later `EVA-*` records can link, qualify, supersede, or contradict source material without erasing its history.

> **Reconciliation rule:** A newer-looking filename, a polished historical pitch, or a repeated statement does not itself establish current authority. Current governing records, direct P0 test outcomes, and bounded external evidence retain their own scope; historical vision and synthesis material remains historical unless a later governing record explicitly adopts it.

## Authority Architecture

| Authority layer | Source families | What it controls | What it does not establish |
|---|---|---|---|
| **Current archive and programme governance** | `EF-GOV-001`, `EF-GOV-002`, `EF-GOV-003`, and current revision records `EF-GOV-005`–`EF-GOV-008` | Founder instructions, archive boundaries, programme scope, and required evidence discipline. | Local agricultural facts, market reality, product feasibility, or field validation. |
| **P0 feasibility and safety governance** | `EF-DAT-002`–`EF-DAT-013`, supported by the limited test/capture records `EF-DAT-014`–`EF-DAT-020` | Source-control rules, consent/data mechanics, safety escalation, observability, operational gates, and bounded test outcomes. | That a source is current, nationwide, complete, suitable for every decision, or a guarantee of product performance. |
| **Field research programme governance** | `EF-FLD-005`–`EF-FLD-017` | How future evidence should be attributed, collected, consented, reviewed, and followed up. | Actual field observations, adoption, behaviour, or outcomes before those observations are recorded. |
| **Historical project reasoning** | `EF-VSN-*`, `EF-PRD-*`, `EF-TEC-*`, historical `EF-DSN-*` | Original intent, conceptual working, alternatives, feature mechanics, and rationale. | A present requirement, implemented capability, validated AI performance, safe control design, or settled architecture. |
| **Contextual research and external-source notes** | `EF-AGR-*`, `EF-REG-*`, `EF-MKT-*`, bounded `EF-FLD-018`–`EF-FLD-020`, institutional captures | Research leads, context, hypotheses, comparison frames, and revalidation targets. | A current general fact unless the underlying primary source, timing, geography, and method are rechecked. |

## Family Reconciliation Matrix

| Family | Sources in family | Relationship pattern | Evidence treatment and current use |
|---|---|---|---|
| **Governance and archive** | `EF-GOV-001`–`003`, `005`–`008` | Current founder instructions and approval records govern archive method. Research-agent handoffs and revisions are programme-control records, not independent research results. `EF-GOV-003` establishes the intended knowledge-base character. | Use current instructions and approvals as **governing**. Treat handoffs as scope/method evidence. Do not cite them as farming, market, legal, or technology evidence. |
| **Founder vision and evolution** | `EF-VSN-001`–`005` | `EF-VSN-003` is a document architecture scaffold; `EF-VSN-005` is a detailed earlier source text; `EF-VSN-004` preserves a dated Smart Farming Ecosystem formulation; `EF-VSN-001` is the richest preserved onboarding version; `EF-VSN-002` is a concise derivative/framing version. Their overlaps and different MVP bounds are meaningful version variation, not duplication to erase. | Use as **historical intent** and design genealogy. Never treat their problem statistics, promised outcomes, stack choice, hardware claims, or broad feature inventory as verified/current merely because multiple versions repeat them. |
| **Product concept and feature mechanics** | `EF-PRD-001`–`007` | The PRD and user-flow records articulate concepts and interactions; the wireframes preserve historical workflow visualization; `EF-PRD-006` and `EF-PRD-007` concentrate the software-first MVP trade-off logic. These are companions to, not implementation proof for, the onboarding family. | Use as **historical intent** and candidate feature/decision trace inputs. Reconcile each feature with P0 constraints, verified data availability, safety needs, and field evidence before considering current use. |
| **Technical architecture, hardware, and AI** | `EF-TEC-001`–`007` | `EF-TEC-001` documents alternatives; `EF-TEC-002` proposes a stack; `EF-TEC-003` and `EF-TEC-004` assess AI/data and hosting; `EF-TEC-005` is the preferred parseable sensor-research export, with stale FireShot/text captures retained only as provenance aliases; `EF-TEC-006` is a broader technical-master blueprint; and `EF-TEC-007` records complementary sensor alternatives and selection criteria. They explain historical option space and recur in the onboarding sources. | Use as **historical technical reasoning**. Treat components, protocols, cloud services, AI models, sensor readings, costs, and scalability claims as candidates requiring current engineering, source, safety, and security validation. |
| **India agriculture problem research** | `EF-AGR-001`–`008` | These sources form a layered national/global problem-synthesis family: broad reports, focused relevance analysis, distress context, and multi-source consolidations. Several restate overlapping external statistics and causal frames. | Use as **secondary synthesis** and a revalidation queue. Preserve cited primary-source leads, but do not aggregate repetition into stronger evidence or extrapolate national/global statements to Namakkal. |
| **Regional microcosm and Namakkal research** | `EF-REG-001`–`013` | `EF-REG-006` and `EF-REG-008` are research-method records; `EF-REG-001`–`005`, `007`, `009`–`011` are historical comparison/selection analyses; `EF-REG-012` and `EF-REG-013` preserve notes from local institutional/statistical sources. The Punjab comparison is a comparator, not proof of Namakkal conditions. | Keep plans as **research_design_only**, comparative analyses as **secondary_synthesis**, and the institutional-note sources as **needs_revalidation** with bounded local relevance. Do not convert a recommended microcosm into a settled entry decision. |
| **Market, commercial, and ecosystem research** | `EF-MKT-001`–`008` | `EF-MKT-001` records founder-market reasoning; `EF-MKT-002`–`004` map alternatives and ecosystem context; `EF-MKT-005`–`008` add localized market/risk, price/decision, data-feasibility, and ecosystem findings. Their purpose is to question assumptions, not provide a commercial conclusion. | Use as **historical intent**, **secondary synthesis**, and **candidate inputs**. Market, competitor, price, and institutional claims need dated primary-source revalidation; behavioural verification methods do not equal behavioural findings. |
| **Farmer decision and field validation** | `EF-FLD-001`–`020` | `EF-FLD-001`–`004` synthesize decision models and candidate scoring; `EF-FLD-005`–`017` govern the field programme and instruments; `EF-FLD-018`–`020` retain bounded study/source notes. The family is deliberately structured to keep research design separate from observed evidence. | Treat protocols, guides, consent packs, maps, and registers as **research_design_only**. Treat study notes as **supported_inference** only within their stated sample, time, and locality limits. No field-validation claim is permitted without recorded observations. |
| **Data sources, safety, and P0 feasibility** | `EF-DAT-001`–`020` | `EF-DAT-001` is a handoff synthesis. `EF-DAT-002`–`013` create the P0 source, consent, feasibility, safety, and observability controls. `EF-DAT-014`–`015` are institutional-source captures; `EF-DAT-016`–`019` are bounded test artifacts; `EF-DAT-020` provides weather/advisory context and differentiation boundaries. | Use the P0 controls as **governing constraints** for source-enabled work. Use direct test records only for the exact test state documented. Treat captures and institutional content as **needs_revalidation** for present availability/currentness. |
| **Historical design, pitch, and media** | `EF-DSN-001`–`019` | Mockups, wireframes, video, decks, pitch documents, charts, and hackathon material preserve historical communication and design context. Visuals often echo feature themes from the vision and PRD families; charts often visualize claims from the research families. | Use as **historical context** only. They cannot prove numerical claims, product delivery, user demand, current design direction, technical readiness, or commercial validation without an attributable supporting source. |

## Version and Dependency Register

| Reconciliation ID | Relationship | Source set | Treatment |
|---|---|---|---|
| `REL-001` | Governs | `EF-GOV-001`, `EF-GOV-002`, `EF-GOV-003` → all Atlas outputs | Current founder/archive rules override older presentation-oriented framing in archive work. |
| `REL-002` | Revises programme method | `EF-GOV-005` → `EF-GOV-006`; `EF-GOV-007` → `EF-GOV-008` | Retain both handoff and revision; the revision qualifies how the research programme is interpreted. |
| `REL-003` | Historical vision family | `EF-VSN-003`, `EF-VSN-005`, `EF-VSN-004`, `EF-VSN-001`, `EF-VSN-002` | Preserve differences in scope and MVP selection; the available file record does not support a universal simple “final” ordering. |
| `REL-004` | Feature-design companions | `EF-VSN-*` ↔ `EF-PRD-001`–`007` ↔ `EF-DSN-001`–`006` | These sources support reconstruction of historical concept and interaction intent, but do not establish implementation. |
| `REL-005` | Technical-option companions | `EF-VSN-*`, `EF-PRD-006`–`007` ↔ `EF-TEC-001`–`007` | Historical stack/sensor descriptions and MVP logic explain one another; `EF-TEC-005` is the preferred retrieval record, while FireShot/text variants remain provenance only; current feasibility remains subject to P0 gates and a fresh engineering review. |
| `REL-006` | Context does not establish local need | `EF-AGR-*` → `EF-REG-*` / `EF-FLD-*` | India/global syntheses can motivate local research but cannot prove the target-area problem, farmer segment, or behavioural pattern. |
| `REL-007` | Research design tests hypotheses | `EF-REG-006`, `EF-REG-008`, `EF-FLD-005`–`017` → regional/market/product hypotheses | Methods, interview guides, selection memos, and consent packs define what to test. They are not results. |
| `REL-008` | Local evidence qualifies broader synthesis | `EF-REG-012`, `EF-REG-013`, `EF-FLD-018`–`020` ↔ `EF-AGR-*`, `EF-REG-001`–`011`, `EF-MKT-*` | Bounded institutional/study notes may qualify broader context only within their stated time, geography, and methodology. |
| `REL-009` | P0 constraints qualify product claims | `EF-DAT-002`–`013`, `EF-DAT-016`–`020` → `EF-VSN-*`, `EF-PRD-*`, `EF-TEC-*`, `EF-MKT-*` | Data-source provenance, semantics, escalation, consent, observability, and fail-closed requirements constrain how historical ideas could be used. |
| `REL-010` | Visuals do not establish underlying claims | `EF-DSN-012`–`018` → related `EF-AGR-*` / `EF-REG-*` claims | Charts are historical communication artifacts unless the cited source/data/method is independently recoverable and revalidated. |

## Evidence-Label Translation Rules

| Atlas label | Use in this archive |
|---|---|
| `historical_intent` | Historical founder vision, requirements, feature mechanics, stack preference, design direction, and pitch content. |
| `secondary_synthesis` | Reports or consolidations that interpret, restate, or combine other sources. They preserve reasoning and leads, but are not primary proof. |
| `research_design_only` | Research plans, interview guides, recruitment/consent material, evaluation forms, source-test plans, and field governance. |
| `supported_inference` | Bounded study notes or direct test artifacts whose method and scope permit a limited inference. The limitation note remains mandatory. |
| `needs_revalidation` | Institutional captures, market/weather/source references, dated external facts, unresolved provider availability, and any quantitative claim needing a current primary source. |
| `product_hypothesis` | Intended solution effects, feature benefits, AI outputs, scalability claims, and commercial impact claims that have not been demonstrated. |
| `unknown` | Missing provenance, method, date, scope, or attributable evidence. Absence of information must remain visible rather than being filled by inference. |

## Current-Use Rules

The Atlas uses `governing` only for current archive rules and active P0/field evidence controls. `historical_context` is appropriate for vision, product, technical, and design families. `candidate_input` is appropriate for research syntheses, bounded local notes, and sources awaiting claim-level revalidation. `not_currently_used` is appropriate where a visual or duplicate-like artifact carries no claim beyond historical context. No raw conversation, credentials, workspace code, or private processing artifact becomes public Atlas evidence.

## Reconciliation Outcomes for Trace Mapping

The next stage must create atomic `EVA-*` records that cite a **specific source span and retrieval chunk**. Every trace record must carry the evidence label above, explicit geography/time/population scope, a limitation note, relationship links, and a current-use designation. Source-family membership is never sufficient evidence by itself.

**Machine-readable companion:** [EcoFarm_Source_Family_Reconciliation.json](EcoFarm_Source_Family_Reconciliation.json)
