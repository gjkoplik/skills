---
name: agent-viz-wiki
description: Conventions for maintaining the agent-viz research wiki under wiki/ — the page schema and status labels, the evidence-class discipline (evidence-backed / authority-asserted / contested / absence of evidence, plus the definitional exemption), the two-tier chart-type structure with flat storage and index pages, the source-extraction rules that exist because specific tooling failures produced confidently wrong output, and the house prose style. Load whenever adding or editing anything under wiki/, adding a source or study page, adding a chart-type page, or running the weekly sweep routine.
---

# Maintaining the agent-viz wiki

The wiki under `wiki/` is the research behind the figure quality bar. Its value is not that it collects claims; it is that **every claim carries the kind of warrant it actually has.** Roughly a third of the received wisdom this project checked did not survive contact with its primary source. Adding a page that launders a convention into a finding does more damage than leaving the topic uncovered.

Read [wiki/README.md](../../../plugins/agent-viz/wiki/README.md) for the current state before editing. It is the index and it carries the live page counts.

## The page schema

**Facts live in frontmatter. Argument lives in the body.** Never both.

```yaml
---
type: source | study | person | concept | chart-type | index
status: primary-read | secondary-only | not-reached   # research pages only
status_partial: true            # coverage is not uniform across the page's material
retrieved: YYYY-MM-DD
author: <people-page slug>      # where a source has a known author
relationships: [part-to-whole]  # chart-type pages only
aliases: [Pie chart, Donut chart]  # chart-type pages only; must agree with chart-types/aliases.md
---
```

Run **`validate.py`** in this skill's directory before finishing, **from the repo root**. It checks frontmatter, the README's asserted counts, page-versus-index agreement, the eight required chart-type sections, alias agreement in both directions, links and anchors, and that nothing links outside the plugin directory (which would break on install). It also reports gaps, which are open items rather than failures.

**Run it as `python3 .claude/skills/agent-viz-wiki/validate.py` from `/home/garyk/repos/skills` and nowhere else.** From another directory the relative path does not resolve, and piped through `grep` it prints nothing at all, which reads exactly like a clean run. That has now happened three times.

**`aliases:` is a name index in two places that must agree.** Every chart-type page lists the names it answers to, and [wiki/chart-types/aliases.md](../../../plugins/agent-viz/wiki/chart-types/aliases.md) maps each name to its page with the provenance of the mapping. `validate.py` checks both directions. A row whose target cell begins "No page" is a **pointer to a different form**, not an alias, and is excluded from the check; that is how a name like "sina plot" can be discussed on a page without being claimed as one of its names. One name per row: a Name cell holding two comma-separated names cannot round-trip.

**Body, by page type:**

- **Source, study, person:** keep *what it is good for* (the question to come back with), *what it does not settle*, and a **"How this was read"** paragraph. Drop the rest; the title carries "what it is" and frontmatter carries the status label.

  **"How this was read" is not the old status line with a new name, and it must not be deleted as a duplicate.** Frontmatter carries the *label*; this paragraph carries the *provenance*, which is the wiki's entire trust story: which artifact was opened, how it was extracted, what was rendered to images because it had no text layer, what was left unopened, and which parts of a split status apply to which material. Losing it would make every `primary-read` unauditable.

- **Never state a bare rank number on a page a reader uses to choose a chart.** Name the channel. "Position instead of area" is what a chooser needs; "rank 1 instead of rank 4" adds nothing and silently depends on which of the two Cleveland & McGill tables you meant, which disagree from area downward.
- **Chart-type and index:** no header block at all. One line of definition under the title, then straight to the decision.

**Status is load-bearing, not decoration.** `primary-read` means someone opened the actual source and quotes come from a local extraction. `secondary-only` means abstracts or summaries, and its quotes are unvouched. Do not upgrade a status because a summary was detailed or confident. Where a page covers several artifacts reached unequally, set `status` to the **principal** subject and `status_partial: true`, and say in the body which parts are which.

**Authorship is not optional bookkeeping.** Independence is this wiki's most-used argument ("three unrelated organizations", "a fourth independent source"), and it once counted the Urban Institute style guide and Jonathan Schwabish as two voices when he is behind both. **Independence is a claim that needs support; the absence of a byline is not support for it.** Record `author` whenever it is known, and before adding a source to a corroboration count, check who wrote it.

