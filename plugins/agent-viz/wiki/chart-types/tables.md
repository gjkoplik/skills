---
type: index
---

# Tables

Printed values in a grid, one row per record and one column per attribute, where the reader retrieves a number instead of reading it off a mark.

This index is ours rather than the FT's, on the same footing as [network-topology.md](network-topology.md): the nine relationships stay as published and this one sits alongside them. The citable precedent for putting tables in a chart-type catalog at all is *Better Data Visualizations*, whose chapter 11 is Tables and carries "The Ten Guidelines of Better Tables" plus two worked redesigns ([schwabish.md](../sources/schwabish.md)). That is the chapter's existence and contents, verified from the book's own contents pages; what it argues is unread in this corpus and is not cited below.

## Is the reader looking up a value?

The Urban Institute style guide names three ways out of drawing a chart, and two of them land here ([urban-institute.md](../sources/urban-institute.md); the passage is quoted in full on [part-to-whole.md](part-to-whole.md)). Generalized:

- **A sentence.** Where explanatory prose distills the point better than a figure would, the prose replaces the figure.
- **One big number.** Where the message is a single quantity, it is set large with a line of context under it.
- **A table.** Where the goal is detailed information rather than a pattern, or the reader has to determine values accurately.

Urban attaches a criterion, where most sources give none: **patterns argue for a chart, accurate value retrieval argues for a table.** `authority-asserted`. That is [inventory.md](../inventory.md) topic 4, "should this be a chart at all", which the inventory states as a judgment call and does not resolve.

| The reader's actual question | Group |
|---|---|
| What is the value for this one row? | **This group** |
| These numbers will be checked against another document | **This group** |
| Which is biggest, and by how much? | [Magnitude](magnitude.md). A sorted bar chart |
| Is it going up? | [Change over time](change-over-time.md). A line chart |
| What shape do these values make? | [Distribution](distribution.md) |
| Do these two variables move together? | [Correlation](correlation.md) |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md) |
| Which one is the outlier? | Any of those. A chart shows it; a grid of digits makes the reader hunt for it |

## The accessibility case

**A table is frequently a required companion to a chart rather than an alternative to it.** [Chartability](../sources/chartability.md) heuristic 30, "No table", is one of its fourteen `critical` heuristics:

> "A table must be provided that contains a human-readable version of the data the chart is based on. This may be excluded if the chart title, summary, context, or annotations are sufficient at conveying all relevant information contained in the chart."

The exemption is stated in the source and is real: a chart whose text already carries everything owes no table. The framework's own default cuts the other way, though, since "the auditor should assume failure when tests are inconclusive," so "the annotations probably cover it" does not reach the exemption.

Two other heuristics bear here. **50, "Difficult chart type has no alternative"**: "Pie charts, line charts without discrete marks, and bar charts without countable isotypes all pose cognitive difficulties." The remedy is not dropping the form, it is providing another path to the same task, and a table is the cheapest one available. **35, "Table/data is static"** is the interactive counterpart and binds only where the reader can sort or filter.

Evidence class: Chartability is peer-reviewed and community-tested with disabled reviewers, and it states itself as heuristics rather than as measurements, with the flat warning that "You cannot 'pass' Chartability 100%." Heuristic 30 is an obligation from a published framework, not a measured result.

The [W3C WAI](../sources/w3c-wai-complex-images.md) reaches the same artifact from the other direction. Its third pattern for attaching a long description to a complex image puts image and description together in a `<figure>`, with the description "presented as headings, text, and a table". That source is evidence-backed in the sense the wiki uses for a published standard: an external citable authority with a defined conformance test, not an experiment.

## What this group costs

**A table spends no perceptual channel at all.** Nothing sits on position, length, angle or area; the value is printed and read as text. So the accuracy ordering in [channels.md](../concepts/channels.md) does not apply here in either direction, and the comparison people want from it has not been run: that literature measures reading a value off a mark, and a table prints the value. Those are different tasks and nothing in this corpus puts them head to head. The retrieval task is what the record covers; the accuracy comparison is not in it.

What the group gives up is everything a chart delivers without the reader working for it. Shape, trend, outliers, gaps and clusters are all present in the numbers and none of them is visible. Every comparison is serial, one pair at a time, in whatever order the rows happen to be in. That follows from the construction rather than from a study.

Row order is the one structural choice a plain table offers, and it does the job an ordering does in an [adjacency matrix](adjacency-matrix.md): sorted by the column in question, a table answers ranking questions it cannot answer unsorted.

