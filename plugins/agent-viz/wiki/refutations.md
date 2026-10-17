# Refutations: rules that did not survive reading the source

Widely repeated claims that changed, weakened, or died when someone opened the primary source. Each entry gives the verdict; the numbers and the design live on the linked page.

Every quote was **re-extracted locally**, not taken from a fetch summary. See [Retrieval hazards](../CONTRIBUTING.md#retrieval-hazards). Extraction was `pdftotext` except where the linked page records otherwise.

## Summary

| The claim as it circulates | Verdict | What is true |
|---|---|---|
| ["Bank to 45 degrees"](#bank-to-45-degrees) | Scope-limited | 45° is not error-minimizing in general; Cleveland's result holds inside the moderate regime he tested |
| [Axis-break glyphs fix truncation](#axis-break-glyphs-as-the-truncation-remedy) | Tested, no measurable help | Two static designs failed to reduce the exaggeration. "Placebo" overstates a knife-edge result |
| [A flat ban on dual axes](#a-flat-ban-on-dual-axes) | `absence of evidence` | No experiment tests the twin-axis chart. The paper usually cited studied something else, and the authorities have softened |
| ["Log scales are fine for experts"](#log-scales-are-fine-for-expert-audiences) | Does not hold | Domain experts read log-log at 56% against 93% for linear |
| [Chartjunk and data-ink are settled](#chartjunk-and-the-data-ink-ratio-as-settled) | `contested`, but not in the usual shape | Decoration *around* the mark is contested; deformation *of* the mark is not |
| ["Gray plus one accent" is evidence-backed](#gray-plus-one-accent-as-an-evidence-backed-rule) | No study exists | Asserted by every major practitioner and tested by none. Fine as house style, not as an anchor |
| [Broad vision-model critique fails, decomposed works](#the-broad-vision-model-critique-fails-decomposed-succeeds-comparison) | Refuted as a comparison | Both numbers are right and non-comparable. The 0.428 *was* decomposed rubric-scoring |
| [Liu, Wang & Willard on prompt length](#a-source-that-should-not-be-cited-at-all) | Do not cite | Arithmetically impossible rows, and the system under test is never named |
| [Pandey et al. 2015 on inverted axes](#a-published-paper-that-contradicts-itself) | Sound conclusion, broken Discussion | Its Discussion inverts its own table. The control error rate is 2.5%, not 18.4% |
| [The Cleveland-McGill ranking is fully ordered](#the-cleveland-mcgill-ranking-is-not-a-fully-ordered-list) | Misattributed and partly untested | The familiar ordered list is the 1985 table, routinely cited to 1984. 1984 has ties it cannot separate |
| ["Pie charts are read by angle"](#pie-charts-are-read-by-angle) | Refuted by decomposition | Angle was the worst cue, not the primary one. Bar-beats-pie survives without the mechanism |
| ["Matrices beat node-link above 20 nodes"](#matrices-beat-node-link-diagrams-above-twenty-nodes) | Scope-limited, and reversed | Density and interaction decide it, not node count |
| ["Bertin's seven visual variables"](#bertins-seven-visual-variables) | The number is wrong | Eight. Collapsing the plane's two dimensions into one breaks the argument it came from |
| [Anand & Chattaraj on instruction stacking](#a-preprint-to-use-directionally-only) | Directional only | Verbatim correct, unreviewed, and its own Table 7 breaks the remediation story |
| ["Chord is harder to read than Sankey"](#chord-diagrams-are-harder-to-read-than-sankey-diagrams) | Supported, and tiny | Effect sizes 0.02 and 0.001, gone by the fourth exposure. The large effect is preference |
| ["Horizontal bars are read less accurately than vertical"](#horizontal-bar-charts-are-read-less-accurately-than-vertical-ones) | Measured in VR, absent face-on | Large at oblique viewing angles in a headset, no difference at the one face-on position, and untested on a flat screen |
| ["Parallel coordinates beat scatterplots for negative correlations"](#parallel-coordinates-beat-scatterplots-for-negative-correlations) | Overstated by the original analysis | The asymmetry is real; the lead over the scatterplot is not. A reanalysis of the same data puts the two in one group and drops Weber's law |

---

## "Bank to 45 degrees"

**Status: not refuted, scope-limited.**

Talbot, Gerth & Hanrahan (InfoVis 2012):

> "we find that, in general, slope ratio errors are not minimized around 45°"

Their shift of the minimum below 30° belongs to the ANGLE strategy only, not the HEIGHT strategy Cleveland's subjects were told to use. Cleveland's model "fit our data well **in the regions considered in the original study**" and fails to extrapolate beyond them.

**Accurate phrasing:** 45° is not the error-minimizing ratio in general; Cleveland's result holds within the moderate regime he tested and does not extrapolate.

The paper's baseline result, often cited for zero baselines, reaches less far: baselines nearly eliminated the error for mid-angles below 45° and did not eliminate the error above 45°. Detail: [studies/talbot-2012-slope-ratio.md](studies/talbot-2012-slope-ratio.md).

## Axis-break glyphs as the truncation remedy

**Status: the tested designs did not measurably help. "Placebo" overstates it.**

Correll, Bertini & Franconeri (CHI 2020):

> "the exaggeration introduced through truncation appears to persist across chart types and chart designs, and even when participants make accurate reports of the numbers they observe"

The failure to reject was knife-edge: F(2,60) = 3.1 against a critical 3.1504, p ≈ 0.052, with 32 and 25 participants and two static designs. The authors: "We reject the unequivocal dichotomy of 'honest' and 'dishonest' charts."

**Accurate phrasing:** the tested break-glyph and gradient designs did not measurably reduce the exaggeration. A jagged-axis marker is not established as a remedy for it.

Detail: [studies/correll-2020-truncating-the-y-axis.md](studies/correll-2020-truncating-the-y-axis.md).

## A flat ban on dual axes

**Status: `absence of evidence`, not evidence of harm.**

The paper usually cited, Isenberg et al. (2011), tested **dual-scale focus-plus-context** charts (two magnifications of one series, not two variables on two scales) and says:

> "empirical evidence on the effectiveness of the Dual-Scale compared to other charts is missing"

Few, the person most cited for the ban: "I certainly cannot conclude, once and for all, that graphs with dual-scaled axes are never useful." Urban names two explicit exceptions, and Datawrapper ships a dual-axis chart type while hard-blocking truncated bar axes.

**Accurate phrasing:** a caution with its reason rather than a ban. The apparent correlation between the two series is a free parameter of the scaling choice, and nothing on the chart records what each scale was pinned to.

Detail: [studies/isenberg-2011-dual-scale-charts.md](studies/isenberg-2011-dual-scale-charts.md), [people/stephen-few.md](people/stephen-few.md).

## "Log scales are fine for expert audiences"

**Status: does not hold.**

623 Ecological Society of America members read log-log at **56%** against **93%** for linear-linear (Menge et al. 2018; reached in **secondary form only**, not primary-verified). Romano et al. (2020) found readers given a logarithmic scale "have a less accurate understanding of how the pandemic unfolded until now, make less accurate predictions on its future, and have different attitudes and policy preferences." The direction comes from two studies on different populations.

Detail: [studies/menge-2018-log-scales.md](studies/menge-2018-log-scales.md), [studies/romano-2020-log-scales-covid.md](studies/romano-2020-log-scales-covid.md).

## Chartjunk and the data-ink ratio as settled

**Status: `contested`, but not in the shape it is usually described.**

Bateman et al. (2010) put imagery around a correctly drawn bar and found accuracy "no worse than for plain charts". Skau et al. (2015) deformed the bars and found error rises. Skau's mechanism reconciles the two. Gillan & Richman's Experiment 1 supports Tufte in aggregate ("the higher the data-ink ratio, the faster the response time and the greater the accuracy"), and their element-level experiments do not. Bateman's long-term recall result does not replicate cleanly: Syeda et al. (2023) found no significant differences on any of the four long-term questions in the asynchronous study. Stock and Behrens (1991) found Tufte's box-less *midgap* plot "substantially less accurate than the original."

**Accurate phrasing:** the evidence separates decoration around the mark, which is contested, from deformation of the mark, which is not. "Maximize" is the verb the element-level data does not support.

Detail: [studies/bateman-2010-useful-junk.md](studies/bateman-2010-useful-junk.md), [studies/skau-2015-embellished-bars.md](studies/skau-2015-embellished-bars.md), [studies/gillan-richman-1994-data-ink.md](studies/gillan-richman-1994-data-ink.md), [chart-types/boxplot.md](chart-types/boxplot.md).

## "Gray plus one accent" as an evidence-backed rule

**Status: no controlled study found.**

No controlled experiment was found comparing one-accent with two-saturated-color emphasis on chart comprehension. The preattentive and visual-search literature supports color pop-out generally and does not test this rule. It is `authority-asserted`: Knaflic states it verbatim in a bylined post, and it is one of Schwabish's five core rules ("Start with Gray"). Both attributions are confirmed from primaries, and neither carries a study.

Detail: [people/cole-nussbaumer-knaflic.md](people/cole-nussbaumer-knaflic.md), [people/jonathan-schwabish.md](people/jonathan-schwabish.md).

## The "broad vision-model critique fails, decomposed succeeds" comparison

**Status: refuted as a comparison. Both underlying numbers are individually correct.**

The claim pairs VisJudgeBench (GPT-5, correlation **0.428** against human experts) with VisEval (readability evaluator at SRCC **0.843**). Four problems, most severe first:

1. **VisJudgeBench is not a broad prompt.** Its template demands structured JSON across six named sub-dimensions, so the 0.428 *is* decomposed rubric-scoring.
2. **The 0.687 is fine-tuning, not decomposition**: LoRA+GRPO on Qwen2.5-VL-7B with the same rubric.
3. **VisEval's success is substantially deterministic code.** Its layout check simulates a browser.
4. **The statistics are not comparable.** Pearson against Spearman, different targets, and no inter-annotator agreement published for VisJudgeBench.

**What survives:** VisEval's within-paper ablation, from 0.507 with neither deterministic sub-check to 0.843 with both, supports *deterministic sub-checks feeding a vision model beat the vision model alone*.

Neither benchmark has a page in this wiki.

## A source that should not be cited at all

**Liu, Wang & Willard, *Effects of Prompt Length on Domain-specific Tasks for LLMs* (arXiv:2502.14255).** Quotes and per-task numbers check out verbatim. Two problems disqualify it:

1. **Arithmetically impossible rows.** The QIC task reports precision 0.48, recall 0.10, **F1 0.84**; their harmonic mean is about 0.17. QIC supplies the headline +0.08, and without it the range is +0.01 to +0.07.
2. **The system under test is never named.** No model, version, temperature or API appears in the Experiments section.

There is no variance reporting or significance testing, and deltas run as small as ±0.01. The "long" condition varies **background knowledge**, never the number of simultaneous constraints, so it would not transfer to a rules document even if sound.

No page: it is an LLM paper, not a visualization source.

## A published paper that contradicts itself

**Pandey et al., *How Deceptive are Deceptive Visualizations?* (CHI 2015).** Table 3 reports the inverted-axis control condition as 39/40 correct (97.50%) and the deceptive condition as 7/38 correct (18.42%). The Discussion says:

> "the deceptive condition led to 97.5% incorrect responses whereas the control condition led to only 18.4% incorrect responses"

It relabeled the two **correct**-column percentages as incorrect and swapped their conditions. A third passage agrees with the table. The conclusion survives because the error preserves direction, but **quoting 18.4% as a control error rate is off by roughly 7x**; the real figure is 2.5%. No secondary source repeating the wrong figure was found.

Detail: [studies/pandey-2015-deceptive-visualizations.md](studies/pandey-2015-deceptive-visualizations.md).

## The Cleveland-McGill ranking is not a fully ordered list

**Status: scope-limited and partly untested. The version in circulation is from a different paper than the one it is cited to.**

The 1984 *JASA* paper has ten tasks in six ranks with ties. The 1985 *Science* paper has seven fully ordered ranks, with length and angle separated and color hue last. The familiar list is the 1985 table cited to 1984. The 1984 paper says:

> "Three of the ranks—3, 5, and 6—have more than one task; at the moment there is not enough information to separate the ties."

**Length, direction and angle are all rank 3.** The two experiments are not comparable, and Heer & Bostock (2010), the one head-to-head test since, failed to separate angle from length. **Color hue is excluded, not ranked last**: rank 6 is *shading and color saturation*.

**What survives:** position beats length, angle, and area, and angle beats area, all measured and replicated. **What does not:** any ordering within rank 3, and the mechanism "bars beat pies because length beats angle".

Detail: [studies/cleveland-mcgill-1984.md](studies/cleveland-mcgill-1984.md), [people/william-cleveland.md](people/william-cleveland.md), [studies/heer-bostock-2010.md](studies/heer-bostock-2010.md).

## "Pie charts are read by angle"

**Status: refuted by direct decomposition.**

Cleveland & McGill flagged it as a conjecture: "we conjecture that the primary elementary visual task for extracting the numerical information is perception of angle". Skau & Kosara (2016) isolated the three cues and found angle the **worst** performer:

> "This was not what we hypothesized, and contradicts common wisdom that angles are critical to pie and donut chart perception."

Eells (1926) found the same by asking. Bar-beats-pie survives as a direct measurement, without the mechanism. The standard case against donut charts falls, since it rests on the cue that carried the least.

Detail: [studies/skau-kosara-2016.md](studies/skau-kosara-2016.md).

## "Matrices beat node-link diagrams above twenty nodes"

**Status: scope-limited. The scope is far narrower than the quote implies, and a larger study comes out the other way.**

Ghoniem et al. (2004) found it for **static** displays of **random** graphs with 20-100 nodes and **link density 0.2 to 0.6**. Real networks are one to two orders of magnitude sparser. Okoe et al. (2018), with two real networks near density 0.03, interaction and 864 participants, found node-link better for topology, connectivity and memorability. Node-link's failure mode is edge occlusion, which tracks density rather than node count, and interaction rescues the tasks it is worst at.

**Accurate phrasing:** density and group-structure tasks favor matrices; sparsity, interaction, and topology or path tasks favor node-link. Size alone does not decide it.

Detail: [studies/ghoniem-2004.md](studies/ghoniem-2004.md), [studies/okoe-2018.md](studies/okoe-2018.md).

## "Bertin's seven visual variables"

**Status: the number is wrong.**

Bertin describes **eight**: the two dimensions of the plane plus six retinal variables. Lists of seven merge the plane into one "position" entry, but the plane having *two* dimensions is why Bertin treats it as the only component carrying every perceptual property. His ordering is not an accuracy ranking. He puts area second among retinal variables, where Cleveland and McGill measure it at rank 4. He ran no experiments; what *Sémiologie Graphique* calls "Tests" are reader-administered demonstrations.

Detail: [people/jacques-bertin.md](people/jacques-bertin.md).

## A preprint to use directionally only

**Anand & Chattaraj, *Instruction Stacking Collapse* (arXiv:2608.02639).** Follow rate falls from ~0.96 at one instruction to 0.604 (Sonnet), 0.433 (Gemini) and 0.201 (GPT-5-mini) at twenty. The numbers are verbatim correct, and the authors ran a pre-registration scorecard and report a prediction they got wrong. It is unreviewed, with three models, one primary task, an abbreviated verifier audit, and no comparison against a competently hand-written prompt. **Its own Table 7 breaks the capability-graded remediation story**: the Anthropic ladder is non-monotonic (Haiku +9.0, Sonnet -6.7, Opus -2.0). The per-model figures are not settled.

No page: it is an LLM paper, not a visualization source.

## "Chord diagrams are harder to read than Sankey diagrams"

**Status: supported, at effect sizes of 0.02 and 0.001 against the paper's own 0.01 threshold for small.**

Gutwin, Mairena & Bandi (2023) ran 51 novices through 2,040 trials on static chord and Sankey drawings of the same data, and the Sankey won on every measure. "More errors" is 0.11 per question at generalized η² = **0.001**, and it fades: "By the fourth iteration, there is little difference between the two types." 42 of 51 preferred the Sankey, and 43 of 51 believed they were more accurate with it, against a measured gap of a ninth of an error. The three mechanisms offered for the chord penalty are the three things hover highlighting fixes.

**Accurate phrasing:** for a static, one-look audience, a Sankey is read faster and with much less reported effort than an equivalent chord diagram, and is strongly preferred. The accuracy difference is negligible, the speed difference mostly disappears with familiarity, and nothing here has been tested with interaction.

Detail: [studies/gutwin-2023-chord-vs-sankey.md](studies/gutwin-2023-chord-vs-sankey.md).

## "Horizontal bar charts are read less accurately than vertical ones"

**Status: measured, and conditional on a viewing geometry a screen does not have.**

[Siqueira Rodrigues, Israel & Kosch (2026)](studies/siqueira-rodrigues-2026-vr-graphical-perception.md) had 13 participants in a head-mounted display read ratios off bar charts on a virtual wall. Collapsed across positions, horizontal bars gave 6.40% mean absolute error against 3.33% for vertical, a gap of 3.07 percentage points at d = 2.46 and generalized η² = .49. The abstract says horizontal bars "produced higher error and greater between-participant variability than vertical bar charts."

Face-on, the orientations did not differ (p = .713). The gap appears only at lateral offsets of 2.75 m and 4.8125 m, where a horizontal bar's value axis runs along the perspective foreshortening. Horizontal error rose monotonically with offset; no vertical pairwise contrast was significant (p = .942, .998, .960). The authors blame the apparatus, a virtual wall with no bezels to serve as length references, and call the result "consistent with the removal of bezel-based spatial anchors rather than a fundamental change in the perceptual hierarchy." Two of their three mechanisms are properties of the headset optics.

**Accurate phrasing:** in a head-mounted display, a bar chart viewed at an oblique angle is read less accurately when its bars extend along the foreshortened axis. Nothing here has been tested on a display the reader faces squarely, where the same experiment found no difference, and this corpus contains no study of bar orientation on a flat screen. The style-guide practice of turning bars horizontal to fit long category labels is untouched.

Detail: [studies/siqueira-rodrigues-2026-vr-graphical-perception.md](studies/siqueira-rodrigues-2026-vr-graphical-perception.md), [chart-types/bar-chart.md](chart-types/bar-chart.md).

## "Parallel coordinates beat scatterplots for negative correlations"

**Status: the asymmetry is measured, the lead is not. A reanalysis of the same data removed it.**

[Harrison et al. (2014)](studies/harrison-2014-ranking-correlation.md) had 1,687 crowdsourced participants tell two correlations apart on nine forms. Parallel coordinates with negative data performed as well as scatterplots, and with positive data far worse (p < 0.001). Their total ranking placed parallel coordinates with negative data above the scatterplot with negative data at r = 0.1, 0.3 and 0.5, and the paper proposed layout algorithms that flip axes "to maximize the number of negative correlations depicted." The ranking carried no uncertainty and was fit to condition means.

Kay & Heer (2016) refit the released data on individual observations with a log transform, censored regression and a participant effect:

> "We believe that these design recommendations overstate the strength of evidence. By contrast, our model finds that the performance of scatterplots and parallel coordinates are virtually indistinguishable at those values of r for negatively-correlated data, and that when considering variance between individuals, scatterplots may even be better."

The twelve-pair total ranking became four groups, and the best-fitting model "deviates from Weber's Law," which the original paper had reported as holding for every form.

**Accurate phrasing:** with two axes, parallel coordinates showing a negative correlation are read as precisely as a scatterplot, and showing a positive one about two precision groups worse. Nothing licenses a lead over the scatterplot, and the scatterplot is the only form in the top group for both directions.

Detail: [studies/harrison-2014-ranking-correlation.md](studies/harrison-2014-ranking-correlation.md), [chart-types/parallel-coordinates.md](chart-types/parallel-coordinates.md).
