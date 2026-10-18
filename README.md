# Ed’s Plumbing & Sewer — static website

Modern, responsive website rebuilt from https://www.thegreatestplumber.com/ on October 18, 2026. Sixteen crawlable content pages. The simplified homepage has four sections: a short introduction, three service categories, Chicagoland coverage and contact options. Residential plumbing, commercial plumbing and remodeling lead to dedicated pages; individual services, pricing, FAQs and the email inquiry form live on supporting pages.

## Files and editing

- `dist/` is the deployable static website; upload its contents to the final host.
- `build.py` generates all HTML, schema, sitemap and legacy URL mappings. Python standard library only.
- `dist/assets/site.css` and `dist/assets/site.js` contain shared styles and interactions. No framework, external fonts, CDN or runtime dependency.
- `scripts/verify.py` checks page structure, metadata, local links, anchors, images, JSON-LD syntax and sitemap coverage. Standard library only.
- All five supplied interior images are included as optimized responsive WebP derivatives. The supplied logo is retained. Interior photos are presented as stock illustrations, not completed jobs.

Run `python3 build.py`, then `python3 scripts/verify.py`. Preview with `python3 -m http.server 8765 --directory dist`.

The old `design.py`, `dist/style.css`, `dist/site.js` and legacy image directory are retained from the previous version for reference; the new site does not load them. Only `build.py` is used to regenerate the new pages.

## Contact behavior

Calls use `tel:` links. The service inquiry form prepares an email in the visitor’s email application. The visitor must review and send it; nothing is submitted or stored by the static website. It never claims a confirmed appointment. A direct email address and phone alternatives are always visible. A server or approved form provider would be required for direct form delivery.

## Source review and content decisions

Reviewed the original homepage and service pages for drains, sewer backups, low pressure, water heaters, tankless heaters, leaks, sump/ejector pumps, commercial/industrial plumbing, utility rooms, major installations and HVAC. Also reviewed contact, service areas, licensing, employees, scheduling, appointments, payments and Why Dig. Fixture and appliance detail pages did not load in the web reader, so their service categories are retained from the homepage navigation rather than adding unsupported detail.

The source states 40+ years of experience; licensed, bonded and insured; flat-rate pricing; 24/7 emergency service; extended hours; no Saturday overtime rate; a dispatch fee credited toward work; and cash, checks and major credit cards accepted. Contact numbers and emails are copied from the original contact page. Confirm these policies remain current before a public launch. No invented reviews, ratings, project photographs, street address, license numbers, precise response-time promises or regular office hours are included. Omitted dated $35 offers, federal tax-credit claims, and model-specific tankless warranties/lifespans.

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
