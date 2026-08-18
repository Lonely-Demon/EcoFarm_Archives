from pathlib import Path
import html
import json
import re
import shutil
import markdown

SOURCE = Path('/home/ubuntu/projects/ecofarm-89bdc8ac/EcoFarm_Master_Knowledge_Base.md')
ARCHIVE = Path('/home/ubuntu/ecofarm_source_archive')
CURATED_ARCHIVE = Path('/home/ubuntu/ecofarm_curated_archive')
OUT = Path('/home/ubuntu/ecofarm_knowledge_html')
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

raw = SOURCE.read_text()
parts = re.split(r'(?m)^## (.+?)\n', raw)
prelude = parts[0]
sections = []
for i in range(1, len(parts), 2):
    title = parts[i].strip()
    body = parts[i + 1]
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    sections.append({'title': title, 'body': body, 'slug': slug, 'file': f'{slug}.html'})

md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc', 'sane_lists', 'nl2br'])
CURATED_INDEX = json.loads((CURATED_ARCHIVE / 'archive_metadata' / 'curated_source_index.json').read_text())
LLM_DOCUMENTS = json.loads((ARCHIVE / 'llm_knowledge_corpus' / 'EcoFarm_LLM_Knowledge_Documents.json').read_text())
LLM_BY_ID = {record['source_id']: record for record in LLM_DOCUMENTS}

CSS = '''
:root { --ink:#17251f; --muted:#5a6a61; --paper:#f7f5ed; --card:#fffdf7; --line:#d9ded4; --green:#23553d; --moss:#577259; --gold:#b2873d; --blue:#355f73; }
* { box-sizing:border-box; } body { margin:0; background:var(--paper); color:var(--ink); font:16px/1.65 Georgia, 'Times New Roman', serif; }
a { color:var(--green); text-decoration-thickness:1px; text-underline-offset:3px; } a:hover { color:var(--gold); }
.shell { min-height:100vh; display:grid; grid-template-columns:300px minmax(0, 1fr); }
aside { background:#18362a; color:#ebf0e8; padding:34px 24px; position:sticky; top:0; height:100vh; overflow:auto; }
.brand { font:600 27px/1.1 Georgia, serif; letter-spacing:.02em; color:#f8f5e9; margin:0 0 8px; } .sub { color:#b8c8ba; font:13px/1.45 Arial,sans-serif; margin:0 0 24px; }
.nav-title { margin:20px 0 8px; color:#9eb6a0; font:700 10px/1 Arial,sans-serif; letter-spacing:.13em; text-transform:uppercase; }
nav a { display:block; padding:8px 10px; margin:2px 0; border-radius:6px; color:#e5ede6; text-decoration:none; font:14px/1.3 Arial,sans-serif; } nav a:hover, nav a.active { background:#2f6048; color:#fff; }
.search { width:100%; border:1px solid #6f947c; border-radius:6px; padding:10px 11px; color:#162b20; background:#fdfdf8; font:14px Arial,sans-serif; }
main { max-width:1080px; padding:56px clamp(26px,6vw,88px) 90px; } .breadcrumb { font:12px Arial,sans-serif; letter-spacing:.06em; text-transform:uppercase; color:var(--moss); margin-bottom:22px; }
h1,h2,h3,h4 { color:#163c2a; line-height:1.2; } h1 { font-size:clamp(38px,5vw,62px); margin:0 0 20px; } h2 { margin:52px 0 18px; font-size:32px; } h3 { margin:38px 0 12px; font-size:24px; } h4 { margin:28px 0 10px; font-size:19px; }
p,li { max-width:84ch; } blockquote { margin:24px 0; padding:16px 21px; background:#edf2ea; border-left:4px solid var(--moss); color:#30483a; } hr { border:0; border-top:1px solid var(--line); margin:44px 0; }
table { display:block; width:100%; overflow:auto; border-collapse:collapse; margin:24px 0 32px; font-family:Arial,sans-serif; font-size:13px; background:var(--card); } th { background:#e6eee4; color:#18362a; text-align:left; } th,td { padding:11px 12px; border:1px solid var(--line); vertical-align:top; min-width:110px; }
code { padding:2px 5px; background:#eef0e9; border-radius:3px; font:12px/1.3 ui-monospace, SFMono-Regular, Consolas, monospace; } pre { background:#1c2e25; color:#ecf2e8; padding:18px; overflow:auto; }
.hero { background:linear-gradient(135deg,#183d2b,#315e45); color:#f9f6eb; padding:clamp(32px,6vw,74px); border-radius:16px; margin:0 0 40px; } .hero h1 { color:#fffdf4; } .hero p { color:#dce7dc; font-size:19px; }
.cards { display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:14px; margin:28px 0; } .card { background:var(--card); border:1px solid var(--line); padding:20px; border-radius:10px; box-shadow:0 2px 14px rgba(31,54,38,.05); } .card h3 { margin:0 0 8px; font:600 18px Georgia,serif; } .card p { margin:0; color:var(--muted); font-size:14px; }
.meta { font:13px Arial,sans-serif; color:var(--muted); border-top:1px solid var(--line); margin-top:50px; padding-top:18px; } .search-results { margin-top:12px; font:13px Arial,sans-serif; } .search-results a { display:block; color:#173c2a; background:#ecf2ea; padding:8px; margin:5px 0; border-radius:5px; } .source-entry { background:var(--card); border:1px solid var(--line); border-radius:8px; padding:12px 14px; margin:10px 0; } .source-entry summary { cursor:pointer; font:600 15px/1.4 Arial,sans-serif; color:#173c2a; } .source-entry p { margin:10px 0 0; font-size:14px; } .filter-buttons { display:flex; flex-wrap:wrap; gap:7px; margin:18px 0 30px; } .filter-buttons button { cursor:pointer; border:1px solid #8aa18b; background:#f4f7f1; color:#173c2a; padding:7px 10px; border-radius:999px; font:700 11px/1 Arial,sans-serif; letter-spacing:.03em; } .filter-buttons button:hover,.filter-buttons button.active { background:#23553d; color:#fff; border-color:#23553d; }
@media (max-width:880px) { .shell { display:block; } aside { position:relative; height:auto; padding:22px; } nav { columns:2; } nav a { break-inside:avoid; } main { padding:36px 24px 70px; } }
'''

