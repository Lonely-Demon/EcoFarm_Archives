from pathlib import Path
import json
import re

ROOT = Path('/home/ubuntu/ecofarm_source_archive')
MANIFEST = json.loads((ROOT / 'manifest' / 'EcoFarm_Source_Manifest.json').read_text())
TEXT = ROOT / 'extracted_text'
OUT = ROOT / 'knowledge_mapping' / 'EcoFarm_Content_Based_Version_Comparison.md'
BY_ID = {row['source_id']: row for row in MANIFEST}

FAMILIES = {
    'Onboarding and core-vision sequence': ['SRC-0007', 'SRC-0033', 'SRC-0034', 'SRC-0035', 'SRC-0039', 'SRC-0040', 'SRC-0334'],
    'Early product requirements and workflow archive': ['SRC-0005', 'SRC-0006', 'SRC-0016', 'SRC-0017', 'SRC-0018', 'SRC-0019', 'SRC-0023', 'SRC-0024'],
    'Sensor and hardware research sequence': ['SRC-0025', 'SRC-0026', 'SRC-0029', 'SRC-0036'],
    'Field interview and learning instruments': ['SRC-0353', 'SRC-0358', 'SRC-0359', 'SRC-0364', 'SRC-0376'],
    'Candidate decision and claim-ledger sequence': ['SRC-0343', 'SRC-0344', 'SRC-0345', 'SRC-0346', 'SRC-0347', 'SRC-0383'],
    'Data-source and ecosystem register sequence': ['SRC-0348', 'SRC-0355', 'SRC-0365', 'SRC-0367', 'SRC-0370', 'SRC-0371', 'SRC-0377', 'SRC-0378', 'SRC-0380'],
}

def text(source_id):
    path = TEXT / f'{source_id}.txt'
    return path.read_text(errors='replace') if path.exists() else ''

def normalize(value):
    value = value.lower()
    value = re.sub(r'\s+', ' ', value)
    value = re.sub(r'[^a-z0-9 ]', '', value)
    return value

def representative_sample(value, limit=24000):
    if len(value) <= limit:
        return value
    half = limit // 2
    return value[:half] + ' [middle omitted for bounded comparison] ' + value[-half:]

def token_set(value):
    return set(re.findall(r'[a-z0-9]{4,}', value))

def headings(value):
    values = []
    for line in value.splitlines():
        line = line.strip()
        if re.match(r'^(#{1,6}\s+|\d+(?:\.\d+)*[.)]\s+)', line):
            values.append(re.sub(r'^(#+\s*|\d+(?:\.\d+)*[.)]\s*)', '', line))
    return values[:25]

lines = ['# EcoFarm Content-Based Version Comparison', '', '> This comparison uses normalized full-text similarity, title/path provenance, extracted headings, and manual disposition notes. It is evidence for semantic-family review, not a claim that a similarity percentage alone proves supersession.', '']

for family, source_ids in FAMILIES.items():
    available = [source_id for source_id in source_ids if source_id in BY_ID]
    lines.extend([f'## {family}', '', '| Source ID | Artifact | Characters | Selected headings / content cues |', '|---|---|---:|---|'])
    content = {}
    for source_id in available:
        source_text = text(source_id)
        content[source_id] = token_set(representative_sample(normalize(source_text)))
        record = BY_ID[source_id]
        heading_text = '; '.join(headings(source_text)[:4]) or '(no headings extracted)'
        lines.append(f'| `{source_id}` | `{record["relative_path"]}` | {len(source_text):,} | {heading_text[:240]} |')
    lines.extend(['', '### Pairwise normalized text similarity', '', '| Source A | Source B | Similarity | Interpretation cue |', '|---|---|---:|---|'])
    for i, source_a in enumerate(available):
        for source_b in available[i + 1:]:
            a, b = content[source_a], content[source_b]
            if not a or not b:
                score = 0.0
            else:
                score = len(a & b) / len(a | b)
            cue = 'Likely duplicate/format conversion' if score >= 0.90 else ('Strong thematic overlap; inspect additions/revisions' if score >= 0.45 else 'Distinct or complementary content')
            lines.append(f'| `{source_a}` | `{source_b}` | {score:.3f} | {cue} |')
    lines.append('')

lines.extend([
    '## Explicit manual dispositions',
    '',
    '| Family | Content-based disposition |',
    '|---|---|',
    '| Onboarding and core vision | `SRC-0007` and `SRC-0033` are duplicate short onboarding copies; `SRC-0034`/`SRC-0334` are format-rendered versions; `SRC-0035` is an older long text; `SRC-0039` is the richest extended historical onboarding record; `SRC-0040` is a concise later/final-labelled orientation record. Preserve all. Use `SRC-0039` for detailed historical mechanics and `SRC-0040` for concise late historical framing; current P0 evidence still governs present scope. |',
    '| Early PRD and workflow archive | The PRD, screen flows, wireframes, and UI syntheses cover different layers of the same early product model. They are complementary rather than serially superseding. The Master Knowledge Base preserves their conceptual workflow logic while excluding implementation-level UI prescriptions. |',
    '| Sensor and hardware research | The repeated sensor corpora have heavy overlap and format duplication, but their sensor trade-off content should remain as historical engineering rationale. None is a current hardware approval or replaces current field feasibility requirements. |',
    '| Field interview and learning instruments | The revised interview guide (`SRC-0359`) supersedes the earlier guide (`SRC-0358`) as the latest proposed interview instrument; discovery/event/follow-up forms are complementary instruments, not replacements. None proves field use absent participant/event evidence. |',
    '| Candidate decision and claim ledgers | Exact duplicate filenames are aliases; the revised field-programme claim ledger (`SRC-0347`) supersedes prior claim-ledger wording for the proposed field programme. Candidate-decision scoring is a separate analytical rationale, not a replacement for field evidence. |',
    '| Data-source and ecosystem registers | P0 operational revisions (`SRC-0365`, `SRC-0367`) are later control documents relative to broad registers (`SRC-0348`, `SRC-0355`) for the named P0. The direct P0 test memo (`SRC-0370`) governs the tested TNAU path only; the source hierarchy (`SRC-0380`) and observability plan (`SRC-0377`) complement it as operating policy. |',
    '',
    '## Residual unresolved relationships',
    '',
    'The archive deliberately retains broad historical platform concepts alongside narrow P0 constraints. This is not an unresolved clerical error: the concepts serve different temporal roles. A future product decision should use the source map, feature dossiers, and current direct test evidence to determine whether a historical capability is still relevant, rather than treating an older feature list as automatically superseded or permanently rejected.',
])
OUT.write_text('\n'.join(lines))
print(json.dumps({'families': len(FAMILIES), 'output': str(OUT)}, indent=2))
