"""Run from any directory: python tests/check_wiki.py. Standard library only."""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAGES = ('index.md', 'pack-map.md', 'mods.md', 'getting-started.md', 'troubleshooting.md', 'sources.md', 'changes.md', 'guides/recipe-search.md', 'guides/ae2-starter.md', 'guides/mi-starter.md')

class ContentTests(unittest.TestCase):
    def test_safe_complete_baseline(self):
        path = ROOT/'_data/baseline.json'
        self.assertTrue(path.is_file(), 'safe baseline has not been generated')
        baseline = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual((baseline['minecraft'], baseline['loader']), ('1.21.1', '21.1.250'))
        self.assertEqual((baseline['active_archives'], baseline['disabled_archives'], baseline['active_mod_ids']), (120, 2, 121))
        mods = baseline['mods']
        self.assertEqual(len(mods), 122)
        self.assertEqual(len({m['filename'] for m in mods}), 122)
        self.assertEqual(sum(len(m['identities']) for m in mods if m['status']=='active'), 121)
        kotlin = next(m for m in mods if m['filename']=='kotlinforforge-5.12.0-all.jar')
        self.assertEqual(kotlin['identities'], [])
        self.assertEqual(kotlin['metadata_status'], 'no_mod_metadata')
        self.assertNotIn('C:/Users/', json.dumps(baseline))
        self.assertTrue(all(set(m)=={'filename','sha256','status','role','identities','metadata_status'} for m in mods))

    def test_all_pages_and_tutorial_contract(self):
        for name in PAGES:
            self.assertTrue((ROOT/name).is_file(), name)
        for name in PAGES:
            text = (ROOT/name).read_text(encoding='utf-8')
            self.assertIn('baseline: dev-0.5-20261015-r2', text, name)
            if name.startswith('guides/'):
                for heading in ('Baseline','Evidence status','Prerequisites','Steps','Expected result','Common failures','Sources'):
                    self.assertIn('## '+heading, text, name)
        text = (ROOT/'pack-map.md').read_text(encoding='utf-8')
        self.assertIn('Unknown', text)
        self.assertIn('awakening', text)
        self.assertIn('evolution', text)
        home=(ROOT/'index.md').read_text(encoding='utf-8')
        self.assertNotIn('You do not need to complete technology before trying magic or character progression.', home)

import importlib.util
import shutil
import tempfile
import os
import subprocess
# Test copies belong in the agent scratch directory, not the system temp tree.
tempfile.tempdir = os.environ.get('TMPDIR') or (str(Path(os.environ.get('LOCALAPPDATA',str(Path.home()/'AppData/Local')))/'hermes/cache/scratch') if os.name=='nt' else None)
if tempfile.tempdir:Path(tempfile.tempdir).mkdir(parents=True,exist_ok=True)

def link_directory(target, link):
    try:os.symlink(target,link,target_is_directory=True)
    except OSError:
        if os.name!='nt':raise
        result=subprocess.run(['cmd','/c','mklink','/J',str(link),str(target)],capture_output=True,text=True)
        if result.returncode:raise OSError(result.stdout+result.stderr)

