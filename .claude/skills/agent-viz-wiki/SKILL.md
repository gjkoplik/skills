---
name: agent-viz-wiki
description: "Conventions for maintaining the agent-viz research wiki under plugins/agent-viz/wiki/: the page schema and status labels, the evidence-class discipline (evidence-backed / authority-asserted / contested / absence of evidence, plus the definitional exemption), the two-tier chart-type structure with flat storage and index pages, the source-extraction rules, and the house prose style. Load whenever adding or editing anything under wiki/, adding a source or study page, adding a chart-type page, or running the weekly sweep routine."
---

# Maintaining the agent-viz wiki

The wiki under `plugins/agent-viz/wiki/` is the research behind the figure quality bar. Its value is that every claim carries the kind of warrant it has. Roughly a third of the received wisdom this project checked did not survive contact with its primary source, so a page that launders a convention into a finding does more damage than leaving the topic uncovered.

Read [wiki/README.md](../../../plugins/agent-viz/wiki/README.md) before editing. It is the index and carries the one machine-checked count.

## Who reads a page

An agent, sometimes a person, with a dataset in front of them. They are choosing a chart and need to defend the choice, or they are about to apply a rule and want to know whether an experiment backs it. They read at decision time and pay per token. They need the decision, what it costs, the sentence that defends it, and the label on the warrant. They do not need how the research went, what the page is about to do, when a line was corrected, or a count of anything in the wiki.

## The page schema

Facts live in frontmatter. Argument lives in the body. Never both.

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

**Status is load-bearing.** `primary-read` means someone opened the source and quotes come from a local extraction. `secondary-only` means abstracts or summaries, and its quotes are unvouched. `not-reached` says where you looked. Do not upgrade a status because a summary was detailed or confident. Where a page covers several artifacts reached unequally, `status` is the principal subject, `status_partial: true`, and the body says which parts are which.

**Record `author` whenever it is known.** Independence is the wiki's most-used argument ("three unrelated organizations") and it once counted the Urban Institute style guide and Jonathan Schwabish as two voices when he is behind both. Before adding a source to a corroboration count, check who wrote it.

**Links are ordinary markdown relative paths.** A link to a page that does not exist is a broken link, not a placeholder. Name a page that should exist in prose without linking it. Never link outside `plugins/agent-viz/`; the plugin cannot read past its own directory once installed.

**`aliases:` is a name index in two places that must agree.** Every chart-type page lists the names it answers to, and [chart-types/aliases.md](../../../plugins/agent-viz/wiki/chart-types/aliases.md) maps each name to its page with the mapping's provenance. A row whose target cell begins "No page" is a pointer to a different form, not an alias, and is excluded from the check. One name per row.

### Body, by page type

- **Source, study, person.** A header block under the title: **What it is good for** (the question to come back with), **What it does not settle**, and **How this was read**. Then substance under `##` headings. Study pages keep the finding with its quotes, the method, the sample, the limits the authors state, and a bulleted "what this result does not license". Person pages use "What they are known for", "What they are good for", "What they do not settle", and are not biographies: a person page says what coming to this person buys you and where their authority stops. `sources/` covers one work; `people/` covers the person across their work. A prolific author can have both.

  **"How this was read" is the provenance and must not be deleted as a duplicate of the status label.** It says which artifact was opened, how it was extracted, what was rendered to images because it had no text layer, what was left unopened, and which parts of a split status apply to which material. Without it a `primary-read` label is unauditable. The retrieval date lives in frontmatter, not here.

- **Concept.** The same header block plus **What it is**, because a concept's slug does not convey it. Its status is prose in the body (usually "synthesis by this project") and takes no frontmatter label.

- **Chart type and index.** No header block. One line of definition under the title, then the decision.

- **Directory READMEs** take no frontmatter and no `Status` field. Coverage belongs in a table that can be checked, not in prose that drifts.

**Never state a bare rank number on a page a reader uses to choose a chart.** Name the channel. "Position instead of area" is what a chooser needs; "rank 1 instead of rank 4" depends on which of two Cleveland & McGill tables you meant, and they disagree from area downward.

## Evidence class, on every claim

