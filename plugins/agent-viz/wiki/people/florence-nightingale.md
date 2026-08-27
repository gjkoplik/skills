---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Florence Nightingale

**What they are known for.** The polar-area diagram of Crimean War mortality, showing that far more British soldiers died of preventable disease than of wounds, and that the death rate collapsed after the Sanitary Commission arrived. It is the canonical example of a chart built to force one specific decision.

**How this was read.** `primary-read` for the book and both plates, `secondary-only` for the archival history. Retrieved 2026-08-23.

- ***Notes on Matters Affecting the Health, Efficiency, and Hospital Administration of the British Army* (1858)**, her privately printed report, was pulled as full text from the Internet Archive (`b20387118`, 2.2 MB of OCR) and read locally. Public domain.
- **Both diagrams were downloaded at full resolution and examined**, not described from memory: the wedges plate (`dr_diagram-of-the-causes-of-mortality-in-the-army-in-the-east-10563002`, 1536x880) and its rejected predecessor, the "bat's wing" (`dr_diagrams-representing-the-relative-mortality-from-zymotic-diseases-blue-10564004`, 1477x1536). Every visual claim below comes from looking at those files.
- **The letters, the print runs, and the naming history are from Hugh Small's 1998 conference paper**, hosted on York's history-of-statistics pages, fetched with `curl` and extracted locally rather than summarized: <https://www.york.ac.uk/depts/maths/histstat/small.htm>. He cites British Library manuscripts I have not seen. Treat those as reported.

**What they are good for.** Come back here with: *this figure has to change one decision, made by named people, this quarter*. Nightingale is the strongest case in the canon for designing backward from the decision, and, because the failed first version survives, she is the only case where you can see the same author get the encoding wrong and then fix it in public.

**What they do not settle.** Whether it worked. The causal claim, that these diagrams moved policy, is not established anywhere on this page, and Small, who has read the archives, says so explicitly.

---

## "In the style of Nightingale" means, concretely

From the wedges plate itself.

**Two panels, one scale, and the good news on the left.** Panel `1.` (April 1854 to March 1855, the catastrophe) sits on the **right**. Panel `2.` (April 1855 to March 1856, after the sanitary works) sits on the **left**, drawn on the same area scale so it is visibly a fraction of the size, with a **dashed leader line running between the two** to tie the scales together. Reading right to left is deliberate and it is the whole argument: the eye lands on the disaster and travels to the remedy.

**Twelve equal-angle sectors, one per month, area proportional to deaths.** The angle carries nothing. Only the radius varies, and area is the quantity. The caption says so in its first line: *"The Areas of the blue, red, & black wedges are each measured from the centre as the common vertex."*

**Three causes overlaid from a common center, not stacked.** Blue is preventable or mitigable zymotic disease, red is deaths from wounds, black is all other causes, each drawn from the center outward so they overlap. Blue swamps everything, which is the point.

**Palette.** A desaturated slate blue doing all the work, a pale pink-red, and a gray-black, on cream paper, with thin black outlines and no fills heavier than a wash. The dominant quantity gets the coolest, largest, most placid color. Nothing is red-for-alarm; red is the *small* category.

**No axes, no gridlines, no radial scale, no numbers anywhere on the wedges.** The finished, famous chart is entirely scale-free.

**A long prose caption that admits the ambiguities by name.** In engraved italic at the lower left, running six lines, including: *"In October 1854, & April 1855, the black area coincides with the red; in January & February 1856, the blue coincides with the black."* She lists the months where the overlay is unreadable rather than hoping nobody checks.

**Month labels set radially outside each rose**, small caps, rotating with the wedge so half of them are upside down, with the year marked at the April and March boundary.

**Title in decorative engraved capitals with a rule under it**, and each panel numbered with its own date range as a subtitle.

**One chart, one decision.** There is no exploratory version of this. It exists to make preventable disease visually dominate wounds on a single sheet handed to ministers.

## What they actually established, and what gets over-claimed in their name

### She did not invent the polar-area diagram, and the honest word is "may"

Playfair's pie predates her by half a century. Most of the graphic forms in her Crimean documents come from **William Farr**, her adviser at the General Register Office, whose Registrar-General reports had already used what Small calls "100% area" and stacked-bar constructions, and had used a honeycomb device for camp density. What Small will say about the two roses is careful:

> "This 'bat's wing' and its successor are so different from any diagrams that Farr did before that they may be Nightingale's own invention."

*May be.* Not *were*.

### "Coxcomb" is a misnomer, and the misnomer is traceable to one book

It is documented rather than asserted.

Nightingale used the word **for a booklet, never for a diagram**. It referred to the 2,000 copies she had privately printed of *Mortality of the British Army*, the showy reprint of a Royal Commission appendix that people would actually read. Her letter of Christmas Day 1857 to Sidney Herbert, which Small quotes from BL Add. MSS 43394 f210, itemizes the print run: *"I send you one of the 'coxcombs' There are 300 of these / 1700 of the vulgar sort / 2000."*