class ExportTests(unittest.TestCase):
    def tool(self):
        path = ROOT/'tools/wiki.py'
        self.assertTrue(path.is_file(), 'export/check implementation is missing')
        spec = importlib.util.spec_from_file_location('wiki_tool', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def fixture(self, root):
        shutil.copytree(ROOT, root, dirs_exist_ok=True, ignore=shutil.ignore_patterns('.git','__pycache__','_site','.jekyll-cache'))
        return root

    def test_project_base_path_and_nested_links(self):
        tool = self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(Path(tmp))
            tool.export(root, 'https://example.org', '/minecraft-pack-wiki')
            self.assertEqual(tool.check(root, 'https://example.org', '/minecraft-pack-wiki'), [])
            index = (root/'llms.txt').read_text(encoding='utf-8')
            self.assertIn('https://example.org/minecraft-pack-wiki/guides/recipe-search/', index)
            guide = (root/'text/guides/ae2-starter.md').read_text(encoding='utf-8')
            self.assertIn('https://example.org/minecraft-pack-wiki/guides/recipe-search/', guide)
            self.assertNotIn('layout: default', guide)
            self.assertNotIn('{{', guide)
            self.assertIn('dev-0.5-20261015-r2', guide)

    def test_root_origin_deterministic_parity_and_literal_ids(self):
        tool = self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(Path(tmp))
            for base in ('','/minecraft-pack-wiki'):
                tool.export(root, 'https://example.org', base)
                first = (root/'llms-full.txt').read_bytes()
                tool.export(root, 'https://example.org', base)
                self.assertEqual(first, (root/'llms-full.txt').read_bytes())
                self.assertEqual(tool.check(root,'https://example.org',base), [])
                self.assertIn(b'ae2',first)
                self.assertIn(b'tensuraleveling',first)

    def test_stale_export_is_rejected(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));tool.export(root,'https://example.org','/pack')
            (root/'text/pack-map.md').write_text('stale',encoding='utf-8')
            self.assertTrue(any('export' in e for e in tool.check(root,'https://example.org','/pack')))

    def test_broken_link_and_anchor_are_rejected(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));p=root/'index.md'
            p.write_text(p.read_text(encoding='utf-8')+'\n[Missing](missing.md)\n[Bad anchor](pack-map.md#missing-heading)\n',encoding='utf-8')
            errors=tool.check(root,'https://example.org','/pack')
            self.assertTrue(any('missing.md' in e for e in errors))
            self.assertTrue(any('missing-heading' in e for e in errors))

    def test_private_path_is_rejected(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));p=root/'index.md'
            p.write_text(p.read_text(encoding='utf-8')+'\nC:/Users/Example/private\n',encoding='utf-8')
            self.assertTrue(any('private' in e.lower() for e in tool.check(root,'https://example.org','')))

    def test_invalid_counts_and_duplicate_permalink_are_rejected(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));p=root/'_data/baseline.json'
            doc=json.loads(p.read_text(encoding='utf-8'));doc['active_archives']=119;p.write_text(json.dumps(doc),encoding='utf-8')
            q=root/'pack-map.md';q.write_text(q.read_text(encoding='utf-8').replace('permalink: /pack-map/','permalink: /'),encoding='utf-8')
            errors=tool.check(root,'https://example.org','')
            self.assertTrue(any('baseline' in e for e in errors))
            self.assertTrue(any('permalink' in e for e in errors))

    def test_bad_address_arguments_rejected(self):
        tool=self.tool()
        for origin,base in (('', ''),('file:///private',''),('https://example.org/path',''),('https://user:pass@example.org',''),('https://example.org','../pack'),('https://example.org','/pack/'),('https://example.org','//pack'),('https://example.org','/a/../b')):
            with self.subTest(origin=origin,base=base):
                with self.assertRaises(ValueError):tool.address(origin,base)

    def test_unexpected_public_file_rejected(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));(root/'private-receipt.json').write_text('{}',encoding='utf-8')
            self.assertTrue(any('unexpected' in e for e in tool.check(root,'https://example.org','')))

    def test_no_python312_junction_api_required(self):
        from unittest.mock import patch
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp))
            with patch.object(Path, 'is_junction', side_effect=AttributeError('Python 3.11 has no is_junction'), create=True):
                tool.export(root,'https://example.org','')
                self.assertEqual(tool.check(root,'https://example.org',''), [])

    def test_private_title_rejected_before_any_export_write(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp))
            before={n:(root/n).read_bytes() for n in tool.GENERATED}
            p=root/'index.md'
            p.write_text(p.read_text(encoding='utf-8').replace('title: "Minecraft pack handbook"','title: "C:/Users/Example/private"'),encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'private'):
                tool.export(root,'https://example.org','')
            self.assertEqual(before,{n:(root/n).read_bytes() for n in tool.GENERATED})

    def test_corrected_source_can_replace_unsafe_stale_export(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp))
            (root/'llms.txt').write_text('C:/Users/Example/private',encoding='utf-8')
            tool.export(root,'https://example.org','')
            self.assertEqual(tool.check(root,'https://example.org',''), [])

    def test_changed_snapshot_hash_or_version_is_rejected(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));p=root/'_data/baseline.json'
            original=json.loads(p.read_text(encoding='utf-8'))
            import copy
            for field in ('sha256','version'):
                doc=copy.deepcopy(original)
                if field=='sha256':doc['mods'][0]['sha256']='0'*64
                else:doc['mods'][0]['identities'][0]['version']='0.0.0-incorrect'
                p.write_text(json.dumps(doc),encoding='utf-8')
                with self.subTest(field=field):
                    self.assertTrue(any('snapshot' in e for e in tool.source_errors(root)))

    def test_dark_print_resets_tokens(self):
        css=(ROOT/'assets/style.css').read_text(encoding='utf-8')
        print_css=css.split('@media print',1)[1]
        self.assertIn('--ink:#000',print_css)
        self.assertIn('--muted:#222',print_css)
        self.assertIn('--paper:#fff',print_css)
        self.assertIn('--tint:#fff',print_css)

    def test_unsafe_link_rejected(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));p=root/'index.md'
            p.write_text(p.read_text(encoding='utf-8')+'\n[Bad](javascript:alert)\n',encoding='utf-8')
            self.assertTrue(any('unsafe' in e for e in tool.check(root,'https://example.org','')))

