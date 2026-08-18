# EcoFarm Core Source Map

This is the high-value reading and citation map for the Master Knowledge Base. The full machine-readable inventory is in `manifest/EcoFarm_Source_Manifest.json`; this map identifies the primary sources most likely to govern a section’s interpretation.

| Source ID | Primary role | Evidence / temporal status | What it contributes | Main caution |
|---|---|---|---|---|
| `SRC-0134` | Canonical current main-conversation capture | `FI`, `current_working` | Founder instructions, preservation requirements, and three-format delivery contract. | Curated canonical capture; use it for governing intent, not external facts. |
| `SRC-0135` | Current approvals record | `FI`, `current_working` | Explicit approval of non-final, concept-first knowledge base. | Summary record, not independent research. |
| `SRC-0039` | Later historical onboarding document | `HV` + `PD`, `historical` | Broad integrated hardware/software vision, original feature mechanics, MVP concepts, sensor rationale. | Contains historical projections and citations requiring current validation; not current P0 scope. |
| `SRC-0040` | Later onboarding final version | `HV` + `PD`, `historical` | Condensed EcoFarm conceptual identity and hardware/software system framing. | Earlier strategic version; must not override current field/P0 evidence. |
| `SRC-0006` | Historical PRD | `PD`, `historical` | Original product requirements, user/workflow logic, feature implications. | Requirements reflect an earlier broad scope. |
| `SRC-0005`, `SRC-0023`, `SRC-0024` | Historical screen/flow and wireframe records | `PD`, `historical` | User-flow intent and design logic for feature mechanics. | Preserve conceptual flows; do not treat as current UI specification. |
| `SRC-0008`–`SRC-0015` | Historical technology-stack research | `PD` + `SR`, `historical` | Earlier architecture choices and trade-offs. | Technology choices may be stale or superseded. |
| `SRC-0025`, `SRC-0026`, `SRC-0029`, `SRC-0036` | Sensor research corpus | `SR` + `PD`, `historical` | Sensor principles, trade-offs, calibration/maintenance implications, early hardware rationale. | Large AI/research compilation; preserve claims with source status and avoid treating its recommendations as current build commitments. |
| `SRC-0274`, `SRC-0285`, `SRC-0286`, `SRC-0300`, `SRC-0301`, `SRC-0309`, `SRC-0314`, `SRC-0315` | Current project regional/microcosm research | `SR` + `AS`, mixed | Agricultural problem landscape, Kongu/Namakkal/Punjab analysis, microcosm comparisons. | Some material is synthesis and needs source-specific attribution. |
| `SRC-0357` | Farmer-problem research report | `SR` + `RH` + `PD`, `current_working` | Current target-segment hypothesis, decision journeys, workaround/trust model, field protocol, safety boundaries. | Explicitly desk research plus field design; no first-party EcoFarm farmer validation completed. |
| `SRC-0351`, `SRC-0352`, `SRC-0343`, `SRC-0383` | Decision design artifacts | `PD` + `AS`, `current_working` | Candidate decisions, tie-break rules, operationalization, analytical scoring. | Scores are analytical judgments, not survey facts. |
| `SRC-0354`, `SRC-0355`, `SRC-0340`, `SRC-0341` | Ecosystem, alternatives, and feasibility work | `SR` + `PD`, `current_working` | Alternatives map, local ecosystem, source feasibility, delivery constraints. | No partnership or automated-source approval can be inferred unless separately documented. |
| `SRC-0342`, `SRC-0345`–`SRC-0347`, `SRC-0360`–`SRC-0364`, `SRC-0372`–`SRC-0376`, `SRC-0381` | Field methodology and launch kit | `PD`, `current_working` | Consent, recruitment, data-quality, household authority, event-follow-up, and governance design. | Method artifacts do not prove fieldwork happened. |
| `SRC-0348`, `SRC-0365`–`SRC-0371`, `SRC-0377`–`SRC-0380`, `SRC-0386`, `SRC-0388`–`SRC-0390` | P0 data, source, safety, and test evidence | `DO` + `OP` + `DA`, `operational_test_result` / `current_working` | Source hierarchy, provenance, test outcomes, fail-closed design, referral constraints. | P0 tests are narrow and source-specific; do not generalize them to all providers. |
| `SRC-0370` | P0 operational test-results memo | `DO` + `DA` + `OP`, `operational_test_result` | Strongest current direct test record: automated TNAU weather/advisory path failed locality and reuse-rights checks for P0. | Does not prove other weather paths are unusable; it blocks only the tested path under stated rules. |
| `SRC-0382` | Market-research conversation export | Mixed `FI`, `HV`, `AS`, and research conversation | Large founder/analyst research history; strategic evolution and market context. | Must be parsed by message/source status; not every assistant statement is a founder decision or verified fact. |
| `SRC-0127`–`SRC-0133` | Historical and agent conversation exports | Mixed `FI`, `HV`, `PD`, `AS` | Turn-by-turn intellectual history and rationale behind versions. | Extract founder/user statements separately from assistant-generated analysis. |

## Citation convention for the Master Knowledge Base

Use source IDs in the form `[SRC-0357]` for internal traceability. When a source includes an external primary citation, cite the primary source in the section’s reference list as well. In every case, retain the source-status and temporal-status labels near material claims.
