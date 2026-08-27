---
type: source
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Chartability

A set of 50 accessibility heuristics for data visualizations, organized under seven principles: the four standard web-accessibility principles (Perceivable, Operable, Understandable, Robust) plus three that extend Robust (Compromising, Assistive, Flexible), giving **POUR+CAF**. Created by Frank Elavsky, published with an academic paper, licensed CC-BY-SA, and explicitly built to be adopted.

**How this was read.** `primary-read` for the heuristics; `not-reached` for the paper. The home page (`chartability.fizz.studio`) and the complete POUR+CAF workbook (`chartability.github.io/POUR-CAF/`) were fetched and converted to text locally, retrieved 2026-08-23; all 50 heuristic titles, the 14 critical flags, and the descriptions quoted below come from that text. **The EuroVis 2022 paper itself was not opened.** The citation as printed on the home page is: "Elavsky, F. and Bennett, C. and Moritz, D. How accessible is my visualization? Evaluating visualization accessibility with Chartability. EuroVis 2022."

**What it is good for.** Being the accessibility inventory this project does not have. It is peer-reviewed, community-tested with disabled reviewers, openly licensed, structured for auditing rather than for reading, and it comes with a shortlist that makes it usable in half an hour. This is the source where **importing beats deriving**, and the recommendation from [roll-call.md](../roll-call.md) and the wiki README stands: adopt it rather than re-deriving a fifth of it.

**What it does not settle.** It is accessibility only. It has nothing on chart-type choice, narrative, color palette design beyond CVD safety and contrast, statistical honesty beyond one heuristic on uncertainty, or production. It is also **not a compliance instrument**: "Chartability should never be used in place of a compliance audit but always in tandem with it." And roughly half of it is scoped to interactive systems, so a static PNG cannot fail most of Operable, Compromising, or Flexible.

---

## Why the framing is unusual, and why that matters

Three design decisions distinguish Chartability from a checklist, and all three affect how it should be adopted.

**It is stated as failures, deliberately.** Every heuristic is named for the defect: "Low contrast", "Small text size", "No table", "Axis labels are unclear or missing".

> "An important note about language: Chartability's tests are framed in negative language, like 'Target pointer interaction size is too small.' This is intentional. Chartability is not meant to be used to 'pass' accessibility requirements. **You cannot 'pass' Chartability 100%.** Rather, Chartability is simply framed as a tool that helps people catch known barriers, or 'failures.' It is possible to have 0 failures in Chartability but still have accessibility issues."

**Accessibility is a scale, not a state.**

> "Generally, Chartability approaches accessibility as a scale rather than a state: how accessible a DX is is determined by how few failures it contains. It should be assumed that even the absolute best DX may contain several failures, even after remediation."

with an obligation attached that is more demanding than a pass/fail gate:

> "Chartability's insistence on a scale (instead of a state) of accessibility requires that designers and creators consider their choices carefully: they must be willing to argue that lack of scope, time, or research or perhaps a unique consideration led to a given failure. **No failure should be left unconsidered.**"

**Inconclusive means fail.** "The auditor should assume failure when tests are inconclusive." That is the opposite default from most review, and it is the right one for a checker that cannot see rendered output.

The negative framing is the piece most likely to be lost in translation. A bar that converts "Low contrast (critical)" into "ensure sufficient contrast" has quietly reintroduced the pass/fail model the author rejected. It also loses the scale, which is what makes the framework usable on a scrappy diagnostic plot as well as on a published dashboard.

## The 50 heuristics

Critical ones marked. Descriptions are the workbook's own, quoted where they carry a testable threshold.

### Perceivable (8)

1. **Low contrast** `critical` -- "Geometries and large text must have >3:1 contrast against background, Regular text must have >4.5:1."
2. **Content is only visual** `critical` -- "Information in the chart must be available without visuals (no screen reader/braille support)... All annotations, 'visually apparent' trends or features, and all major narrative elements must be exposed to screen readers."
3. **Small text size** `critical` -- "Text (any) must not be smaller than 9pt/12px in size. Ideally only minor text is rendered at 9pt (Eg. axis labels) while all other text is larger."
4. **Visual presents seizure risk** `critical`
5. **Color is used alone to communicate meaning** -- "For categorical color schemes: Textures, shapes, or size (for filled elements) or dash patterns (for lines and paths) are required."
6. **Meaningful elements can be distinguished from each other** -- "Adjacent elements must have at least 1px white space between them (like stacked bars or pie charts where elements 'touch')."
7. **Not CVD-friendly** -- "Use tools like Viz Palette or Chroma to test the chart's color palette. Must not have major warnings on either."
8. **Spacing is inappropriate**

