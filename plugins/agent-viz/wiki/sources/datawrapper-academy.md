---
type: source
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Datawrapper Academy

The help documentation for Datawrapper, a browser-based charting tool widely used in newsrooms. Its advice is backed by a product that can refuse to do the wrong thing, and for truncated bar axes it does.

**What it is good for.** Number formatting and locale, and responsive rendering at phone width, which nothing else in this corpus covers seriously. Also a short guide to color as encoding, and the clearest statement of gray as context.

**What it does not settle.** Every claim is authority-asserted house practice, bound to a hosted product with a fixed feature set. Some of it (plot-height sliders, embed flags) does not transfer to a plotting library. Its contrast floor is softer than WCAG and conflicts with the other accessibility sources here.

**How this was read.** Seven articles were fetched and converted locally, and quotes are verbatim from those. The rest of the Academy was not read.

| Article | ID |
|---|---|
| What to consider when choosing colors for data visualization | 140 |
| How we make sure our charts, maps and tables are accessible | 206 |
| How to write good alternative descriptions for your data visualization | 330 |
| Why our column and bar charts start at zero (or below) | 326 |
| How to create a dual-axis chart | 431 |
| Number formats you can display in Datawrapper | 207 |
| How to resize your visualizations | 390 |

---

## Color: twelve numbered rules

Article 140 is a numbered list.

**Gray for context** (inventory topic 29):

> "Using grey for less important elements in your chart makes your highlight colors (which should be reserved for your most important data points) stick out even more. Grey is also helpful for general context data, less important annotations, to show what's unselected by the user, or to calm down the overall visual impression of your charts. Since grey can seem a bit cold, consider using it with a hint of color: Try a warm grey (grey+yellow/orange/red), or use another very light color as an alternative (e.g. super light yellow)."

The warm-gray detail appears nowhere else in this corpus. Three independent style guides state the gray rule, and no controlled study tests it ([refutations.md](../refutations.md)).

**Every mapped channel explained** (inventory topic 42, generalized past color):

> "Every visual mark that represents a value or variable should be explained: What does the height of your bar mean? What does the size of your circles on a symbol map represent? The same is true for colors."

**A single-hue palette on categories implies a ranking:**

> "It might be tempting to use shades of one hue (e.g. blue) even for categories, to make your chart look less colorful. However, since many readers will associate dark colors with 'more/high' and bright colors with 'less/low', such a color palette will imply a ranking of your categories."

**Lightness builds a gradient:** "Your gradient should work in black and white, too. Gradients with many variations in lightness (like rainbow scales) can confuse readers." matplotlib reaches the same conclusion.

**Diverging midpoints are light gray, not white.**

**Gender colors without pink and blue:**

> "When it comes to color-encoding gender data, consider avoiding the stereotypical pink-blue combination. To not confuse your readers entirely, try a cold color for men (e.g. blue or purple) and a warmer color for women (e.g. yellow, orange or a warm green)."

The Urban Institute takes the same position ([urban-institute.md](urban-institute.md)), and both give a replacement rather than only a prohibition.

**A cap of seven colors:** "If you need more than seven colors in a chart, consider using another chart type or to group categories together." This is the third independent source with that cap, and no study backs any of them.

**Color as a secondary encoding** (inventory topic 6, channel effectiveness):

> "Consider showing your most important values with bars, position (like in a dot plot), or even areas, and use colors to only show categories."

### The contrast conflict

> "The contrast ratio between background and foreground should be at least 2.5 for big text and at least 4 for small text. In addition to having a high contrast ratio, avoid complementary hues (e.g. red and green, orange and blue) and bright colors for backgrounds."

WCAG 2.0 AA is 4.5:1 for normal text and 3:1 for large text and graphical objects, so Datawrapper is lower on both. The two floors are incompatible, not averageable. WCAG is a published standard, and Chartability, the only peer-reviewed accessibility source in the corpus, uses it ([chartability.md](chartability.md)). Datawrapper's floor has no stated derivation.

## Zero baselines, enforced by the product

Article 326 explains why a feature does not exist.

> "Truncated y-axes in column charts and bar charts are considered deceptive and misleading. And there's research backing that up."
>
> "We have a responsibility towards your readers -- we don't want them to be misled. That's why Datawrapper doesn't allow you to begin your y-axis at something greater than zero."

It cites Pandey et al., CHI 2015, quoting "participants who saw the deceptive visualization perceived the underlying message in its exaggerated form" and that these techniques "do lead to major misinterpretation from the reader's side and that the effects are also rather large." That paper's Discussion misreports the inverted-axis condition's 2.5% control error rate as 18.4% ([refutations.md](../refutations.md)). Datawrapper's citation avoids that passage, and the effect-size claim it quotes recomputes correctly from Table 2.

The article gives three alternatives to truncation:

- A dot or range plot, because "Readers don't expect dot plots (or, for two values, range plots) to start at zero because there's no filled bar or column that would indicate that." That derives proportional ink from the mark rather than the axis.
- A line chart, if the categories are ordered.
- A plot of the differences between the bars instead of the values.

## Datawrapper ships a dual-axis chart

Article 431 walks through building one, and "Dual-axis & Waterfall Charts" is a top-level Academy category. The feature is on the Business plan.

> "Dual-axis charts combine two vertical axes with differing units or scales into a single chart with one, shared horizontal axis, and also known double Y chart, combo charts, superimposed charts, or mixed line-and-bar series."

