import json
import re
from dataclasses import dataclass, field
from html.parser import HTMLParser


SPACE = re.compile(r'[\t\n\f\r ]+')
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())
INLINE = set('a abbr b bdi bdo br button cite code data del dfn em i img input ins kbd label mark meter output progress q rp rt ruby s samp select small span strong sub sup svg text time u var wbr'.split())
TEXT_BLOCKS = set('title p h1 h2 h3 h4 h5 h6 li dt dd figcaption summary legend option'.split())
RAW = {'pre', 'textarea', 'script', 'style'}


@dataclass
class Element:
    tag: str
    opening: str
    attrs: dict
    children: list = field(default_factory=list)
    self_closing: bool = False


@dataclass
class Literal:
    text: str


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.root = Element('', '', {})
        self.stack = [self.root]
        self.feed(source)
        self.close()

    def handle_starttag(self, tag, attrs):
        element = Element(tag, self.get_starttag_text(), dict(attrs))
        self.stack[-1].children.append(element)
        if tag not in VOID:
            self.stack.append(element)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Element(tag, self.get_starttag_text(), dict(attrs), self_closing=True))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        for position in range(len(self.stack) - 1, 0, -1):
            if self.stack[position].tag == tag:
                del self.stack[position:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)

    def handle_entityref(self, name):
        self.handle_data(f'&{name};')

    def handle_charref(self, name):
        self.handle_data(f'&#{name};')

    def handle_decl(self, declaration):
        self.stack[-1].children.append(Literal(f'<!{declaration}>'))

    def handle_comment(self, data):
        self.stack[-1].children.append(Literal(f'<!--{data}-->'))


def compact_tag(tag):
    result = []
    quote = None
    pending_space = False
    for char in tag:
        if quote:
            result.append(char)
            if char == quote:
                quote = None
        elif char in ('"', "'"):
            if pending_space:
                result.append(' ')
                pending_space = False
            quote = char
            result.append(char)
        elif char in '\t\n\f\r ':
            pending_space = True
        else:
            if pending_space and char != '>':
                result.append(' ')
            pending_space = False
            result.append(char)
    return ''.join(result)


def inline(node, preserve=False):
    if isinstance(node, str):
        return node if preserve else SPACE.sub(' ', node)
    if isinstance(node, Literal):
        return node.text
    opening = compact_tag(node.opening)
    if node.self_closing or node.tag in VOID:
        return opening
    content = ''.join(inline(child, preserve or node.tag in RAW) for child in node.children)
    return f'{opening}{content}</{node.tag}>'


def is_inline(node):
    if not isinstance(node, Element):
        return True
    if node.tag not in INLINE:
        return False
    if node.tag in {'svg', 'select'}:
        return True
    return all(is_inline(child) for child in node.children)


def formatted(node, depth=0):
    padding = '  ' * depth
    if isinstance(node, str):
        text = SPACE.sub(' ', node).strip(' \t\r\n\f')
        return [padding + text] if text else []
    if isinstance(node, Literal):
        return [padding + node.text]
    opening = compact_tag(node.opening)
    if node.tag == 'script' and node.attrs.get('type') == 'application/ld+json':
        content = ''.join(inline(child, True) for child in node.children)
        data = json.dumps(json.loads(content), ensure_ascii=False, indent=2).replace('</', '<\\/')
        return [padding + opening, *('  ' * (depth + 1) + line for line in data.splitlines()), padding + '</script>']
    if node.tag in RAW or node.tag in VOID or node.self_closing:
        return [padding + inline(node)]
    children_inline = all(is_inline(child) for child in node.children)
    if children_inline and (node.tag in INLINE or node.tag in TEXT_BLOCKS or not node.children):
        return [padding + inline(node)]
    lines = [padding + opening] if node.tag else []
    child_depth = depth + 1 if node.tag else depth
    pending = []

    def flush():
        text = ''.join(inline(child) for child in pending).strip(' \t\r\n\f')
        if text:
            lines.append('  ' * child_depth + text)
        pending.clear()

    for child in node.children:
        if is_inline(child):
            pending.append(child)
        else:
            flush()
            lines.extend(formatted(child, child_depth))
    flush()
    if node.tag:
        lines.append(padding + f'</{node.tag}>')
    return lines


def pretty_html(source):
    return '\n'.join(formatted(Document(source).root)) + '\n'
