# EcoFarm P0 Source Operational-Test Plan

**Purpose.** This plan tests whether a source is operationally usable for one human-supervised **sowing/early-establishment decision packet** in a defined Namakkal/Kongu pilot location. A source is not approved because it is official, visible, or technically reachable. It must pass access, provenance, freshness, geographic relevance, rights, and failure-behaviour tests.

## P0 decision packet scope

The packet supports a farmer deciding whether and how to proceed with a narrowly defined sowing or early-establishment event. It may combine farmer-entered constraints, a source-labelled weather/advisory signal, referenced crop guidance, and optional current market context. It produces a bounded comparison or action prompt with assumptions and referral instructions. It does not predict profit or prices, guarantee establishment, diagnose disease, prescribe autonomous high-stakes treatment, execute irrigation, or transact with buyers.

## Operational categories

| Category | Meaning | Product consequence |
|---|---|---|
| Approved P0 source | All required access, rights, freshness, geography, provenance, and failure tests pass. | May support a constrained, source-labelled output. |
| Manual-reference source | Content is reliable, but automated reuse/right/access is not established. | Human reviewer may consult or link it with attribution; no automated ingestion. |
| Context-only source | Useful for background but too coarse, stale, or non-actionable. | Excluded from the farmer decision packet. |
| Permission-dependent source | Requires farmer consent, owner permission, or institutional agreement. | Remains unavailable until documented permission exists. |
| Rejected for first pilot | Cannot satisfy safety, relevance, or operational conditions. | Excluded regardless of technical appeal. |

## Test cases and pass criteria

| P0 source | Owner / access method | Required test request or artifact | Expected response and fields | Update / freshness test | Rights and attribution test | Fallback and fail condition | Pass criteria |
|---|---|---|---|---|---|---|---|
| IMD API forecast or warning | India Meteorological Department; account registration and documented API endpoint. | Obtain test credentials through the official portal; request one Namakkal-relevant forecast/warning for a fixed timestamp and location. | Machine-readable response with endpoint identity, issued time, valid period, location, variables, units, warning/advisory text, and error schema. | Repeat request at two times; compare issued/valid timestamps; record latency and revision behavior. | Obtain written/API terms covering storage, caching, transformation, attribution, rate limits, and farmer-facing redistribution. | If unauthenticated, fields undocumented, location too coarse, stale, or terms unresolved: manual-reference or permission-dependent. | **Not yet passed from desk research.** Pass only after successful authenticated request, documented terms, Namakkal relevance, and stale/error tests. |
| IMD/TNAU public agromet bulletin | IMD/TNAU public bulletin page. | Save one current bulletin and its URL, issue date, forecast period, geography, crop/action text, and language. | Human-readable bulletin with explicit period and location. | Check whether the bulletin is replaced predictably and whether old URLs remain stable. | Confirm whether copying, storing, translating, or transforming wording is permitted; otherwise retain link and human reference only. | If bulletin has no current period, no Namakkal relevance, or unstable access: suppress and show no current advisory. | May be **manual-reference** until reuse/automation terms and monitoring pass. |
| TAWN / local weather network | TNAU/Tamil Nadu Agriculture Weather Network. | Retrieve one target-block weather/advisory record and capture location, issue time, variables, forecast period, and source identity. | Block-relevant weather/advisory record with timestamps and units. | Measure update interval, outage duration, and stale record behaviour for at least one observation cycle. | Verify terms, attribution, automated retrieval, and whether derived alerts may be displayed. | If block coverage or uptime is unproven: manual-reference or context-only. | Approved only after target-block coverage, timestamps, rights, and stale-response handling pass. |
| Agmarknet/data.gov.in price resource | Directorate of Marketing & Inspection / data.gov.in; API/resource access. | Query one target commodity, variety, market, date, and state; save raw response and metadata. | Stable identifiers plus market, commodity, variety, date, min/max/modal price, unit, and any arrival fields. | Compare publication date, update timestamp, and observed reporting delay; request missing and future dates. | Confirm Government Open Data License–India scope, API key/rate limits, attribution, caching, and transformation rights. | If identifiers do not match or missingness is high: do not display the record; use another verified market or no market context. | Approved only for raw observations after semantic and rights tests; never approved for forecasting. |
| TNAU crop-production guidance | Tamil Nadu Agricultural University; public guide/PDF/page. | Select the exact crop and sowing/early-establishment section; save title, version/date, crop, region, and relevant passage. | Referenced agronomic guidance with source/version, not a machine prediction. | Confirm version date and review/update process. | Confirm quotation, excerpt, translation, and derived-rule permissions; preserve attribution. | If crop/region/stage mismatch or version unknown: manual-reference or context-only. | May be approved as **manual/reference content**; automated rule use requires a documented review. |
| Namakkal soil-testing / Soil Health Card | District Agriculture Department / Soil Health Card system. | Obtain a farmer-consented sample report or blank schema; record fields, units, test date, plot relation, and report identifier. | Soil indicators and recommendations tied to a sample/date. | Test whether old reports are distinguishable and whether sample date is mandatory. | Verify consent, data access, retention, and any department permission/API route. | Without farmer consent or authorized access: permission-dependent; district averages cannot substitute silently. | Approved only for farmer-entered or authorized records with consent; not as an open automated feed. |
| CGWB groundwater context | CGWB / India-WRIS public reports or datasets. | Retrieve one scoped Namakkal record and record spatial unit, monitoring date, indicator, and publication date. | District/block/monitoring-point context with dates and definitions. | Check reporting interval and staleness. | Verify reuse and derived-display terms. | If spatial scale cannot support the farmer’s decision: context-only. | Context-only for first pilot unless a scoped, current record directly supports the packet. |
| Farmer-entered constraints | Farmer, with explicit consent. | Complete a minimal test form for one hypothetical/consented farmer and record validation errors. | Location/block, crop, intended sowing window, water status, soil-test availability, labour/input constraint, and objective. | Record entry/update time and detect stale values at the next decision. | Consent notice, purpose, retention, deletion/access process. | Missing critical field means no recommendation; ask only the missing question or refer. | Approved P0 input when minimized, consented, validated, and deletable. |
| Satellite/remote sensing | Public/commercial imagery provider. | Request one image/signal for a target plot and record resolution, acquisition date, cloud mask, and processing terms. | Image/index with acquisition metadata; no direct agronomic diagnosis. | Assess revisit, cloud, and latency. | Confirm derived-product and storage rights. | If no ground truth, cloud-free coverage, or plot relevance: rejected for first pilot. | Rejected for P0 decision output; optional research validation only. |

