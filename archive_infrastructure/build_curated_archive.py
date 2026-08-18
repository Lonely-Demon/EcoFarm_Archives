from pathlib import Path
from collections import defaultdict
import csv
import json
import re
import shutil

ARCHIVE = Path('/home/ubuntu/ecofarm_source_archive')
OUT = Path('/home/ubuntu/ecofarm_curated_archive')
GITHUB_REPOSITORY = 'Lonely-Demon/EcoFarm_Archives'
GITHUB_BRANCH = 'main'
MANIFEST = json.loads((ARCHIVE / 'manifest' / 'EcoFarm_Source_Manifest.json').read_text())
BY_ID = {record['source_id']: record for record in MANIFEST}
BY_HASH = defaultdict(list)
for record in MANIFEST:
    BY_HASH[record['sha256']].append(record['source_id'])

# Content-level aliases supplement exact-hash duplicate tracking. They are reviewed as repeated
# sensor-research captures with the same conceptual coverage, not silently discarded.
SEMANTIC_ALIASES = {
    'SRC-0025': ['SRC-0026', 'SRC-0029', 'SRC-0036'],
}

# Every entry below has been included because its title, source role, and normalized content were reviewed as material to EcoFarm's knowledge, history, research, feature mechanics, safety, or validation work.
CATEGORY_SPECS = [
    ('EF-GOV', '00_governance_and_archive', [
        ('SRC-0134', 'Current main conversation canonical capture', 'Current founder instructions, corrections, and requirements'),
        ('SRC-0135', 'Current session approvals and requirements', 'Current governing approval record'),
        ('SRC-0289', 'Master document reworked architecture', 'Knowledge-base architecture decision record'),
        ('SRC-0130', 'Historical EcoFarm 1 conversation trace', 'Historical founder/assistant project-development context; browse as trace, not as present authority'),
    ]),
    ('EF-VSN', '01_founder_vision_and_evolution', [
        ('SRC-0039', 'Extended EcoFarm onboarding document', 'Richest preserved historical founder vision and feature mechanics'),
        ('SRC-0040', 'Later concise EcoFarm onboarding document', 'Later historical framing and scope orientation'),
        ('SRC-0037', 'EcoFarm onboarding document outline', 'Historical structure and evolution reference'),
    ]),
    ('EF-PRD', '02_product_concept_and_feature_mechanics', [
        ('SRC-0006', 'Historical product requirements document', 'Feature intent, roles, workflows, and capability relationships'),
        ('SRC-0005', 'MVP user flows and key screens outline', 'Historical interaction and decision-flow logic'),
        ('SRC-0023', 'Low-fidelity wireframes part 1', 'Historical workflow/concept reference'),
        ('SRC-0024', 'Low-fidelity wireframes part 2', 'Historical workflow/concept reference'),
        ('SRC-0027', 'AI farming application content', 'Historical capability and farmer-need model'),
        ('SRC-0304', 'MVP considerations and trade-offs', 'Historical feature sequencing rationale'),
        ('SRC-0312', 'Proposed API and software-focused MVP feature list', 'Historical software-first scope reference'),
    ]),
    ('EF-TEC', '03_technical_architecture_hardware_ai', [
        ('SRC-0008', 'Technology stack alternatives and trade-offs', 'Historical technology-choice rationale'),
        ('SRC-0010', 'Proposed technology stack', 'Historical system-stack proposal'),
        ('SRC-0011', 'AI integration and data-source capabilities', 'Historical intelligence/data architecture rationale'),
        ('SRC-0015', 'Cloud hosting and scalability research', 'Historical deployment and scale considerations'),
        ('SRC-0025', 'Sensor research source capture', 'Historical sensor capability and trade-off research'),
    ]),
    ('EF-AGR', '04_india_agriculture_problem_research', [
        ('SRC-0277', 'Unified agricultural crisis document with citations', 'India-wide agricultural-problem research synthesis'),
        ('SRC-0288', 'EcoFarm-relevant agricultural crisis analysis', 'Problem-to-EcoFarm relevance synthesis'),
        ('SRC-0291', 'Farmer suicides and deepening distress', 'Historical distress and structural-risk context'),
        ('SRC-0298', 'India national agriculture crisis', 'India-wide farmer-problem context'),
        ('SRC-0299', 'Indian agriculture comprehensive report', 'National structural context'),
        ('SRC-0311', 'Global farmer problems with India focus', 'Global comparison and India context'),
    ]),
    ('EF-REG', '05_regional_microcosm_and_namakkal_research', [
        ('SRC-0274', 'All agricultural microcosms detailed profiles', 'Comparative regional-entry research'),
        ('SRC-0285', 'Kongu versus Punjab operational difficulties', 'Comparative operational research'),
        ('SRC-0286', 'Comparative microcosm analysis and recommendation', 'Entry-location reasoning'),
        ('SRC-0300', 'Kongu Belt operational difficulties', 'Regional farmer operating context'),
        ('SRC-0301', 'Kongu Belt regional analysis', 'Namakkal/Kongu regional context'),
        ('SRC-0305', 'Microcosm research plan', 'Comparative regional research method'),
        ('SRC-0309', 'Namakkal and Kongu Belt agricultural problems', 'Target-area problem context'),
        ('SRC-0310', 'Operational difficulties research plan', 'Kongu/Punjab analysis method'),
        ('SRC-0314', 'Punjab operational difficulties', 'Comparator region context'),
        ('SRC-0315', 'Tamil Nadu agriculture-specific analysis', 'State-level operating context'),
    ]),
    ('EF-MKT', '06_market_commercial_and_ecosystem_research', [
        ('SRC-0382', 'Market research conversation export', 'Founder-market research and strategic reasoning record'),
        ('SRC-0340', 'Alternatives behavioural verification addendum', 'Alternative/workaround validation method'),
        ('SRC-0341', 'Alternatives matrix', 'Existing alternative and substitute map'),
        ('SRC-0355', 'Ecosystem register', 'Institutional and ecosystem map'),
        ('SRC-0098', 'Market and risk infrastructure notes', 'Local market/risk evidence notes'),
        ('SRC-0099', 'Price, market, and weather-linked decision evidence', 'Decision context for market observations'),
        ('SRC-0123', 'Data feasibility and alternatives findings', 'Alternatives/source evidence synthesis'),
        ('SRC-0124', 'Local ecosystem findings', 'Local ecosystem evidence synthesis'),
    ]),
    ('EF-FLD', '07_farmer_decision_and_field_validation', [
        ('SRC-0357', 'Farmer problem research report', 'Current farmer-decision and field-validation synthesis'),
        ('SRC-0383', 'Candidate decision scoring', 'Candidate-wedge analytical reasoning'),
        ('SRC-0351', 'Decision journey tables', 'Farmer decision reconstruction model'),
        ('SRC-0352', 'Decision operationalization sheets', 'Named decision operationalization'),
        ('SRC-0347', 'Revised field-programme claim ledger', 'Evidence/claim governance for field work'),
        ('SRC-0342', 'Attribution and field-data quality protocol', 'Method for handling claims, outcomes, and evidence quality'),
        ('SRC-0359', 'Revised field interview guide', 'Primary interview instrument'),
        ('SRC-0360', 'Field launch governance index', 'Field programme governing index'),
        ('SRC-0361', 'Field safety card', 'Safe field interaction guidance'),
        ('SRC-0362', 'Field selection memo', 'Sampling and locality rationale'),
        ('SRC-0363', 'Field and partner verification questions', 'Verification prompts'),
        ('SRC-0364', 'Household-authority follow-up', 'Decision-authority research instrument'),
        ('SRC-0372', 'Primary pilot cohort and decision authority protocol', 'Cohort and authority design'),
        ('SRC-0373', 'Recruitment and consent pack', 'Field-consent method'),
        ('SRC-0375', 'Seasonal event and observation map', 'Event timing model'),
        ('SRC-0376', 'Post-event follow-up', 'Outcome/follow-up instrument'),
        ('SRC-0381', 'Weekly event register and evidence dashboard', 'Field evidence tracking method'),
    ]),
    ('EF-DAT', '08_data_sources_safety_and_p0_feasibility', [
        ('SRC-0354', 'Ecosystem, data feasibility, alternatives, and delivery handoff', 'Current systems/data feasibility synthesis'),
        ('SRC-0365', 'P0 data-source register operational revision', 'Current P0 source-control record'),
        ('SRC-0366', 'P0 decision-packet data dictionary and consent map', 'Data/consent mechanics'),
        ('SRC-0367', 'P0 ecosystem register operational revision', 'Current P0 ecosystem-control record'),
        ('SRC-0368', 'P0 feasibility decision memo', 'Feasibility position and limits'),
        ('SRC-0369', 'P0 implementation-ready checklist', 'Implementation readiness gate'),
        ('SRC-0370', 'P0 operational test results memo', 'Direct test result and restriction record'),
        ('SRC-0371', 'P0 source operational-test plan', 'Source test method'),
        ('SRC-0374', 'Safe referral and escalation design', 'Escalation safety mechanics'),
        ('SRC-0377', 'Source-failure and provenance observability plan', 'Fail-closed/observability model'),
        ('SRC-0378', 'Source register', 'Source inventory and classification'),
        ('SRC-0379', 'Target-market semantics verification plan', 'Market-data semantic gate'),
        ('SRC-0380', 'Weather and advisory source hierarchy', 'Evidence hierarchy and source-use logic'),
        ('SRC-0384', 'IMD agricultural meteorology capture', 'External source reference'),
        ('SRC-0385', 'Namakkal Agriculture Department capture', 'External local-source reference'),
        ('SRC-0386', 'Observability simulated failure records', 'Failure-state test artifact'),
        ('SRC-0388', 'Referral directory verification', 'Referral directory test evidence'),
        ('SRC-0389', 'TNAU Agro-Met headers', 'P0 source-test evidence'),
        ('SRC-0390', 'TNAU weather test manifest', 'P0 source-test evidence'),
    ]),
    ('EF-DSN', '09_historical_design_pitch_and_media', [
        ('SRC-0003', 'Field overview high-fidelity mockup', 'Historical visual product concept'),
        ('SRC-0004', 'Home dashboard high-fidelity mockup', 'Historical visual product concept'),
        ('SRC-0001', 'Early AI farming UI video', 'Historical visual product concept'),
        ('SRC-0020', 'Field overview wireframe', 'Historical visual workflow concept'),
        ('SRC-0021', 'Home dashboard wireframe', 'Historical visual workflow concept'),
        ('SRC-0022', 'Marketplace feed wireframe', 'Historical visual workflow concept'),
        ('SRC-0043', 'SkyLabs TechPreneur pitch', 'Historical pitch framing'),
        ('SRC-0044', 'Smart Farming Ecosystem master document', 'Historical technical/commercial narrative'),
        ('SRC-0048', 'ComSoc HackX content plan', 'Historical presentation and narrative framing'),
        ('SRC-0055', 'ComSoc HackX presentation', 'Historical presentation artifact'),
        ('SRC-0062', 'Historical title-slide artifact', 'Historical pitch/deck visual framing'),
        ('SRC-0319', 'Agricultural R&D spending chart', 'Historical research communication asset'),
        ('SRC-0324', 'Farmer income squeeze chart', 'Historical research communication asset'),
        ('SRC-0325', 'Farmer suicides chart', 'Historical research communication asset'),
        ('SRC-0332', 'Groundwater depletion chart', 'Historical research communication asset'),
        ('SRC-0335', 'Regional cluster radar chart', 'Historical comparative visual'),
        ('SRC-0336', 'Regional clusters chart', 'Historical research communication asset'),
        ('SRC-0338', 'Water disputes chart', 'Historical research communication asset'),
    ]),
]

