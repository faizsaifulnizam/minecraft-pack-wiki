"""Export and check a fixed Markdown handbook. Python 3.11+, stdlib only.
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

PAGES = ('index.md','pack-map.md','mods.md','getting-started.md','troubleshooting.md','sources.md','changes.md','guides/recipe-search.md','guides/ae2-starter.md','guides/mi-starter.md')
SUPPORT = ('.gitignore','_config.yml','_layouts/default.html','assets/style.css','_data/baseline.json','tools/wiki.py','tests/check_wiki.py','README.md')
GENERATED = ('llms.txt','llms-full.txt') + tuple('text/'+p for p in PAGES)
ALLOWED = frozenset(PAGES + SUPPORT + GENERATED)
BASELINE = 'dev-0.5-20261015'
SNAPSHOT_SHA256 = '4fd53a0ffcefe03a0800e1e1f9a1ebfe6b3ec4f98e6f72fe1f14e04853d8710a'
HEADINGS = ('Baseline','Evidence status','Prerequisites','Steps','Expected result','Common failures','Sources')
LINK = re.compile(r'(?<!!)\[([^\]\n]+)\]\(([^\s)]+)\)')
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
    return re.sub(r'\s+', '-', re.sub(r'[^\w\s-]', '', heading.strip().lower()))

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
    if path.startswith('/') or '\\' in path:
        raise ValueError('unsafe local link '+href)
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

def public_files(root):
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
            elif rel not in ALLOWED:errors.append('unexpected public file: '+rel)
            else:files.append(rel)
    return sorted(files), errors

def source_errors(root):
    files, errors=public_files(root)
    for name in PAGES + SUPPORT:
        if name not in files:errors.append('missing required source: '+name)
    data={};permalinks=[]
    for name in PAGES:
        if name not in files:continue
        try:
            meta,body=read_page(root,name);data[name]=(meta,body);permalinks.append(meta['permalink'])
            if meta['layout']!='default' or meta['baseline']!=BASELINE or meta['permalink']!=page_url(name):
                errors.append('baseline/layout/permalink mismatch: '+name)
            if '{{' in body or '{%' in body or re.search(r'<\s*(?:script|iframe|object)\b',body,re.I):
                errors.append('unsafe/unresolved content: '+name)
            if PRIVATE.search(body) or any(PRIVATE.search(v) for v in meta.values()):errors.append('private content: '+name)
            if any(c in meta['title'] for c in ('<','>','[',']','\r','\n')):
                errors.append('unsafe page title: '+name)
            if name.startswith('guides/'):
                for heading in HEADINGS:
                    if '## '+heading not in body:errors.append('missing guide heading '+heading+': '+name)
        except (ValueError,UnicodeError) as exc:errors.append(str(exc))
    if len(set(permalinks)) != len(permalinks):errors.append('duplicate permalink')
    for name,(_,body) in data.items():
        for _,href in LINK.findall(body):
            try:
                target,fragment=local_target(name,href)
                if target is None:continue
                if target not in data:
                    errors.append('missing link target '+href+': '+name);continue
                if fragment:
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
    prefix=address(origin,base)
    index=['# Minecraft pack handbook','', '> Development snapshot '+BASELINE+'. Partial tutorial coverage; not runtime certification.','', 'Each entry links to a human page and a Markdown copy. URL access and context size depend on your model.','']
    combined=['# Minecraft pack handbook — combined text edition','', 'Baseline: '+BASELINE+'. Development reference, not a released or runtime-certified pack.','']
    outputs={}
    for name in PAGES:
        meta,body=read_page(root,name)
        def rewrite(match):
            label,href=match.groups();target,fragment=local_target(name,href)
            if target is None:return match[0]
            if target not in PAGES:raise ValueError('missing link target: '+href)
            return '['+label+']('+prefix+page_url(target)+('#'+fragment if fragment else '')+')'
        body=LINK.sub(rewrite,body)
        canonical=prefix+meta['permalink']
        exported='Source: '+canonical+'\nBaseline: '+BASELINE+'\n\n'+body
        outputs['text/'+name]=exported
        index.append('- ['+meta['title']+']('+canonical+') | [Markdown]('+prefix+'/text/'+name+')')
        combined.extend(['--- BEGIN PAGE: '+meta['title']+' ---',exported.rstrip(),'--- END PAGE: '+meta['title']+' ---',''])
    index.extend(['','[Combined text edition]('+prefix+'/llms-full.txt)',''])
    outputs['llms.txt']='\n'.join(index)
    outputs['llms-full.txt']='\n'.join(combined)
    return outputs

def export(root,origin,base):
    address(origin,base)
    errors=source_errors(root)
    if errors:raise ValueError('\n'.join(errors))
    outputs=expected_exports(root,origin,base)
    for name, content in outputs.items():
        if PRIVATE.search(content):raise ValueError('private prospective export: '+name)
    for name,content in outputs.items():
        p=root/name
        if p.is_symlink() or not p.resolve().is_relative_to(root.resolve()):raise ValueError('unsafe export path')
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(content,encoding='utf-8',newline='\n')
    return len(outputs)

def check(root,origin,base):
    address(origin,base)
    errors=source_errors(root)
    if errors:return errors
    for name,expected in expected_exports(root,origin,base).items():
        p=root/name
        if not p.is_file() or p.read_bytes()!=expected.encode('utf-8'):errors.append('missing or stale export: '+name)
    return errors

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
