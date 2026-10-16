---
type: person
status: primary-read
retrieved: 2026-08-29
---

# Michael Correll

**What they are known for.** Being cited for rules stronger than his papers state. The flat "never truncate an axis" and "never use bar-and-whisker error bars" trace to work he co-wrote, and both papers decline to say that. He also writes position papers arguing that the field's evaluations and channel ranking measure less than they get used for.

**How this was read.** Four arXiv author preprints, extracted locally with PyMuPDF after checking each first-page title against its identifier: 1811.07271v2, 2001.02316v1, 2008.11250v1 and 2008.11310v3. The published text may differ. The two experiments come from the wiki's primary readings of [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) and [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md). Affiliation as printed is Tableau Research; no claim is made about where he works now.

**What they are good for.** The author's own hedge on an overstated rule, and the argument that the ranking behind [concepts/channels.md](../concepts/channels.md) covers a narrow family of tasks.

**What they do not settle.** How a mark is read. His two experiments here concern how uncertainty encoding and axis scaling change a *decision*, and he has run no channel decomposition of the kind [Robert Kosara](robert-kosara.md) does. The ranking critique has no experiment. Nothing here bears on color, layout, networks or maps.

---

## What their work established

### Two experiments

**Error bars, 2014, with Michael Gleicher.** Gradient and violin encodings showed none of the within-the-bar bias that bar-and-whisker did, on low-stakes predictions. [studies/correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md)

**Truncation, 2020, with Enrico Bertini and Steven Franconeri.** The exaggeration effect persists across chart types, and the two axis-break designs tested did not measurably reduce it. The authors refuse the strong reading in both directions: "We reject the unequivocal dichotomy of 'honest' and 'dishonest' charts." [studies/correll-2020-truncating-the-y-axis.md](../studies/correll-2020-truncating-the-y-axis.md)

### Scoping the channel ranking

**Bertini, Correll & Franconeri, *Why Shouldn't All Charts Be Scatter Plots? Beyond Precision-Driven Visualizations* (2020, arXiv 2008.11310).** A position paper with no experiment, attacking a strawman it names as one:

> "There is an implicit assumption that the ranking derived from this two-value ratio judgment represents an atomic unit for visualization, so that the additional precision conveyed by position should transfer to better perceptual performance in more complex tasks. We challenge this assumption."

Their Table 1 puts the ratio judgment among about a dozen value tasks (ordinal comparison, min or max identification, summarization, clustering, extrapolation, shape and trend, filtering, correlation):

> "Our recommendations for visual encodings and visualization designs are often related to only a narrow set of these tasks (often the first two, dealing with individual pairs of values). Empirical evidence about the precision of visual encodings for other tasks is often sparse or counter to existing recommendations."

On ordinal and multi-pair tasks:

> "We know of only two studies that have studied these important perceptual tasks... but because both rely primarily on position encodings, they cannot confirm whether the Cleveland & McGill position ranking holds for these alternative tasks."

It keeps the ranking, so it is not in [refutations.md](../refutations.md):

> "Of course we are not proposing to throw the baby out with the bathwater. The ranking of visual variables has had enormous impact on visualization research and practice"

It concludes that "these rankings do not seem to capture important components of how people use, interpret, and learn from visualizations." Its Figure 1 sets Minard's march-on-Moscow map beside the same data as position on a common axis and asks when the map is preferred, an open question [chart-types/flow-map.md](../chart-types/flow-map.md) argues from the other side.

### Mirages

**McNutt, Kindlmann & Correll, *Surfacing Visualization Mirages* (CHI 2020, arXiv 2001.02316).**

> "Dirty data and deceptive design practices can undermine, invert, or invalidate the purported messages of charts and graphs. These failures can arise silently: a conclusion derived from a particular visualization may look plausible unless the analyst looks closer and discovers an issue with the backing data, visual specification, or their own assumptions. We term such silent but significant failures visualization mirages."

The detector borrows metamorphic testing from software testing. It perturbs data or specification in ways that should or should not change the conclusion and flags disagreements. On their test set, it "can reliably identify mirages across a variety of chart types with relatively little prior knowledge of the data or the domain." It bears on [checks/matplotlib.md](../checks/matplotlib.md).

### Position papers

**Correll, *What Do We Actually Learn from Evaluations in the "Heroic Era" of Visualization?* (2020, arXiv 2008.11250).** A position paper arguing that visualization evaluations "fail to tell us very much that is useful or transferable about visualization systems, regardless of the statistical rigor or ecological validity of the evaluation." Thought experiments, no data, so evidence for nothing. A companion to [Kosara's](robert-kosara.md) *An Empire Built On Sand*.

**Correll, *Ethical Dimensions of Visualization Research* (CHI 2019, arXiv 1811.07271).** His most-cited paper, a position paper that "address[es] the moral components of the design and use of visualizations, identif[ies] some ongoing areas of visualization research with ethical dilemmas, and propose[s] a set of additional moral obligations." It supports no evidentiary claim here.

## Where his name is used as authority for more than he showed

**"Correll proved axis-break markers don't work."** It was a knife-edge failure to reject, F(2,60) = 3.1 against a critical value of 3.1504, on 32 participants and two static designs. The paper's verb is "may not be sufficient". See [refutations.md](../refutations.md).

**"Correll says never use error bars."** The study compared uncertainty encodings for inferring whether two means differ. It prohibited no mark.

**"Correll refuted the Cleveland and McGill ranking."** He co-wrote a position paper that keeps the ranking and asks for scope. Nobody has run the settling experiment.

**Counting him as independent.** He is on both uncertainty-and-deception study pages, the ranking critique and the mirages paper, with Bertini and Franconeri on two. "Correll et al." is one voice with recurring collaborators. [sources/urban-institute.md](../sources/urban-institute.md) records the same error for Schwabish.

## See also

- [../studies/correll-2020-truncating-the-y-axis.md](../studies/correll-2020-truncating-the-y-axis.md)
- [../studies/correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md)
- [../concepts/channels.md](../concepts/channels.md): the ranking his co-authored critique scopes
- [../chart-types/flow-map.md](../chart-types/flow-map.md): the form their Figure 1 uses to pose the question
- [robert-kosara.md](robert-kosara.md): the same skepticism aimed at mechanisms rather than objectives
- [../refutations.md](../refutations.md)
