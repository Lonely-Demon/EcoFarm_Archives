# EcoFarm Content-Based Version Comparison

> This comparison uses normalized full-text similarity, title/path provenance, extracted headings, and manual disposition notes. It is evidence for semantic-family review, not a claim that a similarity percentage alone proves supersession.

## Onboarding and core-vision sequence

| Source ID | Artifact | Characters | Selected headings / content cues |
|---|---|---:|---|
| `SRC-0007` | `EcoFarm-1/project_onboarding_document.md` | 2,753 | Project Onboarding Document: Smart Farming Ecosystem; Table of Contents; **The Big Picture: Vision for the Smart Farming Ecosystem**; **Focusing In: Vision for the Mobile Application** |
| `SRC-0033` | `EcoFarm-1-3/project_onboarding_document.md` | 2,753 | Project Onboarding Document: Smart Farming Ecosystem; Table of Contents; **The Big Picture: Vision for the Smart Farming Ecosystem**; **Focusing In: Vision for the Mobile Application** |
| `SRC-0034` | `EcoFarm-1-3/project_onboarding_document.pdf` | 143,586 | Executive Summary; The Big Picture: Vision for the Smart Farming Ecosystem; The Agri-Tech Company & Its Mission; The Problem: Challenges in Modern Farming |
| `SRC-0035` | `EcoFarm-1-3/project_onboarding_document_old.txt` | 139,242 | Executive Summary; The Big Picture: Vision for the Smart Farming Ecosystem; The Agri-Tech Company & Its Mission; The Problem: Challenges in Modern Farming |
| `SRC-0039` | `EcoFarm-1_3/project_onboarding_document.md` | 297,167 | The Big Picture: Vision for the EcoFarm; The Agri-Tech Company & Its Mission; The Problem: Challenges in Modern Farming; Resource Scarcity and Inefficient Resource Management |
| `SRC-0040` | `EcoFarm-1_3/project_onboarding_document_final.md` | 17,803 | Project Onboarding Document: EcoFarm; 1. Introduction; 1.1. Purpose of the Document; 1.2. Scope of the Project |
| `SRC-0334` | `shared_files/project_onboarding_document.pdf` | 143,586 | Executive Summary; The Big Picture: Vision for the Smart Farming Ecosystem; The Agri-Tech Company & Its Mission; The Problem: Challenges in Modern Farming |

### Pairwise normalized text similarity

| Source A | Source B | Similarity | Interpretation cue |
|---|---|---:|---|
| `SRC-0007` | `SRC-0033` | 1.000 | Likely duplicate/format conversion |
| `SRC-0007` | `SRC-0034` | 0.084 | Distinct or complementary content |
| `SRC-0007` | `SRC-0035` | 0.084 | Distinct or complementary content |
| `SRC-0007` | `SRC-0039` | 0.063 | Distinct or complementary content |
| `SRC-0007` | `SRC-0040` | 0.061 | Distinct or complementary content |
| `SRC-0007` | `SRC-0334` | 0.084 | Distinct or complementary content |
| `SRC-0033` | `SRC-0034` | 0.084 | Distinct or complementary content |
| `SRC-0033` | `SRC-0035` | 0.084 | Distinct or complementary content |
| `SRC-0033` | `SRC-0039` | 0.063 | Distinct or complementary content |
| `SRC-0033` | `SRC-0040` | 0.061 | Distinct or complementary content |
| `SRC-0033` | `SRC-0334` | 0.084 | Distinct or complementary content |
| `SRC-0034` | `SRC-0035` | 0.989 | Likely duplicate/format conversion |
| `SRC-0034` | `SRC-0039` | 0.516 | Strong thematic overlap; inspect additions/revisions |
| `SRC-0034` | `SRC-0040` | 0.307 | Distinct or complementary content |
| `SRC-0034` | `SRC-0334` | 1.000 | Likely duplicate/format conversion |
| `SRC-0035` | `SRC-0039` | 0.522 | Strong thematic overlap; inspect additions/revisions |
| `SRC-0035` | `SRC-0040` | 0.309 | Distinct or complementary content |
| `SRC-0035` | `SRC-0334` | 0.989 | Likely duplicate/format conversion |
| `SRC-0039` | `SRC-0040` | 0.575 | Strong thematic overlap; inspect additions/revisions |
| `SRC-0039` | `SRC-0334` | 0.516 | Strong thematic overlap; inspect additions/revisions |
| `SRC-0040` | `SRC-0334` | 0.307 | Distinct or complementary content |

