---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Matejka & Fitzmaurice 2017: Same Stats, Different Graphs

Justin Matejka, George Fitzmaurice. *Same Stats, Different Graphs: Generating Datasets with Varied Appearance and Identical Statistics through Simulated Annealing.* CHI 2017. DOI [10.1145/3025453.3025912](https://doi.org/10.1145/3025453.3025912).

**What it is good for.** A method that perturbs one dataset into many visually different ones with the same summary statistics, and a teaching image for the claim that those statistics do not determine the shape of the data.

**What it does not settle.** Anything about readers. The Datasaurus circulates as if it were evidence.

**How this was read.** PDF from Autodesk Research (`damassets.autodesk.net/.../same-stats-different-graphs.pdf`), re-extracted with `pdftotext -layout`, with Figures 1, 3 and 6 checked on page renders. The paper never uses the name "Datasaurus Dozen", so the Dozen's count comes from the HTML project page at [research.autodesk.com](https://www.research.autodesk.com/publications/same-stats-different-graphs/), fetched with curl.

## It is a construction, not an experiment

The paper has no participants, task, comprehension measure or design comparison. It is a method paper: an algorithm, six worked examples, and limitations about when the output is ugly.

It shows by construction that these summary statistics are compatible with radically different data. That data should be plotted before a five-number summary is trusted is a sound inference from it.

It does not support these, none of which it measures:

- *Readers are misled by summary statistics.*
- *Scatterplots produce better conclusions than summary tables.*
- *This is how often the problem occurs in real data.* The datasets are adversarial by construction, not sampled.

[inventory.md](../inventory.md) topic 50 files the Datasaurus as "a construction, not an experiment," separately from the evidence-backed seaborn claim. The empirical counterpart is [Weissgerber et al. 2015](weissgerber-2015-beyond-bar-line.md), whose Fig 1 makes the same point with realistic data, real p-values from three different tests, and a 703-article prevalence estimate.

## Attribution

The Datasaurus is **Alberto Cairo's**. The paper cites it as reference 4, a 2016 post on thefunctionalart.com titled "Download the Datasaurus: Never trust summary statistics alone; always visualize your data." Matejka and Fitzmaurice use it as the *seed* for datasets matching its statistics (x̄ = 54.26, ȳ = 47.83, sd_x = 16.76, sd_y = 26.93, Pearson's r = -0.06). The paper shows four (Figure 6). The project page describes the released set: "To generate the Datasaurus Dozen, we created 12 shapes to direct the dots towards." The Dozen is the dinosaur plus twelve generated datasets, thirteen in all.

The ancestor is Anscombe's Quartet (1973), whose method Anscombe never explained: "it is not known how Anscombe came up with his datasets."

## Method

Nudging an existing dataset while holding its statistics is easier than generating one from scratch:

```
current_ds <- initial_ds
for x iterations:
    test_ds <- PERTURB(current_ds, temp)
    if ISERROROK(test_ds, initial_ds):
        current_ds <- test_ds
```

Each perturbation moves individual points, and annealing biases moves toward a target shape early and freezes them late. Because `ISERROROK` is just a predicate holding the invariants, the technique is **agnostic to which statistics are held fixed**. Chatterjee & Firat's (2007) genetic algorithm held only means and correlation.

## The six examples

1. **Target shapes.** A generic point cloud of 182 points, coerced toward the 11 target shapes in Figure 3, at 200,000 iterations, about 10 minutes on a laptop. Figure 1's twelve scatterplots, the seed plus a star, an X and parallel lines among them, share x/y means, x/y standard deviations and Pearson's r (+0.32) to two decimal places. No dinosaur is among them.
2. **Alternate statistical measures.** The same seed held on nonparametric properties instead.
3. **Specific initial dataset.** Cairo's Datasaurus as the seed. Figure 6 drives it toward four shapes (concentric rings, slanted lines, horizontal lines, an X), all holding its statistics to two decimal places. The released Datasaurus Dozen extends this example to twelve shapes.
4. **Simpson's paradox.** A dataset with overall Pearson's r of +0.81, coerced toward sloping lines so each subgroup is negatively correlated.
5. **Anonymization.** A Kolmogorov-Smirnov constraint in `ISERROROK` (x and y K-S statistic both below 0.05) keeps the shape while every point moves.
6. **1D boxplots.** Six distributions with identical first quartile, median, third quartile and 1.5-IQR whisker positions, so identical boxplots. Box plots, the usual recommended *fix* for the bar-chart problem, are what gets defeated.

## Limits the authors state themselves

> "When the source dataset and the target shape are vastly different, the produced output might not be desirable."

Their example is a strongly positively correlated dataset forced into a star. The fixes are simpler target shapes covering more of the coordinate space, or pre-scaling the target to the seed.

> "The currently implemented fitness function looks only at the position of individual points in relation to the target shape, which can result in 'clumping' of data points and sparse areas on the target shape."

> "The parameters chosen for the algorithm (95% success rate, quadratic cooling scheme, start/end temperatures, etc.) were found to work well, but should not be considered 'optimal'."

The conclusion:

> "We presented a technique for creating visually dissimilar datasets which are equal over a range of statistical properties. The outputs from our method can be used to demonstrate the importance of visualizing your data, and may serve as a starting point for new data anonymization techniques."

## Links

- Code and datasets: [autodeskresearch.com/publications/samestats](https://www.autodeskresearch.com/publications/samestats)
- Project page with the Datasaurus Dozen: [research.autodesk.com/publications/same-stats-different-graphs](https://www.research.autodesk.com/publications/same-stats-different-graphs/)
- [weissgerber-2015-beyond-bar-line.md](weissgerber-2015-beyond-bar-line.md): the same point with evidence attached
- [evidence-class](../concepts/evidence-class.md): the Datasaurus is a vivid artifact treated as an empirical result
- [inventory.md](../inventory.md), topic 50
