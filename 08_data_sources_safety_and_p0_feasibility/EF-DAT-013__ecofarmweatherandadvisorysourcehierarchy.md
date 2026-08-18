# EcoFarm Weather and Advisory Source Hierarchy

**Scope.** This hierarchy applies only to weather/advisory evidence used inside the single sowing/early-establishment decision packet. It does not create an independent weather product and does not override official warnings.

## Precedence

| Rank | Source | Geographic use | Permitted role | Current status |
|---|---|---|---|---|
| 1 | IMD official warning or forecast for the target location/period, retrieved through an approved API or explicitly current official page | Use only when the response identifies the target district/block or a defensible location scope. | Raw warning/forecast and conservative source-labelled prompt. | Candidate; API approval verification required. |
| 2 | Current IMD/TNAU agromet bulletin that explicitly covers the target district/block and forecast period | District/block scope only; do not silently label it plot-specific. | Human-reviewed advisory reference or approved automated display after rights test. | Manual-reference until operational/reuse tests pass. |
| 3 | TAWN or other TNAU local weather record with target-block coverage and clear timestamps | Block scope only; use as corroboration or local context. | Weather context and conservative action prompt after validation. | Verification required. |
| 4 | Secondary public weather provider | Only as an internal comparison or outage diagnostic; not a farmer-facing authority in P0. | No direct P0 recommendation unless separately approved. | Context-only for first pilot. |
| 5 | Farmer report or local observation | Farmer-specific context, never a replacement for an official warning. | Ask a clarifying question or refer to official source. | P0 input only as explicitly labelled self-report. |

## Freshness policy

Freshness is evaluated against the decision moment, not merely the page’s existence. Each record must carry `issued_at`, `valid_from`, `valid_to`, `retrieved_at`, source, geography, and source version or bulletin identifier. Suggested initial thresholds are operational defaults to be validated with the source owner:

| Evidence type | Display threshold | Suppress threshold |
|---|---|---|
| Severe-weather warning | Current valid period and official source; never silently reuse after `valid_to`. | Missing valid period, expired warning, unverifiable source, or malformed response. |
| Short-horizon forecast | Retrieved within 12 hours and valid period includes the intended sowing/early-establishment action. | Older than 24 hours, outside validity period, or no location match. |
| Agromet bulletin | Current bulletin whose forecast period includes the decision date. | Bulletin period has ended, publication date cannot be established, or target geography is absent. |
| TAWN/local observation | Timestamped observation/forecast within the source’s stated update interval. | Timestamp absent, stale beyond two expected update cycles, or outage state unknown. |

These are **proposed P0 operating thresholds**, not claims about source accuracy. Before launch, the technical lead must compare them with documented source update schedules and field decision timing.

## Conflict policy

If two approved sources disagree, EcoFarm must not average them or choose the more convenient result. It should apply the following sequence:

1. Preserve both raw records and their timestamps.
2. Prefer the higher-ranked source only when it covers the same geography and validity period.
3. If the higher-ranked source is coarser, stale, or outside the period, display the conflict rather than asserting resolution.
4. Downgrade the output to a neutral information state and refer the farmer when the disagreement changes the safety of sowing, spraying, irrigation, or harvest action.
5. Never convert disagreement into a confidence score that implies statistical certainty.

## Transformation rules

EcoFarm may transform a source only through a documented, deterministic rule. A permitted transformation is: “Rain is indicated for the target period; consider checking whether sowing can be delayed and confirm local soil moisture.” It must not become: “Sow on Tuesday,” “rain will ensure establishment,” or “this is the most profitable date.” The original source text or link, source time, location, forecast period, transformation version, and limitations must remain visible to the reviewer and available to the farmer in simplified form.

The system may map a source condition to one of three output states: **informational**, **caution**, or **refer**. It may not create a high-confidence agronomic prescription from weather alone.

## Display requirements

Every displayed weather/advisory item must show the publisher, source type, target location, issued/retrieved time, valid period, freshness state, whether it is a forecast or observation, and a limitation such as “not a plot-level guarantee.” If translated or simplified, the interface must state that wording has been simplified while preserving the original reference.

## Suppression rules

Suppress the action prompt and show a neutral “No current decision-ready advisory is available” state when: the source is stale; the valid period is absent; the target geography is not covered; the response is empty, malformed, contradictory in a safety-relevant way, or rate-limited; the source terms do not permit farmer-facing transformation; or a critical farmer input such as crop stage or intended sowing window is missing.

The suppressed state should offer the latest source link, the retrieval time, the missing reason in plain language, and a generic instruction to contact a current local agriculture adviser or official service. It must not imply that an institution is waiting for the farmer or guarantee a response.

## References

[1]: https://api.imd.gov.in/ "IMD API Management Platform"
[2]: https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php "IMD Agromet Advisory Services"
[3]: https://agritech.tnau.ac.in/agrometeorologicaladvisory/agro_meteorological_advisory_tnau_district.html "TNAU district agro-meteorological advisory"
[4]: http://tawn.tnau.ac.in/ "Tamil Nadu Agriculture Weather Network"
