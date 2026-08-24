# W3C WAI, *Complex Images*

**What it is.** One page of the W3C Web Accessibility Initiative's Images Tutorial, covering charts, diagrams, and maps. It defines the **two-part text alternative**: a short description to identify the image, and a long description that carries the information.

**Status.** `primary-read`. The page at `w3.org/WAI/tutorials/images/complex/` was fetched and converted locally, retrieved 2026-08-23. Quotes are verbatim.

**What it is good for.** The authoritative definition of what alt text for a chart is supposed to *contain*, and the three HTML patterns for attaching a long description. It is the standard that Datawrapper's alt-text guidance and the Urban Institute's alt-text rules are implementations of.

**What it does not settle.** Nothing about the chart itself. This page is about text alternatives for an image that already exists. It also does not address native accessibility of an SVG or canvas chart, screen-reader navigation of chart structure, keyboard interaction, contrast, or any of the other forty-nine things [chartability.md](chartability.md) covers. It is one heuristic, well specified.

---

## The definition

> "Complex images contain substantial information -- more than can be conveyed in a short phrase or sentence. These are typically:
>
> - graphs and charts, including flow charts and organizational charts;
> - diagrams and illustrations where the page text relies on the user being able to understand the image;
> - maps showing locations or other information such as weather systems."

Charts are named first. This page is the chart page.

## The two-part pattern

> "In these cases, a two-part text alternative is required. The first part is the short description to identify the image and, where appropriate, indicate the location of the long description. The second part is the long description -- a textual representation of the essential information conveyed by the image."

Both parts are required, and they have different jobs. The short description **identifies**; the long description **conveys**. A single long `alt` attribute is not the pattern, and neither is a short `alt` with nothing behind it.

The worked example makes the split concrete. Short:

> "Bar chart showing monthly and total visitors for the first quarter 2025 for sites 1 to 3"

Long, described as covering:

> "detailed information, including scales, values, relationships and trends that are represented visually. For example, the long description can point out the declining values for site 1, consistent values for site 2, and increasing values for site 3 that are encoded in the bar chart."

**Scales, values, relationships, trends.** That four-item list is the most usable specification of long-description content anywhere in this corpus, and it is the thing to check a generated description against. A description that names the chart type and the axes but says nothing about direction has covered scales and values and skipped the two that matter.

## Composition can be part of the information

A subtle point the page makes that most alt-text advice misses:

> "There are situations where the composition of an image is important and needs to be provided in the long description. For example, the sequence of colors used and the relative heights of the columns in a bar chart may be relevant information about the structure of the chart, in addition to the actual values and trends that it depicts."

So the standard's own position is that "describe the data, not the visuals" is **too simple**. When the encoding carries meaning, the encoding is content. Compare Datawrapper's article, which argues the opposite in passing ("if words are used instead to describe the data, there's no need to talk about visual elements at all") and then concedes it is a judgment call. The W3C's version is the better one: it depends on whether the composition is load-bearing.

## Long descriptions should be visible to everyone

> "Complex images can be difficult to understand by many people -- especially those with low vision, learning disabilities, and limited subject-matter experience. Make long descriptions available to everyone to reach a wider audience with your content. For example, show the description as part of the main content. It may also be possible to reduce unnecessary complexity in your images and make them easier to understand for everyone."

Two moves in one paragraph. The first is that a long description hidden in markup helps fewer people than the same text printed on the page, so **the accessible artifact and the readable artifact are the same artifact**. The second is a nudge back upstream: if the description is hard to write, consider simplifying the chart.

And on the surrounding prose:

> "It is also good practice to refer to and summarize more complex images from the accompanying text. For example, a reference such as 'The following graph shows that visitors were lost in the first quarter, but the numbers recovered in the second quarter' helps to point out the relevant information that the image is intended to present."

That example sentence is a takeaway title in disguise. The accessibility requirement and inventory topic 37 (title states the takeaway) converge on the same output, which is a useful thing to notice when arguing for either.

## The three attachment patterns

Given a `chart.png` with a short `alt`, the long description can be attached three ways:

**1. An adjacent link.** Universally supported, and the description is a real page others can read, but "the link is not associated with the image in a semantic way." The page shows the semantic upgrade, wrapping both in `<figure role="group">` with the link in `<figcaption>`.

**2. Location described inside `alt`.** The `alt` itself says where to look: `"...Described under the heading Site visitors full text."` Requires the heading text to stay accurate.

**3. `<figure>` containing both.** Image and long description together, the description "presented as headings, text, and a table", wrapped in `<figcaption>`, with `role="group"` for backward compatibility.

`role="group"` appears in all three because `<figure>` semantics were historically inconsistent across browsers. Worth knowing before treating a bare `<figure>` as sufficient.

Note that none of the three is `longdesc`. That attribute is absent from the current tutorial.

## What this means for a figure produced by a plotting library

The gap between this standard and a matplotlib `savefig()` is total. A PNG on disk has no `alt`, no `figcaption`, and no page around it. The two-part pattern binds at the **publication** boundary, not at the plotting boundary, which means:

- A figure bar can require that the long-description content **exists** (scales, values, relationships, trends), and can check that a caption or docstring carries it.
- It cannot check the markup, because the markup is downstream of the library.
- The most useful mechanizable version is a presence check plus a content checklist, which is how [inventory.md](../inventory.md) topic 71 already frames it: mechanizable as presence, judgment as content.

This is also the point where the Urban Institute's web practice collides with the standard. Urban bakes title, subtitle, source, and notes into a single PNG and compensates with `alt` (see [urban-institute.md](urban-institute.md)). That is defensible under this page, since a two-part alternative is what it asks for. It is not defensible under the broader "text should be real text" position (inventory topic 73), and the two sources do not acknowledge each other. A bar has to pick.

## Evidence class

This is a **published standard**, which is a different thing from an experiment and a different thing from a design opinion. The inventory classes topic 71 as evidence-backed on that basis. That is the right call as long as "evidence-backed" is read as "there is an external, citable authority with a defined conformance test", not as "an experiment measured this working." The W3C tutorial is normative guidance built on WCAG success criteria; it does not report a study.

## Where this source is used

Inventory topics 71 and 72. See [roll-call.md](../roll-call.md).

## Links

- [W3C WAI: Complex Images](https://www.w3.org/WAI/tutorials/images/complex/)
- [W3C WAI: Images Tutorial](https://www.w3.org/WAI/tutorials/images/)
- [An alt Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/)
- Related: [chartability.md](chartability.md) for the other forty-nine heuristics, [datawrapper-academy.md](datawrapper-academy.md) for a worked implementation
