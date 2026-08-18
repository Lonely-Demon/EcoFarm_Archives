# EcoFarm P0 Decision-Packet Data Dictionary and Consent Map

**Decision event.** A farmer is considering a defined sowing or early-establishment action for a named crop, location, and intended time window. The packet provides a constrained comparison or caution/referral state. It does not provide guaranteed profitability, buyer assurance, autonomous agronomy, or automated actuation.

## Field dictionary

| Field | Purpose | Source | Required? | Sensitivity | Validation | Retention / access / deletion | Consent wording and failure behavior |
|---|---|---|---|---|---|---|---|
| `decision_id` | Link all inputs and output to one decision event. | System-generated. | Required. | Low. | UUID and creation timestamp. | Retain with decision record for pilot evaluation; user can request deletion of associated record. | Explain: “This ID helps us keep your decision record together.” |
| `created_at` / `updated_at` | Establish freshness and audit trail. | System. | Required. | Low. | Server time; do not accept only client time. | Retain with record; deletion follows decision record. | No separate consent beyond decision-record notice. |
| `language_preference` | Render questions and explanations. | Farmer. | Required for delivery. | Low. | Select from supported languages; allow change. | Retain while active; delete with profile or decision record. | “We use your language choice to show explanations.” If absent, use neutral language-selection prompt; do not infer. |
| `village_or_block` | Select geographically relevant weather/advisory and market context. | Farmer; optional geolocation only with separate consent. | Required. | Moderate location sensitivity. | Controlled list plus free-text confirmation; do not claim plot precision. | Retain only for the decision’s stated purpose; deletion route in settings/support. | “We use your selected area to find relevant public information. We do not treat it as exact plot location.” If absent, no localized output. |
| `crop` | Select crop guidance and interpret sowing event. | Farmer. | Required. | Low. | Controlled crop list; confirm spelling/local name. | Retain with decision record; deletable. | “We use the crop you select to show relevant reference guidance.” If unknown crop, manual reference/referral only. |
| `variety_or_seed_type` | Avoid mismatching crop guidance and market semantics. | Farmer. | Optional P0; required for market comparison when relevant. | Low. | Controlled list plus “unknown”; never silently map unknown to a variety. | Retain only if used; deletable. | “Optional: this helps avoid comparing different varieties.” If absent, exclude variety-specific output. |
| `intended_sowing_window` | Match weather validity and event timing. | Farmer. | Required. | Low. | Date/range validation; reject past or implausibly broad windows. | Retain with decision record; deletable. | “We use this time window to check whether current information applies.” If absent, no weather action prompt. |
| `crop_stage` | Distinguish sowing from early establishment. | Farmer. | Required; default not permitted. | Low. | Controlled stage list and confirmation. | Retain with decision record; deletable. | “The stage changes which information is relevant.” If uncertain, show education/referral only. |
| `land_area` | Explain scale and practical constraints; not for profit prediction. | Farmer. | Optional. | Moderate. | Numeric range and unit; allow unknown. | Retain only if used; deletable. | “Optional; do not enter it unless you want it used for this comparison.” If absent, do not infer cost/scale. |
| `water_availability` | Capture a named constraint for option comparison. | Farmer. | Required for crop-option comparison; not required for raw alert. | Moderate. | Controlled categories: reliable, seasonal, uncertain, rainfed, unknown; confirm. | Retain with decision record; deletable. | “This is used only to compare constraints for this decision.” If absent, suppress comparison and ask/referral. |
| `soil_test_available` | Determine whether a farmer-held report can be used. | Farmer. | Optional; required only if soil evidence is used. | Moderate. | Yes/no/unknown plus test date if yes. | Retain only if used; report values separate and consented. | “We will not access a soil record unless you choose to share it.” If no, do not substitute district averages silently. |
| `soil_test_date` | Detect stale soil information. | Farmer-held report. | Required when report is used. | Moderate. | Valid date and age display. | Retain with soil evidence; deletable. | Separate consent to store report-derived fields. If absent, soil evidence excluded. |
| `soil_test_values` | Use farmer-provided soil evidence as a constraint. | Farmer-held report or permissioned source. | Optional and permission-dependent. | High agricultural/possibly location sensitivity. | Field/unit/schema validation; preserve original report reference. | Shortest practical retention; restricted access; deletion removes derived values and source copy. | “I allow EcoFarm to use these soil-test fields for this decision.” If declined, no soil-based comparison. |
| `farmer_objective` | Explain trade-offs without assuming profit maximization. | Farmer. | Required for comparison. | Moderate. | Controlled choices such as water conservation, lower input burden, timing flexibility, food, or sale; allow multiple. | Retain with decision record; deletable. | “This tells us what matters to you; it is not a promise of income.” If absent, show informational options only. |
| `labour_or_input_constraint` | Capture operational feasibility. | Farmer. | Optional but required for constraint-aware comparison. | Moderate. | Controlled categories plus unknown. | Retain with decision record; deletable. | Same purpose notice; if absent, label comparison incomplete. |
| `market_context_requested` | Determine whether optional observed-price context is relevant. | Farmer. | Optional. | Low. | Yes/no. | Retain with decision record; deletable. | “Prices are observations only, not forecasts or buyer offers.” If no, omit market context. |
| `market`, `commodity`, `variety`, `grade`, `unit`, `observation_date` | Ensure prices are comparable. | Official market data plus farmer selection. | Required if market context is shown. | Low/moderate. | Controlled identifiers, unit normalization, date and market match. | Retain source observation and decision link; deletable with record. | If any semantic field is missing or mismatched, do not show the price as comparable. |
| `weather_source_record` | Preserve raw evidence and provenance. | Approved source or manual reference. | Required when alert shown. | Low. | Source ID, URL, issue/retrieval/valid times, geography, raw response reference. | Retain versioned source record for audit; access restricted; deletion can remove farmer link while retaining non-personal source audit where lawful. | Display source metadata. If unavailable, no alert. |
| `guidance_reference` | Show which agronomy reference informed comparison. | TNAU/KVK/department manual reference. | Required when guidance is used. | Low. | Title, version/date, crop/region/stage match, reviewer. | Retain citation; no hidden copying. | Display attribution and limitation. If no matching reference, refer/manual-only. |
| `decision_output` | Store what EcoFarm showed. | System. | Required. | Moderate. | Rule/version, output state, assumptions, missing-data state. | Retain for pilot accountability; deletion route. | Explain that output is decision support, not a guarantee. |
| `farmer_response` | Learn whether farmer accepted, rejected, changed, or ignored the output. | Farmer. | Optional. | Moderate. | Controlled response plus free-text optional. | Retain only for evaluation with separate consent; deletable. | “Your response helps evaluate the tool and does not change your eligibility.” If declined, continue without it. |
| `escalation_event` | Record referral trigger and result. | System/human. | Required when referral occurs. | Moderate/high. | Trigger, wording shown, source/contact used, completion state. | Restricted access; retain for safety audit; deletion request process. | Explain referral logging; never claim institution responded unless documented. |

