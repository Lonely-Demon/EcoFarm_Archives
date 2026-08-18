from pathlib import Path
import json
import re

MASTER = Path('/home/ubuntu/projects/ecofarm-89bdc8ac/EcoFarm_Master_Knowledge_Base.md')
MAP = Path('/home/ubuntu/ecofarm_curated_archive/archive_metadata/legacy_to_curated_source_map.json')
BACKUP = Path('/home/ubuntu/ecofarm_source_archive/knowledge_mapping/EcoFarm_Master_Knowledge_Base_Legacy_SRC_Reference_Copy.md')

source_map = json.loads(MAP.read_text())
text = MASTER.read_text()
if not BACKUP.exists():
    BACKUP.write_text(text)

unmapped = set()
def replace(match):
    legacy_id = f'SRC-{match.group(1)}'
    record = source_map.get(legacy_id)
    if not record:
        unmapped.add(legacy_id)
        return match.group(0)
    return f'[{record["curated_id"]}]({record["github_url"]} "{record["title"]}; legacy {legacy_id}")'

rewritten = re.sub(r'\[SRC-(\d{4})\]', replace, text)
banner = '''> **Curated citation system:** Each `EF-*` citation links to the canonical reviewed file in the public EcoFarm archive. Legacy `SRC-*` identifiers remain available through the archive crosswalk for historical traceability. A cited source may still be historical, exploratory, or unvalidated; its source status governs interpretation.\n\n'''
if not rewritten.startswith('> **Curated citation system:**'):
    rewritten = banner + rewritten
MASTER.write_text(rewritten)
print(json.dumps({'rewritten_citations': len(re.findall(r'\[EF-[A-Z]+-\d{3}\]', rewritten)), 'unmapped': sorted(unmapped), 'backup': str(BACKUP)}, indent=2))
