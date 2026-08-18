# Verified research findings: data feasibility and alternatives

## Data Feasibility

### Weather and Agricultural Advisories
- **IMD Agromet Advisory Services:** IMD issues district-level forecasts and block-level agro-advisories (e.g., through AMFUs and TNAU). The TNAU Agritech Portal hosts the Weather Watch Group and TamilNadu Agriculture Weather Network (TAWN), providing real-time weather and block-level advisories.
- **API Access:** IMD operates an API Management Platform (api.imd.gov.in) offering real-time observations, forecasts, and warnings.
- **Pilot Feasibility:** Available and pilot-usable. The block-level resolution is sufficient for general weather alerts, but translating generic advisories into specific, localized farmer actions requires careful interpretation and must not claim to guarantee crop outcomes.

### Market-Price Observations
- **Agmarknet / data.gov.in:** The OGD platform (data.gov.in) provides a "Current daily price of various commodities from various markets (Mandi)" dataset via API, sourced from Agmarknet. It includes variety-wise daily market prices (minimum, maximum, modal).
- **Tamil Nadu Regulated Markets:** The Department of Agricultural Marketing & Agri Business operates 268 Regulated Markets (including in Namakkal) ensuring competitive prices through closed tenders.
- **Pilot Feasibility:** Available and pilot-usable. The data is descriptive (current/historical prices). EcoFarm must strictly present this as observation, not as a future-price prediction or buyer assurance.

### Soil, Water, and Crop Context
- **Soil Health Card (SHC):** The national SHC portal distributes soil test data to farmers. Namakkal has a Soil Testing Laboratory and a mobile unit. However, accessing a specific farmer's SHC data programmatically likely requires consent and integration, which is not guaranteed for a pilot.
- **Groundwater (CGWB):** CGWB reports indicate Tamil Nadu is water-scarce with quality issues (e.g., fluoride). Namakkal has undulating terrain and relies on groundwater and rainfall. Specific block-level depletion rates require primary data access.
- **Crop Production Guide:** TNAU publishes comprehensive Crop Production Guides (e.g., Horticulture 2020, general 2024) detailing agronomic practices, pest, and disease management.
- **Pilot Feasibility:** TNAU guides are available and pilot-usable for general agronomy. SHC and specific groundwater data are "requires permission or partnership" or "available but insufficient alone" for automated recommendations.

## Existing Alternatives

- **Institutional / Public Digital:** 
  - **Kisan Suvidha App:** Provides weather, crop advisory, market prices, and agri services.
  - **mKisan SMS Portal:** Delivers region/crop-specific SMS advisories (weather, market, soil).
  - **eNAM:** Pan-India electronic trading portal for APMC mandis, providing price information and remote bidding.
- **Local Institutional:** TNAU KVKs, ATMA, and district agriculture departments provide training, demonstrations, and soil testing.
- **Job Served:** These alternatives provide broad information broadcast, generic advisories, and market price discovery.
- **Limitations:** Often generic, not tailored to the specific constraints of an individual farmer's plot, and may lack a localized, interactive decision-support workflow.
- **EcoFarm Relationship:** EcoFarm should complement these by offering a localized, constraint-aware workflow that aggregates this public data into a specific decision context (e.g., crop-option comparison), rather than just duplicating the broadcast of prices or weather.
