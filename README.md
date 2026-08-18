# EcoFarm Archives

This repository is a **curated, source-traceable knowledge archive** for EcoFarm. It is not a dump of every file ever created around the project. The archive preserves material that has been reviewed as substantively useful for EcoFarm’s vision, product mechanics, technical reasoning, research, field validation, data safety, historical design, or decision history.

> The archive is intentionally non-final. A historical feature, research plan, agent synthesis, market hypothesis, source test, or pitch artifact should never be read as proof that the capability is validated, currently approved, or guaranteed to be built.

## Start here

| File or directory | Purpose |
|---|---|
| [`CURATED_ARCHIVE_INDEX.md`](CURATED_ARCHIVE_INDEX.md) | Human-readable register of every curated canonical source with category-aware ID, role, legacy trace, and GitHub file link. |
| [`10_knowledge_base_outputs/EcoFarm_Master_Knowledge_Base.md`](10_knowledge_base_outputs/EcoFarm_Master_Knowledge_Base.md) | Hyper-detailed human-readable master knowledge base. |
| [`10_knowledge_base_outputs/html_knowledge_site/`](10_knowledge_base_outputs/html_knowledge_site/) | Static navigable HTML edition of the knowledge base. |
| [`10_knowledge_base_outputs/llm_knowledge_corpus/`](10_knowledge_base_outputs/llm_knowledge_corpus/) | Retrieval-oriented corpus and external-LLM use guidance. |
| [`archive_metadata/`](archive_metadata/) | Legacy crosswalk, inclusion/exclusion record, semantic review, coverage record, and public-release audit. |

## Curated category system

| Prefix | Category | What belongs here |
|---|---|---|
| `EF-GOV` | Governance and archive | Founder approvals, decision records, archive rules, and governing context. |
| `EF-VSN` | Founder vision and evolution | Onboarding documents, original thesis, and scope evolution. |
| `EF-PRD` | Product concept and feature mechanics | Feature intent, workflows, PRDs, capability logic, and MVP rationale. |
| `EF-TEC` | Technical architecture, hardware, and AI | Stack reasoning, data/system architecture, sensor/hardware research, and AI framing. |
| `EF-AGR` | India agriculture problem research | Farmer problems, agricultural distress, structural and global/India context. |
| `EF-REG` | Regional microcosm and Namakkal research | Kongu/Namakkal/Punjab comparison, regional context, and location-entry rationale. |
| `EF-MKT` | Market, commercial, and ecosystem research | Market/alternative research, ecosystem mapping, and commercial hypotheses. |
| `EF-FLD` | Farmer decision and field validation | Farmer-problem research, field methods, consent, event/outcome instruments, and validation logic. |
| `EF-DAT` | Data sources, safety, and P0 feasibility | Source controls, P0 tests, consent/data models, safety, referral, and observability. |
| `EF-DSN` | Historical design, pitch, and media | Mockups, wireframes, decks, pitches, and research communication assets. |

## Why some files are absent from the primary catalogue

The original preservation corpus contained **390** raw artifacts. The curated archive retains **97** canonical substantive records. The remainder are documented in [`archive_metadata/inclusion_exclusion_register.md`](archive_metadata/inclusion_exclusion_register.md) as one of the following:

- exact duplicate or semantic alias of a retained canonical record;
- generic application code, dependency/configuration file, or generated build output from the unrelated EcoFarm pilot/task-tracker workspace;
- low-signal, incomplete, redundant, or non-evidence item;
- raw conversation/context trace retained in private preservation rather than treated as normal evidence.

The code that generates, validates, and serves this archive is kept in [`archive_infrastructure/`](archive_infrastructure/). It is separated from research and product evidence on purpose.

## Source identifiers and links

Curated citations use IDs such as `EF-FLD-001` or `EF-DAT-007`. Each corresponds to one canonical file and is linked from the master document directly to GitHub. Original sequential `SRC-xxxx` identifiers are retained in [`archive_metadata/legacy_source_crosswalk.csv`](archive_metadata/legacy_source_crosswalk.csv) for traceability.

## Public-release handling

The public copy has been scanned for credential patterns and contact identifiers. Contact identifiers detected in reviewed records have been redacted in the public archive copy; the raw preservation corpus is retained separately and unchanged. See [`archive_metadata/public_release_audit.md`](archive_metadata/public_release_audit.md) and [`archive_metadata/public_release_redaction_log.md`](archive_metadata/public_release_redaction_log.md).

## Updating the archive

1. Preserve a new raw artifact before summarizing it.
2. Review whether it is substantively useful, an alias, or archive infrastructure.
3. Assign a category-aware `EF-*` identifier only to canonical substantive records.
4. Update the crosswalk, semantic-supersession register, Master Knowledge Base, LLM corpus, and HTML site.
5. Re-run the public-release audit and redaction pass before pushing changes.

