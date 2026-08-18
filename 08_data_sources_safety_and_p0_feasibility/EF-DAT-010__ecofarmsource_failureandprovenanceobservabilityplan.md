# EcoFarm Source-Failure and Provenance Observability Plan

**Scope.** This plan covers the single sowing/early-establishment decision packet. Observability is a safety control: if EcoFarm cannot tell whether evidence is current, complete, authorized, and correctly transformed, it must not produce a decision prompt.

## Required event logs

| Log | Required fields | Retention / access |
|---|---|---|
| Source request | `request_id`, source ID, endpoint/page, request time, auth mode identifier, status, latency, response size/hash, error class. | Operational log; exclude secrets; restricted technical access. |
| Source response | Source version/ETag or bulletin ID, issued time, valid period, location, raw snapshot reference, parsed fields, parser version. | Versioned and immutable for audit; remove farmer linkage on deletion where possible. |
| Freshness evaluation | Retrieved time, source time, expected update interval, age, freshness state, threshold used, suppression decision. | Linked to decision and dashboard. |
| Semantic validation | Commodity/variety/grade/unit/market or weather location/period match, validation result, reviewer. | Retain with relevant decision record. |
| Transformation | Rule/version, input fields, output state, assumptions, language simplification, reviewer or automated status. | Immutable with output. |
| Decision output | Decision ID, input schema version, source IDs, output text/state, confidence label, missing-data state, referral trigger. | Farmer-accessible summary plus restricted audit details. |
| Farmer response | Accepted/rejected/changed/ignored, optional reason, timestamp. | Separate evaluation consent; deletable. |
| Escalation | Trigger, wording shown, public referral link, contact information verification date, farmer-selected action, reported response. | Restricted safety log; never infer institution response. |

## Source states

| State | Definition | User-facing behavior |
|---|---|---|
| `current_valid` | Required fields present; source time/valid period within threshold; geography and terms pass. | May support a source-labelled constrained output. |
| `stale` | Record exists but exceeds threshold or validity period. | Do not use for current action; show historical/source link only if useful. |
| `empty` | Successful request but no record for requested location/time/commodity. | State that no current record was found; ask a narrower question or refer. |
| `malformed` | Response cannot be parsed or required fields absent. | Suppress and log parser/source error. |
| `rate_limited` | Source refuses request due to quota/limit. | Suppress; do not retry aggressively; show unavailable state. |
| `unauthorized` | Credentials, permissions, or terms do not allow access/use. | Treat as permission-dependent/manual-reference; no automated display. |
| `geography_mismatch` | Source scope does not match target decision. | Do not silently substitute district/state data; explain limitation. |
| `semantic_mismatch` | Market/crop/variety/unit/grade or crop-stage meaning does not match. | Exclude from packet. |
| `conflict` | Two applicable sources disagree materially. | Preserve both, downgrade, and refer. |
| `transformation_unverified` | Output rule or translation has not been reviewed. | Show raw reference or manual-only state; no automated prompt. |

## Monitoring and review

A technical review record should show, by source and day: request success rate, empty-response rate, median and maximum latency, freshness age distribution, parser failures, authorization failures, semantic-validation failures, conflict count, suppression count, manual overrides, and farmer-facing referral count. A dashboard may be simple in the first pilot, but the review must be reproducible from logs.

Any source with repeated stale, empty, malformed, or geography-mismatch states must be manually reviewed before reactivation. Any change to source schema, endpoint, bulletin layout, attribution, or terms opens a new approval test. A source is not considered healthy because requests return HTTP 200; content and semantics must pass validation.

## Fail-closed UI states

The UI must distinguish “no current data,” “data found but not comparable,” “source temporarily unavailable,” “source conflict,” and “outside tested scope.” It must never display an old value in a current-looking card, convert missing price into zero, fill a missing forecast with a secondary source without labelling it, or display a transformed recommendation without its source and rule version.

## Manual intervention

A human reviewer can inspect a suppressed packet, confirm a source link, correct an input, or refer the farmer. The reviewer cannot override missing provenance by personal confidence. Every override records the reviewer, evidence, reason, and whether the output remained informational or became a constrained recommendation. High-risk agronomic, pesticide, disease, emergency, and contradictory cases remain referral-only.

## Incident thresholds

Pause the affected workflow if: a stale or wrong-geography value reaches a farmer-facing recommendation; a market record is displayed with incorrect variety/unit; an unauthorized source is redistributed; a source conflict is hidden; a farmer reports harm or material misunderstanding; or a parser/schema change cannot be reconciled. Resume only after root cause, affected records, user notice if needed, corrected tests, and reviewer sign-off are recorded.

## References

[1]: https://api.imd.gov.in/ "IMD API Management Platform"
[2]: https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi "data.gov.in mandi-price resource"
[3]: https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php "IMD Agromet Advisory Services"
[4]: https://namakkal.nic.in/departments/agriculture/ "Namakkal District Agriculture Department"