**Pages under `wiki/people/` use a variant of the same schema**, with "What they are known for", "What they are good for", and "What they do not settle". A person page is not a biography and not a summary of their views. Its job is what coming to this person actually buys you, and where their authority stops. `wiki/sources/` covers a specific work or style guide; `wiki/people/` covers the person across their work. A prolific author can have both.

**Links are ordinary markdown relative paths, not Obsidian wikilinks.** A link to a page that does not exist yet is a broken link, not a placeholder. If you want to name a page that should exist, name it in prose without linking it.

## Evidence class, on every claim

- **Evidence-backed.** A study, experiment or published standard. Cite the source and the number. State it flatly.
- **Authority-asserted.** A practitioner or design book asserting it without an experiment. Perfectly usable. State it as a default with the status visible.
- **Contested.** The record disagrees with itself. State the rule, then the contest, then what survives.
- **Absence of evidence.** Nobody has tested it. **Not the same as contested, and not the same as refuted.** State the caution and its reason, not a prohibition.
- **Definitional.** Describes what something *is* and asserts nothing empirical. **Carries no label**, because labeling it would dilute the labels on real claims. Structural decompositions are the standard case.

**The rule that makes this operational:** do not upgrade a convention into a finding when quoting the wiki. The label has to survive the quotation, so it belongs in the sentence rather than in a footnote.

**Watch for *therefore*.** The characteristic failure is running a secure definitional statement into an empirical conclusion in one sentence. "A hive plot puts node position on a real data scale" is definitional and secure. "Therefore readers read it more accurately" has no study behind it.

Full treatment in [wiki/concepts/evidence-class.md](../../../plugins/agent-viz/wiki/concepts/evidence-class.md).

## Chart types: written for someone making a choice

**The reader is standing in front of a dataset and has to pick a form and defend the pick.** Every section earns its place by helping with that, or it comes out. Three rules follow, and the first two are where the first draft of this tier went wrong badly enough to need rewriting:

- **Lead with the choice, not the anatomy.** The first substantive section asks whether this group or form is even the right frame for the reader's question. The most common failure is not picking the wrong chart within a group, it is being in the wrong group: composition charts get reached for when the question is ranking, network diagrams get drawn when the question is answerable from a per-node table. Structure, channels and evidence come after.
- **No process narration.** Which page was written first, what is a "shape-setter", what remains uncovered, how the research went: none of it helps anyone choose a chart. Coverage and status live in `wiki/chart-types/README.md` and in `wiki/README.md`. Keep them off pages that exist to support a decision.
- **Give the reader the sentences.** Pages carry a "justifying the choice" section: what is defensible and evidence-backed, what is defensible with the label said out loud, and what is commonly repeated and unsupported. The refutations are the project's most valuable output and they are wasted if they only appear in `refutations.md`.

## Page templates

**Source, study and person pages** carry the four-field header block: what it is good for, what it does not settle, and the "How this was read" provenance paragraph, under the frontmatter.

**Concept pages** keep that block *and* add **What it is**, because a concept's slug does not convey it (`floor-and-ceiling` needs a sentence in a way `wilke-fundamentals` does not). Their `status` describes how the idea was arrived at, usually synthesis by this project, so it stays prose in the body and takes no frontmatter label. **The existing concept pages are correct as they stand; do not "fix" them to match the research pages.**

**Directory READMEs take no frontmatter**, and a navigation stub takes no header block. A README that is really the design document for its tier may keep *what it is good for* and *what it does not settle*, but never a `Status` field: coverage belongs in a coverage table where it can be checked, not in prose that drifts.

**Chart-type and index pages carry no header block at all.** That block answers "should I open this page?", and this reader has already arrived with data in front of them. One line of definition under the title, then straight to the decision.

**Index pages** (one per relationship) carry: is this group the right frame, and how to tell; what the group costs, in channel terms; how to choose a form within it; how to justify the choice; the failure mode the group invites; the types it indexes.

**Type pages** carry these eight `##` sections, in this order, spelled exactly as `validate.py` checks for them:

