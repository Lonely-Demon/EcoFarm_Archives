#!/usr/bin/env python3
"""Add the Evidence Atlas to the existing static EcoFarm knowledge site."""

import json
from pathlib import Path

SITE = Path('/home/ubuntu/ecofarm_knowledge_html')
GITHUB = 'https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/10_knowledge_base_outputs/evidence_atlas/'
NAV_LINK = '<a class="" href="evidence-atlas.html">Evidence Atlas</a>'
ACTIVE_NAV_LINK = '<a class="active" href="evidence-atlas.html">Evidence Atlas</a>'

PAGE = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Evidence Atlas — EcoFarm Knowledge Base</title><link rel="stylesheet" href="styles.css"></head><body><div class="shell"><aside><p class="brand">EcoFarm</p><p class="sub">Master Knowledge Base<br>Human-readable HTML edition</p><input id="knowledge-search" class="search" placeholder="Search concepts, features, evidence…" oninput="searchKnowledge()"><div id="search-results" class="search-results"></div><p class="nav-title">Navigate</p><nav><a class="" href="index.html">Knowledge Base Home</a>
<a class="" href="table-of-contents.html">Table of Contents</a>
<a class="" href="1-how-to-use-this-knowledge-base.html">1. How to use this knowledge base</a>
<a class="" href="2-ecofarm-s-mental-universe.html">2. EcoFarm’s mental universe</a>
<a class="" href="3-historical-evolution-of-the-ecofarm-thesis.html">3. Historical evolution of the EcoFarm thesis</a>
<a class="" href="4-problem-landscape-and-research-knowledge.html">4. Problem landscape and research knowledge</a>
<a class="" href="5-conceptual-system-models.html">5. Conceptual system models</a>
<a class="" href="6-feature-and-capability-dossiers.html">6. Feature and capability dossiers</a>
<a class="" href="7-technical-and-data-system-archive.html">7. Technical and data-system archive</a>
<a class="" href="8-trust-safety-consent-and-governance.html">8. Trust, safety, consent, and governance</a>
<a class="" href="9-field-validation-and-operating-memory.html">9. Field validation and operating memory</a>
<a class="" href="10-current-working-map-without-forced-finality.html">10. Current working map without forced finality</a>
<a class="" href="11-commercial-and-investor-material-as-secondary-archive.html">11. Commercial and investor material as secondary archive</a>
<a class="" href="12-knowledge-registers-and-appendices.html">12. Knowledge registers and appendices</a>
<a class="" href="reference-sources-for-the-current-field-p0-evidence.html">Reference sources for the current field/P0 evidence</a>
{ACTIVE_NAV_LINK}
<a class="" href="sources.html">Source Catalogue</a></nav><p class="nav-title">Reading rule</p><p class="sub">Treat historical visions, plans, test artifacts, and external pages according to their stated evidence status. Do not mistake a proposal for validation.</p></aside><main><section class="hero"><p class="breadcrumb" style="color:#c6d7c7">Traceable · Non-final · Evidence-bound</p><h1>EcoFarm Evidence Atlas</h1><p>A source-to-claim navigation layer built only after individual full-file review of the complete curated source set.</p></section><blockquote><p><strong>Atlas rule:</strong> A source’s inclusion does not increase its authority. Read every record with its evidence label, scope, limitation, relationship links, and current-use designation.</p></blockquote><h2>Review completion</h2><table><thead><tr><th>Measure</th><th>Status</th><th>Meaning</th></tr></thead><tbody><tr><td>Canonical sources individually reviewed</td><td><strong>113 / 113</strong></td><td>Every curated source was read in full before trace mapping.</td></tr><tr><td>Source review coverage records</td><td><strong>113</strong></td><td>One stable <code>EVA-SRC-*</code> record per canonical source.</td></tr><tr><td>Cross-source core traces</td><td><strong>23</strong></td><td>Constraints, historical intent, assumptions, contradictions, and open questions.</td></tr><tr><td>Feature evidence families</td><td><strong>12</strong></td><td>Historical features linked to field/P0/data qualifications.</td></tr></tbody></table><h2>Evidence labels</h2><div class="cards"><div class="card"><h3>Historical intent</h3><p>What the archive says EcoFarm previously imagined, preferred, or designed. It is not implementation proof.</p></div><div class="card"><h3>Research design only</h3><p>A method, interview guide, consent pack, or test plan. It does not demonstrate a result.</p></div><div class="card"><h3>Supported inference</h3><p>A bounded conclusion from a scoped study or test whose limitation must remain visible.</p></div><div class="card"><h3>Needs revalidation</h3><p>A dynamic, dated, external, institutional, or quantitative assertion that requires a fresh primary source for current use.</p></div></div><h2>Navigate the Atlas</h2><table><thead><tr><th>Layer</th><th>What it answers</th><th>Access</th></tr></thead><tbody><tr><td>Human-readable Atlas</td><td>How evidence is classified, what it supports, and what stays uncertain.</td><td><a href="{GITHUB}EcoFarm_Evidence_Atlas.md">Read the Evidence Atlas</a></td></tr><tr><td>Review-completion record</td><td>How the full-file review requirement was satisfied before synthesis.</td><td><a href="{GITHUB}full_file_review/EcoFarm_Full_File_Review_Completion_Record.md">Open completion record</a></td></tr><tr><td>Source-family reconciliation</td><td>How the ten source families relate and which kinds of evidence they can establish.</td><td><a href="{GITHUB}EcoFarm_Source_Family_Reconciliation.md">Open reconciliation</a></td></tr><tr><td>Atomic source coverage</td><td>Stable review-based record for all 113 sources, including GitHub source links and limitations.</td><td><a href="{GITHUB}EVA_Source_Review_Records.jsonl">Open source-review dataset</a></td></tr><tr><td>Core trace map</td><td>Cross-source constraints, historical intent, contradictions, and open questions.</td><td><a href="{GITHUB}EVA_Core_Trace_Records.jsonl">Open core traces</a></td></tr><tr><td>Feature evidence map</td><td>Historical feature intentions paired with dependencies and evidence boundaries.</td><td><a href="{GITHUB}EVA_Feature_Evidence_Map.json">Open feature map</a></td></tr><tr><td>Claim and assumption maps</td><td>Claim source sets, revalidation priorities, historical decisions, and exposed assumptions.</td><td><a href="{GITHUB}EVA_Claim_Source_Map.json">Claims</a> · <a href="{GITHUB}EVA_Decision_Assumption_Map.json">Assumptions</a></td></tr><tr><td>Open questions and revalidation</td><td>Preserved tensions, primary-source checks, and the remaining evidence gap.</td><td><a href="{GITHUB}EVA_Contradiction_Open_Question_Register.json">Questions</a> · <a href="{GITHUB}EVA_Revalidation_Findings.md">Findings</a></td></tr></tbody></table><h2>What the Atlas does not conclude</h2><p>The Atlas does not determine a target farmer, crop, locality, first product wedge, current technology stack, sensor selection, safety case, data-source integration, market demand, revenue model, or investor thesis. It keeps the evidence and its limits legible so those decisions can be made later with disciplined new validation.</p><h2>Current primary-source checks</h2><p>The Atlas has rechecked the public existence and stated scope of selected official IMD, Namakkal District, AGMARKNET, and FAO pages. Those checks establish only the narrow statements recorded in the <a href="{GITHUB}EVA_Revalidation_Findings.md">revalidation findings</a>; they do not validate an EcoFarm feature or claim a data source is universally usable.</p><p class="meta">Evidence Atlas · Generated after source-level full-file review · Public sources resolve through the EcoFarm GitHub archive.</p></main></div><script src="search.js?v=20260819a"></script></body></html>'''

PAGE = PAGE.replace('113 / 113', '114 / 114').replace('>113</strong></td><td>One stable <code>EVA-SRC-*</code>', '>114</strong></td><td>One stable <code>EVA-SRC-*</code>').replace('all 113 sources, including GitHub source links and limitations.', 'all 114 sources, including GitHub source links and limitations.')
PAGE = PAGE.replace('<h2>Evidence labels</h2>', '<h2>Preferred sensor-research sources</h2><p><code>EF-TEC-005</code> is the preferred parseable Markdown record for the historical Grok sensor-research conversation. Earlier FireShot PDF/text captures remain stale/deprecated provenance aliases, not normal retrieval sources. <code>EF-TEC-007</code> is a complementary alternatives-and-selection-criteria record. Neither source proves current component suitability, price, compliance, calibration, safety, or field performance.</p><h2>Evidence labels</h2>', 1)
(SITE / 'evidence-atlas.html').write_text(PAGE, encoding='utf-8')

for path in SITE.glob('*.html'):
    if path.name == 'evidence-atlas.html':
        continue
    content = path.read_text(encoding='utf-8')
    if 'href="evidence-atlas.html"' not in content:
        content = content.replace('<a class="" href="sources.html">Source Catalogue</a>', NAV_LINK + '\n<a class="" href="sources.html">Source Catalogue</a>')
        content = content.replace('<a class="active" href="sources.html">Source Catalogue</a>', NAV_LINK + '\n<a class="active" href="sources.html">Source Catalogue</a>')
    if path.name == 'index.html' and 'href="evidence-atlas.html"><h3>Evidence Atlas</h3>' not in content:
        marker = '</div><p class="meta">EcoFarm Master Knowledge Base'
        card = '<a class="card" href="evidence-atlas.html"><h3>Evidence Atlas</h3><p>Evidence labels, completed source reviews, source relationships, feature/claim maps, open questions, and revalidation boundaries.</p></a>'
        content = content.replace(marker, card + marker)
    path.write_text(content, encoding='utf-8')

search_path = SITE / 'search-index.json'
search_records = json.loads(search_path.read_text(encoding='utf-8'))
search_records = [record for record in search_records if record.get('file') != 'evidence-atlas.html']
search_records.append({
    'title': 'Evidence Atlas',
    'file': 'evidence-atlas.html',
    'excerpt': 'Source-level evidence navigation: full-file review completion, evidence labels, feature and claim trace maps, contradictions, open questions, and bounded primary-source revalidation.',
    'search_text': 'evidence atlas source trace claim source feature evidence map decision assumption contradiction open question revalidation full file review 113 canonical sources historical intent product hypothesis research design supported inference needs revalidation provenance p0 field validation safety weather market namakkal agmarknet imd fao'
})
search_records[-1]['search_text'] = 'evidence atlas source trace claim source feature evidence map decision assumption contradiction open question revalidation full file review 114 canonical sources preferred parseable Markdown sensor research EF-TEC-005 EF-TEC-007 FireShot deprecated provenance historical intent product hypothesis research design supported inference needs revalidation provenance p0 field validation safety weather market namakkal agmarknet imd fao'
search_path.write_text(json.dumps(search_records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Evidence Atlas HTML page, navigation, and search index updated.')
