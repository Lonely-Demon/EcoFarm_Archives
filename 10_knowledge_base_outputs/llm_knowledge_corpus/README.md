# EcoFarm LLM-Optimized Knowledge Corpus

This directory is designed for retrieval, ingestion, and exact source tracing by external language models. It does not replace the human-readable Master Knowledge Base.

## Files

| File | Purpose |
|---|---|
| `EcoFarm_LLM_Knowledge_Documents.json` | Source-level metadata, duplicate relations, status hints, and document tags. |
| `EcoFarm_LLM_Knowledge_Chunks.jsonl` | Retrieval-ready source chunks. Every chunk contains the exact source ID, path, heading context, status hint, tags, and text. |
| `EcoFarm_LLM_Topic_Index.json` | Topic-to-chunk lookup index. |

## Retrieval rules

Treat each chunk as source-specific evidence. Use `source_id` and `relative_path` when citing. Do not turn a `plan_or_method_artifact` into completed validation, and do not infer current approval from a `historical_product_or_technical_artifact`. Exact duplicates and explicitly designated semantic retrieval aliases remain recorded at the document level but are excluded from duplicate chunk copies.

## Corpus statistics

- Documents represented: 183
- Canonical text chunks: 901
- Retrieval topics: 16
