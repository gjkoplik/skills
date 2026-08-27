---
type: source
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Datawrapper Academy

The help documentation for Datawrapper, a browser-based charting tool used widely in newsrooms. Unlike the other style guides here, Datawrapper's advice is backed by a product that can refuse to do the wrong thing, and in at least one case it does.

**How this was read.** Seven articles were fetched and converted locally, retrieved 2026-08-23:

| Article | ID |
|---|---|
| What to consider when choosing colors for data visualization | 140 |
| How we make sure our charts, maps and tables are accessible | 206 |
| How to write good alternative descriptions for your data visualization | 330 |
| Why our column and bar charts start at zero (or below) | 326 |
| How to create a dual-axis chart | 431 |
| Number formats you can display in Datawrapper | 207 |
| How to resize your visualizations | 390 |

Quotes are verbatim from those. The Academy is large and the rest of it was not read.

**What it is good for.** Two things nothing else in this corpus covers seriously: **number formatting and locale**, and **responsive rendering at phone width**. Also the best short guide to color-as-encoding, and the clearest statement of the gray-as-context idea.

**What it does not settle.** Every claim is authority-asserted house practice, and the guidance is bound to a hosted product with a fixed feature set. Some of it (plot-height sliders, embed flags) does not transfer to a plotting library at all. Its contrast floor is **softer than WCAG** and conflicts with the other accessibility sources here.

---

## Color: twelve numbered rules

Article 140 is a numbered list, which makes it easy to check a chart against. The ones that carry weight:

**Gray is the important color.**

> "Using grey for less important elements in your chart makes your highlight colors (which should be reserved for your most important data points) stick out even more. Grey is also helpful for general context data, less important annotations, to show what's unselected by the user, or to calm down the overall visual impression of your charts. Since grey can seem a bit cold, consider using it with a hint of color: Try a warm grey (grey+yellow/orange/red), or use another very light color as an alternative (e.g. super light yellow)."

Inventory topic 29. The warm-gray detail is the practical part and appears nowhere else in this corpus. Note again that this rule has **no controlled study behind it** ([refutations.md](../refutations.md)); it is a good default with three independent style guides behind it and zero experiments.

**Every mark gets explained.**

> "Every visual mark that represents a value or variable should be explained: What does the height of your bar mean? What does the size of your circles on a symbol map represent? The same is true for colors."

Inventory topic 42, and the best phrasing of it, because it generalizes past color to any mapped channel.

**Do not cross palette class with data type**, stated with the mechanism rather than as a rule:

> "It might be tempting to use shades of one hue (e.g. blue) even for categories, to make your chart look less colorful. However, since many readers will associate dark colors with 'more/high' and bright colors with 'less/low', such a color palette will imply a ranking of your categories."

**Lightness, not hue, builds a gradient,** with a grayscale check attached: "Your gradient should work in black and white, too. Gradients with many variations in lightness (like rainbow scales) can confuse readers." Same conclusion as matplotlib, argued in one sentence.

**Diverging midpoints should be light gray, not white.** A small, specific, rarely-stated detail.

**Intuitive color, with a named exception for gender:**

> "When it comes to color-encoding gender data, consider avoiding the stereotypical pink-blue combination. To not confuse your readers entirely, try a cold color for men (e.g. blue or purple) and a warmer color for women (e.g. yellow, orange or a warm green)."

Same position as the Urban Institute ([urban-institute.md](urban-institute.md)), and both are careful to give a replacement rather than only a prohibition.

**Seven colors, again.** "If you need more than seven colors in a chart, consider using another chart type or to group categories together." Third independent source with the same cap and no study behind any of them.

**Consider whether color should encode the value at all:**

> "Consider showing your most important values with bars, position (like in a dot plot), or even areas, and use colors to only show categories."

That is channel-effectiveness ranking (inventory topic 6) offered as a first move rather than as theory.

### The contrast conflict

> "The contrast ratio between background and foreground should be at least 2.5 for big text and at least 4 for small text. In addition to having a high contrast ratio, avoid complementary hues (e.g. red and green, orange and blue) and bright colors for backgrounds."

WCAG 2.0 AA is 4.5:1 for normal text and 3:1 for large text and for graphical objects. Datawrapper's numbers are lower on both. This is a genuine disagreement between two sources in this wiki, both of which a figure bar might cite, and **it has to be resolved explicitly rather than averaged.** The recommendation here is to use the WCAG numbers, because they are a published standard and because Chartability, the only peer-reviewed accessibility source in the corpus, uses them ([chartability.md](chartability.md)). Datawrapper's floor is a chart-specific softening with no stated derivation.

