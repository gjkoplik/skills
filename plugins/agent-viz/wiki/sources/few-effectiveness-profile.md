# Few, *Data Visualization Effectiveness Profile*

**What it is.** Stephen Few, "Data Visualization Effectiveness Profile", *Visual Business Intelligence Newsletter*, January/February/March 2017. **An eleven-page article, not a book.** It proposes seven criteria in two groups and a small-multiple strip chart for scoring a visualization against them, then applies it to four worked examples.

**Status: `primary-read`.** Retrieved 2026-08-23. **The PDF that "would not render" renders.** It downloads clean from perceptualedge.com, is not encrypted, and extracts to text in one call:

11 pages, 1,729,801 bytes, `%PDF-1.6`, `is_encrypted == False`. The earlier "unreadable/password-protected binary" report was a retrieval failure, not a property of the file.

**This retires the roll-call's warning that "everything mapped to Few is unvouched at the primary level."** It is vouched now, and two of the mappings turn out to be looser than they looked.

**What it is good for.** Come back here with: *is this figure informative, and separately, will anyone look at it*. Few's split between **informative** and **emotive** criteria is the useful move, and his acceptable-range figure is the closest thing in the canon to this wiki's [floor-and-ceiling](../concepts/floor-and-ceiling.md) idea. He is also the only source in the set that names **construct validity** as a chart problem.

**What it does not settle.** Almost everything, and Few says so himself. There is no evidence here, no study, one author, seven axes, and an explicit refusal to quantify. It is a critique frame, not a rubric to score with.

---

## The seven criteria, with Few's own scale endpoints

**Informative** (produces understanding):

| Criterion | Scale runs from | to |
|---|---|---|
| Usefulness | Useless | Very useful |
| Completeness | No relevant data | All relevant data |
| Perceptibility | Unclear and difficult | Clear and easy |
| Truthfulness | Inaccurate and/or invalid | Accurate and valid |
| Intuitiveness | Unfamiliar; difficult to understand | Familiar; easy to understand |

**Emotive** (produces a useful emotional response):

| Criterion | Scale runs from | via | to |
|---|---|---|---|
| Aesthetics | Ugly | Pleasing to the eye | Beautiful |
| Engagement | Distracts from data | Neutral | Draws one into the data |

Note the emotive scales have a labeled midpoint and the informative ones do not.

## What each criterion actually means, in his words

**Usefulness** is audience-relative and he leads with it: "A data visualization is of little value if it helps people understand something that doesn't matter to them." He grants the subjectivity without softening the criterion: "Evaluating the usefulness of a data visualization is subjective, for it is based on an assessment of the needs and values of others, but that does not diminish the relevance of this criterion."

**Completeness** is about **comparison context**, which is not obvious from the name:

> An effective data visualization includes all of the information that's needed to produce the intended level of understanding, but not more... Context is usually provided in the form of comparisons, such as comparisons to targets, measures of the norm, and historical values.

**Perceptibility** states the channel-effectiveness ranking in one sentence:

> Forcing people to compare the sizes or color intensities of objects, which is somewhat difficult and imprecise, when the positions or lengths of objects could have been used instead, reduces perceptibility.

**Truthfulness** is two things, and the second has no counterpart anywhere else in this wiki:

> Accuracy is a measure of reliability and appropriate precision. Validity indicates how well something represents what it claims... If a graph presents a country's median household income as a measure of its people's happiness, it is invalid.

**Intuitiveness** is explicitly audience-relative rather than a ban on unfamiliar forms: "A parallel coordinates plot would be unfamiliar to most members of the general public, but familiar to select groups of scientists and statisticians."

**Aesthetics** and **Engagement** are separated on purpose. Engagement is not decoration: "I do not mean visual effects or ornamentation that entice people to examine those qualities only without becoming engaged with the information itself."

## The acceptable-range figure, which is the best part

Page 10 gives target ranges rather than target scores, and the ranges are not the same width:

> You'll notice that I've allowed little latitude in the realm of truthfulness, but a great deal of latitude along both of the emotive criteria. This is because, in general, if the visualization presents data that is important to the audience, they will be naturally interested in it, so extra effort to catch their eyes or draw them into the data isn't necessary.