def slug(value):
    stem = Path(value).stem.lower()
    stem = re.sub(r'[^a-z0-9]+', '_', stem).strip('_')
    return stem[:72] or 'untitled'

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

records = []
selected = set()
for prefix, directory, entries in CATEGORY_SPECS:
    target = OUT / directory
    target.mkdir(parents=True, exist_ok=True)
    for sequence, (source_id, label, role) in enumerate(entries, 1):
        record = BY_ID[source_id]
        source_path = ARCHIVE / record['relative_path']
        if not source_path.exists():
            raise FileNotFoundError(source_path)
        curated_id = f'{prefix}-{sequence:03d}'
        destination_name = f'{curated_id}__{slug(record["file_name"])}{record["extension"]}'
        destination = target / destination_name
        shutil.copy2(source_path, destination)
        selected.add(source_id)
        records.append({
            'curated_id': curated_id,
            'category_prefix': prefix,
            'category_directory': directory,
            'source_id': source_id,
            'legacy_source_ids': sorted(set(BY_HASH[record['sha256']] + SEMANTIC_ALIASES.get(source_id, []))),
            'title': label,
            'role': role,
            'source_group': record['source_group'],
            'original_relative_path': record['relative_path'],
            'sha256': record['sha256'],
            'archive_relative_path': str(destination.relative_to(OUT)),
            'github_relative_path': str(destination.relative_to(OUT)),
        })