### Operable (8)

9. **Interaction modality only has one input type** `critical`
10. **No interaction cues or instructions** `critical`
11. **Controls override AT controls** `critical`
12. **Low contrast on interactive elements**
13. **Keyboard focus indicator missing, obscured, or low contrast**
14. **Inappropriate tab stops**
15. **Complex actions have no alternatives**
16. **Target pointer interaction size is too small**

### Understandable (10)

17. **No explanation for purpose or for how to read** `critical` -- "Chart should explain its purpose and how to read, use, and interpret it."
18. **No title, summary, or caption** `critical` -- "A title, summary, context, or caption must be provided."
19. **Reading level inappropriate** `critical` -- "All text (and alternative text) provided must target a reading grade level of 9 or lower."
20. **Interactive context is not clear**
21. **Information complexity is inappropriate**
22. **Changes are not easy to follow**
23. **Metrics and variables are undefined**
24. **Statistical uncertainty isn't clearly communicated** -- "If any statistical confidence interval exists, it must use clear conventions and provide textual explanation."
25. **Axis labels are unclear or missing** -- "Axis must not be truncated without a clear label."
26. **Controls are inappropriate**

### Robust (3)

27. **Does not conform to standards**
28. **Semantically invalid**
29. **Fragile technology support**

### Compromising (7)

30. **No table** `critical` -- "A table must be provided that contains a human-readable version of the data the chart is based on. This may be excluded if the chart title, summary, context, or annotations are sufficient at conveying all relevant information contained in the chart."
31. **Information can only be reached through single process**
32. **Location and history is unclear**
33. **Interactions are not forgivable**
34. **Information cannot be navigated according to narrative or structure**
35. **Table/data is static**
36. **State is not easy to share and reproduce**

### Assistive (6)

37. **Data density is inappropriate** `critical` -- "If too many elements are competing for the same space... clustering or patterns (or lack of) must be explained, chart must be aggregated to a higher level with less elements, or chart must be divided into smaller charts with less data."
38. **Navigation and interaction is tedious** `critical`
39. **Visually apparent features and relationships are not described** -- "Trends, clusters, patterns, outliers, or significant statistical semantics and findings that are considered 'visually apparent' must be described through text at a minimum."
40. **Data in text is not human-readable**
41. **Space does not handle extremes**
42. **No default "build-your-own" provided**

### Flexible (8)

43. **User style change not respected** `critical`
44. **Long animations cannot be controlled**
45. **Scrolling experiences cannot be altered**
46. **Zoom and reflow are not supported**
47. **User's text adjustments are not respected**
48. **Design is not consistent and familiar**
49. **Contrast and textures cannot be adjusted**
50. **Difficult chart type has no alternative** -- "Pie charts, line charts without discrete marks, and bar charts without countable isotypes all pose cognitive difficulties."

## The shortlist

The 14 critical heuristics **are** the shortlist. From the home page:

> "Chartability is meant to be easy to get started, with a shortlist of 14 tests that can be conducted in 20-40 minutes (depending on the tester's experience). But Chartability's full test suite is also incredibly robust (50 heuristics total) and can integrate well into proper auditing work of complex systems."

and from the workbook:

> "The following section contains Chartability's 7 principles and 50 heuristics, 14 of which are considered critical. Those new to chartability should try testing just the critical heuristics first, and then move on to all of them."

Criticality has a stated definition, which is not "most important":

> "Some tests are considered critical by members of the community because they are prohibitively expensive to fix, common, produces signficant barriers, and/or affect many aspects of a data experience design or development."

Expensive to fix, common, high impact, or wide-reaching. That is a **triage** criterion, and it is why the shortlist is the right entry point rather than an abridged version.

Be careful with the 20-40 minute figure. The home page attaches it to the shortlist; the workbook gives a wider range for a full pass and is blunt about the ceiling: a highly trained auditor may manage 30 minutes, "those new to auditing may take anywhere between 2 and 8 hours to complete a full pass", and professional audits "take weeks of work and have between 100 and 200 pages of documented evidence."

### The 14 criticals, sorted by whether they bind on a static figure

