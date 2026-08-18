# EcoFarm Safe Referral and Escalation Design

**Purpose.** Provide a safe next step when the decision packet cannot responsibly answer a farmer’s question. EcoFarm may display publicly documented contact information and links, but must not imply that an institution has agreed to receive EcoFarm referrals, respond within a time limit, validate the product, or endorse its output.

## Referral states

| Trigger | Farmer-facing wording | Current referral behavior | What EcoFarm promises | What requires a documented agreement |
|---|---|---|---|---|
| Critical source missing or stale | “We do not have current, location-matched information for this decision. Please check the latest official agriculture or weather service before acting.” | Show the source link and retrieval time; optionally show publicly documented Namakkal Agriculture Department or KVK contact details with “contact information found on the public source page.” | Only that EcoFarm will not create the missing answer. | Warm transfer, response-time guarantee, case acceptance, or institution-specific escalation queue. |
| Weather/advisory conflict affecting sowing | “The available sources do not agree for your location or time window. We are not resolving this automatically. Please confirm with a current local agriculture adviser before sowing.” | Display both source identities, timestamps, and links; list the conflict plainly. | Preserve and explain the conflict. | Institutional adjudication or formal referral protocol. |
| Crop, stage, or location outside tested scope | “This crop, stage, or area is outside the tested scope of this pilot. We can show general references, but we are not providing a decision recommendation.” | Link to relevant public TNAU/KVK/department material if available. | No recommendation outside scope. | Expert review or expanded scope agreement. |
| Pest/disease symptom or pesticide question | “A text or image description is not enough to safely identify this problem or prescribe treatment. Please consult a qualified local agriculture or plant-protection adviser and follow the product label.” | Provide public institutional sources and contact information; do not diagnose. | No diagnosis, dosage, or treatment assurance. | Named expert review, case triage, or response commitment. |
| Soil or water evidence missing for a constraint-sensitive comparison | “We do not have the soil or water information needed for a responsible comparison. You can continue with a non-recommendation information view or obtain a current test/adviser review.” | Link to the public soil-testing/department information; do not substitute district averages silently. | No inference from unavailable farmer evidence. | Access to laboratory records, sampling service, or institutional workflow. |
| Farmer asks for highest profit or future price | “We only show current observations and documented assumptions. We cannot predict the highest-profit crop, future price, or guarantee a buyer.” | Provide observed market data only when semantics pass. | No price or profit prophecy. | None; this boundary must remain permanent for P0. |
| Source/API inaccessible | “This information is temporarily unavailable. We are not using an older or unverified value as if it were current.” | Log failure; show last successful retrieval only as historical context, never as current advice. | Fail closed. | Vendor/service-level agreement or official support channel. |
| Urgent safety or disaster warning | “Please follow the latest official warning and local emergency instructions. EcoFarm is not an emergency service.” | Link to current official warning/emergency information. | No emergency response or institutional representation. | Emergency-channel integration or formal authorization. |

## Public referral information

At launch, EcoFarm may maintain a reviewed directory containing the Namakkal District Agriculture Department page, publicly listed Agricultural Extension Centre contacts, KVK Namakkal public contact page, TNAU Agritech resources, and official IMD/TNAU weather pages. Each entry must show source URL, last verification date, geography, whether it is a public information link or a confirmed referral, and the following notice:

> “EcoFarm is providing publicly available contact information for independent verification. EcoFarm is not claiming that this institution has partnered with, reviewed, endorsed, or agreed to respond to EcoFarm users.”

The directory must never label an actor “partner,” “official EcoFarm adviser,” “on-call,” or “verified responder” without written evidence.

## Escalation record

When a referral trigger occurs, log only the minimum required fields: decision ID, trigger category, source state, wording shown, public link displayed, timestamp, farmer-selected next step if any, and whether the farmer later reported a response. Do not log a response as successful unless the farmer or institution provides evidence. Store contact details separately from farmer data where possible.

## Human-supervision boundary

A human reviewer may inspect the source evidence and farmer inputs before a constrained output is shown. The reviewer must be able to suppress the output, identify missing fields, record the reason, and refer the case. The reviewer must not convert a generic source into an individualized guarantee, provide unverified pesticide instructions, or imply institutional authority.

## Agreement gates

A documented agreement is required before EcoFarm may: send cases directly to an institution; display a dedicated institutional queue; state that an institution reviews EcoFarm outputs; use non-public data; reproduce protected content beyond permitted terms; promise a response time; use an institution’s logo or endorsement; or describe an actor as a distribution partner. Until then, use public links and neutral wording only.

## References

[1]: https://namakkal.nic.in/departments/agriculture/ "Namakkal District Agriculture Department"
[2]: https://agritech.tnau.ac.in/kvk/kvk_namakal.html "TNAU KVK Namakkal"
[3]: https://api.imd.gov.in/ "IMD API Management Platform"
[4]: https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php "IMD Agromet Advisory Services"