## Choosing a form

| Form | What carries the point | Defined for |
|---|---|---|
| A sentence | Your own conclusion, in words | The message is one comparison and the reader never needs the numbers |
| A big aggregate number | One value set large, with a line of context | The message is a single quantity |
| A plain table | Printed digits in a grid | Values will be looked up, checked or copied |
| A table beside a chart | The chart carries the shape, the table carries the values | Both tasks are real, or heuristic 30 binds and the annotations do not cover it |

Four constraints, all `authority-asserted`:

- **A table caption goes above the table**, where a figure caption goes below. Wilke, [inventory.md](../inventory.md) topic 43.
- **A source line on every table**, the same obligation a figure carries. Urban, topic 44.
- **Every abbreviation is defined, and what was dropped is disclosed.** Urban's Tables section, topic 45.
- **No merged cells, blank cells, blank rows or blank columns.** From Urban's accessibility section: "Tables that meet accessibility requirements cannot have any merged cells, blank cells, blank rows, or blank columns, as screen readers have a difficult time with spanner headings and blank cells" ([urban-institute.md](../sources/urban-institute.md)). Rarely stated anywhere else.

## Justifying the choice

**Defensible, evidence-backed:**

- "The long description is printed as headings, text and a table, which is one of the three patterns the W3C's own tutorial gives." Evidence-backed in the sense that applies to a standard rather than to an experiment ([w3c-wai-complex-images.md](../sources/w3c-wai-complex-images.md)).

Nothing else. No study in this corpus compares a table against a chart on any task.

**Defensible, with the label said out loud:**

- "The reader has to determine values accurately rather than see a pattern, so this is a table." Urban's criterion, and the clearest statement of it in this corpus.
- "One sentence carried the whole finding, so there is no figure at all." Same source, same class.
- "The chart ships with its underlying data as a table, because the title and annotations do not carry everything the chart shows." Chartability heuristic 30, `critical`, with its exemption checked rather than assumed.
- "Tables belong in a chart-type catalog." Chapter 11 of *Better Data Visualizations* is devoted to them, cited here for the chapter's existence rather than for anything it argues.

**Commonly repeated, and the evidence does not support it:**

- ~~"A table is more accurate than a chart, because the reader gets the exact number."~~ The second half is definitional and secure. The first half is a comparison nobody here has run, and it slides from "the value is printed" to "readers end up with better answers", which is a different claim and an untested one.
- ~~"Provide a table and the figure is accessible."~~ Heuristic 30 is one of fourteen criticals, eight of which bind on a static figure. A table does nothing for contrast, text size, reading level, or describing what is visually apparent.

## The failure mode this group invites

**A chart drawn because a figure was expected, where the reader's actual task is looking up a value.** The figure gets made because the section looks bare without one, and then the reader squints at a bar to recover a number that could have been printed. Nothing about the chart is wrong; it is answering a question nobody asked.

Its mirror is just as common: **a table dumped where one sentence would do.** Twelve rows and four columns shipped as raw material because the writer did not want to commit to a finding, when the finding was "two of these went up and the rest did not move."

A check: the caption, written first. Where the caption is the entire finding, the caption carries it. Where no single caption can be written because every reader arrives with a different row in mind, that is the table case.

## Types in this index

None. Every form named above is a way of leaving the chart tier rather than a chart with a page of its own.

Candidates if any of them ever earns a page, and none has a study behind it today: a plain data table, a big aggregate number, a shaded or heat-mapped table (which borrows a color channel and stops being only a table), and a table with inline sparklines.

## See also

- [../inventory.md](../inventory.md) — topic 4 is the rule this index carries; topics 43 to 45 are the table-specific obligations
- [../sources/chartability.md](../sources/chartability.md) — heuristic 30 in full, the fourteen criticals, and how the framework classes its own authority
- [../sources/w3c-wai-complex-images.md](../sources/w3c-wai-complex-images.md) — the two-part text alternative, and where a table sits inside it
- [../sources/urban-institute.md](../sources/urban-institute.md) — the three ways out, and the table accessibility rules
- [../sources/datawrapper-academy.md](../sources/datawrapper-academy.md) — treats tables as an output alongside charts and maps in its accessibility article
- [../concepts/channels.md](../concepts/channels.md) — what the accuracy ordering actually measures, and why it does not settle table against chart
- [part-to-whole.md](part-to-whole.md) — the fullest statement of the three ways out
- [network-topology.md](network-topology.md) — the other index of ours, and the argument for adding rather than amending
