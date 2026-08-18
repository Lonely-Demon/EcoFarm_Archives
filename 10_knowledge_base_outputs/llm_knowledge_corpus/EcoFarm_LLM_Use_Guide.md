# External LLM Use Guide — EcoFarm Knowledge Corpus

## Recommended ingestion order

Start with the human-readable `EcoFarm_Master_Knowledge_Base.md` for conceptual orientation. Then provide the topic index and only the chunks needed for the specific question. This reduces context-window waste and ensures that granular answers retain their provenance.

| Question type | Recommended retrieval path |
|---|---|
| Founder intention, concept, or feature mechanics | Find topics in `EcoFarm_LLM_Topic_Index.json`, then retrieve matching chunk(s) and historical onboarding/design sources. |
| Current field/P0 posture | Retrieve current-session approval sources plus Research Agent 1/2 and P0 chunks. |
| Data-source or safety question | Retrieve source-hierarchy, P0 test, consent, observability, and referral chunks; then check the semantic-supersession register. |
| Historical product/technical question | Retrieve onboarding, PRD, flows, stack, sensor, and proposal chunks, keeping historical status explicit. |
| Conflict or version question | Read both involved chunks and the content-based supersession comparison; do not infer recency from filename alone. |

## JSONL retrieval pattern

Each line in the chunks file can be retrieved independently. Select chunks based on `topics`, `heading_path`, `source_group`, and keyword search in `text`. The key fields are:

```text
chunk_id                 Stable chunk identifier
source_id                Stable raw-source identifier
canonical_source_id      Canonical representative when a duplicate family exists
source_group             Origin of material
heading_path             Context within the original source
topics                   Retrieval tags
evidence_status_hint     Not a final verdict; a reasoned status hint
temporal_status_hint     Historical/current/unknown time context
text                     Grounded source passage
```

## Example question

> “How was automatic irrigation intended to work, what constraints were later recognised, and what must be validated before it is built?”

Retrieve chunks tagged with hardware, sensor, irrigation, automation, safety, and P0; cite the historical architecture sources for intended mechanics and the current safety/P0 sources for constraints. The answer must separate **historical intended capability** from **current evidence requirement**.
