# EcoFarm Archives

EcoFarm Archives is a **curated, source-traceable knowledge base**. It is intentionally non-final: it preserves vision, conceptual mechanics, product hypotheses, technical reasoning, research, field methods, data and safety constraints, historical alternatives, and unresolved questions without pretending that archive presence equals validation.

> **Core reading rule:** A historical feature is not proof of implementation. A research plan is not a field result. A secondary report is not primary evidence. Read every material item according to its stated authority and limitation.

## Choose your entry point

| You are… | Start here | Why |
|---|---|---|
| New to EcoFarm | [Start Here](00_START_HERE/README.md) | A short route to the right archive layer. |
| Reading the project as a person | [Master Knowledge Base](10_knowledge_base_outputs/EcoFarm_Master_Knowledge_Base.md) | The most complete human-readable synthesis. |
| Browsing by topic | [HTML Knowledge Site](10_knowledge_base_outputs/html_knowledge_site/index.html) | Searchable, navigable reading experience. |
| Checking what a statement actually supports | [Evidence Atlas](10_knowledge_base_outputs/evidence_atlas/README.md) | Evidence labels, source relationships, trace maps, gaps, and revalidation boundaries. |
| An LLM or autonomous agent | [LLM / Agent Handoff](00_START_HERE/LLM_AGENT_HANDOFF.md) | Retrieval order and rules against evidence inflation. |
| Looking for an exact source | [Curated Archive Index](CURATED_ARCHIVE_INDEX.md) | Stable `EF-*` IDs, roles, aliases, and canonical GitHub paths. |
| Maintaining the archive | [Infrastructure Guide](archive_infrastructure/README.md) | Rebuild, audit, and publication workflow. |

## Repository map

| Area | What it contains | Use boundary |
|---|---|---|
| [`00_START_HERE/`](00_START_HERE/) | Reading paths and AI-agent handoff material. | Navigation only; not primary evidence. |
| `00_`–`09_` source directories | The 114 reviewed canonical `EF-*` records, grouped by source family. | Durable primary archive paths. |
| [`10_knowledge_base_outputs/`](10_knowledge_base_outputs/README.md) | Master Knowledge Base, HTML site, LLM corpus, and Evidence Atlas. | Synthesis and retrieval layers linked back to source records. |
| [`archive_metadata/`](archive_metadata/README.md) | Curation treatment, source crosswalks, coverage, version relationships, and release audits. | Explains provenance and handling; not independent domain proof. |
| [`archive_infrastructure/`](archive_infrastructure/README.md) | Archive-maintenance utilities. | Local maintenance only; not EcoFarm product code. |

The private preservation corpus contains **392** raw artifacts; the public curated archive retains **114** substantive canonical records. Exact duplicates, generic app code, generated builds, low-signal files, and raw conversation traces are not mixed into ordinary evidence browsing.

## Important current treatment

The Evidence Atlas was created only after the mandatory individual full-file review of all 114 curated sources. It preserves historical intent, research design, evidence limits, contradictions, and revalidation gaps; it does not make a product, field-validation, market, or investment conclusion.

For sensor research, [`EF-TEC-005`](03_technical_architecture_hardware_ai/EF-TEC-005__grok_ecofarm_module_sensor_research.md) is the preferred parseable historical conversation record. Earlier FireShot/text captures remain provenance aliases and are excluded from normal retrieval. [`EF-TEC-007`](03_technical_architecture_hardware_ai/EF-TEC-007__conversation2_ecofarmmodulesensoralternativesresearch.md) preserves complementary alternatives and selection criteria.

## Public-release and maintenance rule

Public files are scanned and redacted for credential patterns and contact identifiers; see the [release audit](archive_metadata/public_release_audit.md) and [redaction log](archive_metadata/public_release_redaction_log.md). When adding material, preserve and review it first, assign an `EF-*` ID only to a canonical source, refresh the crosswalk and knowledge outputs, sanitize, audit, check links, then publish.
