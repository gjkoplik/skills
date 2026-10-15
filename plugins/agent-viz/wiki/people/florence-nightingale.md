---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Florence Nightingale

**What they are known for.** The polar-area diagram of Crimean War mortality, showing that far more British soldiers died of preventable disease than of wounds, and that the death rate collapsed after the Sanitary Commission arrived.

**How this was read.** `primary-read` for the book and both plates, `secondary-only` for the archival history.

- ***Notes on Matters Affecting the Health, Efficiency, and Hospital Administration of the British Army* (1858)**, her privately printed report: full-text OCR from the Internet Archive (`b20387118`, 2.2 MB), read locally. Public domain.
- Both plates, downloaded at full resolution and examined: the wedges (`dr_diagram-of-the-causes-of-mortality-in-the-army-in-the-east-10563002`, 1536x880) and the rejected "bat's wing" (`dr_diagrams-representing-the-relative-mortality-from-zymotic-diseases-blue-10564004`, 1477x1536). Every visual claim below comes from those files.
- Letters, print runs and naming history: Hugh Small's 1998 conference paper, fetched with `curl` from York's history-of-statistics pages and extracted locally, <https://www.york.ac.uk/depts/maths/histstat/small.htm>. The British Library manuscripts he cites were not seen here.

**What they are good for.** The canonical case of designing backward from the decision: *this figure has to change one decision, made by named people, this quarter*. The failed first version survives, so she is also a case of one author getting the encoding wrong and fixing it in public.

**What they do not settle.** Whether it worked. Nothing here establishes that the diagrams moved policy, and Small, who has read the archives, says so.

---

## "In the style of Nightingale" means, concretely

From the wedges plate:

- **Two panels on one area scale, the good news on the left.** Panel `1.` (April 1854 to March 1855) sits on the right. Panel `2.` (April 1855 to March 1856, after the sanitary works) sits on the left, a fraction of the size, tied to the first by a dashed leader line.
- **Twelve equal-angle sectors, one per month.** Radius varies and area is the quantity, as the caption opens: *"The Areas of the blue, red, & black wedges are each measured from the centre as the common vertex."*
- **Three causes overlaid from a common center, not stacked.** Blue is preventable zymotic disease, red is wounds, black is all other causes. Blue swamps everything.
- **Palette.** Desaturated slate blue for the dominant quantity, pale pink-red, gray-black, thin black outlines, wash fills, cream paper. Red is the small category, not an alarm.
- **No axes, gridlines, radial scale or numbers on the wedges.**
- **An italic caption that names the ambiguities**: *"In October 1854, & April 1855, the black area coincides with the red; in January & February 1856, the blue coincides with the black."*
- **Month labels set radially** in small caps, half upside down, under an engraved title.
- **One chart, one decision.** No exploratory version exists. It was made to put disease above wounds on a single sheet for ministers.

## What they established, and what gets over-claimed in their name

### She did not invent the polar-area diagram

Playfair's pie predates her by half a century. Most graphic forms in her Crimean documents come from **William Farr**, her adviser at the General Register Office, whose reports already used what Small calls "100% area" and stacked-bar constructions. Small's claim for the two roses is hedged:

> "This 'bat's wing' and its successor are so different from any diagrams that Farr did before that they may be Nightingale's own invention."

### "Coxcomb" named a booklet, not a diagram

She used the word for the 2,000 privately printed copies of *Mortality of the British Army*. Her Christmas Day 1857 letter to Sidney Herbert (BL Add. MSS 43394 f210, quoted by Small) itemizes the run: *"I send you one of the 'coxcombs' There are 300 of these / 1700 of the vulgar sort / 2000."* That booklet, printed at the start of 1858, carried the bat's wing. The wedges did not exist until late that year. Cook's 1914 biography moved the word to the diagram with "Miss Nightingale's 'coxcomb' diagrams". The usage is settled. Its origin story is folklore.

### The first version was wrong

The bat's wing has circular gridlines and a numeric radial scale (100, 200, 300 and up). Its radius is proportional to the death rate, so area grows as the square while text and shape imply area is the quantity. Small found this and the plate corroborates it. The plate's note says that at the common scale *"the longest Radius, showing the Mortality in February, would have projected 40 inches from the Centre of the Circle."*

Small records that she recognized the error, inserted an erratum slip, and replaced the diagram in three later documents. The famous chart is a correction. Fixing the encoding cost the radial scale, so the corrected chart is sound and unreadable as numbers. The numbers live in the tables.

### "The chart convinced Parliament" is not established

The 1858 volume opens with a War Office letter from Lord Panmure, dated 18 February 1857, asking her for the report: a solicited report to a government already listening. Small argues the more influential diagram was probably the "Lines" bar chart of peacetime death rates in English barracks against nearby civilians, because it described something still happening. His closing question, which he calls the most important and unanswered:

> "did she achieve real success with these arguments, in terms of reducing the mortality of the population as a whole?"

### The argument is in the tables

The 1858 text: of 48,742 sick, 36,179 were zymotic preventable cases, about three quarters of all disease in the army. Of 5,359 deaths, 373 were from wounds. Of the 4,986 from disease, 4,465 were zymotic, leaving 521, so of deaths from disease *"nearly 90 per cent. died from preventible causes alone."* Average army strength was 28,623. The tables establish this. The chart is the part people look at.

### What the form costs

Area, which [Cleveland & McGill](../studies/cleveland-mcgill-1984.md) rank below position, length and angle. Equal angles make each wedge look like a share of a whole when it is not. [Skau & Kosara](../studies/skau-kosara-2016.md) found angle the *worst* of a pie's three cues ([pie-and-donut.md](../chart-types/pie-and-donut.md)), so holding angle constant and varying radius is not obviously the wrong trade. The overlay costs more: where black exceeds blue, the visible blue is not the blue quantity. Her caption names those months. Most modern polar-area charts do not.

## Works, and where they sit in this wiki

- ***Notes on Matters*** (1858). **No source page.** Read in full text.
- ***Mortality of the British Army*** (1858), the "coxcomb" booklet. **Not reached.** It carries the bat's wing and is the object the word refers to, so any account of the naming rests on it.
- ***A Contribution to the Sanitary History of the British Army*** (1859), the anonymous reply to a pamphlet accusing her of exaggerating, and the first appearance of the corrected wedges. **Not reached.**
- ***Notes on Nursing*** (1860). On the Internet Archive, out of scope.

## Links

- [william-playfair.md](william-playfair.md): who got there first
- [edward-tufte.md](edward-tufte.md): the Minard comparison Small uses to place her, and Small's note that Tufte's first book omits her
- [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md): the angle evidence that complicates the standard criticism of her chart
- [concepts/channels.md](../concepts/channels.md): where area sits
- [refutations.md](../refutations.md): other cases where "the received story changed when someone opened the source"
