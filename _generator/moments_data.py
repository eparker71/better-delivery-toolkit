"""Everyday Moments: read and check _content/moments.md.

Used by build_moments.py (the page) and build_guides.py ("Moments where this helps" in each guide). It imports only
modules that don't import build_guides, so there's no import cycle. Prompt ids are checked in build_moments.py, because
build_prompts.py imports build_guides.

Each moment is a dict: id, title, group, notice, going (the idea underneath), ways (a list of two to four different
ways teams handle it), whatif (a question that changes a condition), tools (keys), spot (anti-pattern label or ""),
bigger (scenario title or ""), prompt (prompt id or "").
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_roles import TOOLS  # noqa: E402
from build_antipatterns import ANTIPATTERNS  # noqa: E402
from build_scenarios import parse as parse_scenarios, _smart  # noqa: E402

SRC = Path(__file__).resolve().parent.parent / "_content" / "moments.md"
GROUPS = ["Daily", "Planning & refinement", "Review & demo", "Retro", "Board & flow", "Estimates & forecasts",
          "Stakeholders & reports", "Releases & quality", "Team & conflict", "Working with AI"]
MIN_MOMENTS = 40
MAX_WORDS = {"going": 60}
MAX_WAY_WORDS, WAYS = 25, (2, 4)
FIELDS = {"event": "group", "you'll notice": "notice", "what's going on": "going", "ways to try": "ways",
          "what if": "whatif", "tools": "tools", "spot it": "spot", "bigger version": "bigger", "prompt": "prompt"}
REQUIRED = ["group", "notice", "going", "ways", "whatif", "tools"]
BY_TITLE = {re.sub(r"\s+", " ", v[0]).lower(): k for k, v in TOOLS.items()}


def moment_id(title):
    """Anchor id from a moment's title: apostrophes and quotes dropped, other punctuation to hyphens."""
    t = re.sub(r"[‘’“”'\"]", "", title.lower())
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def parse():
    text = _smart(re.sub(r"<!--.*?-->", "", SRC.read_text(encoding="utf-8"), flags=re.S))
    labels = {a[2] for a in ANTIPATTERNS}
    scenarios = {s["title"] for area in parse_scenarios() for s in area["items"]}
    moments, cur = [], None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("## "):
            cur = {"title": line[3:].strip(), "tools": [], "ways": [], "spot": "", "bigger": "", "prompt": ""}
            cur["id"] = moment_id(cur["title"])
            moments.append(cur)
            continue
        if line.startswith("- ") and cur is not None:
            cur["ways"].append(line[2:].strip())
            continue
        name, _, value = line.partition(":")
        field = FIELDS.get(name.strip().lower())
        if cur is None or not field:
            sys.exit(f"moments.md: don't understand the line “{line[:60]}”")
        value = value.strip()
        if field == "tools":
            for t in [n.strip() for n in value.split(",") if n.strip()]:
                key = BY_TITLE.get(t.lower())
                if not key:
                    sys.exit(f"moments.md: unknown tool “{t}” in “{cur['title']}”. Use a title from TOOLS in build_roles.py.")
                cur["tools"].append(key)
        elif field != "ways":
            cur[field] = value[:1].upper() + value[1:] if field in ("notice", "whatif") else value
    ids = set()
    for m in moments:
        t = m["title"]
        for f in REQUIRED:
            if not m.get(f):
                sys.exit(f"moments.md: “{t}” has no {f}.")
        if m["id"] in ids:
            sys.exit(f"moments.md: two moments share the id “{m['id']}”.")
        ids.add(m["id"])
        if m["group"] not in GROUPS:
            sys.exit(f"moments.md: “{t}” has Event “{m['group']}”; use one of: {', '.join(GROUPS)}.")
        if m["spot"] and m["spot"] not in labels:
            sys.exit(f"moments.md: “{t}” has Spot it “{m['spot']}”, which isn't an anti-pattern label in build_antipatterns.py.")
        if m["bigger"] and m["bigger"] not in scenarios:
            sys.exit(f"moments.md: “{t}” has Bigger version “{m['bigger']}”, which isn't a scenario title in scenarios.md.")
        for f, limit in MAX_WORDS.items():
            if len(m[f].split()) > limit:
                sys.exit(f"moments.md: “{t}” has {len(m[f].split())} words in its {f}; keep it to {limit}.")
        if not WAYS[0] <= len(m["ways"]) <= WAYS[1]:
            sys.exit(f"moments.md: “{t}” has {len(m['ways'])} ways to try; give {WAYS[0]} to {WAYS[1]}.")
        for w in m["ways"]:
            if len(w.split()) > MAX_WAY_WORDS:
                sys.exit(f"moments.md: “{t}” has a way with {len(w.split())} words; keep each to {MAX_WAY_WORDS}: “{w[:40]}…”")
    if len(moments) < MIN_MOMENTS:
        sys.exit(f"moments.md: {len(moments)} moments; expected at least {MIN_MOMENTS}.")
    return moments


def by_tool():
    """Tool key -> the moments that list it, in file order."""
    out = {}
    for m in parse():
        for k in m["tools"]:
            out.setdefault(k, []).append(m)
    return out
