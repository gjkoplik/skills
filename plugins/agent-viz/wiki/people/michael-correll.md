---
type: person
status: primary-read
retrieved: 2026-08-29
---

# Michael Correll

**What they are known for.** Correll is the author most often cited in this corpus for rules stronger than his papers state. The flat "never truncate an axis" and the flat "never use bar-and-whisker error bars" both trace to work he co-wrote, and both papers explicitly decline to say that. Alongside the experiments he runs a steady program of position papers arguing that the field's evaluations, and its central channel ranking, measure something narrower than what they get used for.

**How this was read.** Four arXiv preprints downloaded and extracted locally with PyMuPDF, with the title on the first page checked against the identifier before anything was quoted: 1811.07271v2, 2001.02316v1, 2008.11250v1 and 2008.11310v3. Those are author preprints rather than the publisher's versions, and no claim is made that the published text is word-identical. Added to that are this wiki's existing primary readings of [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) and [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md). Affiliation as printed on the papers is Tableau Research; no claim is made about where he works now.

**What they are good for.** Rules stated more strongly than the studies behind them. He is this corpus's most reliable supplier of the author's own hedge, usually written into the paper's own discussion. Also the argument that the channel ranking the whole chart-type tier inherits from is scoped to one narrow family of tasks, which bears directly on [concepts/channels.md](../concepts/channels.md).

**What they do not settle.** Almost nothing on his own. His two experiments in this corpus are both about how uncertainty and axis scaling change a *decision*, not about how a mark is read, and he has run no channel decomposition of the kind [Robert Kosara](robert-kosara.md) specializes in. The channel-ranking critique is a co-authored position paper with no experiment in it, and it says in as many words that it is not proposing to discard the ranking. Nothing here bears on color, layout, networks or maps.

---

## What their work actually established

### The two experiments this wiki already rests on

**Error bars, 2014, with Michael Gleicher.** The encoding of uncertainty changes the inference, and gradient and violin encodings beat bar-and-whisker for judging whether a difference is real. Full treatment at [studies/correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md).

**Truncation, 2020, with Enrico Bertini and Steven Franconeri.** Truncation's exaggeration effect persists across chart types and designs, and the two axis-break designs tested did not measurably reduce it. Full treatment at [studies/correll-2020-truncating-the-y-axis.md](../studies/correll-2020-truncating-the-y-axis.md). The part worth coming back for is the authors' refusal of the strong reading in *both* directions, including "We reject the unequivocal dichotomy of 'honest' and 'dishonest' charts."

### The challenge to this wiki's own spine

**Bertini, Correll & Franconeri, *Why Shouldn't All Charts Be Scatter Plots? Beyond Precision-Driven Visualizations* (2020, arXiv 2008.11310).** It bears directly on [concepts/channels.md](../concepts/channels.md), and it is a **position paper with no experiment in it**. It attacks a strawman it names as a strawman, and the attack lands on a real assumption:

> "There is an implicit assumption that the ranking derived from this two-value ratio judgment represents an atomic unit for visualization, so that the additional precision conveyed by position should transfer to better perceptual performance in more complex tasks. We challenge this assumption."

Their Table 1 lays out a dozen value-related tasks (ordinal comparison, min or max identification, summarization, clustering, extrapolation, shape and trend, filtering, correlation) against which the ratio judgment is one row, and their gloss on it is the citable claim:

> "Our recommendations for visual encodings and visualization designs are often related to only a narrow set of these tasks (often the first two, dealing with individual pairs of values). Empirical evidence about the precision of visual encodings for other tasks is often sparse or counter to existing recommendations."

The specific evidentiary gap they name is checkable: on the ordinal and multi-pair tasks, "We know of only two studies that have studied these important perceptual tasks... but because both rely primarily on position encodings, they cannot confirm whether the Cleveland & McGill position ranking holds for these alternative tasks."

**They are careful about the size of the claim**, which is why this belongs on a page about overstatement rather than in [refutations.md](../refutations.md):

> "Of course we are not proposing to throw the baby out with the bathwater. The ranking of visual variables has had enormous impact on visualization research and practice"

