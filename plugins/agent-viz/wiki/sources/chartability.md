---
type: source
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Chartability

A set of 50 accessibility heuristics for data visualizations, organized under seven principles: the four web-accessibility principles (Perceivable, Operable, Understandable, Robust) plus three that extend Robust (Compromising, Assistive, Flexible), abbreviated **POUR+CAF**. Created by Frank Elavsky, published with an academic paper, licensed CC-BY-SA, and built to be adopted.

**What it is good for.** The accessibility inventory this wiki lacks: peer-reviewed, community-tested with disabled reviewers, openly licensed, built for auditing, with a half-hour shortlist. [roll-call.md](../roll-call.md) and the wiki README both recommend importing it rather than re-deriving a fifth of it.

**What it does not settle.** Anything outside accessibility, including chart-type choice, narrative, palette design beyond CVD safety and contrast, and statistical honesty beyond one heuristic on uncertainty. It is not a compliance instrument: "Chartability should never be used in place of a compliance audit but always in tandem with it." About half of it applies only to interactive systems, so a static PNG cannot fail most of Operable, Compromising or Flexible.

**How this was read.** `primary-read` for the heuristics, `not-reached` for the paper. The home page (`chartability.fizz.studio`) and the complete POUR+CAF workbook (`chartability.github.io/POUR-CAF/`) were fetched and converted to text locally. All 50 heuristic titles, the 14 critical flags and the descriptions quoted below come from that text. The EuroVis 2022 paper was not opened. The home page cites it as "Elavsky, F. and Bennett, C. and Moritz, D. How accessible is my visualization? Evaluating visualization accessibility with Chartability. EuroVis 2022."

---

## How the heuristics are framed

Every heuristic is named for the defect ("Low contrast", "Small text size", "No table", "Axis labels are unclear or missing"), and accessibility is a scale, not a state.

> "An important note about language: Chartability's tests are framed in negative language, like 'Target pointer interaction size is too small.' This is intentional. Chartability is not meant to be used to 'pass' accessibility requirements. **You cannot 'pass' Chartability 100%.** Rather, Chartability is simply framed as a tool that helps people catch known barriers, or 'failures.' It is possible to have 0 failures in Chartability but still have accessibility issues."

> "Generally, Chartability approaches accessibility as a scale rather than a state: how accessible a DX is is determined by how few failures it contains. It should be assumed that even the absolute best DX may contain several failures, even after remediation."

> "Chartability's insistence on a scale (instead of a state) of accessibility requires that designers and creators consider their choices carefully: they must be willing to argue that lack of scope, time, or research or perhaps a unique consideration led to a given failure. **No failure should be left unconsidered.**"

Inconclusive tests count as failures: "The auditor should assume failure when tests are inconclusive." Rewording "Low contrast (critical)" as "ensure sufficient contrast" restores the pass/fail model the author rejected.

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

The 14 critical heuristics are the shortlist. From the home page, then the workbook:

> "Chartability is meant to be easy to get started, with a shortlist of 14 tests that can be conducted in 20-40 minutes (depending on the tester's experience). But Chartability's full test suite is also incredibly robust (50 heuristics total) and can integrate well into proper auditing work of complex systems."

> "The following section contains Chartability's 7 principles and 50 heuristics, 14 of which are considered critical. Those new to chartability should try testing just the critical heuristics first, and then move on to all of them."

Criticality is a triage criterion, not a ranking by importance:

> "Some tests are considered critical by members of the community because they are prohibitively expensive to fix, common, produces signficant barriers, and/or affect many aspects of a data experience design or development."

The 20-40 minute figure is for the shortlist. For a full pass, the workbook says a highly trained auditor may manage 30 minutes, "those new to auditing may take anywhere between 2 and 8 hours to complete a full pass", and professional audits "take weeks of work and have between 100 and 200 pages of documented evidence."

### The 14 criticals, sorted by whether they bind on a static figure

This split is this wiki's reading of the workbook, not the source's.

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

A plotting-library figure saved to disk faces eight critical tests, seven of them checkable without a screen reader.

### The contrast failure rate

> "Checking for contrast is the most common critical failure across all of our audits (88% of audits failed this heuristic)."

The 88% comes from the authors' own audits, not a sampled study. [checks/matplotlib.md](../checks/matplotlib.md) implements the WCAG relative-luminance calculation.

## What Chartability adds that this wiki does not have

The four accessibility topics in [inventory.md](../inventory.md) map onto Chartability as follows.

| Inventory topic | Chartability |
|---|---|
| 71, alt text | 2 (Content is only visual), 18 (No title, summary, or caption), 39 (Visually apparent features not described) |
| 72, underlying data | 30 (No table), 40 (Data in text is not human-readable) |
| 73, text in raster | 2, partially |
| 74, screen-reader structure | 27, 28 (Robust), 34 (navigable by structure) |

