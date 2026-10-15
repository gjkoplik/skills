---
type: source
status: primary-read
retrieved: 2026-08-23
author: stephen-few
---

# Few, *Data Visualization Effectiveness Profile*

Stephen Few, "Data Visualization Effectiveness Profile", *Visual Business Intelligence Newsletter*, January/February/March 2017. An eleven-page article, not a book. It proposes seven criteria in two groups, a small-multiple strip chart for scoring against them, and four worked examples.

**What it is good for.** Separating *is this figure informative* from *will anyone look at it*, as **informative** and **emotive** criteria. His acceptable-range figure is the closest thing in the canon to this wiki's [floor-and-ceiling](../concepts/floor-and-ceiling.md) idea, and he is the only source in the set that names **construct validity** as a chart problem.

**What it does not settle.** Almost everything, by Few's own account: no study, one author, seven axes, and an explicit refusal to quantify. It is a critique frame, not a scoring rubric.

**How this was read.** The PDF downloads clean from perceptualedge.com and extracts to text: 11 pages, 1,729,801 bytes, `%PDF-1.6`, `is_encrypted == False`. An earlier "unreadable/password-protected binary" report was a retrieval failure. The roll-call's warning no longer holds: "everything mapped to Few is unvouched at the primary level."

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

The emotive scales have a labeled midpoint and the informative ones do not.

## The criteria in his words

**Usefulness** comes first and depends on the audience: "A data visualization is of little value if it helps people understand something that doesn't matter to them." Subjectivity does not weaken it: "Evaluating the usefulness of a data visualization is subjective, for it is based on an assessment of the needs and values of others, but that does not diminish the relevance of this criterion."

**Completeness** means comparison context:

> An effective data visualization includes all of the information that's needed to produce the intended level of understanding, but not more... Context is usually provided in the form of comparisons, such as comparisons to targets, measures of the norm, and historical values.

**Perceptibility** is the channel-effectiveness ranking in one sentence:

> Forcing people to compare the sizes or color intensities of objects, which is somewhat difficult and imprecise, when the positions or lengths of objects could have been used instead, reduces perceptibility.

**Truthfulness** is accuracy plus validity, which nothing else in this wiki covers:

> Accuracy is a measure of reliability and appropriate precision. Validity indicates how well something represents what it claims... If a graph presents a country's median household income as a measure of its people's happiness, it is invalid.

**Intuitiveness** depends on the audience and is not a ban on unfamiliar forms: "A parallel coordinates plot would be unfamiliar to most members of the general public, but familiar to select groups of scientists and statisticians."

**Engagement** is separate from **Aesthetics** and is not decoration: "I do not mean visual effects or ornamentation that entice people to examine those qualities only without becoming engaged with the information itself."

## The acceptable-range figure

Page 10 gives target ranges of different widths rather than scores:

> You'll notice that I've allowed little latitude in the realm of truthfulness, but a great deal of latitude along both of the emotive criteria. This is because, in general, if the visualization presents data that is important to the audience, they will be naturally interested in it, so extra effort to catch their eyes or draw them into the data isn't necessary.

He names the exception: "A journalistic infographic that appears on the web might need something extra to grab readers' attention... In these cases, the acceptable ranges for aesthetics and engagement would be much narrower."

That is a floor on truthfulness and a ceiling that scales with the artifact's job.

## Few's own disclaimers

> I have a slight preference for omitting a quantitative scale to avoid suggesting a level of quantitative precision that does not exist in these subjective measures.

> Notice also that I have not included an overall effectiveness score. It could be useful... but an overall effectiveness score would require that the individual criteria be weighted.

> And finally, I'm not suggesting that these criteria provide scientific rigor, but instead function merely as a consistent guide for meaningful assessment.

## Corrections to the mapping

1. **Completeness maps loosely.** [roll-call.md](../roll-call.md) maps it to topics 42 (every mark explained), 45 (notes and definitions) and 46 (sample size). Few means comparison context (targets, norms, historical values), closer to "a number without a comparison does not mean anything", and the inventory has no topic for it.
2. **Truthfulness maps only half.** The roll-call sends it to topics 9 through 11 and 91, all accuracy (proportional ink, truncation, inversion, truth over beauty). Validity has no inventory topic. "Does this measure what it claims to measure" is not a chart-drawing rule.
3. **Perceptibility is partly extrapolation.** Topic 6 (channel effectiveness) is exact, quoted above. Topics 16 (axis label size) and 33 (text contrast) do not appear in the article.

Two mappings check out:

- Topic 3's quote is accurate in substance. Few wrote "we should acknowledge that the effectiveness of a data visualization can only be fully determined in light of its creator's intentions and its audience's needs." The inventory's capitalized standalone version is a light edit, not a distortion.
- Topic 89's claim that the profile "splits criteria into informative and emotive, with Aesthetics and Engagement in the latter" is exact.

## The worked examples

The first profiles an Excel bar chart titled "SALES ARE IMPROVING": "Perceptibility suffers due to the distracting 3-D effects... we don't know if the title of this graph... is truthful because no insufficient historical context has been provided and we definitely know that the bars don't accurately represent the values because the scale doesn't start at zero." That covers topics 68, 37 and 9. "No insufficient" is Few's typo, reproduced.

The others are Minard's march on Moscow (optimal on all but intuitiveness), McCandless's "The Billion Pound-O-Gram" treemap, and Few's redesign of it. He invites disagreement: "You might assess the effectiveness of this chart differently than I have, and that's fine."

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md): 1, 3, 5, 6, 9, 10, 11, 16, 31, 33, 42, 45, 46, 89, 91. The corrections above bear on 16, 33, 42, 45 and 46.

## Links

- [inventory.md](../inventory.md): the topics this source grounds
- [roll-call.md](../roll-call.md): the mapping corrected here
- [concepts/floor-and-ceiling.md](../concepts/floor-and-ceiling.md): the acceptable-range figure is the same idea from another direction
- [cairo-truthful-art.md](cairo-truthful-art.md): the other criteria-list source
