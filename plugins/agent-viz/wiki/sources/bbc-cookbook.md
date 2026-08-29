---
type: source
status: primary-read
retrieved: 2026-08-23
---

# BBC Visual and Data Journalism cookbook (and `bbplot`)

A recipe book for producing BBC News house-style graphics in R with ggplot2, published by the BBC data team, plus the `bbplot` package it documents. Two functions carry the whole style: `bbc_style()` and `finalise_plot()`.

**How this was read.** The cookbook at `bbc.github.io/rcookbook/` and the `bbc/bbplot` repository README were fetched and converted locally, retrieved 2026-08-23. Quotes are verbatim.

**What it is good for.** The clearest worked example in this wiki of **house style as code rather than prose**, and the source of a specific, readable set of numbers for typography and gridline discipline. It is also useful as a corpus: nearly every recipe repeats the same handful of moves, so what the BBC actually does is recoverable from the code even where the text says nothing.

**What it does not settle.** It is a cookbook, not a style guide. It almost never explains *why*, and it is dated: the page header reads "Last updated: 2019-01-24". It is scoped to R and ggplot2, and to a newsroom's output. Nothing on accessibility. Nothing on uncertainty. No color palette is defined at all: "colours for lines in the case of a line chart or bars for a bar chart, do not come out of the box from the bbc_style() function, but need to be explicitly set."

---

## The reason it exists

Stated in the opening paragraph:

> "At the BBC data team, we have developed an R package and an R cookbook to make the process of creating publication-ready graphics in our in-house style using R's ggplot2 library a more reproducible process, as well as making it easier for people new to R to create graphics."

That is the finding, not the preamble. A newsroom with a design team and a written style already had both, and still built a package, because retyping a style does not hold. The Urban Institute reached the same conclusion independently and shipped `urbnthemes` (see [urban-institute.md](urban-institute.md)); matplotlib documents a mechanism for distributing a style inside a pip-installable package (see [matplotlib.md](matplotlib.md)). Three unrelated organizations, same conclusion: **for anything mechanical, config beats prose.** This is inventory topic 79, and it is the topic with the most independent corroboration in the entire inventory.

`bbplot` is not on CRAN; it installs from GitHub with `devtools::install_github('bbc/bbplot')`.

## What `bbc_style()` actually sets

The cookbook prints the function body, so the house style is readable as data rather than as description. The substantive settings:

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

As claims:

**Text is far larger than any default.** 28 / 22 / 18 in a graphic exported at 640x450. This is inventory topic 16, and the BBC's answer is a hard number rather than Wilke's "chances are they are too small". It is not transferable as-is (it is calibrated to a 640px web graphic) but the ratio is: title roughly 1.5x the body text, and body text much larger than any library default.

**Gridlines run perpendicular to the measured variable, and there is one set of them.** Horizontal only, in a single light gray, no minor grid, no axis line, no ticks. The cookbook confirms this is a deliberate default and shows the inversion for flipped bars: "The default theme only has gridlines for the y axis. Add x gridlines with `panel.grid.major.x = element_line`." Every `coord_flip()` recipe in the book pairs that with `panel.grid.major.y=element_blank()`. Inventory topic 66, shipped rather than described.

**Axis titles are blank by default.** This is a real disagreement with the rest of this wiki. Wilke's position (inventory topic 17) is that every axis carries a title with units, "it is a bad practice to make your readers guess what you mean". The BBC deletes them and puts the units in the subtitle instead: the recipes read `title="Living longer"` / `subtitle="Life expectancy in Malawi 1952-2007"`. The cookbook's own instructions treat re-adding them as the unusual case: "Our default theme has no axis titles, but you may wish to add them in manually."

Both positions are coherent, and they are coherent for different **audiences**. A newsroom chart is read once, fast, by a general reader who will not hunt for a units label; a research figure is read slowly by someone who needs the units to be unambiguous. This is one of the cleanest illustrations in the corpus that inventory topic 3 (audience and consumption context) is not decoration; it changes what other rules say. A bar that hard-codes "axis titles required" flags every BBC chart ever published.

## What `finalise_plot()` does, and why it is a separate function

> "finalise_plot(), the second function of the bbplot package, will left-align the title, subtitle and add the footer with a source and an image in the bottom right corner of your plot. It will also save it to your specified location."