JS = '''
async function searchKnowledge() {
  const query = document.getElementById('knowledge-search').value.trim().toLowerCase();
  const target = document.getElementById('search-results');
  if (!query) { target.innerHTML = ''; return; }
  const index = await fetch('search-index.json', {cache: 'no-store'}).then(r => r.json());
  const terms = query.split(/\s+/).filter(Boolean);
  const hits = index.filter(item => terms.every(term => item.search_text.includes(term))).slice(0, 12);
  target.innerHTML = hits.length ? hits.map(h => `<a href="${h.file}">${h.title}<br><small>${h.excerpt}</small></a>`).join('') : '<span>No matching section title or passage found.</span>';
}
function filterCuratedSources(prefix) {
  document.querySelectorAll('.filter-buttons button').forEach(button => button.classList.toggle('active', button.dataset.prefix === prefix));
  document.querySelectorAll('[data-source-prefix]').forEach(element => {
    element.style.display = (!prefix || element.dataset.sourcePrefix === prefix) ? '' : 'none';
  });
}
'''

def nav(current=None):
    links = ['<a href="index.html" class="%s">Knowledge Base Home</a>' % ('active' if current == 'index.html' else '')]
    for section in sections:
        active = 'active' if current == section['file'] else ''
        links.append(f'<a class="{active}" href="{section["file"]}">{html.escape(section["title"])}</a>')
    links.append('<a class="%s" href="sources.html">Source Catalogue</a>' % ('active' if current == 'sources.html' else ''))
    return '\n'.join(links)

def source_linkify(value):
    return re.sub(r'\[SRC-(\d{4})\]', lambda m: f'<a class="src-ref" href="sources.html#SRC-{m.group(1)}">[SRC-{m.group(1)}]</a>', value)

