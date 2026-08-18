# EcoFarm HTML Knowledge Site — Usability Checks

| Check | Method | Result | Follow-up |
|---|---|---|---|
| Home-page rendering | Opened the live static site in a browser at desktop viewport. | **Pass.** The hero, visual hierarchy, left navigation, article cards, and main introduction rendered legibly. | None. |
| Navigation availability | Inspected sidebar links generated from the Markdown master headings. | **Pass.** The home page exposed linked section/subpage navigation. | Verify one section link after regenerated site. |
| Search control | Queried `weather source hierarchy`. The static index contains matching technical-archive and appendix pages. | **Pass after correction.** The live site returned both the technical-archive and appendix pages, with a visible excerpt. | Token-based retrieval, cache-disabled index fetch, and versioned script URL retained. |
| Section-page navigation and rendering | Opened the technical-and-data-system archive from the sidebar after confirming search results. | **Pass.** The dedicated subpage loaded at its own URL, retained global navigation, and rendered the heading, explanatory prose, and wide technical tables legibly. | None. |
| Source-linked access | Opened `sources.html#SRC-0039` from the generated source-resolution path and expanded the record. | **Pass.** The source catalogue scrolled to the requested record and exposed archive path, source group, duplicate/representation state, and canonical LLM-corpus source ID. | Internal source citations now resolve to this provenance catalogue; raw source files remain in the preserved archive. |
| Responsive layout | CSS includes a mobile breakpoint that changes the fixed/sidebar layout into a document-first layout. | **Code-level pass; browser mobile spot check still required after regeneration.** | Run a browser mobile-viewport check. |
| Source-linked reading | HTML labels internal source IDs and explains their manifest/LLM-corpus resolution path. | **Pass at page level.** Direct source-detail links remain intentionally archive-based rather than generated per source. | Retain source-map and LLM-corpus files in the final package. |

## Interpretation

The first live check found a functional, legible document site rather than a visual mockup. The only interaction defect observed was search strictness, which has been corrected in the generator. Further checks must verify the regenerated search result, a section page, and the mobile breakpoint before final packaging.
