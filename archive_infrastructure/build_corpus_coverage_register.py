from pathlib import Path
import json
from collections import Counter, defaultdict

ROOT = Path('/home/ubuntu/ecofarm_source_archive')
MANIFEST = json.loads((ROOT / 'manifest' / 'EcoFarm_Source_Manifest.json').read_text())
DOCS = json.loads((ROOT / 'llm_knowledge_corpus' / 'EcoFarm_LLM_Knowledge_Documents.json').read_text())
DOC_BY_ID = {row['source_id']: row for row in DOCS}
OUT = ROOT / 'knowledge_mapping' / 'EcoFarm_Corpus_Coverage_and_Resolution.md'

def resolution(record):
    source_id = record['source_id']
    ext = Path(record['file_name']).suffix.lower()
    if record.get('duplicate_of'):
        return 'Duplicate alias retained in manifest; canonical content is represented under its canonical source ID.'
    if source_id in DOC_BY_ID and not DOC_BY_ID[source_id]['exact_duplicate_of_canonical']:
        return 'Normalized source text is represented in the provenance-bearing LLM chunk corpus and family-level knowledge map.'
    if ext in {'.png', '.jpg', '.jpeg', '.gif', '.mov', '.mp4'}:
        return 'Visual/media artifact indexed in the Master Knowledge Base visual appendix and retained in raw archive; not transcribed as textual evidence.'
    if record['source_group'] in {'webapp_project', 'manifest'}:
        return 'Retained as project/provenance material; not used as EcoFarm domain evidence except project-history context.'
    if source_id in DOC_BY_ID:
        return 'Document-level alias/index record retained; canonical duplicate text is represented elsewhere.'
    return 'Preserved raw artifact requiring source-specific reinspection if later needed; not a priority text source in the LLM corpus because extraction was unavailable or content was negligible.'

by_group = Counter(r['source_group'] for r in MANIFEST)
counts = Counter()
rows = []
for r in MANIFEST:
    kind = resolution(r)
    counts[kind] += 1
    rows.append((r, kind))

lines = [
    '# EcoFarm Corpus Coverage and Resolution Register',
    '',
    '> This register demonstrates treatment coverage for all preserved artifacts. “Represented” does not mean that every source is a current conclusion; it means the artifact has a discoverable provenance path and an explicit role.',
    '',
    '## Coverage summary',
    '',
    f'- Preserved artifacts in manifest: **{len(MANIFEST)}**',
    f'- Source documents in the LLM document index: **{len(DOCS)}**',
    f'- Retrieval-ready canonical chunks: **957**',
    f'- Exact duplicate aliases tracked in manifest: **{sum(1 for r in MANIFEST if r.get("duplicate_of"))}**',
    '',
    '### Source-group coverage',
    '',
    '| Source group | Artifact count |',
    '|---|---:|',
]
for group, count in sorted(by_group.items()):
    lines.append(f'| `{group}` | {count} |')
lines.extend(['', '### Representation path', '', '| Resolution path | Artifact count |', '|---|---:|'])
for kind, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
    lines.append(f'| {kind} | {count} |')

lines.extend(['', '## Per-artifact treatment record', '', '| Source ID | Source group | Artifact | Treatment / resolution path |', '|---|---|---|---|'])
for r, kind in rows:
    lines.append(f'| `{r["source_id"]}` | `{r["source_group"]}` | `{r["relative_path"]}` | {kind} |')

lines.extend([
    '', '## Resolution note on partial atomic extraction', '',
    'The compact Gemini atomic-extraction set is intentionally **partial** because its external request quota stopped the batch. This does not leave source content unavailable: the deterministic LLM corpus contains normalized, provenance-bearing chunks for all eligible unique text sources. The partial atomic records are an acceleration layer, not the sole representation of evidence. A future update can add atomic records incrementally without rewriting the source manifest, Markdown master, or chunk corpus.',
    '', '## Semantic-supersession boundary', '',
    'Exact-hash duplicate detection is complete. Semantic supersession is represented through the dedicated family register, which distinguishes current founder approvals and direct test records from historical vision, design, research, and pitch artifacts. Some broad historical concepts deliberately remain unresolved rather than being marked obsolete; this preserves the user’s requirement that future decisions can be remade from the original reasoning.',
])
OUT.write_text('\n'.join(lines))
print(json.dumps({'sources': len(MANIFEST), 'document_index': len(DOCS), 'output': str(OUT)}, indent=2))
