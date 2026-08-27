# Refutations: rules that did not survive reading the source

The point of this file is that you don't redo this work. Each entry is something widely repeated that changed, weakened, or died when someone opened the primary source.

Every quote below was **re-extracted locally with `pdftotext`**, not taken from a fetch summary. That precaution exists for a reason: see [Retrieval hazards](../CONTRIBUTING.md#retrieval-hazards).

Retrieval date throughout: **2026-08-22**.

---

## "Bank to 45 degrees"

**Status: not refuted, scope-limited. The stronger word is wrong.**

Cleveland's aspect-ratio guidance is in every visualization curriculum. Talbot, Gerth & Hanrahan (*An Empirical Model of Slope Ratio Comparisons*, InfoVis 2012) expanded the experimental design and found:

> "we find that, in general, slope ratio errors are not minimized around 45°"

and

> "this effect leads to a shift in the minimum location from near 45° to below 30°"

attributing the original result to a design that "only tested moderate slope ratios and moderate mid-angles."

**Two things a careless citation drops.** The "below 30°" shift appears under *Quality of the ANGLE Submodel* and describes only the ANGLE strategy, not the HEIGHT strategy Cleveland's subjects were instructed to use. And Cleveland replicates inside his own range:

> "while the Cleveland et al. model fit our data well **in the regions considered in the original study**, it fails to extrapolate to either larger mid-angles or smaller true slope percentages"

The authors' own summary is deflationary rather than triumphal: "the theory of aspect ratio selection is not as simple as it once seemed. Minimizing the error in slope ratio estimation does not directly lead to a simple design guideline." Their constructive result is that flatter and wider ratios than banking methods produce should be preferred.

**Accurate phrasing:** 45° is not the error-minimizing ratio in general; Cleveland's result holds within the moderate regime he tested and does not extrapolate.

**Bonus finding from the same paper, worth carrying forward:** "visible baselines can substantially mitigate errors made in slope judgments," which independently supports the zero-baseline rule from an unrelated direction.

## Axis-break glyphs as the truncation remedy

**Status: the tested designs did not measurably help. "Placebo" overstates it.**

Correll, Bertini & Franconeri, *Truncating the Y-Axis: Threat or Menace?* (CHI 2020):

> "Our results fail to support our first hypothesis: there was no significant difference between perceived severity among visualization designs (F(2, 60) = 3.1, p = 0.05). A post-hoc pairwise t-test with a Bonferroni correction failed to find any significant difference between visualization designs."

and

> "the exaggeration introduced through truncation appears to persist across chart types and chart designs, and even when participants make accurate reports of the numbers they observe"

**Why "placebo" is too strong.** Critical F(2,60) at α=.05 is 3.1504 and the observed 3.1 sits just under it, so exact p ≈ 0.052. This is a knife-edge failure to reject, not evidence of no effect, and no equivalence test or Bayes factor is reported. Power is thin: 32 participants in Experiment Two, 25 in Experiment Three. The authors scope it themselves: "we tested only two potential designs for indicating axis truncation in bar charts... we focused only on methods for static charts."

Their own conclusion is hedged: "Merely indicating that truncation has occurred, even in a prominent and unambiguous way, **may not be sufficient** to 'de-bias' viewers." And they refuse the maximalist reading in the other direction too: "we resist the interpretation... that all charts with quantitative axes should include 0... We reject the unequivocal dichotomy of 'honest' and 'dishonest' charts."

**Accurate phrasing:** the tested break-glyph and gradient designs did not measurably reduce the exaggeration, so do not rely on a jagged-axis marker to make truncation honest.

## A flat ban on dual axes

**Status: absence of evidence, not evidence of harm.**

Every strong statement traces to design authority (Few, Datawrapper, practitioner guides), not experiment. The paper usually cited, Isenberg, Bezerianos, Dragicevic & Fekete, *A Study on Dual-Scale Data Charts* (IEEE TVCG / InfoVis 2011), tested **dual-scale focus-plus-context** charts, meaning two magnifications of the same series, not two different variables on two scales. Its superimposed condition is a near neighbor of the twin-axis chart, and the authors note "Superimposed charts are commonly used when two data sets have only one axis in common," but the stimulus they ran was the focus-plus-context variant.

The same paper states the gap plainly:

> "Several experts discuss problems with the Dual-Scale chart... and recommend careful design or to avoid using it altogether. Yet, empirical evidence on the effectiveness of the Dual-Scale compared to other charts is missing."

There is also a published defense of the form in the literature ("Dual Y Axes Charts Defended"), which further undercuts a flat ban.

**The person most often cited for the ban never stated it flatly.** Few's 2008 article on dual-scaled axes ends: "I certainly cannot conclude, once and for all, that graphs with dual-scaled axes are never useful... I invite you to propose viable exceptions." The absolute version is downstream of him, not from him.

**The authorities have since softened, which was checked against the current primaries on 2026-08-23.** The Urban Institute style guide still lists dual axes under its absolutes, but its current text names two explicit exceptions: unit translations such as Fahrenheit against Celsius, and Pareto charts. And **Datawrapper now ships a dual-axis chart type as a product feature**. The contrast is instructive: the same company hard-blocks truncated bar axes in its product while building dual-axis support on purpose, which is a company treating one of these as a correctness issue and the other as a design choice. So the position is not merely unsupported by experiment; the sources most often cited for it no longer state it flatly.

**Accurate phrasing:** a caution with its reason. The apparent correlation is a free parameter of your scaling choice, so prefer two stacked panels sharing an x-axis, and if you keep the twin axis, say what each scale was pinned to.

## "Log scales are fine for expert audiences"

**Status: does not hold.**

A survey of 623 Ecological Society of America members found log-log comprehension at **56%** against **93%** for linear-linear (Menge et al., *Nature Ecology & Evolution* 2018). Romano, Sotis, Dominioni & Guidi (*Health Economics* 2020) found that readers exposed to a logarithmic scale "have a less accurate understanding of how the pandemic unfolded until now, make less accurate predictions on its future, and have different attitudes and policy preferences," recommending linear "at least as a default option."

**Caveat on this entry:** the Menge percentages were reached in **secondary form only**. The direction is triple-sourced; the exact figures are not primary-verified.

## Chartjunk and the data-ink ratio as settled

**Status: contested, but not in the shape it is usually described. The sharper reading is below.**

The lazy version of this entry says "the record is contested in both directions, so nobody gets to claim it." That is true enough to stop someone overclaiming, and it is not what the papers actually say. Once each was read as a primary, a better distinction appeared.

**Decoration *around* the marks is contested. Deformation *of* the marks is not.**

Bateman et al. (*Useful Junk?*, CHI 2010) tested Holmes-style charts, which wrap imagery around a correctly drawn bar with a flat top. They found accuracy "no worse than for plain charts" and better recall after two to three weeks. Skau et al. (2015) deformed the bars themselves, changing their shape, and found error rates rise. Under Skau's own proposed mechanism, that readers project from the bar's strong horizontal terminator onto the axis, a Holmes bar should read accurately, which is exactly what Bateman found. **The two results are compatible**, and the useful rule is: keep the mark's geometry honest, and argue separately about what surrounds it.

**On the data-ink ratio specifically, an earlier version of this entry was one-sided.** Gillan & Richman's Experiment 1 *supports* Tufte: the abstract reports that "the higher the data-ink ratio, the faster the response time and the greater the accuracy." The element-conditional finding, that removing the y-axis line and the x axis generally *increased* response time while tick marks did the opposite, comes from the later experiments. The honest reading is that **the aggregate direction is Tufte's and the element-level decomposition is not**, so "maximize" fails as a mechanical instruction while surviving as a direction of travel. Gillan also found pictorial backgrounds hurt both speed and accuracy, which is 1994 evidence against embellishment that the pro-embellishment side of this debate tends to drop.

**Bateman's headline recall result does not replicate cleanly.** A four-way replication (Syeda et al. 2023, open access) found **no significant differences on any of the four long-term questions** in the asynchronous study, while synchronous replications matched. What is robust across all five studies is *preference*; what replicates best is description accuracy holding up. The original's directional tests were one-tailed at α = .05 with no multiple-comparison correction. Also usually dropped from summaries in the other direction: Bateman found a significant advantage for embellished charts on the value-message description score (p = .003).

The critique of Bateman that was previously unreachable is **Li & Moacdieh 2014, *Is "chart junk" useful?*** It attacks the two limits Bateman named themselves, unlimited viewing time and small data sets. Its body is paywalled and it does not state the direction of its chart-type effects, so do not attribute one.

**A minimization Tufte proposed was tested directly and lost.** Wickham and Stryjewski report that Stock and Behrens (1991) found Tufte's box-less *midgap* plot, his data-ink-minimized replacement for the box plot, "substantially less accurate than the original." That is the cleanest case available: a specific reduction, tested against the thing it reduced, performing worse. Reported rather than primary; Stock and Behrens itself was not reached.

**Accurate phrasing:** strip decoration, keep orientation, and never deform the mark. "Maximize" is the verb the element-level data does not support.

See [studies/bateman-2010-useful-junk.md](studies/bateman-2010-useful-junk.md), [studies/skau-2015-embellished-bars.md](studies/skau-2015-embellished-bars.md) and [studies/gillan-richman-1994-data-ink.md](studies/gillan-richman-1994-data-ink.md).

## "Gray plus one accent" as an evidence-backed rule

**Status: no controlled study found. Deliberate negative result.**

A search for a controlled experiment testing one-accent emphasis against two-saturated-color emphasis on chart comprehension returned nothing. The preattentive and visual-search literature supports color pop-out generally but does not test this rule.

It is a good default and it is **authority-asserted**, and it is asserted very widely. Knaflic states it verbatim in a bylined post: "A mostly neutral palette with one intentional color used sparingly is far more effective than many competing colors." It is also one of Schwabish's five core rules ("Start with Gray"). **Both attributions are now confirmed from primaries, and neither carries a study.** **That breadth is the point, not a mitigation.** A rule repeated independently by every major practitioner still has no experiment under it, and the agreement is easy to mistake for evidence. Fine as house style; not fine as an evidentiary anchor for adding sibling rules to it.

## The "broad vision-model critique fails, decomposed succeeds" comparison

**Status: refuted as a comparison. Both underlying numbers are individually correct.**

The tempting claim pairs VisJudgeBench (GPT-5 at MAE 0.553, correlation **0.428** against human experts) with VisEval (readability evaluator at SRCC **0.843** against 0.782 inter-expert), and concludes that broad quality rating fails while decomposed critique works.

It does not hold, for four reasons in descending severity:

1. **VisJudgeBench is not a broad prompt.** Its evaluation template (Appendix C.5) demands structured JSON across six named sub-dimensions with per-metric criteria. **The 0.428 is what decomposed rubric-scoring achieved.** The comparison's independent variable is not what the paper manipulated.
2. **The 0.687 is fine-tuning, not decomposition.** VisJudge is a LoRA+GRPO fine-tune of Qwen2.5-VL-7B on the same rubric.
3. **VisEval's success is substantially deterministic code.** Its layout check is not a model: "GPT-4V's accuracy in this task was not sufficiently high to be incorporated... we opted for a more reliable approach by simulating a browser environment."
4. **Non-comparable statistics and no shared ceiling.** Pearson against Spearman; real-world aesthetic quality against NL2VIS readability; and VisJudgeBench publishes **no inter-annotator agreement at all**. VisEval's 0.843 also beats 0.782 partly as an averaging artifact, since the evaluator is scored against the mean of three experts.

**What survives, and it is better:** VisEval's own within-paper ablation, 0.507 with neither deterministic sub-check to 0.843 with both. One paper, one metric, one target, one manipulated variable. It supports *deterministic sub-checks feeding a vision model beat the vision model alone*.

GPT-5's 0.428 is not the best baseline correlation in that table. GPT-4o reaches 0.482 and Qwen2.5-VL-72B 0.440; the abstract pairs the best-MAE model's MAE with that same model's correlation.

## A source that should not be cited at all

**Liu, Wang & Willard, *Effects of Prompt Length on Domain-specific Tasks for LLMs* (arXiv:2502.14255).**

Its quotes and per-task numbers check out verbatim. Two disqualifying problems:

1. **Arithmetically impossible rows.** The QIC task reports precision 0.48, recall 0.10, **F1 0.84**. The harmonic mean of 0.48 and 0.10 is about 0.17. QIC+LI repeats it: 0.54, 0.20, 0.92. The authors narrate the anomaly ("QIC shows high F1-score (0.84) but low recall (0.10)") without noticing it is impossible. **QIC supplies the paper's headline +0.08**, its largest long-prompt gain; drop it and the range shrinks to +0.01 to +0.07.
2. **The system under test is never named.** No model, version, temperature or API anywhere in the Experiments section.

Add no variance reporting, no significance testing, and deltas as small as ±0.01.

Separately, even if it were sound it would not transfer to a rules document. Its "long" is explicitly **background knowledge**: "long instructions contain at least 200% tokens of the default prompt, providing not only requirements but also background knowledge and experimental conditions." It never varies the number of simultaneous constraints.

## A published paper that contradicts itself

**Pandey, Rall, Satterthwaite, Nov & Bertini, *How Deceptive are Deceptive Visualizations?* (CHI 2015).**

Table 3, on the inverted-axis condition:

| Treatment | Selected | Correct | Incorrect | Uncertain |
|---|---|---|---|---|
| Control | 40 | 39 (97.50%) | 1 (2.5%) | 0 |
| Deceptive | 38 | 7 (18.42%) | 30 (78.95%) | 1 (0.02%) |

The Discussion says:

> "the deceptive condition led to 97.5% incorrect responses whereas the control condition led to only 18.4% incorrect responses"

It took the two **correct**-column percentages, relabeled them incorrect, *and* swapped which condition each belongs to. A third passage in the body agrees with the table, making the Discussion the outlier two-against-one.

The error is direction-preserving, so the paper's conclusion survives. But **anyone quoting 18.4% as a control error rate is off by roughly 7x** (the real figure is 2.5%). Table 3 separately misprints 1/38 as 0.02% where it should be 2.63%.

**What is *not* established:** that the field propagates the wrong figure. A search for secondary sources repeating 97.5%/18.4% found none. Do not ship that claim without naming specific offenders.

**Sound in the same paper:** "the distorted charts lead to responses between 58.5% and 129.5% bigger than the control condition" recomputes exactly from Table 2 (Line 3.19/1.39 = +129.5%, Bubble 2.71/1.71 = +58.5%).

---

## The Cleveland-McGill ranking is not a fully ordered list

**Status: scope-limited and partly untested. The version in circulation is from a different paper than the one it is cited to.**

> **Reconciled after this entry was first written.** There are **two** Cleveland & McGill rankings. The 1984 *JASA* paper below has six ranks with ties. The 1985 *Science* paper has seven ranks, fully ordered, with length and angle separated and color hue present and last. The familiar list is an accurate reproduction of the 1985 table, routinely cited to 1984. It is not a corruption; it is a misattribution. See [people/william-cleveland.md](people/william-cleveland.md) for both tables side by side.
>
> This changes the diagnosis and not the caution. The 1985 paper calls its own ordering "a tentative working hypothesis," says the authors "have been unable to distinguish the relative accuracy of some tasks," and states that "aspects of the ordering are partly conjectural in that we have no controlled experimentation to support them." Everything below still applies to the 1984 paper, which is what most people think they are citing.

The ranking everyone reproduces runs `position > length > angle > area > volume > color`, fully ordered. [Cleveland & McGill (1984)](studies/cleveland-mcgill-1984.md) p. 536 publishes **ten tasks in six ranks**, and immediately adds (p. 537):

> "Three of the ranks—3, 5, and 6—have more than one task; at the moment there is not enough information to separate the ties."

**Length, direction and angle are all rank 3.** The authors say they cannot separate them.

Three further things a careless citation drops:

**The two experiments are not comparable to each other.** Length was measured against position in one; angle against position in another. p. 541: "it would be inappropriate to compare the means of the first experiment with those of the second." So the paper contains no test of length versus angle, which is exactly why rank 3 is a tie.

**The one head-to-head test failed to find it.** [Heer & Bostock (2010)](studies/heer-bostock-2010.md) built judgment types specifically so angle could be compared with length on a common format: "Theory also suggests that angle should perform worse than length, but the results do not support this."

**Color hue is excluded, not ranked last.** p. 532: hue and texture "are two elementary tasks excluded from the list because they do not have an unambiguous single method of ordering from small to large." Rank 6 is *shading and color saturation*. A ranking that puts "color" at the bottom meaning hue is not reporting this paper.

**What survives:** position beats length (errors 40-250% larger), position beats angle (factor ~2), position beats area, angle beats area. Every one of those is measured and replicated. **What does not:** any ordering within rank 3, and the mechanism "bars beat pies because length beats angle," which is the most citable wrong thing in the category.

## "Pie charts are read by angle"

**Status: refuted by direct decomposition.**

Cleveland & McGill are usually cited for this. What they wrote (p. 533) is a conjecture, flagged as one:

> "we conjecture that the primary elementary visual task for extracting the numerical information is perception of angle, but the areas and arc lengths of the pie slices are variable and probably are also involved in judging the data"

[Skau & Kosara (2016)](studies/skau-kosara-2016.md) isolated the three cues and found angle the **worst** performer, not the primary one:

> "Error was smaller for the baseline charts, area chart, and the arc chart than the two angle-only charts. This was not what we hypothesized, and contradicts common wisdom that angles are critical to pie and donut chart perception."

Eells (1926) had already found the same by asking: 51% of participants reported using arc length, 25% area, 23% angle.

**Consequences.** Bar-beats-pie survives, measured directly, and should be stated without the mechanism. And **the standard case against donut charts collapses**: the objection is that removing the center destroys the angle, which it does, and angle was carrying the least. Skau & Kosara measured donut and pie as "virtually identical."

## "Matrices beat node-link diagrams above twenty nodes"

**Status: scope-limited. The scope is far narrower than the quote implies, and a larger study comes out the other way.**

[Ghoniem, Fekete & Castagliola (2004)](studies/ghoniem-2004.md) is real and says what it is quoted as saying. Its conditions: **static** displays, **random** graphs, 20-100 nodes, **link density 0.2 to 0.6**.

Real networks are typically one to two orders of magnitude sparser. [Okoe, Jianu & Kobourov (2018)](studies/okoe-2018.md) used two real networks near density 0.03, with interaction, 864 participants and 14 tasks, and found node-link better for topology, connectivity and memorability, with matrices winning group and cluster tasks.

Neither study is wrong. Node-link's failure mode is edge occlusion, which is driven by **density**, not node count, and interaction disproportionately rescues exactly the tasks node-link is worst at.

**Accurate phrasing:** density and group-structure tasks favor matrices; sparsity, interaction, and topology or path tasks favor node-link. Size alone does not decide it. Note also that the authors' own conclusion is the modest one: "These techniques proved to be complementary."

## "Bertin's seven visual variables"

**Status: the number is wrong, and the error is not cosmetic.**

Bertin describes **eight** variables: the two dimensions of the plane, plus six retinal variables. Lists of seven have collapsed the plane into a single "position" entry.

That collapse breaks the argument it came from. The plane having *two* dimensions is precisely why Bertin treats it as the only component carrying every perceptual property, and why planar position sits above everything retinal. Flatten it to one and the reason for the hierarchy disappears.

Two further things a citation usually gets wrong:

- **His ordering is not an accuracy ranking**, and it disagrees with the measured one in a checkable place. He puts area second among retinal variables and calls it the only quantitative one; Cleveland and McGill measure area at rank 4. See [studies/cleveland-mcgill-1984.md](studies/cleveland-mcgill-1984.md).
- **He ran no experiments.** What *Sémiologie Graphique* calls "Tests" are reader-administered demonstrations across facing-page figures, not measurements. He is the foundational source for the vocabulary and an `authority-asserted` source for every ranking in it.

See [people/jacques-bertin.md](people/jacques-bertin.md).

## A preprint to use directionally only

**Anand & Chattaraj, *Instruction Stacking Collapse* (arXiv:2608.02639).** Follow rate falls from ~0.96 at one instruction to 0.604 (Sonnet), 0.433 (Gemini), 0.201 (GPT-5-mini) at twenty.

The numbers are verbatim correct and the authors are unusually careful: they run a pre-registration scorecard and report a prediction they got wrong, and they state against their own interest that "our benchmark measures compliance, not the correctness or safety of content."

But: three weeks old at time of reading, unreviewed, three models, one primary task, an abbreviated verifier audit (500 labels, 3 verifiers spot-checked), never compared against a competently hand-written prompt, and **their own Table 7 breaks the capability-graded remediation story** (Anthropic ladder non-monotonic: Haiku +9.0, Sonnet -6.7, Opus -2.0).

Directional use only. Do not quote the per-model figures as settled.
