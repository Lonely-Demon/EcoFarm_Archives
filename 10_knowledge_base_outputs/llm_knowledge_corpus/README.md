# EcoFarm LLM-Optimized Knowledge Corpus

This directory is designed for retrieval, ingestion, and exact source tracing by external language models. It does not replace the human-readable Master Knowledge Base.

## Files

| File | Purpose |
|---|---|
| `EcoFarm_LLM_Knowledge_Documents.json` | Source-level metadata, duplicate relations, status hints, and document tags. |
| `EcoFarm_LLM_Knowledge_Chunks.jsonl` | Retrieval-ready source chunks. Every chunk contains the exact source ID, path, heading context, status hint, tags, and text. |
| `EcoFarm_LLM_Topic_Index.json` | Topic-to-chunk lookup index. |
| `EcoFarm_LLM_Use_Guide.md` | Recommended retrieval order, JSONL fields, example question handling, and external-model operating rules. |

## Retrieval rules

Treat each chunk as source-specific evidence. Use `source_id` and `relative_path` when citing. Do not turn a `plan_or_method_artifact` into completed validation, and do not infer current approval from a `historical_product_or_technical_artifact`. Exact duplicates remain recorded at the document level but are excluded from duplicate chunk copies.

For every material response, cite the relevant `source_id`, `chunk_id`, and heading context. Preserve the evidence-status and temporal-status hints. Where sources conflict, consult the adjacent semantic-supersession and content-based comparison registers rather than silently choosing one. A minimal external-model prompt is available in `EcoFarm_LLM_Use_Guide.md`.

## Corpus statistics

- Documents represented: 181
- Canonical text chunks: 1034
- Retrieval topics: 16
