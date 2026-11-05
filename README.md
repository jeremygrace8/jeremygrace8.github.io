# Ed’s Plumbing & Sewer

A static website for residential plumbing, commercial plumbing and remodeling across Chicagoland.

## Where to make changes

Edit the files in `src/`. The build reads these files and writes the finished website to `docs/`.

| Change | Source file or folder |
| --- | --- |
| Homepage text and layout | `src/pages/index.html` |
| Individual pages and their search metadata | `src/pages/<page>/index.html` |
| Navigation and top utility bar | `src/partials/header.html` |
| Footer and fixed mobile phone buttons | `src/partials/footer.html` |
| Shared emergency section | `src/partials/emergency.html` |
| Service-area section shared by service pages | `src/partials/service-area.html` |
| Homepage service-area wording | `src/pages/index.html` |
| Main styles and interactive behavior | `src/static/assets/site.css` and `src/static/assets/site.js` |
| Images and other static files | `src/static/`, following their published paths |
| Temporary logo review page | `src/pages/logos/index.html` and `src/static/logos/` |
| Legacy redirect fallback pages | `src/pages/*.shtml` |
| Host redirect configuration | `src/static/_redirects` and `src/static/.htaccess` |

Page files contain normal HTML, including their own titles, descriptions and structured data. Shared sections are inserted with a line such as:

```html
{% include "header.html" %}
```

Includes load files from `src/partials/` and can be nested. Editing a partial updates every page that includes it. Page-specific differences stay in their page files; for example, the homepage has its own service-area copy.

## Build, verify and preview

Python 3.9 or newer is the only build requirement. From this repository folder, run:

```bash
python3 build.py
python3 scripts/verify.py
python3 -m http.server 8765 --directory docs
```

Open http://localhost:8765. After changing a source file, run `python3 build.py` again and refresh the browser. Opening a file in `src/pages/` directly does not expand its includes.

The build pretty-prints HTML and structured data with two-space indentation, generates an indented XML sitemap from canonical URLs, and copies static assets unchanged. Pages marked `noindex`, including the temporary logo review page, stay out of the XML sitemap. The visible website sitemap is editable in `src/pages/sitemap/index.html`.

A separate output folder can be used for a trial build:

```bash
python3 build.py --output /tmp/eds-plumbing-preview
```

`docs/` is generated output. The tracked `build-manifest.json` records generated-file hashes. If a generated file is edited directly, the next build stops before changing output. Move those edits into the relevant source page, partial or static file, then rebuild. The build accepts direct edits once they match what the source generates. Commit the updated manifest with the source and output so this protection also works on a fresh checkout.

Removing a source page removes its previously generated output on the next build. To remove the temporary logo review page before launch, remove `src/pages/logos/` and `src/static/logos/`, then rebuild. If source pages are added or removed, update the visible sitemap page as needed.

Run the build regression checks with:

```bash
python3 -m unittest discover -s tests -v
```

## Publishing

Commit `src/`, the rebuilt `docs/` folder, `build-manifest.json`, build scripts and tests. GitHub Pages uses **Settings → Pages → Deploy from a branch → main → /docs**.

The public testing URL is https://jeremygrace8.github.io/. Canonical URLs and the XML sitemap target https://www.thegreatestplumber.com/. A repository subdirectory deployment would need corresponding URL changes.

The separate Sites publishing checkout receives the same source and generated files; its preparation script copies `docs/` into `out/`. Local private publishing configuration is not needed for GitHub Pages.

## Contact behavior

- Chicagoland: (630) 663-1444
- Emergency: (773) 471-1444
- Email: contact@thegreatestplumber.com

Phone links open the phone application. The inquiry form prepares an email for the visitor to review and send; it does not submit or store requests on the website. The About page embeds a Vimeo video.

Local credentials, private publishing configuration, backups and caches stay outside the public repository or are ignored.
