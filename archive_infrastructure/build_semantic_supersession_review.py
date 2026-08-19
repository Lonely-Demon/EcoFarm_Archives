from pathlib import Path
import json
import re
from collections import defaultdict

ROOT = Path('/home/ubuntu/ecofarm_source_archive')
manifest = json.loads((ROOT / 'manifest' / 'EcoFarm_Source_Manifest.json').read_text())
OUT = ROOT / 'knowledge_mapping' / 'EcoFarm_Semantic_Supersession_Review.md'

EXPLICIT_SENSOR_RELATIONS = {
    'SRC-0025': 'Stale/deprecated FireShot PDF capture; retain only as historical provenance alias of preferred parseable Markdown record `SRC-0391`.',
    'SRC-0026': 'Stale/deprecated FireShot PDF capture; retain only as historical provenance alias of preferred parseable Markdown record `SRC-0391`.',
    'SRC-0029': 'Legacy text capture retained as provenance alias; preferred retrieval record is `SRC-0391`.',
    'SRC-0036': 'Legacy text capture retained as provenance alias; preferred retrieval record is `SRC-0391`.',
    'SRC-0391': 'Preferred parseable Markdown record for the historical Grok sensor-research conversation; supersedes FireShot/text captures for retrieval, not as current engineering authority.',
    'SRC-0392': 'Companion parseable Markdown record focused on sensor alternatives and selection constraints; preserve as complementary historical research, not current engineering authority.',
}

def family(record):
    group = record['source_group']
    path = record['relative_path'].lower()
    name = record['file_name'].lower()
    if group in {'current_session'} or 'market_research_export' in name or 'pasted_content_nnuv' in name:
        return '08 — Founder approvals, market-research export, and canonical current conversation'
    if group == 'research_agent_1':
        return '06 — Research Agent 1: farmer decision and field-validation work'
    if group == 'research_agent_2':
        return '07 — Research Agent 2: ecosystem, data, safety, and P0 work'
    if group == 'current_uploads':
        if any(term in name for term in ['sensor', 'hardware', 'grok-ecofarm-module']):
            return '03 — Sensor, hardware, and IoT research'
        if any(term in name for term in ['field', 'decision', 'claimledger', 'candidate', 'recruitment', 'event', 'household']):
            return '06 — Research Agent 1: farmer decision and field-validation work'
        if any(term in name for term in ['source', 'ecosystem', 'alternatives', 'p0', 'weather', 'referral', 'observability', 'imdagrimet', 'tnau_']):
            return '07 — Research Agent 2: ecosystem, data, safety, and P0 work'
    if group == 'project_shared_files':
        if Path(record['relative_path']).suffix.lower() in {'.png', '.jpg', '.jpeg', '.mov'}:
            return '09 — Historical visual, chart, mockup, and media assets'
        return '05 — Regional, agricultural-crisis, and microcosm research'
    if group == 'historical_task_ecofarm_1':
        if Path(record['relative_path']).suffix.lower() in {'.png', '.jpg', '.jpeg', '.mov'}:
            return '09 — Historical visual, chart, mockup, and media assets'
        if any(term in name for term in ['sensor', 'hardware']):
            return '03 — Sensor, hardware, and IoT research'
        if any(term in name for term in ['prd', 'mvp', 'tech_stack', 'ui_ux', 'wireframe']):
            return '02 — Early PRD, flows, UI logic, and technical-stack work'
        return '01 — Onboarding and founder-vision versions'
    if group in {'historical_task_ecofarm_1_2', 'historical_task_ecofarm_1_3', 'historical_task_ecofarm_1_3_later'}:
        if Path(record['relative_path']).suffix.lower() in {'.png', '.jpg', '.jpeg', '.mov'}:
            return '09 — Historical visual, chart, mockup, and media assets'
        if any(term in name for term in ['sensor', 'ai_farming_app']):
            return '03 — Sensor, hardware, and IoT research'
        return '01 — Onboarding and founder-vision versions'
    if group == 'historical_task_ecofarm_2':
        return '04 — Historical proposal, pitch, hackathon, and master-document material'
    if group == 'referenced_task_conversations':
        return '10 — Historical task conversations (contextual trace, not standalone current authority)'
    return '11 — Generated, webapp, manifest, or non-evidence artifact'

