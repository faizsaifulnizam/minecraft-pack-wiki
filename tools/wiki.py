"""Export and check a reviewed-registry Markdown handbook. Python 3.11+, stdlib only.
Does not read the game instance, fetch URLs, install tools or render Jekyll.
"""
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, unquote
import argparse
import collections
import hashlib
import json
import os
import re
import stat
import sys

SUPPORT = ('.gitignore','_config.yml','_layouts/default.html','assets/style.css','_data/baseline.json','tools/wiki.py','tests/check_wiki.py','README.md','_data/pages.json')
BASELINE = 'dev-0.5-20261015-r2'
SNAPSHOT_SHA256 = 'ef6a652895e79928b17f4a6675f44f011e5172037146f31ecec34ddeaaf587ac'
HEADINGS = ('Baseline','Evidence status','Prerequisites','Steps','Expected result','Common failures','Sources')
LINK = re.compile(r'!?\[([^\]\n]*)\]\(([^\s)]+)\)')
PRIVATE = re.compile(r'(?:[A-Za-z]:[\\/](?:Users|Minecraft Modpack)[\\/]|/home/|/Users/|AppData[\\/]|-----BEGIN [A-Z ]*PRIVATE KEY-----|(?:ghp_|github_pat_)[A-Za-z0-9_]{16,})', re.I)

def address(origin, base):
    if not re.fullmatch(r'https?://[A-Za-z0-9.-]+(?::[0-9]+)?', origin):
        raise ValueError('site-url must be an explicit HTTP(S) origin, without path, credentials, query or fragment')
    parsed = urlsplit(origin)
    if not parsed.hostname or (parsed.port is not None and not 1 <= parsed.port <= 65535):
        raise ValueError('invalid origin host/port')
    if base and not re.fullmatch(r'/[A-Za-z0-9_-]+(?:/[A-Za-z0-9_-]+)*', base):
        raise ValueError('base-path must be empty or slash-prefixed segments, without a trailing slash')
    return origin + base

def read_page(root, name):
    text = (root/name).read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n(.*)\Z', text, re.S)
    if not match:
        raise ValueError('missing frontmatter: '+name)
    meta = {}
    for line in match[1].splitlines():
        key, sep, value = line.partition(':')
        if not sep or key in meta:
            raise ValueError('invalid/duplicate frontmatter key: '+name)
        meta[key] = value.strip().strip('"')
    if set(meta) != {'layout','title','permalink','baseline'}:
        raise ValueError('unexpected frontmatter fields: '+name)
    return meta, match[2].strip()+'\n'

def slug(heading):
    return re.sub(r'[^\w-]', '', re.sub(r'\s', '-', heading.strip().lower()))

def page_url(name):
    return '/' if name == 'index.md' else '/'+name[:-3]+'/'

def local_target(name, href):
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        if parsed.scheme not in ('https','http') or not parsed.netloc or parsed.username or parsed.password:
            raise ValueError('unsafe link '+href)
        return None, ''
    if parsed.query:
        raise ValueError('unsupported query in local link '+href)
    path = unquote(parsed.path)
    if '\\' in path or re.search(r'[\x00-\x20]',href):
        raise ValueError('unsafe local link '+href)
    if path.startswith('/'):
        if '..' in path.split('/') or '.' in path.split('/'):raise ValueError('unsafe traversal '+href)
        if path=='/':return 'index.md',unquote(parsed.fragment)
        if path.endswith('/'):return path.strip('/')+'.md',unquote(parsed.fragment)
        return path.lstrip('/'),unquote(parsed.fragment)
    parts = list(PurePosixPath(name).parent.parts)
    if not path:
        return name, unquote(parsed.fragment)
    for part in path.split('/'):
        if part in ('','.'):continue
        if part == '..':
            if not parts:raise ValueError('unsafe traversal '+href)
            parts.pop()
        else:parts.append(part)
    return '/'.join(parts), unquote(parsed.fragment)

