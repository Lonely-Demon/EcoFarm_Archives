from pathlib import Path
import json

ARCHIVE = Path('/home/ubuntu/ecofarm_source_archive')
CURATED = Path('/home/ubuntu/ecofarm_curated_archive')
LLM = ARCHIVE / 'llm_knowledge_corpus'
SOURCE_MAP = json.loads((CURATED / 'archive_metadata' / 'legacy_to_curated_source_map.json').read_text())
CURATED_INDEX = json.loads((CURATED / 'archive_metadata' / 'curated_source_index.json').read_text())
BY_CURATED_ID = {record['curated_id']: record for record in CURATED_INDEX}

def curated_metadata(source_id, canonical_source_id=None):
    source = SOURCE_MAP.get(source_id) or SOURCE_MAP.get(canonical_source_id or '')
    if not source:
        return {
            'curated_id': None,
            'curated_category_prefix': None,
            'curated_category_directory': None,
            'canonical_github_url': None,
            'curation_access': 'private_raw_or_contextual_only',
        }
    record = BY_CURATED_ID[source['curated_id']]
    return {
        'curated_id': source['curated_id'],
        'curated_category_prefix': record['category_prefix'],
        'curated_category_directory': record['category_directory'],
        'canonical_github_url': source['github_url'],
        'curation_access': 'public_canonical_record',
    }

documents_path = LLM / 'EcoFarm_LLM_Knowledge_Documents.json'
documents = json.loads(documents_path.read_text())
for document in documents:
    document.update(curated_metadata(document['source_id'], document.get('canonical_source_id')))
documents_path.write_text(json.dumps(documents, indent=2))

chunks_path = LLM / 'EcoFarm_LLM_Knowledge_Chunks.jsonl'
chunks = []
for line in chunks_path.read_text().splitlines():
    if not line.strip():
        continue
    chunk = json.loads(line)
    chunk.update(curated_metadata(chunk['source_id'], chunk.get('canonical_source_id')))
    chunks.append(chunk)
chunks_path.write_text('\n'.join(json.dumps(chunk, ensure_ascii=False) for chunk in chunks) + '\n')

crosswalk = []
for record in CURATED_INDEX:
    crosswalk.append({
        'curated_id': record['curated_id'],
        'category_prefix': record['category_prefix'],
        'category_directory': record['category_directory'],
        'title': record['title'],
        'legacy_source_ids': record['legacy_source_ids'],
        'github_url': f"https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/{record['github_relative_path']}",
    })
(LLM / 'EcoFarm_LLM_Curated_Source_Crosswalk.json').write_text(json.dumps(crosswalk, indent=2))

summary = {
    'documents': len(documents),
    'chunks': len(chunks),
    'public_canonical_documents': sum(1 for row in documents if row['curation_access'] == 'public_canonical_record'),
    'private_or_contextual_documents': sum(1 for row in documents if row['curation_access'] != 'public_canonical_record'),
    'curated_records': len(crosswalk),
}
(LLM / 'EcoFarm_LLM_Curated_Metadata_Summary.json').write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))
