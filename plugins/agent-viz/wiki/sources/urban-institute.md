---
type: source
status: primary-read
retrieved: 2026-08-23
author: jonathan-schwabish
---

# Urban Institute Data Visualization Style Guide

The Urban Institute's public data visualization style guide, covering typography, color, chart parts, chart-type selection, an explicit list of prohibitions, an accessibility section, and guidance on visualizing data about people. It is paired with two shipped tools: an Excel macro add-in and `urbnthemes`, an R package.

**How this was read.** The full guide at `urbaninstitute.github.io/graphics-styleguide/` and the `UrbanInstitute/urbnthemes` README were fetched and converted locally, retrieved 2026-08-23. Quotes are verbatim.

**Authorship: this guide is not independent of [Jonathan Schwabish](../people/jonathan-schwabish.md).** The guide carries no byline, but its Additional Resources section names him as its sole point of contact ("Contact Jon Schwabish", `jschwabish@urban.org`, live page text verified 2026-08-25), and he is a Senior Fellow at Urban. **This guide and Schwabish are not two sources for the same claim.** One such double-count has already been corrected, in [schwabish.md](schwabish.md).

**What it is good for.** The **broadest** single source in this corpus. It is the only one that covers chart parts, color, prohibitions, accessibility, tables, maps, and the ethics of ordering people-groups in one document, from an organization that publishes research rather than journalism. It is also the source with the most quotable one-liners, which is why it appears against more inventory topics than anything except Wilke.

**What it does not settle.** It is written for Urban staff and says so; some of it is procurement and Word-template mechanics. Nothing in it is evidence-backed on its own authority; where it is right about something measured (WCAG contrast, for instance) it is citing a standard, not reporting a result. And its accessibility section is a compliance posture, not an audit method. For that, see [chartability.md](chartability.md).

---

## Should this be a chart at all

The guide opens the best-practices section by arguing against charts, which is rarer than it should be:

> "Although charts are great for communicating data, they are not the appropriate tool for every situation. If you find explanatory sentences do a better job of distilling the information you want to convey, consider going without a chart. If your main goal is to present detailed information as opposed to showing patterns, or if it's important that the reader can accurately determine the values of your data, consider using a table instead. You may also find that simply including a single, large number (commonly known as 'big aggregate numbers') may be sufficient."

Inventory topic 4. The split is three-way: sentence, table, or big number. It gives a criterion, too, which most sources do not: **patterns argue for a chart, accurate value retrieval argues for a table.**

## The "Data Visualization Absolutes"

Four prohibitions, framed as things the institute avoids rather than as universal law: "there are certain data visualization practices that we avoid."

**Nonzero baselines.**

> "The axis in bar charts (whether vertical or horizontal) should always start at zero. The gaps between bars are overemphasized when the value axis starts at something other than zero."

with a stated escape hatch and a stated scope limit, both of which matter:

> "When small differences between bars are important to show but a zero axis makes those differences difficult for the reader to see, consider adjusting the data to show percent change, difference, or some other similar adjustment. It is important to note that other charts types that do not use length or height as the primary encoding -- including, for example, scatterplots and line charts -- do not necessarily need to start at zero."

That is proportional ink, correctly scoped to length and height encodings. It is narrower than Vega-Lite's default, which forces zero on every quantitative x/y scale regardless of mark ([vega-lite.md](vega-lite.md)), and it matches Observable Plot's reasoning, which forces zero only where area encodes the value ([observable-plot.md](observable-plot.md)). Datawrapper reaches the same place and enforces it in the product ([datawrapper-academy.md](datawrapper-academy.md)).

**Dual axis charts.**

> "Charts that have two axes -- where one series is tagged to one axis and another series is tagged to another, parallel axis -- should be avoided. These kinds of charts are confusing, difficult to read, and are often misleading."

**This is now a softer rule than the version quoted in [inventory.md](../inventory.md).** The current text names remedies (multiple graphs, percent change, connected scatterplot) and then two explicit exceptions:

> "(There are two exceptions to this rule: charts that show the translation of a single measure such as Fahrenheit and Celsius temperatures; and the Pareto chart, which shows individual values as bars and a line showing the cumulative sum.)"

