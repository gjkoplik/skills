---
type: person
status: primary-read
retrieved: 2026-08-23
---

# Lisa Charlotte Muth

**What they are known for.** The Datawrapper blog, where since 2017 she has written the best working practitioner's treatment of color in charts: not "use a colorblind-safe palette" but a numbered account of hue distance, saturation balance, lightness ordering, and how to de-emphasize without accidentally creating a new category. She also writes about text in charts, and argues in public for simple chart types.

**How this was read.** Retrieved 2026-08-23. Five posts under her byline on `datawrapper.de/blog` were pulled with `curl` and stripped to text locally with BeautifulSoup. Every quote below is verbatim from those local files:

| Post | Date |
|---|---|
| How to pick more beautiful colors for your data visualizations | 4 Sep 2020 |
| Which color scale to use when visualizing data (part 1 of 4) | 16 Mar 2021 |
| In defense of simple charts | 26 Jul 2021 |
| What to consider when using text in data visualizations | 28 Sep 2022 |
| Emphasize what you want readers to see with color | undated on the page |

Her own site (`lisacharlottemuth.com`) supplied the biographical line: she writes, creates, talks and hosts events about data vis "currently for Datawrapper in Berlin," and has been paid by Datawrapper to do so since November 2017.

**What they are good for.** Come back here with: *these colors are technically fine and the chart still looks bad*. Nobody else in this section operates at her resolution. Where [Knaflic](cole-nussbaumer-knaflic.md) says use one accent against neutral, Muth tells you which hue, at what saturation, how far from a pure hue, and what happens to it in grayscale. She is also the only one of the five with a worked-out theory of **de-emphasis** as distinct from emphasis.

**What they do not settle.** Everything is authority-asserted house practice, and it is bound to a hosted tool with a fixed feature set. She cites one paper (Bartram, Patra and Stone 2017 on affective color) across five posts. There is nothing on statistical honesty, uncertainty, or scales, and the chart-type advice is explicitly scoped to "a mainstream, lay audience."

---

## "In the style of Lisa Charlotte Muth" means, concretely

**How much of this is inference.** Very little. Her posts are numbered rule lists about her own practice, so this section is mostly quotation. What is **not** grounded here: I did not measure her rendered charts. Her published figures are Datawrapper charts, and no pixel sampling was done, so the palette section below is her stated method rather than a measurement of her output. That is the reverse of the [Schwabish](jonathan-schwabish.md) page and worth knowing when you compare them.

**Palette habits.** She does not have a fixed palette. She has a **procedure**, and it is checkable at every step.

- **Stay in one neighborhood of the wheel.** "There's no need to rely on hues from all around the color wheel... It will look more professional, and therefore more trustworthy, when it only uses a few hues and their neighbors." She names a specific harmony to refuse: "square" or "tetradic," because "it will result in too many hues."
- **Default to warm plus blue.** "There's a complementary color combination that is especially loved by data visualization designers: **yellow/orange/red and blue.**" Her reasons are versatility and accessibility: "colorblind people can easily distinguish blue and orange/red from each other." Her summary line is "when in doubt, use an orange/red with blue," which lands in the same place as Schwabish's grayscale-safe pair by a completely different route.
- **Green is a special case.** Forest green runs roughly 90 to 150 degrees with its peak at 120, and she wants you out of the middle of it. "So when using green, make it a bit yellow or a bit blue." She backs it with a measurement of somebody else's chart: the Washington Post green she points at is "a 142° green, but only 14% saturated."
- **Avoid pure hues.** Exactly 0, 60, 120, 180, 240, 300 degrees. "If you want to have bright, saturated colors, rely on mixed colors **at least 5-10° away from the pure hues.**" There is a check you can run without a color picker: "If at least two of the [RGB] values are the same, they're 'pure'."
- **Avoid the top corner.** "If your colors come close to 100% saturation **and** 100% brightness, it's likely your colors are too colorful."
- **Vary lightness deliberately.** "Get it right in black & white." Convert to grayscale; if your categories land on the same gray, fix the colors rather than adding white borders. She names picking categorical colors out of a sequential ramp as a legitimate shortcut, because "all these gradients move smoothly from light to dark."
- **Then rebalance.** Having given the colors different lightness, "you'll need to balance them out. Try to desaturate bright colors. Put more saturation in dark colors." The goal is that most colors are "more or less equally attention-grabbing," with only one or two meant to stand out.

Her **de-emphasis** rules are the distinctive part, and the strongest one is a prohibition:

> Don't get experimental here, another hue will communicate "this is a separate category," not "these are all less important categories"

She sources that to a documented mistake by Sarah Leo at The Economist, quoting Leo: "The visualiser (me!) ignored the fact that a change of colour often implies a categorical change." The fix is to keep the hue and drop the saturation. Gray is allowed, but only as a special status, never as a spare category color: "If a category is as important as other, colorful ones, don't make it gray." And there is a mechanical trick she gives outright: lower opacity instead of lowering saturation, because a desaturated red "becomes almost brownish" while an 80%-opaque red "looks like a nice pastel red."

**Title and annotation voice.** Heavily annotated, directly labeled, and colloquial at the top.