and their conclusion is a scope claim rather than a contradiction: "these rankings do not seem to capture important components of how people use, interpret, and learn from visualizations."

**Their opening exhibit is Minard.** Figure 1 puts Minard's march-on-Moscow map beside a recreation of the same data encoded entirely as position on a common axis, and asks when the first would be preferred. That is the argument [chart-types/flow-map.md](../chart-types/flow-map.md) is standing on from the other side, and the honest reading of both is that the question is open.

### Mirages

**McNutt, Kindlmann & Correll, *Surfacing Visualization Mirages* (CHI 2020, arXiv 2001.02316).** It names a failure mode and then tries to detect it mechanically:

> "Dirty data and deceptive design practices can undermine, invert, or invalidate the purported messages of charts and graphs. These failures can arise silently: a conclusion derived from a particular visualization may look plausible unless the analyst looks closer and discovers an issue with the backing data, visual specification, or their own assumptions. We term such silent but significant failures visualization mirages."

Their method is metamorphic testing borrowed from software testing: perturb the data or the chart specification in ways that should or should not change the conclusion, and flag the cases where the chart disagrees. They report that it "can reliably identify mirages across a variety of chart types with relatively little prior knowledge of the data or the domain." The claim is about their detector on their test set and is that narrow, but the framing is directly relevant to [checks/matplotlib.md](../checks/matplotlib.md), which is this wiki's own attempt at mechanical checks on a figure.

### The position papers, and what they are not

**Correll, *What Do We Actually Learn from Evaluations in the "Heroic Era" of Visualization?* (2020, arXiv 2008.11250).** A seven-page position paper arguing that visualization evaluations "fail to tell us very much that is useful or transferable about visualization systems, regardless of the statistical rigor or ecological validity of the evaluation." Written as thought experiments, with no data. Useful as a companion to [Kosara's](robert-kosara.md) *An Empire Built On Sand* and to the replication argument, and usable as evidence for nothing.

**Correll, *Ethical Dimensions of Visualization Research* (CHI 2019, arXiv 1811.07271).** His most-cited single paper and also a position paper: it "address[es] the moral components of the design and use of visualizations, identif[ies] some ongoing areas of visualization research with ethical dilemmas, and propose[s] a set of additional moral obligations." Drawn from historical and contemporary examples rather than from an experiment. It is a statement of professional obligations and it establishes no empirical fact, so it supports no evidentiary claim in this wiki's rule set.

## Where his name is used as authority for more than he showed

**"Correll proved axis-break markers don't work."** The relevant test was a knife-edge failure to reject, F(2,60) = 3.1 against a critical value of 3.1504, on 32 participants, across exactly two static designs. The paper's own verb is "may not be sufficient". See [refutations.md](../refutations.md).

**"Correll says never use error bars."** What was measured was inference about whether two means differ, on bar-and-whisker against gradient and violin encodings. It is a finding about which uncertainty encoding supports that inference, not a prohibition on a mark.

**"Correll refuted the Cleveland and McGill ranking."** He co-wrote a position paper, with two other authors, which knocks down a strawman it identifies as one, states that it is not discarding the ranking, and asks for scope rather than replacement. Nobody has run the experiment that would settle it, and the paper says so.

**A note on counting him as an independent voice.** He appears on both of this wiki's uncertainty-and-deception study pages, on the channel-ranking critique, and on the mirages paper, with overlapping co-author sets (Bertini and Franconeri on two of them). "Correll et al." citations are one voice with recurring collaborators, not several. This is the error [sources/urban-institute.md](../sources/urban-institute.md) records for Schwabish.

## See also

- [../studies/correll-2020-truncating-the-y-axis.md](../studies/correll-2020-truncating-the-y-axis.md)
- [../studies/correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md)
- [../concepts/channels.md](../concepts/channels.md) — the ranking his co-authored critique scopes
- [../chart-types/flow-map.md](../chart-types/flow-map.md) — the form their Figure 1 uses to pose the question
- [robert-kosara.md](robert-kosara.md) — the same skepticism aimed at mechanisms rather than at objectives
- [../refutations.md](../refutations.md)
