# EcoFarm Evidence Atlas

## Purpose

This directory contains the **post-review evidence layer** for the EcoFarm archive. It was created only after every one of the 113 curated `EF-*` canonical sources was individually read in full. The Atlas preserves uncertainty and source boundaries; it does not convert historical ideas, field methods, or visual materials into validation.

## Start Here

| Read this | When you need |
|---|---|
| `EcoFarm_Evidence_Atlas.md` | A human-readable guide to authority, evidence labels, feature boundaries, open questions, and primary-source revalidation. |
| `full_file_review/EcoFarm_Full_File_Review_Completion_Record.md` | The method and completion check for the mandatory individual-review stage. |
| `EcoFarm_Source_Family_Reconciliation.md` | The relationship and authority treatment of the ten curated source families. |
| `EVA_Core_Trace_Records.jsonl` | Cross-source constraints, historical intent, contradictions, and open questions in machine-readable form. |
| `EVA_Source_Review_Records.jsonl` | One stable record per individually reviewed canonical source, with a durable canonical GitHub URL and limitation note. |

## LLM Retrieval Order

An LLM should first load the relevant `EVA-CORE-*` record, then retrieve the referenced `EF-*` canonical source using its `canonical_source_urls` and/or `chunk_ids`. It should preserve the record’s `evidence_label`, `limitation_note`, `geography`, `time_scope`, `population_scope`, and `current_use` fields in any answer. If a question needs a present-tense external fact, consult `EVA_Revalidation_Ledger.json` first; a historical source does not substitute for a current primary source.

## Dataset Inventory

| Artifact | Role |
|---|---|
| `EVA_Feature_Evidence_Map.json` | Historical feature-family intent paired with field/P0/data qualifications. |
| `EVA_Claim_Source_Map.json` | Claim families, source sets, evidence labels, and revalidation priority. |
| `EVA_Decision_Assumption_Map.json` | Historical decision logic and exposed assumptions. |
| `EVA_Contradiction_Open_Question_Register.json` | Explicit preserved tensions and unknowns. |
| `EVA_Revalidation_Findings.md` | Narrow, dated primary-source findings; no product inference. |
| `EVA_Revalidation_Ledger.json` | Revalidation status, primary sources checked, bounded conclusions, and remaining gaps. |
| `EVA_Trace_Dataset_Manifest.json` | Dataset counts and the full canonical-source coverage list. |

## Privacy and Archive Boundary

This public directory excludes raw conversation logs, workspace code, credentials, private tool records, generated local working files, and transient review working notes. Canonical source materials remain under the category directories at the repository root. The source-review ledger and completion record are published only as evidence-governance records; they are not a replacement for the linked canonical sources.

## Non-Conclusion Rule

> A feature described in a historical onboarding file is a preserved idea. A field guide is a preserved method. A test artifact is a bounded observation. Neither becomes a validated product claim without new, attributable evidence.