# Curated knowledge-base outputs and archive metadata are copied after substantive evidence.
kb_dir = OUT / '10_knowledge_base_outputs'
kb_dir.mkdir()
shutil.copy2('/home/ubuntu/projects/ecofarm-89bdc8ac/EcoFarm_Master_Knowledge_Base.md', kb_dir / 'EcoFarm_Master_Knowledge_Base.md')
shutil.copytree('/home/ubuntu/ecofarm_knowledge_html', kb_dir / 'html_knowledge_site')
shutil.copytree(ARCHIVE / 'llm_knowledge_corpus', kb_dir / 'llm_knowledge_corpus')

meta_dir = OUT / 'archive_metadata'
meta_dir.mkdir()
for file_name in [
    'EcoFarm_Curated_Archive_Taxonomy.md',
    'EcoFarm_Evidence_Status_Taxonomy.md',
    'EcoFarm_Core_Source_Map.md',
    'EcoFarm_Semantic_Supersession_Review.md',
    'EcoFarm_Content_Based_Version_Comparison.md',
    'EcoFarm_Content_Based_Curation_Review_Register.md',
    'EcoFarm_Corpus_Coverage_and_Resolution.md',
    'EcoFarm_HTML_Usability_Checks.md',
    'EcoFarm_Curated_Archive_Verification_Notes.md',
    'EcoFarm_Master_Knowledge_Base_Legacy_SRC_Reference_Copy.md',
]:
    path = ARCHIVE / 'knowledge_mapping' / file_name
    if path.exists():
        shutil.copy2(path, meta_dir / file_name)
