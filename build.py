from argparse import ArgumentParser
import hashlib
import json
from pathlib import Path
import re
from html.parser import HTMLParser
import xml.etree.ElementTree as ET

from scripts.html_format import pretty_html


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'src'
OUTPUT = ROOT / 'docs'
INCLUDE = re.compile(r'''{%\s*include\s+["']([^"']+)["']\s*%}''')


def expand_includes(text, partials, stack=()):
    def replace(match):
        name = match.group(1)
        path = (partials / name).resolve()
        if not path.is_relative_to(partials.resolve()) or path.suffix != '.html':
            raise ValueError(f'Invalid partial path: {name}')
        if path in stack:
            raise ValueError(f'Circular partial include: {name}')
        if not path.is_file():
            raise ValueError(f'Missing partial: {name}')
        return expand_includes(path.read_text(), partials, (*stack, path)).strip()

    return INCLUDE.sub(replace, text)


class PageMetadata(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.canonical = None
        self.noindex = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.noindex = 'noindex' in attrs.get('content', '').lower()


def sitemap(urls):
    namespace = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    ET.register_namespace('', namespace)
    tree = ET.Element(f'{{{namespace}}}urlset')
    for address in urls:
        item = ET.SubElement(tree, f'{{{namespace}}}url')
        ET.SubElement(item, f'{{{namespace}}}loc').text = address
    ET.indent(tree, space='  ')
    return ET.tostring(tree, encoding='utf-8', xml_declaration=True) + b'\n'


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def build_site(source=SOURCE, output=OUTPUT):
    source, output = Path(source).resolve(), Path(output).resolve()
    if output == source or output.is_relative_to(source) or source.is_relative_to(output):
        raise ValueError('Build output must be separate from the source folder.')
    pages = source / 'pages'
    if not (pages / 'index.html').is_file():
        raise ValueError('Missing src/pages/index.html.')
    files = {}
    for asset in sorted((source / 'static').rglob('*')):
        if asset.is_file():
            if asset.is_symlink():
                raise ValueError(f'Static asset cannot be a symbolic link: {asset}')
            files[asset.relative_to(source / 'static').as_posix()] = asset.read_bytes()
    urls = []
    count = 0
    for page in sorted(pages.rglob('*')):
        if not page.is_file() or page.suffix not in ('.html', '.shtml'):
            continue
        if page.is_symlink():
            raise ValueError(f'Page cannot be a symbolic link: {page}')
        relative = page.relative_to(pages).as_posix()
        if relative in files:
            raise ValueError(f'Page and static asset have the same output path: {relative}')
        html = pretty_html(expand_includes(page.read_text(), source / 'partials'))
        files[relative] = html.encode()
        meta = PageMetadata(html)
        if page.suffix == '.html':
            count += 1
            if not meta.noindex:
                if not meta.canonical:
                    raise ValueError(f'Indexable page is missing its canonical URL: {relative}')
                urls.append(meta.canonical)
    if len(urls) != len(set(urls)):
        raise ValueError('Indexable pages must have unique canonical URLs.')
    if 'sitemap.xml' in files:
        raise ValueError('sitemap.xml is generated from page metadata; remove it from src/static.')
    files['sitemap.xml'] = sitemap(urls)
    files.setdefault('.nojekyll', b'')
    state_path = output.parent / ('build-manifest.json' if output.name == 'docs' else f'.{output.name}-build-state.json')
    previous = {}
    if state_path.is_file():
        state = json.loads(state_path.read_text())
        previous = state.get('files', {})
    edited = []
    for name, expected in previous.items():
        path = output / name
        if not path.is_file():
            edited.append(name)
            continue
        current = path.read_bytes()
        if sha256(current) != expected:
            captured_in_source = current == files.get(name)
            if not captured_in_source and path.suffix in ('.html', '.shtml') and name in files:
                captured_in_source = pretty_html(current.decode()).encode() == files[name]
            if not captured_in_source:
                edited.append(name)
    if edited:
        raise ValueError('Generated files were edited directly: ' + ', '.join(edited) + '. Move those edits into src/pages, src/partials or src/static before rebuilding. No output was changed.')
    for name in files:
        destination = output / name
        if destination.is_symlink() or any(parent.is_symlink() for parent in destination.parents if parent != output.parent):
            raise ValueError(f'Output cannot contain symbolic links: {destination}')
    for name, content in files.items():
        destination = output / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.is_file() or destination.read_bytes() != content:
            destination.write_bytes(content)
    for name in previous.keys() - files.keys():
        (output / name).unlink()
    state = {'files': {name: sha256(content) for name, content in files.items()}}
    state_path.write_text(json.dumps(state, indent=2) + '\n')
    return count, len(urls), len(files)


def main():
    parser = ArgumentParser(description='Build pretty-printed website files from editable HTML sources.')
    parser.add_argument('--output', type=Path, default=OUTPUT, help='Output folder; defaults to docs/.')
    args = parser.parse_args()
    try:
        pages, urls, files = build_site(output=args.output)
    except (ValueError, OSError, json.JSONDecodeError) as error:
        parser.exit(1, f'Build failed: {error}\n')
    print(f'Built {pages} HTML pages, {urls} sitemap URLs and {files} files in {args.output}.')


if __name__ == '__main__':
    main()
