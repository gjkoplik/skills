---
name: what-if
description: 'Take a cheap look at a half-formed idea before committing to a conversation about it. Ask what it would mean to add some capability, library, pattern, or technique, and get back a short calibrated report: what it is in terms you already know, the surface it would land on in this repo, the API and structural implications, what would be hard to undo, the options from smallest to largest with what each one buys, costs and forecloses, and the case for and against at equal length. Deliberately brief, with everything past the first screen behind expandable sections. Use when someone says "should we use X", "what would it take to add X", "I keep hearing about X, is it worth it here", or floats an idea they are not yet committed to. Never implements, never produces a plan, and a "not worth it" is a successful run.'
disable-model-invocation: true
---

# What If

A sunk-cost circuit breaker. Someone throws a half-formed idea at you and wants enough to decide whether it deserves a real conversation, before the conversation itself makes them feel committed.

**Cheap is the point.** Not a research run with a small budget: the cheap version is the only version. Anything that would make someone hesitate before firing this at a shower thought is a bug, however much rigor it buys. If a phase does not survive that test, cut it.

## The two rules

**Do not implement.** No production code, no dependency added, no config changed. A throwaway probe in `/tmp/what-if/<slug>/` is allowed and often the best thing you can do with ten minutes; delete it after and report what it showed, including when it showed the idea does not work.

**Do not produce a plan.** No workstreams, no handoff, no pre-filled brief. A plan is the sunk cost in another form, and it prejudges the decision this exists to keep open. The report ends with the call and stops. What happens next is the reader's: ask follow-up questions, go try the thing, start planning for real, or drop it.

## How much to say

**One hard cap, and it is on the decision surface only.**

- **The top level: under 550 words.** Top level means everything visible before the reader opens a single disclosure, summaries included. That is what someone reads while deciding whether to keep reading, and it never grows. A number here because this is exactly where the pull toward completeness does its damage, and "be brief" loses to that pull every time.

**Everywhere else, length is a relevance judgment, not a budget.** Some things genuinely take a lot of explaining, and a word cap cannot tell padding from the paragraph that finally makes something click. So the test is necessity:

- **If the reader could not make the call without it, it is not a disclosure.** Promote it. Disclosures hold support, not load.
- **If it changes nothing they would do, delete it.** Not collapse it. Collapsed padding is still padding, and it still cost you the reader's time deciding whether to open it.
- **If it changes what they would do only in some cases, disclose it, and say which cases in the summary.** A summary that names what it lets you decide is how a reader chooses by need instead of by curiosity.

Two failure modes, and only the first has a number attached:

- **Long** is a fat top level. The cap catches it.
- **Thin** is worse and has no number: conclusions with the reasons left out. It reads as brevity and it is actually confident hand-waving. Nothing will flag this for you. The check is to reread each claim in the open and ask where a reader who cannot see the code would learn *why*. If the answer is nowhere, that is the work you skipped.

A block under about 40 words is usually not a block. Either it belongs in the sentence above it, or it is a claim you owe more on.

## 1. Calibrate

Two questions, one at a time, each with your recommended answer attached so the reader confirms rather than composes. Never ask what you could find out yourself.

1. **Which exact thing?** Name it at a version. Adoption questions die on ambiguity here more than anywhere.
2. **What next to it do you already know well?** The nearest neighbor, not a self-rated expertise score. People are bad at rating themselves and good at naming what they use. This becomes the spine of every explainer: "it is X but Y."

**The answers set what opens by default.** This is the load-bearing part. Something adjacent to what they know stays collapsed as a one-line reminder. Something genuinely new opens with a short explainer. Same document, different shape per reader, calibration visible in the layout instead of buried in word choice. If six explainers open by default, they are further from this subject than the idea assumed, and that belongs at the top of the report.

## 2. Look

One pass, one context. Three things:

**What it is.** At a stated version, on a stated date. This is where a report like this goes confidently wrong, because the reader asked precisely because they cannot check you. Cite what matters, stamp the version, and search once for the case against rather than only for how to use it.

**What it would touch here.** Grep the repo. Real paths, real symbols, counted rather than described. This is the section no blog post can give them, so it is where the run earns itself. Cover the surface it lands on, the API and default changes, anything needing a deprecation, and what is hard to undo.

**What this repo already decided.** Unfamiliar to the reader does not mean new to the repo. Check the git log and any decision records for an earlier attempt, a dependency deliberately dropped, or a written ruling against it. If a decision record already ruled it out, say so out loud rather than quietly proposing what was declined.

## 3. What you could do

**Almost nothing is one decision.** "Should we adopt X" is usually three or four different projects wearing one name, and the reader cannot tell them apart yet. That is most of what they are asking you for, and a single verdict throws it away.

