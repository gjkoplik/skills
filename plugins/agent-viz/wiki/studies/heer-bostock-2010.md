---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Heer & Bostock (2010), *Crowdsourcing Graphical Perception*

Jeffrey Heer and Michael Bostock, "Crowdsourcing Graphical Perception: Using Mechanical Turk to Assess Visualization Design," CHI 2010, pp. 203-212. A replication of [Cleveland & McGill (1984)](cleveland-mcgill-1984.md) on Mechanical Turk, plus new experiments on rectangular area, luminance contrast, chart size and gridline spacing.

**How this was read.** PDF from the Stanford Vis Group, text re-extracted locally. Quotes come from that extraction.

**What it is good for.** The replication of the channel ranking, and the only test in this corpus of length against angle under a common task format, the comparison Cleveland & McGill could not make.

**What it does not settle.** Tasks other than proportional judgment, the same narrow task as 1984, measured on a different population at 380x380 pixels.

---

## What replicated

Seven judgment types. Types 1-5 reproduce Cleveland & McGill's position-length experiment (1-3 position along a common scale, 4-5 length). Type 6 is angle, as a pie chart, and type 7 is circular area, as a bubble chart. N=50 per chart, 70 trials, $0.05 per judgment, with the original's log absolute error measure and midmean analysis.

> "The new results are similar (though not identical) to the originals: the rough shape and ranking of judgment types by accuracy (T1-5) are preserved, supporting the validity of the crowdsourced study."

Types 1 and 2 came closer together, which the authors attribute to the smaller display reducing the effect of distance, and types 4 and 5 were more accurate than in the original. Position still significantly outperformed length.

A qualification test used three multiple-choice charts whose wrong answers were "grossly wrong." The point was not to filter for accuracy, which "would bias the responses," but to confirm the instructions were understood. A pilot without it produced over 10% unusable responses.

## The finding that contradicts the folk ranking

Types 6 and 7 used the same task format, so angle and area are comparable with length and position (p. 5):

> "Indeed, the new results match expectations: psychophysical theory [7, 34] predicts area to perform worse than angle, and both to be significantly worse than position. Theory also suggests that angle should perform worse than length, but the results do not support this. Cleveland & McGill also did not find angle to perform worse than length, but as stated their position-angle results are not directly comparable to their position-length results."

Angle was not worse than length in the one study designed to test the pair head to head. So the ordering `position > length > angle > area` is contested at the length-angle step, and every other step survives.

## Rectangular area, and the square-is-worst result

Experiment 1B extended area judgment to rectangles for treemaps and cartograms: a 3x2x6 factorial design, 108 trials, aspect ratios drawn from a squarified treemap layout. "The results confirm our hypothesis that, on average, the accuracy of rectangular area judgments matches that of circular area judgments."

Squares were the worst case, against the design goal of squarified treemap algorithms:

> "Somewhat surprisingly, comparisons of rectangles with aspect ratio 1 exhibited the worst performance, a result robust across both the rectangle and treemap display conditions. This finding suggests that viewers actually benefit from the inability of a squarified treemap algorithm to perfectly optimize the rectangles to 1:1 aspect ratios. The result is consistent with the hypothesis that viewers use 1D length comparisons to help estimate area: comparing the lengths of sides as a proxy for area leads to maximal error when comparing squares."

The authors add: "Additional experimentation is needed to form an accurate perceptual model."

Judgments inside a full treemap (T9) did not differ significantly from bare center-aligned rectangles (T8). Interference from varying color intensity was not tested.

## Limits

- Proportional judgment only: identify the smaller of two marked values and estimate what percent it is of the larger.
- 380x380 pixel charts. Chart size was a variable in a different experiment in this paper, so no single-size result is scale-free.
- Mechanical Turk in 2010, on uncontrolled displays. The authors establish luminance-contrast reliability separately for that reason.
- The 0.4% error rate on the verification question (14 of 3,481) is a data-quality statistic, not an accuracy result.

## Evidence class of what this paper supports

- **Evidence-backed.** Position beats length, angle and area. Area is worse than angle. Rectangular and circular area judgments are comparably accurate. Aspect ratio 1 is the worst case for rectangular area comparison.
- **Contested.** Length versus angle: theory predicts angle is worse, this experiment did not find it, and 1984 is silent.
- **Authority-asserted, from this paper.** The side-length-proxy explanation for the square result, offered as a consistent hypothesis, not a tested mechanism.

## See also

- [cleveland-mcgill-1984.md](cleveland-mcgill-1984.md): the original, and why its rank 3 is a tie
- [../concepts/channels.md](../concepts/channels.md): the ranking as a working tool, with this contest folded in
- [../refutations.md](../refutations.md): where the length-versus-angle contest is logged
