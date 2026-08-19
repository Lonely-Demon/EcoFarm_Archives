# EcoFarm Archives

This repository is a **curated, source-traceable knowledge archive** for EcoFarm. It is not a raw file dump. Every primary source was reviewed for lasting value to EcoFarm’s vision, product mechanics, technical reasoning, research, field validation, data safety, historical design, or decision history.

> The archive is non-final. A historical feature, research plan, agent synthesis, market hypothesis, source test, or pitch artifact is not proof that a capability is validated, currently approved, or guaranteed to be built.

## Start here

| Location | Purpose |
|---|---|
| [`CURATED_ARCHIVE_INDEX.md`](CURATED_ARCHIVE_INDEX.md) | Human-readable register of reviewed canonical sources, category-aware IDs, roles, legacy trace, and GitHub links. |
| [`10_knowledge_base_outputs/EcoFarm_Master_Knowledge_Base.md`](10_knowledge_base_outputs/EcoFarm_Master_Knowledge_Base.md) | Hyper-detailed human-readable knowledge base. |
| [`10_knowledge_base_outputs/html_knowledge_site/`](10_knowledge_base_outputs/html_knowledge_site/) | Static, navigable HTML knowledge base. |
| [`10_knowledge_base_outputs/llm_knowledge_corpus/`](10_knowledge_base_outputs/llm_knowledge_corpus/) | Retrieval-oriented corpus and external-LLM use guide. |
| [`10_knowledge_base_outputs/evidence_atlas/`](10_knowledge_base_outputs/evidence_atlas/) | Evidence labels, source-family reconciliation, 114 completed full-file review records, feature/claim/assumption maps, open questions, and bounded primary-source revalidation. |
| [`archive_metadata/`](archive_metadata/) | Crosswalk, semantic review, inclusion/exclusion record, and public-release audit. |

## Meaningful source categories

`EF-GOV` governance/archive · `EF-VSN` founder vision/evolution · `EF-PRD` product/feature mechanics · `EF-TEC` technical architecture/hardware/AI · `EF-AGR` India agriculture problem research · `EF-REG` regional/Namakkal research · `EF-MKT` market/commercial/ecosystem research · `EF-FLD` farmer decision/field validation · `EF-DAT` data sources/safety/P0 feasibility · `EF-DSN` historical design/pitch/media.

The preserved corpus contains **392** raw artifacts. This curated archive retains **114** canonical substantive records. Exact duplicates, generic app code, dependency/configuration files, generated builds, low-signal items, and raw conversation traces are documented rather than mixed into ordinary evidence browsing. Archive-generation code is kept separately under [`archive_infrastructure/`](archive_infrastructure/).

The Evidence Atlas was created after the mandatory individual full-file review of all 114 curated sources. Its records preserve historical intent, research design, evidence limits, contradictions, and revalidation gaps. The Atlas does not make a product, field-validation, market, or investment conclusion on the archive’s behalf.

For sensor research, [`EF-TEC-005`](03_technical_architecture_hardware_ai/EF-TEC-005__grok_ecofarm_module_sensor_research.md) is the preferred parseable Markdown record. The earlier FireShot PDF/text captures remain raw-provenance aliases and are deliberately excluded from normal retrieval; [`EF-TEC-007`](03_technical_architecture_hardware_ai/EF-TEC-007__conversation2_ecofarmmodulesensoralternativesresearch.md) preserves complementary alternatives and selection criteria.

## Public-release policy

The public copy is scanned for credential patterns and contact identifiers; detected contact identifiers are redacted in this repository while the private preservation corpus remains unchanged. See [`archive_metadata/public_release_audit.md`](archive_metadata/public_release_audit.md) and [`archive_metadata/public_release_redaction_log.md`](archive_metadata/public_release_redaction_log.md).

## Updating

Preserve a raw artifact, review it for substantive value, assign an `EF-*` ID only to a canonical source, update the crosswalk and knowledge outputs, then rerun the public-release audit/redaction workflow before publishing.
