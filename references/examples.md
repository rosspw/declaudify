# Examples: before and after, every fact kept

One pair per format where the move is not obvious. Each "after" keeps every name, number, negation and
caveat from its "before" and adds nothing. Where a specific is missing, the Gap is shown rather than filled.

## Chat answer (Last answer mode)

**Before**
> You're right to push back. The honest shape here is asymmetric: reads are gated on the cache being warm,
> but writes bypass it entirely, so the inconsistency you surfaced is real. I verified both paths. The fix
> landed cleanly: writes now invalidate the relevant keys, and the read path is anchored to the invalidation
> timestamp. This is belt-and-suspenders on top of the TTL. Both snapshots are coherent. TL;DR: the cache was
> the load-bearing assumption and it's now explicit. Want me to add a regression test?

**After**
> Yes, the inconsistency is real: reads only worked when the cache was warm, and writes skipped the cache
> entirely. I've changed it so every write clears the keys it touches, and reads compare against the time of
> the last clear. The TTL still applies as a second safeguard. I checked both the read and write paths by
> hand; there is no regression test yet.

Kept: the asymmetry, the TTL as a second safeguard, the timestamp mechanism, "I verified both paths" (now
says how), the fact that no test exists. Dropped: the praise, "honest shape", "gated", "surfaced", "landed
cleanly", "anchored", "coherent", "load-bearing", the TL;DR label, the closing offer. "Cleanly" became what
was actually checked.

## PR description

**Before**
> ## Summary
> This PR introduces a robust retry mechanism for the upload pipeline, significantly improving resilience.
> ## Changes
> - **Retry logic:** Added exponential backoff to `uploader.ts`
> - **Error handling:** Enhanced error handling throughout
> - **Tests:** Comprehensive test coverage added
> ## Testing
> Thoroughly tested. All tests pass cleanly. Closes #142.

**After**
> **Retry failed uploads up to 3 times with exponential backoff**
>
> Uploads that hit a transient 5xx used to fail on the first try (#142). `uploader.ts` now retries up to
> three times, waiting 1s, 2s and 4s. Errors that are not 5xx still fail immediately.
>
> Tested: the upload suite passes (12 tests, 4 new ones cover the retry path). I also retried a forced 503
> from staging by hand and the third attempt succeeded.
>
> Not in this PR: retries for the download path.

Gaps the editor would raise if the numbers were not in the diff: how many retries, which backoff, how many
tests. The after above assumes they were in the diff; if not, they are questions, never guesses.

## LinkedIn post (light touch, voice kept)

**Before**
> I wasn't going to share this, but here's the thing.
>
> Last Tuesday I lost my best engineer.
>
> Not to a competitor. Not to burnout. To a spreadsheet.
>
> She spent 9 hours a week reconciling two systems by hand. For two years.
>
> Here's what nobody tells you: retention isn't about perks. It's about respect for people's time.
>
> Read that again.
>
> What's the spreadsheet in your company? 👇

**After**
> Last Tuesday I lost my best engineer to a spreadsheet.
>
> She spent 9 hours a week reconciling two systems by hand. For two years.
>
> I don't think retention is about perks. I think it's about whether anyone respects what eats your time.
>
> What's the spreadsheet in your company?

Gaps
- What did she say when she left, and what are you doing about the spreadsheet now? The post ends on a
  question because it has no next action; a real one would be stronger than the question.

Kept: the story, 9 hours, two years, the retention claim, the closing question (a real open question is
fine; the pointing emoji was the bait). Dropped: the vulnerability preamble, the negative listing ("Not to a
competitor. Not to burnout."), "here's what nobody tells you", "read that again". Kept the writer's
one-line-per-paragraph rhythm because it carries the story here; the touch was light. Nothing added: the
editor wanted an exit-interview detail and a next step, and asked for them instead of writing them.

## Doc opening (the 50-word test)

**Before**
> ## Introduction
> In today's rapidly evolving landscape, organizations face a myriad of challenges when it comes to
> onboarding. This document provides a comprehensive overview of our onboarding analysis, delving into the
> key metrics, surfacing actionable insights, and setting the stage for a path forward. Let's dive in.

**After**
> New hires take 23 days to ship their first change, against a target of 10. Most of the gap is waiting
> for access: 14 of the 23 days on average. This doc shows the data, the three access requests that cause
> most of the wait, and what we propose to cut it to 10 days by March.

The after assumes the numbers appear later in the doc, moved up. If they do not exist, the opening becomes
a Gap question ("what is the current time-to-first-change and the target?") and the editor leads with the
best concrete claim the doc already has.

## Script (podcast)

**Before**
> HOST: Welcome back. Today we're delving into a multifaceted topic: AI-generated writing. It's not just a
> technical issue — it's a cultural one. Here's the thing: studies show that readers can't tell the
> difference. Let that sink in. We'll unpack three key dimensions: detection, style, and trust.

**After**
> HOST: Welcome back. Today: writing that AI wrote, and why you can't tell any more. There's a study we'll
> get to where people guessed right about as often as a coin flip. So this isn't a tech problem, it's a
> trust problem. Two things today. How people try to detect it. And what it does to how we read each other.

Kept: the topic, the claim that readers can't tell (now says "a study we'll get to", with a Gap to name it),
the shift from technical to cultural. Changed: three dimensions became two because the before only develops
two; "detection, style, trust" was a forced triad. Spoken rhythm: short clauses, "So", a repeated frame.
Gap: which study?

## README opening

**Before**
> # Syncly 🚀
> **Syncly** is a powerful, seamless, next-generation synchronization engine that leverages cutting-edge
> conflict resolution to empower teams. ✨
> ## Features
> - **Blazing fast:** Optimized performance
> - **Robust:** Battle-tested reliability
> - **Flexible:** Works with any backend

**After**
> # Syncly
> Keeps two folders in sync across machines and resolves edit conflicts without asking you. For people who
> work from more than one computer and don't want a cloud account.
>
> ## Install
> ```
> npm install -g syncly
> ```

Kept: the name, the sync-and-conflict claim. Dropped: every adjective that had no number or test behind it,
the emoji, the feature wall. Gaps the editor would raise: how fast, tested how, which backends. The "for
people who" line is a Gap too unless the README says who it is for; shown here as what the shape looks like
when the answer exists.
