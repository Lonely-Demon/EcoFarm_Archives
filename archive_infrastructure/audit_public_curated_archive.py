from pathlib import Path
import json
import re

ROOT = Path('/home/ubuntu/ecofarm_curated_archive')
OUT = ROOT / 'archive_metadata' / 'public_release_audit.md'

secret_patterns = {
    'private key block': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'AWS access key': r'AKIA[0-9A-Z]{16}',
    'GitHub personal token': r'gh[pousr]_[A-Za-z0-9_]{20,}',
    'generic API key assignment': r'(?i)(?:api[_-]?key|secret|password|token)\s*[=:]\s*["\'][^"\']{12,}',
}
personal_patterns = {
    'email address': r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',
    'Indian mobile number': r'(?<!\d)(?:\+91[-\s]?)?[6-9]\d{9}(?!\d)',
}

allowed_code_root = ROOT / 'archive_infrastructure'
code_extensions = {'.ts', '.tsx', '.js', '.jsx', '.py', '.sh', '.json', '.yaml', '.yml'}
findings = []
files = [path for path in ROOT.rglob('*') if path.is_file() and '.git' not in path.parts]
for path in files:
    rel = path.relative_to(ROOT)
    if path.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.mov', '.mp4', '.pdf', '.zip'}:
        continue
    try:
        text = path.read_text(errors='replace')
    except OSError:
        continue
    for label, pattern in secret_patterns.items():
        if re.search(pattern, text):
            findings.append({'severity': 'BLOCK', 'kind': label, 'path': str(rel)})
    for label, pattern in personal_patterns.items():
        if re.search(pattern, text):
            findings.append({'severity': 'REVIEW', 'kind': label, 'path': str(rel)})
    if path.suffix.lower() in code_extensions and not str(rel).startswith('archive_infrastructure/') and not str(rel).startswith('10_knowledge_base_outputs/html_knowledge_site/') and not str(rel).startswith('10_knowledge_base_outputs/llm_knowledge_corpus/') and not str(rel).startswith('archive_metadata/'):
        findings.append({'severity': 'REVIEW', 'kind': 'code or configuration outside approved archive-infrastructure locations', 'path': str(rel)})

third_party_cautions = [
    'Several historical pitch PDFs, screen captures, charts, and external-source captures may contain material whose public redistribution rights are unknown. They are retained as historical/internal research artefacts, not relicensed source material.',
    'External institutional pages and market/weather captures are archived as evidence of reviewed material. Public availability of a page does not imply automated-reuse rights for a production EcoFarm feature.',
    'Historical conversation traces can contain contextual statements by agents and founders. They are not authoritative source material unless the curated record says so.',
]
lines = ['# Public Release Audit — Curated EcoFarm Archive', '', '> Scope: automated pattern scan plus structural review of the curated archive intended for the public GitHub repository. It is not legal advice and does not verify third-party copyright ownership.', '', f'- Files scanned: **{len(files)}**', f'- Blocking credential findings: **{sum(1 for item in findings if item["severity"] == "BLOCK")}**', f'- Review findings: **{sum(1 for item in findings if item["severity"] == "REVIEW")}**', '', '## Findings', '', '| Severity | Type | Path |', '|---|---|---|']
if findings:
    for item in findings:
        lines.append(f"| {item['severity']} | {item['kind']} | `{item['path']}` |")
else:
    lines.append('| None | No credential, direct personal-data marker, or misplaced code finding from this automated scan. | — |')
lines.extend(['', '## Third-party and context cautions', ''])
for caution in third_party_cautions:
    lines.append(f'- {caution}')
lines.extend(['', '## Publication decision', '', '**Do not publish while any `BLOCK` finding remains unresolved.** `REVIEW` findings require an explicit judgement: retain, redact, move to non-public storage, or document why the appearance is non-sensitive.'])
OUT.write_text('\n'.join(lines))
print(json.dumps({'files_scanned': len(files), 'findings': findings, 'output': str(OUT)}, indent=2))
if any(item['severity'] == 'BLOCK' for item in findings):
    raise SystemExit(1)