- **Evidence-backed.** A study, experiment or published standard. Cite the source and the number. State it flatly.
- **Authority-asserted.** A practitioner or design book asserting it without an experiment. Usable as a default, with the status visible.
- **Contested.** The record disagrees with itself. State the rule, the contest, and what survives.
- **Absence of evidence.** Nobody has tested it. Not contested, and not refuted. State the caution and its reason.
- **Definitional.** Describes what something is and asserts nothing empirical. Carries no label, because labeling it would dilute the labels on real claims. Structural decompositions are the standard case.

The label belongs in the sentence, so it survives quotation. Watch for *therefore*: "a hive plot puts node position on a real data scale" is definitional and secure; "therefore readers read it more accurately" has no study behind it. Full treatment in [wiki/concepts/evidence-class.md](../../../plugins/agent-viz/wiki/concepts/evidence-class.md).

## Chart types

Type pages live flat in `wiki/chart-types/`. Index pages, one per data relationship, group them. A data relationship is a view of a chart, not a property of it: a stacked bar is part-to-whole and magnitude and change-over-time, and a directory tree would have to pick one. The FT's nine relationships stay as published; this wiki's own indexes (network-topology, tables, qualitative) sit alongside them. Reclassifying a type is an edit to an index, not a file move.

**Evidence attaches to channels, not to chart types.** No controlled study has tested a chart type as an artifact; they test judgment tasks on stimuli that resemble one. A type page may inherit an accuracy claim from [wiki/concepts/channels.md](../../../plugins/agent-viz/wiki/concepts/channels.md) with a link, stated once as a clause ("the step from mark to channel is conjecture in the source literature"). It may not restate the claim as a native finding. Where a study did decompose a specific type, that is a type-level finding and belongs on the page; `pie-and-donut.md` is the model.

**Three rules for the writing:**

- Lead with the choice, not the anatomy. The common failure is the wrong group (a composition chart for a ranking question), not the wrong chart within a group.
- No process narration. Which page was written first and what remains uncovered belong in `chart-types/README.md` and `wiki/README.md`, not on a page that supports a decision.
- Give the reader the sentences. The "Justifying the choice" section carries what is defensible and evidence-backed, what is defensible with the label said out loud, and what is commonly repeated and unsupported.

**Index pages** carry: is this group the right frame, and how to tell; what the group costs in channel terms; how to choose a form within it; how to justify the choice; the failure mode the group invites; the types it indexes.

**Type pages** carry these six `##` sections, in this order, spelled exactly as `validate.py` checks them. A section with nothing to say is one line ("No study in this corpus tests the form.").

1. **When to reach for it, and when not.** The conditions the form is defined for, and a table of "the reader's question → the alternative".
2. **Structural decomposition.** The six slots below.
3. **Channels.** Which channel each mark puts the reader on, linking to `concepts/channels.md`.
4. **What is measured.** Only study-traceable claims, cited, with the effect and its scope: what the form is measured as good at, what it is measured as bad at, and where the record disagrees with itself. Nearby results that do not transfer get one sentence each saying why.
5. **The failure mode it invites.** Usually `authority-asserted`, and labeled.
6. **Justifying the choice.** The three lists.

**Evidence labels are written one way:** inline, in backticks, from exactly this vocabulary: `evidence-backed`, `authority-asserted`, `contested`, `absence of evidence`. Definitional statements carry no label. No bold labels, no "Mixed", no "refuted by this paper" used as a label.

The six slots, from Wilkinson's *Grammar of Graphics* by way of ggplot2:

| Slot | The question |
|---|---|
| Data | What is one row |
| Transform | What statistic is computed before drawing, if any |
| Geometry | What mark is drawn |
| Scale | How values map to the mark's properties |
| Coordinates | What space the mark is placed in |
| Guides | What axes, legends and reference marks are required to read it |

The slots are definitional and carry no label. They earn their place by collapsing near-duplicates: a coxcomb is a bar chart in polar coordinates, an area chart is a line chart with a fill.

## Source-extraction rules

Each of these exists because a specific failure produced confidently wrong output.

- **Never quote from a fetch summary.** A summarizer once returned, inside quotation marks, the reverse of a paper's stated conclusion. Download, extract locally, quote from the extraction.
- **Verify the identity of what you downloaded.** Print the first lines and confirm the title. A plausible arXiv URL once yielded an unrelated paper.
- **Check for a local copy before recording `not-reached`**, including sibling repos. A paywalled paper was written up as unreachable while a local PDF existed.
- **A scanned PDF with no text layer is still readable.** Render the pages to images and read them.
- **PDF text layers misattribute table values.** Cross-check any table against the prose, or use an HTML rendering.
- **Text layers silently drop characters**, including `±` and comparison operators, which is the difference between a bound and its negation.

