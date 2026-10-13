# Ed’s Plumbing and Sewer Inc.

A portable, static 10-page website. No accounts, backend, paid libraries, external fonts, or build dependencies. The original American flag is served locally. All content is in the HTML, including when JavaScript is disabled.

## Use and edit

Deploy the contents of `dist/` to any static host. Directory-index routing must be enabled. Serve `404.html` with an actual 404 status for missing URLs; do not enable an SPA fallback.

To preview: `python3 -m http.server 8765 --directory dist`

Edit service content and SEO metadata in `build.py`, shared layouts and homepage sections in `design.py`, then run `python3 build.py`. Styles and the small mobile navigation script are maintained directly in `dist/style.css` and `dist/site.js`. Python uses only the standard library. Preserve those assets when rebuilding.

Canonical URLs and sitemap entries target https://edsplumbingandhomerepairsinc.com. Change `BASE` in build.py and rebuild if the permanent domain changes. The Sites preview is private; it is not the production domain and will not replace the existing website automatically.

## Source review

Reviewed the public homepage, /about, and /contact-us on October 12, 2026. Inspected the homepage HTML links: these are the three linked site pages; service links point to homepage sections. The About page contains unfilled template copy. No additional pages appeared in the site search; the sitemap was not accessible through the web reader.

Preserved phone, address, published office hours, emergency-service availability, and the service categories. Updated the name to Ed’s Plumbing and Sewer Inc. as instructed. Chicago-wide coverage comes from the owner's brief. City examples illustrate this coverage; they are not claims of separate offices. No invented reviews, ratings, credentials, guarantees, company age, or veteran-owned status. Removed unsupported absolute drain-cleaning performance claims from the old site.

The existing American flag asset was downloaded from the original site's public image host. The supplied company logo was restored with the built-in image-generation tool and integrated into the header and footer. It is a high-resolution raster reconstruction, not a vector or pixel-exact enlargement. Teal and charcoal now anchor the brand palette while the American flag remains. Five user-approved AI-generated interior images are used as illustrative stock imagery, including the commercial restroom with the open center stall. They are explicitly labeled as illustrations, not completed Ed’s projects. Original PNGs are retained separately; JPEG website derivatives are optimized for delivery. Service icons are original inline SVG artwork. No Carson text, branding, source code, or images were copied.

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

## Redesign direction

The October 12 redesign uses https://carsonplumbinginc.com/ as a visual reference for a photograph-led plumbing site, spacious logo/navigation header, compact service overview, and straightforward service content. Ed’s has its own copy, teal palette, custom layout and service icons. The American flag is retained as a smaller footer accent. All existing service paths, metadata, sitemap, and structured business data are retained.

The homepage gallery includes both bathrooms, the kitchen with dishwasher, the laundry room, and the final commercial restroom image. Navigation is manual, with previous/next buttons, five direct selection buttons, and arrow-key support. It does not auto-advance. No new commercial-service claims were added on the basis of the stock photograph.

## Verification

Static checks passed for all ten pages: internal links and assets, one H1 per content page, unique titles and descriptions, valid JSON-LD, sitemap coverage, and original URL preservation. The local HTTP server returned 200.

Browser-reviewed desktop homepage, service overview, and plumbing detail page; mobile homepage and contact page at 390 pixels; narrow-mobile layout at 320 pixels. Confirmed no horizontal page overflow, gallery next/previous/direct selection, FAQ expansion, mobile menu navigation, and correct telephone destinations. Narrow-mobile header and headline sizing were refined after visual review. Desktop and mobile browser review is now completed, superseding the earlier browser-attachment limitation.

No public-domain migration, Search Console submission, real-user Core Web Vitals measurement, or Google Business Profile changes were performed. The Sites deployment remains an owner-private preview.
