---
type: index
---

# Tables

Printed values in a grid, one row per record and one column per attribute, where the reader retrieves a number instead of reading it off a mark.

Like [network-topology.md](network-topology.md), this index is ours, added alongside the FT's nine relationships rather than amending them. The precedent for tables in a chart-type catalog is chapter 11 of *Better Data Visualizations*, which carries "The Ten Guidelines of Better Tables" plus two worked redesigns ([schwabish.md](../sources/schwabish.md)). Only its contents pages were read, so nothing it argues is cited here.

## Is the reader looking up a value?

The Urban Institute style guide names three ways out of drawing a chart: a sentence, one big number, or a table ([urban-institute.md](../sources/urban-institute.md), quoted in full on [part-to-whole.md](part-to-whole.md)). Two land here. Urban also gives a criterion, which most sources lack: patterns argue for a chart, and accurate value retrieval argues for a table. `authority-asserted`. It is [inventory.md](../inventory.md) topic 4, "should this be a chart at all", which the inventory leaves as a judgment call.

| The reader's question | Group |
|---|---|
| What is the value for this one row? | **This group** |
| These numbers will be checked against another document | **This group** |
| Which is biggest, and by how much? | [Magnitude](magnitude.md). A sorted bar chart |
| Is it going up? | [Change over time](change-over-time.md). A line chart |
| What shape do these values make? | [Distribution](distribution.md) |
| Do these two variables move together? | [Correlation](correlation.md) |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md) |
| Which one is the outlier? | Any of those. A chart shows it, and a grid of digits makes the reader hunt for it |

## The accessibility case

A table is often a required companion to a chart rather than an alternative. [Chartability](../sources/chartability.md) heuristic 30, "No table", is one of its fourteen `critical` heuristics:

> "A table must be provided that contains a human-readable version of the data the chart is based on. This may be excluded if the chart title, summary, context, or annotations are sufficient at conveying all relevant information contained in the chart."

The framework's default limits that exemption: "the auditor should assume failure when tests are inconclusive," so "the annotations probably cover it" does not reach it.

Heuristic 50, "Difficult chart type has no alternative", says "Pie charts, line charts without discrete marks, and bar charts without countable isotypes all pose cognitive difficulties." A table is the cheapest alternative path to the same task. Heuristic 35, "Table/data is static", binds only where the reader can sort or filter.

Chartability was community-tested with disabled reviewers, and its paper is `not-reached` here. It presents itself as heuristics, not measurements, and warns that "You cannot 'pass' Chartability 100%." Heuristic 30 is a published framework's obligation, not a measured result.

The [W3C WAI](../sources/w3c-wai-complex-images.md)'s third pattern for a complex image's long description puts image and description together in a `<figure>`, with the description "presented as headings, text, and a table". That is a WAI tutorial built on WCAG, a citable authority rather than an experiment, and the pattern itself has no conformance test of its own.

## What this group costs

A table spends no perceptual channel. The value is printed, so the accuracy ordering in [channels.md](../concepts/channels.md), which measures reading a value off a mark, does not apply in either direction.

A table gives up everything a chart shows for free: shape, trend, outliers, gaps and clusters. Every comparison is serial, one pair at a time, in row order. That follows from the construction, not from a study. Sorting by the column in question lets a table answer ranking questions, as ordering does in an [adjacency matrix](adjacency-matrix.md).

## Choosing a form

| Form | What carries the point | Defined for |
|---|---|---|
| A sentence | The writer's conclusion, in words | The message is one comparison and the reader never needs the numbers |
| A big aggregate number | One value set large, with a line of context | The message is a single quantity |
| A plain table | Printed digits in a grid | Values will be looked up, checked or copied |
| A table beside a chart | The chart carries the shape, the table carries the values | Both tasks are real, or heuristic 30 binds and the annotations do not cover it |

Four constraints, all `authority-asserted`:

- A table caption goes above the table, where a figure caption goes below. Wilke, [inventory.md](../inventory.md) topic 43.
- Every table carries a source line, as a figure does. Urban, topic 44.
- Every abbreviation is defined, and anything dropped is disclosed. Urban, topic 45.
- No merged cells, blank cells, blank rows or blank columns. Urban: "Tables that meet accessibility requirements cannot have any merged cells, blank cells, blank rows, or blank columns, as screen readers have a difficult time with spanner headings and blank cells" ([urban-institute.md](../sources/urban-institute.md)). Few other sources state it.

## Justifying the choice

**Defensible, evidence-backed:**

- "The long description is printed as headings, text and a table, which is one of the three patterns the W3C's own tutorial gives." Evidence-backed as a standard, not as an experiment ([w3c-wai-complex-images.md](../sources/w3c-wai-complex-images.md)).

No study in this corpus compares a table against a chart on any task.

**Defensible, with the label said out loud:**

- "The reader has to determine values accurately rather than see a pattern, so this is a table." Urban's criterion, `authority-asserted`.
- "One sentence carried the whole finding, so there is no figure at all." Same source, same class.
- "The chart ships with its underlying data as a table, because the title and annotations do not carry everything the chart shows." Chartability heuristic 30, `critical`, with its exemption checked rather than assumed.
- "Tables belong in a chart-type catalog." Chapter 11 of *Better Data Visualizations* is devoted to them, cited for its existence only.

**Commonly repeated, and the evidence does not support it:**

- ~~"A table is more accurate than a chart, because the reader gets the exact number."~~ The second half is definitional. The first is an untested comparison, and it slides from "the value is printed" to "readers end up with better answers", which is a different claim.
- ~~"Provide a table and the figure is accessible."~~ Heuristic 30 is one of fourteen criticals, eight of which bind on a static figure. A table does nothing for contrast, text size, reading level, or describing what is visually apparent.

## The failure mode this group invites

A chart drawn because a figure was expected, when the reader's task is looking up a value. The reader squints at a bar to recover a number that could have been printed.

The mirror case is a table dumped where one sentence would do, because the writer would not commit to a finding when the finding was "two of these went up and the rest did not move."

A caption written first separates the two. Where it is the entire finding, the caption carries it. Where no single caption works because every reader arrives with a different row in mind, that is the table case.

## Types in this index

None. Every form above leaves the chart tier. Candidates, none with a study behind it: a plain data table, a big aggregate number, a shaded or heat-mapped table (which borrows a color channel and stops being only a table), and a table with inline sparklines.

## See also

- [../inventory.md](../inventory.md): topic 4, and topics 43 to 45 on tables
- [../sources/chartability.md](../sources/chartability.md): heuristic 30 and the other criticals
- [../sources/w3c-wai-complex-images.md](../sources/w3c-wai-complex-images.md): the two-part text alternative
- [../sources/urban-institute.md](../sources/urban-institute.md): the three ways out, and the table accessibility rules
- [../sources/datawrapper-academy.md](../sources/datawrapper-academy.md): treats tables as an output alongside charts and maps in its accessibility article
- [../concepts/channels.md](../concepts/channels.md): what the accuracy ordering measures
- [part-to-whole.md](part-to-whole.md): the three ways out, quoted in full
- [network-topology.md](network-topology.md): the other index of ours
