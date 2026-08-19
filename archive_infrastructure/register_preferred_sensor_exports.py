#!/usr/bin/env python3
"""Register user-supplied parseable Grok sensor exports without renumbering legacy sources."""

import csv
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path('/home/ubuntu/ecofarm_source_archive')
UPLOAD = Path('/home/ubuntu/upload')
MANIFEST_JSON = ROOT / 'manifest' / 'EcoFarm_Source_Manifest.json'
MANIFEST_CSV = ROOT / 'manifest' / 'EcoFarm_Source_Manifest.csv'
TEXT_ROOT = ROOT / 'extracted_text'
PACKET_ROOT = ROOT / 'evidence_atlas' / 'full_file_review' / 'packets'
LEDGER_PATH = ROOT / 'evidence_atlas' / 'full_file_review' / 'EcoFarm_Full_File_Review_Ledger.json'

SOURCES = [
    {
        'source_id': 'SRC-0391',
        'file_name': 'Grok-EcoFarm-Module-Sensor-Research.md',
        'curated_id': 'EF-TEC-005',
        'title': 'Preferred parseable Grok sensor-research export',
        'role': 'Preferred historical sensor design-intent and component-research record; supersedes FireShot capture for retrieval',
        'packet_name': 'EF-TEC-005.md',
        'unique_value': 'This user-provided parseable export is the preferred readable record of the long historical Grok sensor-research conversation. It preserves the founder’s evolving hardware-module intent, changing component and cost constraints, sensor-technology questions, provisional field-grid/gateway reasoning, and custom-PCB exploration without forcing future users to retrieve a FireShot PDF.',
        'version_relationship': 'Preferred parseable retrieval representation for the historical sensor-research conversation previously captured through FireShot PDF and legacy text variants (SRC-0025, SRC-0026, SRC-0029, SRC-0036). It complements the separate alternatives-focused export EF-TEC-007 and remains historically bounded by later P0 feasibility and safety materials.',
        'archive_treatment': 'Use as primary evidence of historical founder intent, questions, design mechanics, and constraint evolution. Cite this Markdown source instead of the stale FireShot PDF for retrieval. Preserve its older captures as provenance aliases; require direct manufacturer, regulatory, engineering, safety, calibration, and field-validation evidence for every operational claim.',
        'limitations': 'This is an AI-assisted historical conversation, not a datasheet set, engineering design, approved BOM, safety case, RF compliance opinion, calibration report, procurement quote, or field trial. It contains contradictions and unverified claims about components, prices, availability, certifications, RF rules, interfaces, energy design, sensor spacing, agronomy, and architecture.',
    },
    {
        'source_id': 'SRC-0392',
        'file_name': 'Conversation2—EcoFarmModuleSensorAlternativesResearch.md',
        'curated_id': 'EF-TEC-007',
        'title': 'Companion Grok sensor-alternatives research export',
        'role': 'Historical component-alternatives and selection-criteria record',
        'packet_name': 'EF-TEC-007.md',
        'unique_value': 'This companion export uniquely preserves the founder’s explicit sensor-selection criteria and alternative-search questions for ambient temperature/humidity, direct NPK, and soil-temperature sensing, including the conflict between low cost, non-Chinese provenance, direct in-field NPK measurement, and field durability.',
        'version_relationship': 'Companion to EF-TEC-005 rather than a replacement for it. It narrows attention to selection constraints and alternatives; it is historical design reasoning that informs, but does not resolve, later feasibility, calibration, and qualification work.',
        'archive_treatment': 'Use as historical evidence of requirements, trade-offs, and open procurement questions. Cite it for its stated criteria and unresolved alternatives only; do not cite it as proof that a sensor exists, meets a specification, has a particular origin, or is deployable.',
        'limitations': 'This AI-assisted historical comparison contains retailer-derived and assumed technical claims, uncertain certifications, incomplete specifications, and unverified absence claims. It does not provide manufacturer validation, controlled comparison data, current price or availability, component qualification, soil-specific calibration, or field-performance evidence.',
    },
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def packet(source: dict, text: str) -> str:
    lines = text.split('\n')
    header = [
        '# EcoFarm Full-File Review Packet',
        '',
        '| Field | Value |',
        '|---|---|',
        f'| Curated ID | `{source["curated_id"]}` |',
        f'| Title | {source["title"]} |',
        '| Category | `03_technical_architecture_hardware_ai` |',
        f'| Legacy source | `{source["source_id"]}` |',
        f'| Public file | `03_technical_architecture_hardware_ai/{source["curated_id"]}__{source["file_name"].replace("—", "_").replace("-", "_").lower()}` |',
        '| Required review mode | `line_by_line_markdown_export` |',
        f'| Normalized review lines | {len(lines)} |',
        '',
        '> **Completion rule:** Read the complete content below. Do not mark this source reviewed from its title, heading, filename, hash, excerpt, or relationship. Record unique value, evidence status, version relationship, archive treatment, and limitations only after full review.',
        '',
        '## Line-numbered source content',
        '',
    ]
    header.extend(f'{number:06d} | {line}' for number, line in enumerate(lines, start=1))
    return '\n'.join(header) + '\n'


def ledger_entry(source: dict, source_path: str, line_count: int) -> dict:
    return {
        'curated_id': source['curated_id'],
        'source_id': source['source_id'],
        'title': source['title'],
        'category': '03_technical_architecture_hardware_ai',
        'github_relative_path': source_path,
        'review_mode': 'line_by_line_markdown_export',
        'review_packet': f'packets/{source["packet_name"]}',
        'line_count': line_count,
        'full_review_status': 'completed_individual_full_review',
        'unique_value': source['unique_value'],
        'evidence_status': 'Primary evidence of founder questions, constraints, reasoning, and tentative decisions at the time. Any surrounding technical, legal, market, agricultural, pricing, supplier, certification, component, safety, or performance claim is an unverified historical research assertion; this source does not evidence working hardware, compliant deployment, safe advice, availability, or validated feasibility.',
        'version_relationship': source['version_relationship'],
        'archive_treatment': source['archive_treatment'],
        'limitations': source['limitations'],
    }


def main() -> None:
    manifest = json.loads(MANIFEST_JSON.read_text(encoding='utf-8'))
    by_id = {entry['source_id']: entry for entry in manifest}
    ledger = json.loads(LEDGER_PATH.read_text(encoding='utf-8'))
    ledger_by_id = {entry['curated_id']: entry for entry in ledger}
    TEXT_ROOT.mkdir(exist_ok=True)
    PACKET_ROOT.mkdir(parents=True, exist_ok=True)

    for source in SOURCES:
        origin = UPLOAD / source['file_name']
        if not origin.exists():
            raise FileNotFoundError(origin)
        destination = ROOT / 'uploads' / source['file_name']
        shutil.copy2(origin, destination)
        text = destination.read_text(encoding='utf-8')
        (TEXT_ROOT / f'{source["source_id"]}.txt').write_text(text, encoding='utf-8')
        record = {
            'source_id': source['source_id'],
            'relative_path': f'uploads/{source["file_name"]}',
            'source_group': 'current_uploads',
            'file_name': source['file_name'],
            'extension': '.md',
            'bytes': destination.stat().st_size,
            'sha256': digest(destination),
            'duplicate_group': '',
            'duplicate_status': 'unique',
        }
        by_id[source['source_id']] = record
        source_path = '03_technical_architecture_hardware_ai/' + (
            'EF-TEC-005__grok_ecofarm_module_sensor_research.md'
            if source['curated_id'] == 'EF-TEC-005'
            else 'EF-TEC-007__conversation2_ecofarmmodulesensoralternativesresearch.md'
        )
        (PACKET_ROOT / source['packet_name']).write_text(packet(source, text), encoding='utf-8')
        ledger_by_id[source['curated_id']] = ledger_entry(source, source_path, len(text.split('\n')))

    ordered_manifest = sorted(by_id.values(), key=lambda item: int(item['source_id'].split('-')[1]))
    MANIFEST_JSON.write_text(json.dumps(ordered_manifest, indent=2) + '\n', encoding='utf-8')
    with MANIFEST_CSV.open('w', newline='', encoding='utf-8') as stream:
        fields = list(ordered_manifest[0].keys())
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(ordered_manifest)

    ordered_ledger = sorted(ledger_by_id.values(), key=lambda item: item['curated_id'])
    LEDGER_PATH.write_text(json.dumps(ordered_ledger, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'registered_sources': [source['source_id'] for source in SOURCES], 'reviewed_curated_sources': len(ordered_ledger)}, indent=2))


if __name__ == '__main__':
    main()