1. **When to reach for it, and when not.** The conditions under which the form is the right answer, and the nearest alternative when it is not. A table of "the reader's actual question → the alternative" is the usual shape.
2. **Structural decomposition.** The six slots below.
3. **Channels.** Which perceptual channel the mark puts the reader on, primary and secondary, linking to `concepts/channels.md`. Flagged as conjecture unless a study decomposed this specific type.
4. **What it is measurably good at.** Only claims traceable to a study. Cited, with the effect.
5. **What it is measurably bad at.** Same bar.
6. **What is contested.** Where the record disagrees with itself, both sides named.
7. **The failure mode it invites.** What goes wrong in practice. Usually `authority-asserted`, and labeled as such.
8. **Justifying the choice.** The defensible sentences, and the commonly repeated ones the evidence does not support.

The six slots, borrowed from Wilkinson's *Grammar of Graphics* by way of ggplot2's layered restatement:

| Slot | The question |
|---|---|
| Data | What is one row |
| Transform | What statistic is computed before drawing, if any |
| Geometry | What mark is drawn |
| Scale | How values map to the mark's properties |
| Coordinates | What space the mark is placed in |
| Guides | What axes, legends and reference marks are required to read it |

**These slots carry no evidence label.** They are definitional: they describe what the chart *is* and assert nothing empirical. Labeling them would dilute the labels on rows that are actually claims.

The decomposition earns its place by collapsing near-duplicates. A coxcomb is a bar chart with polar coordinates. An area chart is a line chart with a fill. Stacked and grouped bars differ in one transform slot. Without it, the tier becomes sixty pages holding ten pages of content.

## Chart types: flat storage, index pages

Type pages live **flat** in `wiki/chart-types/`. Grouping happens in index pages that point at them.

A data relationship is a **view** of a chart, not a property of it: a stacked bar is part-to-whole and magnitude and change-over-time. A directory tree would force one home and demote the rest. Flat storage also means the FT's nine relationships are never amended, only indexed alongside indexes of our own.

- Every type page declares its own `**Relationships.**` line in the header, so an index is checkable against the pages rather than maintained by hand.
- Every type page carries the six-slot structural decomposition (data, transform, geometry, scale, coordinates, guides). Those slots are definitional and carry no evidence label.
- **The inheritance rule: evidence attaches to channels, not to chart types.** No controlled study has tested a chart type as an artifact in the world; they test stripped judgment tasks on stimuli that resemble one. Every accuracy claim on a type page is therefore a two-step inference whose first step (this chart puts the reader on that channel) is conjecture in the source literature, flagged as such by Cleveland and McGill every time they make it. A type page may **inherit** an accuracy claim from [wiki/concepts/channels.md](../../../plugins/agent-viz/wiki/concepts/channels.md) with a link. It may not **restate** it as a native finding, and it may not present the mapping as settled when the source calls it a conjecture. Where a study *has* decomposed a specific type, that is a genuine type-level finding and belongs on the page; `pie-and-donut.md` is the model case and currently the only one.
- **The reader is someone standing in front of a dataset who has to pick a form and defend the pick.** Usually an agent, sometimes a person. Every section on every page earns its place by helping with that, or it comes out.
- **Taxonomy is an index, not a home, and that has consequences for editing.** Nobody's taxonomy gets amended: the FT's nine stay as published and this wiki's own indexes sit alongside them rather than inside. Paths stay stable, so reclassifying a type is an edit to an index rather than a file move that breaks inbound links. And a bespoke form that fits no relationship still gets a page; it just appears in fewer indexes, which is information rather than a filing problem.

## Source-extraction rules, each written in blood

These exist because a specific failure produced confidently wrong output that nearly shipped.

- **Never quote from a fetch summary.** A summarizer once returned, inside quotation marks, the reverse of a paper's stated conclusion. Download and extract locally, then quote from the extraction.
- **Verify the identity of what you downloaded.** Print the first lines of the extraction and confirm the title matches before using it. A plausible-looking arXiv URL once yielded an entirely unrelated paper.
- **Check for a local copy before recording a source as `not-reached`.** A paywalled paper with no open-access deposit was written up as unreachable while a local PDF existed the whole time. Search the filesystem, including sibling repos, before concluding.
- **A scanned PDF with no text layer is still readable.** Render the pages to images and read them. That is a stronger primary read than OCR. Decrypt or re-render if a reader refuses the file.
- **PDF text layers misattribute table values.** Interleaved metric blocks and vertically centered cells both slide labels onto the wrong rows. Cross-check any table against the prose, or use an HTML rendering.
- **Text layers silently drop characters**, including comparison operators and `±`, which is the difference between a bound and its negation.

