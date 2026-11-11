#!/usr/bin/env python3
"""Rebuild index.html.

  python3 build.py            pull epics, releases and stories from Jira, save stories.json, build
  python3 build.py --offline  build from the saved stories.json

Release outcomes come from each Jira version's description.
"""
import json
import sys
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

payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
template = (here / "template.html").read_text()
(here / "index.html").write_text(template.replace("__DATA__", payload))
print("wrote index.html")
