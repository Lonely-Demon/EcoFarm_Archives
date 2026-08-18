# EcoFarm P0 Feasibility Decision Memo

**Decision context:** One human-supervised sowing/early-establishment decision packet for the Namakkal/Kongu pilot. **Status:** Revision decision as of 13 August 2026.

## 1. Approved P0 inputs and sources.

No external automated source has yet passed every operational test, so the only immediately defensible P0 inputs are **consented, farmer-entered minimum context** and **human-reviewed public references**. Farmer-entered language, village/block, crop, crop stage, intended sowing window, water category, and decision objective may support a packet after validation, consent, retention, and deletion tests pass. TNAU crop guidance may be used as a manual reference with title/version/attribution and human review. Current IMD/TNAU/TAWN weather or Agmarknet/data.gov.in market observations remain candidate sources pending authenticated access or retrieval, field schema, freshness, geography, rights, semantic, and failure tests. A market observation, if approved, remains raw descriptive context only.[1] [2] [3] [4]

## 2. Manual-only, permission-dependent, and rejected sources.

IMD API access, TAWN automated retrieval, and automated IMD/TNAU bulletin transformation are **verification required** until credentials, endpoint fields, terms, timestamps, target geography, and failure behavior pass. Public agromet and TNAU crop materials are **manual-reference** until reuse and transformation rights are confirmed. Farmer soil reports and Soil Health Card records are **permission-dependent** because the farmer’s consent, report access, and owner permissions are not established. Namakkal Agriculture Department, ATMA, KVK Namakkal, TANUVAS, FPOs, and market actors are **documented context or field-verification targets**, not partners. CGWB/India-WRIS water context is **context-only** for P0. Satellite/remote sensing is **rejected for the first pilot decision output** because small-field interpretation, ground truth, cloud/latency, and rights do not justify its use yet.[5] [6] [7]

## 3. Required UI/UX provenance, uncertainty, consent, and failure-state requirements.

Every output must show source name, publisher, source URL or reference, issue/retrieval time, valid period or observation date, geography/market, source version, freshness state, and limitation. The interface must distinguish observation, forecast, reference guidance, transformed prompt, and referral. It must show why a field is requested, collect only fields needed for the named decision, obtain purpose-specific consent for farmer data, and provide a deletion/support route. It must fail closed for stale, empty, malformed, unauthorized, wrong-geography, semantically mismatched, contradictory, or unreviewed transformed data. User-facing states must say “no current decision-ready information,” “not comparable,” “temporarily unavailable,” “sources conflict,” or “outside tested scope” rather than displaying an old or substituted value.

## 4. Technical blockers that must be resolved before a narrow pilot build can start.

The team must complete one end-to-end source test for the selected weather/advisory path and one real target commodity/market semantic sample if market context remains relevant. It must document access credentials, fields, update delay, rate limits, storage/redistribution rights, attribution, source-version capture, empty/error behavior, and fallback. It must complete a Tamil-language farmer input/comprehension test, consent/deletion implementation, a human-review and no-partnership referral process, and the observability logs for source freshness, conflicts, transformations, suppression, and escalation. The pilot must preserve the prohibitions on future-price prediction, buyer assurance, guaranteed-profit recommendations, autonomous high-stakes agronomy, hardware actuation, marketplace functions, and implied institutional partnership.

[1]: https://api.imd.gov.in/ "IMD API Management Platform"
[2]: https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi "data.gov.in mandi-price resource"
[3]: https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php "IMD Agromet Advisory Services"
[4]: https://tnau.ac.in/site/research/crop-production-guide/ "TNAU Crop Production Guide"
[5]: https://namakkal.nic.in/departments/agriculture/ "Namakkal District Agriculture Department"
[6]: https://agritech.tnau.ac.in/kvk/kvk_namakal.html "TNAU KVK Namakkal"
[7]: https://soilhealth.dac.gov.in/ "Soil Health Card Portal"
