from pathlib import Path
import json
import re

ROOT = Path('/home/ubuntu/ecofarm_curated_archive')
LOG = ROOT / 'archive_metadata' / 'public_release_redaction_log.md'

patterns = [
    ('email address', re.compile(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'), '[REDACTED_EMAIL]'),
    ('Indian mobile number', re.compile(r'(?<!\d)(?:\+91[-\s]?)?[6-9]\d{9}(?!\d)'), '[REDACTED_PHONE]'),
]
skip = {'.png', '.jpg', '.jpeg', '.gif', '.mov', '.mp4', '.pdf', '.zip'}
changes = []
for path in ROOT.rglob('*'):
    if not path.is_file() or path.suffix.lower() in skip or path.name == LOG.name:
        continue
    try:
        text = path.read_text(errors='replace')
    except OSError:
        continue
    updated = text
    counts = {}
    for label, pattern, replacement in patterns:
        updated, count = pattern.subn(replacement, updated)
        if count:
            counts[label] = count
    if counts:
        path.write_text(updated)
        changes.append({'path': str(path.relative_to(ROOT)), 'redactions': counts})

lines = ['# Public Release Redaction Log', '', '> The private preservation corpus remains unchanged. This log applies only to the public GitHub-ready curated copy.', '', f'- Files redacted: **{len(changes)}**', '', '| Public archive path | Redactions applied |', '|---|---|']
if changes:
    for change in changes:
        lines.append(f"| `{change['path']}` | {', '.join(f'{label}: {count}' for label, count in change['redactions'].items())} |")
else:
    lines.append('| None | No matching contact identifiers found. |')
LOG.write_text('\n'.join(lines))
print(json.dumps({'files_redacted': len(changes), 'changes': changes}, indent=2))
