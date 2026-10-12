# Ed’s Plumbing and Sewer Inc.

A portable, static 10-page website. No accounts, backend, paid libraries, external fonts, or build dependencies. The original American flag is served locally. All content is in the HTML, including when JavaScript is disabled.

## Use and edit

Deploy the contents of `dist/` to any static host. Directory-index routing must be enabled. Serve `404.html` with an actual 404 status for missing URLs; do not enable an SPA fallback.

To preview: `python3 -m http.server 8765 --directory dist`

Edit page content in `build.py`, then run `python3 build.py`. Styles and the small mobile navigation script are maintained directly in `dist/style.css` and `dist/site.js`. Python uses only the standard library. Preserve those assets when rebuilding.

Canonical URLs and sitemap entries target https://edsplumbingandhomerepairsinc.com. Change `BASE` in build.py and rebuild if the permanent domain changes. The Sites preview is private; it is not the production domain and will not replace the existing website automatically.

## Source review

Reviewed the public homepage, /about, and /contact-us on October 12, 2026. Inspected the homepage HTML links: these are the three linked site pages; service links point to homepage sections. The About page contains unfilled template copy. No additional pages appeared in the site search; the sitemap was not accessible through the web reader.

Preserved phone, address, published office hours, emergency-service availability, and the service categories. Updated the name to Ed’s Plumbing and Sewer Inc. as instructed. Chicago-wide coverage comes from the owner's brief. City examples illustrate this coverage; they are not claims of separate offices. No invented reviews, ratings, credentials, guarantees, company age, or veteran-owned status. Removed unsupported absolute drain-cleaning performance claims from the old site.

The existing American flag asset was downloaded from the original site's public image host. The supplied company logo was restored with the built-in image-generation tool and integrated into the header and footer. It is a high-resolution raster reconstruction, not a vector or pixel-exact enlargement. Teal and charcoal now anchor the brand palette while the American flag remains. Other graphics use CSS; there are no new stock-image licensing dependencies.

## Launch and local SEO

1. Confirm the new business name is also accurate on Google Business Profile and other directories. Confirm address, telephone, services, and emergency availability before the public launch. Only show the address as a customer-facing business location on Google if customers can actually visit it.
2. Publish `dist/` on the existing domain, preserving `/about` and `/contact-us`. Configure single-hop permanent redirects from HTTP and www to the canonical HTTPS hostname and normalize trailing slashes. Current clean paths should resolve to their directory-index pages.
3. Keep this private preview private. A public duplicate should be noindexed until the domain migration is complete. Do not block or noindex the final production site.
4. Verify the domain in Google Search Console, submit `/sitemap.xml`, and request indexing of the home and service pages. Check the rendered canonical URLs and indexing status after launch.
5. Validate the Plumber, Service, and BreadcrumbList JSON-LD with Google's Rich Results Test and Schema.org Validator. Structured data is descriptive; it does not guarantee enhanced search results.
6. Run PageSpeed Insights on the deployed public site, including a mobile test. This build uses local assets and minimal JavaScript, but no measured Core Web Vitals score is claimed.
7. Keep Google Business Profile complete: genuine categories and services, accurate hours, authentic project photographs, and consistent contact information. Invite honest customer reviews without incentives and respond to them.
8. Add authentic job stories and original photos over time. Only create additional location pages when they contain useful, distinct local work and information. Do not create hundreds of near-identical city pages.
9. Track search impressions, calls, and relevant service queries. Improve pages based on real customer questions. No analytics or tracking scripts have been installed.

Google local results depend on relevance, distance, and prominence. A Darien company cannot be promised the first result for every searcher across Chicago. This site provides the technical/content foundation; local reputation and ongoing business-profile work remain necessary.

Sources:
- https://edsplumbingandhomerepairsinc.com/
- https://edsplumbingandhomerepairsinc.com/about
- https://edsplumbingandhomerepairsinc.com/contact-us
- https://developers.google.com/search/docs/essentials
- https://support.google.com/business/answer/7091

## Verification

The local server returned HTTP 200. Automated static checks verify all ten pages, internal links/assets, one H1 per content page, unique titles and descriptions, valid JSON-LD, sitemap coverage, and original URL preservation. Browser visual and interaction QA could not be completed because the in-app browser failed to attach. Mobile styling and accessible native FAQ disclosures are implemented but require a browser review before production launch.
