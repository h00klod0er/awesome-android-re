#!/usr/bin/env python3
"""Refresh ★ and 更新 columns in README.md from GitHub API."""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
GITHUB_RE = re.compile(
    r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:[)/\s#]|$)"
)
TABLE_ROW_RE = re.compile(
    r"^(\| \[[^\]]+\]\(https://github\.com/([^/\)]+)/([^/\)#\s]+)(?:/[^\)]*)?\)(?:[^|]*)\| )"
    r"([^|]*?)(\| )([^|]*?)(\| )",
    re.MULTILINE,
)
INLINE_RE = re.compile(
    r"(\[([^\]]+)\]\(https://github\.com/([^/\)]+)/([^/\)#\s]+)(?:/[^\)]*)?\))"
    r"((?:[^\n]*?)· ★)([\d,]+)( · 更新 )(\d{4}-\d{2}-\d{2})"
)
STATS_NOTE_RE = re.compile(r"> \*\*统计说明（[^）]+）\*\*：.*")


def fmt_stars(n: int) -> str:
    return f"{n:,}"


def fetch_repo(owner: str, repo: str, token: str | None) -> dict | None:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-re-mcp-stats",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"warn: {owner}/{repo} HTTP {e.code}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"warn: {owner}/{repo} {e}", file=sys.stderr)
        return None
    pushed = data.get("pushed_at") or data.get("updated_at")
    if not pushed:
        return None
    dt = datetime.fromisoformat(pushed.replace("Z", "+00:00")).astimezone(timezone.utc)
    return {
        "stars": int(data.get("stargazers_count") or 0),
        "pushed": dt.strftime("%Y-%m-%d"),
        "full": data.get("full_name") or f"{owner}/{repo}",
    }


def collect_repos(text: str) -> list[tuple[str, str]]:
    seen: set[tuple[str, str]] = set()
    out: list[tuple[str, str]] = []
    for m in GITHUB_RE.finditer(text):
        owner, repo = m.group(1), m.group(2)
        if repo.endswith(".git"):
            repo = repo[:-4]
        key = (owner.lower(), repo.lower())
        if key in seen:
            continue
        if owner.lower() in {"topics", "settings", "marketplace"}:
            continue
        seen.add(key)
        out.append((owner, repo))
    return out


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    text = README.read_text(encoding="utf-8")
    repos = collect_repos(text)
    cache: dict[tuple[str, str], dict] = {}
    for i, (owner, repo) in enumerate(repos):
        info = fetch_repo(owner, repo, token)
        if info:
            cache[(owner.lower(), repo.lower())] = info
            print(f"{info['full']:40} ★{info['stars']:6}  {info['pushed']}")
        if i + 1 < len(repos):
            time.sleep(0.05)

    def lookup(owner: str, repo: str) -> dict | None:
        return cache.get((owner.lower(), repo.lower()))

    def repl_table(m: re.Match[str]) -> str:
        owner, repo = m.group(2), m.group(3)
        info = lookup(owner, repo)
        if not info:
            return m.group(0)
        stars = fmt_stars(info["stars"])
        return f"{m.group(1)}{stars}{m.group(5)}{info['pushed']}{m.group(7)}"

    new_text = TABLE_ROW_RE.sub(repl_table, text)

    def repl_inline(m: re.Match[str]) -> str:
        owner, repo = m.group(3), m.group(4)
        info = lookup(owner, repo)
        if not info:
            return m.group(0)
        return (
            f"{m.group(1)}{m.group(5)}{fmt_stars(info['stars'])}"
            f"{m.group(7)}{info['pushed']}"
        )

    new_text = INLINE_RE.sub(repl_inline, new_text)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    note = (
        f"> **统计说明（{now}）**：`★` = GitHub Stars；`更新` = 仓库最近一次 `pushed_at`（推送）日期。"
        f"由 [GitHub Actions](.github/workflows/update-stats.yml) 每周一自动刷新；也可手动 `workflow_dispatch`。"
        f"PyPI-only 包无独立 star，会注明对应源码仓。"
    )
    if STATS_NOTE_RE.search(new_text):
        new_text = STATS_NOTE_RE.sub(note, new_text, count=1)
    else:
        new_text = new_text.replace(
            "> 不含：通用编程助手、与 RE 无关的安全扫描器。\n",
            "> 不含：通用编程助手、与 RE 无关的安全扫描器。\n\n" + note + "\n",
            1,
        )

    if new_text == text:
        print("no changes")
        return 0
    README.write_text(new_text, encoding="utf-8")
    print("README.md updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
