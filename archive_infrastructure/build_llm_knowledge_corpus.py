from pathlib import Path
import json
import re
from collections import Counter, defaultdict

ROOT = Path('/home/ubuntu/ecofarm_source_archive')
MANIFEST_PATH = ROOT / 'manifest' / 'EcoFarm_Source_Manifest.json'
TEXT_ROOT = ROOT / 'extracted_text'
OUT = ROOT / 'llm_knowledge_corpus'
OUT.mkdir(exist_ok=True)
MAX_CHARS = 6000

INCLUDED_GROUPS = {
    'historical_task_ecofarm_1', 'historical_task_ecofarm_2', 'historical_task_ecofarm_1_2',
    'historical_task_ecofarm_1_3', 'historical_task_ecofarm_1_3_later',
    'research_agent_1', 'research_agent_2', 'project_shared_files', 'current_uploads',
    'referenced_task_conversations', 'current_session',
}
TOPICS = {
    'founder_intent': ['vision', 'founder', 'intuition', 'mental model', 'why ecofarm'],
    'crop_decision_support': ['crop recommendation', 'crop selection', 'what crop', 'decision packet'],
    'crop_production': ['planting', 'fertilizer', 'irrigation', 'harvest', 'crop calendar', 'yield'],
    'weather': ['weather', 'rainfall', 'forecast', 'agromet', 'imd'],
    'market_and_prices': ['market price', 'mandi', 'price', 'buyer', 'wholesale', 'retail'],
    'soil_water_and_sensors': ['soil', 'moisture', 'ph', 'npk', 'sensor', 'irrigation', 'water'],
    'hardware_and_iot': ['motor', 'starter', 'valve', 'iot', 'camera', 'remote control'],
    'ai_and_reasoning': ['artificial intelligence', ' ai ', 'machine learning', 'model', 'diagnosis'],
    'farmer_reality': ['farmer', 'household', 'authority', 'trust', 'workaround', 'interview'],
    'safety_and_consent': ['consent', 'safety', 'escalation', 'referral', 'harm', 'privacy'],
    'data_provenance': ['source hierarchy', 'provenance', 'data source', 'freshness', 'observability'],
    'ecosystem_and_partnerships': ['fpo', 'kvk', 'tnau', 'department', 'partner', 'ecosystem'],
    'validation': ['validation', 'field', 'cohort', 'event', 'evidence', 'pilot', 'test'],
    'technical_architecture': ['api', 'backend', 'database', 'architecture', 'frontend', 'stack'],
    'community_and_marketplace': ['community', 'marketplace', 'equipment rental', 'labour', 'equipment'],
    'commercial_hypotheses': ['business model', 'revenue', 'investor', 'pitch', 'market size', 'monetization'],
}

def status_for(group, path):
    lower = path.lower()
    if group == 'current_session':
        return 'founder_instruction_or_approval'
    if group == 'referenced_task_conversations':
        return 'historical_conversation_record'
    if group.startswith('research_agent'):
        return 'research_agent_output_or_artifact'
    if 'test' in lower or 'statusmemo' in lower or 'status_memo' in lower:
        return 'test_or_operational_artifact'
    if any(term in lower for term in ['plan', 'protocol', 'checklist', 'guide', 'form', 'register']):
        return 'plan_or_method_artifact'
    if group.startswith('historical_task'):
        return 'historical_product_or_technical_artifact'
    return 'research_or_reference_artifact'

def conversation_to_text(text):
    output = []
    for raw in text.splitlines():
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if obj.get('type') == 'chat':
            sender = obj.get('sender', 'unknown')
            content = obj.get('content')
            if isinstance(content, str) and content.strip():
                output.append(f'[{sender}] {content.strip()}')
    return '\n\n'.join(output)

def extract_heading(line):
    line = line.strip()
    if re.match(r'^#{1,6}\s+\S', line):
        return re.sub(r'^#+\s*', '', line)
    if re.match(r'^\d+(?:\.\d+)*[.)]\s+\S', line) and len(line) < 180:
        return line
    return None

def topic_tags(text):
    lower = f' {text.lower()} '
    return sorted(topic for topic, needles in TOPICS.items() if any(needle in lower for needle in needles))

def chunks_with_headings(text):
    chunks = []
    current = []
    current_heading = '[document opening]'
    length = 0
    for line in text.splitlines():
        heading = extract_heading(line)
        if heading:
            current_heading = heading
        line_length = len(line) + 1
        if current and length + line_length > MAX_CHARS:
            chunks.append((current_heading, '\n'.join(current)))
            current = []
            length = 0
        current.append(line)
        length += line_length
    if current:
        chunks.append((current_heading, '\n'.join(current)))
    return [(heading, body.strip()) for heading, body in chunks if body.strip()]

