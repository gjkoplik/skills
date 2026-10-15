---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Ware, Stone & Szafir 2023: Rainbow Colormaps Are Not All Bad

Colin Ware (University of New Hampshire), Maureen Stone (Tableau Research), Danielle Albers Szafir (UNC Chapel Hill). *IEEE Computer Graphics and Applications* 43(3), 88-93, May/June 2023. DOI [10.1109/MCG.2023.3246111](https://doi.org/10.1109/MCG.2023.3246111). Open access, CC-BY.

This is not a study. It is a six-page Visualization Viewpoints department article, an argued position piece replying to Borland & Taylor's 2007 *Rainbow Color Map (Still) Considered Harmful* in the same department. It has no experiment, participants, data or statistics of its own. Every empirical claim in it cites someone else's work. The common misuse is citing it as an experiment that vindicated rainbows.

**What it is good for.**

- Showing that three researchers who each argued against rainbows now think the blanket prohibition overreaches: "each of the authors of this article have written past articles discouraging the use of rainbow colormaps."
- A clear account of which rainbow properties cause the problem (nonmonotonic luminance, perceptual nonuniformity, hue banding) and which designs address which.
- A pointer to the primary empirical literature, tabled below.
- The technical claim that feature resolving power tracks the gradient of CIE L\*, which is a usable design heuristic.

**What it does not settle.** Anything empirical, on its own. It argues how to read other people's evidence.

**How this was read.** Extracted locally with `pdftotext` from the IEEE open-access PDF, with CC-BY confirmed on the article's first page.

## The argument

The abstract:

> "Subsequent articles often repeat and extend these arguments, so much so that avoiding rainbow colormaps, along with their derivatives, has become dogma in the visualization community. Despite this loud and persistent recommendation, scientists continue to use rainbow colormaps. Have we failed to communicate our message, or do rainbow colormaps offer advantages that have not been fully appreciated? We argue that rainbow colormaps have properties that are underappreciated by existing design conventions... Choosing a colormap is a complex task, and rainbow colormaps can be useful for selected applications."

They answer the three standard arguments against rainbows in turn.

**Nonmonotonic luminance.** The apple-and-portrait demonstration used to condemn rainbows relies on shape-from-shading, which most data visualizations do not: "Losing the ability to perceive shape-from-shading in rainbows is not relevant when shape-from-shading perception is not required."

**Perceptual nonuniformity.** Real, and unfixable for classic RGB-interpolated rainbows: "Because they are simple interpolations in RGB (a perceptually nonlinear colorspace), these rainbows inevitably perform poorly on any test of perceived metric distance between displayed quantities." Feature resolving power is driven mostly by luminance gradient, so a diverging-luminance rainbow (Turbo, Paraview's Uniform) fixes the part that matters for detection.

**Hue banding.** Conceded, then argued as a tool: "people tend to read meaning into color categories even when they are simply artifacts of the colormap. Critics of the rainbow colormap rightfully worry about this problem." The fix is to align the breaks with the data: "Meaningful segmentation requires controlling the function that maps data to colors to intentionally align data semantics with perceived bins."

The conclusion:

> "While poorly designed rainbow colormaps can correspond to poor data visualizations, we believe well-designed rainbows, like well-designed multi-hued colormaps, can be valuable tools for visualization."

On how the field spends its experiments:

> "We would like to see these well-designed rainbows used more often in evaluative studies, especially for tasks where luminance and uniformity are known to be important. It is unclear what value we gain by continuing to rediscover that classic rainbows do poorly."

## Method and sample size

None. No experiment was run, so sample size is not applicable. The evidence is in the sources cited:

| Claim | Source cited |
|---|---|
| Rainbows most accurate for reading a value from a key | Ware 1988, *IEEE CG&A* 8(5) |
| Color nameability predicts inference accuracy | Reda, Salvi, Gray & Papka 2021, CGF 40(3) |
| Rainbows outperform grayscale for comparing distributions | Reda & Szafir 2021, TVCG 27(2) |
| Feature detection depends mostly on luminance | Ware, Turton, Bujack, Samsel, Shrivastava & Rogers 2019, TVCG 25(9) |
| Well-designed multihue maps beat single-hue sequential and diverging | Liu & Heer 2018, CHI |
| Rainbow use declining in vis research but not in domain science | Gołębiowska & Çöltekin 2022, ISPRS J. |

## Limits the authors state themselves

> "The critiques levied against rainbows are valid, especially for the original 'rainbow': a simple interpolation of the display primary colors in many early visualization systems. Furthermore, full rainbow maps are very difficult to make accessible, especially to those with severe colorblindness."

> "Classic rainbows have poor perceptual properties with respect to perceptual uniformity and lack a linear, or even a predictably varying, luminance profile."

On adding luminance waves to boost resolving power:

> "However, the tradeoffs of this design choice are not yet well understood."

On the cognitive-grouping argument, which their own verbs mark as unsettled:

> "Preliminary studies suggest that the nameability of color regions may support such reasoning processes. We speculate that this grouping may simplify the data to allow people to more effectively complete tasks involving large subsets of the data... Further research is needed to fully understand how the visual system simultaneously processes hue and luminance variation in colormaps to support a range of tasks."

On why people prefer rainbows, which they leave unexplained:

> "people often prefer these colormaps to best practice nonrainbow colormaps, either because they are familiar or because they provide value that we have yet to clearly identify."

On accessibility:

> "Accessibility is a more difficult problem to solve for rainbows... We believe there is much more to learn about creating and evaluating accessible rainbows."

And the close:

> "We still have much to understand about how people perceive and use rainbows in practice, especially in discovering the tasks and contexts where they excel."

## What this result does not license

- **Not "a study found rainbows are fine."** There is no study and no data of its own. Cited as empirical support, it is an opinion column.
- **Not a defense of jet or the classic HSV rainbow.** Those "inevitably perform poorly on any test of perceived metric distance." The defense is of purpose-built rainbows: Turbo, Paraview's Uniform, the thermal-imaging rainbow, the Tableau density rainbow in Figure 7.
- **Not "rainbows are accessible."** The paper says the opposite twice. Its narrow exception is a colormap that carries its information in luminance, accessible "as long as the information provided by color segmentation is not essential."
- **Not a default for continuous quantitative data.** The use cases named are specific: reading a value off a key, surfacing iso-value contours and extrema, and global-structure or distribution-comparison tasks. The accuracy-for-details argument runs through luminance, not hue.
- **Not evidence that hue banding aids reasoning.** The authors' words are "preliminary studies suggest," "we speculate," and "further research is needed."
- **Not a refutation of Borland & Taylor 2007.** It rebuts the dogma that grew around that paper and concedes the original critiques hold for the original rainbow.

## Links

- IEEE open access PDF: [ieeexplore.ieee.org/document/10128890](https://ieeexplore.ieee.org/document/10128890)
- The article it replies to: Borland & Taylor, *Rainbow Color Map (Still) Considered Harmful*, IEEE CG&A 27(2), 2007
- Robert Kosara's summary: [eagereyes.org/blog/2023/rainbow-colormaps-are-not-all-bad-paper](https://eagereyes.org/blog/2023/rainbow-colormaps-are-not-all-bad-paper)
- [inventory.md](../inventory.md), topic 25 (rainbow / jet / turbo)