## The wiki records facts. It does not give advice.

**This is the rule that gets violated most, and it is the reason for most rewrites.** The wiki is a vault of findings and the links between them, built so an agent can navigate it fast. That agent forms opinions, weighs trade-offs and makes recommendations to its user. **The wiki does none of those things.** It says what was measured, by whom, with what limits, and it stops.

The worked example: a wiki page never says "don't use pie charts." It says what the studies found, which is that pies are not as bad as the received wisdom claims. The advice is downstream and belongs to the consumer.

Three mechanical tests, applied to every sentence:

- **No second person and no imperatives.** "Label the volumes", "read the size of that", "cite it to 2.1 or later", "reach for it when", "say that the gap is small or you are overstating it" are all advice. The factual forms are "the volumes are unlabeled on this chart", "the effect size is 0.001", "the criterion entered in WCAG 2.1".
- **No exhortation or scolding.** "worth carrying forward", "that is the number to design against", "read strictly it says X, read loosely it gets cited as Y", "anyone quoting this is off by 7x". State the finding and the discrepancy; the reader draws the conclusion.
- **Delete the bolded lead-in. If no fact is lost, it was advertising.** A lead-in is the claim itself, or a label that names *which* thing follows. The superlative frame is banned outright: "the sharpest statement of this is X", "the limit that matters most", "the interesting direction". Say the thing.

  **A label has to name the thing, not its category.** "**Density.**" and "**The zero baseline.**" identify what the paragraph is about. "**The trap.**", "**Caveat.**", "**The facts.**" and "**Note.**" announce that a thing of some kind is coming, which the next clause was going to say anyway. The one exception is a **repeated field**: where every comparable page carries the same label in the same position, it is functioning as a column name and earns its place. `roll-call.md`'s per-source "**Caveat.**" and the "**The tell.**" line on every person page are fields. A single "**The trap:**" in running prose is an announcement, and it goes.

**Worked examples, all of them real and all written after the rule above existed.** The abstract test does not stop this on its own, so match against these shapes:

| Written | Why it fails | Fixed |
|---|---|---|
| "**The sharpest statement of this limit is a position paper, and it names the missing evidence.** Bertini, Correll & Franconeri argue against the assumption that…" | Ranks the source, promises what follows, then the next sentence delivers all of it. Every fact in the lead-in is restated immediately. | Delete the lead-in. Open on "Bertini, Correll & Franconeri argue…" |
| "Status: measured, and **much smaller than the sentence sounds**." | A remark about how a sentence reads, in a field whose job is the evidence's status. | "Status: supported, at effect sizes of 0.02 and 0.001 against the paper's own 0.01 threshold for small." |
| "This is **the newest claim on the page and the only one here** that is genuinely supported by its primary." | The wiki narrating its own page composition. A reader wants the claim, not its position in the file. | "The primary supports the claim." |
| "…[Okoe et al. (2018)](x.md), **a few entries above**." | Page-layout narration. The link already does this, and it survives reordering. | Delete the clause. |
| "**Both halves are load-bearing.**" / "the FT gloss is ten words" | Admiring a quote instead of spending it, and "load-bearing" worn as a hard hat. Keep that term for its literal sense: an element the thing breaks without, like a shared scale or a channel nothing else duplicates. | Say what the second clause *means*. |
| "**The entry exists because** the abstract invites an overstatement…" | Explaining why the entry is here rather than saying the thing. | "What the abstract does not carry is the size of it." |

**Sections whose names sound like advice still hold facts.** "When to reach for it, and when not" is the conditions under which the form is defined to work and the evidence for them. "Justifying the choice" is what the evidence supports, what it does not, and what is commonly claimed without support. Both are statements about the record, phrased in the third person.

## The wiki changelog

