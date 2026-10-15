---
type: source
status: primary-read
retrieved: 2026-08-23
author: jonathan-schwabish
---

# Urban Institute Data Visualization Style Guide

The Urban Institute's public style guide for typography, color, chart parts, chart-type selection, prohibitions, accessibility, and data about people. It ships with an Excel macro add-in and `urbnthemes`, an R package. The guide has no byline, but its Additional Resources section names [Jonathan Schwabish](../people/jonathan-schwabish.md), a Senior Fellow at Urban, as its sole contact ("Contact Jon Schwabish", `jschwabish@urban.org`). It and [Schwabish](schwabish.md) are one source, not two, for any claim they share.

**What it is good for.** The broadest single source in this corpus. One document covers chart parts, color, prohibitions, accessibility, tables, maps, and the ethics of ordering people-groups, from a research organization rather than a newsroom. It is also the most quotable.

**What it does not settle.** It is written for Urban staff, and some of it is procurement and Word-template mechanics. Nothing in it is evidence-backed on its own authority. Where it is right about something measured, such as WCAG contrast, it is citing a standard. Its accessibility section is a compliance posture, not an audit method; see [chartability.md](chartability.md).

**How this was read.** The full guide at `urbaninstitute.github.io/graphics-styleguide/` and the `UrbanInstitute/urbnthemes` README were fetched and converted locally. Quotes are verbatim. The Schwabish contact line was checked against the live page text.

## Should this be a chart at all

> "Although charts are great for communicating data, they are not the appropriate tool for every situation. If you find explanatory sentences do a better job of distilling the information you want to convey, consider going without a chart. If your main goal is to present detailed information as opposed to showing patterns, or if it's important that the reader can accurately determine the values of your data, consider using a table instead. You may also find that simply including a single, large number (commonly known as 'big aggregate numbers') may be sufficient."

Inventory topic 4. The choice is sentence, table, or big number, with a criterion most sources lack: patterns argue for a chart, accurate value retrieval for a table.

## The "Data Visualization Absolutes"

Four prohibitions, framed as house practice: "there are certain data visualization practices that we avoid."

**Nonzero baselines.**

> "The axis in bar charts (whether vertical or horizontal) should always start at zero. The gaps between bars are overemphasized when the value axis starts at something other than zero."

> "When small differences between bars are important to show but a zero axis makes those differences difficult for the reader to see, consider adjusting the data to show percent change, difference, or some other similar adjustment. It is important to note that other charts types that do not use length or height as the primary encoding -- including, for example, scatterplots and line charts -- do not necessarily need to start at zero."

Proportional ink, scoped to length and height. That is narrower than Vega-Lite's default of zero on every quantitative x/y scale ([vega-lite.md](vega-lite.md)) and matches Observable Plot, which forces zero only where area encodes the value ([observable-plot.md](observable-plot.md)). Datawrapper enforces the same rule in the product ([datawrapper-academy.md](datawrapper-academy.md)).

**Dual axis charts.**

> "Charts that have two axes -- where one series is tagged to one axis and another series is tagged to another, parallel axis -- should be avoided. These kinds of charts are confusing, difficult to read, and are often misleading."

The current text is not a flat ban. It names remedies (multiple graphs, percent change, connected scatterplot) and two exceptions:

> "(There are two exceptions to this rule: charts that show the translation of a single measure such as Fahrenheit and Celsius temperatures; and the Pareto chart, which shows individual values as bars and a line showing the cumulative sum.)"

In both, one axis is a function of the other (a unit conversion, a cumulative sum). [refutations.md](../refutations.md) finds no experiment supporting a flat ban, so a citation of Urban for "never use two axes" needs the parenthesis. Elsewhere connected scatterplots are "a clearer substitute for dual-axis line charts, which Urban does not publish."

**Pie charts with too many slices.**

> "This advice is purposely left unclear. There is no specific 'rule' about how many slices are too many slices in a pie chart, but the general recommendation is to keep the overall number of slices in pie charts to fewer than 5."

Also: "Pie charts should always add up to 100 percent" (inventory topic 54).

**Too many categories.**

> "our standard is to keep the number of categories in any graph to fewer than seven."

Same cap as seaborn's "more than a handful" and Datawrapper's seven, and none of the three has a study behind it. Inventory topic 28.

## Chart parts, and the text-case convention

> "Titles use headline/title case, and subtitles use sentence case; all titles are left aligned."
>
> "All text within the figure uses sentence-style capitalization."

> "Urban charts require a title, source line, and axis or other labels identifying the elements and units of the chart."

Units appear once: "The unit of measurement should be mentioned only once, either in the subtitle or the y-axis label."

> "instead of a purely descriptive title, such as 'Labor Force Participation Rate, Men and Women, 1950-2024,' a more active title would be 'The Labor Force Participation Rate Has Declined for Men and Increased for Women.'"

Inventory topic 37. A descriptive title is regex-detectable; an active one takes judgment.

Legends stretch across the top, and "Order the series in the legend in a logical way, mirroring the order of the data in the chart", and "When possible, directly label the data in the chart and omit the legend." Topics 39 and 40.

Every figure gets a source line. Notes "should also define all acronyms and abbreviations used within the figure". Asterisks are reserved for significance levels. Topics 44 and 45.

