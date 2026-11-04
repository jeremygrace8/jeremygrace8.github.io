from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,xml.etree.ElementTree as ET
class Doc(HTMLParser):
 def __init__(self,text):
  super().__init__();self.tags=[];self.title='';self.in_title=False;self.ld=False;self.json=[];self.script='';self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);self.tags.append((tag,a))
  if tag=='title':self.in_title=True
  if tag=='script' and a.get('type')=='application/ld+json':self.ld=True;self.script=''
 def handle_endtag(self,tag):
  if tag=='title':self.in_title=False
  if tag=='script' and self.ld:self.ld=False;self.json.append(json.loads(self.script))
 def handle_data(self,data):
  if self.in_title:self.title+=data
  if self.ld:self.script+=data
 def all(self,tag):return [a for t,a in self.tags if t==tag]
root=Path(__file__).resolve().parents[1]/'docs'
errors=[];titles=[];descriptions=[];indexable=[];count=0;docs={p:Doc(p.read_text()) for p in root.rglob('*.html')}
for path,soup in docs.items():
 rel=path.relative_to(root)
 if path.name=='404.html':continue
 count+=1
 assert len(soup.all('h1'))==1,f'{rel}: expected one H1'
 meta={t.get('name'):t.get('content') for t in soup.all('meta')}
 titles.append(soup.title);descriptions.append(meta['description'])
 assert soup.all('html')[0].get('lang')=='en'
 canonical=next(a['href'] for a in soup.all('link') if a.get('rel')=='canonical')
 assert canonical.startswith('https://www.thegreatestplumber.com/')
 if 'noindex' not in meta.get('robots',''):indexable.append(canonical)
 assert 'viewport' in meta
 for data in soup.json:
  for item in data:assert '@type' in item
 for el,attribute in [('a','href'),('img','src'),('script','src'),('link','href')]:
  for tag in soup.all(el):
   value=tag.get(attribute,'');u=urlsplit(value)
   if not value or u.scheme or value.startswith('//'):continue
   target=root/unquote(u.path.lstrip('/')) if u.path.startswith('/') else path.parent/unquote(u.path)
   if not u.path:target=path
   if target.is_dir():target=target/'index.html'
   if not target.exists():errors.append(f'{rel}: missing {value}')
   elif u.fragment:
    doc=docs.get(target) or Doc(target.read_text())
    if not any(a.get('id')==u.fragment for _,a in doc.tags):errors.append(f'{rel}: missing anchor {value}')
 for im in soup.all('img'):
  assert im.get('alt'),f'{rel}: image needs alt'
  assert im.get('width') and im.get('height'),f'{rel}: image dimensions missing'
assert len(set(titles))==len(titles),'duplicate titles'
assert len(set(descriptions))==len(descriptions),'duplicate descriptions'
urls=[x.text for x in ET.parse(root/'sitemap.xml').iter() if x.tag.endswith('loc')]
assert len(urls)==len(indexable),(len(urls),len(indexable))
assert set(urls)==set(indexable),'sitemap must contain every indexable page and exclude noindex pages'
assert not errors,'\n'.join(errors)
print(f'PASS: {count} pages; unique metadata; internal links and anchors; image alt text and dimensions; JSON-LD; sitemap coverage.')
