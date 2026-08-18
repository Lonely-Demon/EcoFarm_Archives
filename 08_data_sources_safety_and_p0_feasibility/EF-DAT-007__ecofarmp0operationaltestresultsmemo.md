# EcoFarm P0 Operational Test Results Memo

**Test date:** 13 August 2026  
**Decision scope:** One human-supervised sowing/early-establishment decision packet for Namakkal/Kongu.  
**Selected candidate weather/advisory path:** TNAU public district Agro-Met Advisory Bulletin page, not the IMD API or a second weather source.  
**Decision rule:** An official webpage, logo, HTTP 200 response, or public page is not approval. Each source must pass access, rights, freshness, locality, provenance, semantics, and failure-behaviour checks.

> **Bottom line:** No external automated source passed P0 approval. The selected TNAU weather/advisory path is **rejected for the first pilot’s automated P0 workflow** because its current bulletin explicitly states that **Namakkal district weather details are not available**, and the publicly retrieved page contains an “All Rights” notice without an identified automated reuse, storage, transformation, or redistribution permission. The only defensible next test is a **human-reviewed packet using consented farmer context and manual references**, with no automated weather prompt.

## 1. Test fixture and evidence boundary

The test used the public URL `https://agritech.tnau.ac.in/agrometeorologicaladvisory/agro_meteorological_advisory_tnau_district.html`, retrieved from the sandbox without credentials at `2026-08-13T15:00:47Z`. The response was `HTTP 200`, with `Last-Modified: Wed, 12 Aug 2026 04:10:41 GMT`, `ETag: "5048-658d1c54077e0"`, and page text showing forecast period **12.08.2026 to 16.08.2026**. The page also stated: “Krishnagiri, Dharmapuri, Salem, **Namakkal**, Kanyakumari - Districts weather details are not available for now.” This is direct evidence of a target-locality failure for the chosen event.[1]

The operational artifacts are preserved under `p0_test_artifacts/`: `tnau_agromet_headers.txt`, `tnau_agromet_body.html`, `tnau_weather_test_manifest.txt`, and the body SHA-256 `f900533879bf2fd1eb285cc259987585cae4948d573f8f406515e194c0954a96`. A conditional request using the server ETag returned `HTTP 304`; a deliberately nonexistent public path returned `HTTP 404`. These tests confirm basic HTTP/cache/error responses, not an approval for automated use.

## 2. Pass/fail table for tested sources and controls

