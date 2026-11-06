# declaudify

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) ![version](https://img.shields.io/badge/version-1.1.2-informational)

declaudify makes anything an AI wrote plain, point-first and easy to follow, without changing what it says.

It is a skill for Claude Code, claude.ai, Codex, Cursor and any agent that reads a `SKILL.md`. It also ships as an always-on output style and as a plain prompt you can paste into any model.

**Before** (a Claude Code reply)

> You're absolutely right to push back on this, and I want to be transparent about the honest shape of what landed.
>
> **Context:** The upload pipeline was gated on a single attempt, so any transient 5xx from the storage layer surfaced as a hard failure to the caller (#142). The load-bearing assumption was that the storage layer is reliable, and that assumption was not holding in staging.
>
> **What I did:**
> - **Retry logic:** Threaded a retry loop through `uploader.ts` with exponential backoff (1s → 2s → 4s), capped at 3 attempts.
> - **Error classification:** Only 5xx responses are retried. 4xx responses fail closed immediately, preserving the existing contract for callers.
> - **Scope boundary:** The download path is orthogonal and was deliberately left untouched to keep the blast radius narrow.
> - **Public API:** Byte-identical. No signature changes.
>
> **Verification:** I ran the full upload suite and it passed cleanly (12 tests, 4 of which are new and exercise the retry seam). As a belt-and-suspenders check I also forced a 503 from staging by hand; the third attempt succeeded, which validates the backoff cadence end-to-end.
>
> One honest caveat: this is a durable path forward for uploads specifically. Downloads remain on the old single-attempt behavior.
>
> **TL;DR:** Uploads now retry up to 3 times on 5xx with 1s/2s/4s backoff; 4xx still fails fast; downloads unchanged; 12 tests green; API unchanged. That's not nothing.
>
> Want me to open a follow-up for the download path, or add the retry count to the telemetry?

**After**

> Uploads now retry on 5xx errors, up to 3 attempts with 1s, 2s, 4s backoff. 4xx errors still fail immediately, so callers see the same contract as before. Downloads are unchanged: still a single attempt. No public API changes, no signature changes.
>
> The cause (#142): the upload pipeline made one attempt, so any transient 5xx from the storage layer reached the caller as a hard failure. That design assumed the storage layer is reliable, and in staging it wasn't. The retry loop lives in `uploader.ts`.
>
> I left the download path alone on purpose, so if the retry has a bug it only affects uploads.
>
> Testing: the full upload suite passes, 12 tests, 4 of them new and covering the retries. I also forced a 503 from staging by hand; the third attempt succeeded.
>
> Still open if you want them: a follow-up for the download path, and adding the retry count to telemetry.

The answer moved to the first sentence. "Gated on", "load-bearing", "byte-identical" and "belt-and-suspenders" became plain words. "Passed cleanly" became the tests that ran. Every number, file and issue survived, and nothing was added. This is a real output from the blind eval below.

## What it does

declaudify edits for the reader, in five moves, in this order:

1. **Find the point and the reader.** What should they know, do or decide? What do they already have?
2. **Lead with it, then give the text the shape its format needs.** A chat answer gets the decision first. A README gets install near the top. A podcast script gets no headings at all. Ten formats have their own rules.
3. **Translate Claudish.** That's the compressed dialect of coding agents: gated on, load-bearing, surfaced, landed cleanly, the honest shape. A 60-entry dictionary turns it into plain words.
4. **Remove the tells, in proportion.** Contrasts, one-line closers, run-ups and chatbot residue go on sight. Triads, bold labels and "-ing" riders go when they cluster. Strong human sentences stay.
5. **Check every fact.** It writes a list of names, numbers, quotes, negations, caveats, paths and commands before editing, and checks the list after. Nothing moves and nothing is added. A missing detail becomes a question, never a guess.

It does not try to beat AI detectors, and it never scores how "AI" a text sounds.

## How it compares

A real 1,071-word plan that Claude wrote, with tables, checklists and a closing question. Each tool edited it three times. Six blind judges scored every output on seven criteria, out of 35, and checked 45 facts that had to survive.

| Tool | Score (of 35) | Facts lost (of 45) |
|---|---|---|
| declaudify | 31.5 | 0.8 |
| blader/humanizer | 29.8 | 1.8 |
| unslop (cursor) | 24.7 | 2.7 |
| Claude, no skill | 24.3 | 4.8 |
| copy-editing (coreyhaines31) | 23.0 | 3.5 |
| no-ai-slop (petergyang) | 22.5 | 2.8 |
| stop-slop | 22.2 | 4.0 |

Only declaudify and blader/humanizer moved the decision from the bottom of the answer to the top. The rest, plain Claude included, cleaned the words and left the shape. The table shows declaudify 1.1.0. This release, 1.1.2, scored 34.2 on the same text in a later blind round against 1.1.0 (33.0) and blader/humanizer (28.2), and lost 0.3 facts of 45.

That is one text, so read it as a direction. A second eval on six formats (chat answer, PR, LinkedIn post, report, podcast script, README) came out the same way. Rubric, fixtures, raw outputs and every judge note are in [`evals/`](evals/).

## Install

Pick the lightest option that fits where you write.

### Claude Code

```text
/plugin marketplace add rosspw/declaudify
/plugin install declaudify@declaudify
```

The plugin answers to `/declaudify:declaudify`. To install the skill alone, under the shorter name `/declaudify`:

```bash
npx skills add rosspw/declaudify --global --agent claude-code
```

### Codex, Cursor, Gemini CLI, Copilot, Windsurf and others

```bash
npx skills add rosspw/declaudify --global --agent '*'
```

Leave off `--global` to install for the current project only. For an agent the Skills CLI doesn't know, copy `SKILL.md` and `references/` into its skills folder.

### claude.ai and Claude Desktop

Download this repository as a ZIP (**Code → Download ZIP**) and upload it under Settings → Capabilities → Skills.

### Always on, in Claude Code

Copy [`output-styles/declaudify.md`](output-styles/declaudify.md) to `~/.claude/output-styles/`, then run `/output-style declaudify`. Replies come out plain the first time. It changes prose only; code, commands and paths are untouched.

### Any model, nothing to install

Paste [`prompt.txt`](prompt.txt) into ChatGPT, Gemini, a claude.ai chat or a Project's instructions, then paste your text.

## Use

```text
/declaudify

[paste your text]
```

Or ask in plain words: "declaudify this", "make this readable", "I can't follow this", "humanize this post", "audit this for AI tells". After one of Claude's own answers, just say "declaudify that".

| Mode | Ask | You get |
|---|---|---|
| Edit (default) | Paste text | The format and how much it changed, the full edit, 3 to 6 bullets on what changed, and any questions under "Gaps" |
| Audit | "audit", "flag", "does this sound like AI", "don't rewrite" | A table of tell, quoted line and fix. No rewrite, no score |
| Last answer | "declaudify that" | Claude's previous reply, rewritten decision-first, every fact and command kept |

**Files.** Point it at a file ("declaudify the prose in docs/launch.md") and it edits prose only. Code blocks, commands, paths, frontmatter, data and link targets stay as they are. To check, keep a copy and run:

```bash
python3 scripts/check_protected.py original.md edited.md
```

It fails if any code, link, table or number moved.

**Your voice.** Paste two or three paragraphs of your own writing first and say so. Your sample overrides every default, dashes included. Personal writing keeps its opinions, humor and asides. Technical text stays plain. A Claude answer has no voice to keep.

## More examples

All three are real outputs from the blind eval (declaudify 1.0). Every fact in each "before" survives in its "after".

<details>
<summary><strong>A PR description</strong>: the template becomes sections a reviewer can scan</summary>

**Before**

> ## 🚀 Summary
>
> This PR introduces a comprehensive, two-phase migration strategy to add the `orders.fulfilled_at` column, significantly enhancing our ability to track fulfillment timelines while maintaining robust backward compatibility. Closes #88.
>
> ## 🔧 Changes
>
> - **Database upgrade:** Migrates from Postgres 14 to 16 to leverage improved batch performance.
> - **Phase 1 (Schema):** Adds `fulfilled_at` as a nullable column, ensuring zero-downtime deployment.
> - **Phase 2 (Backfill):** Executes `scripts/backfill_fulfilled_at.py`, which processes rows in batches of 5,000 to minimize lock contention.
> - **Rollback safety:** Rollback is supported, but only prior to Phase 2 initiation.
>
> ## ⏱️ Performance
>
> The backfill is estimated to take approximately 40 minutes on production. During this window, the read replica may lag by up to 30 seconds. No downtime is anticipated.
>
> ## ✅ Testing
>
> - All 212 existing tests pass.
> - 6 new tests have been added covering the migration and backfill logic.
> - The migration has been thoroughly validated.
>
> ## 📝 Notes
>
> This change marks an important step forward in our data model evolution. Reviewers should note that the two-phase approach was chosen deliberately to balance safety and velocity.

**After**

> **Add orders.fulfilled_at in two phases and upgrade Postgres 14 to 16**
>
> Adds `orders.fulfilled_at` so we can track when orders were fulfilled (#88). The change runs in two phases, a deliberate choice to keep it safe without slowing us down, and stays backward compatible.
>
> ## What changed
>
> - Upgrades Postgres from 14 to 16 for better batch performance.
> - Phase 1 adds `fulfilled_at` as a nullable column, so the deploy needs no downtime.
> - Phase 2 runs `scripts/backfill_fulfilled_at.py`, which fills the column in batches of 5,000 rows to keep lock contention low.
>
> ## What to expect in production
>
> The backfill should take about 40 minutes. While it runs, the read replica may lag by up to 30 seconds. We don't expect any downtime.
>
> ## Rollback
>
> Rollback works only before Phase 2 starts.
>
> ## Testing
>
> All 212 existing tests pass. 6 new tests cover the migration and backfill logic.

</details>

<details>
<summary><strong>A LinkedIn post</strong>: the slop goes, the voice stays</summary>

**Before**

> I wasn't going to post this. But here's the thing.
>
> 11 days ago I opened Claude Code for the first time.
>
> I'm a designer. Not an engineer. Not a founder. Just someone who was tired of our family meal planning living in a group chat.
>
> Today I shipped a meal planner for our family of five.
>
> Nobody asked me to build it. My partner has been using it for three weeks (yes, the prototype came before the "shipping" 😅).
>
> Here's what nobody tells you about vibe coding:
>
> → It works.
> → It also looks like every other AI app. Same gradient. Same cards. Same gray-on-gray text.
> → And I'm a designer, so that hurts more than it should.
>
> The uncomfortable truth? The hard part isn't building anymore. It's taste.
>
> Read that again.
>
> If you've built something with AI: what would you fix first, the function or the look?
>
> #vibecoding #design #claudecode #buildinpublic

**After**

> 11 days ago I opened Claude Code for the first time. Today I shipped a meal planner for our family of five.
>
> I'm a designer. Not an engineer. Not a founder. Just someone who was tired of our family meal planning living in a group chat. Nobody asked me to build it. My partner has been using it for three weeks (yes, the prototype came before the "shipping" 😅).
>
> What I learned about vibe coding: it works. It also looks like every other AI app. Same gradient, same cards, same gray-on-gray text. And I'm a designer, so that hurts more than it should.
>
> Building isn't the hard part anymore. Taste is.
>
> If you've built something with AI: what would you fix first, the function or the look?

</details>

<details>
<summary><strong>A README</strong>: install moves up, the feature wall comes down</summary>

See [`evals/fixtures/6-readme.md`](evals/fixtures/6-readme.md) for the before and [`evals/results/iteration-2/out/NEW/6-readme.md`](evals/results/iteration-2/out/NEW/6-readme.md) for the after. It scored 35 of 35 from its blind judge.

</details>

## How it works

A model writes the choice that fits the widest range of readers. A person writes for one reader. Every habit declaudify fixes is a form of that default: explaining what the reader already knows, staging a point instead of making it, structure applied by rule, a dialect of borrowed metaphors, reassurance with no evidence behind it.

The skill fixes structure first and words second, because word habits change with every model release and structural habits don't. When rules conflict, facts and certainty win, then the user's scope, then the writer's voice, then removing tells. A negation that limits a claim ("not for unlimited energy") and a marker of a guess ("we think") count as facts, not slop.

| File | What it holds |
|---|---|
| [`SKILL.md`](SKILL.md) | The five moves, the modes, the rules that don't bend (under 2,500 words) |
| [`references/format-map.md`](references/format-map.md) | Structure rules for ten formats, with how to detect each |
| [`references/claudish.md`](references/claudish.md) | The Claudish dictionary, combining rules, and habits that survive a word-by-word pass |
| [`references/tells.md`](references/tells.md) | AI tells in three strength tiers, each with a fix and a "keep" line for the lookalike that stays |
| [`references/examples.md`](references/examples.md) | Before and after for each format |
| [`references/self-check.md`](references/self-check.md) | The checklist the skill runs silently after every edit |
| [`output-styles/declaudify.md`](output-styles/declaudify.md) | The always-on version for Claude Code |
| [`prompt.txt`](prompt.txt) | The plain prompt for any model |
| [`evals/`](evals/) | Fixtures, rubric, raw outputs, judge scores |
| [`scripts/`](scripts/) | `validate.py` (package checks) and `check_protected.py` (did code, links or numbers move?) |

## What it isn't

- **A detector-beater.** Detectors and people both guess near chance. If you need text to pass as human for graded or disclosed work, that isn't a writing problem, and this isn't the tool.
- **A scorer.** Audit mode names tells with the line quoted so you can learn them. It never gives a number.
- **A writer.** It won't add a fact, example or source you didn't give it. For new copy, use a copywriting skill.

## Contributing

Found a tell it misses, or a rewrite that changed a fact? Open an issue and paste the real sentence, with what you expected. [`AGENTS.md`](AGENTS.md) has the rules for changing the skill. Run `python3 scripts/validate.py` before a pull request.

## Sources and credit

- Wikipedia, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup.
- [blader/humanizer](https://github.com/blader/humanizer), for the account of why AI text sounds the way it does, the strength ordering, and the repo layout this one follows.
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop), for false agency and narrator-from-a-distance.
- [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh), for the rule priority order, the "keep" examples, and the structure check `check_protected.py` adapts.
- Yuntian Deng's [Claudish translator and dictionary](https://programasweights.com/claudish), and the University of Waterloo Q&A that named the dialect.
- [louisabraham/load-bearing](https://github.com/louisabraham/load-bearing), for the vocabulary measured across 47k GitHub PRs.

## License

MIT. Fork it, translate it, make it yours. If it helps, a star helps other people find it.

Built by [Ross Popoff-Walker](https://rosspw.com), a designer who builds tools for people who build with AI.
