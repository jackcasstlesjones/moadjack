"""Pull the CT2 story map (epics, releases, stories) from Jira Cloud."""
import base64
import json
import re
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

SITE = "https://zigzagai.atlassian.net"
PROJECT = "CT2"
SECONDS_PER_DAY = 8 * 3600  # Jira's default working day
START_DATE_FIELD = "customfield_10015"


def load_env(path):
    env = {}
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


class Jira:
    def __init__(self, email, token):
        cred = base64.b64encode(f"{email}:{token}".encode()).decode()
        self.headers = {"Authorization": f"Basic {cred}", "Accept": "application/json",
                        "Content-Type": "application/json", "User-Agent": "story-map-sync"}

    def get(self, path, params=None):
        url = SITE + path + ("?" + urllib.parse.urlencode(params) if params else "")
        with urllib.request.urlopen(urllib.request.Request(url, headers=self.headers)) as r:
            return json.load(r)

    def search(self, jql, fields):
        issues, token = [], None
        while True:
            params = {"jql": jql, "fields": ",".join(fields), "maxResults": 100}
            if token:
                params["nextPageToken"] = token
            page = self.get("/rest/api/2/search/jql", params)
            issues += page["issues"]
            token = page.get("nextPageToken")
            if page.get("isLast", True) or not token:
                return issues


def first_paragraph(wiki):
    """Plain text of the first paragraph of a Jira wiki-markup description."""
    para = re.split(r"\n\s*\n", (wiki or "").strip())[0]
    para = re.sub(r"\[([^|\]]+)\|[^\]]+\]", r"\1", para)  # [text|link] -> text
    return re.sub(r"[*_]{1,2}([^*_]+)[*_]{1,2}", r"\1", para).replace("\n", " ").strip()


def release_slug(name):
    """'Release 2: Full answers' -> 'r2', 'Foundation: ...' -> 'foundation', 'Pre-release: ...' -> 'pre-release'."""
    head = name.split(":")[0].strip().lower()
    m = re.fullmatch(r"release (\d+)", head)
    return f"r{m.group(1)}" if m else head.replace(" ", "-")


def days(seconds):
    d = (seconds or 0) / SECONDS_PER_DAY
    return int(d) if d == int(d) else d


def fetch(env):
    jira = Jira(env["ATLASSIAN_EMAIL_ACCOUNT"], env["ATLASSIAN_API_KEY"])
    project = jira.get(f"/rest/api/2/project/{PROJECT}")
    versions = [v for v in jira.get(f"/rest/api/2/project/{PROJECT}/versions") if not v.get("archived")]
    version_order = {v["name"]: i for i, v in enumerate(versions, 1)}
    could_label = {f"could-{release_slug(v['name'])}": n for v, n in zip(versions, version_order.values())}
    backlog = len(versions) + 1  # coulds with no release label

    epics = jira.search(f"project = {PROJECT} AND issuetype = Epic ORDER BY Rank ASC", ["summary", "description"])
    raw = jira.search(f"project = {PROJECT} AND issuetype = Story ORDER BY Rank ASC",
                      ["summary", "parent", "fixVersions", "timeoriginalestimate", "timeestimate",
                       "status", "duedate", START_DATE_FIELD, "issuelinks", "labels"])

    stories, skipped = [], []
    for i in raw:
        f = i["fields"]
        fv = [v["name"] for v in f.get("fixVersions") or [] if v["name"] in version_order]
        if not f.get("parent"):
            skipped.append(i["key"])
            continue
        # A could keeps its fix version empty so it stays out of Jira's release progress;
        # its intended release comes from a could-<release> label instead.
        placed = [could_label[l] for l in f.get("labels") or [] if l in could_label]
        release = version_order[fv[0]] if fv else (placed[0] if placed else backlog)
        links = [l for l in f.get("issuelinks") or [] if l["type"]["name"] == "Blocks"]
        stories.append({
            "key": i["key"],
            "summary": f["summary"],
            "epic": f["parent"]["key"],
            "release": release,
            "could": not fv,
            "estimate_days": days(f.get("timeoriginalestimate") or f.get("timeestimate")),
            "status": f["status"]["name"],
            "start_date": f.get(START_DATE_FIELD),
            "due_date": f.get("duedate"),
            "blocked_by": [l["inwardIssue"]["key"] for l in links if "inwardIssue" in l],
            "blocks": [l["outwardIssue"]["key"] for l in links if "outwardIssue" in l],
            "url": f"{SITE}/browse/{i['key']}",
        })

    releases = []
    for v in versions:
        n = version_order[v["name"]]
        releases.append({
            "order": n,
            "name": v["name"],
            "start_date": v.get("startDate"),
            "release_date": v.get("releaseDate"),
            "target_outcome": (v.get("description") or "").strip(),
            "estimate_days": days(sum((s["estimate_days"] or 0) * SECONDS_PER_DAY
                                      for s in stories if s["release"] == n and not s["could"])),
        })

    backlog_stories = [s for s in stories if s["release"] == backlog]
    if backlog_stories:
        releases.append({
            "order": backlog,
            "name": "Backlog",
            "start_date": None,
            "release_date": None,
            "target_outcome": "Coulds not yet placed in a release.",
            "estimate_days": 0,
        })

    data = {
        "project": {"name": project["name"], "jira_space": PROJECT, "exported": date.today().isoformat()},
        "epics": [{"order": n, "key": e["key"], "name": e["fields"]["summary"],
                   "description": first_paragraph(e["fields"].get("description")),
                   "url": f"{SITE}/browse/{e['key']}"} for n, e in enumerate(epics, 1)],
        "releases": releases,
        "stories": stories,
    }
    return data, skipped
