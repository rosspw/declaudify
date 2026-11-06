#!/usr/bin/env python3
"""Check the declaudify package: frontmatter, name, description length, SKILL.md word cap, version sync,
references present. Run from anywhere: python3 scripts/validate.py"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORD_CAP = 2500
fails = []

skill = (ROOT / "SKILL.md").read_text()
m = re.match(r"---\n(.*?)\n---\n(.*)", skill, re.S)
if not m:
    fails.append("SKILL.md has no YAML frontmatter")
    fm, body = "", skill
else:
    fm, body = m.group(1), m.group(2)

name = re.search(r"^name:\s*(.+)$", fm, re.M)
desc = re.search(r"^description:\s*(.+)$", fm, re.M)
ver = re.search(r'^\s*version:\s*"?([0-9]+\.[0-9]+\.[0-9]+)"?', fm, re.M)
if not name or name.group(1).strip() != "declaudify":
    fails.append("frontmatter name must be 'declaudify'")
if not desc:
    fails.append("frontmatter needs a description")
else:
    dtext = desc.group(1).strip()
    if dtext[:1] in "'\"" and dtext[-1:] == dtext[:1]:
        dtext = dtext[1:-1].replace("''", "'") if dtext[0] == "'" else dtext[1:-1]
    elif re.search(r":\s", dtext):
        fails.append("description has ': ' but is not quoted; strict YAML parsers (the Skills CLI) reject it")
    if len(dtext) > 1024:
        fails.append(f"description is {len(dtext)} chars (max 1024)")
if not ver:
    fails.append("frontmatter needs metadata.version")

words = len(re.findall(r"\S+", body))
if words > WORD_CAP:
    fails.append(f"SKILL.md body is {words} words (cap {WORD_CAP})")

for ref in ["format-map.md", "claudish.md", "tells.md", "examples.md", "self-check.md"]:
    if not (ROOT / "references" / ref).exists():
        fails.append(f"missing references/{ref}")
for f in ["output-styles/declaudify.md", "prompt.txt", "README.md", "LICENSE", "CHANGELOG.md"]:
    if not (ROOT / f).exists():
        fails.append(f"missing {f}")

if ver:
    v = ver.group(1)
    for mf in [".claude-plugin/plugin.json", ".cursor-plugin/plugin.json"]:
        p = ROOT / mf
        if p.exists():
            data = json.loads(p.read_text())
            if data.get("version") != v:
                fails.append(f"{mf} version {data.get('version')} != SKILL.md {v}")
    cl = (ROOT / "CHANGELOG.md")
    if cl.exists():
        first = re.search(r"^## (\S+)", cl.read_text(), re.M)
        if first and first.group(1) != v:
            fails.append(f"CHANGELOG first heading {first.group(1)} != SKILL.md {v}")

# No em dashes in the skill's own prose (code and tells examples excepted by file)
for f in ["SKILL.md", "output-styles/declaudify.md", "prompt.txt"]:
    txt = (ROOT / f).read_text()
    if "—" in txt.replace("em and en dashes", "").replace("(—)", ""):
        fails.append(f"{f} contains an em dash in its own prose")

if fails:
    print("FAIL")
    for f in fails:
        print(" -", f)
    sys.exit(1)
print(f"ok: declaudify {ver.group(1) if ver else '?'}, SKILL.md body {words} words, description {len(dtext)} chars")
