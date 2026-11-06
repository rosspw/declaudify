# Guide for agents and contributors

This repo is one skill written in Markdown. `SKILL.md` is the prompt agents read. There is no build step.

## Files that matter

- `SKILL.md` is the product. Every word of it is read on every use, so the validator caps its body at
  2,500 words. Anything that does not need to be read every time goes in `references/`.
- `references/format-map.md`, `claudish.md`, `tells.md`, `examples.md`, `self-check.md` are loaded by the
  skill when it needs them. They can grow; keep their contents tables current.
- `output-styles/declaudify.md` and `prompt.txt` are the always-on versions. When a rule changes in
  `SKILL.md`, change it there too, shorter.
- `README.md` opens with a before/after and lists install paths for every surface. Keep it in sync with
  the skill's modes and files.
- `CHANGELOG.md` holds release notes, newest first. Its first heading is the version.
- `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.cursor-plugin/plugin.json`,
  `agents/openai.yaml` are the manifests. Their descriptions are the first sentence of the skill's.
- `evals/` holds the fixtures, the pre-registered rubric and the results. The README's table is copied
  from `evals/results.md` and nowhere else.

## Rules for changes

- **Version.** The same version in `SKILL.md` (`metadata.version`), both plugin manifests and the first
  `CHANGELOG.md` heading. `python3 scripts/validate.py` checks this.
- **Tells.** A new tell earns an entry only when no existing one implies it. Put it in the right strength
  tier with a watched phrase, a quoted example and a fix. Prefer folding into an existing entry.
- **Claudish.** A new term needs the sentence it appeared in and the plain meaning. Add it to the table in
  `claudish.md`. Do not add banned-word lists to the output style: it describes good prose positively, so it
  doesn't prime the model toward the words it should avoid.
- **Facts.** Every example in `examples.md` keeps every fact from its before and adds none. A missing
  specific is shown as a Gap. An example that adds a detail is a bug.
- **Formats.** A new format gets a detection row and a section with four parts: structure that serves,
  structure that is noise, patterns to flag, rewrite rules.
- **Evals.** A change that touches a move or a tier gets re-run against the fixtures before release. Update
  `evals/results.md` and the README table together, with n.
- **Claims.** No detector claims, no scores, no user counts without a number and a date behind them.
- **Examples.** Run every new example through `scripts/check_protected.py` against its before.
- **Checks before publishing.** `python3 scripts/validate.py`, `npx skills add . --list`,
  `claude plugin validate .`.

## Writing style for this repo

Plain words, short sentences, active voice, one term per thing, sentence case headings, no em dashes.
Explain why a rule exists so an agent can apply it to a case the rule did not foresee. The skill's own
prose must pass the skill.
