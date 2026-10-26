#!/usr/bin/env python3
"""Generate moments.html: small moments in the working day, each with the idea underneath and a few different ways teams handle it.

The content is _content/moments.md (format explained at the top of that file), read and checked by moments_data.py.
Each moment links the tools it draws on, the anti-pattern it can be spotted as, the bigger scenario, the Prompt Library
entry and, when there is one, the worked example in the Basket team's story. A moment's "I tried this" button sends a
GoatCounter event, and only appears when GoatCounter has loaded (the same approach as the guides' feedback buttons).

Run:  python3 _generator/build_moments.py
"""
import re
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths  # noqa: E402  (where each file lives; see paths.py)
from build_roles import TOOLS, FONT_URL  # noqa: E402
from build_antipatterns import ap_id  # noqa: E402
from build_prompts import PROMPTS  # noqa: E402
from moments_data import parse, GROUPS  # noqa: E402
from brand import ACCENT, NAVY, CREDIT  # noqa: E402

slug = lambda s: re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
PROMPT_TITLES = {p[0]: p[2] for p in PROMPTS}
STEM = "Which would fit your team? What would you change? What's a way nobody here has tried?"

TRIED_JS = ("(function(){window.addEventListener('load',function(){if(!(window.goatcounter&&window.goatcounter.count))return;"
            "document.querySelectorAll('.tried').forEach(function(b){b.hidden=false;b.onclick=function(){"
            "window.goatcounter.count({path:'moment/'+b.dataset.id+'/tried',title:'Moment tried',event:true});"
            "b.disabled=true;b.textContent='Thanks, nice one';}})})})();")


def card(m):
    deeper = ["Tools: " + " · ".join(f'<a href="{TOOLS[k][1]}">{escape(TOOLS[k][0])}</a>' for k in m["tools"])]
    if m["spot"]:
        deeper.append(f'Spot it: <a href="anti-patterns.html#{ap_id(m["spot"])}">{escape(m["spot"])}</a>')
    if m["bigger"]:
        deeper.append(f'Bigger version: <a href="scenarios.html#{slug(m["bigger"])}">{escape(m["bigger"])}</a>')
    if m["prompt"]:
        deeper.append(f'Prompt: <a href="prompt-library.html#{m["prompt"]}">{escape(PROMPT_TITLES[m["prompt"]])}</a>')
    ex = next((f"worked-example-{TOOLS[k][1]}" for k in m["tools"] if paths.path(f"worked-example-{TOOLS[k][1]}").exists()), None)
    if ex:
        deeper.append(f'<a href="{ex}">See it in the Basket story →</a>')
    search = " ".join([m["title"], m["group"], m["notice"], m["going"], *m["ways"], m["whatif"]] + [TOOLS[k][0] for k in m["tools"]]).lower()
    return (f'<article class="mc" id="{m["id"]}" data-text="{escape(search)}"><h3>{escape(m["title"])}</h3>'
            f'<p class="notice"><b>You\'ll notice</b> {escape(m["notice"])}</p>'
            f'<p class="going"><b>What\'s going on</b> {escape(m["going"])}</p>'
            f'<div class="ways"><p class="lbl">Ways to try <em>(examples, not answers)</em></p>'
            f'<ul>{"".join(f"<li>{escape(w)}</li>" for w in m["ways"])}</ul></div>'
            f'<div class="yours"><p class="lbl">Make it yours</p><p class="wi">What if: {escape(m["whatif"])}</p>'
            f'<p class="stem">{escape(STEM)}</p></div>'
            f'<p class="deeper">{" · ".join(deeper)}</p>'
            f'<button type="button" class="tried" data-id="{m["id"]}" hidden>I tried a version of this</button></article>')


def build():
    moments = parse()
    for m in moments:
        if m["prompt"] and m["prompt"] not in PROMPT_TITLES:
            sys.exit(f"moments.md: “{m['title']}” has Prompt “{m['prompt']}”, which isn't a prompt id in build_prompts.py.")
    groups = {g: [m for m in moments if m["group"] == g] for g in GROUPS}
    present = [g for g in GROUPS if groups[g]]
    chips = "".join(f'<a href="#g-{slug(g)}">{escape(g)}</a>' for g in present)
    sections = "\n".join(f'<section class="grp" id="g-{slug(g)}"><h2>{escape(g)} <span>{len(groups[g])}</span></h2>'
                         f'<div class="grid">{"".join(card(m) for m in groups[g])}</div></section>' for g in present)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Everyday Moments</title>
