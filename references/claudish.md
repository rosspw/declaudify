# Claudish: the dictionary and how to translate it

Claudish is the compressed dialect of coding agents: engineering metaphors borrowed from many subcultures,
combined at a density no single person uses, in short statements about complicated relationships. Each
term is real somewhere. The tell is the frequency, the combination, and the compression. (Named in a
Waterloo Q&A with Yuntian Deng, Sep 2026; his dictionary at programasweights.com/claudish/dictionary is the
seed of this one. Additions from the "load-bearing" analysis of 47k GitHub PRs and its Hacker News thread.)

## Contents

1. How to translate
2. The dictionary
3. Combining rules
4. Habits beyond words
5. When to keep a term

---

## 1. How to translate

- **Say who did what.** Most Claudish hides the actor: "the probe surfaced a mismatch" has no person in it.
  Plain English puts one back: "the check found that the settings don't match."
- **Replace the metaphor with the mechanism.** "Load-bearing invariant" → "this only works if X stays the
  same." Translate what it means in *this* sentence, not the general concept.
- **Reassurance words need evidence.** "Landed cleanly", "both snapshots are coherent", "robust": either name
  the check that was run or delete the word. If you cannot tell what was checked, cut it and write a Gap.
- **Nouns back to verbs.** "The merge is owner-gated" → "only owners can merge." "Rollback has a cleanup
  dependency" → "you can only roll back before cleanup runs."
- **One term, one translation, in context.** The dictionary gives the usual meaning; the sentence decides.

## 2. The dictionary

| Claudish | Plain English | Note |
|---|---|---|
| gated on / X-gated / owner-gated / quality-gated | blocked until X; only X can do it | "Deployment is gated on CI" → "We can't deploy until the checks pass" |
| land / landed / landing | merged | Merged is not deployed. Say which |
| surface / surfaced | find, show, reveal | Always add who found it and how |
| provenance / lineage | where it came from | |
| the honest shape / one honest caveat / honest take | the real situation; one limitation | "Honest" adds nothing. Cut it and state the limitation |
| load-bearing (assumption, invariant, distinction) | everything depends on it; this only works if | The single most Claude-specific word (39x more frequent in Claude PRs) |
| belt-and-suspenders / belt-and-braces | a second safeguard in case the first fails | |
| cadence | how often; every day, every week | |
| canonical / source of truth / authoritative | the official one; the copy everyone should use | |
| thread / wire / plumb through / wired end to end | pass it to every part that needs it | |
| durable path forward / durable | a fix meant to last; long-term | Say how long or what would break it, or cut |
| shape / response shape / shape of the problem / X-shaped | format; kind; looks like X but may not be X | |
| hard gate / hard stop / hard boundary / hard constraint | strictly enforced; must stop; must not cross | |
| coherent / coherence | consistent | A loose reassurance unless the check is named |
| cleanly / clean | without errors | Name the check or cut |
| seam | where two parts connect | |
| substrate | the system underneath | Name it: the database, the log |
| drift / drifted / schema drift | stopped matching over time | |
| blast radius | what else breaks if this fails | |
| fail closed / fails closed | block when the check fails or can't answer | Standard security term; keep for security readers |
| spine | the central structure that organizes the rest | |
| boundary / trust boundary / ownership boundary | the line between two parts' responsibilities | |
| wedged / wedge | stuck; makes something else stuck | |
| contract / preserve the contract | the behavior other code relies on; don't break what callers expect | |
| anchored / anchor | compared against a fixed point | |
| that's not nothing | a small real win; it helps but doesn't solve it | |
| byte-identical / byte-for-byte | exactly the same | "The biggest claudism" per one HN reader |
| you're right to push back / You are absolutely right | you're right | Cut the ceremony |
| freeze the binding / frozen | stop it changing | |
| non-trivial | hard; big; real | Say which |
| orthogonal | unrelated; independent | |
| first-class (citizen) | fully supported; built in | |
| idempotent | safe to run twice | Keep for engineers; explain once for others |
| hermetic | self-contained; no outside dependencies | |
| sidecar | a helper that runs alongside | |
| spike | a quick throwaway experiment | |
| footgun | an easy way to hurt yourself | |
| long pole | the slowest part; what everything waits on | |
| smoking gun | the proof | |
| greenfield | new, from scratch | |
| the crux | the hard part; the real question | |
| earns its keep | is worth having | |
| add color | add detail; explain | |
| vacuous / vacuously true | empty; true for no reason | |
| latch / latched | stays set once triggered | |
| carries (for contains) | contains; holds | |
| verdict (for result) | result; answer | |
| names (as a verb: "the error names the file") | says; identifies | |
| surgical | small and precise | Usually just "small" |
| that said | but | |
| quietly / plainly / genuinely / outright | (cut) | Intensifiers with no content |
| shipped / ship | released; done | Fine for builders; say what was released |
| TL;DR | (cut the label) | Lead with the point instead of labeling it |

