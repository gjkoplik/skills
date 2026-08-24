# Heer & Bostock (2010), *Crowdsourcing Graphical Perception*

**What it is.** Jeffrey Heer and Michael Bostock, "Crowdsourcing Graphical Perception: Using Mechanical Turk to Assess Visualization Design," CHI 2010, pp. 203-212. A replication of [Cleveland & McGill (1984)](cleveland-mcgill-1984.md) on Mechanical Turk, plus new experiments on rectangular area, luminance contrast, chart size and gridline spacing.

**Status.** `primary-read`. PDF from the Stanford Vis Group, text re-extracted locally. Quotes below are from that extraction, not from a fetch summary.

**What it is good for.** Two things. It is the reason the channel ranking can be called replicated at all. And it is the only place the length-versus-angle comparison has actually been run under a common task format, which is the comparison Cleveland & McGill could not make.

**What it does not settle.** Anything about tasks other than proportional judgment. It measures the same narrow thing the 1984 paper measured, on a different population, at 380x380 pixels.

---

## What replicated

Seven judgment types. Types 1-5 reproduce Cleveland & McGill's position-length experiment (1-3 position along a common scale, 4-5 length). Type 6 is angle, as a pie chart. Type 7 is circular area, as a bubble chart. N=50 per chart, 70 trials, paid $0.05 per judgment, same log absolute error measure and same midmean analysis as the original.

The replication held:

> "The new results are similar (though not identical) to the originals: the rough shape and ranking of judgment types by accuracy (T1-5) are preserved, supporting the validity of the crowdsourced study."

with one noted difference: types 1 and 2 came closer together, which the authors attribute to the smaller display reducing the effect of distance, and types 4 and 5 were more accurate than in the original. Position still significantly outperformed length.

**A methodological detail worth stealing.** Subjects had to pass a qualification test of three multiple-choice charts whose wrong answers were "grossly wrong." The point was not to filter for accuracy, which "would bias the responses," but to confirm the instructions were understood. A pilot without it produced over 10% unusable responses.

## The finding that contradicts the folk ranking

Types 6 and 7 were built to the same task format as the others precisely so that angle and area could be compared against length and position on a common scale. On the result (p. 5):

> "Indeed, the new results match expectations: psychophysical theory [7, 34] predicts area to perform worse than angle, and both to be significantly worse than position. Theory also suggests that angle should perform worse than length, but the results do not support this. Cleveland & McGill also did not find angle to perform worse than length, but as stated their position-angle results are not directly comparable to their position-length results."

Three claims land here, and they should be kept distinct:

- **Confirmed.** Area is worse than angle. Both are significantly worse than position.
- **Not supported.** Angle worse than length. The theory predicts it; the one study designed to test it head to head did not find it.
- **Correctly attributed.** Cleveland & McGill did not find it either, and could not have, because their two experiments are not comparable.

So the widely repeated ordering `position > length > angle > area` is **contested at the length-angle step specifically**. Every other step in it survives. This is the cleanest available case of a rule that is right in outline and wrong at one joint, which is exactly the kind of thing that survives summarization intact and should not.

## Rectangular area, and the square-is-worst result

Experiment 1B extended circular area judgment to rectangles, motivated by treemaps and cartograms. A 3x2x6 factorial design, 108 trials, aspect ratios drawn from a squarified treemap layout.

Two results:

**Rectangular area is about as accurate as circular area.** "The results confirm our hypothesis that, on average, the accuracy of rectangular area judgments matches that of circular area judgments."

**Squares are the worst case, not the best.** This one is counterintuitive and directly contradicts the design goal of squarified treemap algorithms:

> "Somewhat surprisingly, comparisons of rectangles with aspect ratio 1 exhibited the worst performance, a result robust across both the rectangle and treemap display conditions. This finding suggests that viewers actually benefit from the inability of a squarified treemap algorithm to perfectly optimize the rectangles to 1:1 aspect ratios. The result is consistent with the hypothesis that viewers use 1D length comparisons to help estimate area: comparing the lengths of sides as a proxy for area leads to maximal error when comparing squares."

The authors hedge it themselves: "Additional experimentation is needed to form an accurate perceptual model." Treat the mechanism as a hypothesis and the effect as measured.

**Treemap surround does not interfere.** No significant difference between bare center-aligned rectangles (T8) and the same judgment inside a full treemap (T9), suggesting the other rectangles in the display do not degrade the judgment. The authors note they did not test for interference from varying color intensity.

## Limits worth carrying

- Proportional judgment only. Same narrow task as 1984: identify the smaller of two marked values, estimate what percent it is of the larger.
- 380x380 pixel charts. Chart size was a variable in a *different* experiment in this paper, which is itself a reason not to treat any single-size result as scale-free.
- Mechanical Turk in 2010. Uncontrolled displays, which is why the authors establish luminance-contrast reliability separately before relying on it.
- The 0.4% error rate on the verification question (14 of 3,481) is a data-quality statistic, not an accuracy result.

## Evidence class of what this paper supports

- **Evidence-backed.** Position beats length. Position beats angle and area. Area is worse than angle. Rectangular and circular area judgments are comparably accurate. Aspect ratio 1 is the worst case for rectangular area comparison.
- **Contested.** Length versus angle. Theory says one thing, this experiment says otherwise, and 1984 is silent.
- **Authority-asserted, from this paper.** The side-length-proxy explanation for the square result, offered by the authors as a consistent hypothesis rather than a tested mechanism.

## See also

- [cleveland-mcgill-1984.md](cleveland-mcgill-1984.md) — the original, and why its rank 3 is a tie
- [../concepts/channels.md](../concepts/channels.md) — the ranking as a working tool, with this contest folded in
- [../refutations.md](../refutations.md) — where the length-versus-angle contest is logged