shutil.copy2(ARCHIVE / 'manifest' / 'EcoFarm_Source_Manifest.json', meta_dir / 'legacy_source_manifest.json')
shutil.copy2(ARCHIVE / 'manifest' / 'EcoFarm_Source_Manifest.csv', meta_dir / 'legacy_source_manifest.csv')

# Archive infrastructure: only the tools that create or validate the public knowledge archive, never the unrelated pilot/tracker application code.
infra_dir = OUT / 'archive_infrastructure'
infra_dir.mkdir()
for script_name in [
    'build_curated_archive.py',
    'build_html_knowledge_site.py',
    'build_llm_knowledge_corpus.py',
    'build_source_manifest.py',
    'build_semantic_supersession_review.py',
    'compare_version_families.py',
    'build_corpus_coverage_register.py',
    'build_curation_review_register.py',
    'augment_llm_corpus_with_curated_metadata.py',
    'sanitize_public_curated_archive.py',
    'audit_public_curated_archive.py',
    'migrate_master_citations_to_curated_ids.py',
    'validate_knowledge_deliverables.py',
    'serve_html_knowledge.sh',
]:
    script = Path('/home/ubuntu/ecofarm_inventory') / script_name
    if script.exists():
        shutil.copy2(script, infra_dir / script_name)

excluded = []
for record in MANIFEST:
    if record['source_id'] in selected:
        continue
    reason = (
        'Excluded from primary curated archive: EcoFarm pilot/task-tracker application, generated build, dependency, configuration, or generic component code.'
        if record['source_group'] == 'webapp_project' else
        'Not separately copied: exact duplicate or format/version alias of retained material; use legacy manifest and canonical source mapping.'
        if record['duplicate_status'] == 'exact_duplicate' else
        'Preserved in the private raw archive but excluded from the primary public catalogue after relevance review; it is low-signal, generated, incomplete, conversational trace, redundant source capture, or requires future source-specific escalation.'
    )
    excluded.append({
        'source_id': record['source_id'],
        'source_group': record['source_group'],
        'original_relative_path': record['relative_path'],
        'reason': reason,
    })

(meta_dir / 'curated_source_index.json').write_text(json.dumps(records, indent=2))
legacy_to_curated = {}
for record in records:
    for legacy_id in record['legacy_source_ids']:
        legacy_to_curated.setdefault(legacy_id, {
            'curated_id': record['curated_id'],
            'title': record['title'],
            'github_relative_path': record['github_relative_path'],
            'github_url': f"https://github.com/{GITHUB_REPOSITORY}/blob/{GITHUB_BRANCH}/{record['github_relative_path']}",
            'canonical_source_id': record['source_id'],
        })
(meta_dir / 'legacy_to_curated_source_map.json').write_text(json.dumps(legacy_to_curated, indent=2))
with (meta_dir / 'legacy_source_crosswalk.csv').open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=['curated_id','source_id','legacy_source_ids','title','category_directory','archive_relative_path','original_relative_path'])
    writer.writeheader()
    for record in records:
        row = {key: record[key] for key in writer.fieldnames if key in record}
        row['legacy_source_ids'] = ';'.join(record['legacy_source_ids'])
        writer.writerow(row)

