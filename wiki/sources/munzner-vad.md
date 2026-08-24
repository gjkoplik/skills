# Munzner, *Visualization Analysis and Design*

**What it is.** Tamara Munzner, *Visualization Analysis and Design* (A K Peters / CRC Press, 2014, 428 pp). A framework book rather than a chart cookbook: it decomposes every design into *what* data you have, *why* the user is looking, and *how* the encoding and interaction are built. Companion site at [cs.ubc.ca/~tmm/vadbook](https://www.cs.ubc.ca/~tmm/vadbook/).

**Status: `secondary-only`.** The book is not free and was not read. Retrieved 2026-08-23:

1. the publisher's **section-level** table of contents (routledge.com product page, fetched with `curl` and stripped locally), which is the book's own outline rather than a third-party reconstruction;
2. **Munzner's own 689-slide deck** covering the entire book (`vadallslides-2021.pdf`, 68 MB, from her companion site), downloaded and text-extracted locally with `pypdf`;
3. the companion site itself.

Every quote below is **from the slides, not the book**. They are the author's own words on the same material, which is a stronger secondary than a review or a summary, and it is still not the book's sentences. Do not present them as quotations from *Visualization Analysis and Design*.

This is an upgrade on the previous state, which had chapter names from two third-party decks and no rule text at all.

**What it is good for.** Come back here with: *what is this figure for, what is the data actually made of, and is the most important attribute on the most accurate channel*. Munzner is also the only canon source with serious coverage of **networks and trees** (node-link versus matrix as a size-dependent choice), **interaction** as an encoding decision rather than a feature, and **reduction** (filter, aggregate) as a legitimate design move.

**What it does not settle.** Nothing on titles, captions, annotation, source lines, number formatting, locale, or narrative. No accessibility beyond "get it right in black and white". No production or reproducibility. The four-levels validation framework in chapter 4 is research methodology and is deliberately excluded from the inventory, not overlooked.

---

## Structure

Fifteen chapters. From the publisher's own listing:

1. What's Vis, and Why Do It?
2. What: Data Abstraction
3. Why: Task Abstraction
4. Analysis: Four Levels for Validation
5. Marks and Channels
6. Rules of Thumb
7. Arrange Tables
8. Arrange Spatial Data
9. Arrange Networks and Trees
10. Map Color and Other Channels
11. Manipulate View
12. Facet into Multiple Views
13. Reduce Items and Attributes
14. Embed: Focus+Context
15. Analysis Case Studies

## Chapter 6, the rules of thumb, from the publisher's section list

This is the chapter a figure bar borrows from, and the section-level TOC names **nine** rules, not eight:

- No Unjustified 3D
- **No Unjustified 2D**
- Eyes Beat Memory
- Resolution over Immersion
- Overview First, Zoom and Filter, Details on Demand
- Responsiveness Is Required
- Get It Right in Black and White
- Function First, Form Next

(plus "Why and When to Follow Rules of Thumb?" and "The Big Picture" as the framing sections)

[roll-call.md](../roll-call.md) lists this chapter's rules and omits **No Unjustified 2D**, which is about not forcing network data into a spatial layout when a text list would read better. It is the rule most directly relevant to graph visualization, so the omission matters more than its size suggests.

## What the slides actually say

On channel choice, the compact statement of both principles:

> expressiveness: match channel type to data type
> effectiveness: some channels are better than others

The effectiveness ranking as the slides present it, magnitude channels in order: position on common scale, position on unaligned scale, length (1D size), tilt/angle, area (2D size), depth (3D position), color luminance, color saturation, curvature, volume (3D size). Identity channels: spatial region, color hue, motion, shape.

On 3D:

> 3D legitimate for true 3D spatial data. 3D needs very careful justification for abstract data. Enthusiasm in 1990s, but now skepticism. Be especially careful with 3D for point clouds or networks.

with the mechanism named rather than asserted: occlusion hides information, perspective distortion "interferes with all size channel encodings", and tilted text is far less legible.

On function first:

> dangerous to start with aesthetics. Usually impossible to add function retroactively.

On responsiveness, which is the only quantitative rule in the chapter:

> 0.1 seconds: perceptual processing. Subsecond response for mouseover highlighting.
> 1 second: immediate response. Fast response after mouseclick, button press.
> 10 seconds: brief tasks. Bounded response after dialog box.

A provenance detail the wiki did not have: **"Get It Right in Black and White" is Maureen Stone's phrase**, not Munzner's. Her slides cite Stone's 2010 post of that title directly.

## Not confirmed

Inventory topic 7 carries this, attributed to Munzner:

> "the visual encoding should express all of, and only, the information in the dataset attributes"

That sentence does not appear anywhere in the 689-slide deck. The slides state expressiveness as "match channel type to data type". The quoted sentence may well be in the book, which was not read. Treat it as unvouched until someone opens chapter 5.

## Where its advice is contested

Two places worth naming, neither of them a refutation:

- **The channel-effectiveness ranking** is the one part of Munzner with a real experimental lineage behind it (Cleveland and McGill onward), and the inventory labels it evidence-backed for that reason. The ranking's *ordering* is better supported than any single gap between adjacent channels.
- **Aspect ratio** does not appear in Munzner at all, and the banking-to-45-degrees result it would have rested on is scope-limited. See [refutations.md](../refutations.md).

The rules of thumb themselves are authority-asserted. "No Unjustified 3D" has supporting perceptual arguments in the slides; it does not have a controlled study attached in this project's reading.

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md), do not recompute: 1, 2, 4, 5, 6, 7, 21, 22, 23 through 36, 27, 57, 61, 62, 63, 68, 82, 83, 84, 92.

Chapter 4 is a stated exclusion (research-methodology framework, not mechanizable for a one-off chart). Chapter 15 is a stated exclusion (worked examples).

## What the project got wrong about it

- The rules-of-thumb list in the roll-call is missing **No Unjustified 2D**. Fixed above, from the publisher's own section list.
- The roll-call's caveat said rule names were "confirmed across two independent slide decks (UBC and HKUST)". The publisher's section-level TOC is a better source for the same fact and now supersedes it.
- Topic 7's quote is unvouched (above).

## Links

- [inventory.md](../inventory.md), the topics this source grounds
- [roll-call.md](../roll-call.md), the chapter-by-chapter mapping
- [refutations.md](../refutations.md), aspect ratio, dual axes
- [wilke-fundamentals.md](wilke-fundamentals.md), the complementary source; Wilke covers what Munzner skips (text, annotation, production) and vice versa
