#!/usr/bin/env python3
"""Pull the latest from Jira, rebuild the page, and push it to GitHub Pages.

  python3 publish.py
"""
import subprocess
import sys
from datetime import date
from pathlib import Path

here = Path(__file__).parent


def run(*cmd, check=True):
    return subprocess.run(cmd, cwd=here, check=check, text=True, capture_output=True)


subprocess.run([sys.executable, "build.py"], cwd=here, check=True)

if not run("git", "status", "--porcelain").stdout.strip():
    print("No changes since the last publish.")
    sys.exit(0)

run("git", "add", "-A")
run("git", "commit", "-m", f"Sync from Jira {date.today().isoformat()}")
run("git", "push")
print("Pushed. The site updates in about a minute: https://jackcasstlesjones.github.io/moadjack/")
