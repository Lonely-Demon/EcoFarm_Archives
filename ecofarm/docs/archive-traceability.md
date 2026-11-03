# Archive → code traceability

This file records which archive decision governs which piece of code, and where
this build is deliberately weaker than the archive's specification. It exists so
a future engineer can reopen a decision rather than inherit a mystery.

Archive repository: `Lonely-Demon/EcoFarm_Archives`.

## 1. Scope

| Archive | Rule | Code |
|---|---|---|
| `EF-DAT-005` §1 | P0 is one sowing / early-establishment decision packet for Namakkal/Kongu | `POST /api/v1/decisions`, all of `engine/` |
| `EF-DAT-006` pre-build gate | Narrow build only after consent, deletion, source-log, suppression and referral controls exist | `core/storage.py`, `api/decisions.py`, `engine/packet.py` |
| `EF-PRD-002` | Broad MVP (marketplace, community, sensors) | **Not built.** Deferred by the later P0 decision. |

## 2. Sources

| Archive | Rule | Code |
|---|---|---|
| `EF-DAT-007` §3 | TNAU district bulletin rejected: Namakkal not covered, rights unclear | `sources.yaml` `tnau_agromet_district` → `rejected_locality`; `weather_gate.py` |
| `EF-DAT-005` §2 | IMD API requires credentials → permission-dependent, no retry loop | `sources.yaml` `imd_api` → `blocked_permission` |
| `EF-DAT-005` §2 | Agmarknet untested → excluded from P0 | `sources.yaml` `agmarknet_market` → `not_tested` |
| `EF-DAT-006` guidance row | TNAU Crop Production Guide is manual-reference only, never transformed | `score_*` never parses it; shown as `guidance` citation only |
| `EF-DAT-011` | Source register with limitation/use status | `sources.yaml` mirrors it; `GET /api/v1/sources` |
| `EF-DAT-007` §6 | Eight fail-closed states must be implemented | see §4 below |

## 3. Consent, retention, deletion

| Archive | Rule | Code |
|---|---|---|
| `EF-DAT-003` | Purpose-specific consent before a decision record exists | `consent_granted` required; 403 `consent_required` |
| `EF-DAT-003` | 90-day retention default | `RETENTION_DAYS = 90`; `retention` block in every packet |
| `EF-DAT-003` | Deletion route; source audit may outlive the record | `DELETE /api/v1/decisions/{id}`; `audit_events` holds no farmer context |
| `EF-DAT-003` | Do not infer language | `language` is an explicit field, no detection |
| `EF-DAT-003` §minimum | Required fields: block, crop stage, window, objective (+ water for comparison) | `DecisionRequest` required fields |

## 4. Fail-closed states

Archive states (from `EF-DAT-016` simulated records) mapped to implementation:

| Archive state | Implementation |
|---|---|
| `stale` | No cached packet is ever served; server render fails closed |
| `empty` | No market data shown at all (`market_price` excluded) |
| `malformed` | Pydantic validation rejects; API returns 422 |
| `unauthorized` | `blocked_permission` sources cannot reach scoring |
| `geography_mismatch` | Non-Namakkal block → 422 `outside_tested_scope` |
| `semantic_mismatch` | Market excluded entirely rather than compared |
| `conflict` | No second weather source exists, so no silent merge is possible |
| `transformation_unverified` | TNAU guidance shown as `reference_only`; never computed on |

## 5. Referrals

| Archive | Rule | Code |
|---|---|---|
| `EF-DAT-009` | Neutral public contact info, no partnership implied | `blocks.yaml` `neutral_notice`, printed on every referral |
| `EF-DAT-009` | Record trigger, wording, verification date | `ReferralEntry` |
| `EF-DAT-009` | Never claim a response or acceptance | no such field exists |
| `EF-DAT-015` | Block AEC contacts and JDA office | `blocks.yaml` |
| `EF-DAT-007` §4 | KVK Namakkal contact | `blocks.yaml` `kvk` |

## 6. Agricultural content

| Archive | Rule | Code |
|---|---|---|
| `EF-DAT-015` | Major Namakkal crops: paddy, sorghum, groundnut, green gram, black gram, maize, cotton, sugarcane | `crops.yaml` (plus pearl millet, cowpea, tapioca as locally notable) |
| `EF-DAT-015` | Red soil ~77%, pH 5.2–8.7, 716.54 mm normal rainfall | `blocks.yaml` district block; shown as district context, never as plot data |
| `EF-FLD-019` | Rainfed groundnut establishment is a research hypothesis, not a validated advantage | `objective_notes.risk_reduction` says so explicitly |
| `EF-DAT-006` | EC cannot be converted into a fertilizer prescription | no EC input, no nutrient output anywhere |

## 7. Where this build is weaker than the archive requires

Recorded honestly rather than silently:

1. **Agronomist review (blocking).** `crops.yaml` is `unreviewed_pending_agronomist`.
   `EF-DAT-006`'s "guidance reference: reviewer identity" row cannot be satisfied
   until a named reviewer signs each crop.
2. **Tamil first (blocking).** The archive requires a Tamil input/comprehension
   test before field use. The API carries `ta`; the UI is English only.
3. **Human reviewer console (blocking for P0).** `EF-DAT-009` requires a person
   able to suppress an output and record a reason. Automatic fail-closed states
   exist; a reviewer workflow does not.
4. **Directory re-verification.** `verified_on: 2026-08-13` with a 180-day
   interval. `is_stale` is computed and surfaced, but no scheduled job enforces
   recheck or removes stale entries.
5. **Evaluation loop.** `farmer_response` is stored; the weekly evidence register
   described in `EF-FLD-017` is not built.
6. **Scope guard is a block list.** A Namakkal block list prevents cross-district
   generalisation. It does not stop a block-level result being read as
   plot-level advice — only wording and the referral path mitigate that.

## 8. Deliberate non-features

Absent on purpose, with the governing line:

- Weather-derived sowing prompt — `EF-DAT-005` §1: no source passed.
- Market price card — `EF-DAT-005` §1: raw observation only, and no semantic
  test exists; so it is omitted rather than shown.
- Pest/disease diagnosis — `EF-DAT-009`: "a text or image description is not
  enough to safely identify this problem or prescribe treatment".
- Irrigation actuation — `EF-DAT-005` §4: hardware actuation prohibited in P0.
- Profit ranking — `EF-DAT-009`: no price or profit prophecy, permanent.