def linked(path):
    # lstat reparse attributes cover Windows junctions on Python 3.11 too.
    return path.is_symlink() or bool(getattr(path.lstat(), 'st_file_attributes', 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT)

def unique_object(pairs):
    result={}
    for key,value in pairs:
        if key in result:raise ValueError('duplicate JSON field: '+key)
        result[key]=value
    return result

def registry(root):
    path=root/'_data/pages.json'
    if linked(root) or linked(path.parent) or linked(path):raise ValueError('unsafe linked registry')
    doc=json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=unique_object)
    fields={'source','id','group','kind','mods','aliases','spoiler','evidence','reviewed'}
    if set(doc)!={'schema','pages'} or type(doc['schema']) is not int or doc['schema']!=1 or not isinstance(doc['pages'],list) or not doc['pages']:
        raise ValueError('invalid registry schema')
    sources=set();ids=set()
    for row in doc['pages']:
        if not isinstance(row,dict) or set(row)!=fields:raise ValueError('unknown/missing registry fields')
        for key in ('source','id','group','kind','spoiler','evidence'):
            if not isinstance(row[key],str) or not row[key]:raise ValueError('invalid registry '+key)
        if not re.fullmatch(r'[a-z0-9_-]+(?:/[a-z0-9_-]+)*\.md',row['source']):raise ValueError('unsafe registry source')
        if not all(re.fullmatch(r'[a-z0-9_-]+',row[k]) for k in ('id','group','kind')):raise ValueError('unsafe registry identifier')
        if row['source'].startswith('full/'):raise ValueError('reserved generated full route namespace')
        if row['source'] in sources or row['id'] in ids:raise ValueError('duplicate registry source/id')
        sources.add(row['source']);ids.add(row['id'])
        if row['spoiler'] not in ('safe','full') or row['evidence'] not in ('documented-static','not-runtime-tested','unknown') or row['reviewed'] is not True:raise ValueError('unreviewed/invalid registry status')
        for key in ('mods','aliases'):
            if not isinstance(row[key],list) or any(not isinstance(v,str) or not v or any(c in v for c in '<>\r\n') for v in row[key]):raise ValueError('invalid registry '+key)
        values=[row[k] for k in ('source','id','group','kind','spoiler','evidence')]+row['mods']+row['aliases']
        if any(PRIVATE.search(v) for v in values):raise ValueError('private registry metadata')
    return doc['pages']

def full_name(row):
    return 'full/'+row['id']+'.md'

def human_url(row):
    return page_url(full_name(row) if row['spoiler']=='full' else row['source'])

def generated_names(rows):
    return {full_name(r) for r in rows if r['spoiler']=='full'} | set(('llms.txt','llms-safe.txt','llms-full.txt','assets/search-safe.json','assets/search-full.json','_data/release.json')) | {'text/'+r['source'] for r in rows} | {'text/groups/'+r['group']+'-'+mode+'.txt' for r in rows for mode in ('safe','full')}

def full_header(name):
    return '---\nlayout: default\ntitle: "FULL SPOILERS"\npermalink: '+page_url(name)+'\nbaseline: '+BASELINE+'\n---\n<!-- wiki.py managed full human schema=1 -->\n'

def owned_full(name, content):
    return bool(re.fullmatch(r'full/[a-z0-9_-]+\.md',name)) and content.startswith(full_header(name))

def stale_owned(root, outputs):
    # Only our exact export header identifies ownership; unknown files never get deleted.
    stale=[]
    text=root/'text'
    if text.exists() and not linked(text):
        for current,dirs,names in os.walk(text,followlinks=False):
            dirs[:]=[d for d in dirs if not linked(Path(current)/d)]
            for filename in names:
                p=Path(current)/filename
                if p.suffix not in ('.md','.txt') or linked(p):continue
                name=p.relative_to(root).as_posix()
                content=p.read_text(encoding='utf-8')
                owned=(p.suffix=='.md' and content.startswith('<!-- wiki.py managed raw export schema=1 -->\nSource: http')) or (name.startswith('text/groups/') and p.suffix=='.txt' and content.startswith('<!-- wiki.py managed group export schema=1 -->\n'))
                if name not in outputs and owned:stale.append(name)
    full=root/'full'
    if full.exists() and not linked(full):
        for p in full.glob('*.md'):
            if not linked(p) and p.is_file() and p.relative_to(root).as_posix() not in outputs and owned_full(p.relative_to(root).as_posix(),p.read_text(encoding='utf-8')):
                stale.append(p.relative_to(root).as_posix())
    return sorted(stale)