Both exceptions are cases where the two axes are not independent variables: one is a unit conversion of the other, and the other is a cumulative function of the other. That is a principled line, and a better rule than the flat ban. It also sits well with [refutations.md](../refutations.md), which finds no experiment supporting a flat ban. The parenthesis belongs with any citation of Urban for "never use two axes."

Elsewhere the guide states the practice as an editorial fact rather than a rule, which is the honest form: connected scatterplots are "a clearer substitute for dual-axis line charts, which Urban does not publish."

**Pie charts with too many slices,** and this entry is unusually candid about its own status:

> "This advice is purposely left unclear. There is no specific 'rule' about how many slices are too many slices in a pie chart, but the general recommendation is to keep the overall number of slices in pie charts to fewer than 5."

Elsewhere: "Pie charts should always add up to 100 percent" (inventory topic 54).

**Too many categories.**

> "our standard is to keep the number of categories in any graph to fewer than seven."

Same cap as seaborn's "more than a handful" and Datawrapper's seven, and none of the three has a study behind it. Inventory topic 28.

## Chart parts, and the text-case convention

The guide fixes conventions that are trivially mechanizable and almost always inconsistent in practice:

> "Titles use headline/title case, and subtitles use sentence case; all titles are left aligned."
>
> "All text within the figure uses sentence-style capitalization."

And it fixes what a chart must have:

> "Urban charts require a title, source line, and axis or other labels identifying the elements and units of the chart."

with a nice unit-duplication rule: "The unit of measurement should be mentioned only once, either in the subtitle or the y-axis label."

On titles it gives the canonical before/after, which is the most useful form this advice takes:

> "instead of a purely descriptive title, such as 'Labor Force Participation Rate, Men and Women, 1950-2024,' a more active title would be 'The Labor Force Participation Rate Has Declined for Men and Increased for Women.'"

Inventory topic 37. The negative case is regex-detectable; the positive case is judgment.

On legends, three separate rules in one bullet: stretch across the top, "Order the series in the legend in a logical way, mirroring the order of the data in the chart", and "When possible, directly label the data in the chart and omit the legend." Topics 39 and 40.

Source and notes are required and specified: every figure gets a source line, notes "should also define all acronyms and abbreviations used within the figure", asterisks are reserved for significance levels. Topics 44 and 45.

## Color, highlighting, consistency

Four palette classes, matched to data type, in the same taxonomy every other source uses (categorical, sequential, diverging, binary). The diverging entry carries a rule most guides omit: "The center of the diverging palette should always be labeled to avoid confusing the reader." Topic 32.

Highlighting is stated twice, once as a technique and once as a caution:

> "consider a line chart with all 50 US states -- you could use gray for the majority of states and add color to just the few you want to highlight."
>
> "The observations you want the reader to focus on should be rendered in a color that helps them stand out (usually pink or yellow at Urban), while the rest of the series are in a different color (usually blue, black, or gray). However, be selective with your use of color to highlight specific values, series, or observations, because too many colors can make it difficult to pick out the values on which you want your reader to focus."

Urban's palette hierarchy has a shape: cyan, gray, black as main colors, with yellow and magenta as **highlight-only** secondaries used "sparingly". The emphasis palette is a property of the palette, not of the individual chart.

And consistency across a set: "Once you've chosen blue to represent one group in one chart, make sure all other charts in your publication or slide deck use blue to represent that group as well." Topic 30.

## Accessibility

Urban's section is compliance-shaped: Section 508 of the Rehabilitation Act plus WCAG 2.0 Level AA. It is precise where it matters.

**Contrast, with the actual numbers:**

> "Web Content Accessibility Guidelines (WCAG) 2.0 Level AA requires the contrast ratio of the luminance (think: brightness) of two colors to be 4.5:1 for normal text and 3:1 for large text. A higher level of contrast (Level AAA), requires a contrast ratio of 7:1 for normal text and 4.5:1 for large text. Large text is defined as 14 point (typically 18.66px) and bold or larger, or 18 point (typically 24px) or larger. **Text standards also apply to text in graphics, such as data labels in a chart or text boxes in a logic model.**"

