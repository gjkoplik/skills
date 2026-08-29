---
type: study
status: primary-read
retrieved: 2026-08-29
---

# Gutwin, Mairena & Bandi (2023), *Showing Flow*

Carl Gutwin, Aristides Mairena and Venkat Bandi, "Showing Flow: Comparing Usability of Chord and Sankey Diagrams," CHI 2023. The first study in this corpus that tests any form in the [flow](../chart-types/flow.md) group.

**How this was read.** ACM's gold open-access HTML full text at `doi.org/10.1145/3544548.3581119`, read in a browser and extracted section by section from the rendered document. `curl` could not reach it: ACM's edge returns 403 to a scripted client, and no repository copy exists, which was checked against Unpaywall, OpenAlex and Semantic Scholar (all three point back at the ACM PDF) and against the local filesystem. The title on the retrieved document was checked against the DOI before anything below was quoted. Every number and quote here comes from that extraction; the abstract was not used as the source of any figure.

**What it is good for.** A measured comparison of a radial against a linear layout of the same flow data, on time, errors, perceived effort and preference. Also the size of the gap, which is much smaller than the abstract's wording suggests, and its dependence on how many times the reader has seen the form before.

**What it does not settle.** Whether a reader can get a *volume* off a ribbon. No condition here asks anyone to read a quantity off a width, so the value-extraction cautions on [sankey-diagram.md](../chart-types/sankey-diagram.md) and [chord-diagram.md](../chart-types/chord-diagram.md) are untouched by it. It also says nothing about interactive versions of either form.

---

## Design

Within-participants, fully crossed:

- **VisType**: Chord, Sankey
- **QuestionType**: Existence, Find Element, Compare Magnitude, Minimum/Maximum, Count Links
- **Dataset**: Debt, Immigration, Phone switching, Space investment
- **QuestionIteration**: first through fourth time the participant saw each question type, derived from the other factors

40 questions per participant, 2,040 trials in total. VisType was fully counterbalanced and Dataset used a Latin square.

**Participants.** 57 recruited on Mechanical Turk, 51 complete sessions (32 men, 19 women, mean age 37.2), paid $6 for about 30 minutes. Every participant was a novice on the stimulus: "None of the participants reported using any type of flow visualization (including Chord or Sankey diagrams)."

**Stimuli.** Custom D3 rendering to SVG, one color per node from Tableau10, arrowheads from D3's `ribbonArrow`, equal drawing areas for the two types, entities left in the source dataset's order. Datasets were 8 to 15 nodes and 50 to 100 links, with directed links in three of the four. The authors checked that neither type carried noticeably more crossings and that no question turned on a link under eight pixels wide.

**Two design choices decide how far this generalizes**, and the authors name both. The first:

> "We did not add any interactivity (e.g., hover highlighting) to either type, as a main goal of the study was to assess the diagrams' ability to support purely visual interpretation and information-seeking."

The second is the error measure, which is a retry count rather than a single response: "If participants selected an incorrect answer, the system asked them to try again; once the correct answer was chosen, the system moved to the next question." Completion time "record[ed] the time needed for participants to correctly answer the questions, including time to fix errors", so time and errors are not independent measures.

## Results

**Completion time.** Chord 22.01s, Sankey 18.35s. Main effect of VisType F(1,50) = 16.93, p < .001, generalized η² = 0.02. No effect of Dataset (F(3,150) = 0.19, p = .90) and no interactions with VisType.

**Errors.** Chord 1.07 per question, Sankey 0.96, a gap of 0.11. Main effect of VisType F(1,50) = 5.37, p < .05, η² = 0.001. A three-way interaction (F(12,600) = 2.23, p < .01) that "appears to be caused by particularly high error counts for Chord with 'count links' questions."

**Perceived effort.** NASA-TLX differences favoring Sankey on mental effort, perceived success, work required, and frustration, all p < 0.01.

**Preference**, which is the paper's largest effect by a wide margin:

| Question | Chord | Sankey | χ² | p |
|---|---|---|---|---|
| Which was fastest? | 16 | 35 | 7.08 | < .05 |
| Which was most accurate? | 8 | 43 | 24.02 | < .001 |
| Which did you prefer overall? | 9 | 42 | 21.35 | < .001 |

## Effect size and first exposure

