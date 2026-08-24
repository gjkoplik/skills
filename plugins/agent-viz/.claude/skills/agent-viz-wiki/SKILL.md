---
name: agent-viz-wiki
description: Conventions for maintaining the agent-viz research wiki under wiki/ — the page schema and status labels, the evidence-class discipline (evidence-backed / authority-asserted / contested / absence of evidence, plus the definitional exemption), the two-tier chart-type structure with flat storage and index pages, the source-extraction rules that exist because specific tooling failures produced confidently wrong output, and the house prose style. Load whenever adding or editing anything under wiki/, adding a source or study page, adding a chart-type page, or running the weekly sweep routine.
---

# Maintaining the agent-viz wiki

The wiki under `wiki/` is the research behind the figure quality bar. Its value is not that it collects claims; it is that **every claim carries the kind of warrant it actually has.** Roughly a third of the received wisdom this project checked did not survive contact with its primary source. Adding a page that launders a convention into a finding does more damage than leaving the topic uncovered.

Read [wiki/README.md](../../../wiki/README.md) for the current state before editing. It is the index and it carries the live page counts.

## The page schema

Every page opens with four things, then the substance, then links:

- **What it is.** One or two sentences.
- **Status.** `primary-read`, `secondary-only`, or `not-reached`.
- **What it is good for.** The specific question to come back with.
- **What it does not settle.** The limits, stated rather than implied.

**Status is load-bearing, not decoration.** `primary-read` means someone opened the actual source and the quotes come from a local extraction. `secondary-only` means abstracts or summaries, and its quotes are unvouched. Do not upgrade a status because a summary was detailed or confident.

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

Full treatment in [wiki/concepts/evidence-class.md](../../../wiki/concepts/evidence-class.md).

## Chart types: written for someone making a choice

**The reader is standing in front of a dataset and has to pick a form and defend the pick.** Every section earns its place by helping with that, or it comes out. Three rules follow, and the first two are where the first draft of this tier went wrong badly enough to need rewriting:

- **Lead with the choice, not the anatomy.** The first substantive section asks whether this group or form is even the right frame for the reader's question. The most common failure is not picking the wrong chart within a group, it is being in the wrong group: composition charts get reached for when the question is ranking, network diagrams get drawn when the question is answerable from a per-node table. Structure, channels and evidence come after.
- **No process narration.** Which page was written first, what is a "shape-setter", what remains uncovered, how the research went: none of it helps anyone choose a chart. Coverage and status live in `wiki/chart-types/README.md` and in `wiki/README.md`. Keep them off pages that exist to support a decision.
- **Give the reader the sentences.** Pages carry a "justifying the choice" section: what is defensible and evidence-backed, what is defensible with the label said out loud, and what is commonly repeated and unsupported. The refutations are the project's most valuable output and they are wasted if they only appear in `refutations.md`.

## Chart types: flat storage, index pages

Type pages live **flat** in `wiki/chart-types/`. Grouping happens in index pages that point at them.

A data relationship is a **view** of a chart, not a property of it: a stacked bar is part-to-whole and magnitude and change-over-time. A directory tree would force one home and demote the rest. Flat storage also means the FT's nine relationships are never amended, only indexed alongside indexes of our own.

- Every type page declares its own `**Relationships.**` line in the header, so an index is checkable against the pages rather than maintained by hand.
- Every type page carries the six-slot structural decomposition (data, transform, geometry, scale, coordinates, guides). Those slots are definitional and carry no evidence label.
- **The inheritance rule: evidence attaches to channels, not to chart types.** No controlled study has tested a chart type as an artifact in the world. A type page inherits accuracy claims from [wiki/concepts/channels.md](../../../wiki/concepts/channels.md) with a link; it does not restate them as native findings. Where a study *has* decomposed a specific type, that is a genuine type-level finding and belongs on the page.

## Source-extraction rules, each written in blood

These exist because a specific failure produced confidently wrong output that nearly shipped.

- **Never quote from a fetch summary.** A summarizer once returned, inside quotation marks, the reverse of a paper's stated conclusion. Download and extract locally, then quote from the extraction.
- **Verify the identity of what you downloaded.** Print the first lines of the extraction and confirm the title matches before using it. A plausible-looking arXiv URL once yielded an entirely unrelated paper.
- **Check for a local copy before recording a source as `not-reached`.** A paywalled paper with no open-access deposit was written up as unreachable while a local PDF existed the whole time. Search the filesystem, including sibling repos, before concluding.
- **A scanned PDF with no text layer is still readable.** Render the pages to images and read them. That is a stronger primary read than OCR. Decrypt or re-render if a reader refuses the file.
- **PDF text layers misattribute table values.** Interleaved metric blocks and vertically centered cells both slide labels onto the wrong rows. Cross-check any table against the prose, or use an HTML rendering.
- **Text layers silently drop characters**, including comparison operators and `±`, which is the difference between a bound and its negation.

## House prose style

- **No em-dashes in your own sentences.** Use commas, parentheses, semicolons, or shorter sentences. The one exception is a verbatim quote, which stays verbatim. The ` — ` separator in see-also list glosses is established convention here and is fine.
- American spelling. Direct, slightly informal, no throat-clearing.
- No AI filler: "delve", "moreover", "furthermore", "it's worth noting that", "in essence".
- **Length discipline.** A page with little to say should be short. Padding a thin topic with plausible practitioner advice dressed as findings is the specific failure this wiki exists to avoid.
- State gaps plainly. A wiki that hides its holes is worse than a short one.

## Before finishing any edit

- Every internal link and anchor resolves.
- Every new type page appears in at least one index, and its `**Relationships.**` line agrees with the indexes that list it.
- New study or source pages are added to the tables in `wiki/README.md`, and the `primary-read` / `secondary-only` / `not-reached` counts there are updated.
- A claim that changed when someone opened the primary goes in `wiki/refutations.md`, which is the highest-value page in the wiki.
- Nothing is committed. Leave edits in the working tree for the maintainer to review.