lines = ['# Curated EcoFarm Archive Index', '', '> This is the human-facing source index. It contains only reviewed substantive content. Code, package metadata, generated builds, duplicate aliases, and archive noise do not appear as ordinary source records.', '']
for prefix, directory, _ in CATEGORY_SPECS:
    entries = [record for record in records if record['category_prefix'] == prefix]
    lines.extend([f'## {prefix} — {directory.replace("_", " ").title()}', '', '| Curated ID | Title | Role | Legacy source ID(s) | GitHub file |', '|---|---|---|---|---|'])
    for record in entries:
        github_url = f"https://github.com/{GITHUB_REPOSITORY}/blob/{GITHUB_BRANCH}/{record['github_relative_path']}"
        lines.append(f"| `{record['curated_id']}` | {record['title']} | {record['role']} | {', '.join('`'+id+'`' for id in record['legacy_source_ids'])} | [Open on GitHub]({github_url}) |")
    lines.append('')
(OUT / 'CURATED_ARCHIVE_INDEX.md').write_text('\n'.join(lines))

lines = ['# Inclusion and Exclusion Register', '', '| Treatment | Count | Explanation |', '|---|---:|---|', f'| Curated substantive canonical records | {len(records)} | Reviewed sources copied into category folders. |', f'| Legacy raw artifacts not copied as primary records | {len(excluded)} | Either duplicate aliases, irrelevant/generic app code, generated material, conversation trace, or low-signal/redundant source material. |', '', '## Per-source exclusion or demotion record', '', '| Legacy source ID | Source group | Original path | Treatment rationale |', '|---|---|---|---|']
for record in excluded:
    lines.append(f"| `{record['source_id']}` | `{record['source_group']}` | `{record['original_relative_path']}` | {record['reason']} |")
(meta_dir / 'inclusion_exclusion_register.md').write_text('\n'.join(lines))

readme = f'''# EcoFarm Archives

This repository is a **curated, source-traceable knowledge archive** for EcoFarm. It is not a raw file dump. Every primary source was reviewed for lasting value to EcoFarm’s vision, product mechanics, technical reasoning, research, field validation, data safety, historical design, or decision history.

> The archive is non-final. A historical feature, research plan, agent synthesis, market hypothesis, source test, or pitch artifact is not proof that a capability is validated, currently approved, or guaranteed to be built.

## Start here

| Location | Purpose |
|---|---|
| [`CURATED_ARCHIVE_INDEX.md`](CURATED_ARCHIVE_INDEX.md) | Human-readable register of reviewed canonical sources, category-aware IDs, roles, legacy trace, and GitHub links. |
| [`10_knowledge_base_outputs/EcoFarm_Master_Knowledge_Base.md`](10_knowledge_base_outputs/EcoFarm_Master_Knowledge_Base.md) | Hyper-detailed human-readable knowledge base. |
| [`10_knowledge_base_outputs/html_knowledge_site/`](10_knowledge_base_outputs/html_knowledge_site/) | Static, navigable HTML knowledge base. |
| [`10_knowledge_base_outputs/llm_knowledge_corpus/`](10_knowledge_base_outputs/llm_knowledge_corpus/) | Retrieval-oriented corpus and external-LLM use guide. |
| [`archive_metadata/`](archive_metadata/) | Crosswalk, semantic review, inclusion/exclusion record, and public-release audit. |

## Meaningful source categories

`EF-GOV` governance/archive · `EF-VSN` founder vision/evolution · `EF-PRD` product/feature mechanics · `EF-TEC` technical architecture/hardware/AI · `EF-AGR` India agriculture problem research · `EF-REG` regional/Namakkal research · `EF-MKT` market/commercial/ecosystem research · `EF-FLD` farmer decision/field validation · `EF-DAT` data sources/safety/P0 feasibility · `EF-DSN` historical design/pitch/media.

The original preservation corpus contained **{len(MANIFEST)}** raw artifacts. This curated archive retains **{len(records)}** canonical substantive records. Exact duplicates, generic app code, dependency/configuration files, generated builds, low-signal items, and raw conversation traces are documented rather than mixed into ordinary evidence browsing. Archive-generation code is kept separately under [`archive_infrastructure/`](archive_infrastructure/).

## Public-release policy

The public copy is scanned for credential patterns and contact identifiers; detected contact identifiers are redacted in this repository while the private preservation corpus remains unchanged. See [`archive_metadata/public_release_audit.md`](archive_metadata/public_release_audit.md) and [`archive_metadata/public_release_redaction_log.md`](archive_metadata/public_release_redaction_log.md).

## Updating

Preserve a raw artifact, review it for substantive value, assign an `EF-*` ID only to a canonical source, update the crosswalk and knowledge outputs, then rerun the public-release audit/redaction workflow before publishing.
'''
(OUT / 'README.md').write_text(readme)

print(json.dumps({'curated_records': len(records), 'excluded_or_aliased': len(excluded), 'output': str(OUT)}, indent=2))