## Evidence register for each test

For every executed test, store the request timestamp, source URL/endpoint, authentication mode without storing secrets, raw response hash or snapshot reference, parsed fields, HTTP/status error, latency, freshness calculation, geography, terms URL, attribution text, reviewer, and classification decision. A “verification required” result must name the source owner, exact missing artifact, test owner, and threshold for approval.

## Current desk-research status

No source is upgraded to **Approved P0 source** merely from the existing webpages. The current defensible status is: farmer-entered minimum fields are potentially approved after consent/validation testing; Agmarknet/data.gov.in is a candidate for raw price observations pending semantic and rights tests; IMD API, TAWN, and automated TNAU/IMD bulletin use remain verification required; TNAU guidance is manual-reference pending reuse and rule-review confirmation; soil records are permission-dependent; CGWB is context-only; satellite data is rejected for the first decision packet.

## References

[1]: https://api.imd.gov.in/ "IMD API Management Platform"
[2]: https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php "IMD Agromet Advisory Services"
[3]: http://tawn.tnau.ac.in/ "Tamil Nadu Agriculture Weather Network"
[4]: https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi "data.gov.in mandi-price resource"
[5]: https://tnau.ac.in/site/research/crop-production-guide/ "TNAU Crop Production Guide"
[6]: https://namakkal.nic.in/departments/agriculture/ "Namakkal District Agriculture Department"
[7]: https://soilhealth.dac.gov.in/ "Soil Health Card Portal"
[8]: https://indiawris.gov.in/wiki/doku.php?id=cgwb_ground_water_resources "India-WRIS / CGWB groundwater resources"
