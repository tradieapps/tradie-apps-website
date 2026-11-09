#!/usr/bin/env python3
"""Builds the Tradie Apps static site into ./site from page bodies in ./pages."""
import pathlib, re, datetime

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "site"
QW = "https://apps.apple.com/app/id6823936339"
IM = "https://apps.apple.com/app/id6498627150"
EMAIL = "dannielappdevelopment@gmail.com"
YEAR = datetime.date.today().year

NAV = [("index.html", "Home"), ("quotewalk.html", "QuoteWalk"), ("invomile.html", "Invomile"),
       ("tools.html", "Free tools"), ("support.html", "Support")]

def header(current):
    links = "".join(
        f'<a href="{h}"{" aria-current=page" if h == current else ""}>{t}</a>' for h, t in NAV)
    return f'''<header class="nav"><div class="wrap">
<a class="brand" href="index.html"><span class="brand-mark">TA</span>TRADIE APPS</a>
<button class="menu-btn" aria-label="Menu" onclick="document.querySelector('.nav nav').classList.toggle('open')">☰</button>
<nav>{links}</nav></div></header>'''

FOOTER = f'''<footer><div class="wrap"><div class="cols">
<div><a class="brand" href="index.html"><span class="brand-mark">TA</span>TRADIE APPS</a>
<p style="margin-top:12px">Simple iPhone apps for tradies and sole traders. Your data stays on your phone.</p></div>
<div><h4>Apps</h4><a href="quotewalk.html">QuoteWalk</a><a href="invomile.html">Invomile</a></div>
<div><h4>Free tools</h4><a href="paint-calculator.html">Paint calculator</a><a href="tile-flooring-calculator.html">Tile &amp; flooring calculator</a><a href="painting-quote-calculator.html">Quote calculator</a></div>
<div><h4>Help</h4><a href="support.html">Support</a><a href="mailto:{EMAIL}">Email us</a><a data-link="qwPrivacy" href="#">QuoteWalk privacy</a><a data-link="imPrivacy" href="#">Invomile privacy</a></div>
</div><div class="copy">© {YEAR} Tradie Apps · Australia · Apple, iPhone and App Store are trademarks of Apple Inc.</div></div></footer>'''

def store(url, label="Download on the", big="App Store"):
    return f'<a class="appstore" href="{url}" target="_blank" rel="noopener"><span><small>{label}</small><b>{big}</b></span></a>'

def page(fname, title, desc, body, extra_head=""):
    html = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:type" content="website"><meta name="theme-color" content="#0b1a3a">
<link rel="icon" href="apple-touch-icon.png"><link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="stylesheet" href="assets/style.css">
<script src="assets/site.js"></script>{extra_head}
</head><body>
{header(fname)}
<main>{body}</main>
{FOOTER}
</body></html>'''
    html = html.replace("{QW}", QW).replace("{IM}", IM).replace("{EMAIL}", EMAIL)
    html = html.replace("{STORE_QW}", store(QW)).replace("{STORE_IM}", store(IM))
    (OUT / fname).write_text(html)

for f in sorted((ROOT / "pages").glob("*.html")):
    src = f.read_text()
    m = re.match(r"<!--\s*title:(.*?)\n\s*desc:(.*?)\n(?:\s*head:(.*?)\n)?\s*-->\n", src, re.S)
    title, desc, head = m.group(1).strip(), m.group(2).strip(), (m.group(3) or "").strip()
    page(f.name, title, desc, src[m.end():], head)
    print("built", f.name)
