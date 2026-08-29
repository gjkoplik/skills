# Refutations: rules that did not survive reading the source

Widely repeated claims that changed, weakened, or died when someone opened the primary source. Each entry is short on purpose: the numbers and the design live on the linked page, so this file can be scanned rather than read.

Every quote was **re-extracted locally**, not taken from a fetch summary. See [Retrieval hazards](../CONTRIBUTING.md#retrieval-hazards). Retrieval date **2026-08-22** except where an entry says otherwise; extraction was `pdftotext` except where the linked page records otherwise.

## What is in here

| The claim as it circulates | Verdict | What is actually true |
|---|---|---|
| ["Bank to 45 degrees"](#bank-to-45-degrees) | Scope-limited | 45° is not error-minimizing in general; Cleveland's result holds inside the moderate regime he tested |
| [Axis-break glyphs fix truncation](#axis-break-glyphs-as-the-truncation-remedy) | Tested, no measurable help | Two static designs failed to reduce the exaggeration. "Placebo" overstates a knife-edge result |
| [A flat ban on dual axes](#a-flat-ban-on-dual-axes) | Absence of evidence | No experiment tests the twin-axis chart. The paper usually cited studied something else, and the authorities have softened |
| ["Log scales are fine for experts"](#log-scales-are-fine-for-expert-audiences) | Does not hold | Domain experts read log-log at 56% against 93% for linear |
| [Chartjunk and data-ink are settled](#chartjunk-and-the-data-ink-ratio-as-settled) | Contested, but not in the usual shape | Decoration *around* the mark is contested; deformation *of* the mark is not |
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

---

## "Bank to 45 degrees"

**Status: not refuted, scope-limited. The stronger word is wrong.**

Talbot, Gerth & Hanrahan (InfoVis 2012) expanded the experimental design:

> "we find that, in general, slope ratio errors are not minimized around 45°"

Two things a careless citation drops. The "below 30°" shift they report describes only the ANGLE strategy, not the HEIGHT strategy Cleveland's subjects were instructed to use. And Cleveland replicates inside his own range: the model "fit our data well **in the regions considered in the original study**" and fails to extrapolate beyond it.

**Accurate phrasing:** 45° is not the error-minimizing ratio in general; Cleveland's result holds within the moderate regime he tested and does not extrapolate.

The same paper's baseline finding is often cited alongside this one as independent support for zero baselines. It does not reach that far: baselines helped for mid-angles below 45° and did nothing above. Detail: [studies/talbot-2012-slope-ratio.md](studies/talbot-2012-slope-ratio.md).

## Axis-break glyphs as the truncation remedy

**Status: the tested designs did not measurably help. "Placebo" overstates it.**

Correll, Bertini & Franconeri (CHI 2020):

> "the exaggeration introduced through truncation appears to persist across chart types and chart designs, and even when participants make accurate reports of the numbers they observe"

The failure to reject was knife-edge (observed F(2,60) = 3.1 against a critical 3.1504, so p ≈ 0.052) on 32 and 25 participants, across two static designs. The authors refuse the maximalist reading in both directions: "We reject the unequivocal dichotomy of 'honest' and 'dishonest' charts."

**Accurate phrasing:** the tested break-glyph and gradient designs did not measurably reduce the exaggeration. A jagged-axis marker is not established as a remedy for it.

Detail: [studies/correll-2020-truncating-the-y-axis.md](studies/correll-2020-truncating-the-y-axis.md).

## A flat ban on dual axes

**Status: absence of evidence, not evidence of harm.**

Every strong statement traces to design authority, not experiment. The paper usually cited, Isenberg et al. (2011), tested **dual-scale focus-plus-context** charts, meaning two magnifications of one series, not two variables on two scales. It states the gap itself:

> "empirical evidence on the effectiveness of the Dual-Scale compared to other charts is missing"

Two further facts. Few, the person most cited for the ban, never stated it flatly: "I certainly cannot conclude, once and for all, that graphs with dual-scaled axes are never useful." And the authorities have since softened, checked against current primaries on 2026-08-23: Urban names two explicit exceptions, and Datawrapper ships a dual-axis chart type as a product feature while hard-blocking truncated bar axes.

**Accurate phrasing:** a caution with its reason rather than a ban. The apparent correlation between the two series is a free parameter of the scaling choice, and nothing on the chart records what each scale was pinned to.

Detail: [studies/isenberg-2011-dual-scale-charts.md](studies/isenberg-2011-dual-scale-charts.md), [people/stephen-few.md](people/stephen-few.md).

## "Log scales are fine for expert audiences"

**Status: does not hold.**

623 Ecological Society of America members read log-log at **56%** against **93%** for linear-linear. Readers given a logarithmic scale "have a less accurate understanding of how the pandemic unfolded until now, make less accurate predictions on its future, and have different attitudes and policy preferences."

The direction is triple-sourced. The Menge percentages were reached in **secondary form only** and are not primary-verified.

Detail: [studies/menge-2018-log-scales.md](studies/menge-2018-log-scales.md), [studies/romano-2020-log-scales-covid.md](studies/romano-2020-log-scales-covid.md).

## Chartjunk and the data-ink ratio as settled

**Status: contested, but not in the shape it is usually described.**

**Decoration *around* the marks is contested. Deformation *of* the marks is not.** Bateman et al. (2010) wrapped imagery around a correctly drawn bar and found accuracy "no worse than for plain charts". Skau et al. (2015) deformed the bars themselves and found error rises. The two results are compatible under Skau's own mechanism.

On the data-ink ratio, the record splits by level. Gillan & Richman's Experiment 1 supports Tufte in aggregate ("the higher the data-ink ratio, the faster the response time and the greater the accuracy"); the element-level findings from their later experiments do not. Bateman's long-term recall result does not replicate cleanly: a four-way replication (Syeda et al. 2023) found no significant differences on any of the four long-term questions in the asynchronous study.

One Tufte minimization was tested directly and lost: Stock and Behrens (1991) found his box-less *midgap* plot "substantially less accurate than the original."

**Accurate phrasing:** the evidence separates decoration around the mark, which is contested, from deformation of the mark, which is not. "Maximize" is the verb the element-level data does not support.

Detail: [studies/bateman-2010-useful-junk.md](studies/bateman-2010-useful-junk.md), [studies/skau-2015-embellished-bars.md](studies/skau-2015-embellished-bars.md), [studies/gillan-richman-1994-data-ink.md](studies/gillan-richman-1994-data-ink.md), [chart-types/boxplot.md](chart-types/boxplot.md).

## "Gray plus one accent" as an evidence-backed rule

**Status: no controlled study found. Deliberate negative result.**

A search for a controlled experiment testing one-accent emphasis against two-saturated-color emphasis on chart comprehension returned nothing. The preattentive and visual-search literature supports color pop-out generally and does not test this rule.

It is `authority-asserted` and asserted very widely: Knaflic states it verbatim in a bylined post, and it is one of Schwabish's five core rules ("Start with Gray"). Both attributions are confirmed from primaries and neither carries a study. The breadth is the risk rather than a mitigation, because agreement across every major practitioner is easy to mistake for evidence.

Detail: [people/cole-nussbaumer-knaflic.md](people/cole-nussbaumer-knaflic.md), [people/jonathan-schwabish.md](people/jonathan-schwabish.md).

## The "broad vision-model critique fails, decomposed succeeds" comparison

**Status: refuted as a comparison. Both underlying numbers are individually correct.**

The tempting claim pairs VisJudgeBench (GPT-5, correlation **0.428** against human experts) with VisEval (readability evaluator at SRCC **0.843**) and concludes that broad quality rating fails while decomposed critique works. Four reasons it does not hold, in descending severity:

1. **VisJudgeBench is not a broad prompt.** Its template demands structured JSON across six named sub-dimensions. The 0.428 *is* what decomposed rubric-scoring achieved, so the comparison's independent variable is not what the paper manipulated.
2. **The 0.687 is fine-tuning, not decomposition**, a LoRA+GRPO fine-tune of Qwen2.5-VL-7B on the same rubric.
3. **VisEval's success is substantially deterministic code.** Its layout check simulates a browser rather than calling a model.
4. **Non-comparable statistics and no shared ceiling.** Pearson against Spearman, different targets, and VisJudgeBench publishes no inter-annotator agreement at all.

**What survives, and it is better:** VisEval's own within-paper ablation, 0.507 with neither deterministic sub-check to 0.843 with both. One paper, one metric, one manipulated variable, supporting *deterministic sub-checks feeding a vision model beat the vision model alone*.

No page: these two benchmarks have none in this corpus.

## A source that should not be cited at all

**Liu, Wang & Willard, *Effects of Prompt Length on Domain-specific Tasks for LLMs* (arXiv:2502.14255).** Quotes and per-task numbers check out verbatim. Two disqualifying problems:

1. **Arithmetically impossible rows.** The QIC task reports precision 0.48, recall 0.10, **F1 0.84**; the harmonic mean of 0.48 and 0.10 is about 0.17. QIC supplies the paper's headline +0.08, and dropping it shrinks the range to +0.01 to +0.07.
2. **The system under test is never named.** No model, version, temperature or API anywhere in the Experiments section.

No variance reporting, no significance testing, deltas as small as ±0.01. Separately, its "long" condition varies **background knowledge**, never the number of simultaneous constraints, so it would not transfer to a rules document even if it were sound.

No page: it is an LLM paper, not a visualization source.

## A published paper that contradicts itself

**Pandey et al., *How Deceptive are Deceptive Visualizations?* (CHI 2015).** Table 3 reports the inverted-axis control condition as 39/40 correct (97.50%) and the deceptive condition as 7/38 correct (18.42%). The Discussion says:

> "the deceptive condition led to 97.5% incorrect responses whereas the control condition led to only 18.4% incorrect responses"

It took the two **correct**-column percentages, relabeled them incorrect, and swapped which condition each belongs to. A third passage agrees with the table, making the Discussion the outlier two-against-one.

The error is direction-preserving, so the conclusion survives, but **quoting 18.4% as a control error rate is off by roughly 7x**; the real figure is 2.5%. Not established: that the field propagates the wrong figure. A search for secondary sources repeating it found none.

Detail: [studies/pandey-2015-deceptive-visualizations.md](studies/pandey-2015-deceptive-visualizations.md).

## The Cleveland-McGill ranking is not a fully ordered list

**Status: scope-limited and partly untested. The version in circulation is from a different paper than the one it is cited to.**

There are **two** rankings. The 1984 *JASA* paper has ten tasks in six ranks with ties; the 1985 *Science* paper has seven ranks, fully ordered, with length and angle separated and color hue present and last. The familiar list reproduces the 1985 table and is routinely cited to 1984. A misattribution rather than a corruption.

The 1984 paper says of its own ties:

> "Three of the ranks—3, 5, and 6—have more than one task; at the moment there is not enough information to separate the ties."

**Length, direction and angle are all rank 3**, its two experiments are not comparable to each other, and the one head-to-head test since (Heer & Bostock 2010) failed to separate angle from length. **Color hue is excluded, not ranked last**: rank 6 is *shading and color saturation*.

**What survives:** position beats length, angle, and area, and angle beats area, all measured and replicated. **What does not:** any ordering within rank 3, and the mechanism "bars beat pies because length beats angle".

Detail: [studies/cleveland-mcgill-1984.md](studies/cleveland-mcgill-1984.md), [people/william-cleveland.md](people/william-cleveland.md), [studies/heer-bostock-2010.md](studies/heer-bostock-2010.md).

## "Pie charts are read by angle"

**Status: refuted by direct decomposition.**

Cleveland & McGill are cited for this. What they wrote is flagged as a conjecture: "we conjecture that the primary elementary visual task for extracting the numerical information is perception of angle". Skau & Kosara (2016) isolated the three cues and found angle the **worst** performer:

> "This was not what we hypothesized, and contradicts common wisdom that angles are critical to pie and donut chart perception."

Eells (1926) had already found the same by asking. Two consequences: bar-beats-pie survives, measured directly, and is stated without the mechanism; and the standard case against donut charts collapses, since it rests on the cue that was carrying the least.

Detail: [studies/skau-kosara-2016.md](studies/skau-kosara-2016.md).

## "Matrices beat node-link diagrams above twenty nodes"

**Status: scope-limited. The scope is far narrower than the quote implies, and a larger study comes out the other way.**

Ghoniem et al. (2004) says what it is quoted as saying, under conditions of **static** displays, **random** graphs, 20-100 nodes and **link density 0.2 to 0.6**. Real networks are one to two orders of magnitude sparser. Okoe et al. (2018) used two real networks near density 0.03, with interaction and 864 participants, and found node-link better for topology, connectivity and memorability.

Neither is wrong: node-link's failure mode is edge occlusion, driven by density rather than node count, and interaction rescues the tasks it is worst at.

**Accurate phrasing:** density and group-structure tasks favor matrices; sparsity, interaction, and topology or path tasks favor node-link. Size alone does not decide it.

Detail: [studies/ghoniem-2004.md](studies/ghoniem-2004.md), [studies/okoe-2018.md](studies/okoe-2018.md).

## "Bertin's seven visual variables"

**Status: the number is wrong, and the error is not cosmetic.**

Bertin describes **eight**: the two dimensions of the plane, plus six retinal variables. Lists of seven collapse the plane into a single "position" entry, which breaks the argument it came from, since the plane having *two* dimensions is why Bertin treats it as the only component carrying every perceptual property.

Two further things a citation gets wrong. His ordering is not an accuracy ranking, and it disagrees with the measured one in a checkable place: he puts area second among retinal variables while Cleveland and McGill measure it at rank 4. And he ran no experiments; what *Sémiologie Graphique* calls "Tests" are reader-administered demonstrations.

Detail: [people/jacques-bertin.md](people/jacques-bertin.md).

## A preprint to use directionally only

**Anand & Chattaraj, *Instruction Stacking Collapse* (arXiv:2608.02639).** Follow rate falls from ~0.96 at one instruction to 0.604 (Sonnet), 0.433 (Gemini), 0.201 (GPT-5-mini) at twenty.

The numbers are verbatim correct and the authors are careful, running a pre-registration scorecard and reporting a prediction they got wrong. But: unreviewed, three models, one primary task, an abbreviated verifier audit, never compared against a competently hand-written prompt, and **their own Table 7 breaks the capability-graded remediation story** (Anthropic ladder non-monotonic: Haiku +9.0, Sonnet -6.7, Opus -2.0). The per-model figures are not settled.

No page: it is an LLM paper, not a visualization source.

## "Chord diagrams are harder to read than Sankey diagrams"

**Status: supported, at effect sizes of 0.02 and 0.001 against the paper's own 0.01 threshold for small. Retrieved 2026-08-29.**

The primary supports the claim: Gutwin, Mairena & Bandi (2023) ran 51 novices through 2,040 trials on static chord and Sankey drawings of the same data, and the Sankey won on every measure. What the abstract does not carry is the size. "More errors" is 0.11 per question at generalized η² = **0.001**, a tenth of that paper's own threshold for small. The gap is a first-exposure effect: "By the fourth iteration, there is little difference between the two types."

The large effect is preference, not performance: 42 of 51 preferred the Sankey, and 43 of 51 believed they were more accurate with it when the measured gap was a ninth of an error. The stimuli were static, and the three mechanisms offered for the chord penalty are the three things hover highlighting fixes.

**Accurate phrasing:** for a static, one-look audience, a Sankey is read faster and with much less reported effort than an equivalent chord diagram, and is strongly preferred. The accuracy difference is negligible, the speed difference mostly disappears with familiarity, and nothing here has been tested with interaction.

Detail: [studies/gutwin-2023-chord-vs-sankey.md](studies/gutwin-2023-chord-vs-sankey.md).
