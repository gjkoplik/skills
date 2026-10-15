---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Tamara Munzner

**What they are known for.** *Visualization Analysis and Design*, the framework textbook that splits any design into *what* data there is, *why* the user is looking, and *how* it is encoded, and the source of the marks-and-channels vocabulary most courses teach. Her nested four-level model is the field's standard answer to "what kind of evaluation does this contribution need."

**How this was read.** `primary-read` for the nested-model paper and its 2013 revision, downloaded from UBC and extracted locally with `pdftotext`. All quotes are from them. `secondary-only` for the book, as set out at [sources/munzner-vad.md](../sources/munzner-vad.md).

**What they are good for.** What a figure is for, and whether the most important attribute sits on the most accurate channel. She organizes task and data abstraction, marks and channels, networks and trees, and interaction and reduction as design decisions. She also says which kind of evidence a design claim needs.

**What they do not settle.** Perceptual mechanism, left out on purpose. Titles, captions, annotation, source lines, number formats, narrative. Accessibility past "get it right in black and white." Production and reproducibility. And **she did not measure the channel ranking**, though she is often cited as if she had.

---

## What their work established

### The framework is definitional

The what/why/how decomposition and the marks-and-channels vocabulary are definitional. They assert nothing that could turn out false, so under [concepts/evidence-class.md](../concepts/evidence-class.md) they carry no evidence label. Their use is that they force a question order.

### The nested model

The 2009 paper has four nested levels: domain problem and data, abstraction into operations and data types, encoding and interaction, and algorithm.

> "The output from a level above is input to the level below, bringing attention to the design challenge that an upstream error inevitably cascades to all downstream levels."

Each level has its own threat to validity and its own kind of evaluation, and outer-level threats mostly cannot be validated until the inner levels exist. She states the cost herself:

> "A clear limitation of this model is that it errs on the side of oversimplifying the situation. This choice was deliberate, as the goal of providing very clear guidance took priority over that of presenting a more subtle and sophisticated discussion. Many nuances of evaluation methodology are glossed over here. Moreover, the reductionist assumption that complex sensemaking tasks can be broken down into low-level components is unlikely to be completely true."

and

> "This model is by no means the only way to approach the design and development process."

### The boundary between design and capability

From the 2009 paper's limitations:

> "We also deliberately leave out some kinds of user studies from our discussion, such as the psychophysical style of characterizing human perceptual and cognitive capabilities, because their intent is not to validate a particular design or application."

Her frame validates *designs*. [Ware's](colin-ware.md) and [Cleveland's](william-cleveland.md) validate *capabilities*, so citing Munzner for a perceptual claim crosses her own line.

### She revised the model

The 2009 model was revisited at BELIV 2012 and extended into the **nested blocks and guidelines model** (Meyer, Sedlmair, Quinan & Munzner, 2013), because the original could not record *why* a design decision was made:

> "The NBGM extends the previously proposed four-level nested model by adding finer grained structure within each level, providing explicit mechanisms to capture and discuss design decision rationale."

Most citations are still to the 2009 version.

### Where her name is used for more than she showed

**The channel-effectiveness ranking.** [inventory.md](../inventory.md) topic 6 calls it "evidence-backed via the Cleveland-McGill lineage" and cites Munzner ch. 5. The class is right, but the citation is a `secondary-only` textbook restating a 1984 and a 1985 result by authors who called their own ordering "partly conjectural." The evidence is [cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) and [heer-bostock-2010.md](../studies/heer-bostock-2010.md), which her slides cite.

**The rules of thumb.** Eight, per the section-level table of contents extracted on [munzner-vad.md](../sources/munzner-vad.md), all authority-asserted. "No Unjustified 3D" has perceptual arguments in her slides and no controlled study attached in this reading. "Responsiveness Is Required" uses 0.1 second, 1 second and 10 seconds, which are the classic HCI latency thresholds, not her measurements. "Get It Right in Black and White" is Maureen Stone's phrase, as her slides say.