## The wiki records facts. It does not give advice.

The wiki is a vault of findings an agent navigates. That agent forms opinions and makes recommendations to its user. The wiki says what was measured, by whom, with what limits, and stops. A page never says "don't use pie charts"; it says what the studies found.

Three tests, applied to every sentence:

- **No second person and no imperatives.** "Label the volumes" is advice; "the volumes are unlabeled on this chart" is a fact.
- **No exhortation.** "That is the number to design against", "anyone quoting this is off by 7x". State the finding and the discrepancy.
- **Delete the bolded lead-in. If no fact is lost, it stays deleted.** A label names the thing ("**Density.**", "**The zero baseline.**"), not its category ("**The trap.**", "**Caveat.**", "**Note.**"). The one exception is a repeated field in the same position on every comparable page, such as "**The tell.**" on person pages.

Sections whose names sound like advice still hold facts. "When to reach for it" is the conditions the form is defined for. The quoted first-person sentences under "Justifying the choice" are sentences a chooser could say, and they stay in quotation marks.

## House prose style

Direct, slightly informal, American spelling. Plain declaratives, one idea per sentence, around twenty words. A full sentence beats a fragment with a colon. No em-dashes outside a verbatim quotation, including in see-also glosses, where a colon follows the link. No "delve", "moreover", "furthermore", "it is worth noting", "in essence".

What gets cut on sight:

- **Zingers and closers.** A sentence whose job is to land the paragraph rather than add a fact. "The stronger word is wrong." "Written in blood." "And it stops."
- **Meta-commentary on the page or the project.** "Stated up front, because", "this follows from the section above", "the entry exists because", "this page will not pretend otherwise".
- **History narration.** Inline dated corrections, "an earlier version said", retrieval dates in body text, research-run vocabulary. The changelog holds history. Keep the corrected claim; drop the story of the correction.
- **Repeated epistemics.** The inheritance caveat once per page. Evidence classes are not re-explained.
- **Self-referential counts.** "40 type pages", "resolves 105 names", "31 of the 40". They rot on every edit. Describe coverage in words or not at all. The one exception is the `Current state:` line in `wiki/README.md`, which `validate.py` enforces.
- **Intensifiers.** "genuinely", "actually", "plainly", "outright", "at all", "real" as in "a real constraint". "load-bearing" only in its literal sense.
- **Superlative previews.** "The sharpest statement of this is", "the one that matters most". Say the thing.
- **Admiring a quote.** "The FT gloss is ten words." Give the quote and what it means.

**Length.** A type page runs 500 to 900 words, an index 700 to 1200, a study 500 to 900 plus its quotations, a source 600 to 1100, a person 600 to 1000, a concept 500 to 800. A page with nothing measured sits at the low end. Padding a thin topic with practitioner advice dressed as findings is the failure this wiki exists to avoid.

## The wiki changelog

Calendar dated by the work that produced the entry: a sweep writes its own `## vYYYY.MM.DD` heading the day it runs. Nothing installs against a wiki date. Do not park work under `## Unreleased`. Open the entry with one line naming what produced it. Entries are one line each and link to the page rather than restating it. Group under **Added**, **Changed** and **Corrected**; omit an empty heading.

## Before finishing any edit

- Run `python3 .claude/skills/agent-viz-wiki/validate.py` from the repo root. It checks frontmatter, the README's count line, page-versus-index agreement, the eight type-page sections, alias agreement in both directions, links and anchors, and plugin-boundary escapes. Gaps are open items, not failures. **From another directory the relative path does not resolve, and piped through `grep` it prints nothing, which reads as a clean run.**
- Every new type page appears in at least one index and its `relationships:` agrees with the indexes that list it.
- New study or source pages are added to the tables in `wiki/README.md`, and the `Current state:` line is updated.
- A claim that changed when someone opened the primary goes in `wiki/refutations.md`.
- Nothing is committed unless the maintainer asked for a branch. Leave edits in the working tree for review.
