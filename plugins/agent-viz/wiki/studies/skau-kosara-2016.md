---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Skau & Kosara (2016), *Arcs, Angles, or Areas*

Drew Skau and Robert Kosara, "Arcs, Angles, or Areas: Individual Data Encodings in Pie and Donut Charts," *Computer Graphics Forum* 35(3) (EuroVis 2016). Two studies that isolate the three encodings a pie slice carries and measure each one separately.

**How this was read.** PDF from kosara.net, text re-extracted locally.

**What it is good for.** The only direct test of which channel a pie chart puts the reader on. [Cleveland & McGill](cleveland-mcgill-1984.md) left that step as conjecture, and every "pies are bad because angles are bad" argument depends on it.

**What it does not settle.** Whether pie charts are a good choice. It measures reading accuracy on two-segment charts, a floor case, not the multi-slice case where pies are usually criticized.

---

## Three encodings in one slice

A pie slice encodes one number three times: as a center angle, an arc length and a wedge area. Cleveland & McGill conjectured angle was primary and said so in those words, and the paper cites Bertin, Robbins and Munzner as treating angle as the mechanism. Nobody had isolated the three. The one prior attempt, Eells (1926), asked people what they had done. The paper reports the methods his participants named as used "exclusively or predominantly": 51% arc length, 25% area, 23% angle, 1% chord length. That is self-report, not measurement, and it points the same way as the results below. Figure 8 sets these beside this study's own self-reports, which had "far more answers for area".

## Method

Six chart types, each isolating an encoding as far as the geometry allows:

| Type | What it carries |
|---|---|
| Baseline pie | All three cues |
| Baseline donut | Area and arc length; angle degraded by the missing center |
| Arc | Arc length only |
| Angle pie | Angle only, no fill or arc |
| Angle donut | Angle only, donut geometry |
| Area | Area only, wedge fills proportionally |

Two segments per chart, blue on light gray. 102 participants recruited on Mechanical Turk, 92 retained. Error is Cleveland & McGill's log absolute error, so the numbers are comparable with theirs. Study 2 varied a donut's inner radius from a filled pie to a thin outline, which progressively removes the angle cue.

In the angle-only condition some participants answered for the wrong side of the angle. The authors corrected for this on 16 participants and report both corrected and uncorrected distributions.

## Results

ANOVA: F(5, 4650) = 121.955, p < 0.001.

> "Error was smaller for the baseline charts, area chart, and the arc chart than the two angle-only charts. This was not what we hypothesized, and contradicts common wisdom that angles are critical to pie and donut chart perception."

Both angle-only conditions produced the highest error and the widest spread.

Donut is not worse than pie: "the baseline donut chart had a slightly lower log error than the baseline pie chart, but well within the 95% confidence interval (virtually identical between the two)." Study 2 extends this across inner radii, so removing the center, and with it the angle cue, costs nothing measurable.

Area alone is about as accurate as the full chart:

> "The unusual area-only chart has very similar error to the pie and donut. This is remarkable, given how difficult it generally is to correctly estimate area, and also the chart's lack of familiarity."

Arc length has the highest mean error among the non-angle conditions but the tightest distribution: "the amount a participant would be wrong by is be more predictable."

Error grows with segment size in every condition except the two angle-only ones, which are V-shaped with the lowest error in the middle third.

## Limits

- Two segments only, chosen "to avoid complicating the task." The common criticism of pies concerns comparing many slices, which this does not test.
- Proportional judgment only, on uncontrolled Mechanical Turk displays.
- The isolating arc, angle and area charts are unfamiliar forms, a plausible confound the authors note and do not fully rule out.

## What this does and does not overturn

- **Evidence-backed.** Angle is the least accurate of the three pie encodings. Donut charts are as accurate as pie charts. Area alone performs comparably to the full pie. Error grows with segment size for every encoding except angle alone.
- **Refuted by this paper.** "Pie charts are read by angle," as a claim about mechanism. The chain "pies are read by angle, angle is a poor channel, therefore pies are poor" has a false first link, so angle does not explain why bars beat pies. It also weakens the case against donuts: cutting out the center destroys the angle cue, and for the two-segment stimuli tested that cost nothing measurable.
- **Untouched by this paper.** Pie versus bar, which Cleveland & McGill and [Heer & Bostock](heer-bostock-2010.md) measured directly, and anything involving more than two segments.

## See also

- [cleveland-mcgill-1984.md](cleveland-mcgill-1984.md): where the angle conjecture comes from, flagged as a conjecture by its own authors
- [../chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md): the type page that inherits this
- [../concepts/channels.md](../concepts/channels.md): why type-level decompositions like this one are rare