## Early product requirements and workflow archive

| Source ID | Artifact | Characters | Selected headings / content cues |
|---|---|---:|---|
| `SRC-0005` | `EcoFarm-1/mvp_screens_flows.md` | 5,382 | MVP User Flows & Key Screens Outline; Core MVP Features (Reference); **Accurate Weather Data:** Display current and forecasted weather.; **Farm/Field Mapping (Basic):** Allow users to define farm boundaries and basic field sectors (manual i |
| `SRC-0006` | `EcoFarm-1/prd_draft.md` | 30,156 | Product Requirements Document (PRD): Smart Farming Ecosystem Mobile App; 1. Introduction; 1.1. Overview; 1.2. Goals & Objectives |
| `SRC-0016` | `EcoFarm-1/ui_ux_guidelines.md` | 5,138 | Actionable UI/UX Guidelines (Based on content.pdf Mockups); 1. Overall Style & Philosophy; 2. Color Palette; 3. Typography |
| `SRC-0017` | `EcoFarm-1/ui_ux_guidelines_refined.md` | 4,793 | Actionable UI/UX Guidelines (Focused on GrowWise Style + Video Insights); 1. Overall Style & Philosophy; 2. Color Palette; 3. Typography |
| `SRC-0018` | `EcoFarm-1/ui_ux_synthesis.md` | 4,423 | UI/UX Synthesis from Mockup Review (content.pdf); Overall Aesthetic & Themes; Key UI/UX Elements; **Color Palette:** |
| `SRC-0019` | `EcoFarm-1/ui_ux_synthesis_growwise.md` | 4,018 | UI/UX Synthesis (Focused on GrowWise Style - Pages 3-9 of content.pdf); Overall Aesthetic & Themes (GrowWise Focus); Key UI/UX Elements (GrowWise Focus); **Color Palette:** |
| `SRC-0023` | `EcoFarm-1/wireframes_part1.md` | 2,627 | Low-Fidelity Wireframes (MVP - Part 1); 1. Onboarding & Authentication; 2. Main Dashboard / Home |
| `SRC-0024` | `EcoFarm-1/wireframes_part2.md` | 7,860 | Low-Fidelity Wireframes (MVP - Part 2); 3. Weather Details; 4. Farm & Field Management (MVP Basic); 5. AI Planting Recommendations |

### Pairwise normalized text similarity

| Source A | Source B | Similarity | Interpretation cue |
|---|---|---:|---|
| `SRC-0005` | `SRC-0006` | 0.131 | Distinct or complementary content |
| `SRC-0005` | `SRC-0016` | 0.082 | Distinct or complementary content |
| `SRC-0005` | `SRC-0017` | 0.078 | Distinct or complementary content |
| `SRC-0005` | `SRC-0018` | 0.086 | Distinct or complementary content |
| `SRC-0005` | `SRC-0019` | 0.082 | Distinct or complementary content |
| `SRC-0005` | `SRC-0023` | 0.189 | Distinct or complementary content |
| `SRC-0005` | `SRC-0024` | 0.299 | Distinct or complementary content |
| `SRC-0006` | `SRC-0016` | 0.158 | Distinct or complementary content |
| `SRC-0006` | `SRC-0017` | 0.155 | Distinct or complementary content |
| `SRC-0006` | `SRC-0018` | 0.128 | Distinct or complementary content |
| `SRC-0006` | `SRC-0019` | 0.119 | Distinct or complementary content |
| `SRC-0006` | `SRC-0023` | 0.071 | Distinct or complementary content |
| `SRC-0006` | `SRC-0024` | 0.114 | Distinct or complementary content |
| `SRC-0016` | `SRC-0017` | 0.569 | Strong thematic overlap; inspect additions/revisions |
| `SRC-0016` | `SRC-0018` | 0.372 | Distinct or complementary content |
| `SRC-0016` | `SRC-0019` | 0.258 | Distinct or complementary content |
| `SRC-0016` | `SRC-0023` | 0.086 | Distinct or complementary content |
| `SRC-0016` | `SRC-0024` | 0.080 | Distinct or complementary content |
| `SRC-0017` | `SRC-0018` | 0.294 | Distinct or complementary content |
| `SRC-0017` | `SRC-0019` | 0.345 | Distinct or complementary content |
| `SRC-0017` | `SRC-0023` | 0.085 | Distinct or complementary content |
| `SRC-0017` | `SRC-0024` | 0.076 | Distinct or complementary content |
| `SRC-0018` | `SRC-0019` | 0.374 | Distinct or complementary content |
| `SRC-0018` | `SRC-0023` | 0.083 | Distinct or complementary content |
| `SRC-0018` | `SRC-0024` | 0.087 | Distinct or complementary content |
| `SRC-0019` | `SRC-0023` | 0.098 | Distinct or complementary content |
| `SRC-0019` | `SRC-0024` | 0.099 | Distinct or complementary content |
| `SRC-0023` | `SRC-0024` | 0.269 | Distinct or complementary content |

## Sensor and hardware research sequence

| Source ID | Artifact | Characters | Selected headings / content cues |
|---|---|---:|---|
| `SRC-0025` | `EcoFarm-1-2/FireShotCapture004-EcoFarm_Module-SensorResearch-Grok-[grok.com].pdf` | 447,969 | **1. Soil Moisture Sensors (FDR/Capacitance)**; **2. Soil pH Sensors (Antimony Electrode)**; **3. NPK Sensors (EC-Based)**; **4. Temperature/Humidity/Barometric Sensors** |
| `SRC-0026` | `EcoFarm-1-2/FireShotCapture008-EcoFarm_Module-SensorResearch-Grok-[grok.com].pdf` | 444,255 | **1. Soil Moisture Sensors (FDR/Capacitance)**; **2. Soil pH Sensors (Antimony Electrode)**; **3. NPK Sensors (EC-Based)**; **4. Temperature/Humidity/Barometric Sensors** |
| `SRC-0029` | `EcoFarm-1-2/sensor_research_grok_content_new.txt` | 389,502 | **3. NPK Sensors (EC-Based)**; **Availability in India**: All listed sensors are sold on [Robu.in](https://robu.in),; **Calibration**: Most soil sensors require **minimal initial calibration** (e.g., dry/wet; **Waterproofing**: Use epoxy re |
| `SRC-0036` | `EcoFarm-1-3/sensor_research_grok_content.txt` | 389,502 | **3. NPK Sensors (EC-Based)**; **Availability in India**: All listed sensors are sold on [Robu.in](https://robu.in),; **Calibration**: Most soil sensors require **minimal initial calibration** (e.g., dry/wet; **Waterproofing**: Use epoxy re |

### Pairwise normalized text similarity

| Source A | Source B | Similarity | Interpretation cue |
|---|---|---:|---|
| `SRC-0025` | `SRC-0026` | 0.999 | Likely duplicate/format conversion |
| `SRC-0025` | `SRC-0029` | 0.992 | Likely duplicate/format conversion |
| `SRC-0025` | `SRC-0036` | 0.992 | Likely duplicate/format conversion |
| `SRC-0026` | `SRC-0029` | 0.991 | Likely duplicate/format conversion |
| `SRC-0026` | `SRC-0036` | 0.991 | Likely duplicate/format conversion |
| `SRC-0029` | `SRC-0036` | 1.000 | Likely duplicate/format conversion |

## Field interview and learning instruments

| Source ID | Artifact | Characters | Selected headings / content cues |
|---|---|---:|---|
| `SRC-0353` | `uploads/EcoFarmDiscoveryForm—20–30Minutes.md` | 3,923 | EcoFarm Discovery Form — 20–30 Minutes; 1. Interview metadata; 2. Neutral opening; 3. Recent decision reconstruction |
| `SRC-0358` | `uploads/EcoFarmFieldInterviewGuide.md` | 6,709 | EcoFarm Field Interview Guide; Interview protocol; A. Farm and household context; Tell me about the last crop you completed. What was the crop, when was it sown, how much land was involved, and what kind of water was available? |
| `SRC-0359` | `uploads/EcoFarmFieldInterviewGuide—Revised.md` | 10,155 | EcoFarm Field Interview Guide — Revised; Interview opening and consent; A. Farm and recent crop-cycle context; Tell me about the most recent crop you completed or are currently managing. What was planted, when, on how much land, and with wh |
| `SRC-0364` | `uploads/EcoFarmHousehold-AuthorityFollow-Up.md` | 2,498 | EcoFarm Household-Authority Follow-Up; 1. Link to event; 2. Role verification; 3. Neutral verification questions |
| `SRC-0376` | `uploads/EcoFarmShortPost-EventFollow-Up.md` | 2,677 | EcoFarm Short Post-Event Follow-Up; 1. Event link and evidence state; 2. Actual action; What did you actually do after the earlier decision point? |

### Pairwise normalized text similarity

| Source A | Source B | Similarity | Interpretation cue |
|---|---|---:|---|
| `SRC-0353` | `SRC-0358` | 0.221 | Distinct or complementary content |
| `SRC-0353` | `SRC-0359` | 0.286 | Distinct or complementary content |
| `SRC-0353` | `SRC-0364` | 0.193 | Distinct or complementary content |
| `SRC-0353` | `SRC-0376` | 0.203 | Distinct or complementary content |
| `SRC-0358` | `SRC-0359` | 0.368 | Distinct or complementary content |
| `SRC-0358` | `SRC-0364` | 0.130 | Distinct or complementary content |
| `SRC-0358` | `SRC-0376` | 0.128 | Distinct or complementary content |
| `SRC-0359` | `SRC-0364` | 0.169 | Distinct or complementary content |
| `SRC-0359` | `SRC-0376` | 0.161 | Distinct or complementary content |
| `SRC-0364` | `SRC-0376` | 0.193 | Distinct or complementary content |

## Candidate decision and claim-ledger sequence

| Source ID | Artifact | Characters | Selected headings / content cues |
|---|---|---:|---|
| `SRC-0343` | `uploads/EcoFarmCandidateDecisionTie-BreakProtocol(1).md` | 7,821 | EcoFarm Candidate Decision Tie-Break Protocol; 1. Purpose; 2. Candidate definitions; 3. Evidence states and weights |
| `SRC-0344` | `uploads/EcoFarmCandidateDecisionTie-BreakProtocol.md` | 7,821 | EcoFarm Candidate Decision Tie-Break Protocol; 1. Purpose; 2. Candidate definitions; 3. Evidence states and weights |
| `SRC-0345` | `uploads/EcoFarmClaimLedger(1).md` | 7,317 | EcoFarm Claim Ledger |
| `SRC-0346` | `uploads/EcoFarmClaimLedger.md` | 8,714 | EcoFarm Claim Ledger |
| `SRC-0347` | `uploads/EcoFarmClaimLedger—RevisedField-ProgrammeVersion.md` | 12,609 | EcoFarm Claim Ledger — Revised Field-Programme Version; Event-state vocabulary for all future claims |
| `SRC-0383` | `uploads/EcoFarmcandidatedecisionscoring—analyticaljudgments.md` | 2,209 | EcoFarm candidate decision scoring — analytical judgments |

### Pairwise normalized text similarity

| Source A | Source B | Similarity | Interpretation cue |
|---|---|---:|---|
| `SRC-0343` | `SRC-0344` | 1.000 | Likely duplicate/format conversion |
| `SRC-0343` | `SRC-0345` | 0.088 | Distinct or complementary content |
| `SRC-0343` | `SRC-0346` | 0.116 | Distinct or complementary content |
| `SRC-0343` | `SRC-0347` | 0.182 | Distinct or complementary content |
| `SRC-0343` | `SRC-0383` | 0.131 | Distinct or complementary content |
| `SRC-0344` | `SRC-0345` | 0.088 | Distinct or complementary content |
| `SRC-0344` | `SRC-0346` | 0.116 | Distinct or complementary content |
| `SRC-0344` | `SRC-0347` | 0.182 | Distinct or complementary content |
| `SRC-0344` | `SRC-0383` | 0.131 | Distinct or complementary content |
| `SRC-0345` | `SRC-0346` | 0.166 | Distinct or complementary content |
| `SRC-0345` | `SRC-0347` | 0.157 | Distinct or complementary content |
| `SRC-0345` | `SRC-0383` | 0.089 | Distinct or complementary content |
| `SRC-0346` | `SRC-0347` | 0.682 | Strong thematic overlap; inspect additions/revisions |
| `SRC-0346` | `SRC-0383` | 0.112 | Distinct or complementary content |
| `SRC-0347` | `SRC-0383` | 0.103 | Distinct or complementary content |

## Data-source and ecosystem register sequence

| Source ID | Artifact | Characters | Selected headings / content cues |
|---|---|---:|---|
| `SRC-0348` | `uploads/EcoFarmData-SourceRegister.md` | 9,124 | EcoFarm Data-Source Register; Required operational tests before implementation |
| `SRC-0355` | `uploads/EcoFarmEcosystemRegister.md` | 10,394 | EcoFarm Ecosystem Register |
| `SRC-0365` | `uploads/EcoFarmP0Data-SourceRegister—OperationalRevision.md` | 5,771 | EcoFarm P0 Data-Source Register — Operational Revision; Institutional classification rule; References |
| `SRC-0367` | `uploads/EcoFarmP0EcosystemRegister—OperationalRevision.md` | 6,900 | EcoFarm P0 Ecosystem Register — Operational Revision; Classification rule |
| `SRC-0370` | `uploads/EcoFarmP0OperationalTestResultsMemo.md` | 14,230 | EcoFarm P0 Operational Test Results Memo; 1. Test fixture and evidence boundary; 2. Pass/fail table for tested sources and controls; 3. Required operational result for the selected weather path |
| `SRC-0371` | `uploads/EcoFarmP0SourceOperational-TestPlan.md` | 9,917 | EcoFarm P0 Source Operational-Test Plan; P0 decision packet scope; Operational categories; Test cases and pass criteria |
| `SRC-0377` | `uploads/EcoFarmSource-FailureandProvenanceObservabilityPlan.md` | 5,892 | EcoFarm Source-Failure and Provenance Observability Plan; Required event logs; Source states; Monitoring and review |
| `SRC-0378` | `uploads/EcoFarmSourceRegister.md` | 7,947 | EcoFarm Source Register |
| `SRC-0380` | `uploads/EcoFarmWeatherandAdvisorySourceHierarchy.md` | 6,159 | EcoFarm Weather and Advisory Source Hierarchy; Precedence; Freshness policy; Conflict policy |

### Pairwise normalized text similarity

| Source A | Source B | Similarity | Interpretation cue |
|---|---|---:|---|
| `SRC-0348` | `SRC-0355` | 0.212 | Distinct or complementary content |
| `SRC-0348` | `SRC-0365` | 0.237 | Distinct or complementary content |
| `SRC-0348` | `SRC-0367` | 0.227 | Distinct or complementary content |
| `SRC-0348` | `SRC-0370` | 0.181 | Distinct or complementary content |
| `SRC-0348` | `SRC-0371` | 0.268 | Distinct or complementary content |
| `SRC-0348` | `SRC-0377` | 0.148 | Distinct or complementary content |
| `SRC-0348` | `SRC-0378` | 0.117 | Distinct or complementary content |
| `SRC-0348` | `SRC-0380` | 0.160 | Distinct or complementary content |
| `SRC-0355` | `SRC-0365` | 0.199 | Distinct or complementary content |
| `SRC-0355` | `SRC-0367` | 0.284 | Distinct or complementary content |
| `SRC-0355` | `SRC-0370` | 0.148 | Distinct or complementary content |
| `SRC-0355` | `SRC-0371` | 0.162 | Distinct or complementary content |
| `SRC-0355` | `SRC-0377` | 0.106 | Distinct or complementary content |
| `SRC-0355` | `SRC-0378` | 0.138 | Distinct or complementary content |
| `SRC-0355` | `SRC-0380` | 0.128 | Distinct or complementary content |
| `SRC-0365` | `SRC-0367` | 0.322 | Distinct or complementary content |
| `SRC-0365` | `SRC-0370` | 0.229 | Distinct or complementary content |
| `SRC-0365` | `SRC-0371` | 0.320 | Distinct or complementary content |
| `SRC-0365` | `SRC-0377` | 0.186 | Distinct or complementary content |
| `SRC-0365` | `SRC-0378` | 0.110 | Distinct or complementary content |
| `SRC-0365` | `SRC-0380` | 0.203 | Distinct or complementary content |
| `SRC-0367` | `SRC-0370` | 0.183 | Distinct or complementary content |
| `SRC-0367` | `SRC-0371` | 0.205 | Distinct or complementary content |
| `SRC-0367` | `SRC-0377` | 0.141 | Distinct or complementary content |
| `SRC-0367` | `SRC-0378` | 0.118 | Distinct or complementary content |
| `SRC-0367` | `SRC-0380` | 0.161 | Distinct or complementary content |
| `SRC-0370` | `SRC-0371` | 0.251 | Distinct or complementary content |
| `SRC-0370` | `SRC-0377` | 0.223 | Distinct or complementary content |
| `SRC-0370` | `SRC-0378` | 0.110 | Distinct or complementary content |
| `SRC-0370` | `SRC-0380` | 0.213 | Distinct or complementary content |
| `SRC-0371` | `SRC-0377` | 0.235 | Distinct or complementary content |
| `SRC-0371` | `SRC-0378` | 0.095 | Distinct or complementary content |
| `SRC-0371` | `SRC-0380` | 0.236 | Distinct or complementary content |
| `SRC-0377` | `SRC-0378` | 0.083 | Distinct or complementary content |
| `SRC-0377` | `SRC-0380` | 0.246 | Distinct or complementary content |
| `SRC-0378` | `SRC-0380` | 0.106 | Distinct or complementary content |

## Explicit manual dispositions

| Family | Content-based disposition |
|---|---|
| Onboarding and core vision | `SRC-0007` and `SRC-0033` are duplicate short onboarding copies; `SRC-0034`/`SRC-0334` are format-rendered versions; `SRC-0035` is an older long text; `SRC-0039` is the richest extended historical onboarding record; `SRC-0040` is a concise later/final-labelled orientation record. Preserve all. Use `SRC-0039` for detailed historical mechanics and `SRC-0040` for concise late historical framing; current P0 evidence still governs present scope. |
| Early PRD and workflow archive | The PRD, screen flows, wireframes, and UI syntheses cover different layers of the same early product model. They are complementary rather than serially superseding. The Master Knowledge Base preserves their conceptual workflow logic while excluding implementation-level UI prescriptions. |
| Sensor and hardware research | The repeated sensor corpora have heavy overlap and format duplication, but their sensor trade-off content should remain as historical engineering rationale. None is a current hardware approval or replaces current field feasibility requirements. |
| Field interview and learning instruments | The revised interview guide (`SRC-0359`) supersedes the earlier guide (`SRC-0358`) as the latest proposed interview instrument; discovery/event/follow-up forms are complementary instruments, not replacements. None proves field use absent participant/event evidence. |
| Candidate decision and claim ledgers | Exact duplicate filenames are aliases; the revised field-programme claim ledger (`SRC-0347`) supersedes prior claim-ledger wording for the proposed field programme. Candidate-decision scoring is a separate analytical rationale, not a replacement for field evidence. |
| Data-source and ecosystem registers | P0 operational revisions (`SRC-0365`, `SRC-0367`) are later control documents relative to broad registers (`SRC-0348`, `SRC-0355`) for the named P0. The direct P0 test memo (`SRC-0370`) governs the tested TNAU path only; the source hierarchy (`SRC-0380`) and observability plan (`SRC-0377`) complement it as operating policy. |

## Residual unresolved relationships

The archive deliberately retains broad historical platform concepts alongside narrow P0 constraints. This is not an unresolved clerical error: the concepts serve different temporal roles. A future product decision should use the source map, feature dossiers, and current direct test evidence to determine whether a historical capability is still relevant, rather than treating an older feature list as automatically superseded or permanently rejected.