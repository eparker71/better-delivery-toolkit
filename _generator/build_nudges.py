#!/usr/bin/env python3
"""Add a "Try this today" nudge to the home page, built from content the site already has.

The pool is each guide's first TIPS_PER_GUIDE tips plus every anti-pattern's "try this". The banner is written into index.html between marked
regions (like build_roles.py's roles:... regions): /* nudge:css */, <!-- nudge:banner --> and <!-- nudge:js -->. The
banner is rendered with the first nudge, so it works without JavaScript; with JavaScript it shows a different nudge each
day, with an "Another" button. The order is fixed by a hash, not by random, so the output is identical on every Python
version (CI fails if committed output differs).

Run after build_roles.py (build_all.py does):  python3 _generator/build_nudges.py
"""
import hashlib
import json
import re
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths  # noqa: E402  (where each file lives; see paths.py)
from build_guides import GUIDES  # noqa: E402
from build_antipatterns import ANTIPATTERNS, ap_id  # noqa: E402

STEM = "How would this fit your team? What would you change?"
TIPS_PER_GUIDE = 2   # keeps the home page light: every tip would add about 120 KB; this gives about 215 nudges, seven months of days
SEED = "2026"

CSS = """/* nudge:css */
.nudge{display:block;margin-top:20px;max-width:760px;padding:12px 16px;border:1px solid #334155;border-left:4px solid var(--accent);border-radius:8px;background:rgba(255,255,255,.05);font-size:13.5px;line-height:1.5;}
.nudge .nk{display:block;font:500 9px 'Geist Mono',monospace;letter-spacing:.14em;color:#FDBA74;text-transform:uppercase;margin-bottom:4px;}
.nudge .nt{color:#fff;font-weight:600;margin-right:6px;}
.nudge .nx{color:#CBD5E1;}
.nudge .ns{display:block;margin-top:6px;font:italic 15px/1.3 'Instrument Serif',Georgia,serif;color:#94A3B8;}
.nudge .nlinks{display:flex;flex-wrap:wrap;gap:6px 16px;align-items:center;margin-top:8px;font-size:12.5px;}
.nudge a{color:#FDBA74;}
.nudge button{font:500 11px 'Geist Mono',monospace;letter-spacing:.04em;color:#fff;background:none;border:1px solid #334155;border-radius:14px;padding:4px 11px;cursor:pointer;}
.nudge button:hover{border-color:var(--accent);color:var(--accent);}
.nudge button[hidden]{display:none;}
/* /nudge:css */
"""


def pool():
    """Each guide's first tips and every anti-pattern fix, in a fixed pseudo-random order, as dicts: t title, x text, h link, l label, s source."""
    items = []
    for g in GUIDES:
        page = f"facilitator-guide-{g['slug']}.html"
        assert paths.path(page).exists(), f"{page} is missing: run build_guides.py first"
        for title, text in g["tips"][:TIPS_PER_GUIDE]:
            items.append(dict(t=title, x=text, h=paths.href("index.html", page), l="Open the guide", s=g["slug"]))
    for _area, symptom, short, _why, fix, _keys in ANTIPATTERNS:
        items.append(dict(t=short, x=f"{symptom} Try this: {fix}", h=paths.href("index.html", f"anti-patterns.html#{ap_id(short)}"),
                          l="See the anti-pattern", s="anti-pattern"))
    return sorted(items, key=lambda n: hashlib.sha256(f"{SEED}|{n['t']}|{n['x']}".encode()).hexdigest())


def build():
    items = pool()
    first = items[0]
    banner = (f'<!-- nudge:banner --><aside class="nudge" aria-label="Try this today"><span class="nk">Try this today</span>'
              f'<span aria-live="polite"><b class="nt">{escape(first["t"])}</b><span class="nx">{escape(first["x"])}</span></span>'
              f'<span class="ns">{escape(STEM)}</span>'
              f'<span class="nlinks"><a class="nl" href="{escape(first["h"])}">{escape(first["l"])} →</a>'
              f'<button type="button" class="nmore" hidden>Another ↻</button><a href="moments.html">Everyday moments →</a></span>'
              f'</aside><!-- /nudge:banner -->')
    data = json.dumps(items, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    js = ("<!-- nudge:js -->\n<script>\n(function(){\nvar N=" + data + ";\n"
          "var box=document.querySelector('.nudge');if(!box||!N.length)return;\n"
          "var i=Math.floor(Date.now()/864e5)%N.length,nl=box.querySelector('.nl'),more=box.querySelector('.nmore');\n"
          "function show(){var n=N[i];box.querySelector('.nt').textContent=n.t;box.querySelector('.nx').textContent=n.x;"
          "nl.href=n.h;nl.textContent=n.l+' →';}\n"
          "more.hidden=false;more.onclick=function(){i=(i+1)%N.length;show();};\n"
          "nl.addEventListener('click',function(){if(window.goatcounter&&window.goatcounter.count)"
          "window.goatcounter.count({path:'nudge/'+N[i].s+'/opened',title:'Nudge opened',event:true});});\n"
          "show();\n})();\n</script>\n<!-- /nudge:js -->\n")

    s = paths.read_index()
    s = re.sub(r"/\* nudge:css \*/.*?/\* /nudge:css \*/\n", "", s, flags=re.S)
    s = s.replace("</style>", CSS + "</style>", 1)
    s = re.sub(r"<!-- nudge:banner -->.*?<!-- /nudge:banner -->\n?", "", s, flags=re.S)
    assert "<!-- roles:bar -->" in s, "run build_roles.py first: the banner sits above its role bar"
    s = s.replace("<!-- roles:bar -->", banner + "\n<!-- roles:bar -->", 1)
    s = re.sub(r"<!-- nudge:js -->.*?<!-- /nudge:js -->\n", "", s, flags=re.S)
    s = s.replace("</body>", js + "</body>", 1)
    paths.write_page("index.html", s)
    print(f"added the Try this today nudge to index.html ({len(items)} nudges, {len(data) // 1024} KB)")


if __name__ == "__main__":
    build()