Contrast (topic 33) and CVD (topic 26), which the inventory files under Color, correspond to heuristics 1 and 7.

Heuristics with no inventory counterpart that a general figure bar plausibly owes:

- **A text-size floor of 9pt/12px.** Inventory topic 16 says only that text is probably too small.
- **Reading level** of figure text, grade 9 or lower and tool-checkable. Nothing else in this corpus mentions it.
- **1px separation** between adjacent elements, such as touching stacked bars and pie slices.
- **Respect for user style changes**, including OS high-contrast modes (the workbook's Figure 8 shows a bar chart under Windows High Contrast White Mode). Hard-coded colors fail this critical heuristic by construction. Inventory topic 81 (background and dark-mode assumption) covers the ground without the requirement.
- **Zoom, reflow and user text adjustments**, which baked-in text cannot honor.
- **An alternative for difficult chart types.** Not "avoid pie charts", but "if you use one, provide a path to the same analytical task another way."
- **A prose explanation of statistical uncertainty**, stronger than inventory topic 49's "state the kind on the figure".
- **Data density as a critical, cognitive failure**, where the inventory treats overplotting (topics 58 to 61) as perceptual. The workbook states its basis: "we couldn't find any research on this from a cognitive or perceptual perspective."

## The license, and how it interacts with an MIT repo

The home page and the workbook word it identically:

> "Chartability was created by Frank Elavsky and is licensed under the CC-BY-SA (Creative Commons Attribution-ShareAlike 3.0 Unported) license."

The canonical source is the `Chartability/POUR-CAF` GitHub repository, which also offers the workbook as a Word file. CC BY-SA 3.0 requires attribution, and ShareAlike requires adaptations to carry the same or a compatible license. This repo is MIT, and neither license absorbs the other, so copying the heuristic text into an MIT-licensed file is not clean. The routes, in order of increasing obligation:

1. **Cite and link.** Copyright protects expression, not ideas, facts or a taxonomy's structure, so naming the heuristics with sparing, attributed quotation triggers no ShareAlike. This page does that. It imports a pointer, not the content, and does not work offline.
2. **Vendor the text into a separately licensed file**, such as `wiki/sources/chartability-heuristics.md`, with a CC BY-SA 3.0 notice and attribution to Frank Elavsky at its top, and the exception noted in the repo's `LICENSE` and `README`. Per-file licensing is ordinary practice. The file cannot be relicensed later, and downstream users inherit the condition.
3. **Write original checks against the heuristic names.** Code for the mechanizable subset, with the framework attributed and the descriptions not copied, is original expression and can be MIT. [checks/matplotlib.md](../checks/matplotlib.md) is built this way, and its contrast check is heuristic 1 in all but name.

This is a reading of a license notice, not legal advice. How CC BY-SA 3.0 Unported interacts with later versions and other copyleft licenses is not settled here, and the deed governs route 2. The source invites adoption, and contributions through its GitHub repository:

> "we highly recommend that every data visualization practitioner (at the bare minimum) learns to use Chartability as they design and engineer."

## What adopting it would involve

1. **A scope split** between static figures, interactive charts and full data interfaces, which upstream lacks. A plotting-library figure bar binds on maybe 20 of the 50 heuristics.
2. **The 14-critical shortlist as the accessibility floor**, annotated with the **8** that bind on a static figure, including a throwaway diagnostic plot.
3. **Inventory topics 71 to 74 retired** in favor of the mapping above, with contrast (33) and CVD (26) moved under accessibility. Numbering stays stable and the substitution is recorded.
4. **The mechanizable subset**: contrast (already in the checks file), text size (one `Text.get_fontsize()` sweep), adjacent-element separation, CVD simulation, and reading level (a syllable counter).
5. **The negative framing kept**: failures reported against a scale, each one argued, no pass list.
6. **Attribution and license notice in the skill file** if the shortlist ships there.

Steps 1 through 3 are an afternoon of judgment and step 4 is a day. Step 5 changes how every rule in the bar is worded.

## Where this source is used

No inventory topic cites it yet. [roll-call.md](../roll-call.md) lists it under "Sources deliberately not consulted", since it was found after the accessibility topics were derived.

## Links

- [Chartability](https://chartability.fizz.studio/)
- [The Chartability Workbook (POUR+CAF)](https://chartability.github.io/POUR-CAF/)
- [Chartability/POUR-CAF on GitHub](https://github.com/Chartability/POUR-CAF)
- [Workbook, Microsoft Word version](https://chartability.github.io/POUR-CAF/Chartability_Worksheet_V2.docx)
- [CC BY-SA 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/)
- [DatavizA11y resources](https://github.com/dataviza11y/resources)
- Related: [w3c-wai-complex-images.md](w3c-wai-complex-images.md), [urban-institute.md](urban-institute.md), [datawrapper-academy.md](datawrapper-academy.md)
