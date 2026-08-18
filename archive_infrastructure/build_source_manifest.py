from pathlib import Path
import csv
import hashlib
import json
from collections import defaultdict

ROOT = Path('/home/ubuntu/ecofarm_source_archive')
OUT = ROOT / 'manifest'
OUT.mkdir(exist_ok=True)
EXCLUDE_NAMES = {'source_paths.txt', 'source_hashes.sha256'}
EXCLUDE_SUFFIXES = {'.meta'}

def classify(path: Path) -> str:
    parts = path.relative_to(ROOT).parts
    top = parts[0] if parts else 'unknown'
    return {
        'EcoFarm-1': 'historical_task_ecofarm_1',
        'EcoFarm-2': 'historical_task_ecofarm_2',
        'EcoFarm-1-2': 'historical_task_ecofarm_1_2',
        'EcoFarm-1-3': 'historical_task_ecofarm_1_3',
        'EcoFarm-1_3': 'historical_task_ecofarm_1_3_later',
        'Research-Agent-1': 'research_agent_1',
        'Research-Agent-2': 'research_agent_2',
        'shared_files': 'project_shared_files',
        'uploads': 'current_uploads',
        'local_project': 'webapp_project',
        'conversations': 'referenced_task_conversations',
    }.get(top, top)

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

records = []
hash_to_ids = defaultdict(list)
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or path.name in EXCLUDE_NAMES or path.suffix in EXCLUDE_SUFFIXES:
        continue
    rel = path.relative_to(ROOT).as_posix()
    digest = sha256(path)
    source_id = f'SRC-{len(records)+1:04d}'
    record = {
        'source_id': source_id,
        'relative_path': rel,
        'source_group': classify(path),
        'file_name': path.name,
        'extension': path.suffix.lower() or '[none]',
        'bytes': path.stat().st_size,
        'sha256': digest,
    }
    records.append(record)
    hash_to_ids[digest].append(source_id)

for record in records:
    peers = hash_to_ids[record['sha256']]
    record['duplicate_group'] = '' if len(peers) == 1 else '|'.join(peers)
    record['duplicate_status'] = 'unique' if len(peers) == 1 else 'exact_duplicate'

with (OUT / 'EcoFarm_Source_Manifest.json').open('w') as f:
    json.dump(records, f, indent=2)
fields = list(records[0].keys()) if records else []
with (OUT / 'EcoFarm_Source_Manifest.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)

summary = defaultdict(int)
for record in records:
    summary[record['source_group']] += 1
duplicate_groups = [ids for ids in hash_to_ids.values() if len(ids) > 1]
with (OUT / 'EcoFarm_Source_Manifest_Summary.md').open('w') as f:
    f.write('# EcoFarm Source Manifest Summary\n\n')
    f.write(f'- **Total preserved source files:** {len(records)}\n')
    f.write(f'- **Exact-duplicate hash groups:** {len(duplicate_groups)}\n')
    f.write(f'- **Files participating in exact duplicates:** {sum(len(ids) for ids in duplicate_groups)}\n\n')
    f.write('## Source Groups\n\n| Source group | Files |\n|---|---:|\n')
    for group, count in sorted(summary.items()):
        f.write(f'| {group} | {count} |\n')
    f.write('\n## Use\n\nThis manifest preserves provenance and exact hashes. Near-duplicate and supersession analysis is a subsequent semantic review step; identical bytes alone do not establish conceptual supersession.\n')

print(f'Created manifest for {len(records)} files; {len(duplicate_groups)} exact-duplicate groups.')
