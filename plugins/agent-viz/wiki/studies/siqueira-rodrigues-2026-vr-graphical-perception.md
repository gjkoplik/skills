---
type: study
status: primary-read
status_partial: true
retrieved: 2026-09-05
---

# Siqueira Rodrigues, Israel & Kosch (2026), *Evaluating Graphical Perception in Virtual Reality*

Lucas Siqueira Rodrigues, Johann Habakuk Israel and Thomas Kosch, "Evaluating Graphical Perception in Virtual Reality: Evidence from Two Visualization Experiments," Proceedings of the 52nd Graphics Interface Conference (GI '26), Waterloo, June 2026. A conceptual replication of [Cleveland & McGill (1984)](cleveland-mcgill-1984.md) on a virtual tabletop, and a partial replication of Bezerianos & Isenberg (2012) on a virtual wall.

**How this was read.** The camera-ready PDF from the GI '26 program site (`cs.uwaterloo.ca/~dvogel/gi2026/papers/1088b.pdf`), fetched with `curl` and a browser user-agent, title checked before quoting. `pdftotext -layout` silently dropped every Greek letter and math-italic variable (`F(2, 24) = 33.01` became `(2, 24)= 33.01`, each generalized eta squared a bare `2`) and dropped hypothesis H3 where a figure caption interleaved with it. A `pypdf` pass with the Mathematical Alphanumeric Symbols block normalized to ASCII recovered all of it and supplies every statistic below. Nothing was taken from the abstract. `status_partial` because the authors' OSF analysis scripts and materials were not opened, so nothing is checked against their data.

**What it is good for.** Whether the position-length-area ordering survives a change of medium. Also a large interaction between bar orientation and viewing geometry, which the paper's own abstract states more broadly than its results support.

**What it does not settle.** Angle, which is not a condition, so the [contested joint](../concepts/channels.md#the-one-joint-where-the-folk-ranking-breaks) between length and angle is untouched. Conventional screens, since every stimulus was in a head-mounted display. Distance separately from viewing angle, which the design confounds.

---

## Design

Within-subjects, two experiments, order counterbalanced. 13 participants (students and researchers at Sorbonne Université), 102 trials each: 54 on the virtual table, 48 on the virtual wall. HTC Vive (2160 x 1200, 90 Hz, 110-degree field of view), Unity 3D, integer-percentage responses on the controller thumbpad.

The task is ratio estimation, not Cleveland & McGill's constant-sum production: *"If the larger shape represents 100%, what percentage is the smaller shape?"* The dependent variable is absolute error in percentage points.

**Experiment 1, the virtual table.** A virtual A4 sheet on a 72 cm table, head movement unconstrained.

| Condition | What was drawn | The channel it stands for |
|---|---|---|
| Bar Chart | Vertical bars aligned at their bases | Position along a common scale |
| Line | Vertical lines at randomized positions, not aligned | Length |
| Circle | Circles at randomized positions | Area |

**Experiment 2, the virtual wall.** Bar charts only, Orientation (vertical, horizontal) by Position, 2 x 3. The positions are lateral offsets to the participant's right of 0 m, 2.75 m and 4.8125 m, reproducing positions A3, E3 and H3 of Bezerianos & Isenberg's tiled display. The participant sat 60 cm from the wall at its leftmost point and was free to rotate. The virtual wall had none of the original's physical bezels, and a textured surface stood in for the depth cues a physical wall supplies.

## Experiment 1: the ordering replicates

Repeated-measures ANOVA on participant means, Greenhouse-Geisser corrected: F(2, 24) = 33.01, p < .001, generalized η² = .62.

| Condition | Mean absolute error | SD |
|---|---|---|
| Bar Chart | 3.68% | 0.69 |
| Line | 6.61% | 2.60 |
| Circle | 12.05% | 4.03 |

All three Bonferroni-corrected pairwise contrasts are significant: area against bar p < .001, d = 2.65; area against length p = .004, d = 1.60; length against bar p = .002, d = 1.28. A trial-level mixed-effects model with random participant intercepts reproduces the pattern.

The three channels were blocked within one design, so they are comparable by construction. [Cleveland & McGill](cleveland-mcgill-1984.md) could not offer that, because their length and angle results come from two experiments they state may not be compared.

Exploratory power-law fits of *y = x^a* per participant, where an exponent of 1 is veridical, agree: bar 1.04 (SD 0.05), length 1.10 (SD 0.15), area 1.49 (SD 0.35). The paper calls this analysis descriptive, not inferential. Absolute errors exceed paper-and-desktop baselines, which the authors attribute to known distance and scale distortion in immersive displays.

## Experiment 2: orientation and viewing geometry interact

Two-way repeated-measures ANOVA. Orientation: F(1, 12) = 77.43, p < .001, generalized η² = .49. Position: F(2, 24) = 41.38, p < .001, η² = .39. Interaction: F(2, 24) = 27.45, p < .001, η² = .40.

Collapsed across positions, horizontal bars produced 6.40% error against vertical bars' 3.33%: paired t(12) = 8.80, p < .001, mean difference 3.07 percentage points, 95% CI [2.31, 3.83], d = 2.46. The effect is absent at one of the three positions:

| Position | Lateral offset | Horizontal against vertical |
|---|---|---|
| 0 | 0 m, face-on | No significant difference, p = .713 |
| 1 | 2.75 m | Horizontal worse, p < .001 |
| 2 | 4.8125 m | Horizontal worse, p < .001 |

Horizontal error rose monotonically with offset, and every pairwise contrast was significant: 0 against 1 is 3.37 pp (d = 1.91), 0 against 2 is 6.20 pp (d = 3.28), 1 against 2 is 2.84 pp (d = 1.22). No vertical contrast was significant (p = .942, .998, .960). Power-law exponents across the three positions: horizontal 1.01, 1.10, 1.26, vertical 1.04, 1.01, 1.05.

## The mechanism, and how far it travels

The authors' account is geometric, not a claim about horizontal bars as such. Oblique viewing foreshortens the retinal projection along one axis, and the correction leans on depth cues a virtual environment supplies less richly than a room. At a lateral offset a horizontal bar's length runs along the foreshortened axis and a vertical bar's runs across it. Face-on there is no such axis, and no measured difference.

Bezerianos & Isenberg's participants reportedly used the bezels between display panels as length references. The authors acknowledge the divergence:

> "Comparatively, Bezerianos & Isenberg found horizontal length judgments to be relatively unaffected by viewing distance."

and attribute it to the changed apparatus:

> "an outcome consistent with the removal of bezel-based spatial anchors rather than a fundamental change in the perceptual hierarchy"

They also cite two headset properties: transverse chromatic aberration beyond roughly 6 degrees from the center of the field of view, which blurs bar edges laterally, and the vergence-accommodation conflict of fixed-focus optics.

## Limits, and two internal inconsistencies

The authors name these limits:

- Thirteen participants, and demographic records (age, gender, VR and visualization experience) lost when platform access expired. Whether the Experiment 2 magnitudes are partly a sample effect is open.
- Simple stimuli, so no trend or pattern tasks.
- Ratio estimation invites rounding and anchoring, and the thumbpad's per-frame increment likely made participants satisfice.
- One headset and tracking setup, and horizontal spatial variation only.

The paper does not name the confound between distance and viewing angle: a farther stimulus on this wall is also a more oblique one. H3 is worded as distance, "as charts are positioned closer to the viewer," while the discussion's mechanism is angular.

The paper contradicts itself twice, without changing a result:

- Section 3.4 says that in the table experiment "the larger stimulus randomly varied in size by up to 10% between trials to prevent participants from adapting to a fixed reference size." Section 3.6 says "While Cleveland & McGill randomized the size of the reference stimulus, we fixed it across trials in this experiment." Jitter rather than full randomization would reconcile them, but as written they conflict.
- The Results scope H3 to one orientation: "Therefore, H3 is only supported for horizontal bars." The Discussion drops the qualifier, "supporting H2 and H3." The position contrasts support the Results version.

## Evidence class of what this paper supports

- **Evidence-backed, within scope.** In a head-mounted display on a virtual tabletop, ratio judgments are most accurate off aligned bars, then unaligned lengths, then circle areas, with large effects in one comparable design. It is the ordering's first replication in this corpus outside a two-dimensional display.
- **Evidence-backed, within a narrower scope than the abstract carries.** On a virtual wall, horizontal bars are read less accurately than vertical bars at oblique lateral positions and identically face-on.
- **Authority-asserted.** The foreshortening, bezel-anchor, chromatic-aberration and vergence-accommodation explanations, none of them manipulated.
- **Absence of evidence.** Angle as a condition, non-HMD displays, vertical obliqueness, distance separated from viewing angle, and any task other than two-mark ratio estimation.

## See also

- [cleveland-mcgill-1984.md](cleveland-mcgill-1984.md): the ordering being replicated, and the comparability caveat this design avoids
- [heer-bostock-2010.md](heer-bostock-2010.md): the other replication in this corpus, which did not find angle worse than length
- [../concepts/channels.md](../concepts/channels.md): the measured-against-inherited table that records this study
- [../chart-types/bar-chart.md](../chart-types/bar-chart.md): the form whose orientation is at issue
- [../refutations.md](../refutations.md)
