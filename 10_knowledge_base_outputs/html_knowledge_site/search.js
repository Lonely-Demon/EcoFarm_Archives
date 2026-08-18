
async function searchKnowledge() {
  const query = document.getElementById('knowledge-search').value.trim().toLowerCase();
  const target = document.getElementById('search-results');
  if (!query) { target.innerHTML = ''; return; }
  const index = await fetch('search-index.json', {cache: 'no-store'}).then(r => r.json());
  const terms = query.split(/\s+/).filter(Boolean);
  const hits = index.filter(item => terms.every(term => item.search_text.includes(term))).slice(0, 12);
  target.innerHTML = hits.length ? hits.map(h => `<a href="${h.file}">${h.title}<br><small>${h.excerpt}</small></a>`).join('') : '<span>No matching section title or passage found.</span>';
}
