---
type: person
status: primary-read
retrieved: 2026-08-23
---

# Lisa Charlotte Muth

**What they are known for.** The Datawrapper blog, where since 2017 she has written a detailed practitioner's treatment of chart color: hue distance, saturation balance, lightness ordering, and de-emphasis without an accidental new category. She also writes about chart text and defends simple chart types.

**How this was read.** Five posts under her byline on `datawrapper.de/blog` were pulled with `curl` and stripped to text locally with BeautifulSoup. Every quote is verbatim from those files.

| Post | Date |
|---|---|
| How to pick more beautiful colors for your data visualizations | 4 Sep 2020 |
| Which color scale to use when visualizing data (part 1 of 4) | 16 Mar 2021 |
| In defense of simple charts | 26 Jul 2021 |
| What to consider when using text in data visualizations | 28 Sep 2022 |
| Emphasize what you want readers to see with color | undated on the page |

Her site (`lisacharlottemuth.com`) says she writes, creates, talks and hosts events about data vis "currently for Datawrapper in Berlin," paid by Datawrapper since November 2017.

**What they are good for.** Colors that are technically fine on a chart that still looks bad. Where [Knaflic](cole-nussbaumer-knaflic.md) says one accent against neutral, Muth names the hue, saturation, distance from a pure hue, and grayscale result. She also has a worked-out theory of **de-emphasis**.

**What they do not settle.** Everything is authority-asserted house practice, bound to a hosted tool with a fixed feature set. She cites one paper (Bartram, Patra and Stone 2017 on affective color) across five posts. Nothing on statistical honesty, uncertainty, or scales, and the chart-type advice is scoped to "a mainstream, lay audience."

---

## "In the style of Lisa Charlotte Muth" means, concretely

Mostly quotation from her numbered rule lists. Her Datawrapper charts were not pixel-sampled, so the palette below is her stated method, not a measurement. The [Schwabish](jonathan-schwabish.md) palette is measured, which matters for any comparison.

**Palette habits.** A procedure, not a fixed palette.

- **One neighborhood of the wheel.** "There's no need to rely on hues from all around the color wheel... It will look more professional, and therefore more trustworthy, when it only uses a few hues and their neighbors." She rejects "square" or "tetradic" harmony because "it will result in too many hues."
- **Warm plus blue by default.** "There's a complementary color combination that is especially loved by data visualization designers: **yellow/orange/red and blue.**" Partly for accessibility: "colorblind people can easily distinguish blue and orange/red from each other." Her summary, "when in doubt, use an orange/red with blue," lands on Schwabish's grayscale-safe pair by another route.
- **Green pushed off center.** Forest green runs roughly 90 to 150 degrees with its peak at 120: "So when using green, make it a bit yellow or a bit blue." Her example is a Washington Post green, "a 142° green, but only 14% saturated."
- **No pure hues** (exactly 0, 60, 120, 180, 240, 300 degrees). "If you want to have bright, saturated colors, rely on mixed colors **at least 5-10° away from the pure hues.**" The check: "If at least two of the [RGB] values are the same, they're 'pure'."
- **Not the top corner.** "If your colors come close to 100% saturation **and** 100% brightness, it's likely your colors are too colorful."
- **Varied lightness.** "Get it right in black & white." Categories that collapse to one gray get new colors, not white borders. Taking categorical colors from a sequential ramp works because "all these gradients move smoothly from light to dark."
- **Rebalancing.** "you'll need to balance them out. Try to desaturate bright colors. Put more saturation in dark colors." Most colors should be "more or less equally attention-grabbing," with one or two standing out.

Her strongest de-emphasis rule is a prohibition:

> Don't get experimental here, another hue will communicate "this is a separate category," not "these are all less important categories"

Her source is Sarah Leo's documented mistake at The Economist: "The visualiser (me!) ignored the fact that a change of colour often implies a categorical change." The fix keeps the hue and drops the saturation. Gray marks a special status, never a spare category color: "If a category is as important as other, colorful ones, don't make it gray." Lower opacity beats lower saturation, because a desaturated red "becomes almost brownish" while an 80%-opaque red "looks like a nice pastel red."

**Title and annotation voice.** Heavily annotated, directly labeled, colloquial at the top.