> "The values do not have to be of the same measure (in our examples, rainfall in mm and temperature in degree Celcius) -- in fact, your dual-axis chart will be easiest to understand if they're not."

[inventory.md](../inventory.md) topic 13 cites Datawrapper among the practitioner sources behind a flat dual-axis ban, and [refutations.md](../refutations.md) finds no experiment supporting one. Datawrapper hard-blocks truncated bar axes but treats dual axes as a design tool. Its caveat inverts the usual worry about spurious correlation: unrelated units make the chart safer, because nobody mistakes millimeters of rain for degrees Celsius.

## Number formats and locale

Article 207 is the only serious treatment of number formatting in this corpus. Inventory topic 18 names formatting as one of the most common visible defects in machine-generated figures.

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

The `[]` convention separates "how many decimals do I allow" from "how many do I insist on". `0.[00]` renders `0.061` as `0.06` and `1600` as `1600`, not `1600.00`. That is significant-digit discipline (topic 18) in one token, which matplotlib's formatters lack.

Locale belongs to the output, not the format. The decimal mark and thousands separator "depend on the output locale (language) you choose for your visualization", as does the currency symbol (inventory topic 19). The format string says *group thousands*, and the renderer chooses between `1,000` and `1.000`.

## Responsive sizing

Article 390 supplies the widths the inventory quotes:

> "Embedded visualizations are fully responsive. That means that the width of your embedded visualization adapts smoothly to the width of your reader's screen. If your visualization gets embedded, the width can't be defined; it depends on the device the visualization is viewed on. **On mobile screens, your chart might only be 380px or 400px wide, while on a big computer screen, it might be 700px wide.**"

> "You don't actually set a width for your visualization; the width gets set by your reader's screen size."

It sets plot height, not chart height:

> "The plot is the chart area without header, footer, color key, or annotations. In Datawrapper, you set a height for the plot instead of the full chart. That's because on mobile screens, a long title, footer, or annotations shown as a key would otherwise 'eat away' the space for the actual chart."

Height is either fixed pixels or an aspect ratio derived from width, the responsive version of inventory topic 14. Bar charts, dot plots, range plots, arrow plots and tables take their height from their row count, so a 40-bar chart cannot be made to fit a phone by resizing.

## Accessibility

Article 206 lists four shipped features.

- **A colorblind checker** that "warns you if the colors in your chart/map would not be distinguishable by those with any of the three main types of color vision deficiency."
- **Data download**, so "a reader with a visual impairment has the possibility to download the data so that they can get it to read or interpreted to them by a screen reader in the way that suits their needs." Inventory topic 72. No other source here treats reachable data as an accessibility feature rather than a reproducibility one.
- **Alternative descriptions.** Writing one sets the chart body to `aria-hidden`, so the description replaces the auto-generated announcements.
- **Fallback descriptions** for charts nobody wrote alt text for: "Line chart with 7 lines", "Horizontal date axis, ranging from January 2019 to March 2021", "Category legend with x items", "This chart has one annotation." Line charts and scatter plots only. Inventory topic 74.

Article 330 gives an alt-text formula credited to Amy Cesal:

> `alt=" Chart type of type of data where reason for including chart"`

The parts are chart type, what the axes show, and "the 'why': what your visualization shows that is meaningful." The article then qualifies its own formula:

> "This formula is not set in stone. You could also argue that any mention of the chart type is unnecessary: The visualization is a way of representing the data; if words are used instead to describe the data, there's no need to talk about visual elements at all."

It adds two rules. The frame is not repeated: "The header and footer (including the title, description, data source, byline, notes etc.) are being read out by the screen reader, so you don't need to worry about repeating the same points." Live-updating charts need maintained alt text: "Make sure you update your alt text every time the highlight in your chart changes."

This implements the W3C's two-part short and long pattern ([w3c-wai-complex-images.md](w3c-wai-complex-images.md)).

## Where this source is used

Inventory topics 6, 18, 19, 23, 24, 26, 29, 30, 31, 32, 33, 37, 39, 41, 42, 44, 45, 62, 71, 72, 74, 80. See [roll-call.md](../roll-call.md).

Datawrapper does not support a flat dual-axis ban (topic 13), since it ships the chart type. Its contrast numbers (topic 33) are a softer, non-standard floor, distinct from WCAG's.

## Links

- [Choosing colors for data visualization](https://academy.datawrapper.de/article/140-what-to-consider-when-choosing-colors-for-data-visualization)
- [Why our column and bar charts start at zero (or below)](https://academy.datawrapper.de/article/326-why-our-column-and-bar-charts-start-at-zero)
- [How we make sure our charts, maps and tables are accessible](https://academy.datawrapper.de/article/206-how-we-make-sure-our-charts-maps-and-tables-are-accessible)
- [How to write good alternative descriptions](https://academy.datawrapper.de/article/330-how-to-write-good-alternative-descriptions-for-your-data-visualization)
- [Number formats you can display in Datawrapper](https://academy.datawrapper.de/article/207-custom-number-formats-that-you-can-display-in-datawrapper)
- [How to resize your visualizations](https://academy.datawrapper.de/article/390-how-to-change-the-size-of-your-visualizations)
- [How to create a dual-axis chart](https://academy.datawrapper.de/article/431-how-to-create-a-dual-axis-chart)
