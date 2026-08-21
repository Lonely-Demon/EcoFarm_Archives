# LLM / Agent Handoff

## Purpose

Use this sequence when an AI agent is asked to answer, analyze, summarize, or plan from the EcoFarm archive. The archive is designed to preserve reasoning and uncertainty; it must not be compressed into unsupported product, market, field-validation, or investment conclusions.

## Required retrieval order

1. Read the [LLM Corpus Use Guide](../10_knowledge_base_outputs/llm_knowledge_corpus/EcoFarm_LLM_Use_Guide.md) and the [Evidence Atlas README](../10_knowledge_base_outputs/evidence_atlas/README.md).
2. Retrieve the relevant `EVA-*` trace record where one exists. Preserve its `evidence_label`, `limitation_note`, scope fields, relationship, and `current_use` designation.
3. Open the linked canonical `EF-*` source via its `canonical_github_url` or category path before making a substantive assertion.
4. For a present-tense external fact, treat historical sources as leads only. Consult the Atlas revalidation materials and then a current attributable primary source.
5. State what is supported, what is only historical intent or a hypothesis, and what remains unknown.

## Non-negotiable rules

| Rule | Required agent behaviour |
|---|---|
| Do not upgrade archive presence into validation | Do not call a described feature built, useful, safe, adopted, or ready without evidence at that level. |
| Preserve scope | Retain geography, date, population, method, and source boundaries instead of generalizing. |
| Preserve contradictions | Identify version differences and unresolved alternatives; do not silently select a “final” historical version. |
| Keep safety and data controls active | Apply the P0 provenance, consent, escalation, and observability constraints to any data-enabled interpretation. |
| Cite recoverably | Include `EF-*` IDs and canonical GitHub source paths. Use `EVA-*` IDs where a trace record is relevant. |

## Preferred source treatment

`EF-TEC-005` is the preferred parseable historical sensor-research record. The earlier FireShot/text captures are provenance aliases, not normal retrieval sources. `EF-TEC-007` is complementary alternatives research. Neither establishes current component qualification, cost, regulatory suitability, field performance, or a deployment decision.

## Minimum answer structure

For any consequential question, provide a concise answer in four parts: **what the archive preserves**, **what it supports**, **what it does not establish**, and **what evidence would be needed next**.