- **No legend if you can help it.** "One big part of doing so is to **remove the color key and directly label your categories.**" Her museum analogy is the argument: a legend is a label placed next to the door.
- **Annotate on principle, not on exception.** "If you're creating an *explanatory* chart or map, it will likely be better with annotations in it." Three prompts she gives: annotate any design element that needs explaining, any data point you want readers to see, and any context that explains why the data looks the way it does.
- **Titles are conversational; precision moves down.** "'Is higher than ever' can be a stronger choice in a title than 'peaks'." And, flatly: "if you're visualizing for a mainstream audience, don't use words like 'median' or 'standard deviation' in your title." The precise definition goes in the description or the note, and she walks through a Washington Post map to show the three-tier split of title, description, and small gray footnote.
- **Two text levels, not five.** "use only two levels of hierarchy that are clearly different from each other, like a 12px gray and a 14px black."
- **Left-align.** "Left- or right-aligned text looks tidier than center-aligned text... Both center- and right-aligned annotations are also harder to read, so don't use them for lengthy text (everything above roughly 10 words)." ([Knaflic](cole-nussbaumer-knaflic.md) independently names center alignment as a pet peeve. They agree.)
- **Never rotate axis labels.** "Instead of rotating axis labels, find another place inside your chart for them." If the labels are still too long, change the chart type rather than the text.
- **Outline text that overlaps anything.** "If your text sits on other elements, even just a subtle gridline, consider using a **text outline.**"
- **Round the numbers.** "Don't add unnecessary precision when showing numbers," and prefer `20k` / `20m` / `20b` to a multiplier note in the description.

Her stated body-text default is unusually specific: "sans-serif, regular, sentence case, neither overly narrow nor wide, >12px, (almost) black text."

**Chart-type preferences and aversions.** She is the section's defender of the plain chart, and she has published the argument under that name. Her scope: "bar, column, line, area, pie, and donut charts, and others like them." **Note that pie and donut are inside her fence**, which puts her at odds with [Knaflic](cole-nussbaumer-knaflic.md), whose book has a named visuals-to-avoid section containing both.

What she is skeptical of is not any particular type but the ornate one-off: glyphs, novel forms, chart types with extra encodings layered on, combinations. Her stated reaction is a taste position honestly labeled as one: "When I look at a nonstandard chart, I might marvel at the beauty and ingenuity of its design. But often, I become skeptical. I often assume that its content can't be *extremely* interesting, otherwise, it would be shown more simply." Her positive claim is that "there's a reason why journalists show us the data we're most interested in as simple charts."

**Density and restraint.** Not minimal. Restrained in **color**, generous in **text**. That combination is the thing that separates her from everyone else here: she will spend a paragraph getting a category down to a desaturated gray-blue and then put four annotations on the plot area. Her framing of the tradeoff is explicit: "**By sacrificing some legibility for your gray categories, you can gain great clarity for the highlighted few.**"

She has no stated position on gridlines or frames in what was read, which is a real gap in this profile.

**The tell.** Direct labels where a legend should be, a bold left-aligned title in plain speech with a smaller gray description under it, annotations sitting on the plot area with a background-colored stroke around the letters, exactly two type sizes, one orange-red against one blue, and the de-emphasized series in a paler version of the **same** hue rather than in gray or in a new color. If the unimportant category is a desaturated sibling of the important one, that is her signature and almost nobody else in this canon states it as a rule.

## What they would say about your figure first

She would go to the color, and not to whether it is accessible. She would ask what the color is **doing**: which category is it telling the reader to look at, and did you decide that or did the tool? Her opening move is procedural and slightly startling if you have not heard it: gray everything out first, then color back in only what matters. "I actually recommend **graying out all your colorful categories first.**" Then she would check whether your de-emphasis is a different hue, because that is the specific mistake she has written about most. Then grayscale: convert the whole thing and see whether your categories collapse into the same value. Then the text, which she thinks you have not thought about at all, and she is usually right. "Text is maybe the most underrated element in any data visualization." She would ask you to say the title out loud as if to a friend, and if it contains a statistical term or the phrasing of the dataset's official documentation, she would rewrite it. What she would **not** do is tell you the chart type is too plain. "Simple charts are great. That they're underappreciated. Necessary. And that you should be proud of yourself if you create simple charts."

## Works, and where they sit in this wiki

- **[sources/datawrapper-academy.md](../sources/datawrapper-academy.md)** is `primary-read` and covers seven Datawrapper Academy help articles, including article 140, "What to consider when choosing colors for data visualization," which covers ground overlapping the blog posts above. **Note the distinction**: the Academy is Datawrapper's product documentation and the articles carry no byline, so this page does not attribute them to her. The blog posts here do carry her byline. Anything about number formats, responsive sizing, alt text, the zero-baseline enforcement, or the contrast floor should be read from the Academy page, not here.
- **The blog series "Which color scale to use when visualizing data"** runs to four parts. Only part 1 was read. Parts 2 through 4, and the separate post on choosing an interpolation for a color scale, are **not covered anywhere in this wiki** and are the obvious next retrieval. Interpolation in particular is a topic nothing else in the canon touches.
- **"A detailed guide to colors in data vis style guides"** was fetched but not read in this pass. At 85KB of extracted text it is the longest thing she has written on the subject and would bear directly on any house-style work.
- **Her personal site**, talks, and the data vis crossword are not covered.

## Links

- [sources/datawrapper-academy.md](../sources/datawrapper-academy.md), the product documentation side of the same house
- [cole-nussbaumer-knaflic.md](cole-nussbaumer-knaflic.md), the same emphasis-through-color problem at lower resolution, and the opposite verdict on pie charts
- [jonathan-schwabish.md](jonathan-schwabish.md), whose book she argues with by name over whether simple charts are boring
- [refutations.md](../refutations.md), for why "gray plus one accent" is an assertion rather than a finding no matter who is stating it
- [concepts/channels.md](../concepts/channels.md), the evidence her color reasoning does and does not rest on
