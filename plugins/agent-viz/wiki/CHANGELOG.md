# Wiki changelog

What changed in the **research**, as distinct from what changed in the **bar**. Most recent first.

Calendar versioned, `vYYYY.MM.DD`. A wiki release records that the corpus grew or that a claim moved, and it carries no
semantic promise: nothing installs against it and no version pins to it.

## Why this is separate from the plugin changelog

The corpus and the skill change for different reasons and on different clocks.

- **[../CHANGELOG.md](../CHANGELOG.md)** is semantic, and answers *what does the bar now tell me to do*. A user reads it
  to find out whether a rule changed under them.
- **This file** is calendar, and answers *what does the wiki now know*. Adding a person page, reaching a source that was
  previously `secondary-only`, or overturning a claim in `refutations.md` are all real events that frequently change no
  rule at all.

Most research lands without moving the bar. A source page can double in size, and a study can be read at primary for the
first time, and the skill's instructions stay identical. Recording that under a semantic version would either inflate the
version for nothing or hide the work entirely.

**A plugin release cites this file rather than restating it.** When research does move a rule, the plugin changelog says
what the rule now is and links the entry here for why.

## What counts as an entry

- A new page in `sources/`, `studies/`, `people/`, `concepts/` or `chart-types/`.
- A `status` change, especially `secondary-only` or `not-reached` becoming `primary-read`. That is the wiki's core
  currency and it is always worth a line.
- A new or corrected entry in `refutations.md`. These are the highest-value events in the project.
- A structural change to the schema or the tiers.
- A correction to a claim the wiki previously made. **Corrections are recorded, never quietly edited**, in keeping with
  the discipline the corpus applies to everyone else.

Routine copy-editing, link fixes and formatting do not earn an entry.

**Sectioning starts at the second release.** From then on entries group under **Added**, **Changed** and
**Corrected**, because a reader will have a previous version to compare against and the three answer different
questions. The first release has no previous version, so it is one section: everything in it is new, and a
correction made to unreleased work is not a correction anyone can have been misled by. Corrections to claims the
wiki has actually published always get their own line, and are recorded rather than quietly edited.

---

## Unreleased

The first cut of the wiki, so everything in it is new and there is nothing yet to have changed under anyone.
**Added / Changed / Corrected start at the second release**, when a reader has a previous version to compare against.
What follows is what the wiki now knows, at the level a reader would care about rather than page by page.

**The corpus.** 111 pages: 17 sources, 23 studies, 15 people, 3 concepts, and a chart-type tier of 40 type pages
under 12 relationship indexes plus a name index. 49 pages are `primary-read`, 6 are `secondary-only`, none is
`not-reached`, and 23 carry `status_partial` because their coverage is uneven and saying so is more useful than
picking one label.

**Every claim carries the kind of warrant it actually has.** Evidence-backed, authority-asserted, contested, absence
of evidence, and a definitional exemption for statements that describe what a thing *is* and assert nothing
empirical. This is the whole point of the wiki, and the reason the chart-type tier reads as thin: **31 of the 40
type pages say plainly that no study in this corpus tests the form.** Deviation, ranking, spatial and flow have no
experiment behind any of their forms at all. Those pages inherit what they can, say where the evidence stops, and
stop, rather than filling the gap with plausible practitioner advice.

**Evidence attaches to channels, not to chart types.** No controlled study has ever tested a chart type as an
artifact in the world; they test stripped judgment tasks on stimuli that resemble one. So every type-level accuracy
claim is a two-step inference whose first step is a conjecture the source authors flag as one every time they make
it. [concepts/channels.md](concepts/channels.md) carries the evidence; type pages inherit it with a link and are not
allowed to restate it as a native finding.

**A third of the field's received wisdom did not survive contact with its primary.** That is what
[refutations.md](refutations.md) is for, and it is the highest-value page here. "Pies are read by angle" is refuted
by the one study that isolated the three cues, and the case against donut charts collapses with it. Bank-to-45 is
scope-limited rather than general. The axis-break glyph was tested as a truncation remedy and did not measurably
work. The flat ban on dual axes rests on a paper that studied something else. "Log scales are fine for experts"
fails at 56% against 93% among professional ecologists. Gray-plus-one-accent, which this project's own bar
recommends, has no controlled study behind it and both practitioners it is credited to assert it in their own words.

**The Cleveland-McGill ranking is two rankings**, 1984 and 1985, which disagree from area downward. The list
everyone reproduces is the 1985 one, routinely cited to 1984. Not a corruption, a misattribution. No page a reader
uses to choose a chart states a bare rank number, because the number silently depends on which table was meant.

**Taxonomy is an index, not a home.** A data relationship is a view of a chart rather than a property of it, so type
pages are stored flat and grouped by index pages that point at them. Nobody else's scheme gets amended: the FT's
nine relationships stand as published, and network-topology, tables and qualitative sit alongside them as ours.
Membership is declared on the page and checked against the indexes mechanically.

**Chart names are not stable, and the wiki now says so with numbers.**
[chart-types/aliases.md](chart-types/aliases.md) resolves 103 names to pages. Its third column is the useful part:
some mappings are recorded in a source read here, some are a page's own stipulation said out loud, and a large
share are simply in circulation with nothing here defining them. Three names collide badly enough to get their own
sections. "Mosaic plot" is largely settled by a primary definition; "heat map" takes at least four referents; "range
plot" means either two measurements or an interval around an estimate. Each type page declares the names it answers
to, and the two lists are checked against each other.

**Sources vouch for different things, and the difference is recorded.** A book's contents pages vouch for where a
type is filed and for not one word of what the book argues, which is how Schwabish's catalog and Munzner's course
slides are used. Full text vouches for both, which is why Wilke closes a batch of names at primary that no contents
listing could. The FT Visual Vocabulary is recorded complete, 67 entries under 59 names, with every gloss verbatim
including the source's own typos.

**Independence is a claim that needs support.** The absence of a byline is not support for it, and neither is it
support for authorship. The Urban Institute style guide and Jonathan Schwabish were counted as two voices when they
are one, and the correction runs the other way too: the evidence supports non-independence, not that he wrote it.

**Provenance is auditable or it is worthless.** Every research page carries a "How this was read" paragraph naming
which artifact was opened, how it was extracted, what was rendered to images for want of a text layer, and what was
left unread. The extraction rules exist because specific failures produced confidently wrong output: a summarizer
once returned, inside quotation marks, the reverse of a paper's stated conclusion, and a paywalled paper was written
up as unreachable while a local copy existed the whole time.

**What is honestly missing.** Cairo's choropleth-classification and uncertainty chapters were not reached. *The
Visual Display of Quantitative Information* is read only through Wilke quoting it, so the data-ink, chartjunk and
lie-factor quotes are quotes of quotes; the one part of Tufte read directly is the sparklines chapter of *Beautiful
Evidence*, from an excerpt on his own site. Accessibility duplicates a licensed inventory that should be imported
rather than re-derived. Two inventory topics have no coverage at all, both found only because Few's primary turned
out to be readable after being written up as unreadable.