## 3. Combining rules

**X-shaped.** Looks or behaves like X but may not be X: "credential-shaped" → "looks like a credential but
may not be valid"; "report-shaped" → "organized like a report".

**Metaphor stacking.** Several metaphors in one phrase: "the load-bearing spine" → "the central part
everything depends on". Translate each, then combine.

**Not X, but Y / X, not Y.** Ruling X out: "This isn't a cache problem; it's an ownership problem" → "The
ownership rules caused this, not the cache." Keep both halves only when the correction is one the reader
actually holds. Otherwise state Y.

**X-gated, X-bound, X-anchored, X-scoped.** Compound adjectives from a noun plus a mechanism word. Unpack:
"approval-gated" → "needs approval first"; "request-scoped" → "lasts for one request".

## 4. Habits beyond words

These are structural and survive a word-by-word pass. Fix them in move 2.

| Habit | What it looks like | Fix |
|---|---|---|
| Status-report voice | "Verified. Both pass. The fix is in." Clipped fragments reporting state | Full sentences with an actor: "I ran both tests and they pass" |
| The fix before the problem | "The fix is X" before saying what was wrong | Problem, then fix, in one or two sentences |
| TL;DR longer than the answer | A labeled summary, then the same content again | One opening paragraph that passes the 50-word test; no label |
| Bold-label bullets as paragraphs | `- **Cause:** ...` `- **Fix:** ...` for what is one argument | Prose, unless the labels carry information a skimmer needs |
| A heading over every two sentences | Five `##` for 200 words | One heading per section a reader jumps to |
| Arrow chains | `A → B → C` for causation | A sentence: "A causes B, which means C" |
| Nouning | "the merge is owner-gated", "has a cleanup dependency" | A verb: "only owners can merge" |
| Stacked parentheticals | Three asides mid-sentence (each qualifying) (the last) | One, or a new sentence |
| The answer in the last line | Diagnosis, evidence, proof, then the decision | Decision first; keep only the reasoning that would change the reader's mind |
| "It <verb>s no <noun>" | "It takes no arguments and makes no network calls" as a rhythm | Fine once; a row of them is a tell |
| Two abrupt sentences | "One brief sentence. Second abrupt sentence." as a closing beat | Join them or cut one |
| Three numbered revelations with a kicker each | 1. ... *That's the point.* 2. ... | Numbers only for sequences; cut the kickers |
| Colons as the new dash | "The result: it works." "The catch: it's slow." | A plain sentence |
| Horror vacui | Every clause carries a qualifier; the paragraph is too dense to parse | Fewer claims per sentence; one idea each |
| Explaining shared context | Restating the user's question and the history before answering | Cut; the reader has it |
| Writing about the document | "The table below compares", "this section is organized by", "generated from" | Describe the subject, not the document |

## 5. When to keep a term

Keep a Claudish or technical word when all three hold: it is the standard word for the reader (an engineer
reading a PR: idempotent, race condition, rebase, schema, fail closed); a plain substitute would be longer or
less exact; and it appears once or twice, not as a texture. Otherwise translate it, or keep it and explain it
once in plain words on first use: "the write is idempotent (safe to run twice)".

A quotation, a proper noun, a command, a file name and a passage that discusses the word rather than uses
it are never translated.

**Gloss, don't rewrite,** when the user asks to understand a text rather than to replace it (Audit mode, or
"what does this mean"): leave the sentence and add the plain meaning in brackets after each term. "The merge
is owner-gated [only owners can merge]; it landed cleanly [it was merged; which checks ran is not stated]."