def public_files(root, allowed=None):
    if allowed is None:allowed=set(SUPPORT)|set(r['source'] for r in registry(root))|generated_names(registry(root))
    files=[]; errors=[]
    for current, dirs, names in os.walk(root, followlinks=False):
        for d in list(dirs):
            p=Path(current)/d
            if linked(p):
                errors.append('unsafe linked directory: '+p.relative_to(root).as_posix());dirs.remove(d)
            elif d in ('.git','__pycache__','_site','.jekyll-cache','.superpowers'):
                dirs.remove(d)
        for name in names:
            p=Path(current)/name;rel=p.relative_to(root).as_posix()
            if linked(p):errors.append('unsafe linked file: '+rel)
            elif rel not in allowed:errors.append('unexpected public file: '+rel)
            else:files.append(rel)
    return sorted(files), errors

def source_errors(root):
    try:rows=registry(root)
    except (OSError,ValueError,TypeError,KeyError) as exc:return ['registry: '+str(exc)]
    PAGES=tuple(r['source'] for r in rows)
    GENERATED=generated_names(rows)
    files, errors=public_files(root,set(PAGES)|set(SUPPORT)|GENERATED|set(stale_owned(root,GENERATED))|{'assets/search.js'})
    for name in PAGES + SUPPORT:
        if name not in files:errors.append('missing required source: '+name)
    data={};permalinks=[]
    for name in PAGES:
        if name not in files:continue
        try:
            meta,body=read_page(root,name);data[name]=(meta,body);permalinks.append(meta['permalink'])
            if meta['layout']!='default' or meta['baseline']!=BASELINE or meta['permalink']!=page_url(name):
                errors.append('baseline/layout/permalink mismatch: '+name)
            starts={m.start() for m in LINK.finditer(body)}
            if any(m.start() not in starts for m in re.finditer(r'!?\[[^\]\n]*\]\(',body)):errors.append('unsupported inline link syntax: '+name)
            if re.search(r'^\s*\[[^\]]+\]:',body,re.M):errors.append('unsupported reference link syntax: '+name)
            if '{{' in body or '{%' in body or '{:' in body or re.search(r'<\s*/?\s*[A-Za-z][^>]*>',body):
                errors.append('unsafe/unresolved content: '+name)
            if PRIVATE.search(body) or any(PRIVATE.search(v) for v in meta.values()):errors.append('private content: '+name)
            if any(c in meta['title'] for c in ('<','>','[',']','\r','\n')):
                errors.append('unsafe page title: '+name)
            if name.startswith('guides/'):
                for heading in HEADINGS:
                    if '## '+heading not in body:errors.append('missing guide heading '+heading+': '+name)
        except (ValueError,UnicodeError) as exc:errors.append(str(exc))
    if len(set(permalinks)) != len(permalinks):errors.append('duplicate permalink')
    by_source={r['source']:r for r in rows}
    for name,(_,body) in data.items():
        if by_source[name]['spoiler']=='safe':
            for row in rows:
                if row['spoiler']=='full' and any(alias in body for alias in row['aliases']):errors.append('full-spoiler alias in safe manuscript: '+name)
        for _,href in LINK.findall(body):
            try:
                target,fragment=local_target(name,href)
                if target is None:continue
                if target not in data:
                    errors.append('missing link target '+href+': '+name);continue
                if fragment:
                    if by_source[name]['spoiler']=='safe' and by_source[target]['spoiler']=='full':errors.append('full-spoiler anchor in safe manuscript: '+name)
                    anchors={slug(h) for h in re.findall(r'^#{1,6}\s+(.+)$',data[target][1],re.M)}
                    if fragment not in anchors:errors.append('missing anchor '+href+': '+name)
            except ValueError as exc:errors.append(str(exc)+': '+name)
    try:
        baseline=json.loads((root/'_data/baseline.json').read_text(encoding='utf-8'))
        digest=hashlib.sha256(json.dumps(baseline, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode('utf-8')).hexdigest()
        if digest != SNAPSHOT_SHA256:raise ValueError('approved snapshot identity differs; review changes before rebasing')
        rows=baseline['mods']; active=[m for m in rows if m['status']=='active']; disabled=[m for m in rows if m['status']=='disabled']
        if (baseline['minecraft'],baseline['loader'],baseline['baseline_id'])!=('1.21.1','21.1.250',BASELINE):raise ValueError('platform/ID')
        if (len(active),len(disabled),sum(len(m['identities']) for m in active))!=(120,2,121):raise ValueError('population')
        if (baseline['active_archives'],baseline['disabled_archives'],baseline['active_mod_ids'])!=(120,2,121):raise ValueError('declared population')
        if len(rows)!=122 or len({m['filename'] for m in rows})!=122:raise ValueError('duplicate archive')
        for m in rows:
            if set(m)!={'filename','sha256','status','role','identities','metadata_status'}:raise ValueError('unsafe row fields')
            if not re.fullmatch(r'[a-f0-9]{64}',m['sha256']):raise ValueError('archive hash')
            if m['filename'] not in data.get('mods.md',({},''))[1]:raise ValueError('mod page incomplete')
            for identity in m['identities']:
                if set(identity)!={'id','name','version'}:raise ValueError('unsafe identity fields')
                if identity['id'] not in data.get('mods.md',({},''))[1]:raise ValueError('mod identity absent from reference')
    except (OSError,ValueError,KeyError,TypeError) as exc:errors.append('baseline validation: '+str(exc))
    for name in files:
        if name in ('tools/wiki.py','tests/check_wiki.py') or name in PAGES or name in GENERATED:continue
        try:
            if PRIVATE.search((root/name).read_text(encoding='utf-8')):errors.append('private content: '+name)
        except UnicodeError:errors.append('non-text public payload: '+name)
    return errors

def expected_exports(root,origin,base):
    prefix=address(origin,base);rows=registry(root)
    pages={r['source']:read_page(root,r['source']) for r in rows}
    by_source={r['source']:r for r in rows}
    safe_names={r['source'] for r in rows if r['spoiler']=='safe'}
    outputs={};documents=[];safe=[];full=['# FULL SPOILERS — combined text edition',''];groups={g:{'safe':[],'full':[]} for g in sorted({r['group'] for r in rows})}
    index=['# Minecraft pack handbook','', '[Safe text edition]('+prefix+'/llms-safe.txt)', '[FULL SPOILERS text edition]('+prefix+'/llms-full.txt)','']
    for row in rows:
        name=row['source'];meta,body=pages[name]
        def rewrite(match, human=False):
            label,href=match.groups();target,fragment=local_target(name,href)
            if target is None:return match[0]
            if target not in pages:raise ValueError('missing link target: '+href)
            if row['spoiler']=='safe' and target not in safe_names:return '[Full-spoiler content omitted]'
            return ('!' if match[0].startswith('!') else '')+'['+label+']('+(base if human else prefix)+human_url(by_source[target])+('#'+fragment if fragment else '')+')'
        exported_body=LINK.sub(rewrite,body)
        canonical=prefix+human_url(row)
        if row['spoiler']=='full':
            outputs[full_name(row)]=full_header(full_name(row))+'**FULL SPOILERS**\n\nWARNING: FULL SPOILERS. Direct links, reload and history may reveal everything here; this distinct full-human route is exempt from ordinary-entry consent/reset guarantees.\n\n[Return to safe entry]('+base+meta['permalink']+')\n\n'+LINK.sub(lambda m: rewrite(m,True),body)
        warning='WARNING: FULL SPOILERS. This text may reveal progression and outcomes.\n' if row['spoiler']=='full' else ''
        exported='<!-- wiki.py managed raw export schema=1 -->\nSource: '+canonical+'\nBaseline: '+BASELINE+'\nSpoiler: '+row['spoiler']+'\n'+warning+'\n'+exported_body
        outputs['text/'+name]=exported
        block=['--- BEGIN PAGE: '+meta['title']+' ---',exported.rstrip(),'--- END PAGE: '+meta['title']+' ---','']
        full.extend(block);groups[row['group']]['full'].extend(block)
        if row['spoiler']=='safe':
            groups[row['group']]['safe'].extend(block)
            safe.extend(block);index.append('- ['+meta['title']+']('+canonical+') | [Markdown]('+prefix+'/text/'+name+')')
        sections=re.split(r'^#{1,6}\s+(.+)$',exported_body,flags=re.M)
        chunks=[('',sections[0])]+[(sections[i],sections[i+1]) for i in range(1,len(sections),2)]
        counts=collections.Counter()
        for heading,text in chunks:
            anchor=slug(heading) if heading else ''
            if anchor:
                n=counts[anchor];counts[anchor]+=1
                if n:anchor+='-'+str(n)
            documents.append(dict(title=meta['title']+(' — '+heading if heading else ''),url=base+human_url(row),anchor=anchor,text=text.strip(),aliases=row['aliases']+row['mods']+[row['id']],group=row['group'],kind=row['kind'],evidence=row['evidence'],spoiler=row['spoiler']))
    for group,modes in groups.items():
        for mode,blocks in modes.items():
            outputs['text/groups/'+group+'-'+mode+'.txt']='<!-- wiki.py managed group export schema=1 -->\n# '+('Safe' if mode=='safe' else 'FULL SPOILERS')+' group bundle\n\n'+'\n'.join(blocks)
    outputs['llms.txt']='\n'.join(index)+'\n'
    outputs['llms-safe.txt']='# Safe text edition\n\n'+'\n'.join(safe)
    outputs['llms-full.txt']='\n'.join(full)
    release=hashlib.sha256(json.dumps({'rows':rows,'outputs':outputs,'documents':documents,'origin':origin,'base':base},sort_keys=True,ensure_ascii=True,separators=(',',':')).encode()).hexdigest()
    for mode in ('safe','full'):
        outputs['assets/search-'+mode+'.json']=json.dumps(dict(schema=1,release=release,documents=[d for d in documents if mode=='full' or d['spoiler']=='safe']),ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    outputs['_data/release.json']=json.dumps(dict(schema=1,id=release),sort_keys=True)+'\n'
    safe_payload='\n'.join(outputs[n] for n in ('llms.txt','llms-safe.txt','assets/search-safe.json'))
    for row in rows:
        if row['spoiler']=='full':
            meta,body=pages[row['source']]
            for secret in [meta['title'],body.strip()]+row['aliases']:
                if secret and secret in safe_payload:raise ValueError('full-spoiler metadata/body leaked into safe export; review safe source')
    return outputs

def export(root,origin,base):
    address(origin,base)
    errors=source_errors(root)
    if errors:raise ValueError('\n'.join(errors))
    outputs=expected_exports(root,origin,base)
    for name, content in outputs.items():
        if PRIVATE.search(content):raise ValueError('private prospective export: '+name)
    stale=stale_owned(root,outputs)
    for name in list(outputs)+stale:
        p=root/name
        if p.exists() and not p.is_file():raise ValueError('unsafe export target type: '+name)
        if p.exists() and linked(p):raise ValueError('unsafe export path')
        if name.startswith('full/') and p.is_file() and not owned_full(name,p.read_text(encoding='utf-8')):raise ValueError('unowned full route collision: '+name)
        if not p.resolve().is_relative_to(root.resolve()):raise ValueError('unsafe export path')
        for parent in p.parents:
            if parent==root:break
            if parent.exists() and (linked(parent) or not parent.is_dir()):raise ValueError('unsafe export directory')
    for name,content in outputs.items():
        p=root/name
        if p.is_symlink() or not p.resolve().is_relative_to(root.resolve()):raise ValueError('unsafe export path')
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(content,encoding='utf-8',newline='\n')
    for name in stale:(root/name).unlink()
    return len(outputs)

def check(root,origin,base):
    address(origin,base)
    errors=source_errors(root)
    if errors:return errors
    try:outputs=expected_exports(root,origin,base)
    except (OSError,ValueError) as exc:return ['export generation: '+str(exc)]
    errors.extend('stale managed export: '+n for n in stale_owned(root,outputs))
    for name,expected in outputs.items():
        p=root/name
        if not p.is_file() or p.read_bytes()!=expected.encode('utf-8'):errors.append('missing or stale export: '+name)
    return errors

def __getattr__(name):
    # Compatibility introspection only; caller-root operations always load their own registry.
    rows=registry(Path(__file__).resolve().parents[1])
    if name=='PAGES':return tuple(r['source'] for r in rows)
    if name=='GENERATED':return tuple(sorted(generated_names(rows)))
    if name=='ALLOWED':return frozenset(SUPPORT)|generated_names(rows)|{r['source'] for r in rows}|{'assets/search.js'}
    raise AttributeError(name)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=('export','check'))
    parser.add_argument('--site-url',required=True)
    parser.add_argument('--base-path',required=True)
    args=parser.parse_args();root=Path(__file__).resolve().parents[1]
    try:
        if args.command=='export':print('Exported',export(root,args.site_url,args.base_path),'deterministic text files')
        else:
            errors=check(root,args.site_url,args.base_path)
            if errors:
                print('\n'.join(errors));return 1
            print('PASS: content, baseline, links, public allowlist and exact text-export parity')
    except (OSError,ValueError) as exc:
        print('ERROR:',exc,file=sys.stderr);return 1
    return 0

if __name__=='__main__':
    raise SystemExit(main())