Lay out the options, smallest first, usually two to four. Give each a plain name and use the name, not a number, everywhere else in the report. For each:

- **What it buys**, in terms of the thing they wanted.
- **What it costs**, as the specific work, not a duration. You will be wrong about durations.
- **What it forecloses.** The level that is hard to reverse is the one worth naming as such.

Options are cumulative where they genuinely are and independent where they are not, and saying which is often the finding. The most useful thing this section produces is usually the discovery that the cheap level captures most of the value, or that two levels people talk about as one have nothing to do with each other.

This is also where scope questions go to die honestly. If the reader has an appetite in mind, they can hold it against the ladder themselves, which is better than you guessing at it up front.

## 4. Weigh

The case for and the case against, **at equal length**. One context writes both, which is the cost of cheap, so symmetry is the substitute for independence: a weak side cannot be padded and a strong one cannot be truncated. Both must name a concrete fact, not an adjective. "Faster" without a number is not an argument, and neither is "more surface to maintain" without saying what surface.

**A fact on its own is not a reason.** "bokeh already uses narwhals" is a fact; why that changes anything here is the reason, and the reason is the part the reader cannot supply. Each item gets its fact and then the sentence that says what follows from it. Items that fit on one line are usually facts with the reason left off.

Then name what the two actually disagree about. It is usually one empirical question, and saying what would settle it is worth more than either case.

Watch your own thumb on the scale, in both directions. Effort already spent pulls toward yes. Imagining the thing already failed pulls toward no. Before landing on a flat "not worth it," check once whether the honest answer is "not yet" with a trigger.

## 5. Call

One line, plus one sentence of why:

- **Worth doing.** Naming which option, by name.
- **Not worth doing.** With the reason that is carrying the weight.
- **Not yet.** With the trigger that would change the answer. Without a trigger this is a "no" that gets re-researched from scratch in six months.
- **Worth doing smaller.** The fraction that captures most of the value, when there is one.

Then the cheapest thing that would settle it. Often that is "spend an hour with it," and when it is, say so and let the report be short. A "not worth doing" is a successful run.

## Output

**The order is context, options, trade-offs, surface.** In full:

1. **The call.** Self-contained. Never reference a section below it, and never name an option by a number the reader has not met yet. Someone who reads only this box should get an answer, not a pointer.
2. **What it is.** The subject, anchored to what they already know.
3. **What you could do.** The options, smallest first.
4. **Trade-offs.** For and against, on whichever option is actually in question.
5. **What it would touch here.** The repo surface, which is now serving a choice the reader has already seen rather than arriving before there is anything to attach it to.

Evidence goes next to the decision it informs, not in an evidence section. A probe result that kills one option belongs under that option, not three sections away.

A self-contained HTML file plus a markdown twin of the same content. The HTML is what gets read; the markdown is what version controls, since HTML does not diff and does not render on a repo host. Build the HTML from `${CLAUDE_SKILL_DIR}/assets/report-template.html`, which carries the disclosure mechanics, the expand and collapse controls, and both themes.

**Do not write the twin by hand.** Generate it:

```
python ${CLAUDE_SKILL_DIR}/assets/html-to-markdown-twin.py <report>.html <report>.md
```

Written twice, the two versions drift the moment you revise one, and the markdown is the copy that ends up in review. Generated, they cannot.

**Assume nothing about the reader's viewer.** Some strip JavaScript. `<details>` is native HTML and survives that; the expand and collapse controls do not, so the template injects them from script rather than putting dead buttons in the markup. For the same reason the word counts are printed to the console while you draft and **pasted into the footer as static text** before you finish.

Write both to **`<repo>/what-if/YYYY-MM-DD-<slug>.html`** and `.md`, where `<repo>` is `git rev-parse --show-toplevel` from the working directory, or the working directory itself if that is not a git repo. Root rather than `docs/`, because a docs directory is usually an input to a build and this is not documentation. Visible rather than dotted, because the point is that the reader sees it and decides.

**Do not stage or commit them.** Print both paths and let the reader decide whether this idea is worth keeping; that choice is itself part of the triage.

The subject may live in a different repo than the conversation. Ask which one before writing if it is not obvious, and read the surface from that repo, not this one.

## Honesty is a formatting job

The reader cannot check you, so mark the exceptions rather than everything. Default voice is your read. Two things get marked: **ran** for anything observed in the probe, and **sourced** for a cited, version-stamped claim. Marking every sentence is noise; marking the two that outrank your judgment is signal.

Never present unexecuted code as a working example. Mark it unrun.

Diagrams of structure are welcome and grounded: where the new thing meets the old, the blast radius as real paths, a before and after call site. Scores are not. A feasibility gauge or risk heatmap built from your own adjectives launders a guess into a graphic. The test is one line: name the measurement.
