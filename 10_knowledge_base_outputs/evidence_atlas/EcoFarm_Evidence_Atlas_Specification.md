# EcoFarm Evidence Atlas — Specification and Boundaries

## Purpose

The Evidence Atlas is an archive-only trace layer for EcoFarm. It does not choose a product wedge, recommend investment, rewrite the founder’s vision, or turn desk research into field validation. Its purpose is to make the reasoning already present in the EcoFarm corpus easier to inspect, challenge, and reuse.

> **Core rule:** A trace record explains what a source says and how the archive has used it. It never upgrades a historical claim, a research design, a model-generated synthesis, or a product hypothesis into verified fact.

## Confirmed input list

| Input set | Planned use | Authority boundary |
|---|---|---|
| **114 curated canonical `EF-*` source records** | Primary source material for claims, feature intentions, research observations, and decision rationale | Canonical publication record; evidence status still varies by source |
| **183 LLM knowledge documents and 901 retrieval chunks** | Source-span discovery and retrieval backbone | Navigation aid; not independent evidence |
| **Master Knowledge Base** | Identify concepts/features that require trace links | Interpretive synthesis; must link back to source records |
| **Curation, supersession, coverage, and review registers** | Clarify duplicate, historical, contextual, and excluded material | Archive-governance evidence, not domain evidence |
| **Visual-asset metadata and selected historical visuals** | Record design/communication context without inventing visual claims | Historical/design context only unless a source establishes the underlying fact |
| **Primary public sources referenced by high-impact current claims** | Freshness and provenance checks | Used only to label currentness or correct a source citation; no strategic conclusion changes |

## Atomic trace record

Every record must have a stable `EVA-*` identifier and the following fields:

| Field | Meaning |
|---|---|
| `trace_type` | `claim`, `feature_intent`, `assumption`, `decision`, `research_finding`, `open_question`, `contradiction`, or `constraint` |
| `statement` | Compact, faithful restatement of the source material |
| `source_ids` and `chunk_ids` | Curated EF records and normalized-text chunks enabling exact recovery |
| `source_excerpt` | Brief supporting excerpt or heading cue; never an invented quotation |
| `evidence_label` | `verified_fact`, `supported_inference`, `product_hypothesis`, `historical_intent`, `secondary_synthesis`, `research_design_only`, `unknown`, or `needs_revalidation` |
| `geography`, `time_scope`, and `population_scope` | Scope boundary; `not_specified` is acceptable and meaningful |
| `confidence` | `high`, `medium`, or `low`, with a limitation note |
| `relationships` | `supports`, `qualifies`, `contradicts`, `supersedes`, `depends_on`, `tests`, or `does_not_establish` links |
| `current_use` | `governing`, `historical_context`, `candidate_input`, `private_context`, or `not_currently_used` |

## Required outputs

The programme will produce a human-readable Atlas, machine-readable JSON/JSONL tables, concept maps, feature-evidence maps, decision-assumption maps, a contradiction/open-question register, a revalidation ledger, and HTML navigation. All public output will remain inside the curated EcoFarm archive; raw conversation logs, workspace code, credentials, and private preservation records remain excluded.

## Non-conclusion and safety rules

1. **No validation inflation.** Field forms, launch kits, and protocols remain research designs unless actual field observations are documented.
2. **No source laundering.** A secondary synthesis remains secondary even when it is useful.
3. **No scope creep.** No EcoFarm Pilot/task-board code, application features, investor narrative, or new product proposal belongs in this programme.
4. **No false precision.** Missing geography, dates, samples, and methodologies must remain explicit gaps.
5. **No silent replacement.** Contradictions and version changes must be recorded as relationships, not erased.