| Tested source or control | Access | Rights / terms | Freshness / validity | Locality / semantics | Provenance / schema | Failure behaviour | Classification | Safe user-facing state | Attribution / next owner | Allowed in a future narrow pilot? |
|---|---|---|---|---|---|---|---|---|---|---|
| **TNAU public district Agro-Met Advisory Bulletin** | **Pass:** public unauthenticated `HTTP 200` page. | **Fail:** page contains “All Rights”; no tested permission for automated retrieval, caching, transformation, translation, or farmer-facing redistribution. | **Pass for page freshness only:** response dated 13 Aug; `Last-Modified` 12 Aug; page period 12–16 Aug. | **Fail:** page explicitly says Namakkal district weather details are unavailable. No target-district advisory/action text exists. | **Partial pass:** publisher, URL, ETag, last-modified, page period, and HTML body captured; **fail as P0 schema** because it is an HTML district directory/image-map, not a documented stable target record. | **Partial pass:** conditional cache request returned 304; nonexistent path returned 404; no documented empty/error schema or source SLA. | **Rejected for the first pilot** for automated P0 weather/advisory output. It is not useful as a Namakkal manual reference for this tested bulletin either. | “No current Namakkal decision-ready weather advisory is available from this source. EcoFarm is not using a substitute value.” | If only linked: “TNAU district Agro-Met Advisory Bulletin; checked [date].” Next owner: research/technical lead to obtain written reuse terms and retest only after Namakkal coverage is present. | **No** automated or transformed output. A human may independently visit the public page, but the packet must not rely on it. |
| **TNAU crop-production guidance** | Not newly retrieved in this test; prior public-source evidence only. | Unresolved for excerpting, transformation, and translation. | Version/crop/stage match must be checked per use. | Not a weather source; general guidance may not match plot/season. | Citation/version can be captured manually. | No automated failure test executed. | **Manual-reference source**. | “Reference guidance only; confirm local conditions with a qualified adviser.” | Display title/version/link; next owner: agronomy reviewer and rights owner. | **Yes, human-reviewed reference only.** |
| **Farmer-entered P0 context** | No external access needed. | Allowed only with purpose-specific consent. | Timestamp at entry and re-confirm before action. | Passes only after crop, stage, block, sowing window, constraint, and objective validation. | Source is the farmer-input record with consent and schema version. | Missing critical field must fail closed. | **Permission-dependent until consent/validation/deletion test passes; candidate approved input afterward.** | “We need [missing field] before we can show a constrained comparison.” | State field purpose and deletion route; next owner: product/privacy/engineering lead. | **Yes, after the implementation checklist passes.** |
| **Agmarknet/data.gov.in market source** | Not tested: Agent 1 has not identified a decision-relevant target crop and market. | Not tested for the selected sample. | Not tested for update delay. | Not tested; crop/variety/grade/unit/market relevance unknown. | No raw response captured in this assignment. | No source failure test executed; simulated semantic/empty states tested only. | **Context-only pending Agent 1’s crop/market selection and one semantic test.** | No market card; no “live price” or forecast. | If later tested, display full market/date/variety/unit caveat; next owner: Agent 1 + market-research owner. | **No** in P0 now. Explicitly exclude if fieldwork finds it does not influence sowing. |
| **Namakkal District Agriculture Department public directory** | **Pass:** public URL retrieved without contact. | Display is limited to neutral public-reference directory; no data or endorsement right inferred. | Page source verified 13 Aug 2026; reconfirm before release. | **Pass:** Namakkal district page; public AEC contacts visible, including examples such as Namakkal office `04286 233698`. | Page URL and body hash captured. | Directory entry must be marked stale if not rechecked on schedule. | **Current referral information**, not a partner. | “Public contact information for independent verification. EcoFarm does not claim a partnership or response-time commitment.” | URL, page verification date, and public contact provenance; next owner: operations lead. | **Yes, link/public contact only** after periodic reconfirmation. |
| **KVK Namakkal public directory** | **Pass:** public URL retrieved without contact. | Same neutral-directory limitation; no referral protocol or partnership inferred. | Page source verified 13 Aug 2026; reconfirm before release. | **Pass:** page identifies KVK at Veterinary College and Research Institute Campus, Namakkal 637002, with public phone `04286-266345, 266244` and email `[REDACTED_EMAIL]`.[2] | Page URL and body hash captured. | If URL/contact changes or lacks verification date, remove from public directory. | **Current referral information**, not a partner. | “Public contact information for independent verification. EcoFarm does not claim that KVK Namakkal reviews, endorses, or responds to EcoFarm cases.” | URL, contact, geography, verification date; next owner: operations lead. | **Yes, link/public contact only** after periodic reconfirmation. |
| **Observability simulated failure suite** | **Pass:** eight records created and validated. | Not an external-source rights question. | N/A. | N/A. | Each record includes a state, expected UI, expected action, and PASS result. | **Pass:** records cover stale, empty, malformed, unauthorized, geography mismatch, semantic mismatch, conflict, and transformation unverified. | **Approved design-control test only.** It does not approve a live integration. | See the per-state fail-closed wording below. | Artifact: `p0_test_artifacts/observability_simulated_failure_records.jsonl`; next owner: engineering/QA lead to implement and replay in test environment. | **Yes, as a pre-build QA control.** |

## 3. Required operational result for the selected weather path

The path fails P0 approval even though it is public, current at the statewide bulletin level, and returns successful HTTP/cache responses. The decisive failure is target relevance: a Namakkal farmer cannot receive a geographically matched advisory when the page states Namakkal details are unavailable. The separate rights failure means EcoFarm also cannot convert the page into a stored or transformed automated alert. The correct classification is **Rejected for the first pilot**, not “approved with caveats.”

The user-facing state is therefore:

> “No current Namakkal decision-ready weather advisory is available from this source. EcoFarm is not using an older, general, or substitute value. You can review the public source directly or check current local agriculture guidance.”

Do not substitute a statewide page, a nearby district, a generic weather provider, a past bulletin, or an untested API. Doing so would violate the one-path test and obscure the locality failure.

