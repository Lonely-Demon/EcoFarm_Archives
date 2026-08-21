# Archive Infrastructure

These scripts maintain the curated archive. They are **maintenance utilities**, not EcoFarm product code and not ordinary evidence. Run them only in a controlled local working copy where the private preservation corpus and output paths are available.

| Workflow | Main scripts |
|---|---|
| Source registration and canonical curation | `build_source_manifest.py`, `build_curated_archive.py`, `register_preferred_sensor_exports.py` |
| Corpus and retrieval metadata | `build_llm_knowledge_corpus.py`, `augment_llm_corpus_with_curated_metadata.py` |
| Source relationships and checks | `build_semantic_supersession_review.py`, `compare_version_families.py`, `build_corpus_coverage_register.py` |
| Human-readable outputs | `build_html_knowledge_site.py`, `update_evidence_atlas_html.py` |
| Public-release safeguards | `sanitize_public_curated_archive.py`, `audit_public_curated_archive.py`, `validate_knowledge_deliverables.py` |

The safe maintenance order is: preserve and review a new source; register it; rebuild the curated archive and corpus; update the Evidence Atlas where required; sanitize; audit; check links; then publish. Keep raw conversations, credentials, local workspace data, and transient working notes out of the public repository.