That last sentence is the one that makes this actionable for figures rather than for web pages. Datawrapper publishes a *softer* chart-specific floor (2.5 for big text, 4 for small); the two disagree, and a bar has to pick one. Chartability picks the WCAG numbers and adds the 3:1 non-text floor for marks.

**Alt text**, with the best one-line definition in the corpus:

> "Alternative text should present the content and function, not necessarily a description, of an image. If you had to remove the image, what text would you put in its place?"

Plus the decorative-image rule: empty alt, and specifically "You should not put empty spaces, empty quotes (except in HTML `alt=""`), or any other nonsense information in these fields."

**Redundant encoding is offered as an accessibility override.** That is a guide admitting its own aesthetic preference has a cost:

> "This style guide promotes clean design and graphs that are free of extraneous colors, but when communicating data to readers with accessibility needs, additional encodings may be important."

**Tables:** "Tables that meet accessibility requirements cannot have any merged cells, blank cells, blank rows, or blank columns, as screen readers have a difficult time with spanner headings and blank cells." Real, tedious, and rarely stated.

### The unresolved conflict about live text

For web products, "all text is included in a single image (e.g., PNG) file." That is a deliberate decision **against** live, selectable, screen-reader-native chart text, compensated for with alt text. It is a real disagreement with the general accessibility position (inventory topic 73), and the guide does not acknowledge it as one. A bar that ignores the conflict will review inconsistently.

## Data about people

The section on race, ethnicity, and gender is short and is the part of this guide with the least competition anywhere else.

> "Many graphs and tables encode data by demographic group. Graph producers should take an active role in choosing how to order and present data values for different groups. Urban does not have universal rules about ordering demographic data in visuals, but a few considerations can help you make decisions about order."

and on palettes:

> "Urban tries not to use color palettes that reinforce gender or racial stereotypes (e.g., pink for women and blue for men). Furthermore, researchers should avoid using colors associated with skin tones."

Inventory topics 36, 57, 90. The framing is the contribution: ordering is an **editorial choice** that someone makes whether or not they notice, which is the same insight as the alphabetical-sort failure mode, arrived at from an ethical direction instead of a technical one.

## Two tools, same finding as the BBC

> "The Urban Institute Excel Macro add-in and the Urban styles package for R (urbnthemes) are two open source tools Urban staff can use to more easily create and format their data visualizations for different publication types. **Both tools automate much of the information in this guide,** including applying formatting conventions for charts created in Urban style."

`urbnthemes` ships `set_urbn_defaults(style = "print")`, `theme_urbn_print()`, `theme_urbn_map()`, plus helpers that encode individual guide rules as functions: `remove_ticks()`, `scatter_grid()`, `urbn_source()`, `urbn_note()`, `urbn_logo_text()`. Font handling is a first-class problem with its own test (`lato_test()`) and installer (`lato_import()`).

Same pattern as `bbplot` ([bbc-cookbook.md](bbc-cookbook.md)): a written guide, then a package, because the guide alone did not hold. Urban is honest about the ceiling, though, in a way the BBC is not:

> "library(urbnthemes) makes ggplot2 output align more closely with this style guide, but it does not produce publication-ready graphics. Visual styles must still be edited using your project's normal editing workflow."

A theme covers the mechanizable part. It does not cover the judgment part. That split is the same one the floor-and-ceiling idea makes about review.

## Where this source is used

Inventory topics 4, 5, 9, 13, 21, 22, 23, 28, 29, 30, 32, 33, 36, 37, 38, 39, 41, 43, 44, 45, 47, 53, 54, 55, 57, 62, 68, 71, 73, 79, 80, 86, 90. See [roll-call.md](../roll-call.md).

**One correction:** the roll-call and inventory record the dual-axis rule as a flat ban. The current text states two exceptions, so topic 13 is out of date against the primary.

## Links

- [Urban Institute Data Visualization Style Guide](https://urbaninstitute.github.io/graphics-styleguide/)
- [UrbanInstitute/urbnthemes](https://github.com/UrbanInstitute/urbnthemes)
- Related: [bbc-cookbook.md](bbc-cookbook.md), [chartability.md](chartability.md), [datawrapper-academy.md](datawrapper-academy.md)
