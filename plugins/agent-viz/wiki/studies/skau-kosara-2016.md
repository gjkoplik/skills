---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Skau & Kosara (2016), *Arcs, Angles, or Areas*

Drew Skau and Robert Kosara, "Arcs, Angles, or Areas: Individual Data Encodings in Pie and Donut Charts," *Computer Graphics Forum* 35(3) (EuroVis 2016). Two studies that isolate the three encodings a pie slice carries and measure each one separately.

**How this was read.** PDF from kosara.net, text re-extracted locally.

**What it is good for.** The only direct test of *which channel a pie chart actually puts the reader on*. This is the step that [Cleveland & McGill](cleveland-mcgill-1984.md) explicitly left as conjecture, and it is the step every "pies are bad because angles are bad" argument depends on.

**What it does not settle.** Whether pie charts are a good choice. It measures reading accuracy on two-segment charts, which is a floor case, not the multi-slice case where pies are usually criticized.

---

## Why this study exists

A pie slice encodes the same number three times: as a **center angle**, as an **arc length**, and as a **wedge area**. Cleveland & McGill conjectured angle was primary and said so in those words. Bertin, Robbins and Munzner are all cited in the paper as treating angle as the mechanism. Nobody had isolated them.

The one prior attempt is Eells (1926), who simply asked people what they had done. Self-reports came out **51% arc length, 25% area, 23% angle, 1% chord length**. That is a self-report, not a measurement, but it points the same direction as what follows and it predates the angle consensus by six decades.

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

Two segments per chart, blue on light gray, so the target is unambiguous. 102 participants recruited on Mechanical Turk, 92 retained. Cleveland & McGill's log absolute error measure, kept deliberately so the numbers sit on a comparable scale.

Study 2 varied the inner radius of a donut from a filled pie to a thin outline, which progressively removes the angle cue.

**One methodological wrinkle the authors handle explicitly.** The angle-only condition made participants answer for the wrong side of the angle. They corrected for this on 16 participants and report both corrected and uncorrected distributions.

## Results

ANOVA: F(5, 4650) = 121.955, p < 0.001.

> "Error was smaller for the baseline charts, area chart, and the arc chart than the two angle-only charts. This was not what we hypothesized, and contradicts common wisdom that angles are critical to pie and donut chart perception."

Four distinct findings:

**Angle is the worst of the three, not the primary one.** Both angle-only conditions produced the highest error and the widest spread. The channel the literature named as the mechanism is the channel that performs worst when isolated.

**Donut is not worse than pie.** "the baseline donut chart had a slightly lower log error than the baseline pie chart, but well within the 95% confidence interval (virtually identical between the two)." Study 2 extends this across inner radii. Removing the center, which removes the angle cue, costs nothing measurable.

**Area alone is about as good as the full chart.**

> "The unusual area-only chart has very similar error to the pie and donut. This is remarkable, given how difficult it generally is to correctly estimate area, and also the chart's lack of familiarity."

**Arc length is the most consistent.** Highest mean error among the non-angle conditions but the tightest distribution: "the amount a participant would be wrong by is be more predictable." Mean and variance disagree here, and which one matters depends on whether typical error or worst-case error is at issue.

**Segment size matters.** All conditions except the two angle-only ones show more error as the segment gets larger. The angle-only conditions are V-shaped, with lowest error in the middle third.

## What this does and does not overturn

**It does not overturn:** bar charts beat pie charts for value extraction. That is measured directly in Cleveland & McGill and again in [Heer & Bostock](heer-bostock-2010.md), and this study does not test bars at all.

**It does overturn the usual explanation.** The chain "pies are read by angle, angle is a poor channel, therefore pies are poor" has a false first link. Pies are not primarily read by angle. Whatever makes bars beat pies, it is not that.

**It removes the case against donuts entirely.** The standard argument against donut charts is that cutting out the center destroys the angle. It does, and it does not matter.

## Limits

- **Two segments only.** The authors chose this "to avoid complicating the task." Real pie charts have more, and the common criticism of pies concerns comparing many slices, which this does not test.
- **Proportional judgment only.** Same narrow task as the 1984 lineage: read one value and report it.
- **Mechanical Turk, 92 subjects, uncontrolled displays.**
- **The isolating conditions are unfamiliar chart forms.** The authors note the arc, angle and area charts are not things people have seen, and unfamiliarity is a plausible confound they do not fully rule out.

## Evidence class of what this paper supports

- **Evidence-backed.** Angle is the least accurate of the three pie encodings. Donut charts are as accurate as pie charts. Area alone performs comparably to the full pie. Error grows with segment size for every encoding except angle alone.
- **Refuted by this paper.** "Pie charts are read by angle," as a claim about mechanism.
- **Untouched by this paper.** Pie versus bar, and anything involving more than two segments.

## See also

- [cleveland-mcgill-1984.md](cleveland-mcgill-1984.md) — where the angle conjecture comes from, flagged as a conjecture by its own authors
- [../chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md) — the type page that inherits this
- [../concepts/channels.md](../concepts/channels.md) — why type-level decompositions like this one are rare