And he names the exception rather than leaving it implied: "A journalistic infographic that appears on the web might need something extra to grab readers' attention... In these cases, the acceptable ranges for aesthetics and engagement would be much narrower."

That is a floor on truthfulness and a ceiling that scales with the artifact's job, arrived at from a different direction than this wiki did.

## Few's own disclaimers, which a citer should carry

He gives away more than most authority sources do, and all three of these are load-bearing:

> I have a slight preference for omitting a quantitative scale to avoid suggesting a level of quantitative precision that does not exist in these subjective measures.

> Notice also that I have not included an overall effectiveness score. It could be useful... but an overall effectiveness score would require that the individual criteria be weighted.

> And finally, I'm not suggesting that these criteria provide scientific rigor, but instead function merely as a consistent guide for meaningful assessment.

Anyone building a scored rubric on top of the profile is doing the thing its author declined to do.

## Corrections to the mapping, now that the primary is readable

Three, in descending order of consequence.

1. **Completeness maps loosely.** [roll-call.md](../roll-call.md) sends Completeness to topics 42 (every mark explained), 45 (notes and definitions) and 46 (sample size). Few's completeness is about **comparison context**: targets, norms, historical values. That is closer to "a number without a comparison does not mean anything" and **the inventory has no topic for it**. This is a real hole, and it is the one thing Few would add to the list.
2. **Truthfulness maps only half.** The roll-call sends it to topics 9 through 11 and 91, all of which are accuracy (proportional ink, truncation, inversion, truth over beauty). **Validity has no inventory topic at all.** "Does this measure what it claims to measure" is not a chart-drawing rule, which is presumably why nobody derived it, and it is still the failure mode that produces the most confidently wrong figures.
3. **Perceptibility is partly extrapolation.** Topic 6 (channel effectiveness) is exact, quoted above. Topics 16 (axis label size) and 33 (text contrast) do not appear in the article in any form.

Two things check out clean:

- Topic 3's quote is accurate in substance. Few's sentence reads "we should acknowledge that the effectiveness of a data visualization can only be fully determined in light of its creator's intentions and its audience's needs." The inventory presents it capitalized as a standalone sentence, which is a light edit and not a distortion.
- Topic 89's claim that the profile "splits criteria into informative and emotive, with Aesthetics and Engagement in the latter" is exactly right.

## The worked examples

Four, and the first one is a compact statement of three inventory topics at once. Profiling an Excel bar chart titled "SALES ARE IMPROVING": "Perceptibility suffers due to the distracting 3-D effects... we don't know if the title of this graph... is truthful because no insufficient historical context has been provided and we definitely know that the bars don't accurately represent the values because the scale doesn't start at zero." That is topics 68, 37 and 9 in one paragraph. (The "no insufficient" is Few's typo, reproduced.)

The others: Minard's march on Moscow (optimal on everything except intuitiveness), McCandless's "The Billion Pound-O-Gram" treemap, and Few's own redesign of it. He is careful to invite disagreement on the ratings: "You might assess the effectiveness of this chart differently than I have, and that's fine."

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md), do not recompute: 1, 3, 5, 6, 9, 10, 11, 16, 31, 33, 42, 45, 46, 89, 91. See the corrections above before leaning on 16, 33, 42, 45 or 46.

## What the project got wrong about it

The status, and it mattered. Two topics (3 and 89) were carried on search aggregation of a PDF that was one `curl` flag away. Both turned out to be right, which is luck rather than method. The retrieval failure also cost the project the two findings above, since neither the comparison-context gap nor the validity gap is visible in a summary of the criteria list.

## Links

- [inventory.md](../inventory.md), the topics this source grounds
- [roll-call.md](../roll-call.md), the mapping being corrected here
- [concepts/floor-and-ceiling.md](../concepts/floor-and-ceiling.md), Few's acceptable-range figure is the same idea from another direction
- [cairo-truthful-art.md](cairo-truthful-art.md), the other criteria-list source
