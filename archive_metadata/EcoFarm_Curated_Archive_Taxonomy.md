# EcoFarm Curated Archive Taxonomy and Source-ID Scheme

> **Purpose:** Transform the initial preservation corpus into a human-organized, semantically curated archive. The archive must make it easy to find meaningful EcoFarm material without treating workspace code, generated files, exact duplicates, or operational noise as evidence.

## Governing rules

1. A file enters the primary curated archive only when a direct skim shows it has lasting value for EcoFarm’s vision, product reasoning, research evidence, technical reasoning, validation work, or historical design record.
2. Similar files are organized as a **family**. One canonical record receives the category-aware source ID; genuine revised versions remain distinct, while byte-identical or format-equivalent copies become aliases.
3. Project application code, package/dependency metadata, build outputs, and internal task-tracker plumbing are not EcoFarm knowledge evidence. They are excluded from the primary catalogue.
4. Code used to generate, validate, or publish the curated archive belongs in `archive_infrastructure/`, separate from evidence and research.
5. Every retained canonical record must have a stable GitHub path and link. The knowledge base will cite those paths instead of local sandbox-only identifiers.
6. Material is classified by its **substantive purpose**, not merely by where it was found or which task produced it.

## Curated evidence categories

| Prefix | Repository directory | Included material | Excluded or demoted material |
|---|---|---|---|
| `EF-GOV` | `00_governance_and_archive/` | Founder approvals, archive rules, source maps, evidence taxonomy, decision/history registers. | Generic task tracker artifacts and non-EcoFarm project settings. |
| `EF-VSN` | `01_founder_vision_and_evolution/` | Onboarding documents, founder vision, thesis evolution, historical scope revisions. | Duplicate format exports where the canonical text is already preserved. |
| `EF-PRD` | `02_product_concept_and_feature_mechanics/` | PRDs, capability logic, workflow models, conceptual feature dossiers, decision flows. | Screen-level boilerplate and generic component source code. |
| `EF-TEC` | `03_technical_architecture_hardware_ai/` | Architecture, stack rationale, sensors, hardware/IoT, AI reasoning, data models. | Framework config, package locks, ordinary app component code. |
| `EF-AGR` | `04_india_agriculture_problem_research/` | India-wide farmer problems, agricultural stress, suicide/crisis context, structural/global comparison research. | Charts without usable underlying source/context, unless retained as historical communication artifacts. |
| `EF-REG` | `05_regional_microcosm_and_namakkal_research/` | Kongu/Namakkal/Punjab comparisons, microcosm profiling, crop/regional research, local operating conditions. | Local copies with no EcoFarm relevance. |
| `EF-MKT` | `06_market_commercial_and_ecosystem_research/` | Market research, alternatives, farmer buyer/market dynamics, commercial hypotheses, ecosystem mapping. | Pitch claims treated as evidence of traction. |
| `EF-FLD` | `07_farmer_decision_and_field_validation/` | Farmer problem research, decision scoring, field/interview/event material, consent, outcomes, validation plans. | Unused form copies or generated redundancy; retain one canonical form/version chain. |
| `EF-DAT` | `08_data_sources_safety_and_p0_feasibility/` | Data-source registers, source tests, P0 design, consent, safety, provenance, observability, referrals. | Live credentials, access tokens, or duplicated reports. |
| `EF-DSN` | `09_historical_design_pitch_and_media/` | Mockups, wireframes, conceptual design assets, historical decks, proposals, selected pitch artefacts. | Image/cache duplicates and unrelated design exports. |
| `EF-KB` | `10_knowledge_base_outputs/` | Markdown master, LLM corpus, HTML site, validation report, curated index. | Raw inputs already represented in an evidence category. |
| `EF-INF` | `archive_infrastructure/` | HTML generator, corpus builder, validators, packaging instructions, site assets. | The EcoFarm pilot/task-tracker application and unrelated developer tooling. |

## Category-aware source-ID grammar

```text
EF-<CATEGORY>-<THREE-DIGIT-SEQUENCE>
```

Examples:

| Curated ID | Meaning |
|---|---|
| `EF-VSN-001` | Canonical founder/onboarding vision document. |
| `EF-PRD-004` | Historical feature/workflow specification. |
| `EF-TEC-007` | Technical architecture or sensor research item. |
| `EF-AGR-003` | India-wide agricultural problem research report. |
| `EF-REG-005` | Namakkal/Kongu/microcosm research artifact. |
| `EF-MKT-002` | Market/alternatives/ecosystem research artifact. |
| `EF-FLD-009` | Field validation or farmer-decision research artifact. |
| `EF-DAT-006` | Data-source/P0/safety/provenance artifact. |
| `EF-DSN-003` | Historical design/pitch/media artifact. |
| `EF-GOV-004` | Governing archive or decision record. |

Legacy `SRC-xxxx` values remain in the preservation manifest as traceability aliases. The curated index maps each retained `EF-*` canonical ID to all relevant legacy IDs, raw archive paths, duplicate aliases, status, and GitHub link.

## Proposed GitHub repository layout

```text
EcoFarm_Archives/
├── README.md
├── CURATED_ARCHIVE_INDEX.md
├── 00_governance_and_archive/
├── 01_founder_vision_and_evolution/
├── 02_product_concept_and_feature_mechanics/
├── 03_technical_architecture_hardware_ai/
├── 04_india_agriculture_problem_research/
├── 05_regional_microcosm_and_namakkal_research/
├── 06_market_commercial_and_ecosystem_research/
├── 07_farmer_decision_and_field_validation/
├── 08_data_sources_safety_and_p0_feasibility/
├── 09_historical_design_pitch_and_media/
├── 10_knowledge_base_outputs/
│   ├── EcoFarm_Master_Knowledge_Base.md
│   ├── html_knowledge_site/
│   └── llm_knowledge_corpus/
├── archive_infrastructure/
└── archive_metadata/
    ├── curated_source_index.json
    ├── inclusion_exclusion_register.md
    ├── legacy_source_crosswalk.csv
    └── semantic_supersession_register.md
```

## Primary catalogue behaviour

The HTML source catalogue will default to **canonical substantive source records only**. It will show category, title, source role, evidence/temporal status, version/alias relationship, and a direct GitHub link. A separate archival disclosure can state the count of excluded code/generated files and duplicate aliases without mixing them into ordinary browsing.

