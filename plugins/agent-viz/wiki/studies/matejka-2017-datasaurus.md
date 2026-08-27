---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Matejka & Fitzmaurice 2017: Same Stats, Different Graphs

Justin Matejka, George Fitzmaurice. *Same Stats, Different Graphs: Generating Datasets with Varied Appearance and Identical Statistics through Simulated Annealing.* CHI 2017. DOI [10.1145/3025453.3025912](https://doi.org/10.1145/3025453.3025912).

A simulated-annealing method for taking one dataset and perturbing it into many visually different datasets that hold the same summary statistics to two decimal places. The famous output is the Datasaurus Dozen: twelve scatterplots including a dinosaur, a star and a set of parallel lines, all sharing x/y means, x/y standard deviations and Pearson's r.

**How this was read.** PDF retrieved from Autodesk Research (`damassets.autodesk.net/.../same-stats-different-graphs.pdf`) and re-extracted with `pdftotext -layout`.

## What it is good for

Exactly one thing: an unforgettable picture for the claim that summary statistics do not determine the shape of the data. It is a teaching image and a generator, and both are genuinely good.

## What it does not settle

**Anything about readers.** The Datasaurus circulates as if it were evidence.

## It is a construction, not an experiment

There are no participants in this paper. There is no task, no measurement of comprehension, no comparison of designs, and no human subject of any kind. It is a method paper in the graphics-and-optimization sense: an algorithm, a cooling schedule, six worked examples, and a limitations section about when the algorithm produces ugly output.

So the Datasaurus can support:

- *These summary statistics are compatible with radically different data.* True by construction, which is the strongest form of true available.
- *Therefore plot your data before trusting a five-number summary.* A sound inference from the construction.

It cannot support:

- *Readers are misled by summary statistics.* Not measured.
- *Scatterplots produce better conclusions than summary tables.* Not measured.
- *This is how often the problem occurs in real data.* Not measured, and by construction the datasets are adversarial rather than sampled.

[inventory.md](../inventory.md) topic 50 already gets this right, marking the seaborn claim as evidence-backed and the Datasaurus separately as "a construction, not an experiment." Keep that split. When the claim you need is empirical, cite [Weissgerber et al. 2015](weissgerber-2015-beyond-bar-line.md), whose Fig 1 makes the same point with realistic data, real p-values from three different tests, and a 703-article prevalence estimate behind it. Use the Datasaurus for the slide.

## Attribution, which is usually gotten wrong

The Datasaurus is **Alberto Cairo's**, not Matejka and Fitzmaurice's. The paper cites it as reference 4, a 2016 post on thefunctionalart.com titled "Download the Datasaurus: Never trust summary statistics alone; always visualize your data." What this paper contributes is using the datasaurus as the *seed* and generating eleven more datasets matching its statistics (x̄ = 54.26, ȳ = 47.83, sd_x = 16.76, sd_y = 26.93, Pearson's r = -0.06). The dinosaur is Cairo's; the Dozen is Matejka and Fitzmaurice's.

The ancestor is Anscombe's Quartet (1973), and the paper is candid that Anscombe never explained his method: "it is not known how Anscombe came up with his datasets."

## Method

The insight is that generating a dataset from scratch to hit target statistics is hard, but nudging an existing one while holding the statistics is easy:

```
current_ds <- initial_ds
for x iterations:
    test_ds <- PERTURB(current_ds, temp)
    if ISERROROK(test_ds, initial_ds):
        current_ds <- test_ds
```

Perturbation moves individual points; a simulated-annealing temperature schedule biases moves toward a target shape early and freezes them late. `ISERROROK` is where the invariants live, and because it is just a predicate, the technique is **agnostic to which statistics are held fixed**. That is the actual contribution over the prior genetic-algorithm approach of Chatterjee & Firat (2007), which held only means and correlation.

## The six examples

1. **Target shapes.** 182 points, 200,000 iterations, about 10 minutes on a laptop, holding x/y mean, x/y standard deviation and Pearson's r to two decimals.
2. **Alternate statistical measures.** The same seed held constant on nonparametric properties instead of parametric ones.
3. **The Datasaurus Dozen.**
4. **Simpson's paradox, generated on purpose.** A dataset with overall Pearson's r of +0.81, coerced toward sloping lines so each subgroup is individually negatively correlated.
5. **Cloned data for anonymization.** A Kolmogorov-Smirnov constraint inside `ISERROROK` (both x and y K-S statistic below 0.05) keeps the output similar in shape while every point moves.
6. **1D boxplots.** Six distributions with identical first quartile, median, third quartile and 1.5-IQR whisker positions, producing an identical boxplot. Box plots are usually the recommended *fix* for the bar-chart problem, and here they are the thing being defeated.

## Limits the authors state themselves

Short, and all about the algorithm.

> "When the source dataset and the target shape are vastly different, the produced output might not be desirable."

Their example is coercing a strongly positively correlated dataset into a star, which fails. The mitigation is simpler target shapes with better coverage of the coordinate space, or pre-scaling the target to align with the seed.

> "The currently implemented fitness function looks only at the position of individual points in relation to the target shape, which can result in 'clumping' of data points and sparse areas on the target shape."

> "The parameters chosen for the algorithm (95% success rate, quadratic cooling scheme, start/end temperatures, etc.) were found to work well, but should not be considered 'optimal'."

And the conclusion, which claims only what it should:

> "We presented a technique for creating visually dissimilar datasets which are equal over a range of statistical properties. The outputs from our method can be used to demonstrate the importance of visualizing your data, and may serve as a starting point for new data anonymization techniques."

"Can be used to demonstrate" is doing honest work in that sentence. The paper does not overclaim; the citation practice around it does.

## Links

- Code and datasets: [autodeskresearch.com/publications/samestats](https://www.autodeskresearch.com/publications/samestats)
- [weissgerber-2015-beyond-bar-line.md](weissgerber-2015-beyond-bar-line.md), which you should cite instead when you need the same point with evidence attached
- [evidence-class](../concepts/evidence-class.md). The Datasaurus is the cleanest example in this wiki of a vivid artifact that gets treated as an empirical result.
- [inventory.md](../inventory.md), topic 50