def layout(title, content, current):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} — EcoFarm Knowledge Base</title><link rel="stylesheet" href="styles.css"></head><body><div class="shell"><aside><p class="brand">EcoFarm</p><p class="sub">Master Knowledge Base<br>Human-readable HTML edition</p><input id="knowledge-search" class="search" placeholder="Search concepts, features, evidence…" oninput="searchKnowledge()"><div id="search-results" class="search-results"></div><p class="nav-title">Navigate</p><nav>{nav(current)}</nav><p class="nav-title">Reading rule</p><p class="sub">Treat historical visions, plans, and test artifacts according to their stated evidence status. Do not mistake a proposal for validation.</p></aside><main>{content}<p class="meta">EcoFarm Master Knowledge Base · Generated from the editable Markdown source · Internal source IDs resolve through the preserved corpus manifest and LLM retrieval files.</p></main></div><script src="search.js?v=20260818c"></script></body></html>'''

search = []
cards = []
for section in sections:
    md.reset()
    page_body = source_linkify(md.convert(f'# {section["title"]}\n\n{section["body"]}'))
    page = layout(section['title'], f'<p class="breadcrumb">EcoFarm Master Knowledge Base</p>{page_body}', section['file'])
    (OUT / section['file']).write_text(page)
    plain = re.sub(r'\s+', ' ', re.sub(r'[`#>*_\[\]\|]', ' ', section['body'])).strip()
    search.append({'title': section['title'], 'file': section['file'], 'excerpt': plain[:260], 'search_text': (section['title'] + ' ' + plain).lower()})
    cards.append(f'<a class="card" href="{section["file"]}"><h3>{html.escape(section["title"])}</h3><p>{html.escape(plain[:190])}…</p></a>')

md.reset()
intro = source_linkify(md.convert(prelude))
home = f'''<section class="hero"><p class="breadcrumb" style="color:#c6d7c7">Preserved · Non-final · Evidence-aware</p><h1>EcoFarm Master Knowledge Base</h1><p>A source-traceable map of EcoFarm’s vision, feature mechanics, mental models, research, technical reasoning, alternatives, and unresolved questions.</p></section>{intro}<h2>Browse the knowledge base</h2><div class="cards">{''.join(cards)}</div>'''
(OUT / 'index.html').write_text(layout('Home', home, 'index.html'))

source_groups = {}
for record in CURATED_INDEX:
    source_groups.setdefault((record['category_prefix'], record['category_directory']), []).append(record)
source_entries = []
for (prefix, directory), entries in sorted(source_groups.items()):
    source_entries.append(f'<h2 data-source-prefix="{prefix}">{html.escape(prefix)} — {html.escape(directory.replace("_", " ").title())}</h2>')
    for record in entries:
        legacy_ids = ', '.join(record['legacy_source_ids'])
        github_url = f'https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/{record["github_relative_path"]}'
        source_entries.append(f'''<details id="{record['curated_id']}" data-source-prefix="{record['category_prefix']}" class="source-entry"><summary><code>{record['curated_id']}</code> — {html.escape(record['title'])}</summary><p><strong>Role:</strong> {html.escape(record['role'])}<br><strong>Category:</strong> <code>{html.escape(record['category_directory'])}</code><br><strong>Legacy trace:</strong> <code>{html.escape(legacy_ids)}</code><br><a href="{github_url}">Open canonical file on GitHub</a></p></details>''')
filter_buttons = ['<button class="active" data-prefix="" onclick="filterCuratedSources(\'\')">All sources</button>']
for prefix, _ in sorted(source_groups):
    filter_buttons.append(f'<button data-prefix="{prefix}" onclick="filterCuratedSources(\'{prefix}\')">{prefix}</button>')
sources_body = '''<p class="breadcrumb">EcoFarm Master Knowledge Base / Curated Evidence Catalogue</p><h1>Curated Source Catalogue</h1><p>This catalogue contains only reviewed substantive EcoFarm sources. Workspace code, dependency files, generated builds, generic UI components, exact duplicate aliases, and low-signal archive noise have been excluded from ordinary browsing. Each record uses a category-aware <code>EF-*</code> identifier and links to its canonical file in the GitHub archive.</p><p><a href="data/CURATED_ARCHIVE_INDEX.md">Download curated source index</a> · <a href="data/EcoFarm_LLM_Knowledge_Documents.json">Download LLM document index</a> · <a href="data/EcoFarm_LLM_Topic_Index.json">Download LLM topic index</a></p><div class="filter-buttons">''' + ''.join(filter_buttons) + '</div>' + ''.join(source_entries)
(OUT / 'sources.html').write_text(layout('Source Catalogue', sources_body, 'sources.html'))
(OUT / 'data').mkdir(exist_ok=True)
shutil.copy2(ARCHIVE / 'llm_knowledge_corpus' / 'EcoFarm_LLM_Knowledge_Documents.json', OUT / 'data' / 'EcoFarm_LLM_Knowledge_Documents.json')
shutil.copy2(ARCHIVE / 'llm_knowledge_corpus' / 'EcoFarm_LLM_Topic_Index.json', OUT / 'data' / 'EcoFarm_LLM_Topic_Index.json')
shutil.copy2(CURATED_ARCHIVE / 'CURATED_ARCHIVE_INDEX.md', OUT / 'data' / 'CURATED_ARCHIVE_INDEX.md')
(OUT / 'styles.css').write_text(CSS)
(OUT / 'search.js').write_text(JS)
(OUT / 'search-index.json').write_text(json.dumps(search, indent=2))
(OUT / 'README.md').write_text(f'''# EcoFarm HTML Knowledge Base\n\nOpen `index.html` in a modern browser, or host this directory with any static server. The site has {len(sections) + 2} linked pages, client-side search, and a curated source catalogue. Citations in the article pages use category-aware `EF-*` IDs and link directly to canonical GitHub archive files. The catalogue intentionally excludes ordinary app code, dependency/configuration files, generated builds, and duplicate aliases. It is generated from `EcoFarm_Master_Knowledge_Base.md` using `build_html_knowledge_site.py`.\n''')
print(json.dumps({'pages': len(sections) + 2, 'output': str(OUT)}, indent=2))