<link rel="stylesheet" href="{FONT_URL}">
<style>
:root{{--accent:{ACCENT};--navy:{NAVY};--ink:#1E293B;--muted:#5B6B82;--rule:#E2E8F0;}}
*{{box-sizing:border-box;}}
[hidden]{{display:none !important;}}
html,body{{margin:0;background:#F1F5F9;}}
body{{font-family:'Geist',Inter,system-ui,sans-serif;color:var(--ink);font-size:14px;line-height:1.55;}}
header{{background:var(--navy);border-top:4px solid var(--accent);color:#fff;padding:36px 16px 26px;}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 16px;}}
h1{{font:400 44px/1.05 'Instrument Serif',Georgia,serif;margin:0 0 8px;}}
header p{{color:#94A3B8;margin:0 0 14px;max-width:780px;}}
header p a{{color:#FDBA74;}}
header a.back{{color:#94A3B8;font:500 11px 'Geist Mono',monospace;letter-spacing:.06em;}}
input{{font:14px 'Geist',system-ui,sans-serif;padding:8px 12px;border-radius:6px;border:1px solid #334155;background:#0F2236;color:#fff;width:100%;max-width:380px;margin-bottom:12px;}}
input::placeholder{{color:#8291A6;}}
nav.chips{{display:flex;flex-wrap:wrap;gap:8px;}}
nav.chips a{{color:#fff;text-decoration:none;font-size:12.5px;border:1px solid #334155;border-radius:999px;padding:5px 12px;background:#0F2236;}}
nav.chips a:hover{{border-color:var(--accent);}}
main{{padding:20px 0 48px;}}
.how{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:0 0 4px;}}
.how div{{background:#fff;border:1px solid var(--rule);border-radius:8px;padding:12px 16px;font-size:13px;}}
.how b{{display:block;font:600 9.5px 'Geist Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:#9A3412;margin-bottom:3px;}}
h2{{font:500 11px 'Geist Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:28px 0 10px;scroll-margin-top:12px;}}
h2 span{{margin-left:6px;}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:12px;}}
.mc{{background:#fff;border:1px solid var(--rule);border-top:4px solid #0C4A6E;border-radius:8px;padding:14px 16px;display:flex;flex-direction:column;scroll-margin-top:12px;}}
.mc h3{{margin:0 0 6px;font-size:16px;}}
.mc p{{margin:0 0 8px;}}
.mc .notice{{color:var(--muted);font-size:13px;}}
.mc .notice b,.mc .going b{{font:600 9.5px 'Geist Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:#0C4A6E;margin-right:6px;}}
.ways{{background:#FFF7ED;border:1px solid #FED7AA;border-left:4px solid #C2410C;border-radius:6px;padding:9px 12px;margin:2px 0 8px;}}
.ways ul{{margin:0;padding-left:18px;}}
.ways li{{margin:0 0 5px;}}
.ways li:last-child{{margin:0;}}
.lbl{{font:600 9.5px 'Geist Mono',monospace;letter-spacing:.12em;text-transform:uppercase;margin:0 0 4px !important;}}
.ways .lbl{{color:#9A3412;}}
.ways .lbl em{{font-style:normal;text-transform:none;letter-spacing:0;font-weight:500;color:var(--muted);}}
.yours{{background:#EFF6FF;border:1px solid #BFDBFE;border-left:4px solid #1E3A8A;border-radius:6px;padding:9px 12px;margin:0 0 8px;}}
.yours .lbl{{color:#1E3A8A;}}
.yours p{{margin:0 0 4px;}}
.yours .wi{{font:italic 15px/1.35 'Instrument Serif',Georgia,serif;}}
.yours .stem{{font-size:12.5px;color:var(--muted);margin:0;}}
.mc .deeper{{font-size:12px;color:var(--muted);margin:auto 0 0;padding-top:8px;border-top:1px solid var(--rule);}}
.mc .deeper a{{color:#9A3412;}}
button{{align-self:flex-start;font:500 12.5px 'Geist',system-ui,sans-serif;color:#fff;background:#0C1A2E;border:0;border-radius:999px;padding:6px 13px;cursor:pointer;margin-top:10px;}}
button:hover{{background:#C2410C;}}
button:disabled{{background:#475569;cursor:default;}}
.hidden{{display:none !important;}}
footer{{font:9px 'Geist Mono',monospace;letter-spacing:.08em;color:#5B6B82;text-align:center;padding:0 16px 32px;}}
@media (max-width:700px){{.how{{grid-template-columns:1fr;}}}}
@media print{{header{{padding:16px;}} input,nav.chips,button{{display:none;}} .mc{{break-inside:avoid;}}}}
</style>
</head>
<body>
<header><div class="wrap">
  <a class="back" href="index.html">← All tools</a>
  <h1>Everyday Moments</h1>
  <p>Small moments in the working day, and what each can teach. Each gives you the idea underneath and a few different ways teams handle it: examples to adapt, not answers to copy. For bigger situations, see the <a href="scenarios.html">Scenario Playbook</a>.</p>
  <input type="search" placeholder="Search moments, e.g. “stand-up” or “estimate”…" aria-label="Search moments">
  <nav class="chips" aria-label="Groups">{chips}</nav>
</div></header>
<main><div class="wrap">
<div class="how">
  <div><b>1 · Notice it</b>Find the moment that sounds like your week. You don't need to be an expert, or in charge.</div>
  <div><b>2 · See the pattern</b>Read the idea underneath, and the different ways teams handle it. They're examples, not answers.</div>
  <div><b>3 · Make it yours</b>Pick one, change it to fit your team, ask what you'd do if a condition changed, then try a way that isn't listed.</div>
</div>
{sections}
</div></main>
<footer>{escape(CREDIT)}</footer>
<script>
(function(){{
  var input=document.querySelector('input');
  input.addEventListener('input', function(){{
    var q=input.value.trim().toLowerCase();
    document.querySelectorAll('.grp').forEach(function(sec){{
      var any=false;
      sec.querySelectorAll('.mc').forEach(function(c){{
        var ok=!q || c.dataset.text.indexOf(q)>=0; c.classList.toggle('hidden', !ok); if(ok) any=true;
      }});
      sec.classList.toggle('hidden', !any);
    }});
  }});
}})();
{TRIED_JS}
</script>
</body>
</html>
"""
    paths.write_page("moments.html", page)
    print(f"wrote moments.html ({len(moments)} moments)")


if __name__ == "__main__":
    build()
