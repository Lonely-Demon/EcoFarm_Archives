# EcoFarm P0 Data-Source Register — Operational Revision

**Decision context:** One human-supervised sowing/early-establishment decision packet. **Status date:** 13 August 2026. **Important:** No source is marked Approved P0 unless the operational tests in `EcoFarm_P0_Source_Operational_Test_Plan.md` have passed.

| Source | Intended P0 use | Desk evidence | Operational classification today | Missing approval evidence | Decision consequence |
|---|---|---|---|---|---|
| Farmer-entered crop, stage, location/block, sowing window, water and objective | Minimum decision context | Required fields can be collected directly with consent; no external integration required. | **Permission-dependent until consent/validation flow passes; candidate Approved P0 afterward.** | Consent copy, validation test, deletion route, language test, and missing-field behavior. | May support packet only when critical fields are complete. |
| IMD API | Weather forecast/warning input | Official portal advertises observations, forecasts, warnings, and bulletins; registration/login visible.[1] | **Verification required; not Approved P0.** | Credentials, endpoint schema, Namakkal coverage, timestamp/validity, rate limits, rights, and error tests. | No automated weather output until passed. |
| IMD/TNAU public bulletin | Human-reviewed weather/advisory reference | Official pages expose current agromet material.[2] [3] | **Manual-reference.** | Reuse/translation/redistribution terms, stable retrieval, target geography, and monitoring. | Human may link or review; automated transformation blocked. |
| TAWN | Potential block/local weather context | TNAU network describes local weather/advisory service.[4] | **Verification required.** | Target-block record, update timing, uptime, source metadata, rights, and stale behavior. | Excluded from P0 until tests pass. |
| Agmarknet/data.gov.in | Optional raw market observation | OGD resource publishes daily mandi-price data and identifies government ownership/metadata.[5] | **Verification required for Approved P0; candidate raw-observation source.** | One real commodity/market semantic sample, reporting delay, missingness, API terms, rate limits, and local relevance. | No market number displayed until semantic pass; never forecasting. |
| TNAU crop-production guide | Referenced agronomic context | University crop guidance is publicly available.[6] | **Manual-reference.** | Version, crop/region/stage match, reuse/translation terms, and human review. | May be cited or reviewed; no hidden automated prescription. |
| KVK Namakkal content/contact | Technical validation and referral context | KVK page documents location, services, and contacts.[7] | **Documented context / current referral information only.** | Current service confirmation; no partnership or data right shown. | Display public link/contact with neutral disclaimer; no automated dependency. |
| Namakkal Agriculture Department/ATMA | Local context, public referral, human escalation | District page documents extension, soil testing, training, ATMA, and AECs.[8] | **Documented context / current referral information only.** | Current contact verification and any written referral/data agreement. | Public link only; no response promise. |
| Soil Health Card / farmer report | Optional farmer-consented constraint | District lab and national portal exist.[8] [9] | **Permission-dependent.** | Farmer consent, report schema, sample date, access method, storage/deletion, and owner permission if not farmer-provided. | Excluded unless consented record is available. |
| CGWB/India-WRIS | Background water context | Public reports and portal exist.[10] [11] | **Context-only.** | A current, scoped record directly relevant to the target decision. | Must not enter P0 packet as farmer-level water status. |
| eNAM | Market context only | Official portal documents electronic market network.[12] | **Context-only for P0.** | Local market participation and transaction conditions. | No trading or buyer-assurance function. |
| Satellite/remote sensing | Research validation only | Public/commercial imagery is technically available. | **Rejected for first pilot.** | Would require ground truth, plot relevance, cloud/latency, and rights beyond P0 need. | Excluded from decision output. |

## Institutional classification rule

The named institutions above are documented context or current public-referral information. None is a **documented partner**. That category remains unused because no written agreement, endorsement, data-sharing authorization, referral protocol, or distribution commitment was found in the current evidence.

## References

[1]: https://api.imd.gov.in/ "IMD API Management Platform"
[2]: https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php "IMD Agromet Advisory Services"
[3]: https://agritech.tnau.ac.in/agrometeorologicaladvisory/agro_meteorological_advisory_tnau_district.html "TNAU district agro-meteorological advisory"
[4]: http://tawn.tnau.ac.in/ "Tamil Nadu Agriculture Weather Network"
[5]: https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi "data.gov.in mandi-price resource"
[6]: https://tnau.ac.in/site/research/crop-production-guide/ "TNAU Crop Production Guide"
[7]: https://agritech.tnau.ac.in/kvk/kvk_namakal.html "TNAU KVK Namakkal"
[8]: https://namakkal.nic.in/departments/agriculture/ "Namakkal District Agriculture Department"
[9]: https://soilhealth.dac.gov.in/ "Soil Health Card Portal"
[10]: https://cgwb.gov.in/cgwbpnm/public/uploads/documents/17096271421048841089file.pdf "CGWB groundwater report"
[11]: https://indiawris.gov.in/wiki/doku.php?id=cgwb_ground_water_resources "India-WRIS / CGWB groundwater resources"
[12]: https://enam.gov.in/ "eNAM"
