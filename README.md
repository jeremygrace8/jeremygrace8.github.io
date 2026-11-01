# Ed’s Plumbing & Sewer — static website

Modern, responsive website rebuilt from https://www.thegreatestplumber.com/ on October 18, 2026. Sixteen crawlable content pages. The homepage has a short introduction, three service categories and Chicagoland coverage. Contact us links lead to the dedicated contact page. Residential plumbing, commercial plumbing and remodeling lead to dedicated pages; individual services, pricing, FAQs and the email inquiry form live on supporting pages.

## Files and editing

- `docs/` is the deployable static website; upload its contents to the final host.
- `build.py` generates all HTML, schema, sitemap and legacy URL mappings. Python standard library only.
- `docs/assets/site.css` and `docs/assets/site.js` contain shared styles and interactions. No framework, external fonts, CDN or runtime dependency.
- `scripts/verify.py` checks page structure, metadata, local links, anchors, images, JSON-LD syntax and sitemap coverage. Standard library only.
- All five supplied interior images are included as optimized responsive WebP derivatives. The supplied logo is retained. Interior photos are presented as stock illustrations, not completed jobs.

Run `python3 build.py`, then `python3 scripts/verify.py`. Preview with `python3 -m http.server 8765 --directory docs`.

The old `design.py`, `docs/style.css`, `docs/site.js` and legacy image directory are retained from the previous version for reference; the new site does not load them. Only `build.py` is used to regenerate the new pages.

## Contact behavior

Calls use `tel:` links. The service inquiry form prepares an email in the visitor’s email application. The visitor must review and send it; nothing is submitted or stored by the static website. It never claims a confirmed appointment. A direct email address and phone alternatives are always visible. A server or approved form provider would be required for direct form delivery.

## Source review and content decisions

Reviewed the original homepage and service pages for drains, sewer backups, low pressure, water heaters, tankless heaters, leaks, sump/ejector pumps, commercial/industrial plumbing, utility rooms, major installations and HVAC. Also reviewed contact, service areas, licensing, employees, scheduling, appointments, payments and Why Dig. Fixture and appliance detail pages did not load in the web reader, so their service categories are retained from the homepage navigation rather than adding unsupported detail.

The source states 40+ years of experience; licensed, bonded and insured; flat-rate pricing; 24/7 emergency service; extended hours; no Saturday overtime rate; a dispatch fee credited toward work; and cash, checks and major credit cards accepted. Contact email and phone numbers use the owner’s latest instructions below. Confirm these policies remain current before a public launch. No invented reviews, ratings, project photographs, street address, license numbers, precise response-time promises or regular office hours are included. Omitted dated $35 offers, federal tax-credit claims, and model-specific tankless warranties/lifespans.

Canonical metadata targets **https://www.thegreatestplumber.com**, as requested. The private Sites preview is a review environment. It does not replace the public domain automatically. Preserve owner-private access until launch.

## Verification

All sixteen content pages pass local checks for unique titles and descriptions, one H1, valid JSON-LD syntax, local links and anchors, image alt text and dimensions, and sitemap coverage. JavaScript syntax was checked with Node. Local HTTP returned 200.

Local browser visual QA was blocked by the browser tool’s URL policy. The deployed private preview can be reviewed in the connected browser. No measured Core Web Vitals score or ranking improvement is claimed.

## Public launch and traffic growth

See `LAUNCH.md` for domain migration, search setup, business-profile work and measurement. Technical SEO helps search engines understand the site; rankings and traffic gains depend on launch, local competition, business relevance, distance, reputation and continued work.

## Homepage simplification

Updated around the owner’s three offerings: residential plumbing, commercial plumbing and remodeling. The main page omits detailed service lists, the process section, the separate trust section, FAQs and form. Detailed service pages remain crawlable, and pricing/payment FAQs are on `/contact-us/#faq`. The footer and main navigation are also simplified.

Design references supplied by the owner: https://carsonplumbinginc.com/ and https://www.riverfrontplumbing.com/. Used broad cues of strong interior imagery, clear service labels and direct contact access. No third-party copy, branding or images were reused.

## About page video

The About hero embeds the owner-supplied Vimeo video (792992602), retaining its unlisted access hash and display options. The responsive 16:9 player does not autoplay, supports fullscreen and picture-in-picture, and includes a direct-player fallback link. The privacy page describes the Vimeo connection. No video file is downloaded or hosted locally.

## Emergency contact visibility

The homepage starts with a prominent high-contrast emergency banner immediately beneath the navigation, showing 24/7 availability, Ed’s direct emergency number and a large click-to-call action. The persistent mobile bar also makes the emergency call the primary action and keeps routine service scheduling separate. The banner does not promise a response time.

## Current phone numbers

The owner specifies one regular contact and one dedicated emergency contact:

- Chicagoland: (630) 202-0050, `tel:+16302020050`.
- Emergency: (773) 471-1444, `tel:+17734711444`.

These supersede the previous Darien/Chicago office pair and the earlier emergency assignment. Shared call buttons, the header, service areas, sidebars, contact page, emergency FAQ, mobile bar, metadata, business schema, 404 and email-form fallback use these roles consistently. No office address or location-specific hours are inferred from either number.

## Current contact email

All visible email addresses, mailto links, the inquiry-email recipient and fallback, privacy contact and business schema use `contact@thegreatestplumber.com`.

## GitHub Pages external testing

The generated site is in `docs/`, including an empty `.nojekyll` file so GitHub serves the static output without a Jekyll build. Rebuilding preserves that marker.

After pushing to the existing `github` remote, open the repository’s **Settings → Pages**, select **Deploy from a branch**, choose **main** and **/docs**, then click **Save**.

This repository is `jeremygrace8/jeremygrace8.github.io`, so the testing URL is `https://jeremygrace8.github.io/` and the site’s root-relative links work unchanged. A project repository published under `/repository-name/` would require path adjustments. A directory rename does not enable GitHub Pages automatically.

Canonical URLs and the XML sitemap continue to target the intended production domain, `https://www.thegreatestplumber.com`. GitHub Pages is an external testing copy. `_redirects` and `.htaccess` are retained for compatible production hosts; GitHub Pages does not apply those host-specific redirect rules.

## Private Sites preview packaging

`docs/` is the authoritative deployable website and the GitHub Pages publishing folder. The existing Sites host accepts only certain output-directory names, so its manifest points to an ignored generated `out/` copy. Run `python3 scripts/prepare_sites.py` after building to refresh that copy for Sites packaging. Do not edit `out/`; it is regenerated from `docs/` and is not committed or needed by GitHub Pages.
