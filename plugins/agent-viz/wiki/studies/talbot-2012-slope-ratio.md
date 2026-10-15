---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Talbot, Gerth & Hanrahan 2012: An Empirical Model of Slope Ratio Comparisons

Justin Talbot, John Gerth, Pat Hanrahan (all Stanford). IEEE TVCG (Proceedings of InfoVis) 2012. PDF: [vis.stanford.edu/files/2012-SlopeComparison-InfoVis.pdf](http://vis.stanford.edu/files/2012-SlopeComparison-InfoVis.pdf).

**What it is good for.** A re-test of Cleveland, McGill & McGill's "banking to 45 degrees" guideline over a much wider range of slope comparisons, without Cleveland's instruction to compare heights. It shows 45 degrees is not the general error-minimizing aspect ratio and Cleveland's result is a local fit, not a global one. A separate finding that a visible baseline under each segment reduced slope-judgment error for mid-angles below 45 degrees, which is cited elsewhere as support for baselines and gridlines and reaches less far than that. A replacement guideline: flatter, wider aspect ratios than existing banking algorithms produce.

**What it does not settle.** Whether any of this transfers to real plots, which the authors say has not been shown. Aspect-ratio selection as a whole, since slope-ratio accuracy is one task among several.

**How this was read.** Extracted locally with `pdftotext` from the Stanford Vis Group copy, retrieved 2026-08-23.

## The finding

From the abstract:

> "we find that, in general, slope ratio errors are not minimized around 45°"

Subjects estimate slope ratios with one of two strategies, which the paper names HEIGHT (compare y-extents, exact when x-extents match) and ANGLE (compare each segment's angle with the horizontal, not exact). Cleveland told his subjects to use HEIGHT. Without that instruction, most of Talbot et al.'s subjects used ANGLE, unaware the two give different answers.

The shift of the minimum below 30 degrees belongs to ANGLE only (*Quality of the ANGLE Submodel*):

> "as the true slope ratio decreases, the error function becomes increasingly asymmetric, with very large errors for tall-narrow aspect ratios, and small errors for short-wide aspect ratios. Second, this effect leads to a shift in the minimum location from near 45° to below 30°."

Cleveland's model replicates inside his own range and fails outside it (*Quality of the HEIGHT Submodel*):

> "Note that in these halves, their model (blue) fits the shape of our data pretty well; our subjects appear to have consistently higher error than in the original study. However, when extrapolating the model beyond their sample space the fit is quite poor. Where our data shows a continued downward trend as the mid-angle increases, their model goes back up, creating a false minimum at 45°."

> "while the Cleveland et al. model fit our data well in the regions considered in the original study, it fails to extrapolate to either larger mid-angles or smaller true slope percentages. Further, we have seen that slope ratio estimation accuracy is not, in general, minimized at 45°."

**Baseline.** Experiment 2 randomly gave half the subjects a horizontal baseline under each segment:

> "As predicted, the addition of a baseline nearly eliminates the judgment error for mid-angles less than 45°. The error here is now nearly as small as in the height approximation results from Experiment 1. But, unpredicted, the linear trend was not eliminated for mid-angles larger than 45°."

The authors: "Our hypothesis is not fully confirmed."

**Aspect-ratio selection.** Minimizing predicted ANGLE error over all segment pairs "consistently selects flatter, wider aspect ratios" than AWO, arc-length, GOR, MS and LOR.

## Method

Eleven exploratory pilots on Amazon Mechanical Turk preceded two lab experiments. Each stimulus was a pair of line segments with equal x-extents in opposite quadrants (upper-left, lower-right), so extents could not be compared directly. The upper segment was always 200 pixels long. Stimuli varied by mid-angle (the angle halfway between the segments) and true slope ratio as a percentage. Subjects knew the ratio lay between 0% and 100% and were asked for "quick visual estimates," untimed and with no strategy suggested. The instructions avoided the words "height" and "angle," and did not mention the matched x-extents. A post-session question about whether they had used "any specific strategy" classified each subject as ANGLE, HEIGHT or other. Experiment 2 added the baseline for half the subjects and subdivided mid-angle by a factor of 3 rather than repeating each stimulus 3 times.

Cleveland et al.'s original used 16 subjects and 44 line pairs with true slope ratios between 50% and 100%, shown for 2.5 seconds each, and told subjects to compare y-extents.

## Sample size and population

- **Pilots:** 148 MTurk workers across 11 studies (some took part more than once), up to 300 slope comparisons, 3 cents per comparison. No screening: "we chose to make no effort to screen participants and accepted every non-empty response." Quality "varied greatly". Each comparison got 3 to 10 replications, median used.
- **Experiment 1:** **8 subjects** (4 female, 4 male), described as naive but all "Ph.D. students in visualization or computer graphics." 49 line pairs, 3 repetitions each, 1,176 responses. Self-reported strategy: 5 ANGLE, 3 HEIGHT.
- **Experiment 2:** **20 subjects** (18 male, 2 female; 19 PhD students, post-docs or staff in a university computer science department, 1 physics PhD), 10 with baseline and 10 without. 147 comparisons each, 2,940 responses. One subject held out for applying a mental correction.

## Limits the authors state themselves

> "The high-level conclusion we draw from this work is that the theory of aspect ratio selection is not as simple as it once seemed. Minimizing the error in slope ratio estimation does not directly lead to a simple design guideline. Substantial future work remains to flesh out a full theory of aspect ratio selection."

> "Further, we did not gather data from the extremes of the comparison space... Additionally, the fact that we had few subjects choose to use height comparisons means that we did not gather enough data to further analyze the interesting trends that we saw there."

> "A major limitation shared by Cleveland et al.'s original study and our study is that both only look at slope comparisons between pairs of lines in isolation. But this is not how graph reading is done; graphs typically consist of many line segments, and frequently graphs have enough line segments that the data curve looks continuous. It is still unclear if the results derived in our studies for pairwise discrete comparisons will transfer to real plots. Additionally, our finding that angle ratio comparisons are more common than height comparisons also needs to be verified using real plots and real plot-reading tasks."

> "slope ratio estimation is just one graph reading task among many... Any specific aspect ratio necessarily has to make a tradeoff between reducing errors for some tasks and increasing it for others. It's likely that these previous automated techniques are trading off slope ratio estimation accuracy for better accuracy on something else."

Their model does not explain the downward trend in the right four HEIGHT panels, and it fails at the 86.7% slope percentage under ANGLE.

## What this result does not license

- **Not "banking to 45 degrees is refuted."** It is scope-limited. Cleveland's model fits inside the moderate regime he tested, as the authors say.
- **Not "the optimum is 30 degrees."** That shift is in the ANGLE submodel only. Cleveland's subjects were told to use HEIGHT, and under HEIGHT the paper reports a continued downward trend, not a new minimum.
- **Not a validated aspect-ratio algorithm.** The application section fits the model to a set of time series and shows the resulting ratios are flatter. No experiment shows readers do better on those plots.
- **Not a claim about real charts.** The stimulus is two isolated segments in opposite quadrants, the major limitation the authors name.
- **Not a demographic result.** With 8 and 20 technically expert, mostly male subjects from a CS department, the ANGLE-versus-HEIGHT prevalence is an observation, not a population estimate.
- **Not evidence that baselines fix slope judgment.** The paper reports that "visible baselines can substantially mitigate errors made in slope judgments," and that sentence is quoted elsewhere as independent support for the zero-baseline rule. Baselines nearly eliminated the error for mid-angles below 45 degrees and did not eliminate it above.

## Two papers that get conflated

Talbot, Gerth and Hanrahan also wrote *Arc Length-Based Aspect Ratio Selection* (TVCG 2011), which is reference 15 here. This page covers *An Empirical Model of Slope Ratio Comparisons* (InfoVis 2012). The attribution "Talbot, Gehrke & Heer, InfoVis 2011," matches neither author list. [inventory.md](../inventory.md) topic 14 names both papers.

## Links

- PDF: [vis.stanford.edu/files/2012-SlopeComparison-InfoVis.pdf](http://vis.stanford.edu/files/2012-SlopeComparison-InfoVis.pdf)
- Project page: [vis.stanford.edu/papers/slope-ratio-comparison](http://vis.stanford.edu/papers/slope-ratio-comparison)
- [refutations.md](../refutations.md), "Bank to 45 degrees"
- [inventory.md](../inventory.md), topic 14 (aspect ratio)
