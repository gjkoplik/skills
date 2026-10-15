---
type: source
status: primary-read
retrieved: 2026-08-23
---

# W3C WAI, *Complex Images*

One page of the W3C Web Accessibility Initiative's Images Tutorial, covering charts, diagrams and maps. It defines the **two-part text alternative**: a short description that identifies the image and a long description that carries the information.

**What it is good for.** What alt text for a chart should *contain*, and three HTML patterns for attaching a long description. Datawrapper's and the Urban Institute's alt-text rules implement it.

**What it does not settle.** The chart itself, only text alternatives for it. Not native SVG or canvas accessibility, screen-reader navigation of chart structure, keyboard interaction, contrast, or the other forty-nine heuristics [chartability.md](chartability.md) covers.

**How this was read.** The page at `w3.org/WAI/tutorials/images/complex/` was fetched and converted locally. Quotes are verbatim.

---

## The definition

> "Complex images contain substantial information -- more than can be conveyed in a short phrase or sentence. These are typically:
>
> - graphs and charts, including flow charts and organizational charts;
> - diagrams and illustrations where the page text relies on the user being able to understand the image;
> - maps showing locations or other information such as weather systems."

## The two-part pattern

> "In these cases, a two-part text alternative is required. The first part is the short description to identify the image and, where appropriate, indicate the location of the long description. The second part is the long description -- a textual representation of the essential information conveyed by the image."

The short description **identifies** and the long description **conveys**. A single long `alt` is not the pattern, and neither is a short `alt` with nothing behind it.

The worked example's short description:

> "Bar chart showing monthly and total visitors for the first quarter 2025 for sites 1 to 3"

Its long description covers:

> "detailed information, including scales, values, relationships and trends that are represented visually. For example, the long description can point out the declining values for site 1, consistent values for site 2, and increasing values for site 3 that are encoded in the bar chart."

**Scales, values, relationships, trends** is the most usable specification of long-description content in this corpus. A description that names the chart type and axes but not direction skips the last two.

## Composition can be part of the information

> "There are situations where the composition of an image is important and needs to be provided in the long description. For example, the sequence of colors used and the relative heights of the columns in a bar chart may be relevant information about the structure of the chart, in addition to the actual values and trends that it depicts."

So for the standard, "describe the data, not the visuals" is too simple: when the encoding carries meaning, the encoding is content. Datawrapper's article argues the opposite in passing ("if words are used instead to describe the data, there's no need to talk about visual elements at all"), then calls it a judgment call.

## Long descriptions as visible content

> "Complex images can be difficult to understand by many people -- especially those with low vision, learning disabilities, and limited subject-matter experience. Make long descriptions available to everyone to reach a wider audience with your content. For example, show the description as part of the main content. It may also be possible to reduce unnecessary complexity in your images and make them easier to understand for everyone."

A long description hidden in markup helps fewer people than the same text printed on the page. And a description that is hard to write points back at the chart's complexity.

> "It is also good practice to refer to and summarize more complex images from the accompanying text. For example, a reference such as 'The following graph shows that visitors were lost in the first quarter, but the numbers recovered in the second quarter' helps to point out the relevant information that the image is intended to present."

That example sentence is a takeaway title, the output inventory topic 37 also asks for.

## The three attachment patterns

Given a `chart.png` with a short `alt`:

1. **An adjacent link.** Universally supported, but "the link is not associated with the image in a semantic way." The upgrade wraps both in `<figure role="group">` with the link in `<figcaption>`.
2. **Location described inside `alt`**: `"...Described under the heading Site visitors full text."` The heading text has to stay accurate.
3. **`<figure>` containing both**, the description "presented as headings, text, and a table" in `<figcaption>`, with `role="group"` for backward compatibility.

`role="group"` recurs because `<figure>` semantics were historically inconsistent across browsers. `longdesc` is absent from the current tutorial.

## Plotting-library output

A PNG from matplotlib's `savefig()` has no `alt`, no `figcaption` and no page around it. The two-part pattern binds at publication, not at plotting.

- A figure bar can require that long-description content (scales, values, relationships, trends) **exists**, and check that a caption or docstring carries it.
- It cannot check the markup, which is downstream of the library. [inventory.md](../inventory.md) topic 71 frames it as mechanizable presence, judgment on content.

Urban bakes title, subtitle, source and notes into a single PNG and compensates with `alt` ([urban-institute.md](urban-institute.md)). That satisfies this page's two-part requirement and fails the broader "text should be real text" position (inventory topic 73). Neither source acknowledges the other.

## Evidence class

A **published standard**, not an experiment and not a design opinion. The inventory classes topic 71 as `evidence-backed` on that basis. That holds as long as "evidence-backed" is read as "there is an external, citable authority with a defined conformance test", not as "an experiment measured this working." The tutorial is normative guidance built on WCAG success criteria and reports no study.

## Where this source is used

Inventory topics 71 and 72. See [roll-call.md](../roll-call.md).

## Links

- [W3C WAI: Complex Images](https://www.w3.org/WAI/tutorials/images/complex/)
- [W3C WAI: Images Tutorial](https://www.w3.org/WAI/tutorials/images/)
- [An alt Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/)
- Related: [chartability.md](chartability.md): the other heuristics; [datawrapper-academy.md](datawrapper-academy.md): a worked implementation
