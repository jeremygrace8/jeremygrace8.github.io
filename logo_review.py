from pathlib import Path
import struct


def build_logo_review(root):
    folder = root / 'logos'
    images = sorted((folder / 'images').glob('*.png'))
    if len(images) != 7:
        raise ValueError('The logo review requires seven logo images.')
    rows = []
    for number, image in enumerate(images, 1):
        width, height = struct.unpack('>II', image.read_bytes()[16:24])
        loading = 'eager' if number == 1 else 'lazy'
        rows.append(f'<li class="logo-row"><span class="logo-number" aria-hidden="true">{number}</span><img src="/logos/images/{image.name}" alt="Logo option {number}: Ed’s Plumbing &amp; Sewer Inc." width="{width}" height="{height}" loading="{loading}" decoding="async"></li>')
    (folder / 'index.html').write_text(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Logo Color Options | Ed’s Plumbing &amp; Sewer</title>
<meta name="description" content="Compare seven logo color options for Ed’s Plumbing &amp; Sewer.">
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="https://www.thegreatestplumber.com/logos/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/logos/review.css">
</head>
<body>
<main class="logo-review">
<header class="review-heading">
<a class="back-link" href="/">← Back to website</a>
<p class="review-eyebrow">ED’S PLUMBING &amp; SEWER</p>
<h1>Logo color options</h1>
<p>Compare the seven options below. Use the number beside your preferred logo.</p>
</header>
<ol class="logo-options" aria-label="Logo color options">{''.join(rows)}</ol>
</main>
</body>
</html>''')
    (folder / 'review.css').write_text('''*{box-sizing:border-box}body{margin:0;background:#fff;color:#111;font-family:Arial,Helvetica,sans-serif;line-height:1.5}.logo-review{width:min(1180px,100%);margin:0 auto;padding:40px 32px 56px}.review-heading{padding-bottom:28px}.back-link{display:inline-block;color:#444;font-size:14px;text-underline-offset:4px}.back-link:focus-visible{outline:2px solid #111;outline-offset:5px}.review-eyebrow{margin:32px 0 10px;font-size:15px;letter-spacing:.12em;font-weight:700}h1{margin:0 0 12px;font-size:clamp(28px,4vw,42px);line-height:1.15;letter-spacing:-.035em}.review-heading>p:last-child{margin:0;color:#555;font-size:16px;max-width:620px}.logo-options{list-style:none;padding:0;margin:0}.logo-row{display:grid;grid-template-columns:56px minmax(0,1fr);align-items:center;gap:28px;padding:32px 0}.logo-row+.logo-row{border-top:3px solid #000}.logo-number{font-size:40px;font-weight:700;line-height:1;text-align:center;font-variant-numeric:tabular-nums}.logo-row img{display:block;width:100%;height:auto}@media(max-width:600px){.logo-review{padding:24px 16px 32px}.review-heading{padding-bottom:20px}.review-eyebrow{margin-top:24px}.logo-row{grid-template-columns:28px minmax(0,1fr);gap:12px;padding:24px 0}.logo-number{font-size:26px}.review-heading>p:last-child{font-size:15px}}''')
