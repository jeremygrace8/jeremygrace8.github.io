# Ed’s Plumbing & Sewer

Static, responsive website for residential plumbing, commercial plumbing, remodeling, and related services across Chicagoland.

## Project files

- `docs/`: published website, including HTML, CSS, JavaScript, images, sitemap, and legacy URL mappings.
- `build.py`: regenerates the website pages and search metadata using Python’s standard library.
- `scripts/verify.py`: checks page structure, metadata, internal links, image attributes, structured data, and sitemap coverage.

## Build and verify

```bash
python3 build.py
python3 scripts/verify.py
```

Edit shared styles and interactions in `docs/assets/site.css` and `docs/assets/site.js`. Rebuilding preserves these assets and the `.nojekyll` marker.

## Local preview

```bash
python3 -m http.server 8765 --directory docs
```

## GitHub Pages

Push changes to `main`, then select **Settings → Pages → Deploy from a branch → main → /docs → Save**.

The repository’s testing URL is https://jeremygrace8.github.io/. Production canonical URLs and the XML sitemap target https://www.thegreatestplumber.com/. A project site published under a repository-name subdirectory would require link-path changes.

GitHub Pages serves the generated static files directly. The `.htaccess` and `_redirects` files are for compatible production hosts; GitHub Pages does not apply those host-specific rules.

## Contact behavior

Phone links open the visitor’s phone application. The inquiry form prepares an email for the visitor to review and send in their own email application; it does not submit or store requests on this static website.

- Chicagoland: (630) 202-0050
- Emergency: (773) 471-1444
- Email: contact@thegreatestplumber.com

The About page embeds a Vimeo video. Connection details are described on the website’s privacy page.

## Repository hygiene

Keep `docs/`, the build and verification scripts, and this README tracked. Local credentials, private publishing configuration, internal launch notes, caches, dependencies, and temporary artifacts are ignored. Ignored configuration files are not needed for GitHub Pages.
