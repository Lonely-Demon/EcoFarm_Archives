# EcoFarm Evidence Atlas — Primary-Source Revalidation Findings

## Method Boundary

This ledger records only what the referenced primary public pages state at the time reviewed. It does not infer forecast accuracy, local usefulness, data licensing, API access, recommendation quality, or product feasibility from service existence.

## RV-001 — IMD Agricultural Weather and Advisory Service Context

| Field | Recorded finding |
|---|---|
| Revalidation status | Partially completed: official service existence and high-level presentation verified. Decision-specific access, licensing, API terms, and operational use still require separate source/use-case review. |
| Primary source 1 | [IMD Agricultural Meteorology Division](https://imdagrimet.gov.in/) identifies itself as the Agricultural Meteorology Division of the India Meteorological Department under the Ministry of Earth Sciences. Its page presents agricultural meteorology and advisory content, including agromet advisories, farmer registration/feedback, and named tools/services such as KALP, SANKALP, Meghdoot, and Damini. |
| Primary source 2 | [IMD Agromet Advisory Services](https://mausam.imd.gov.in/responsive/agromet_adv_ser_state_current.php) presents district bulletins, district-level weather forecasts, state bulletins, national bulletins, an interactive agromet map, special agromet advisory material, and state current bulletins including Tamil Nadu. |
| Narrow conclusion | The official IMD pages establish that IMD publicly presents agricultural-weather/advisory services and multiple bulletin/forecast access routes. They do not establish that any specific EcoFarm feature has a usable data interface, the right semantic fields, appropriate refresh rate, local accuracy, or safe advisory applicability. |
| Evidence Atlas treatment | `needs_revalidation` for every named feature use case; availability is a source-specific input, not a blanket validation. |

## Remaining Revalidation Items

| ID | Topic | Status |
|---|---|---|
| `RV-002` | Current Namakkal agriculture department and district-level context | Partially completed: official department and directory pages checked; individual historical numeric and operational claims remain time-bounded to the official page and require source/date care. |
| `RV-003` | Current market-price information service and price-data semantics | Partially completed: AGMARKNET portal and report filters checked; use-case-specific semantics, data access, coverage, and freshness acceptance criteria remain to be established. |
| `RV-004` | Historical national/global agricultural statistics | Partially completed: two recurring global-context claims were checked against official FAO pages. Other archive statistics remain individually unverified. |
| `RV-005` | Historical stack, sensor, AI, and automation claims | Not started; requires engineering, vendor, safety, and controlled test evidence rather than web-source substitution. |

## RV-002 — Namakkal Department and District Context

| Field | Recorded finding |
|---|---|
| Revalidation status | Partially completed: official district-page content and the official Joint Director directory entry were inspected. Individual numbers and statements must retain their page/date limitation; the review did not establish a longitudinal district dataset or operational performance. |
| Primary source 1 | [Agriculture — Namakkal District, Government of Tamil Nadu](https://namakkal.nic.in/departments/agriculture/) presents the district Agriculture Department’s stated policy/objectives, agricultural context, listed crops, irrigation sources, facilities, schemes, extension-centre structure, and contact information. It also states area/rainfall/soil/crop figures and programme descriptions on the page. |
| Primary source 2 | [Joint Director (Agriculture), Namakkal — official district directory](https://namakkal.nic.in/directory/joint-director-agriculturenamakkal/) lists the role on a page owned by the Namakkal District Administration and showed a last-updated date of 18 August 2026 when reviewed. The directory page itself displayed no substantive operational detail. |
| Narrow conclusion | The official district site confirms a current public Agriculture Department page and a current directory listing for the Joint Director role. The page is a revalidation source for what it states, but its figures should be cited with the page/date and should not be generalized beyond its stated district context or treated as independent proof of farmer demand, product need, or intervention effect. |
| Evidence Atlas treatment | `needs_revalidation` for time-sensitive local facts; `supported_inference` only for the bounded statement that the official page presents the listed information and services. |

## RV-003 — Agricultural Market Price and Arrival Information

| Field | Recorded finding |
|---|---|
| Revalidation status | Partially completed: the official portal’s public information scope and report filters were verified. No API, licensing, use-case mapping, data-quality audit, or product integration was attempted. |
| Primary source 1 | [AGMARKNET 2.0](https://agmarknet.gov.in/home) identifies the Government of India’s Department of Agriculture & Farmers Welfare and Directorate of Marketing & Inspection. When reviewed, its landing page displayed a daily price-and-arrival report date, market-wise price/arrival access, crop-season-wise price/arrival access, and filters for State/UT, district, market, commodity group, commodity, variety, and grade. The page also displayed a data-freeze notice. |
| Primary source 2 | [AGMARKNET Daily Price and Arrival Report](https://agmarknet.gov.in/daily-price-and-arrival-report) presents a report workflow with required selection fields for price/arrivals, commodity group, commodity, and State/UT, together with district and market filters. A CAPTCHA-gated retrieval interaction was present when reviewed. |
| Narrow conclusion | AGMARKNET publicly presents a government market-information portal containing price-and-arrival reporting with geographic, commodity, variety, and grade-related selection context. This does not establish that the data is complete, real-time in the product sense, available through a suitable integration route, semantically comparable across markets, or appropriate for an EcoFarm recommendation or price forecast. |
| Evidence Atlas treatment | `needs_revalidation` and `candidate_input`: every use must preserve commodity, variety/grade, market, unit, date/freeze/update state, and the distinction between price/arrival fields. |

## RV-004 — Selected High-Impact Global Context Claims

| Historical claim family | Primary-source finding | Narrow conclusion and boundary |
|---|---|---|
| Plant pests and diseases cause material global crop losses. | [FAO — Plant Production and Protection](https://www.fao.org/plant-production-protection/about/en) states: “Every year, up to 40 percent of global crop production is lost due to plant pests and diseases.” The page frames this as a global plant-production/plant-health statement. | The statement supports the bounded global-context claim. It does **not** quantify loss for India, Tamil Nadu, Namakkal, a crop, a season, or a farmer population; it does not validate EcoFarm disease/pest features. |
| Agriculture is the largest category of global freshwater withdrawal. | [FAO AQUASTAT — Water use](https://www.fao.org/aquastat/en/overview/methodology/water-use/) defines its withdrawal categories and states global ratios of 69% agricultural, 12% municipal, and 19% industrial. It cautions that global figures are strongly influenced by countries with very high withdrawals and states that ratios vary substantially by region. | The official source supports a global, method-bounded withdrawal-context statement. It should not be restated as local irrigation demand, water consumption, crop water need, efficiency loss, or a Namakkal-specific fact. |
| Remaining high-impact historical statistical claims | The reviewed archive contains additional historical claims about climate, soil degradation, farmer economics, adoption, inputs, and environmental impacts. | Each remains `needs_revalidation` until it is linked to a specific current primary institutional or peer-reviewed source with its date, method, geography, and population scope recorded. No repeated secondary citation raises its evidence strength. |
