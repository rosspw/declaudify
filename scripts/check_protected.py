#!/usr/bin/env python3
"""Compare the parts of a Markdown file that declaudify must never change: frontmatter, fenced code,
inline code, link targets, table rows, explicit HTML ids, URLs, and every number. Use it after File mode:

    python3 scripts/check_protected.py original.md edited.md

Headings and ordered steps are reported but not failed, because a requested restructure may change them.
Exits non-zero when a protected part differs. Read-only. Adapted from op7418/humanizer-zh
tests/check_structure.py (MIT)."""
import argparse, json, re, sys
from pathlib import Path

def parts(text):
    fm = re.match(r"\A---\n.*?\n---\n", text, re.S)
    body = text[fm.end():] if fm else text
    fences = re.findall(r"^```[^\n]*\n.*?^```[ \t]*$", body, re.M | re.S)
    prose = re.sub(r"^```[^\n]*\n.*?^```[ \t]*$", "", body, flags=re.M | re.S)
    return {
        "frontmatter": [fm.group(0)] if fm else [],
        "fenced_code": fences,
        "inline_code": re.findall(r"(?<!`)`([^`\n]+)`(?!`)", prose),
        "link_targets": re.findall(r"\]\(([^\s)]+)", prose),
        "urls": re.findall(r"https?://[^\s)>\]]+", prose),
        "table_rows": re.findall(r"^\|.*\|$", prose, re.M),
        "explicit_ids": re.findall(r'<[^>]+\bid="[^"]+"[^>]*>', prose),
        "numbers": [n.rstrip(".,") for n in re.findall(r"\d[\d,.]*%?", re.sub(r"`[^`\n]+`", "", prose))],
    }, {
        "headings": re.findall(r"^#{1,6} .+$", prose, re.M),
        "ordered_steps": re.findall(r"^\d+\. .+$", prose, re.M),
    }

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("original", type=Path); ap.add_argument("edited", type=Path)
    a = ap.parse_args()
    (p1, i1), (p2, i2) = parts(a.original.read_text(encoding="utf-8")), parts(a.edited.read_text(encoding="utf-8"))
    report = {}
    for k in p1:
        # numbers, urls and inline code may move or repeat: fail only on a value that vanished or a new one.
        if k in ("numbers", "urls", "inline_code"):
            missing, added = sorted(set(p1[k]) - set(p2[k])), sorted(set(p2[k]) - set(p1[k]))
            report[k] = {"same": not missing and not added, "missing": missing, "added": added}
        else:
            report[k] = {"same": p1[k] == p2[k]}
    info = {k: {"same": i1[k] == i2[k]} for k in i1}
    ok = all(v["same"] for v in report.values())
    print(json.dumps({"protected": report, "info_only": info, "passed": ok}, indent=2, ensure_ascii=False))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