## Consent states

| State | Meaning | System behavior |
|---|---|---|
| Not asked | Field not needed yet. | Do not collect. |
| Declined | Farmer chose not to provide or store it. | Do not ask repeatedly; exclude dependent output. |
| Granted for this decision | Use limited to the named decision. | Use only for that packet and stated retention period. |
| Granted for evaluation | Separate permission for de-identified product evaluation. | Store evaluation record separately and allow withdrawal. |
| Permission pending | External owner or institutional agreement required. | Do not ingest or display as an automated source. |

## Minimum P0 collection

The absolute minimum for a weather-supported sowing packet is language, village/block, crop, crop stage, intended sowing window, and a farmer-confirmed objective or constraint. A crop-option comparison additionally requires water availability and at least one operational constraint. Soil-test values, exact plot coordinates, phone number, land title, identity documents, income, and market context are not required unless a named test needs them.

## Retention and deletion default

During the pilot, retain decision records only for the shortest period needed for safety review and agreed evaluation; an initial proposal is 90 days after the decision unless the farmer requests earlier deletion. Source records may be retained separately in a non-personal operational log for integrity and incident review. The UI must expose a deletion/support route and state what deletion removes or cannot remove from legally required safety records.

## References

[1]: https://namakkal.nic.in/departments/agriculture/ "Namakkal District Agriculture Department"
[2]: https://soilhealth.dac.gov.in/ "Soil Health Card Portal"
[3]: https://api.imd.gov.in/ "IMD API Management Platform"
[4]: https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi "data.gov.in mandi-price resource"
[5]: https://tnau.ac.in/site/research/crop-production-guide/ "TNAU Crop Production Guide"