This split is the practical contribution of reading the workbook, and it is not in the source.

**Binds on any static figure (8):**

- Low contrast
- Content is only visual
- Small text size
- No explanation for purpose or for how to read
- No title, summary, or caption
- Reading level inappropriate
- Data density is inappropriate
- User style change not respected (a PNG with hard-coded colors cannot honor an OS high-contrast mode, so it fails by construction)

**Binds only on interactive output (4):**

- Interaction modality only has one input type
- No interaction cues or instructions
- Controls override AT controls
- Navigation and interaction is tedious

**Conditional (2):**

- Visual presents seizure risk (animation only)
- No table (has a stated exemption when the title, summary, context, or annotations already carry the information)

So a figure produced by a plotting library and saved to disk has **eight** critical tests against it, not fourteen. That number is small enough to run every time, and seven of the eight are checkable without opening a screen reader.

### One data point worth carrying

> "Checking for contrast is the most common critical failure across all of our audits (88% of audits failed this heuristic)."

88% is a claim about the authors' own audit practice, not a sampled study, and it is stated as such. It is still the single most useful prior in this wiki for deciding what to check first. [checks/matplotlib.md](../checks/matplotlib.md) already implements the WCAG relative-luminance calculation in about a dozen lines.

## What Chartability adds that this wiki does not have

[inventory.md](../inventory.md) has four accessibility topics: alt text and long description (71), underlying data reachable (72), text baked into raster (73), and screen-reader-legible structure (74). Mapped onto Chartability:

| Inventory topic | Chartability |
|---|---|
| 71, alt text | 2 (Content is only visual), 18 (No title, summary, or caption), 39 (Visually apparent features not described) |
| 72, underlying data | 30 (No table), 40 (Data in text is not human-readable) |
| 73, text in raster | 2, partially |
| 74, screen-reader structure | 27, 28 (Robust), 34 (navigable by structure) |

Plus contrast (topic 33) and CVD (topic 26), which the inventory files under Color rather than Accessibility. Call it **six of fifty**, generously counted, against the README's estimate of three. Either way the conclusion holds.

The heuristics with no inventory counterpart at all, and which a general figure bar plausibly owes:

- **Small text size with an absolute floor** (9pt/12px). Inventory topic 16 says text is probably too small; Chartability gives a number and a rationale for why the number is a floor rather than a target.
- **Reading level of the text you wrote.** Grade 9 or lower, tool-checkable. Nothing else in this corpus mentions it.
- **Adjacent elements need 1px of separation.** A specific, mechanizable rule about touching stacked bars and pie slices.
- **User style changes must be respected**, including OS high-contrast modes. The workbook's Figure 8 shows a categorical bar chart against Windows High Contrast White Mode. A figure with hard-coded colors and no adaptation fails this by construction, and it is a **critical**. This is inventory topic 81 (background and dark-mode assumption) with real teeth.
- **Zoom and reflow, and user text adjustments.** A figure with baked-in text does not reflow. Ever.
- **Difficult chart types need an alternative.** Not "avoid pie charts", but "if you use one, provide a path to the same analytical task another way."
- **Statistical uncertainty must carry a textual explanation**, which is stronger than inventory topic 49's "state the kind on the figure": Chartability wants prose, not a legend abbreviation.
- **Data density as an accessibility failure.** The inventory covers overplotting under Density (topics 58 to 61) as a perceptual concern. Chartability makes it critical and cognitive, and its remedy list is aggregate, split, or explain the pattern. Note the workbook's own honesty here: "we couldn't find any research on this from a cognitive or perceptual perspective."

## The license, and how it interacts with an MIT repo

**The facts.** From the home page and the workbook, identically worded:

> "Chartability was created by Frank Elavsky and is licensed under the CC-BY-SA (Creative Commons Attribution-ShareAlike 3.0 Unported) license."

The canonical source is the `Chartability/POUR-CAF` GitHub repository. A Word version of the workbook is offered for download, which is a deliberate affordance for people keeping audit records.

**The shape of the obligation.** CC BY-SA 3.0 requires attribution, and ShareAlike requires that **adaptations** be licensed under the same or a compatible license. This repo is MIT. MIT and CC BY-SA are not the same license and one does not absorb the other, so a straight copy of the heuristic text into an MIT-licensed file is not clean.

**Three routes, in order of increasing obligation.**