**Release cadence does not apply here.** The wiki changelog is calendar dated by the work that produced the entry, so a sweep writes its own `## vYYYY.MM.DD` heading on the day it runs. Nothing installs against a wiki date and no version pins to it; the plugin's own changelog is where releases live. Do not wait for a release, and do not park work under `## Unreleased`.

Open the entry with one line naming what produced it, for example "The results of a dream run: the weekly research sweep, plus a corpus-wide pass converting the wiki from advice-voice to record-voice."

**Entries are one line each, and they are short.** The changelog answers *what does the wiki now know* at a glance. It is not a place to restate the finding: the page holds that, and the entry links to it. A reader who wants the numbers clicks through.

- Good: "Flow group has its first experiment: [gutwin-2023-chord-vs-sankey.md](...). Sankey beat chord on time, errors and preference; effects are small and wear off with familiarity."
- Bad: the same thing across four sentences with the effect sizes, the sample, the retrieval story and a cross-reference to another study's pattern.

Group under **Added**, **Changed** and **Corrected**. If a section has nothing in it, omit the heading.

## No self-referential counts

**A page never counts the wiki.** "40 type pages, 12 indexes", "43 of the 103 names it resolves", "31 of the 40 report no study", "resolves 107 chart names". These are maintenance burden with no reader value: they rot on every edit, and nobody navigating the corpus needs a total. Describe coverage in words ("most type pages report no study in this corpus") or not at all.

**Never narrate the bookkeeping either.** "An earlier version of this line said 31 of 40 while the table held 27" is the wiki talking about its own edit history at a reader who came for a fact. Corrections to *claims* are recorded, in `refutations.md` and the changelog. Corrections to counts are not corrections, they are cleanup, and they leave no trace.

The one exception is the `Current state:` line in `wiki/README.md`, which exists because `validate.py` parses and enforces it. A count with a machine behind it cannot rot silently. No other count gets that protection, so no other count is written down.

## House prose style

- **No em-dashes in your own sentences.** Use commas, parentheses, semicolons, or shorter sentences. The one exception is a verbatim quote, which stays verbatim. The ` — ` separator in see-also list glosses is established convention here and is fine.
- American spelling. Direct, slightly informal, no throat-clearing.
- No AI filler: "delve", "moreover", "furthermore", "it's worth noting that", "in essence".
- **Do not admire a quote. Spend it.** The characteristic tic is talking *about* a quote instead of using it:
  counting its words ("the FT gloss is ten words"), or declaring that every part of it matters ("both halves are
  load-bearing"). Give the rule, the quote and the reason, and let the reader judge the phrasing. If a second clause
  is easy to miss, say what that clause *means*, which is the useful version of the same observation.

  **This is not a ban on assessing a source.** A source or person page's *what it is good for* and *what it does not
  settle* sections exist to do exactly that, and "the per-chart glosses are unusually sharp" is the job being done.
  The tic is praising the wording of a quote you are in the middle of citing, on a page whose job is a chart decision.
- **Keep "load-bearing" for its literal sense**, an element the thing breaks without: a shared scale, a channel no
  other channel duplicates. It is a real term here and it appears in [wiki/inventory.md](../../../plugins/agent-viz/wiki/inventory.md) topic 69. Used to mean
  "this bit matters too", it is filler wearing a hard hat.
- **No meta-commentary on the writing.** Not how the page is organized, not which sentence is the important one, not
  what the section is about to do. The reader wants the chart decision, not a tour of the prose.
- **Length discipline.** A page with little to say should be short. Padding a thin topic with plausible practitioner advice dressed as findings is the specific failure this wiki exists to avoid.
- State gaps plainly. A wiki that hides its holes is worse than a short one.

## Before finishing any edit

- Every internal link and anchor resolves.
- Every new type page appears in at least one index, and its `**Relationships.**` line agrees with the indexes that list it.
- New study or source pages are added to the tables in `wiki/README.md`, and the `primary-read` / `secondary-only` / `not-reached` counts there are updated.
- A claim that changed when someone opened the primary goes in `wiki/refutations.md`, which is the highest-value page in the wiki.
- Nothing is committed. Leave edits in the working tree for the maintainer to review.
