# Format map

Detect the format, then apply its section on top of `tells.md`. The writer's own established style for a
format beats these defaults. Structure here means what serves *this* reader in *this* format; it is never a
list of things to strip.

## Contents

- Detection
- Chat answer
- Doc or report
- README or technical doc
- PR description or commit message
- LinkedIn post
- Email
- Slack or DM
- Script (podcast, video, talk)
- Slides or artifact text
- UI copy

---

## Detection

| Format | Signals |
|---|---|
| Chat answer | The target is the previous assistant turn, or pasted text that answers a question: "Yes, because...", status lines, "I ran...", a TL;DR label, bold-label bullets, a closing offer |
| Doc or report | Headings, 1,500+ words of developed argument, an executive summary, numbered sections, "this document" |
| README or technical doc | A project name as title, install or usage sections, code fences, badges, "Getting started", a file tree |
| PR description or commit | "This PR", "Closes #", a Summary / Changes / Testing shape, a diff vocabulary (refactor, migrate, bump), a one-line subject under 72 chars |
| LinkedIn post | One sentence per line, hashtags, @mentions, an engagement ask, a story hook, under 3,000 characters, no headings |
| Email | Subject line, To or greeting ("Hi Sam"), sign-off plus name, "following up", one ask |
| Slack or DM | #channel or @here, :emoji_codes:, no greeting or sign-off, fragments, under ~500 characters |
| Script | Speaker labels, timestamps, "[pause]", stage directions, second person spoken rhythm, "welcome back", a cold open |
| Slides or artifact text | Slide numbers or titles, very short lines, speaker notes, HTML or a component tree with copy inside, a hero and sections |
| UI copy | Button labels, empty states, error messages, tooltips, onboarding steps, a strings file |

Ambiguous: treat as a doc and say "Format: doc (unclear). Tell me if it's something else and I'll re-run."

---

## Chat answer

The reader asked a question and already has the whole conversation. They want the decision or answer, and
only the reasoning that would change whether they agree.

**Structure that serves:** the answer in the first sentence; the one fact or risk that would change it;
then details in the order the reader would ask for them. Code, commands and paths exactly as they were.
Passes the 50-word test.

**Structure that is noise:** restating the question; a TL;DR label above a one-paragraph answer; the
diagnosis walked through before the conclusion; proof that a plan will work; bold-label bullets for a
single argument; a heading on a reply under 300 words; a closing offer ("Want me to...", "Let me know").

