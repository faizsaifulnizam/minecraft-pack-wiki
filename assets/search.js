/* Static literal-token search; no network except same-origin index files. */
(function (root) {
  'use strict';
  const fold = value => String(value).normalize('NFKC').toLocaleLowerCase('en').replace(/[’‘]/g, "'");
  function rank(documents, query, filters = {}) {
    const q = fold(query).trim().slice(0, 160);
    if (!q) return [];
    const tokens = q.split(/\s+/).filter(Boolean);
    return documents.filter(d => (!filters.group || d.group === filters.group) && (!filters.kind || d.kind === filters.kind))
      .map((d, order) => {
        const title = fold(d.title), aliases = d.aliases.map(fold), text = fold(d.text);
        const haystack = [title, ...aliases, text].join(' ');
        if (!tokens.every(t => haystack.includes(t))) return null;
        const score = (title === q ? 100 : title.includes(q) ? 40 : 0) + (aliases.includes(q) ? 80 : 0) + tokens.reduce((n,t)=>n+(title.includes(t)?10:0)+(aliases.some(a=>a.includes(t))?5:0),0);
        return {doc:d, score, order};
      }).filter(Boolean).sort((a,b)=>b.score-a.score || a.order-b.order).slice(0,20).map(row=>row.doc);
  }
  function validateIndex(data, release, base) {
    if (!data || data.schema !== 1) throw new Error('Unsupported search schema');
    if (data.release !== release) throw new Error('Search release mismatch');
    if (!Array.isArray(data.documents) || data.documents.length > 50000) throw new Error('Search document limit');
    for (const d of data.documents) {
      if (!d || !['title','url','anchor','text','group','kind','evidence','spoiler'].every(k=>typeof d[k] === 'string') || !Array.isArray(d.aliases) || !d.aliases.every(a=>typeof a === 'string')) throw new Error('Invalid search document');
      let decoded;
      try { decoded = decodeURIComponent(d.url); } catch (_) { throw new Error('Invalid route encoding'); }
      if (!d.url.startsWith(base + '/') || d.url.startsWith('//') || /[\\?#\x00-\x20]/.test(decoded) || decoded.split('/').some(p=>p==='..'||p==='.') || !['safe','full'].includes(d.spoiler)) throw new Error('Invalid search route');
      if (!/^[\w-]*$/.test(d.anchor)) throw new Error('Invalid section anchor');
    }
    return data;
  }
  function excerpt(text, limit = 220) {
    const plain = String(text).replace(/!?\[([^\]]*)\]\([^)]*\)/g, '$1').replace(/[`*#]/g, '').replace(/\|/g, ' · ').replace(/\s+/g, ' ').trim();
    if (plain.length <= limit) return plain;
    const cut = plain.slice(0, limit - 1);
    return cut.slice(0, cut.lastIndexOf(' ') > 0 ? cut.lastIndexOf(' ') : cut.length).trimEnd() + '…';
  }
  const api = {rank, validateIndex, excerpt};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  if (!root.document) return;
  root.WikiSearch = api;
  const host = document.querySelector('[data-wiki-search]');
  if (!host) return;
  const form = host.querySelector('form'), input = host.querySelector('[name=q]');
  const include = host.querySelector('[name=spoilers]'), groups = host.querySelector('[name=group]');
  const kinds = host.querySelector('[name=kind]'), status = host.querySelector('[role=status]');
  const results = host.querySelector('ol'), clear = host.querySelector('[data-clear]');
  const base = host.dataset.base, release = host.dataset.release;
  let generation = 0;
  let safe = null, full = null;
  form.querySelectorAll('input,button,select').forEach(e=>{e.disabled=false;});
  status.textContent = 'Search titles, aliases, exact IDs and page text. Spoilers excluded.';
  async function load(withSpoilers) {
    if (withSpoilers ? full : safe) return withSpoilers ? full : safe;
    const path = withSpoilers ? host.dataset.full : host.dataset.safe;
    const response = await fetch(path, {credentials:'omit',redirect:'error'});
    if (!response.ok) throw new Error('Index unavailable');
    const data = validateIndex(await response.json(), release, base);
    if (!withSpoilers && data.documents.some(d=>d.spoiler!=='safe')) throw new Error('Invalid safe partition');
    if (withSpoilers) full = data; else safe = data;
    return data;
  }
  function reset() {
    generation++; include.checked=false; full=null; results.replaceChildren();
    status.textContent='Spoilers excluded. Search is ready.';
  }
  async function search() {
    const current = ++generation, withSpoilers=include.checked;
    results.replaceChildren();
    if (!input.value.trim()) { status.textContent='Enter a mod, item, ID or task.';return; }
    status.textContent='Loading search…';
    try {
      const data=await load(withSpoilers);
      if(current!==generation || withSpoilers!==include.checked) return;
      const matches=rank(data.documents,input.value,{group:groups.value,kind:kinds.value});
      for(const d of matches) {
        const li=document.createElement('li'), link=document.createElement('a'), p=document.createElement('p'), meta=document.createElement('small');
        link.href=d.url+(d.anchor?'#'+encodeURIComponent(d.anchor):'');link.textContent=d.title;
        p.textContent=excerpt(d.text);meta.textContent=[d.group,d.kind,d.evidence,d.spoiler==='full'?'FULL SPOILERS':''].filter(Boolean).join(' · ');
        li.append(link,p,meta);results.append(li);
      }
      status.textContent=matches.length ? `${matches.length} results shown (maximum 20). ${withSpoilers?'Full spoilers included.':'Spoilers excluded.'}` : 'No matches. Try a shorter term or browse the topic index.';
      // Keep only safe query/filter context in this tab's session storage.
      if(!withSpoilers) try { sessionStorage.setItem('wiki-safe-search',JSON.stringify({q:input.value,group:groups.value,kind:kinds.value})); } catch(_) {}
    } catch(_) {
      if(current===generation) status.textContent='Search unavailable or out of date. Use the topic index below.';
    }
  }
  form.addEventListener('submit',e=>{e.preventDefault();search();});
  include.addEventListener('change',()=>{generation++;results.replaceChildren();if(!include.checked)full=null;search();});
  [groups,kinds].forEach(e=>e.addEventListener('change',search));
  clear.addEventListener('click',()=>{reset();input.value='';groups.value='';kinds.value='';try{sessionStorage.removeItem('wiki-safe-search');}catch(_){}input.focus();});
  input.addEventListener('keydown',e=>{if(e.key==='Escape'){reset();input.focus();}});
  addEventListener('pagehide',reset);
  addEventListener('pageshow',e=>{
    reset();
    if(e.persisted) return;
    try { const previous=JSON.parse(sessionStorage.getItem('wiki-safe-search'));if(previous){input.value=String(previous.q||'').slice(0,160);groups.value=previous.group||'';kinds.value=previous.kind||'';} }catch(_){}
  });
  // Semantic native details remains fully usable without this enhancement.
  if(matchMedia('(max-width: 760px)').matches) document.querySelectorAll('[data-mobile-nav],[data-mobile-text]').forEach(e=>{e.open=false;});
})(typeof globalThis !== 'undefined' ? globalThis : this);
