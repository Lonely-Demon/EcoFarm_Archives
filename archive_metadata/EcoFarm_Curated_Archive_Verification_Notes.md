# Curated Archive Verification Notes

| Check | Result | Follow-up |
|---|---|---|
| Published canonical GitHub file | `EF-FLD-001` opened successfully from `Lonely-Demon/EcoFarm_Archives`, displaying the intended Farmer-Problem Research Report. | GitHub source-link pattern verified. |
| Curated HTML catalogue | Live local HTML catalogue displayed category-aware `EF-*` records and no workspace-code/dependency entries in the primary browse view. | Confirmed the curated catalogue intent. |
| Build freshness | The live local HTML view still showed an earlier `EF-TEC-006` duplicate after the curatorial source definition had been corrected. | Regenerate HTML, rebuild the curated archive, re-run sanitization/audit, then amend the GitHub repository. |
| Explicit category filters | Regenerated catalogue visibly exposed `All sources` plus one control for each `EF-*` category; no workspace-code category was present. | Complete a fresh-session click test after the browser tab reference expired. |
| Filter interaction | In a fresh browser session, selecting `EF-FLD` hid all unrelated source groups and displayed only the 17 curated farmer-decision and field-validation records. | Category filter behavior verified. |

The duplicate is a build freshness issue, not a retained canonical-record decision. The category definition contains only five `EF-TEC` canonical records after the correction.