## Color, highlighting, consistency

Four palette classes: categorical, sequential, diverging, binary. The diverging entry adds a rule most guides omit: "The center of the diverging palette should always be labeled to avoid confusing the reader." Topic 32.

> "consider a line chart with all 50 US states -- you could use gray for the majority of states and add color to just the few you want to highlight."
>
> "The observations you want the reader to focus on should be rendered in a color that helps them stand out (usually pink or yellow at Urban), while the rest of the series are in a different color (usually blue, black, or gray). However, be selective with your use of color to highlight specific values, series, or observations, because too many colors can make it difficult to pick out the values on which you want your reader to focus."

The main colors are cyan, gray and black. Yellow and magenta are highlight-only, used "sparingly", so emphasis is built into the palette rather than chosen per chart.

Across a set: "Once you've chosen blue to represent one group in one chart, make sure all other charts in your publication or slide deck use blue to represent that group as well." Topic 30.

## Accessibility

Section 508 of the Rehabilitation Act plus WCAG 2.0 Level AA.

**Contrast.**

> "Web Content Accessibility Guidelines (WCAG) 2.0 Level AA requires the contrast ratio of the luminance (think: brightness) of two colors to be 4.5:1 for normal text and 3:1 for large text. A higher level of contrast (Level AAA), requires a contrast ratio of 7:1 for normal text and 4.5:1 for large text. Large text is defined as 14 point (typically 18.66px) and bold or larger, or 18 point (typically 24px) or larger. **Text standards also apply to text in graphics, such as data labels in a chart or text boxes in a logic model.**"

The last sentence extends the standard to chart text. Datawrapper publishes a softer chart-specific floor (2.5 for big text, 4 for small), so a bar has to pick one. Chartability uses the WCAG numbers and adds a 3:1 non-text floor for marks.

**Alt text.**

> "Alternative text should present the content and function, not necessarily a description, of an image. If you had to remove the image, what text would you put in its place?"

Decorative images get empty alt: "You should not put empty spaces, empty quotes (except in HTML `alt=""`), or any other nonsense information in these fields."

**Redundant encoding** overrides the guide's own minimalism:

> "This style guide promotes clean design and graphs that are free of extraneous colors, but when communicating data to readers with accessibility needs, additional encodings may be important."

**Tables.** "Tables that meet accessibility requirements cannot have any merged cells, blank cells, blank rows, or blank columns, as screen readers have a difficult time with spanner headings and blank cells."

### The unresolved conflict about live text

For web products, "all text is included in a single image (e.g., PNG) file." That rules out live, screen-reader-native chart text in favor of alt text. It conflicts with the general accessibility position (inventory topic 73), and the guide does not acknowledge the conflict, so a bar that ignores it will review inconsistently.

## Data about people

> "Many graphs and tables encode data by demographic group. Graph producers should take an active role in choosing how to order and present data values for different groups. Urban does not have universal rules about ordering demographic data in visuals, but a few considerations can help you make decisions about order."

> "Urban tries not to use color palettes that reinforce gender or racial stereotypes (e.g., pink for women and blue for men). Furthermore, researchers should avoid using colors associated with skin tones."

Inventory topics 36, 57, 90. Ordering is an editorial choice made whether or not anyone notices it, which is the alphabetical-sort failure mode seen from the ethical side. Few other sources cover this.

## Two tools, same finding as the BBC

> "The Urban Institute Excel Macro add-in and the Urban styles package for R (urbnthemes) are two open source tools Urban staff can use to more easily create and format their data visualizations for different publication types. **Both tools automate much of the information in this guide,** including applying formatting conventions for charts created in Urban style."

`urbnthemes` ships `set_urbn_defaults(style = "print")`, `theme_urbn_print()`, `theme_urbn_map()`, and one-rule helpers: `remove_ticks()`, `scatter_grid()`, `urbn_source()`, `urbn_note()`, `urbn_logo_text()`. Fonts get a test (`lato_test()`) and an installer (`lato_import()`).

This is the `bbplot` pattern ([bbc-cookbook.md](bbc-cookbook.md)): a guide, then a package, because the guide alone did not hold. Unlike the BBC, Urban states the ceiling:

> "library(urbnthemes) makes ggplot2 output align more closely with this style guide, but it does not produce publication-ready graphics. Visual styles must still be edited using your project's normal editing workflow."

A theme covers the mechanizable part, not the judgment part, the same split the floor-and-ceiling idea makes about review.

## Where this source is used

[Inventory](../inventory.md) topics 4, 5, 9, 13, 21, 22, 23, 28, 29, 30, 32, 33, 36, 37, 38, 39, 41, 43, 44, 45, 47, 53, 54, 55, 57, 62, 68, 71, 73, 79, 80, 86, 90. See [roll-call.md](../roll-call.md).

## Links

- [Urban Institute Data Visualization Style Guide](https://urbaninstitute.github.io/graphics-styleguide/)
- [UrbanInstitute/urbnthemes](https://github.com/UrbanInstitute/urbnthemes)
- Related: [bbc-cookbook.md](bbc-cookbook.md), [chartability.md](chartability.md), [datawrapper-academy.md](datawrapper-academy.md)