**Topic 7's quote is unverified.** [sources/munzner-vad.md](../sources/munzner-vad.md) records that the sentence attributed to her about expressing "all of, and only, the information in the dataset attributes" is not in her 689-slide deck. It may be in chapter 5, which has not been opened.

**Design study methodology.** *Design Study Methodology* (2012, with Sedlmair and Meyer) is a process framework drawn from prior design studies, unread here. Citing it as evidence that a process works is the same category error.

---

## What they would object to in a figure

*Reconstruction from her stated priorities, not a response to any actual figure.*

She would ask for the task in abstract terms and the data in type terms before looking, since without them no polish helps. Then whether the most important attribute is on the most accurate channel or landed on color because color was left over. Then 3D for data that is not spatially 3D, a sequential ramp on a categorical column, and panels held in memory that could sit side by side. Beauty comes last. Her distinctive objection is not "this is drawn badly." It is "this is a well-drawn answer to a question nobody asked," an upstream error.

---

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| *Visualization Analysis and Design* (A K Peters / CRC, 2014) | `secondary-only`. Publisher section-level TOC plus her own slide deck. | [sources/munzner-vad.md](../sources/munzner-vad.md). Grounds many inventory topics; see [roll-call.md](../roll-call.md). |
| Munzner (2009), "A Nested Model for Visualization Design and Validation," *IEEE TVCG* 15(6) | `primary-read`. [cs.ubc.ca](https://www.cs.ubc.ca/labs/imager/tr/2009/NestedModel/NestedModel.pdf), extracted locally. | No page. The book's chapter 4, which summarizes it, is a stated exclusion from the inventory. |
| Meyer, Sedlmair, Quinan & Munzner (2013), "The Nested Blocks and Guidelines Model" | `primary-read`. [cs.ubc.ca](https://www.cs.ubc.ca/labs/imager/tr/2013/NBGM/nbgm.pdf), extracted locally. | No page. The revision of the model above. |
| Sedlmair, Meyer & Munzner (2012), "Design Study Methodology: Reflections from the Trenches and the Stacks," *IEEE TVCG* 18(12) | Reachable, not read: [cs.ubc.ca](https://www.cs.ubc.ca/labs/imager/tr/2012/dsm/dsm.pdf) | No page. Out of scope for a figure bar, in scope for a process around one. |
| Munzner (2008), "Process and Pitfalls in Writing Information Visualization Research Papers" | Reachable, not read: [cs.ubc.ca](https://www.cs.ubc.ca/labs/imager/tr/2008/pitfalls/pitfalls.pdf) | No page. The flat list of evaluation methods whose inadequacy prompted the nested model. |
| Brehmer & Munzner (2013), "A Multi-Level Typology of Abstract Visualization Tasks," *IEEE TVCG* | Reachable, not read: [cs.ubc.ca](https://www.cs.ubc.ca/labs/imager/tr/2013/MultiLevelTaskTypology/brehmer_infovis13.pdf) | No page. The research behind the book's chapter 3, which [inventory.md](../inventory.md) topic 1 cites. |
| "A Taxonomy of Visual Cluster Separation Factors" (2012) and "Empirical Guidance on Scatterplot and Dimension Reduction Technique Choices" (2013), both co-authored | Reachable, not read. Listed on her papers page with local PDFs. | No page. Experimental work: she does run experiments, but they are not what she is cited for. |

Her full publication list, with local PDFs for most entries, is at [cs.ubc.ca/~tmm/papers.html](https://www.cs.ubc.ca/~tmm/papers.html).

## See also

- [sources/munzner-vad.md](../sources/munzner-vad.md): the book's page, including the missing "No Unjustified 2D" rule and the unverified topic-7 quote
- [concepts/channels.md](../concepts/channels.md): what the ranking she presents rests on
- [william-cleveland.md](william-cleveland.md): the measurements behind chapter 5
- [colin-ware.md](colin-ware.md): the perceptual layer she leaves out
- [concepts/evidence-class.md](../concepts/evidence-class.md): why "definitional," "authority-asserted" and "evidence-backed" stay separate
