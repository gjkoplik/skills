---
type: study
status: primary-read
status_partial: true
retrieved: 2026-09-05
---

# Siqueira Rodrigues, Israel & Kosch (2026), *Evaluating Graphical Perception in Virtual Reality*

Lucas Siqueira Rodrigues, Johann Habakuk Israel and Thomas Kosch, "Evaluating Graphical Perception in Virtual Reality: Evidence from Two Visualization Experiments," Proceedings of the 52nd Graphics Interface Conference (GI '26), Waterloo, June 2026. Two experiments: a conceptual replication of [Cleveland & McGill (1984)](cleveland-mcgill-1984.md) on a virtual tabletop, and a partial replication of Bezerianos & Isenberg (2012) on a virtual wall.

**How this was read.** The camera-ready PDF from the GI '26 program site at `cs.uwaterloo.ca/~dvogel/gi2026/papers/1088b.pdf`, fetched with `curl` and a browser user-agent, title checked against the intended target before anything was quoted. **Two extractions were needed and the difference matters.** `pdftotext -layout` silently dropped every Greek letter and every math-italic variable, so `F(2, 24) = 33.01` came out as `(2, 24)= 33.01` and every generalized eta squared came out as a bare `2`; it also dropped hypothesis H3 entirely, where a figure caption interleaved with it. A second pass through `pypdf`, with the Mathematical Alphanumeric Symbols block normalized back to ASCII, recovered all of it. Every statistic below comes from that second extraction. The abstract was not used as the source of any figure. `status_partial` because the paper is read end to end while the analysis scripts and materials the authors deposited on OSF were not opened, so nothing here is checked against their data.

**What it is good for.** Whether the position-length-area ordering survives a change of medium, measured rather than assumed. Also a large, clean interaction between bar orientation and viewing geometry, and the reason the paper's own abstract overstates it.

**What it does not settle.** Anything about angle, which is not a condition here, so the [contested joint](../concepts/channels.md#the-one-joint-where-the-folk-ranking-breaks) between length and angle is untouched. Anything about a conventional screen: every stimulus was rendered in a head-mounted display. And distance separately from viewing angle, which the design confounds.

---

## Design

Within-subjects, two experiments, order counterbalanced. 13 participants (students and researchers at Sorbonne Université), 102 trials each: 54 on the virtual table, 48 on the virtual wall. HTC Vive at 2160 x 1200, 90 Hz, 110-degree field of view; Unity 3D; responses entered on the controller thumbpad as an integer percentage.

The task is ratio estimation throughout, chosen over Cleveland & McGill's constant-sum production: *"If the larger shape represents 100%, what percentage is the smaller shape?"* The dependent variable is absolute error in percentage points.

**Experiment 1, the virtual table.** A virtual A4 sheet on a 72 cm table, head movement unconstrained, three conditions:

| Condition | What was drawn | The channel it stands for |
|---|---|---|
| Bar Chart | Vertical bars aligned at their bases | Position along a common scale |
| Line | Vertical lines at randomized positions, deliberately not aligned | Length |
| Circle | Circles at randomized positions | Area |

**Experiment 2, the virtual wall.** Only bar charts, crossed 2 x 3: Orientation (vertical, horizontal) by Position. The three positions are **lateral offsets to the participant's right** of 0 m, 2.75 m and 4.8125 m, reproducing positions A3, E3 and H3 of Bezerianos & Isenberg's tiled display; the participant sat 60 cm from the wall at its leftmost point and was free to rotate. Bezerianos & Isenberg's physical bezels were not reproduced, since a virtual wall has none, and a textured surface was substituted for the depth cues the physical wall supplied implicitly.

## Experiment 1: the ordering replicates

Repeated-measures ANOVA on participant means, Greenhouse-Geisser corrected: F(2, 24) = 33.01, p < .001, generalized η² = .62.

| Condition | Mean absolute error | SD |
|---|---|---|
| Bar Chart | 3.68% | 0.69 |
| Line | 6.61% | 2.60 |
| Circle | 12.05% | 4.03 |

All three Bonferroni-corrected pairwise contrasts are significant and the effect sizes are large: area against bar p < .001, d = 2.65; area against length p = .004, d = 1.60; length against bar p = .002, d = 1.28. A trial-level mixed-effects model with random participant intercepts reproduces the pattern.

**Position beats length beats area, in a head-mounted display, with all three measured inside one experiment.** That last clause is the part [Cleveland & McGill](cleveland-mcgill-1984.md) could not offer: their length result and their angle result come from two experiments they state may not be compared. Here the three conditions are blocked within one design and are comparable by construction.

**The exploratory power-law fits point the same way.** Fitting *y = x^a* per participant per condition, where an exponent of 1 is veridical: bar 1.04 (SD 0.05), length 1.10 (SD 0.15), area 1.49 (SD 0.35). The paper flags this analysis as descriptive rather than inferential.

Absolute errors are higher than paper-and-desktop baselines, which the authors attribute to known distance and scale distortion in immersive displays.

## Experiment 2: orientation and viewing geometry interact

Two-way repeated-measures ANOVA. Main effect of Orientation, F(1, 12) = 77.43, p < .001, generalized η² = .49. Main effect of Position, F(2, 24) = 41.38, p < .001, η² = .39. **Orientation by Position interaction**, F(2, 24) = 27.45, p < .001, η² = .40.

Collapsed across positions, horizontal bars produced 6.40% error against vertical bars' 3.33%: paired t(12) = 8.80, p < .001, mean difference 3.07 percentage points, 95% CI [2.31, 3.83], d = 2.46.

**The collapsed number is not the finding, because the effect is absent at one of the three positions:**

| Position | Lateral offset | Horizontal against vertical |
|---|---|---|
| 0 | 0 m, face-on | **No significant difference, p = .713** |
| 1 | 2.75 m | Horizontal worse, p < .001 |
| 2 | 4.8125 m | Horizontal worse, p < .001 |

Within the horizontal condition, error rose monotonically with offset and every pairwise contrast was significant and large: 0 against 1 is 3.37 pp (d = 1.91), 0 against 2 is 6.20 pp (d = 3.28), 1 against 2 is 2.84 pp (d = 1.22). **Within the vertical condition, no pairwise contrast was significant at all** (p = .942, .998, .960). The power-law exponents track it: horizontal 1.01, 1.10, 1.26 across the three positions, vertical 1.04, 1.01, 1.05.

## The mechanism, and how far it travels

The authors offer a geometric account rather than a claim about horizontal bars as such. Oblique viewing foreshortens the retinal projection along one axis, and the visual system's usual correction for that leans on depth cues the virtual environment does not supply as richly as a physical room does. Bezerianos & Isenberg's participants had physical bezels between display panels and reportedly used them as length references; the virtual wall had none. The authors say plainly that their result diverges from the study they replicated:

> "Comparatively, Bezerianos & Isenberg found horizontal length judgments to be relatively unaffected by viewing distance."

and read that divergence as an artifact of the changed apparatus:

> "an outcome consistent with the removal of bezel-based spatial anchors rather than a fundamental change in the perceptual hierarchy"

Two further mechanisms offered are properties of the headset: transverse chromatic aberration measurable beyond roughly 6 degrees from the center of the field of view, which blurs bar edges laterally, and the vergence-accommodation conflict of fixed-focus optics.

**The asymmetry follows from which axis carries the value.** A vertical bar's length runs perpendicular to the axis being foreshortened at a lateral offset; a horizontal bar's length runs along it. A fronto-parallel display has no foreshortening axis, and at Position 0 there was no measured difference.

## Limits, and two internal inconsistencies

**Limits the authors state.** Thirteen participants. Demographic records were lost when access to the data-collection platform expired, so age, gender and prior VR or visualization experience are unavailable, and the authors note this leaves open whether the Experiment 2 magnitudes are partly a sample effect. Stimuli were deliberately simple, so trend and pattern tasks are untouched. Ratio estimation is exposed to rounding and anchoring, and the thumbpad's per-frame increment made fine correction costly enough that participants likely satisficed. One headset, one tracking setup. Spatial variation was restricted to the horizontal axis, so vertical obliqueness is untested.

**Distance and viewing angle are confounded**, which the paper does not name as a limitation. Position varies lateral offset along a wall the participant sits 60 cm from, so a farther stimulus is also a more oblique one, and nothing here separates the two. H3 is worded as distance, "as charts are positioned closer to the viewer," while the discussion's mechanism is angular.

**Two places where the paper disagrees with itself**, neither of which changes a result:

- Section 3.4 says that in the table experiment "the larger stimulus randomly varied in size by up to 10% between trials to prevent participants from adapting to a fixed reference size." Section 3.6 says "While Cleveland & McGill randomized the size of the reference stimulus, we fixed it across trials in this experiment." The reconciling reading is that the reference was jittered rather than randomized across the full range, but as written the two sentences conflict.
- The Results scope H3 to one orientation: "Therefore, H3 is only supported for horizontal bars." The Discussion drops the qualifier, "supporting H2 and H3." The position contrasts support the Results version.

## Evidence class of what this paper supports

- **Evidence-backed, within scope.** In a head-mounted display on a virtual tabletop, ratio judgments off aligned bars are more accurate than off unaligned lengths, which are more accurate than off circle areas. Large effects, one comparable design, and the first replication of that ordering in this corpus outside a two-dimensional display.
- **Evidence-backed, within a narrower scope than the abstract carries.** On a virtual wall, horizontal bars are read less accurately than vertical bars **at oblique lateral positions**, and identically at face-on. The degradation with offset is confined to the horizontal orientation.
- **Authority-asserted.** The foreshortening, bezel-anchor, chromatic-aberration and vergence-accommodation explanations. None was manipulated; they are the authors' reading of why their result diverges from the study they replicated.
- **Absence of evidence.** Angle as a condition, non-HMD displays, vertical obliqueness, distance separated from viewing angle, and any task other than two-mark ratio estimation.

## See also

- [cleveland-mcgill-1984.md](cleveland-mcgill-1984.md) — the ordering being replicated, and the comparability caveat this design does not have
- [heer-bostock-2010.md](heer-bostock-2010.md) — the other replication in this corpus, and the one that failed to separate length from angle
- [../concepts/channels.md](../concepts/channels.md) — where the measured-against-inherited table records this
- [../chart-types/bar-chart.md](../chart-types/bar-chart.md) — the form whose orientation is at issue
- [../refutations.md](../refutations.md)