def relation(record):
    name = record['file_name'].lower()
    path = record['relative_path'].lower()
    if record['source_id'] in EXPLICIT_SENSOR_RELATIONS:
        return EXPLICIT_SENSOR_RELATIONS[record['source_id']]
    if record.get('duplicate_of'):
        return f"Exact duplicate of `{record['duplicate_of']}`; retain as provenance alias, not independent evidence."
    if 'revised' in name or 'operationalrevision' in name:
        return 'Likely later revision; content-level precedence must be set within this family.'
    if 'final' in name:
        return 'Likely final-labelled historical version; does not automatically govern later current work.'
    if re.search(r'\(1\)|_old|_new', name):
        return 'Variant copy/version; compare content and retain chronology.'
    if record['source_group'] == 'referenced_task_conversations':
        return 'Conversation trace; founder/user statements outrank assistant-synthesis statements for intent.'
    return 'Standalone or family member; determine role from document content and chronology.'

families = defaultdict(list)
for record in manifest:
    families[family(record)].append(record)

lines = ['# EcoFarm Semantic Supersession Review', '', '> This register separates exact duplicate detection from semantic supersession. A file may be byte-distinct yet semantically obsolete, complementary, or unresolved. No item is deleted; the register records its intended role.', '']
lines.append('## Governing interpretation rules')
lines.append('')
lines.extend([
    '1. Current founder approvals and direct operational evidence govern their stated scope over historical design narratives.',
    '2. A `revised`, `final`, or `operational revision` filename is a chronology clue, not enough evidence by itself to erase the predecessor.',
    '3. Historical documents preserve vision and conceptual mechanics even when they no longer govern P0 scope.',
    '4. Research plans and launch kits remain plans until an event/participant artifact records execution.',
    '5. Exact duplicates are preserved as aliases but not counted as independent support.',
    '',
])

family_status = {
    '01 — Onboarding and founder-vision versions': 'Historical vision sequence; later documents preserve broader detail while current P0 restrictions supersede only present-scope claims.',
    '02 — Early PRD, flows, UI logic, and technical-stack work': 'Historical product/technical design archive; use for conceptual mechanism, not current requirements or screen-level delivery.',
    '03 — Sensor, hardware, and IoT research': 'Historical engineering archive; keep alternatives and rationale, but require separate current feasibility and field-value work.',
    '04 — Historical proposal, pitch, hackathon, and master-document material': 'Historical commercial/innovation framing; secondary knowledge, not evidence of traction or present product scope.',
    '05 — Regional, agricultural-crisis, and microcosm research': 'Research/reference family; preserve source-level attribution and distinguish compiled/AI synthesis from primary data.',
    '06 — Research Agent 1: farmer decision and field-validation work': 'Current research-design family. Revised or governance variants can supersede prior forms procedurally, but none prove completed field validation without event records.',
    '07 — Research Agent 2: ecosystem, data, safety, and P0 work': 'Current feasibility/governance family. Direct test results govern their narrow tested path; later operational revisions govern the named P0 control, not all possible integrations.',
    '08 — Founder approvals, market-research export, and canonical current conversation': 'Current governing intent for knowledge-base format; market export is a mixed conversation record and must be read turn-by-turn.',
    '09 — Historical visual, chart, mockup, and media assets': 'Visual evidence/design archive; retain as references and index captions, not as current UI or statistical authority without underlying source check.',
    '10 — Historical task conversations (contextual trace, not standalone current authority)': 'Chronological rationale archive; source role depends on speaker and date, with later current approvals taking precedence for present work.',
    '11 — Generated, webapp, manifest, or non-evidence artifact': 'Do not use as EcoFarm domain evidence; retain only for system provenance or prior app-work history.',
}

for name in sorted(families):
    rows = sorted(families[name], key=lambda r: r['source_id'])
    lines.extend([f'## {name}', '', f'**Family-level disposition:** {family_status.get(name, "Requires source-by-source review.")}', '', '| Source ID | Artifact | Source group | File relation / required treatment |', '|---|---|---|---|'])
    for r in rows:
        lines.append(f"| `{r['source_id']}` | `{r['relative_path']}` | `{r['source_group']}` | {relation(r)} |")
    lines.append('')

OUT.write_text('\n'.join(lines))
print(json.dumps({'families': len(families), 'sources': len(manifest), 'output': str(OUT)}, indent=2))
