---
type: study
status: primary-read
retrieved: 2026-08-29
---

# Gutwin, Mairena & Bandi (2023), *Showing Flow*

Carl Gutwin, Aristides Mairena and Venkat Bandi, "Showing Flow: Comparing Usability of Chord and Sankey Diagrams," CHI 2023. A test of two forms in the [flow](../chart-types/flow.md) group.

**What it is good for.** Radial against linear layouts of the same flow data, measured on time, errors, effort and preference. The gap is much smaller than the abstract suggests and depends on how often the reader has seen the form.

**What it does not settle.** Whether a reader can get a *volume* off a ribbon. No task asks for one, so the value-extraction cautions on [sankey-diagram.md](../chart-types/sankey-diagram.md) and [chord-diagram.md](../chart-types/chord-diagram.md) are untouched. Nor interactive versions of either form.

**How this was read.** ACM's gold open-access HTML full text at `doi.org/10.1145/3544548.3581119`, read in a browser and extracted section by section. ACM returns 403 to `curl`. Unpaywall, OpenAlex and Semantic Scholar all point back at the ACM PDF, and no copy was on the local filesystem. The title was checked against the DOI before quoting. Every number and quote comes from that extraction, not the abstract.

## Design

Within-participants, fully crossed: **VisType** (Chord, Sankey); **QuestionType** (Existence, Find Element, Compare Magnitude, Minimum/Maximum, Count Links); **Dataset** (Debt, Immigration, Phone switching, Space investment); and **QuestionIteration**, the first through fourth exposure to each question type. 40 questions per participant, 2,040 trials. VisType fully counterbalanced, Dataset by Latin square.

**Participants.** 57 recruited on Mechanical Turk, 51 complete sessions (32 men, 19 women, mean age 37.2), paid $6 for about 30 minutes. All were novices:

> "None of the participants reported using any type of flow visualization (including Chord or Sankey diagrams)."

**Stimuli.** Custom D3 SVG, one Tableau10 color per node, D3 `ribbonArrow` arrowheads, equal drawing areas, entities in source order. 8 to 15 nodes and 50 to 100 links, directed in three of four datasets. Crossings were comparable across types, and no question turned on a link under eight pixels wide.

> "We did not add any interactivity (e.g., hover highlighting) to either type, as a main goal of the study was to assess the diagrams' ability to support purely visual interpretation and information-seeking."

Errors are retry counts, and time includes the retries, so the two are not independent:

> "If participants selected an incorrect answer, the system asked them to try again; once the correct answer was chosen, the system moved to the next question."

> "record[ed] the time needed for participants to correctly answer the questions, including time to fix errors"

## Results

**Completion time.** Chord 22.01s, Sankey 18.35s. VisType F(1,50) = 16.93, p < .001, generalized η² = 0.02. No Dataset effect (F(3,150) = 0.19, p = .90), no interactions with VisType.

**Errors.** Sankey 0.96 per question, Chord 1.07. VisType F(1,50) = 5.37, p < .05, η² = 0.001. A three-way interaction (F(12,600) = 2.23, p < .01) "appears to be caused by particularly high error counts for Chord with 'count links' questions."

**Perceived effort.** NASA-TLX favored Sankey on mental effort, perceived success, work required and frustration, all p < 0.01.

**Preference**, the largest effect:

| Question | Chord | Sankey | χ² | p |
|---|---|---|---|---|
| Which was fastest? | 16 | 35 | 7.08 | < .05 |
| Which was most accurate? | 8 | 43 | 24.02 | < .001 |
| Which did you prefer overall? | 9 | 42 | 21.35 | < .001 |

## Effect size and first exposure

The paper's generalized η² thresholds are "with < .01 considered small, .06 medium, and > .14 large". Time, at 0.02, is between small and medium. Errors, at 0.001, are a tenth of small, on a raw gap of 0.11 errors per question. The 3.7-second gap sits on a roughly twenty-second task.

Time showed a QuestionIteration by VisType interaction (F(3,150) = 4.89, p < .005):

> "We found participants improved as they gained more experience with the visualizations – but there were clear differences between the visualizations, with Chord substantially slower (compared to Sankey) on the first question iteration than on iterations 2-4. By the fourth iteration, there is little difference between the two types."

Errors had no main effect of iteration (F(3,150) = 0.92, p = .43) but an interaction (F(3,150) = 5.24, p < .005), with the Chord penalty in iterations one and two. The Discussion gives first-iteration gaps of 9.2s and 0.42 errors, against 3.7s and 0.1 errors overall. The authors argue the first look is what counts:

> "Performance with Chord diagrams was worse on the first iteration of each question type, which is an important result because Chord diagrams have often been used in settings where users are unfamiliar with the visualization and will be carrying out analyses for the first time – e.g., mainstream media stories [46] or 'Data Storytelling' [7]."

A one-look audience pays roughly nine seconds and half an error per question. Repeat users pay close to nothing.

## Limits

The authors' mechanisms for the Chord penalty are tracing a ribbon, reading arrowhead direction, and separating incoming from outgoing links at a shared node. Hover highlighting addresses all three, and nearly every deployed chord diagram has it; the authors list interactivity as future work. In [ghoniem-2004.md](ghoniem-2004.md) against [okoe-2018.md](okoe-2018.md), adding interaction and real topology reversed a static result. This finding is about *static* chord diagrams.

The authors also state: one node per entity, so the incoming-outgoing problem was not designed away; 8 to 15 nodes only; directed links only, though chord is often used for undirected data; MTurk participants with no domain interest and fixed pay; standard D3 parameters, no clutter-reducing layout.

One number does not reconcile. The results call the gap "a difference of 3.74s", but 22.01 minus 18.35 is 3.66, and in a balanced within-participants design those should match. The Discussion rounds to 3.7s. Nothing turns on it, and unlike [Pandey](pandey-2015-deceptive-visualizations.md), no passage inverts its own table.

## Evidence class of what this paper supports

- **Evidence-backed, within scope.** On static 8-to-15-node directed flow drawings, novices are slower with chord than Sankey, make marginally more errors and report more effort, with the penalties concentrated in first exposure.
- **Evidence-backed.** Preference: 42 of 51 chose Sankey overall. It is a preference measure.
- **Authority-asserted.** The mechanisms (left-to-right familiarity, arrowhead visibility, ribbon thinning at the circle's center, shared nodes) come from participant comments and the authors' reading, not a manipulation. The shared-node account has some support: the one-way Space dataset showed similar link-counting performance on both types.
- **Absence of evidence.** Interactive versions, larger data, undirected data, reading a volume off a ribbon width, and every other flow form.

## See also

- [../chart-types/chord-diagram.md](../chart-types/chord-diagram.md)
- [../chart-types/sankey-diagram.md](../chart-types/sankey-diagram.md)
- [../chart-types/flow.md](../chart-types/flow.md): the group
- [ghoniem-2004.md](ghoniem-2004.md) and [okoe-2018.md](okoe-2018.md): static versus interactive
- [../refutations.md](../refutations.md)
