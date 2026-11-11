#!/usr/bin/env python3
"""Rebuild index.html.

  python3 build.py            pull epics, releases and stories from Jira, save stories.json, build
  python3 build.py --offline  build from the saved stories.json

Release outcomes and details come from updates-to-releases.md when present.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

here = Path(__file__).parent

if "--offline" in sys.argv:
    data = json.loads((here / "stories.json").read_text())
else:
    import jira
    data, skipped = jira.fetch(jira.load_env(here / ".env"))
    (here / "stories.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"pulled {len(data['epics'])} epics, {len(data['releases'])} releases, {len(data['stories'])} stories from Jira")
    if skipped:
        print("skipped (no release or epic):", ", ".join(skipped))
MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}


def parse_range(text):
    m = re.match(r"(\d+) (\w+)(?: (\d{4}))? to (\d+) (\w+) (\d{4})", text)
    d1, m1, y1, d2, m2, y2 = m.groups()
    y2 = int(y2)
    y1 = int(y1) if y1 else (y2 - 1 if MONTHS[m1] > MONTHS[m2] else y2)
    iso = lambda d, mo, y: datetime(y, MONTHS[mo], int(d)).strftime("%Y-%m-%d")
    return iso(d1, m1, y1), iso(d2, m2, y2)


def parse_releases(md):
    out = {}
    for block in re.split(r"^## ", md, flags=re.M)[1:]:
        head = re.match(r"Release (\d+): (.+)", block)
        if not head:
            continue
        rel = {"name": f"Release {head[1]}: {head[2].strip()}"}
        meta = re.search(r"^\*\*(.+?)\*\*\s*$", block, flags=re.M)
        if meta:
            rel["start_date"], rel["release_date"] = parse_range(meta[1])
            days = re.search(r"([\d.]+) days", meta[1])
            if days:
                rel["estimate_days"] = float(days[1])
        sections = {}
        for sec in re.split(r"^### ", block, flags=re.M)[1:]:
            title, _, body = sec.partition("\n")
            body = body.split("\n---")[0].strip()
            if title.strip() == "What people can do":
                groups = []
                for line in body.splitlines():
                    line = line.strip()
                    if re.fullmatch(r"\*\*.+\*\*", line):
                        groups.append({"epic": line.strip("*"), "items": []})
                    elif line.startswith("- ") and groups:
                        groups[-1]["items"].append(line[2:])
                sections[title.strip()] = groups
            else:
                sections[title.strip()] = body
        rel["target_outcome"] = sections.pop("Outcome", None)
        rel["details"] = sections
        out[int(head[1])] = {k: v for k, v in rel.items() if v}
    return out


md_path = here / "updates-to-releases.md"
if md_path.exists():
    updates = parse_releases(md_path.read_text())
    for r in data["releases"]:
        u = updates.get(r["order"], {})
        for k in ("target_outcome", "details"):
            if k in u:
                r[k] = u[k]

payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
template = (here / "template.html").read_text()
(here / "index.html").write_text(template.replace("__DATA__", payload))
print("wrote index.html")
