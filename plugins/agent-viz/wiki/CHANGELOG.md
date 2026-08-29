# Wiki changelog

What changed in the **research**, as distinct from what changed in the **bar**. Most recent first.

Calendar dated, `vYYYY.MM.DD`, by the work that produced the entry. **These are not releases.** Nothing installs
against a wiki date and no version pins to it; release cadence belongs to the plugin and does not apply here. An entry
records that the corpus grew or that a claim moved, and it is written the day the work lands.

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

---

## v2026.08.29

The results of a dream run: the weekly research sweep, plus a corpus-wide pass converting the wiki
from advice-voice to record-voice.

### Added

- [studies/gutwin-2023-chord-vs-sankey.md](studies/gutwin-2023-chord-vs-sankey.md). First experiment in the corpus on any form in [chart-types/flow.md](chart-types/flow.md). Sankey beat chord on time, errors, effort and preference; the performance effects are small and largely gone by the fourth exposure, and the stimuli were static.
- [chart-types/flow-map.md](chart-types/flow-map.md). The type page both the flow and spatial indexes named as missing.
- [people/michael-correll.md](people/michael-correll.md). Four preprints read at primary.
- [concepts/channels.md](concepts/channels.md) records Bertini, Correll & Franconeri's argument that the channel ranking is derived from one task and untested on the rest. A position paper, and its authors decline the strong reading.

### Changed

- [chart-types/chord-diagram.md](chart-types/chord-diagram.md), [chart-types/sankey-diagram.md](chart-types/sankey-diagram.md) and [chart-types/network-topology.md](chart-types/network-topology.md) no longer report that no study tests these forms.
- [refutations.md](refutations.md) gains the chord-versus-Sankey entry: the primary supports the finding, not the strength the abstract implies.

### Corrected

- The 3:1 contrast floor for graphical objects is WCAG 2.1 SC 1.4.11, not WCAG 2.0, whose guideline 1.4 stops at 1.4.9. Corrected in [checks/matplotlib.md](checks/matplotlib.md) and [inventory.md](inventory.md) topic 33.
- Four source pages record an `author` for the first time: Few, Knaflic, Schwabish, Tufte.

## v2026.08.27

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
