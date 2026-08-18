# EcoFarm Target-Market Semantics Verification Plan

**Purpose.** Market data is optional context for the sowing/early-establishment decision packet. It must be excluded unless one real target commodity/market sample is shown to be semantically comparable, current enough, and safely displayable. This plan does not create a price-prediction workflow.

## Selection protocol

Before testing, Agent 1 and fieldwork must identify one crop that farmers actually consider around sowing and one market that farmers can realistically access. Record the local crop name, English/official name, variety, grade/quality convention, unit, quantity, market name/code, distance/route, and the farmer’s actual alternative source of price information.

## Required sample

Obtain one raw sample from the official Agmarknet/data.gov.in route for the target commodity and market, plus one independent confirmation from the regulated market, FPO, trader, or farmer sale record. The independent confirmation is not treated as a replacement official feed; it tests whether the official observation is locally intelligible.

| Semantic field | Required evidence | Pass condition | Fail behavior |
|---|---|---|---|
| Market identifier and name | Official code/name plus local name and location. | Exact market is identified and farmer can distinguish it from nearby markets. | Exclude from packet; do not merge markets. |
| Commodity identifier | Official commodity name and local name. | Same crop/product, not a broad category. | Exclude or ask for clarification. |
| Variety | Variety field or explicit “not reported.” | Display only when the source and farmer selection match. | Do not compare unlike varieties; show “variety not comparable.” |
| Grade/quality | Grade, quality, moisture, or “not reported.” | Grade/quality assumptions are visible. | Do not imply farmer’s produce would receive the modal/minimum/maximum value. |
| Price statistic | Minimum, maximum, modal, and exact definition. | Statistic is labelled as reported, not expected. | Exclude if definition is unclear. |
| Unit | Official unit and normalized display unit. | Unit is explicit and conversion is deterministic. | Exclude; never silently convert. |
| Date | Observation date, publication/update time, retrieval time. | Farmer can see how current it is. | Show stale/missing state or suppress. |
| Reporting delay | Compare observation date to publication/retrieval time. | Delay is measured and under a documented threshold. | Display delay warning or suppress. |
| Missingness | Query known missing date/market/commodity and record response. | Empty result is distinguishable from zero price. | Fail closed; never display zero or interpolate. |
| Local relevance | Independent farmer/market confirmation. | A farmer or local actor recognizes the market/commodity and statistic. | Keep as technical observation only; exclude from farmer packet. |
| Terms / reuse | Resource license, API terms, attribution, rate limit. | Rights allow intended retrieval, storage, transformation, and display. | Manual-reference or permission-dependent. |

## Safe display wording

If all pass conditions are met, display:

> “Reported mandi observation: [commodity/variety] at [market], [statistic] ₹[amount]/[unit], observation date [date], retrieved [time]. This is a current observation, not a forecast, buyer offer, or guaranteed sale price. Actual realization may differ by quality, quantity, timing, transport, deductions, and buyer terms.”

If only part of the semantics pass, display no number and state:

> “A market record was found, but its market, variety, quality, unit, or freshness could not be matched reliably to your produce. It is not shown as a comparable price.”

## Verification interview prompts

Ask the farmer: “Which market would you realistically use?” “What do you call this crop and variety locally?” “What unit does the trader quote?” “Do min/max/modal labels make sense to you?” “How different is the trader’s quote from the displayed observation?” “What deductions or transport costs affect the actual sale?” “Would this observation change your sowing decision, or is it only useful at harvest?”

Ask the market/FPO/trader, without treating the response as official validation: “Does this commodity/variety/grade trade in this market?” “What does the displayed unit mean?” “How delayed are official records?” “What quality factors move the realized price?” “What would make the record misleading to a farmer?”

## Decision outcomes

| Outcome | Classification | P0 consequence |
|---|---|---|
| Official record and local interpretation match; rights and freshness pass. | Approved P0 input for raw observation. | May appear as optional context with full metadata. |
| Official record is credible but local semantics or rights are unresolved. | Manual-reference or permission-dependent. | Human may inspect/link; automated display blocked. |
| Record is too stale, incomplete, or incomparable. | Context-only or rejected for first pilot. | Exclude from packet. |
| Fieldwork shows the price does not affect the sowing decision. | Product-scope exclusion. | Do not collect or display market context for P0. |

## References

[1]: https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi "data.gov.in mandi-price resource"
[2]: https://www.agrimark.tn.gov.in/ "Tamil Nadu Agricultural Marketing Department"
[3]: https://agritech.tnau.ac.in/agricultural_marketing/agrimark_Regulated%20markets_list.html "TNAU regulated-market list"
[4]: https://enam.gov.in/ "eNAM"
