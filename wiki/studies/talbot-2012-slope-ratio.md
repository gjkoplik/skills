# Talbot, Gerth & Hanrahan 2012: An Empirical Model of Slope Ratio Comparisons

Justin Talbot, John Gerth, Pat Hanrahan (all Stanford). IEEE TVCG (Proceedings of InfoVis) 2012. PDF: [vis.stanford.edu/files/2012-SlopeComparison-InfoVis.pdf](http://vis.stanford.edu/files/2012-SlopeComparison-InfoVis.pdf).

## What it is

A re-examination of Cleveland, McGill & McGill's "banking to 45 degrees" guideline. The authors widen the sampled space of slope comparisons well past Cleveland's, drop his instruction to compare heights, build a two-strategy model of how people actually estimate slope ratios, and validate it in two experiments.

## Status

**`primary-read`.** Extracted locally with `pdftotext` from the Stanford Vis Group copy. Retrieval date: **2026-08-23**.

## What it is good for

- Establishing that **45 degrees is not the general error-minimizing aspect ratio**, and that Cleveland's result is a local fit rather than a global one.
- The independent finding that **a visible baseline substantially reduces slope-judgment error**, which supports the zero-baseline and gridline rules from an unrelated direction.
- A constructive replacement guideline: prefer **flatter, wider** aspect ratios than existing banking algorithms produce.

## What it does not settle

Whether any of this transfers to real plots. The authors say plainly that it has not been shown to. It also does not settle aspect-ratio selection as a whole, because slope-ratio accuracy is one task competing with others.

---

## The finding

From the abstract:

> "we find that, in general, slope ratio errors are not minimized around 45°"

The mechanism is that people use two different approximation strategies, which the paper names HEIGHT (compare the y-extents, which is exactly correct when x-extents match) and ANGLE (compare the angles each segment makes with the horizontal, which is not). Cleveland instructed his subjects to use HEIGHT. Talbot et al. removed the instruction, and most subjects spontaneously used ANGLE without realizing the two would give different answers.

**The "below 30 degrees" shift belongs to ANGLE only.** It appears under the heading *Quality of the ANGLE Submodel*:

> "as the true slope ratio decreases, the error function becomes increasingly asymmetric, with very large errors for tall-narrow aspect ratios, and small errors for short-wide aspect ratios. Second, this effect leads to a shift in the minimum location from near 45° to below 30°."

**Cleveland replicates inside his own range.** From *Quality of the HEIGHT Submodel*:

> "Note that in these halves, their model (blue) fits the shape of our data pretty well; our subjects appear to have consistently higher error than in the original study. However, when extrapolating the model beyond their sample space the fit is quite poor. Where our data shows a continued downward trend as the mid-angle increases, their model goes back up, creating a false minimum at 45°."

and the summary sentence:

> "while the Cleveland et al. model fit our data well in the regions considered in the original study, it fails to extrapolate to either larger mid-angles or smaller true slope percentages. Further, we have seen that slope ratio estimation accuracy is not, in general, minimized at 45°."

**The baseline result.** Experiment 2 randomly assigned half the subjects to see a horizontal baseline under each line segment:

> "As predicted, the addition of a baseline nearly eliminates the judgment error for mid-angles less than 45°. The error here is now nearly as small as in the height approximation results from Experiment 1. But, unpredicted, the linear trend was not eliminated for mid-angles larger than 45°."

Their own summary of that: "Our hypothesis is not fully confirmed."

**The constructive result.** Minimizing predicted ANGLE error over all segment pairs "consistently selects flatter, wider aspect ratios" than AWO, arc-length, GOR, MS and LOR.

## Method

Eleven exploratory pilot studies on Amazon Mechanical Turk, then two lab experiments.

Stimuli: pairs of line segments with equal x-extents, placed in the upper-left and lower-right quadrants so that direct x- or y-extent comparison across the pair is impossible. The upper segment was always 200 pixels long. The sample space is parameterized by mid-angle (the angle halfway between the two segments) and true slope ratio as a percentage. Subjects were told the true percentage lay between 0% and 100% and asked to make "quick visual estimates," with no time limit and no suggested strategy. The instructions deliberately avoided the words "height" and "angle," and subjects were not told the x-extents were matched.

After each session the experimenter asked whether the subject had used "any specific strategy," and used the self-report to classify each subject as ANGLE, HEIGHT or other.

Experiment 2 was identical except that half the subjects saw a visible baseline, and the mid-angle axis was subdivided by a factor of 3 instead of repeating each stimulus 3 times.

For reference, the original Cleveland et al. study used 16 subjects, 44 line pairs with true slope ratios between 50% and 100%, each shown for 2.5 seconds, with subjects explicitly instructed to compare y-extents.

## Sample size and population

- **Pilots:** 148 MTurk workers across 11 studies, some participating more than once, up to 300 slope comparisons in total. Paid 3 cents per comparison. No screening: "we chose to make no effort to screen participants and accepted every non-empty response." Response quality "varied greatly"; 3 to 10 replications per comparison, median used.
- **Experiment 1:** **8 subjects** (4 female, 4 male), described as naive but all "Ph.D. students in visualization or computer graphics." 49 line pairs, 3 repetitions each, 1,176 responses. Self-reported strategy: 5 ANGLE, 3 HEIGHT.
- **Experiment 2:** **20 subjects** (18 male, 2 female; 19 PhD students, post-docs or staff in a university computer science department, 1 physics PhD), split 10 with baseline and 10 without. 147 comparisons each, 2,940 responses. One subject's data held out for applying a mental correction.

This is a small, technically expert, heavily male sample. That matters for how far the ANGLE/HEIGHT prevalence split generalizes.

## Limits the authors state themselves

Their own high-level summary is deflationary, not triumphal:

> "The high-level conclusion we draw from this work is that the theory of aspect ratio selection is not as simple as it once seemed. Minimizing the error in slope ratio estimation does not directly lead to a simple design guideline. Substantial future work remains to flesh out a full theory of aspect ratio selection."

> "Further, we did not gather data from the extremes of the comparison space... Additionally, the fact that we had few subjects choose to use height comparisons means that we did not gather enough data to further analyze the interesting trends that we saw there."

> "A major limitation shared by Cleveland et al.'s original study and our study is that both only look at slope comparisons between pairs of lines in isolation. But this is not how graph reading is done; graphs typically consist of many line segments, and frequently graphs have enough line segments that the data curve looks continuous. It is still unclear if the results derived in our studies for pairwise discrete comparisons will transfer to real plots. Additionally, our finding that angle ratio comparisons are more common than height comparisons also needs to be verified using real plots and real plot-reading tasks."

And on the tradeoff that a flatter aspect ratio buys:

> "slope ratio estimation is just one graph reading task among many... Any specific aspect ratio necessarily has to make a tradeoff between reducing errors for some tasks and increasing it for others. It's likely that these previous automated techniques are trading off slope ratio estimation accuracy for better accuracy on something else."

They also leave their own model's failures on the record: it does not explain the downward trend in the right four HEIGHT panels, and it fails at the 86.7% slope percentage under ANGLE.

## What this result does not license

- **Not "banking to 45 degrees is refuted."** It is scope-limited. Cleveland's model fits inside the moderate regime he tested, and the authors say so. The stronger word is wrong.
- **Not "the optimum is 30 degrees."** The shift below 30 degrees describes the ANGLE submodel only. Cleveland's subjects were instructed to use HEIGHT, and under HEIGHT the paper reports a continued downward trend rather than a new minimum.
- **Not a validated aspect-ratio algorithm.** The application section fits the model to a set of time series and shows the resulting ratios are flatter. There is no experiment showing readers do better on those plots.
- **Not a claim about how people read real charts.** The stimulus is two isolated line segments in opposite quadrants, and the authors name this as the major shared limitation.
- **Not a demographic result.** With 8 and 20 subjects drawn from a CS department, the ANGLE-versus-HEIGHT prevalence is an observation, not a population estimate.
- **Not evidence that baselines fix slope judgment.** They fixed it for mid-angles below 45 degrees and did nothing above.

## Naming note

Two different Talbot/Gerth/Hanrahan papers get confused. **Arc Length-Based Aspect Ratio Selection** is TVCG 2011 (it is reference 15 in this paper). **An Empirical Model of Slope Ratio Comparisons** is the 2012 InfoVis paper this page covers. [inventory.md](../inventory.md) topic 14 cites "Talbot, Gehrke & Heer, InfoVis 2011," which is neither author list.

## Links

- PDF: [vis.stanford.edu/files/2012-SlopeComparison-InfoVis.pdf](http://vis.stanford.edu/files/2012-SlopeComparison-InfoVis.pdf)
- Project page: [vis.stanford.edu/papers/slope-ratio-comparison](http://vis.stanford.edu/papers/slope-ratio-comparison)
- [refutations.md](../refutations.md), "Bank to 45 degrees"
- [inventory.md](../inventory.md), topic 14 (aspect ratio)