class RegistryTests(unittest.TestCase):
    tool = ExportTests.tool
    fixture = ExportTests.fixture
    def test_registry_strict_and_no_write(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp)); p=root/'_data/pages.json'
            self.assertTrue(p.exists(), 'reviewed registry missing')
            original=json.loads(p.read_text(encoding='utf-8'))
            for change in ('duplicate','unknown','traversal','private','private-backslash'):
                doc=json.loads(json.dumps(original))
                if change=='duplicate':doc['pages'].append(doc['pages'][0])
                elif change=='unknown':doc['pages'][0]['secret']='x'
                elif change=='traversal':doc['pages'][0]['source']='../outside.md'
                elif change=='private-backslash':doc['pages'][0]['aliases']=[r'C:\Users\Example\private']
                else:doc['pages'][0]['aliases']=['C:/Users/Example/private']
                p.write_text(json.dumps(doc),encoding='utf-8')
                before={f.relative_to(root).as_posix():f.read_bytes() for f in root.rglob('*') if f.is_file()}
                with self.assertRaises(ValueError):tool.export(root,'https://example.org','/pack')
                self.assertEqual(before,{f.relative_to(root).as_posix():f.read_bytes() for f in root.rglob('*') if f.is_file()})

    def test_safe_full_sections_release_and_reclassification(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));p=root/'_data/pages.json'
            self.assertTrue(p.exists(), 'reviewed registry missing')
            doc=json.loads(p.read_text(encoding='utf-8'));row=next(r for r in doc['pages'] if r['source']=='changes.md')
            row['spoiler']='full';row['aliases']=['SECRET_ALIAS'];p.write_text(json.dumps(doc),encoding='utf-8')
            q=root/'changes.md';q.write_text(q.read_text(encoding='utf-8').replace('title:','title:').replace('title: "Changes"','title: "SECRET_TITLE"')+'\n## Exact ae2:controller / MI!\nSECRET_BODY ae2:controller\n',encoding='utf-8')
            tool.export(root,'https://example.org','/pack')
            for name in ('llms-safe.txt','assets/search-safe.json','llms.txt'):
                text=(root/name).read_text(encoding='utf-8')
                for token in ('SECRET_ALIAS','SECRET_BODY','SECRET_TITLE'):self.assertNotIn(token,text)
            full=json.loads((root/'assets/search-full.json').read_text(encoding='utf-8'))
            self.assertTrue(any('ae2:controller' in d['text'] and d['anchor']=='exact-ae2controller--mi' for d in full['documents']))
            self.assertTrue(all(set(d)=={'title','url','anchor','text','aliases','group','kind','evidence','spoiler'} for d in full['documents']))
            self.assertEqual(full['release'],json.loads((root/'_data/release.json').read_text())['id'])
            self.assertIn('FULL SPOILERS',(root/'llms-full.txt').read_text(encoding='utf-8'))
            raw=(root/'text/changes.md').read_text(encoding='utf-8')
            self.assertIn('Spoiler: full',raw)
            self.assertIn('FULL SPOILERS',raw)
            row['spoiler']='safe';p.write_text(json.dumps(doc),encoding='utf-8');tool.export(root,'https://example.org','/pack')
            self.assertIn('SECRET_BODY',(root/'llms-safe.txt').read_text(encoding='utf-8'))
            self.assertEqual(tool.check(root,'https://example.org','/pack'),[])

    def test_full_human_route_and_reclassification(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));p=root/'_data/pages.json';doc=json.loads(p.read_text())
            row=next(r for r in doc['pages'] if r['source']=='changes.md');row.update(spoiler='full',aliases=['SECRET_ALIAS'])
            p.write_text(json.dumps(doc));q=root/'changes.md';q.write_text(q.read_text()+'\n## Secret section\nSECRET_BODY\n',encoding='utf-8');before=q.read_bytes()
            tool.export(root,'https://example.org','/pack')
            route=root/'full/changes.md'
            self.assertTrue(route.is_file(),'distinct full-human route missing')
            self.assertIn('FULL SPOILERS',route.read_text(encoding='utf-8'))
            self.assertIn('Return to safe entry',route.read_text(encoding='utf-8'))
            self.assertIn('SECRET_BODY',route.read_text(encoding='utf-8'))
            self.assertEqual(before,q.read_bytes())
            docs=json.loads((root/'assets/search-full.json').read_text(encoding='utf-8'))['documents']
            self.assertTrue(any(d['url']=='/pack/full/changes/' and d['anchor']=='secret-section' for d in docs))
            self.assertNotIn('SECRET', (root/'assets/search-safe.json').read_text(encoding='utf-8'))
            route.write_text(route.read_text(encoding='utf-8')+'STALE',encoding='utf-8')
            self.assertTrue(any('stale' in e for e in tool.check(root,'https://example.org','/pack')))
            row['spoiler']='safe';p.write_text(json.dumps(doc));tool.export(root,'https://example.org','/pack')
            self.assertFalse(route.exists(),'reclassification left revealing route')
            self.assertEqual(tool.check(root,'https://example.org','/pack'),[])

    def test_heading_punctuation_preserves_kramdown_space_hyphens(self):
        self.assertEqual(self.tool().slug('Conditional J1 reading chain — not a completed journey'), 'conditional-j1-reading-chain--not-a-completed-journey')

    def test_ordinary_layout_omits_curated_full_content(self):
        layout=(ROOT/'_layouts/default.html').read_text(encoding='utf-8')
        self.assertIn("entry.spoiler == 'full'",layout)
        self.assertIn('Reveal full spoilers',layout)
        branch=layout.rsplit("{% if spoiler_entry.spoiler == 'full' %}",1)[1].split('{% endif %}',1)[0]
        full,safe=branch.split('{% else %}',1)
        self.assertNotIn('content',full)
        self.assertIn("{{ content | replace: '<table>', table_open | replace: '</table>', table_close }}",safe)
        self.assertIn('display_title | escape',layout)

    def test_safe_links_cannot_leak_full_anchor_or_alias(self):
        tool=self.tool()
        for payload in ('\n[Neutral](changes.md#secret-section)\n','\n[SECRET_ALIAS](changes.md)\n'):
            with self.subTest(payload=payload),tempfile.TemporaryDirectory() as tmp:
                root=self.fixture(Path(tmp));p=root/'_data/pages.json';doc=json.loads(p.read_text());row=next(r for r in doc['pages'] if r['source']=='changes.md');row.update(spoiler='full',aliases=['SECRET_ALIAS']);p.write_text(json.dumps(doc))
                q=root/'changes.md';q.write_text(q.read_text()+'\n## Secret section\nSECRET_BODY\n',encoding='utf-8')
                q=root/'index.md';q.write_text(q.read_text()+payload,encoding='utf-8')
                before=(root/'llms.txt').read_bytes()
                with self.assertRaisesRegex(ValueError,'spoiler'):tool.export(root,'https://example.org','/pack')
                self.assertEqual(before,(root/'llms.txt').read_bytes())

    def test_unowned_full_route_collision_no_write(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));p=root/'_data/pages.json';doc=json.loads(p.read_text());next(r for r in doc['pages'] if r['source']=='changes.md')['spoiler']='full';p.write_text(json.dumps(doc))
            (root/'full').mkdir(exist_ok=True);q=root/'full/changes.md';q.write_text('unowned content',encoding='utf-8');before=(root/'llms.txt').read_bytes()
            with self.assertRaisesRegex(ValueError,'unowned'):tool.export(root,'https://example.org','/pack')
            self.assertEqual(q.read_text(),'unowned content');self.assertEqual(before,(root/'llms.txt').read_bytes())

    def test_full_body_unsafe_injection_no_write(self):
        tool=self.tool()
        for payload in ('[Link](sources.md){: onclick="alert(1)"}', '<img src="x" onerror="alert(1)">'):
            with self.subTest(payload=payload),tempfile.TemporaryDirectory() as tmp:
                root=self.fixture(Path(tmp));p=root/'_data/pages.json';doc=json.loads(p.read_text());next(r for r in doc['pages'] if r['source']=='changes.md')['spoiler']='full';p.write_text(json.dumps(doc))
                q=root/'changes.md';q.write_text(q.read_text()+'\n'+payload,encoding='utf-8');before=(root/'llms.txt').read_bytes()
                with self.assertRaisesRegex(ValueError,'unsafe'):tool.export(root,'https://example.org','/pack')
                self.assertFalse((root/'full/changes.md').exists());self.assertEqual(before,(root/'llms.txt').read_bytes())

    def test_stale_remove_and_unowned_refusal(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));tool.export(root,'https://example.org','/pack')
            p=root/'_data/pages.json';doc=json.loads(p.read_text());doc['pages']=[r for r in doc['pages'] if r['source']!='changes.md'];p.write_text(json.dumps(doc))
            (root/'changes.md').unlink()
            for page in doc['pages']:
                q=root/page['source'];q.write_text(q.read_text(encoding='utf-8').replace('(changes.md)','(sources.md)'),encoding='utf-8')
            tool.export(root,'https://example.org','/pack');self.assertFalse((root/'text/changes.md').exists())
            (root/'text/unowned.md').write_text('Source: https://example.org/pack/unowned/\nBaseline: '+tool.BASELINE+'\n\nunowned')
            with self.assertRaises(ValueError):tool.export(root,'https://example.org','/pack')
            self.assertIn('unowned',(root/'text/unowned.md').read_text())

    def test_image_and_html_url_safety_no_write(self):
        tool=self.tool()
        for payload in ('[Safe](sources.md){: onclick="alert(12345)"}', '{: #unsafe onclick="alert(1)"}', '![bad](javascript:alert)', '![missing](assets/missing.png)', '[bad]( javascript:alert)', '[bad](javascript:alert "title")', '![]( javascript:alert)', '<img src="x" onerror="alert(1)">', '<a href="javascript:alert(1)">bad</a>'):
            with self.subTest(payload=payload),tempfile.TemporaryDirectory() as tmp:
                root=self.fixture(Path(tmp));q=root/'index.md';q.write_text(q.read_text(encoding='utf-8')+'\n'+payload+'\n',encoding='utf-8')
                before=(root/'llms.txt').read_bytes()
                with self.assertRaises(ValueError):tool.export(root,'https://example.org','/pack')
                self.assertEqual(before,(root/'llms.txt').read_bytes())

    def test_family_bundles_safe_full_and_stale_cleanup(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));p=root/'_data/pages.json';doc=json.loads(p.read_text());row=next(r for r in doc['pages'] if r['source']=='changes.md');row.update(group='canary',spoiler='full',aliases=['SECRET_ALIAS']);p.write_text(json.dumps(doc))
            q=root/'changes.md';q.write_text(q.read_text(encoding='utf-8').replace('title: "Changes"','title: "SECRET_TITLE"')+'\nSECRET_BODY\n',encoding='utf-8')
            tool.export(root,'https://example.org','/pack')
            safe=root/'text/groups/canary-safe.txt';full=root/'text/groups/canary-full.txt'
            self.assertTrue(safe.exists(),'family safe bundle missing');self.assertTrue(full.exists(),'family full bundle missing')
            self.assertNotIn('SECRET',safe.read_text(encoding='utf-8'));self.assertIn('SECRET_BODY',full.read_text(encoding='utf-8'));self.assertIn('FULL SPOILERS',full.read_text(encoding='utf-8'))
            row['group']='handbook';p.write_text(json.dumps(doc));tool.export(root,'https://example.org','/pack')
            self.assertFalse(safe.exists());self.assertFalse(full.exists())

    def test_export_directory_collision_no_write(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));tool.export(root,'https://example.org','/pack');q=root/'assets/search-full.json';q.unlink();q.mkdir()
            before={f.relative_to(root).as_posix():f.read_bytes() for f in root.rglob('*') if f.is_file()}
            with self.assertRaisesRegex(ValueError,'export|unexpected'):tool.export(root,'https://example.org','/different')
            self.assertEqual(before,{f.relative_to(root).as_posix():f.read_bytes() for f in root.rglob('*') if f.is_file()})

    def test_linked_registry_directory_rejected_before_read(self):
        import os
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp,tempfile.TemporaryDirectory() as outside:
            root=self.fixture(Path(tmp));shutil.rmtree(root/'_data');(Path(outside)/'pages.json').write_text('not JSON')
            try:link_directory(outside,root/'_data')
            except OSError as exc:self.skipTest('symlink unavailable: '+str(exc))
            with self.assertRaisesRegex(ValueError,'linked'):tool.export(root,'https://example.org','/pack')

    def test_linked_export_directory_no_write(self):
        import os
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp,tempfile.TemporaryDirectory() as outside:
            root=self.fixture(Path(tmp));shutil.rmtree(root/'text')
            try:link_directory(outside,root/'text')
            except OSError as exc:self.skipTest('symlink unavailable: '+str(exc))
            before=(root/'llms.txt').read_bytes()
            with self.assertRaisesRegex(ValueError,'linked|unsafe'):tool.export(root,'https://example.org','/pack')
            self.assertEqual(before,(root/'llms.txt').read_bytes());self.assertEqual(list(Path(outside).iterdir()),[])

    def test_safe_source_cannot_leak_full_metadata(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));p=root/'_data/pages.json';doc=json.loads(p.read_text());row=next(r for r in doc['pages'] if r['source']=='changes.md');row['spoiler']='full';row['aliases']=['SECRET_ALIAS'];p.write_text(json.dumps(doc))
            q=root/'index.md';q.write_text(q.read_text(encoding='utf-8')+'\nSECRET_ALIAS\n',encoding='utf-8')
            before=(root/'llms.txt').read_bytes()
            with self.assertRaisesRegex(ValueError,'spoiler'):tool.export(root,'https://example.org','/pack')
            self.assertEqual(before,(root/'llms.txt').read_bytes())
            self.assertTrue(any('spoiler' in e for e in tool.check(root,'https://example.org','/pack')))

    def test_canonical_paths_and_unsafe_reference_links(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));q=root/'index.md';original=q.read_text(encoding='utf-8')
            q.write_text(original+'\n[Guide](/guides/recipe-search/)\n',encoding='utf-8')
            tool.export(root,'https://example.org','/pack')
            self.assertIn('https://example.org/pack/guides/recipe-search/',(root/'text/index.md').read_text(encoding='utf-8'))
            q.write_text(original+'\n[bad][x]\n[x]: javascript:alert\n',encoding='utf-8')
            with self.assertRaises(ValueError):tool.export(root,'https://example.org','/pack')

    def test_registry_duplicate_json_key_rejected(self):
        tool=self.tool()
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(Path(tmp));p=root/'_data/pages.json';p.write_text(p.read_text().replace('"schema": 1','"schema": 0, "schema": 1'))
            with self.assertRaises(ValueError):tool.export(root,'https://example.org','/pack')

if __name__ == '__main__':
    unittest.main(verbosity=2)
