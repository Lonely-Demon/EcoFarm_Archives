from pathlib import Path
from html.parser import HTMLParser
import json
import re

PROJECT = Path('/home/ubuntu/projects/ecofarm-89bdc8ac')
ARCHIVE = Path('/home/ubuntu/ecofarm_source_archive')
HTML = Path('/home/ubuntu/ecofarm_knowledge_html')
MASTER = PROJECT / 'EcoFarm_Master_Knowledge_Base.md'
MANIFEST = json.loads((ARCHIVE / 'manifest' / 'EcoFarm_Source_Manifest.json').read_text())
SOURCE_IDS = {record['source_id'] for record in MANIFEST}

failures = []
master_text = MASTER.read_text()
sections = re.findall(r'^## ', master_text, flags=re.M)
refs = set(re.findall(r'\[SRC-(\d{4})\]', master_text))
missing_ids = sorted({f'SRC-{source_id}' for source_id in refs} - SOURCE_IDS)
if len(sections) < 12:
    failures.append(f'Master document has only {len(sections)} top-level sections; expected at least 12.')
if len(master_text) < 40000:
    failures.append(f'Master document has {len(master_text)} characters; expected a hyper-detailed baseline of at least 40,000.')
if missing_ids:
    failures.append(f'Master references missing source IDs: {missing_ids}')

llm_dir = ARCHIVE / 'llm_knowledge_corpus'
documents = json.loads((llm_dir / 'EcoFarm_LLM_Knowledge_Documents.json').read_text())
chunks = []
for line_number, line in enumerate((llm_dir / 'EcoFarm_LLM_Knowledge_Chunks.jsonl').read_text().splitlines(), start=1):
    try:
        chunks.append(json.loads(line))
    except json.JSONDecodeError as exc:
        failures.append(f'Invalid LLM chunk JSON at line {line_number}: {exc}')
if len(documents) < 100:
    failures.append(f'LLM document index has only {len(documents)} documents.')
if len(chunks) < 500:
    failures.append(f'LLM retrieval corpus has only {len(chunks)} chunks.')
for chunk in chunks:
    if chunk['source_id'] not in SOURCE_IDS:
        failures.append(f'LLM chunk {chunk["chunk_id"]} has unknown source ID.')
        break

index = json.loads((HTML / 'search-index.json').read_text())
html_files = {path.name for path in HTML.glob('*.html')}
if 'index.html' not in html_files:
    failures.append('HTML site lacks index.html.')
for item in index:
    if item['file'] not in html_files:
        failures.append(f'HTML search index points to missing file {item["file"]}.')
if len(html_files) < 16:
    failures.append(f'HTML site has only {len(html_files)} pages.')
if 'sources.html' not in html_files:
    failures.append('HTML site lacks the source-catalogue page.')

critical_sources = {'SRC-0039', 'SRC-0357', 'SRC-0370'}
chunk_source_ids = {chunk['source_id'] for chunk in chunks}
for source_id in critical_sources:
    if source_id not in master_text:
        failures.append(f'Master document lacks critical source reference {source_id}.')
    if source_id not in {row['source_id'] for row in documents}:
        failures.append(f'LLM document index lacks critical source {source_id}.')
    else:
        canonical_source = DOC_BY_ID = {row['source_id']: row['canonical_source_id'] for row in documents}
        represented_source = canonical_source[source_id]
        if represented_source not in chunk_source_ids:
            failures.append(f'LLM chunk corpus lacks critical source {source_id} or canonical alias {represented_source}.')

technical_page = (HTML / '7-technical-and-data-system-archive.html').read_text()
if 'TNAU weather-path test' not in technical_page or 'Data-source hierarchy' not in technical_page:
    failures.append('Technical HTML page lacks the expected P0 weather-test and source-hierarchy content.')
if 'href="sources.html#SRC-0039"' not in technical_page:
    failures.append('Technical HTML page lacks an internal source-resolution link for SRC-0039.')
source_catalogue = (HTML / 'sources.html').read_text()
if 'id="SRC-0039"' not in source_catalogue or 'EcoFarm-1_3/project_onboarding_document.md' not in source_catalogue:
    failures.append('HTML source catalogue lacks expected SRC-0039 provenance metadata.')
for mapping_file in [
    ARCHIVE / 'knowledge_mapping' / 'EcoFarm_Semantic_Supersession_Review.md',
    ARCHIVE / 'knowledge_mapping' / 'EcoFarm_Content_Based_Version_Comparison.md',
    ARCHIVE / 'knowledge_mapping' / 'EcoFarm_Corpus_Coverage_and_Resolution.md',
    ARCHIVE / 'knowledge_mapping' / 'EcoFarm_HTML_Usability_Checks.md',
]:
    if not mapping_file.exists() or len(mapping_file.read_text()) < 400:
        failures.append(f'Missing or incomplete mapping/verification artifact: {mapping_file.name}')

summary = {
    'master_characters': len(master_text),
    'master_top_level_sections': len(sections),
    'master_source_references': len(refs),
    'manifest_sources': len(MANIFEST),
    'llm_documents': len(documents),
    'llm_chunks': len(chunks),
    'html_pages': len(html_files),
    'html_search_entries': len(index),
    'critical_source_cross_format_spot_check': sorted(critical_sources),
    'failures': failures,
}
(PROJECT / 'EcoFarm_Knowledge_Base_Validation.json').write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))
if failures:
    raise SystemExit(1)