**Patterns to flag:** status-report voice ("Verified. Both pass."); "the fix is X" before the problem;
"you're right to push back"; the reassurance words (cleanly, coherent, robust); method narration ("I checked
the file and then...") where the result is what matters; everything in `claudish.md` §4.

**Rewrite rules:** decision first. Prose for an argument, a short list only for parallel items the reader
will act on one by one. Keep every fact, link, path and command. If the answer was wrong or uncertain, the
rewrite says so as plainly as the original did; do not harden a hedge.

## Doc or report

A reader who may skim, jump, or read once and forward it.

**Structure that serves:** a first paragraph that passes the 50-word test and states the conclusion;
headings that say the claim or the content ("Costs rise 30% at 10k users", not "Analysis"); a table for any
comparison with three or more rows; one idea per paragraph; the recommendation or next action at the end
where a reader looks for it; an appendix for detail most readers skip.

**Structure that is noise:** an "Introduction" that announces the document; "Key takeaways" that restate
the body; a heading over every two sentences; uniform paragraph length; a "Conclusion" that recaps; "In
this document we will"; bold on every term; horizontal rules between sections; a title repeated as the
first sentence.

**Patterns to flag:** generic headings; inflated significance; stock "Challenges and future outlook"
sections; weasel attribution ("studies show") without a source; "the table below compares" (the reader can
see it).

**Rewrite rules:** keep the heading structure where it helps a reader jump; sharpen generic headings;
merge tiny sections; vary paragraph length; end on the last real point or the next action, not a recap. One
or two dashes are acceptable at this length if they clearly help. Keep a risks, decisions or options table
even when it has one row: readers look for it by shape. Keep the author or owning team in the first lines;
"who wrote this" is a fact.

## README or technical doc

A first-time visitor who wants to know, in 60 seconds: what is this, is it for me, how do I run it.

**Structure that serves:** one sentence under the title that says what it is and for whom; a before/after
or a 10-second example near the top; Install, Usage, then everything else; headings in sentence case; one
table where a comparison exists; code fences for every command, with the expected result; a short "What it
doesn't do" or "Limits" section; license at the bottom.

**Structure that is noise:** a feature wall of bold-label bullets above the install; badges that carry no
information; emoji headings; "Why X?" sections that argue with no one; marketing adjectives (powerful,
seamless, blazing); a philosophy section before anyone has run it.

**Patterns to flag:** sales language; inflated claims with no number; "comprehensive", "robust",
"production-ready" without a test or a user behind them; instructions that assume context (which directory,
which shell).

**Rewrite rules:** never touch code blocks, commands, paths, URLs or frontmatter. Order sections by what a
new visitor needs first. State what is unbuilt in plain words. Keep a standard technical term for a
technical reader; explain it once otherwise.

## PR description or commit message

A reviewer who will decide whether to read the diff, and a future engineer running `git log`.

**Structure that serves:** a subject line under 72 characters that says what changed, in the imperative
("Retry failed uploads once before erroring"); a first sentence that says why; what changed in one short
paragraph or a list of parallel items; how it was tested, as what was run and what happened ("ran the
upload suite, 42 pass; manually retried a 500 from staging"); what is out of scope or follows; a link to the
issue.

**Structure that is noise:** a "Summary" heading over one sentence; "This PR" as the subject; a bullet per
file; the diff restated in prose; a "Testing" section that says "tested thoroughly"; status-report
fragments; emoji; "Closes #12" as the only content.

**Patterns to flag:** landed, gated, surfaced, load-bearing, byte-identical, coherent, cleanly (see
`claudish.md`); "comprehensive tests" with no numbers; "refactor" covering a behavior change; a scope wider
than the subject line.

**Rewrite rules:** why, what, how tested, what's next. Numbers for tests. Name behavior changes as behavior
changes. Keep every path, command and issue number exactly, and cite the issue once. A PR longer than one
paragraph keeps short labeled sections a reviewer scans for (What changed, Why, Testing, Rollback, Not in
this PR); those labels carry information. A one-paragraph PR needs none.

## LinkedIn post

A reader scrolling, who sees two lines before "see more" and decides in a second.

**Structure that serves:** a first line that is the specific claim, story or number, not a hook that hides
it; prose in paragraphs of one to four sentences; one idea; a real detail only this writer could know; an
ending on the last concrete point or an honest open question. Under 3,000 characters. The 50-word test does
not apply; the first two lines have a different job (earn the click and pay it off).

**Structure that is noise:** one sentence per line throughout (a template, unless it is the writer's
established style); a hashtag stack; emoji bullets; "Agree?" / "Thoughts?" / "Repost if this resonates";
"Read that again."; a self-intro paragraph at the bottom; an outbound link in the body (suggest the first
comment).

**Patterns to flag:** the information-withheld hook ("At Netflix we had 1 UNSPOKEN rule."); common-belief-
then-counter ("Most people think X. They're wrong."); vulnerability performance ("I wasn't going to share
this"); the achievement formula (emotion word, announcement, team thanks, generic lesson, emoji); fake
dialogue ("CEO: ... CMO: ..."); the fake-profound kicker; stacked abstract nouns ("creativity, passion, joy").

**Rewrite rules:** rewrite a hook only from material already in the post. If there is no specific to lead
with, say so in Gaps. Keep the writer's voice first; this is the one format where personality beats plainness.
Hashtags: none, or one to three woven in. No dashes.

## Email

One recipient who wants to know what you need from them and by when.

**Structure that serves:** a subject line about the content ("Tuesday 2pm for the pricing call?"); the
ask or purpose in the first two sentences; the minimum context the recipient does not already have; one
ask, specific ("Free Tuesday at 2?" not "let me know if you want to chat sometime"); one sign-off.

**Structure that is noise:** "I hope this finds you well"; "I wanted to reach out because"; context the
recipient already knows; two asks; a PS that holds the real pitch; stacked thanks or apologies; "Please
don't hesitate to reach out."

**Patterns to flag:** corporate filler (per my last email, at your earliest convenience, circle back, loop
in, bandwidth); fake personalization ("I've been impressed by the great things your company is doing");
hedge pileups ("I was wondering if perhaps it might be possible").

**Rewrite rules:** ask first. Formality matches the relationship. Most padded emails lose half.

## Slack or DM

A channel that already has the context, and a reader on a phone.

**Structure that serves:** the ask or action item first, then one line of context; four to five sentences
at most; a thread or a doc for anything longer, with a one-line summary up top; the channel's casual
register.

**Structure that is noise:** email register (greeting, sign-off, "Please be advised"); "Just wanted to flag",
"Wanted to surface this", "Looping in X for visibility"; "Sorry to bother you, but"; three or more emoji to
soften; re-explaining what the channel knows; a heading or bold labels in a two-line message.

**Rewrite rules:** say what you need from whom. A shared link gets one sentence on why it matters, not a
summary.

## Script (podcast, video, talk)

A listener who cannot re-read. Everything is heard once, in order, at talking speed.

**Structure that serves:** spoken sentences: contractions, short clauses, one idea per breath; the point
said early and said again later in different words (repetition is how listeners hold on); signposts in
speech ("Two things. First...") instead of headings; a concrete example before the abstraction; a real
transition between segments ("That's the problem. Here's what we tried."), which is fine in speech even
though it is a tell in prose; names and numbers said in the form a mouth says them ("about forty percent",
not "~40%").

**Structure that is noise:** headings, bullets, bold, parentheses, tables, footnotes, anything only an eye
can use; sentences with embedded clauses a listener loses; "as mentioned above"; written transitions
("Furthermore"); a summary slide read aloud; the 50-word test (exempt: an opening can be a cold open, a
question or a story).

**Patterns to flag:** Claudish and generic AI vocabulary, which sound worse aloud than on the page; the
staged run-up ("Here's the thing") when it stacks; dashes meant as pauses (write the pause: a period, or
"[pause]" if the script uses directions); false agency ("the data tells us"); stat bombs (three numbers in a
row; a listener keeps one).

**Rewrite rules:** read it aloud in your head. If a sentence needs a breath mid-way, split it. Keep speaker
labels, timestamps and directions exactly. Keep the host's verbal habits and jokes; they are the voice.

## Slides or artifact text

A viewer who reads a slide in five seconds while someone talks, or scans a page in ten.

**Structure that serves:** one claim per slide or section, in the title, as a sentence ("Churn doubled
after the price change", not "Churn"); three to five words per bullet if bullets exist at all; the number
large and its unit plain; speaker notes carrying the argument in full sentences; on a page, a hero line
that passes the 50-word test and sections a scanner can land on.

**Structure that is noise:** paragraphs on slides; a bullet that is a sentence with the article removed;
title case everywhere; a "Thank you" or "Questions?" slide as content; decorative emoji; stacked
qualifiers; "Agenda" slides that list the headings the viewer is about to see.

**Rewrite rules:** titles are claims. Notes are prose. Never edit markup, component names, props, class
names or data; edit only the strings a viewer reads. Keep every number and its source.

## UI copy

A user mid-task who reads only what blocks them.

**Structure that serves:** the verb on the button ("Save draft", not "OK"); an error that says what
happened and what to do next ("Couldn't save. Check your connection and try again."); an empty state that
says what will appear here and how to start; one sentence where one will do; consistent terms (one name
per thing across the product).

**Structure that is noise:** "Oops!"; apology stacks; exclamation points; "Please"; jargon the user did not
choose ("token", "payload"); humor in an error; a paragraph where a label belongs; synonym cycling (Save,
Store, Keep for one action).

**Rewrite rules:** every word carries information. Match the product's existing vocabulary. Keep placeholder
variables and keys exactly. If the copy lives in a strings file, change values only, never keys.