Two consequences:

- **The booklet she called the coxcomb did not contain the famous chart.** It was printed at the start of 1858 and carried the older bat's wing. The wedges did not exist until late that year.
- **The transfer of the word to the diagram is Cook's**, in his 1914 biography, which refers to "Miss Nightingale's 'coxcomb' diagrams". Everything since inherits it.

Calling the polar-area chart a coxcomb is not wrong in the sense that usage has settled, but the origin story attached to it is folklore.

### The first version was wrong, and I checked

The bat's wing plate is a genuinely different construction, and a designer's error preserved in print.

- It has **circular gridlines and a numeric radial scale** (100, 200, 300 and up), which the wedges plate does not.
- **The radius is proportional to the death rate**, so the shaded area grows as the square. Small's finding, which the plate corroborates: the text and the shape both imply the *area* is the quantity, and it is not.
- The distortion is visible in the plate's own note: had one of its figures been drawn at the same scale as the others on the sheet, *"the longest Radius, showing the Mortality in February, would have projected 40 inches from the Centre of the Circle."*

Small records that she recognized the error, inserted an erratum slip, and replaced the diagram in the three later documents. So the famous chart is **a correction**, which is the most useful thing about it and almost never mentioned.

Note the trade she made. Fixing the encoding meant abandoning the radial scale, because a scale-free area comparison is honest and a labeled radius was not. The corrected chart is quantitatively sound and completely unreadable as numbers, and the numbers live in the tables instead.

### "The chart convinced Parliament" is not established

What the primary source supports is narrower and still substantial. The 1858 volume opens with a War Office letter from Lord Panmure, dated 18 February 1857, formally asking her for the report. She wrote it, printed it privately, and circulated it. That is a solicited report to a government that was already listening, not a chart that broke through a wall.

Small, who has read the archives, argues the more influential diagram was probably a different one entirely: the "Lines" bar chart contrasting peacetime death rates of soldiers in English barracks against civilians around them, because that described a situation **still happening**, while the roses described a war the Army could claim was over. And his own closing paragraph refuses the triumphal ending:

> "did she achieve real success with these arguments, in terms of reducing the mortality of the population as a whole?"

He calls that the most important question and says it is unanswered pending archival work.

### The argument is in the arithmetic, and the arithmetic is in the book

From the 1858 text, of 48,742 sick, 36,179 were zymotic preventable cases, so preventable disease was 75 per cent of all disease in the army. Of 5,359 deaths, 373 were from wounds; of the 4,986 from disease, 4,465 were zymotic, leaving 521, so *"nearly 90 per cent. died from preventible causes alone."* Average army strength for the period, 28,623.

The chart does not establish this. The tables do. The chart is the part people look at, which is precisely the function she gave the word coxcomb.

### What the form costs, in this wiki's own terms

A polar-area diagram puts the reader on **area**, which [Cleveland & McGill](../studies/cleveland-mcgill-1984.md) place below position, length and angle, and the equal angles make each wedge look like a share of a whole when it is not. It is the pie chart's problem without the pie chart's excuse. See [pie-and-donut.md](../chart-types/pie-and-donut.md), and note the twist: since [Skau & Kosara](../studies/skau-kosara-2016.md) found angle the *worst* of a pie's three cues, holding angle constant and varying radius is not obviously the wrong trade.

The overlay is the sharper problem. Where black exceeds blue in a month, the visible blue is not the blue quantity. She names those months in the caption. Most modern polar-area charts do not.

## Works, and where they sit in this wiki

- ***Notes on Matters Affecting the Health, Efficiency, and Hospital Administration of the British Army*** (1858). **No source page.** Read in full text for this page.
- ***Mortality of the British Army*** (1858), the actual "coxcomb" booklet, 2,000 copies. **Not reached.** It carries the erroneous bat's wing and is the object the word refers to, so anyone writing about the naming should get hold of it.
- ***A Contribution to the Sanitary History of the British Army*** (1859), the anonymous public reply to a pamphlet accusing her of exaggerating, and the first appearance of the corrected wedges. **Not reached.**
- ***Notes on Nursing*** (1860) is on the Internet Archive in several editions and is out of scope here.

**Coverage before this page: zero.** No mention anywhere in this wiki. Small notes in passing that **Tufte does not mention her in *The Visual Display of Quantitative Information* either**, which is part of why the canon this project sampled had no route to her.

## Links

- [william-playfair.md](william-playfair.md), who got there first and argued about taxes instead of typhus
- [edward-tufte.md](edward-tufte.md), and the Minard comparison that Small uses to place her
- [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md), the nearest type page, and the evidence about angle that complicates the standard criticism of hers
- [concepts/channels.md](../concepts/channels.md), where area sits
- [refutations.md](../refutations.md), for the general shape of "the received story changed when someone opened the source"