1. **Cite and link.** Reference the heuristics by name, link to the workbook, quote sparingly with attribution. Ideas, facts, and a taxonomy's structure are not what copyright protects; the expression is. This page itself is that route. No ShareAlike trigger, and it is enough for a bar that says "run the Chartability shortlist" and points at it. **The weakness is that it does not survive offline**, and a checklist you have to leave the repo to read is a checklist that does not get run.

2. **Vendor the workbook text into a separately licensed file.** Copy the heuristics verbatim (or adapt them) into something like `wiki/sources/chartability-heuristics.md`, put a CC BY-SA 3.0 notice and the attribution to Frank Elavsky at the top of that file, and note the exception in the repo's `LICENSE` and `README`. Per-file licensing inside an otherwise-MIT repo is ordinary practice, and it is the honest way to carry copyleft text. The cost is that the file cannot be relicensed later and downstream users inherit the condition on that file.

3. **Write original checks against the heuristic names.** Implement the mechanizable subset in code (contrast, text size, 1px separation, CVD simulation, reading level), attribute the framework, and do not copy the descriptions. The code is your expression and can be MIT. This is how [checks/matplotlib.md](../checks/matplotlib.md) is already structured, and the contrast check there is already a Chartability heuristic in everything but name.

**The recommendation is 3 for the code and 2 for the text**, if the text is wanted verbatim. Route 1 alone under-delivers on the "importing beats deriving" conclusion, because it imports the pointer rather than the content.

Two caveats, stated rather than buried. This is a reading of a license notice, **not legal advice**, and the interaction of CC BY-SA 3.0 Unported with later versions and with other copyleft licenses has details that matter and are not settled here. Anyone doing route 2 should check the actual deed. Separately, the source **wants** to be adopted:

> "we highly recommend that every data visualization practitioner (at the bare minimum) learns to use Chartability as they design and engineer."

along with an invitation to contribute through the GitHub repository and its discussions. The friction here is license mechanics, not permission.

## What adopting it would actually involve

Concretely, and in order:

1. **Decide the scope split.** Chartability covers static figures, interactive charts, and full data interfaces. A figure bar for a plotting library binds on maybe 20 of the 50. Publish the split, since it does not exist upstream and it is the main thing that makes the framework usable here.
2. **Adopt the 14-critical shortlist as the accessibility floor,** annotated with which **8** apply to a static figure, the list given above. This is a floor-level obligation, not a ceiling-level one: it should bind on a throwaway diagnostic plot as much as on a docs figure.
3. **Retire the four derived accessibility topics** (71 to 74) in favor of the mapping above, and move contrast (33) and CVD (26) so they read as accessibility rather than as color. Keep the inventory numbering stable and record the substitution, so the derivation history stays legible.
4. **Implement the mechanizable subset.** Contrast, minimum text size, adjacent-element separation, CVD simulation, and reading level are all cheap. Contrast already exists in the checks file. Text size is one `Text.get_fontsize()` sweep. Reading level needs a syllable counter and nothing else.
5. **Carry the negative framing through.** Report failures against a scale and require that each one be argued rather than silently accepted. Do not convert the heuristics into a pass list.
6. **Attribute in the skill, not just in the wiki.** If the shortlist ships inside the skill file, the attribution and license notice ship with it.

The honest cost estimate: steps 1 through 3 are an afternoon of judgment. Step 4 is a day. Step 5 is a design decision that affects how every rule in the bar is worded, and it is the one worth arguing about before starting.

## Where this source is used

Nowhere yet. It is listed under "Sources deliberately not consulted" in [roll-call.md](../roll-call.md), discovered after the accessibility topics were derived, and flagged in the wiki README as the standing import-rather-than-derive recommendation. This page is the first pass at the primary.

## Links

- [Chartability](https://chartability.fizz.studio/)
- [The Chartability Workbook (POUR+CAF)](https://chartability.github.io/POUR-CAF/)
- [Chartability/POUR-CAF on GitHub](https://github.com/Chartability/POUR-CAF)
- [Workbook, Microsoft Word version](https://chartability.github.io/POUR-CAF/Chartability_Worksheet_V2.docx)
- [CC BY-SA 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/)
- [DatavizA11y resources](https://github.com/dataviza11y/resources)
- Related: [w3c-wai-complex-images.md](w3c-wai-complex-images.md), [urban-institute.md](urban-institute.md), [datawrapper-academy.md](datawrapper-academy.md)
