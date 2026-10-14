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
            self.assertIn('baseline: dev-0.5-20261015', text, name)
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
            self.assertIn('dev-0.5-20261015', guide)

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

if __name__ == '__main__':
    unittest.main(verbosity=2)
