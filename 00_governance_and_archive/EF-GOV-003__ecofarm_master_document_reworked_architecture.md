# EcoFarm Master Document — Reworked Architecture

## Purpose

The EcoFarm Master Document will be a **hyper-detailed, non-final knowledge base**, not primarily an investor document, pitch document, or final strategy document.

Its purpose is to preserve enough context for the founder or future collaborators to remake decisions later:

> What was EcoFarm trying to achieve? Why did each idea exist? How was each feature intended to work? What mental model supported it? What evidence existed? What alternatives were considered? What changed? What remains unresolved?

The document will preserve the full vision without presenting every historical idea as current, validated, or approved.

## Weighting of content

| High-weight content | Secondary content |
|---|---|
| Founder intuition and original vision | Investor presentation structure |
| Conceptual working of each major feature | Fundraising readiness |
| Mental models behind EcoFarm | Polished pitch language |
| Unique research data and source-specific findings | Premature market-size conclusions |
| Historical evolution and changed assumptions | Final-sounding positioning |
| Technical reasoning and information flows | Detailed screen-by-screen UI specifications |
| Safety, trust, uncertainty, and failure behaviour | Forced strategic conclusions |
| Alternatives, contradictions, and unresolved questions | Generic summaries |

## Main architecture

### Part 0 — How to read the knowledge base

Explain the deliberately non-final posture, source identifiers, evidence labels, chronology, contradiction handling, and the difference between fact, observation, intuition, hypothesis, interpretation, decision, and open question.

### Part I — EcoFarm’s mental universe

Preserve the original motivation, founder intuition, view of agricultural problems, assumptions about farmers and households, trust and adoption beliefs, the relationship between data and human judgement, and the distinction between EcoFarm as a product, system, ecosystem, and long-term vision.

This section preserves the **way of seeing the problem**, not merely a mission statement.

### Part II — Complete historical evolution

Reconstruct EcoFarm-1, EcoFarm-2, EcoFarm-1-2, EcoFarm-1-3, EcoFarm 1.3, the market-research conversation, and the Research Agent 1 and 2 work chronologically.

For each stage, record what EcoFarm was believed to be, which users and problems were prioritised, what features were proposed, why they were considered necessary, what technical and market assumptions existed, and what later work changed or challenged.

### Part III — Consolidated research knowledge base

Group unique research by subject instead of scattering it across reports.

Domains will include farmer decision reality; Namakkal, Kongu, Punjab, and crop context; markets and value chains; weather and climate; soil and water; existing alternatives; behaviour and adoption; institutional ecosystems; technical feasibility; safety and ethics; and field-validation methods.

Each domain will contain both a readable synthesis and a traceable preservation record. Research will remain attached to its source, date, geography, method, limitations, and status.

### Part IV — EcoFarm’s conceptual system models

Describe the interacting models behind EcoFarm:

1. Farmer context and identity.
2. Crop and production.
3. Risk and uncertainty.
4. Decision support.
5. Localisation.
6. Evidence and provenance.
7. Human advice and referral.
8. Outcome learning.
9. Trust and explainability.
10. Safety and escalation.
11. Ecosystem and institutional relationships.

For each model, explain purpose, assumptions, inputs, outputs, dependencies, historical variants, interactions, and unresolved questions.

### Part V — Feature and capability dossiers

This will be the heart of the document. Every major current, historical, deferred, rejected, speculative, or not-yet-prioritised feature will receive a conceptual dossier.

Likely dossiers include crop recommendation, crop comparison, crop-risk assessment, weather-linked advisories, market observations, soil and water context, crop calendars, input planning, pest and disease support, activity and outcome logging, explainable recommendation packets, alternative comparisons, expert referral, FPO workflows, sensors, AI interpretation, provenance, consent, offline use, feedback loops, notifications, farm histories, buyer and market features, finance or insurance concepts, community features, and the long-term ecosystem vision.

Every dossier will answer:

| Question | Required preservation |
|---|---|
| What is it? | Names, synonyms, versions, and source locations |
| What problem does it solve? | Real-world situation, pain, risk, or inefficiency |
| Why was it imagined? | Intuition, observation, analogy, or strategic reasoning |
| How should it work? | Inputs → processing → reasoning → output → action → feedback |
| What is its mental model? | Conceptual metaphor or system logic |
| What data is needed? | Required, optional, local, external, human, and freshness requirements |
| How does it decide? | Ranking, weighting, filtering, warnings, comparisons, or deferral |
| How does it build trust? | Reasons, trade-offs, uncertainty, source visibility, limitations |
| What happens when it fails? | Missing, stale, conflicting, unsafe, or unavailable data behaviour |
| Who participates? | Farmer, household, field worker, agronomist, FPO, institution, system |
| What does it depend on? | Technical, behavioural, operational, and institutional prerequisites |
| What alternatives existed? | Product and non-product alternatives |
| What evidence exists? | Research, observation, test results, counter-evidence, gaps |
| How has it evolved? | Revisions, supersession, narrowing, and current interpretation |
| What remains open? | Questions needed for future decisions |

