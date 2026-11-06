# Changelog

## 1.1.2

First public release, 2026-11-06, as its own repo. The SKILL.md description is now quoted so strict YAML
parsers (the Skills CLI) can read it; `scripts/validate.py` checks for this.

2026-11-06. The 1.1.1 re-run showed the new fact rules made the editor cautious everywhere: it kept the original
order and decoration and led with the plan's shape less often. One paragraph added under "Rules that do not
bend": the rules limit what changes, not how much moves. Move the decision and a one-line summary to the
top, cut empty decoration, restructure, and carry each fact to its new place.

Re-run the same day (3 runs, 6 blind judges, against 1.1.0, 1.1.1 and blader): 34.2 of 35, highest in 5 of 6
packets. Facts 4.7, 0.3 items lost of 45, no fact added; point first and structure back to 5.0.

## 1.1.1

2026-11-03. One fix from the seven-way eval. declaudify 1.1.0's only
repeated miss there was dropping "We think" from a hypothesis, which turned a guess into a claim. Every
competitor's most common miss was dropping the "not" half of a limiting negation ("not for unlimited
energy", "it doesn't add"), because anti-slop rules read it as a "not X but Y" tell. SKILL.md and the
self-check now name both as facts.

Re-run 2026-11-06 (3 runs, 6 blind judges, against 1.1.0 and blader): the fix worked (facts 4.3 vs 3.3, every
hedge and negation kept), but the editor got more cautious (point first 4.3 vs 5.0) and scored 32.0 vs 33.0
overall.

## 1.1.0

2026-11-02. Lessons from a teardown of five humanizer skills (blader/humanizer, humanizer-zh, stop-slop,
humanizerai, proseify). Not re-run through the blind eval; the 1.0.0 numbers below still describe 1.0.0.

- A priority order for conflicting rules: facts and certainty, then the user's scope, then voice, then tells.
  (From humanizer-zh.)
- A *Keep* line on each act-on-sight tell: the nearest thing that looks like the tell and must stay.
  (From humanizer-zh's keep examples.)
- Warnings are content: a ❌, ⚠️ or bold on a danger is removed only by putting its meaning into words.
  (From humanizer-zh issue #41, where a stripped ❌ turned a first-aid prohibition into an instruction.)
- When you can't ask (file or embedded input), keep the general sentence and list the Gap; bracket only where
  the sentence can't stand. (From blader/humanizer issue #238.)
- The always-on output style now describes good prose and no longer lists banned words, so it doesn't prime
  the model toward them. (From stop-slop issue #10.)
- `scripts/check_protected.py`: compares frontmatter, code, links, URLs, tables, ids and every number
  between an original and an edit. On the eval outputs it caught blader dropping "#142" and adding "12".
  (Adapted from humanizer-zh's `check_structure.py`, MIT.)
- Blind comparison against stop-slop added: stop-slop 27.3 of 35,
  declaudify 32.5, blader 30.7; stop-slop changed or added facts in 5 of 6.

## 1.0.0

First public release, 2026-11-01. Rebuilt from the author's `humanize-writing` skill (two private
iterations, used daily across two repos) after reading the four best-known humanizer skills, Wikipedia's
"Signs of AI writing", and the Claudish dictionary.

- Five moves in a fixed order: point and reader, lead and structure, translate dialect, remove tells,
  check the must-survive list. Structure comes from a format map (ten formats), not from a list of tells.
- The 50-word test for answers and docs. Scripts and personal posts are exempt.
- A Claudish dictionary with 60 entries, three combining rules and 15 structural habits.
- Tells in three strength tiers (act on sight, act in clusters, weak alone), merged from the previous
  catalog, blader/humanizer 3.1, stop-slop and de-slop.
- A must-survive list written before editing and checked after; nothing added, nothing moved.
- Three modes: Edit, Audit, Last answer. File and embedded input shapes.
- A touch budget stated up front: light, medium or rebuild.
- Always-on: a Claude Code output style, a CLAUDE.md snippet, a plain prompt for any model.
- Six fixtures, a pre-registered rubric, and a blind three-way comparison.
- No detector claims, no AI scores, no authorship guesses.

Eval, iteration 2, blind, n=6 per condition: declaudify 32.8 of 35, blader/humanizer 3.1 29.3, the previous
skill 28.7. Won 5 of 6 fixtures; lost the podcast script (30 to 33) for keeping and adding host aphorisms.
Iteration 1 found two misses that were fixed before the re-run: a role descriptor dropped from an
introduction ("solo founder", "the developer-experience team"), and a fact restated in the body after being
moved into the lead. Both are now explicit rules.

Known weakness for 1.1: scripts. Spoken rhythm invites the closers and run-ups the skill strips in prose, and
the script section does not yet say which of those are speech and which are slop.
