from pathlib import Path
import json
import re

ARCHIVE = Path('/home/ubuntu/ecofarm_source_archive')
CURATED = Path('/home/ubuntu/ecofarm_curated_archive')
MANIFEST = json.loads((ARCHIVE / 'manifest' / 'EcoFarm_Source_Manifest.json').read_text())
INDEX = json.loads((CURATED / 'archive_metadata' / 'curated_source_index.json').read_text())
OUT = ARCHIVE / 'knowledge_mapping' / 'EcoFarm_Content_Based_Curation_Review_Register.md'

canonical = {}
for item in INDEX:
    for legacy in item['legacy_source_ids']:
        canonical.setdefault(legacy, item)

def treatment(record):
    source_id = record['source_id']
    name = record['file_name'].lower()
    path = record['relative_path'].lower()
    group = record['source_group']
    if source_id in canonical:
        item = canonical[source_id]
        if source_id == item['source_id']:
            return 'CURATED CANONICAL', f"Reviewed as substantive. Canonical record is `{item['curated_id']}` in `{item['category_directory']}`: {item['role']}"
        return 'ALIAS / SEMANTIC FAMILY', f"Not copied as an independent primary record. Resolve through canonical `{item['curated_id']}` (`{item['title']}`), retaining legacy trace in the crosswalk."
    if group == 'webapp_project':
        return 'ARCHIVAL-ONLY CODE / GENERATED APP', 'EcoFarm pilot/task-tracker application source, dependency/configuration, framework component, build output, or generic UI code. Not EcoFarm domain evidence; excluded from public evidence browse.'
    if group == 'manifest':
        return 'ARCHIVE METADATA', 'Preservation-manifest artifact. Replaced in public browsing by the curated index, legacy crosswalk, and curation review register.'
    if group == 'referenced_task_conversations':
        return 'CONTEXT TRACE ONLY', 'Historical conversation trace. Preserved in the private corpus; not an ordinary public evidence record because direct founder documents and current approvals are more precise sources of intent.'
    if group == 'research_agent_1' and (name in {'skill.md', 'config.json'} or name.endswith('.py')):
        return 'ARCHIVE INFRASTRUCTURE / AGENT CONFIG', 'Agent instruction, configuration, or helper script; not independent EcoFarm research evidence.'
    if group == 'research_agent_2' and name.endswith('.jsonl'):
        return 'TEST SUPPORT ARTIFACT', 'Underlying simulated-failure/event support artifact is represented by the curated observability/source-control record; retained privately for audit.'
    if group == 'current_uploads' and '3000-' in name:
        return 'GENERATED SITE CAPTURE', 'Snapshot of an earlier task-board web page; unrelated to the knowledge archive and excluded.'
    if group == 'current_uploads' and 'pasted_content' in name:
        return 'CONVERSATION EXCERPT / SUPERSEDED CONTEXT', 'Fragmentary pasted conversation context. Current-session approval captures and the market-research export are the retained governing records.'
    if group == 'project_shared_files' and name.startswith(('chatgpt', 'gemini', 'gemni', 'mistral', 'grok', 'lutra', 'futurehouse', 'my report')):
        return 'SECONDARY SYNTHESIS', 'AI-generated or compiled secondary problem synthesis. Themes were reviewed, but it is not treated as a canonical evidence source when stronger consolidated/cited records are retained.'
    if group == 'project_shared_files' and record['extension'].lower() in {'.png', '.jpg', '.jpeg'}:
        return 'HISTORICAL COMMUNICATION ASSET', 'Chart or visual communication artifact. Retained only where selected as a representative historical design/research asset; otherwise its underlying statistic requires primary-source revalidation before reuse.'
    if group.startswith('historical_task') and any(term in name for term in ['ui_ux', 'wireframe', 'slide', 'blank_', 'content.pdf']):
        return 'HISTORICAL DESIGN DETAIL', 'Useful for historical reference but not copied as an independent primary record because the master archive retains the conceptual workflow/design logic and selected representative visual assets.'
    if group.startswith('historical_task') and name.endswith(('.html', '.pdf')):
        return 'HISTORICAL PRESENTATION / FORMAT VARIANT', 'Historical presentation, pitch-page, or alternate file format. Its substantive concepts are retained through selected onboarding, PRD, technical-master, or design/pitch records.'
    if 'irrelevant' in name:
        return 'EXPLICITLY IRRELEVANT / ARCHIVE ONLY', 'The source itself labels the material as archival/irrelevant; retained only in private preservation for traceability.'
    if group in {'research_agent_1', 'research_agent_2', 'current_uploads'}:
        return 'SUPPORTING / SUPERSEDED WORKING ARTIFACT', 'A supporting note, earlier instrument, duplicate upload, or bounded artifact whose substantive contribution is represented by a reviewed canonical report, revised instrument, or P0 control record.'
    return 'SECONDARY / ARCHIVE ONLY', 'Reviewed at source-family level as non-canonical, redundant, incomplete, low-signal, or already represented by a more complete selected record. Retained in private preservation and traceable through the legacy manifest.'

family_rules = [
    ('Founder vision and onboarding', 'Canonical long-form/later onboarding documents retained; format copies and partial variants are aliases or historical-context records.'),
    ('Product, technical, and design work', 'Feature mechanics, PRD, selected flows, stack rationale, sensor research, and representative design media retained. Framework/app code and screen-level implementation detail are not evidence.'),
    ('National, global, and regional research', 'Cited/consolidated reports and region-specific analyses retained. Repetitive AI-generated summaries are secondary synthesis; charts are historical communication assets unless underlying data is separately verified.'),
    ('Research Agent 1 and current uploads', 'Current/revised farmer-decision, consent, field-method, and evidence-governance documents retained. Agent configuration, helper code, duplicates, and superseded instruments are demoted.'),
    ('Research Agent 2 and P0 feasibility', 'Current data-source, safety, provenance, referral, and direct-test artifacts retained. Supporting test traces and duplicate copies are mapped to the governing P0 source record.'),
    ('Conversations and workspace files', 'Current founder approvals and a selected historical trace retained for chronology. Raw conversation logs and task-tracker code remain private/contextual and never appear as ordinary catalogue evidence.'),
]

lines = ['# Content-Based Curation Review Register', '', '> This register records the treatment decision for every preserved legacy source. It is the answer to “why is this file here, or why is it not in the primary catalogue?” The decision is based on source purpose, title, normalized content role, duplicate relationship, and the user’s direction to prioritize meaningful knowledge over workspace noise.', '', '## Family-level review decisions', '', '| Source family | Decision |', '|---|---|']
for family, decision in family_rules:
    lines.append(f'| {family} | {decision} |')
lines.extend(['', '## Per-source decisions', '', '| Legacy ID | Original artifact | Source group | Treatment | Reason / canonical resolution |', '|---|---|---|---|---|'])
for record in MANIFEST:
    status, rationale = treatment(record)
    lines.append(f"| `{record['source_id']}` | `{record['relative_path']}` | `{record['source_group']}` | **{status}** | {rationale} |")
OUT.write_text('\n'.join(lines))
print(json.dumps({'legacy_sources_reviewed': len(MANIFEST), 'canonical_records': len(INDEX), 'output': str(OUT)}, indent=2))
