---
type: source
status: primary-read
retrieved: 2026-08-23
---

# BBC Visual and Data Journalism cookbook (and `bbplot`)

The BBC data team's recipe book for BBC News house-style graphics in R with ggplot2, plus the `bbplot` package it documents. Two functions carry the style: `bbc_style()` and `finalise_plot()`.

**What it is good for.** The clearest worked example in this wiki of house style as code rather than prose, with concrete numbers for typography and gridlines. Where the text is silent, the recipes' code shows the practice.

**What it does not settle.** It is a cookbook, not a style guide, and rarely says why. It is dated: the page header reads "Last updated: 2019-01-24". It covers only R, ggplot2 and newsroom output, with nothing on accessibility or uncertainty. No color palette is defined: "colours for lines in the case of a line chart or bars for a bar chart, do not come out of the box from the bbc_style() function, but need to be explicitly set."

**How this was read.** The cookbook at `bbc.github.io/rcookbook/` and the `bbc/bbplot` repository README were fetched and converted locally. Quotes are verbatim.

## The reason it exists

> "At the BBC data team, we have developed an R package and an R cookbook to make the process of creating publication-ready graphics in our in-house style using R's ggplot2 library a more reproducible process, as well as making it easier for people new to R to create graphics."

A newsroom with a design team and a written style still built a package, because a retyped style drifts. Urban shipped `urbnthemes` for the same reason ([urban-institute.md](urban-institute.md)), and matplotlib documents packaging a style for pip ([matplotlib.md](matplotlib.md)). Three unrelated organizations, one conclusion: for anything mechanical, config beats prose (inventory topic 79).

`bbplot` is not on CRAN. It installs with `devtools::install_github('bbc/bbplot')`.

## What `bbc_style()` sets

The cookbook prints the function body:

| Element | Value |
|---|---|
| Font family | `Helvetica` throughout |
| `plot.title` | size 28, bold, `#222222` |
| `plot.subtitle` | size 22 |
| `plot.caption` | blank |
| `axis.text` | size 18, `#222222` |
| `axis.title` | **blank** |
| `axis.ticks` | blank |
| `axis.line` | blank |
| `legend.position` | `top`, no title, no key background |
| `legend.text` | size 18 |
| `panel.grid.major.y` | `#cbcbcb` |
| `panel.grid.major.x` | blank |
| `panel.grid.minor` | blank |
| `panel.background` | blank |
| `strip.text` | size 22, left-aligned (`hjust = 0`) |

**Text size.** 28 / 22 / 18 at 640x450, far above any library default, a hard number for inventory topic 16 where Wilke says "chances are they are too small". The sizes fit a 640px web graphic; the ratio (title about 1.5x body) transfers.

**Gridlines.** One light gray set, horizontal, perpendicular to the measured variable, with no minor grid, axis line or ticks. Flipped bars invert it: "The default theme only has gridlines for the y axis. Add x gridlines with `panel.grid.major.x = element_line`." Every `coord_flip()` recipe pairs that with `panel.grid.major.y=element_blank()`. Inventory topic 66.

**Axis titles.** Blank by default. Wilke (inventory topic 17) wants a title with units on every axis: "it is a bad practice to make your readers guess what you mean". The BBC puts units in the subtitle: `title="Living longer"` / `subtitle="Life expectancy in Malawi 1952-2007"`. Adding titles back is the exception: "Our default theme has no axis titles, but you may wish to add them in manually."

The split is audience: a newsroom chart is read once, fast, and a research figure slowly, by someone who needs the units. Inventory topic 3 (audience and consumption context) thus changes other rules: a bar requiring axis titles flags every BBC chart.

## What `finalise_plot()` does, and why it is a separate function

> "finalise_plot(), the second function of the bbplot package, will left-align the title, subtitle and add the footer with a source and an image in the bottom right corner of your plot. It will also save it to your specified location."

Signature: `finalise_plot(plot_name, source, save_filepath, width_pixels = 640, height_pixels = 450, logo_image_path)`. The `source` argument is required, and "Source:" is typed into the value rather than supplied by the function: `source = "Source: ONS"`.

1. **The source line cannot be forgotten**, because export requires it (inventory topic 44).
2. **Export size is a named default**, 640x450, and the cookbook trusts the exported file over the IDE preview: "the position of the text and other elements do not render accurately in the RStudio Plots panel because this depends on the size and aspect ratio you want your plot to appear, so saving it out and opening up the files give you an accurate representation." Inventory topic 64.
3. **Styling and finishing are split**, theme in `bbc_style()` and production in `finalise_plot()`. Inventory topic 92 (function first, form next) as package architecture.

Margins for taller exports:

| height | top margin | bottom margin |
|---|---|---|
| 550px | 5 | 10 |
| 650px | 7 | 10 |
| 750px | 10 | 10 |
| 850px | 14 | 10 |

## The recipes as a corpus

**Zero baseline.** Almost every line, bar and area recipe includes `geom_hline(yintercept = 0, size = 1, colour="#333333")`. The BBC does not rely on the axis to communicate zero; it draws a visible rule at it. The aspect-ratio literature in [refutations.md](../refutations.md) is adjacent rather than corroborating: Talbot et al. found that "visible baselines can substantially mitigate errors made in slope judgments," but their baseline sat under each segment rather than at zero and helped only below 45 degrees.

**Gray plus one accent.**

```r
fill = ifelse(bar_df$country == "Mauritius", "#1380A1", "#dddddd")
```

One saturated blue for the subject, light gray for the other twelve. Inventory topic 29 has no controlled study behind it ([refutations.md](../refutations.md)), and a shipped recipe adds authority, not evidence.

**Sorting.** "By default, R will display your data in alphabetical order, but arranging it by size instead is simple: just wrap `reorder()` around the x or y variable." Inventory topic 57. Alphabetical order arrives when nobody chooses, which makes it a programmatic failure mode, not a design one.

## Small multiples

> "By default, faceting uses fixed axis scales across the small multiples. It's always best to use the same y axis scale across small multiples, to avoid misleading, but sometimes you may need to set these independently for each multiple, which we can do by adding the argument `scales = "free"`."

Inventory topic 62. The safe behavior is the default, and the deviation is visible in source as `free`. The fixed-scales example states the cost: "Oceania, with its relatively small population, has disappeared completely".

Legend recipes cover removing, repositioning, reversing, wrapping into rows, and spacing, including reversing order to match stack order (inventory topic 40).

## Limits

- **Dated.** 2019, ggplot2 of that era; one recipe still prints a deprecated-`size` idiom.
- **British spelling** (`colour`, `visualisation`), preserved in quotes.
- **No accessibility content**, though the output is web PNGs. [chartability.md](chartability.md) and [datawrapper-academy.md](datawrapper-academy.md) cover it.
- **No color palette.** Hex codes recur (`#1380A1` blue, `#FAAB18` yellow, `#990000` red, `#588300` green, `#dddddd` gray) but are never defined or justified as a palette.

## Where this source is used

Inventory topics 15, 16, 17, 18, 29, 39, 40, 42, 44, 47, 56, 57, 62, 64, 65, 66, 75, 79. This reading confirms that [roll-call.md](../roll-call.md) maps every cookbook heading.

## Links

- [BBC Visual and Data Journalism cookbook for R graphics](https://bbc.github.io/rcookbook/)
- [bbc/bbplot](https://github.com/bbc/bbplot)
- Related: [urban-institute.md](urban-institute.md): the same idea with a research audience
