# EcoFarm Evidence-Status Taxonomy

This taxonomy governs all three knowledge-base formats. It classifies the **status of a statement within the available archive**, not whether the statement is ultimately true or desirable.

| Code | Label | Meaning | Examples | Not permitted to infer |
|---|---|---|---|---|
| `FI` | Founder instruction / intent | An explicit founder requirement, objective, preference, constraint, or approval. | The desired knowledge-base form; the broad EcoFarm vision. | External validation or technical feasibility. |
| `HV` | Historical vision / concept | A past expression of the EcoFarm vision, design, architecture, or feature set. | Hardware-plus-software ecosystem; community and market concepts. | Current approval, validated demand, or build readiness. |
| `PD` | Proposal / design | A feature, workflow, stack, architecture, test, or operating design proposed in a source. | MVP feature list; source hierarchy; decision-packet design. | Completed implementation or tested real-world outcome. |
| `RH` | Research hypothesis | A problem, segment, causal theory, or expected user behaviour proposed for investigation. | Groundnut entry wedge; information-translation gap. | Field validation, willingness to pay, adoption, or prevalence. |
| `SR` | Secondary research / cited context | A source-derived fact, study summary, market claim, or institutional description reported by a source. | District crop context; published study result. | Local current behaviour beyond the source conditions. |
| `DO` | Direct observation / operational artifact | A captured source response, test result, event record, or completed evidence artifact. | TNAU locality failure; HTTP responses; simulated failure records. | Broad generalisation beyond the tested source or fixture. |
| `OP` | Operating policy / safety control | A current internal rule for how EcoFarm should behave if built or tested. | Fail closed; no autonomous pesticide prescription; referral wording. | Regulatory approval, institutional endorsement, or user acceptance. |
| `DA` | Deferred / abandoned / rejected path | A direction explicitly postponed, narrowed, or rejected under stated conditions. | Automated TNAU weather path for first P0; broad P0 product scope. | Permanent impossibility or rejection of the long-term concept. |
| `UQ` | Unresolved question | A material unknown, contradiction, missing data point, or decision requiring more evidence. | Whether farmers trust the workflow; reuse rights for data sources. | A positive or negative answer. |
| `AS` | Agent synthesis / analytical judgement | A model-generated or analyst-generated interpretation clearly marked as such. | Candidate-decision scores; comparative recommendation. | Independent evidence or definitive truth. |

## Temporal statuses

Use these separately from the evidence-status code:

| Status | Meaning |
|---|---|
| `historical` | Belongs to a previous version of EcoFarm’s thinking. |
| `current_working` | Current internal direction or operating constraint, subject to revision. |
| `future_hypothesis` | Intended possibility requiring future evidence or design work. |
| `operational_test_result` | Result of a bounded test with recorded conditions. |
| `deferred_or_rejected` | Not to be used in the stated context unless reopening conditions are met. |
| `unresolved` | Cannot yet be categorized confidently. |

## Core interpretation rules

1. An `FI` item has high authority over document format and project intent, but does not validate an external fact.
2. A `DO` item is strong only within its explicit test conditions.
3. A `PD`, `RH`, or `AS` item must never be written as if it were a completed product outcome or customer validation.
4. A `DA` item remains part of the knowledge base because its constraints and reasoning may be reopened under different conditions.
5. When sources conflict, preserve both source records and assign `UQ` until a later artifact resolves the conflict.