- **Direct labels.** "One big part of doing so is to **remove the color key and directly label your categories.**" Her analogy: a legend is a museum label placed next to the door.
- **Annotation by default.** "If you're creating an *explanatory* chart or map, it will likely be better with annotations in it." Her three prompts: a design element that needs explaining, a data point readers should see, and context for why the data looks as it does.
- **Plain titles, precision lower down.** "'Is higher than ever' can be a stronger choice in a title than 'peaks'." And "if you're visualizing for a mainstream audience, don't use words like 'median' or 'standard deviation' in your title." Definitions go lower, as in a Washington Post map she walks through: title, description, small gray footnote.
- **Two text levels.** "use only two levels of hierarchy that are clearly different from each other, like a 12px gray and a 14px black."
- **Left alignment.** "Left- or right-aligned text looks tidier than center-aligned text... Both center- and right-aligned annotations are also harder to read, so don't use them for lengthy text (everything above roughly 10 words)." [Knaflic](cole-nussbaumer-knaflic.md) independently names center alignment as a pet peeve.
- **No rotated axis labels.** "Instead of rotating axis labels, find another place inside your chart for them." If labels are still too long, the chart type changes.
- **Outlined text.** "If your text sits on other elements, even just a subtle gridline, consider using a **text outline.**"
- **Rounded numbers.** "Don't add unnecessary precision when showing numbers," with `20k` / `20m` / `20b` preferred to a multiplier note.

Body text default: "sans-serif, regular, sentence case, neither overly narrow nor wide, >12px, (almost) black text."

**Chart-type preferences and aversions.** Her defense of simple charts covers "bar, column, line, area, pie, and donut charts, and others like them." Pie and donut are inside it, against [Knaflic](cole-nussbaumer-knaflic.md), whose book lists both among visuals to avoid. She distrusts the ornate one-off (glyphs, novel forms, extra encodings, combinations), and labels that as taste: "When I look at a nonstandard chart, I might marvel at the beauty and ingenuity of its design. But often, I become skeptical. I often assume that its content can't be *extremely* interesting, otherwise, it would be shown more simply." Her positive claim: "there's a reason why journalists show us the data we're most interested in as simple charts."

**Density and restraint.** Restrained in color, generous in text. "**By sacrificing some legibility for your gray categories, you can gain great clarity for the highlighted few.**" Nothing read states a position on gridlines or frames.

**The tell.** Direct labels where a legend would be, a bold left-aligned title in plain speech with a smaller gray description under it, annotations on the plot area with a background-colored stroke around the letters, exactly two type sizes, one orange-red against one blue, and the de-emphasized series in a paler version of the **same** hue rather than gray or a new color. Almost nobody else in this canon states that last one as a rule.

## What they would say about a figure first

She would go first to what the color is doing, not to whether it is accessible, and ask whether it was a decision or a tool default: "I actually recommend **graying out all your colorful categories first.**" Then whether de-emphasis uses a new hue, whether categories collapse in grayscale, and the text: "Text is maybe the most underrated element in any data visualization." A title with a statistical term gets rewritten as if said aloud to a friend. She would not call the chart too plain: "Simple charts are great. That they're underappreciated. Necessary. And that you should be proud of yourself if you create simple charts."

## Works, and where they sit in this wiki

- [sources/datawrapper-academy.md](../sources/datawrapper-academy.md) is `primary-read` and covers seven Datawrapper Academy help articles, including article 140, "What to consider when choosing colors for data visualization," which overlaps the posts above. The Academy is unbylined product documentation, so this page does not attribute it to her. Number formats, responsive sizing, alt text, zero-baseline enforcement and the contrast floor are there.
- "Which color scale to use when visualizing data" has four parts, and only part 1 was read. Parts 2 through 4 and her post on color-scale interpolation are not covered, and nothing else in the canon covers interpolation.
- "A detailed guide to colors in data vis style guides" was fetched but not read. It is her longest piece on the subject.
- Her personal site, talks, and the data vis crossword are not covered.

## Links

- [sources/datawrapper-academy.md](../sources/datawrapper-academy.md): the same house's product documentation
- [cole-nussbaumer-knaflic.md](cole-nussbaumer-knaflic.md): the same color-emphasis problem at lower resolution, and the opposite verdict on pies
- [jonathan-schwabish.md](jonathan-schwabish.md): whose book she argues with by name over whether simple charts are boring
- [refutations.md](../refutations.md): why "gray plus one accent" is an assertion rather than a finding, whoever states it
- [concepts/channels.md](../concepts/channels.md): the evidence her color reasoning does and does not rest on