### Part VI — Technical conceptual archive

Preserve historical and current architecture, modules, data entities, information flows, AI and rules-based logic, sensors, APIs, weather sources, provenance, auditability, observability, privacy, consent, offline assumptions, failure handling, and abandoned technical paths.

Clearly distinguish what was tested, what was theoretically possible, what failed operationally, and what remains unknown.

### Part VII — Evidence and knowledge registers

Include integrated registers for research findings; farmer problems and decisions; market and crop data; alternatives and institutions; data sources and technical tests; safety risks and referral rules; field-validation events; assumptions; open questions; counterarguments; and terminology.

### Part VIII — Decision history

Record decisions as historical events, not automatically permanent truths. Each record will contain date, context, alternatives, reasoning, evidence, assumptions, acknowledged risks, consequences, later revisions, and the evidence that would justify reopening the decision.

### Part IX — Current working map

Provide a modest navigation layer identifying active explorations, current validation candidates, P0 candidates, tested technical paths, deferred ideas, blockers, and founder decisions still required. This section will not erase or override the archive.

### Part X — Commercial and investor archive

Preserve commercial research, business-model hypotheses, market sizing, pitch material, credibility requirements, and investor-readiness work as a secondary historical and research archive. It will not determine the overall structure of the knowledge base.

## Source-treatment rules

1. **Preserve before synthesising.** Old, speculative, repetitive, and superseded material may be labelled but will not be discarded if it contains useful reasoning.
2. **Separate source from interpretation.** Clearly distinguish what a source says, what is inferred, what the synthesis believes, and what remains uncertain.
3. **Do not force contradictions into one answer.** Preserve conflicting claims, chronology, and the evidence needed to resolve them.
4. **Do not convert plans into validation.** A handoff, checklist, field kit, or test plan is not proof that the corresponding work occurred.
5. **Preserve intuition as intuition.** Founder beliefs will not be rewritten as externally validated facts.
6. **Preserve abandoned paths.** Rejected APIs, sensors, business models, and features remain part of the reasoning history.
7. **Keep claims attached to evidence.** Retain date, geography, method, source, limitations, and test conditions.
8. **Distinguish missing evidence from negative evidence.** Lack of proof does not automatically prove impossibility or invalidity.
9. **Treat uncertainty as knowledge.** Open questions and ambiguity are first-class records.
10. **Use reversible status labels.** Concepts may be labelled vision concept, conceptual candidate, research hypothesis, technical hypothesis, validated observation, operationally tested, current working candidate, deferred, superseded, rejected, or unresolved.

## What will be reduced

Investor-style executive summaries, pitch language, fundraising readiness, premature market-size conclusions, final-sounding positioning, and detailed UI implementation specifications will not dominate the document. They will remain where they contain unique information or historical reasoning.

## Final character

The document should feel like a combination of a preserved founder notebook, product-concept encyclopedia, research archive, technical systems explanation, decision-history ledger, field-validation memory, and map of unresolved questions.

## Recommended defaults for approval

| Decision | Recommended default |
|---|---|
| Purpose | Preserve the complete EcoFarm knowledge universe for future re-evaluation |
| Posture | Non-final, exploratory, evidence-aware, and reversible |
| Main emphasis | Conceptual working, feature mechanics, mental models, intuition, research, technical reasoning, and open questions |
| Commercial material | Preserve it, but keep it secondary |
| Feature coverage | Include current, historical, deferred, rejected, and speculative major features |
| UI/UX coverage | Preserve workflow and design logic; exclude detailed implementation specifications from the main body |
| Conclusions | Do not force conclusions where the archive does not justify them |
| Output | One editable Markdown document with integrated appendices and traceability registers |

The proposed confirmation is:

> Proceed with a hyper-detailed, non-final EcoFarm knowledge base that preserves the conceptual working, mental models, intentions, intuition, research data, technical reasoning, historical alternatives, and unresolved questions, while keeping commercial and investor material secondary.