## Zero baselines, enforced by the product

Article 326 is unusual: a help article explaining why a feature does not exist.

> "Truncated y-axes in column charts and bar charts are considered deceptive and misleading. And there's research backing that up."
>
> "We have a responsibility towards your readers -- we don't want them to be misled. That's why Datawrapper doesn't allow you to begin your y-axis at something greater than zero."

Two things to note carefully.

**The citation is sound, and it matters which part of the paper it uses.** Datawrapper cites Pandey et al., CHI 2015, and quotes "participants who saw the deceptive visualization perceived the underlying message in its exaggerated form" and that these techniques "do lead to major misinterpretation from the reader's side and that the effects are also rather large." [refutations.md](../refutations.md) documents that this same paper contradicts itself in its Discussion section about the inverted-axis condition, misreporting a 2.5% control error rate as 18.4%. Datawrapper does not touch the broken passage. Its citation is on the sound part of the paper, and the effect-size claim it quotes recomputes correctly from Table 2.

**The remedies are better than the rule.** The article lists three alternatives to truncation rather than just refusing:

- A dot or range plot, with the reasoning stated: "Readers don't expect dot plots (or, for two values, range plots) to start at zero because there's no filled bar or column that would indicate that." Proportional ink, correctly derived from the mark rather than from the axis.
- A line chart, if the categories are ordered.
- Plot the differences between the bars instead of the values.

That is the shape a quality bar should copy. A rule that only prohibits produces truncated bars with a rationalization attached; a rule that supplies three replacements produces a different chart.

## And yet: Datawrapper now ships a dual-axis chart

Article 431 walks through building one, and "Dual-axis & Waterfall Charts" is a top-level category in the Academy's navigation. The feature is on the Business plan.

> "Dual-axis charts combine two vertical axes with differing units or scales into a single chart with one, shared horizontal axis, and also known double Y chart, combo charts, superimposed charts, or mixed line-and-bar series."

and, on the data:

> "The values do not have to be of the same measure (in our examples, rainfall in mm and temperature in degree Celcius) -- in fact, your dual-axis chart will be easiest to understand if they're not."

This matters for the wiki's bookkeeping. [inventory.md](../inventory.md) topic 13 cites Datawrapper among the practitioner sources behind a flat dual-axis ban, and [refutations.md](../refutations.md) already finds no experiment supporting one. Datawrapper, which is willing to hard-block a feature it thinks is deceptive, **built this one on purpose.** Set that against the fact that it refuses to let you truncate a bar axis and the contrast is informative: the same organization treats truncation as a bright line and dual axes as a design tool with a caveat.

That caveat inverts the usual worry. The danger of a twin axis is spurious apparent correlation; Datawrapper's advice is that *unrelated units* make it safer, not more dangerous, because nobody mistakes millimeters of rain for degrees Celsius.

## Number formats and locale

Article 207 is the only serious treatment of number formatting in this entire corpus, and inventory topic 18 names it as one of the most common visible defects in machine-generated figures.

The format tokens are a compact vocabulary worth stealing conceptually even outside Datawrapper:

| Token | Effect |
|---|---|
| `0.0` | fixed decimal places, even when zero |
| `0.[0]` | maximum decimal places, shown only if non-zero |
| `0,0` | group thousands |
| `0;0` | group thousands only from 10,000 up |
| `0a` | abbreviate thousands (`7000` to `7k`) |
| `0%` | percent sign |
| `(0)` | negatives in parentheses |
| `+0` | plus sign on positives |
| `\|0\|` | strip the minus sign |
| `$0` | currency symbol |

Two design ideas in there are the actual contribution.

**The `[]` convention separates "how many decimals do I allow" from "how many do I insist on".** `0.[00]` renders `0.061` as `0.06` and `1600` as `1600`, not `1600.00`. That is significant-digit discipline (inventory topic 18) expressed as a format string. Nothing in matplotlib's formatter vocabulary does this in one token.

**Locale is a property of the output, not the format.** Both the decimal mark and the thousands separator "depend on the output locale (language) you choose for your visualization", and so does the currency symbol. Inventory topic 19. Getting this right means the format string says *group thousands* and the renderer decides whether that means `1,000` or `1.000`, which is the only design that survives translation.

## Responsive sizing

Article 390 supplies the number the inventory quotes, and the framing behind it:

> "Embedded visualizations are fully responsive. That means that the width of your embedded visualization adapts smoothly to the width of your reader's screen. If your visualization gets embedded, the width can't be defined; it depends on the device the visualization is viewed on. **On mobile screens, your chart might only be 380px or 400px wide, while on a big computer screen, it might be 700px wide.**"

and, more sharply:

> "You don't actually set a width for your visualization; the width gets set by your reader's screen size."

The most transferable idea in the article is the **plot height versus chart height** distinction:

> "The plot is the chart area without header, footer, color key, or annotations. In Datawrapper, you set a height for the plot instead of the full chart. That's because on mobile screens, a long title, footer, or annotations shown as a key would otherwise 'eat away' the space for the actual chart."

Anyone who has watched a long title consume half a `figsize` will recognize the problem. Height is then either fixed pixels or an aspect ratio derived from width, which is the responsive version of inventory topic 14.

The article also documents which chart types cannot have their height set at all, because the data determines it: bar charts, dot plots, range plots, arrow plots, and tables are sized by their row count. That is a real constraint on "target the display size" advice, and it is the reason a 40-bar chart cannot be made to fit a phone by resizing.

## Accessibility

Article 206 lists four shipped features rather than rules, which is the honest form for a tool.

- **A colorblind checker** that "warns you if the colors in your chart/map would not be distinguishable by those with any of the three main types of color vision deficiency."
- **Data download.** "a reader with a visual impairment has the possibility to download the data so that they can get it to read or interpreted to them by a screen reader in the way that suits their needs." Inventory topic 72, and the only source here that treats reachable underlying data as an accessibility feature rather than a reproducibility one.
- **Alternative descriptions**, with a mechanism detail worth knowing: writing one sets the chart body to `aria-hidden`, so the description replaces the auto-generated announcements rather than adding to them.
- **Fallback descriptions**, an experiment in what a screen reader says when nobody wrote alt text. The examples are specific: "Line chart with 7 lines", "Horizontal date axis, ranging from January 2019 to March 2021", "Category legend with x items", "This chart has one annotation." Rolled out for line charts and scatter plots only. Inventory topic 74.

Article 330, on writing alt text, is the practical companion and gives a usable formula, credited to Amy Cesal:

> `alt=" Chart type of type of data where reason for including chart"`

with the three parts glossed as chart type, what the axes show, and "the 'why': what your visualization shows that is meaningful." The article then argues with its own formula:

> "This formula is not set in stone. You could also argue that any mention of the chart type is unnecessary: The visualization is a way of representing the data; if words are used instead to describe the data, there's no need to talk about visual elements at all."

Two other rules from that article that a bar should carry:

- **Do not repeat the frame.** "The header and footer (including the title, description, data source, byline, notes etc.) are being read out by the screen reader, so you don't need to worry about repeating the same points."
- **Live-updating charts need maintained alt text.** "Make sure you update your alt text every time the highlight in your chart changes." An alt text with a stale number in it is worse than none.

Compare the W3C's two-part short/long pattern ([w3c-wai-complex-images.md](w3c-wai-complex-images.md)), which is the standard this is an implementation of.

## Where this source is used

Inventory topics 6, 18, 19, 23, 24, 26, 29, 30, 31, 32, 33, 37, 39, 41, 42, 44, 45, 62, 71, 72, 74, 80. See [roll-call.md](../roll-call.md).

**Two corrections to carry forward.** Datawrapper should no longer be cited in support of a flat dual-axis ban (topic 13); it ships the chart type. And its contrast numbers (topic 33) should be recorded as the softer, non-standard floor they are, not blended with WCAG's.

## Links

- [Choosing colors for data visualization](https://academy.datawrapper.de/article/140-what-to-consider-when-choosing-colors-for-data-visualization)
- [Why our column and bar charts start at zero (or below)](https://academy.datawrapper.de/article/326-why-our-column-and-bar-charts-start-at-zero)
- [How we make sure our charts, maps and tables are accessible](https://academy.datawrapper.de/article/206-how-we-make-sure-our-charts-maps-and-tables-are-accessible)
- [How to write good alternative descriptions](https://academy.datawrapper.de/article/330-how-to-write-good-alternative-descriptions-for-your-data-visualization)
- [Number formats you can display in Datawrapper](https://academy.datawrapper.de/article/207-custom-number-formats-that-you-can-display-in-datawrapper)
- [How to resize your visualizations](https://academy.datawrapper.de/article/390-how-to-change-the-size-of-your-visualizations)
- [How to create a dual-axis chart](https://academy.datawrapper.de/article/431-how-to-create-a-dual-axis-chart)