## 4. Referral directory verification

| Directory entry | Public URL | Public contact / geography | Verified | Required neutral wording | Status |
|---|---|---|---|---|---|
| Namakkal District Agriculture Department | https://namakkal.nic.in/departments/agriculture/ | Namakkal District; page lists block/AEC contacts, including `04286 233698` for the Namakkal office. | 13 Aug 2026 | “Public contact information for independent verification. EcoFarm does not claim a partnership, endorsement, case acceptance, or response-time commitment.” | Current referral information only. |
| KVK Namakkal | https://agritech.tnau.ac.in/kvk/kvk_namakal.html | Veterinary College and Research Institute Campus, Namakkal 637002; phone `04286-266345, 266244`; email `[REDACTED_EMAIL]`. | 13 Aug 2026 | Same no-partnership wording. | Current referral information only. |

No institution, FPO, KVK, department, or actor is classified as a partner. The directory must record its last verification date and remove/recheck entries after a defined review interval. EcoFarm must not call, message, or send case data to any listed actor without a documented agreement and farmer consent where appropriate.

## 5. Implementation-ready P0 checklist result

The detailed field-by-field build gate is in `EcoFarm_P0_Implementation_Ready_Checklist.md`. The minimal packet may request only: language, village/block, crop, crop stage, intended sowing window, water category, and objective. It must show purpose-specific consent, validation, retention/deletion action, farmer-input source record, source/freshness record, output state, referral trigger, and fail-closed behaviour.

The weather-source row is **blocked**. A narrow prototype could test consented farmer context plus a human reviewer using manual references, but it must not emit a weather-derived recommendation. Soil records remain permission-dependent; market context is excluded until the designated crop/market semantic test exists.

## 6. Observability simulation results

All eight required failure states were simulated once and produced the intended fail-closed action in the design artifact. These are control tests, not evidence of external-source approval.

| Simulated state | Expected safe state | Result |
|---|---|---|
| Stale | “No current decision-ready information”; suppress prompt. | Pass. |
| Empty | “No comparable record found”; do not substitute zero or nearby data. | Pass. |
| Malformed | “Source temporarily unavailable”; suppress and log parser error. | Pass. |
| Unauthorized | “Source not available for this packet”; classify permission-dependent. | Pass. |
| Geography mismatch | “Not available for your area”; suppress local action prompt. | Pass. |
| Semantic mismatch | “Market record not comparable”; hide price number. | Pass. |
| Conflict | “Sources conflict”; preserve both, suppress action, refer. | Pass. |
| Transformation unverified | “Reference only, not a recommendation”; require human review. | Pass. |

## 7. P0 eligibility decision and owners

| Decision | Result | Owner / exact next artifact |
|---|---|---|
| Approve automated weather/advisory source | **No.** Selected source failed locality and rights. | Research/technical lead: do not test a second path under this assignment; future separate plan requires source owner terms, target coverage, schema, and failure test. |
| Approve human-reviewed packet | **Conditional yes.** It may use consented farmer context and manual references only. | Product/privacy/engineering: implement checklist, consent/deletion, logging, suppression, and reviewer gate. |
| Include market context | **No.** | Agent 1: provide real crop + market relevance; market owner: execute one semantic sample. |
| Launch referral directory | **Conditional yes.** Public links/contacts only, with verification date and neutral wording. | Operations: recheck contact/page before pilot release and periodically after. |
| Build narrow pilot with automated source-derived output | **No.** | Technical lead: blocked until an external source separately passes all P0 tests. |

## References

[1]: https://agritech.tnau.ac.in/agrometeorologicaladvisory/agro_meteorological_advisory_tnau_district.html "TNAU Agro-Met Advisory Bulletin for Tamil Nadu districts"
[2]: https://agritech.tnau.ac.in/kvk/kvk_namakal.html "TNAU Krishi Vigyan Kendra, Namakkal"
[3]: https://namakkal.nic.in/departments/agriculture/ "Namakkal District Agriculture Department"
[4]: https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi "data.gov.in daily mandi-price resource"
[5]: https://tnau.ac.in/site/research/crop-production-guide/ "Tamil Nadu Agricultural University Crop Production Guide"