**Both performance effects are tiny, by the paper's own yardstick.** It states its thresholds up front: generalized η² "with < .01 considered small, .06 medium, and > .14 large". The time effect lands at 0.02, between small and medium. **The error effect lands at 0.001**, a tenth of the paper's own benchmark for small, on a raw gap of 0.11 errors per question. "Made more errors" is true, statistically significant, and worth about a ninth of an error. The 3.7-second time gap sits on a task taking roughly twenty seconds.

**The gap is mostly a first-exposure effect, and it closes.** Time showed a QuestionIteration by VisType interaction (F(3,150) = 4.89, p < .005), and the authors describe it plainly:

> "We found participants improved as they gained more experience with the visualizations – but there were clear differences between the visualizations, with Chord substantially slower (compared to Sankey) on the first question iteration than on iterations 2-4. By the fourth iteration, there is little difference between the two types."

Errors behave the same way: no main effect of iteration (F(3,150) = 0.92, p = .43) but an interaction (F(3,150) = 5.24, p < .005), with the Chord penalty concentrated in iterations one and two. The Discussion gives the first-iteration gaps as 9.2s and 0.42 errors, against 3.7s and 0.1 errors overall.

**That cuts both ways, and the authors argue the second direction themselves.** A shrinking penalty does not dispose of the result, because chord diagrams are mostly deployed where nobody gets a fourth look:

> "Performance with Chord diagrams was worse on the first iteration of each question type, which is an important result because Chord diagrams have often been used in settings where users are unfamiliar with the visualization and will be carrying out analyses for the first time – e.g., mainstream media stories [46] or 'Data Storytelling' [7]."

The penalty is therefore conditional on the reader rather than on the chart. A one-look audience pays roughly nine seconds and half an error per question. An audience that will work with the form repeatedly pays close to nothing.

## The interaction limit

**No interaction.** The three mechanisms the authors offer for the Chord penalty are tracing a ribbon from source to destination, seeing which way an arrowhead points, and separating incoming from outgoing links at a shared node. Hover highlighting addresses all three, and close to every deployed chord diagram has it. The authors list interactivity as future work.

This is the same shape as [ghoniem-2004.md](ghoniem-2004.md) against [okoe-2018.md](okoe-2018.md), where adding interaction and moving to real network topology reversed a static result. That does not make this study wrong. It does mean the finding is about *static* chord diagrams, and that the obvious follow-up has a live chance of coming out differently, as it did last time.

**Other limits the authors state.** One node per entity, so the incoming-outgoing separation problem was not designed away; medium-sized data at 8 to 15 nodes, with larger sets untested; directed links only, though chord is commonly used for undirected data; MTurk participants with no domain interest and a fixed payment; and standard D3 parameters, so no clutter-reducing layout was tried.

**One internal check that does not reconcile.** The results text gives the means as 22.01s and 18.35s and calls the gap "a difference of 3.74s"; those means differ by 3.66. The design is balanced and within-participants, so the mean of the paired differences should equal the difference of the means. The Discussion rounds to 3.7s. Nothing downstream turns on it, and it is not the [Pandey](pandey-2015-deceptive-visualizations.md) case, where a Discussion passage inverted its own table.

## Evidence class of what this paper supports

- **Evidence-backed, within scope.** On static, non-interactive drawings of 8-to-15-node directed flow data, novice readers answer questions more slowly with a chord diagram than with an equivalent Sankey, make marginally more errors, report more effort, and prefer the Sankey by a wide margin. The time and error penalties are largest on first exposure and are close to gone by the fourth.
- **Evidence-backed, and the strongest result here.** Preference: 42 of 51 chose Sankey overall. It is a preference measure.
- **Authority-asserted.** The mechanisms: left-to-right familiarity, arrowhead visibility, ribbon thinning at the circle's center, and shared incoming-outgoing nodes. These come from participant comments and the authors' reading rather than from a manipulation. The one with internal support is the shared-node account, since the one-way Space dataset showed similar link-counting performance across both types.
- **Absence of evidence.** Interactive versions of either form, larger data, undirected data, reading a volume off a ribbon width, and every other form in the flow group.

## See also

- [../chart-types/chord-diagram.md](../chart-types/chord-diagram.md) — the form this measures a cost for
- [../chart-types/sankey-diagram.md](../chart-types/sankey-diagram.md)
- [../chart-types/flow.md](../chart-types/flow.md) — the group, which until this page had no experiment behind any of its forms
- [ghoniem-2004.md](ghoniem-2004.md) and [okoe-2018.md](okoe-2018.md) — the corpus's other static-versus-interactive pair, and how that one turned out
- [../refutations.md](../refutations.md)