Signature: `finalise_plot(plot_name, source, save_filepath, width_pixels = 640, height_pixels = 450, logo_image_path)`. The `source` argument is required, and the word "Source:" is typed into the value rather than supplied by the function: `source = "Source: ONS"`.

Three things are structural here:

1. **The source line cannot be forgotten,** because export is impossible without passing it. Inventory topic 44, enforced by an API signature rather than by a checklist.
2. **Export size is a named default,** 640x450, and the cookbook insists on the exported file rather than the IDE preview: "the position of the text and other elements do not render accurately in the RStudio Plots panel because this depends on the size and aspect ratio you want your plot to appear, so saving it out and opening up the files give you an accurate representation." Inventory topic 64.
3. **Styling and finishing are split.** `bbc_style()` is theme; `finalise_plot()` is production. Inventory topic 92 (function first, form next) as package architecture.

There is even a margin table for taller exports, which is the kind of detail that only exists because somebody shipped a broken chart:

| height | top margin | bottom margin |
|---|---|---|
| 550px | 5 | 10 |
| 650px | 7 | 10 |
| 750px | 10 | 10 |
| 850px | 14 | 10 |

## The recipes as a corpus

Three patterns repeat across nearly every example and are more informative than the prose.

**A zero baseline is drawn explicitly.** Almost every line, bar, and area recipe includes `geom_hline(yintercept = 0, size = 1, colour="#333333")`. The BBC does not rely on the axis to communicate zero; it draws a visible rule at it. This is quietly corroborated from an unrelated direction by the aspect-ratio literature in [refutations.md](../refutations.md), where Talbot et al. found that "visible baselines can substantially mitigate errors made in slope judgments."

**Gray plus one accent, as code.** The conditional-color recipe:

```r
fill = ifelse(bar_df$country == "Mauritius", "#1380A1", "#dddddd")
```

One saturated blue for the subject, light gray for the other twelve. This is inventory topic 29 in its most literal form. The same topic has **no controlled study behind it** ([refutations.md](../refutations.md)); the BBC shipping it as a recipe is more authority, not evidence.

**Sorting is treated as a bug fix.** "By default, R will display your data in alphabetical order, but arranging it by size instead is simple: just wrap `reorder()` around the x or y variable." Inventory topic 57, and this is the framing that makes it a *programmatic* failure mode rather than a design one: nobody chooses alphabetical order, it is what arrives in the absence of a choice.

## Small multiples

> "By default, faceting uses fixed axis scales across the small multiples. It's always best to use the same y axis scale across small multiples, to avoid misleading, but sometimes you may need to set these independently for each multiple, which we can do by adding the argument `scales = "free"`."

Inventory topic 62. Two useful properties: the safe behavior is the default, and freeing scales requires typing the word `free`, so the deviation is visible in the source. The cookbook shows a free-scales example and narrates the cost ("Oceania, with its relatively small population, has disappeared completely" in the fixed version), which is honest about why anyone reaches for it.

The legend section covers removing, repositioning, reversing order, rearranging into rows, and spacing. Reversing legend order to match stack order (inventory topic 40) is a named recipe, which again suggests it is a mistake somebody kept making.

## Limits

- **Dated.** 2019, ggplot2 of that era, and one recipe still prints a deprecated-`size` idiom. The style is stable; the code is not necessarily current.
- **British spelling throughout** (`colour`, `visualisation`). Quotes above preserve it; prose elsewhere in this wiki uses American spelling.
- **No accessibility content at all.** No contrast floor, no colorblind guidance, no alt text, despite the output being web-published PNGs. [chartability.md](chartability.md) and [datawrapper-academy.md](datawrapper-academy.md) cover that ground.
- **No color palette.** The hex codes recur across recipes (`#1380A1` blue, `#FAAB18` yellow, `#990000` red, `#588300` green, `#dddddd` gray) but are never defined as a palette or justified.

## Where this source is used

Inventory topics 15, 16, 17, 18, 29, 39, 40, 42, 44, 47, 56, 57, 62, 64, 65, 66, 75, 79. [roll-call.md](../roll-call.md) records every cookbook heading as mapped, which this reading confirms.

## Links

- [BBC Visual and Data Journalism cookbook for R graphics](https://bbc.github.io/rcookbook/)
- [bbc/bbplot](https://github.com/bbc/bbplot)
- Related: [urban-institute.md](urban-institute.md), the same idea with a research audience