manifest = json.loads(MANIFEST_PATH.read_text())
canonical_by_hash = {}
for record in manifest:
    if record['source_group'] not in INCLUDED_GROUPS:
        continue
    input_path = TEXT_ROOT / f'{record["source_id"]}.txt'
    if not input_path.exists():
        continue
    candidate_text = input_path.read_text(errors='replace')
    if record['source_group'] == 'referenced_task_conversations':
        candidate_text = conversation_to_text(candidate_text)
    if len(candidate_text.strip()) < 150:
        continue
    canonical_by_hash.setdefault(record['sha256'], record['source_id'])

documents = []
chunks = []
for record in manifest:
    if record['source_group'] not in INCLUDED_GROUPS:
        continue
    input_path = TEXT_ROOT / f'{record["source_id"]}.txt'
    if not input_path.exists():
        continue
    text = input_path.read_text(errors='replace')
    if record['source_group'] == 'referenced_task_conversations':
        text = conversation_to_text(text)
    if len(text.strip()) < 150:
        continue
    canonical = canonical_by_hash.get(record['sha256'], record['source_id'])
    is_exact_duplicate = canonical != record['source_id']
    document = {
        'source_id': record['source_id'],
        'canonical_source_id': canonical,
        'exact_duplicate_of_canonical': is_exact_duplicate,
        'source_group': record['source_group'],
        'relative_path': record['relative_path'],
        'status_hint': status_for(record['source_group'], record['relative_path']),
        'characters': len(text),
        'document_tags': topic_tags(text[:40000]),
    }
    documents.append(document)
    if is_exact_duplicate:
        continue
    for number, (heading, body) in enumerate(chunks_with_headings(text), start=1):
        chunks.append({
            'chunk_id': f'{record["source_id"]}-C{number:04d}',
            'source_id': record['source_id'],
            'source_group': record['source_group'],
            'relative_path': record['relative_path'],
            'status_hint': document['status_hint'],
            'heading_context': heading,
            'tags': topic_tags(body),
            'text': body,
        })

with (OUT / 'EcoFarm_LLM_Knowledge_Documents.json').open('w') as f:
    json.dump(documents, f, indent=2)
with (OUT / 'EcoFarm_LLM_Knowledge_Chunks.jsonl').open('w') as f:
    for chunk in chunks:
        f.write(json.dumps(chunk, ensure_ascii=False) + '\n')

tag_index = defaultdict(list)
for chunk in chunks:
    for tag in chunk['tags']:
        tag_index[tag].append(chunk['chunk_id'])
with (OUT / 'EcoFarm_LLM_Topic_Index.json').open('w') as f:
    json.dump({tag: ids for tag, ids in sorted(tag_index.items())}, f, indent=2)

readme = OUT / 'README.md'
with readme.open('w') as f:
    f.write('# EcoFarm LLM-Optimized Knowledge Corpus\n\n')
    f.write('This directory is designed for retrieval, ingestion, and exact source tracing by external language models. It does not replace the human-readable Master Knowledge Base.\n\n')
    f.write('## Files\n\n')
    f.write('| File | Purpose |\n|---|---|\n')
    f.write('| `EcoFarm_LLM_Knowledge_Documents.json` | Source-level metadata, duplicate relations, status hints, and document tags. |\n')
    f.write('| `EcoFarm_LLM_Knowledge_Chunks.jsonl` | Retrieval-ready source chunks. Every chunk contains the exact source ID, path, heading context, status hint, tags, and text. |\n')
    f.write('| `EcoFarm_LLM_Topic_Index.json` | Topic-to-chunk lookup index. |\n\n')
    f.write('## Retrieval rules\n\n')
    f.write('Treat each chunk as source-specific evidence. Use `source_id` and `relative_path` when citing. Do not turn a `plan_or_method_artifact` into completed validation, and do not infer current approval from a `historical_product_or_technical_artifact`. Exact duplicates remain recorded at the document level but are excluded from duplicate chunk copies.\n\n')
    f.write(f'## Corpus statistics\n\n- Documents represented: {len(documents)}\n- Canonical text chunks: {len(chunks)}\n- Retrieval topics: {len(tag_index)}\n')

print(json.dumps({'documents': len(documents), 'canonical_chunks': len(chunks), 'topics': len(tag_index)}, indent=2))
