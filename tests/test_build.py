import json
from pathlib import Path
import tempfile
import unittest

from build import build_site, expand_includes
from scripts.html_format import pretty_html


class FormattingTests(unittest.TestCase):
    def test_mixed_inline_text_and_entities(self):
        source = '<p>Call <a href="tel:+17734711444">our <strong>emergency</strong> line</a> &amp; ask.</p>'
        self.assertEqual(pretty_html(source), source + '\n')
        self.assertIn('<span>A</span><span>B</span>', pretty_html('<div><span>A</span><span>B</span></div>'))

    def test_block_content_inside_links_is_indented(self):
        html = pretty_html('<div><a href="/"><div><h2>Service</h2><p>Details</p></div></a></div>')
        self.assertIn('\n  <a href="/">\n    <div>\n      <h2>Service</h2>', html)
        self.assertEqual(pretty_html(html), html)

    def test_preserves_raw_text_and_attribute_case(self):
        source = '<textarea>  keep\n spaces </textarea><pre>  x\n  y</pre><script>if (x < 2) { run(); }</script><svg viewBox="0 0 24 24"><path d="M4 12h16" /></svg>'
        html = pretty_html(source)
        for fragment in ['<textarea>  keep\n spaces </textarea>', '<pre>  x\n  y</pre>', '<script>if (x < 2) { run(); }</script>', 'viewBox="0 0 24 24"']:
            self.assertIn(fragment, html)
        self.assertEqual(pretty_html(html), html)

    def test_pretty_prints_json_without_changing_data(self):
        data = [{'@type': 'Service', 'name': 'Ed’s & sewer', 'details': {'available': True}}]
        html = pretty_html('<script type="application/ld+json">' + json.dumps(data) + '</script>')
        self.assertIn('\n  [\n', html)
        self.assertEqual(json.loads(html.split('>', 1)[1].rsplit('</script>', 1)[0]), data)
        self.assertEqual(pretty_html(html), html)


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'src'
        self.output = self.root / 'docs'
        for folder in ['pages', 'partials', 'static/assets']:
            (self.source / folder).mkdir(parents=True)
        self.page = self.source / 'pages/index.html'
        self.page.write_text('<!doctype html><html lang="en"><head><title>Example</title><link rel="canonical" href="https://example.com/"></head><body>{% include "header.html" %}<main><h1>My manual edits</h1><p>Latest page copy.</p></main></body></html>')
        (self.source / 'partials/header.html').write_text('<header>{% include "nav.html" %}</header>')
        (self.source / 'partials/nav.html').write_text('<nav><a href="/">Home</a></nav>')
        self.asset = self.source / 'static/assets/site.css'
        self.asset.write_text('body { color: green; }\n')

    def snapshot(self):
        return {p.relative_to(self.output).as_posix(): p.read_bytes() for p in self.output.rglob('*') if p.is_file()}

    def test_edits_flow_from_sources_and_builds_are_repeatable(self):
        source_before = self.page.read_bytes()
        build_site(self.source, self.output)
        html = (self.output / 'index.html').read_text()
        self.assertIn('<h1>My manual edits</h1>', html)
        self.assertIn('<nav>', html)
        self.assertNotIn('{% include', html)
        self.assertIn('\n    <main>\n', html)
        self.assertEqual(self.page.read_bytes(), source_before)
        self.assertEqual((self.output / 'assets/site.css').read_bytes(), self.asset.read_bytes())
        first = self.snapshot()
        build_site(self.source, self.output)
        self.assertEqual(first, self.snapshot())
        self.page.write_text(self.page.read_text().replace('Latest page copy.', 'Updated copy.'))
        (self.source / 'partials/nav.html').write_text('<nav><a href="/">Updated navigation</a></nav>')
        self.asset.write_text('body { color: blue; }\n')
        build_site(self.source, self.output)
        self.assertIn('Updated copy.', (self.output / 'index.html').read_text())
        self.assertIn('Updated navigation', (self.output / 'index.html').read_text())
        self.assertEqual((self.output / 'assets/site.css').read_bytes(), self.asset.read_bytes())

    def test_noindex_pages_and_removing_a_source_page(self):
        page = self.source / 'pages/review/index.html'
        page.parent.mkdir()
        page.write_text('<html><head><meta name="robots" content="noindex,follow"><link rel="canonical" href="https://example.com/review/"></head><body>Review</body></html>')
        build_site(self.source, self.output)
        self.assertTrue((self.output / 'review/index.html').exists())
        self.assertNotIn('/review/', (self.output / 'sitemap.xml').read_text())
        page.unlink()
        build_site(self.source, self.output)
        self.assertFalse((self.output / 'review/index.html').exists())

    def test_direct_output_edits_are_protected(self):
        build_site(self.source, self.output)
        (self.output / 'index.html').write_text('<h1>Unsaved manual changes</h1>')
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'edited directly'):
            build_site(self.source, self.output)
        self.assertEqual(before, self.snapshot())

    def test_output_edits_can_be_captured_in_source(self):
        build_site(self.source, self.output)
        output = self.output / 'index.html'
        output.write_text(output.read_text().replace('Latest page copy.', 'Preserved manual copy.'))
        self.page.write_text(self.page.read_text().replace('Latest page copy.', 'Preserved manual copy.'))
        build_site(self.source, self.output)
        self.assertIn('Preserved manual copy.', output.read_text())

    def test_missing_circular_and_outside_includes_fail_before_writing(self):
        build_site(self.source, self.output)
        before = self.snapshot()
        partials = self.source / 'partials'
        for directive, message in [('{% include "missing.html" %}', 'Missing partial'), ('{% include "../pages/index.html" %}', 'Invalid partial')]:
            with self.assertRaisesRegex(ValueError, message):
                expand_includes(directive, partials)
        (partials / 'nav.html').write_text('{% include "header.html" %}')
        with self.assertRaisesRegex(ValueError, 'Circular partial'):
            build_site(self.source, self.output)
        self.assertEqual(before, self.snapshot())

    def test_source_output_overlap_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'separate'):
            build_site(self.source, self.source / 'docs')


if __name__ == '__main__':
    unittest.main()
