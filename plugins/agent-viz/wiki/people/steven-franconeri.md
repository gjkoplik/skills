---
type: person
status: primary-read
status_partial: true
retrieved: 2026-10-17
---

# Steven Franconeri

**What they are known for.** Bringing the perception laboratory's methods into visualization experiments as a co-author rather than a lead: just-noticeable differences, working-memory loads and preferential-viewing tasks applied to charts, and the habit of asking which visual feature a reader computes rather than which chart they were shown. Five papers in this corpus carry his name, and on every one the first author is someone else.

**How this was read.** Through the wiki's primary readings of five co-authored papers: [Harrison et al. (2014)](../studies/harrison-2014-ranking-correlation.md) and [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md), each with a study page; Haroz, Kosara & Franconeri (2015) on ISOTYPE and (2016) on the connected scatterplot, downloaded from `media.eagereyes.org` and extracted locally with `pdftotext`; and Bertini, Correll & Franconeri (2020), read as an arXiv preprint for [Michael Correll's page](michael-correll.md). His 2021 review, "The Science of Visual Data Communication: What Works" (*Psychological Science in the Public Interest*, with four co-authors), is closed access and was not reached, and no local copy was found. Affiliation as printed is Northwestern University. `status_partial`: the review is the work most often cited to him and it is the one not read.

**What they are good for.** *What is the reader's visual system doing with this chart?* The Harrison paper's visual-features argument and the ISOTYPE paper's working-memory framing are two of the few places in this corpus where a result is explained by a perceptual mechanism rather than by the chart's name. Also the hedge on rules his co-authored papers get cited for: the truncation paper refuses an honest-dishonest binary, and the ranking critique keeps the ranking.

**What they do not settle.** Whether any proposed mechanism transfers. Each is offered after the fact from one experiment, and none has been tested as a prediction here. No sole-authored study appears in this corpus, so nothing can be attributed to him alone. Nothing on color, maps, networks or accessibility, and the review that would carry his synthesis is unread.

---

## What their work established

### Correlation precision across nine forms, 2014, with Harrison, Yang and Chang

[Harrison et al.](../studies/harrison-2014-ranking-correlation.md) measured how precisely 1,687 crowdsourced readers told two correlations apart on nine forms. Scatterplots led with positive and negative data alike, parallel coordinates matched them on negative data only, and six form-direction pairs were at chance. The paper's explanation runs through features rather than forms:

> "our results suggest that the reason the perception of correlation in scatterplots follows Weber's law is because the underlying visual features that vary with correlation follow Weber's law."

Kay & Heer's reanalysis kept the scatterplot result, grouped the rest into four precision bands, and dropped the Weber model.

### Pictographs, 2015, with Haroz and Kosara

*ISOTYPE Visualization: Working Memory, Performance, and Engagement with Pictographs* (CHI 2015) tested simple bar charts whose bars were stacks of pictographs against the same data with the images as decoration or as axis labels, on memory for values just seen and under an added load, on speed of finding a value, and on which chart readers chose to inspect. The abstract: "We find that superfluous images can distract." The conclusion: "We found no strong evidence that using pictographs to communicate data hurts performance on any of our tasks." The four stated conclusions are that only pictographs carrying the data mapping help or at least do not hurt, that discretizing a bar into small items improves encoding and recall for small values only, that pictographs help memory during demanding tasks, and that they draw closer inspection. The authors' own limits: short abstracted tasks, three bars, one color, and "it is unclear whether ISOTYPE visualization would be useful for tasks such as search or group segmentation." [refutations.md](../refutations.md) reaches the same decoration-versus-data-mark split from Bateman and Skau.

### The connected scatterplot, 2016, with Haroz and Kosara

*The Connected Scatterplot for Presenting Paired Time Series* (*TVCG*) ran four studies against the dual-axis line chart. Fourteen college students read two news datasets in both forms: understanding was high on both, the three qualitative errors were all on the connected scatterplot, and correlational language appeared 28 times for the line charts against 3 for the connected scatterplots. Thirty-five Mechanical Turk workers translated one form into the other, with 8 excluded for chance-level copying: performance was 92% overall, time was reversed on 13% of translation trials and on 5% of trials that merely copied a connected scatterplot. In a six-thumbnail viewing task, readers "chose to look at it first more often than at standard line charts." The paper's own guideline: "If a major purpose of a graph is to leave the viewer with an understanding of negative or positive correlation in a dataset, a more traditional DALC may make this conclusion far more salient." Detail on [chart-types/connected-scatterplot.md](../chart-types/connected-scatterplot.md).

### Truncation, 2020, with Correll and Bertini

[Truncating the Y-Axis: Threat or Menace?](../studies/correll-2020-truncating-the-y-axis.md) found the exaggeration from a truncated axis persists across chart types and that two static break-glyph designs did not measurably reduce it. The authors refuse the strong reading: "We reject the unequivocal dichotomy of 'honest' and 'dishonest' charts."

### Scoping the ranking, 2020, with Bertini and Correll

*Why Shouldn't All Charts Be Scatter Plots?* is a position paper with no experiment. It challenges the assumption that precision on a two-value ratio judgment transfers to other tasks, and it keeps the ranking: "Of course we are not proposing to throw the baby out with the bathwater." The quotes and their placement are on [michael-correll.md](michael-correll.md); the empirical counterpart is Kim & Heer (2018) on [jeffrey-heer.md](jeffrey-heer.md).

## Where his name is used for more than he showed

**"Franconeri showed chartjunk helps."** The ISOTYPE paper found no cost and some benefit for pictographs that carry the data, and found decorative images distracting. It tested three-bar charts on memory, search and viewing choice, not comprehension of a message.

**"Franconeri's lab proved scatterplots are the best chart."** For telling two correlations apart, between r of 0.3 and 0.8, on bivariate normal points. Not for reading a value, not for seeing a trend, and the reanalysis that confirmed the scatterplot result also replaced the total ranking with four groups.

**Counting him as independent.** He is on Harrison et al., Correll et al. 2020, the ranking critique and both Haroz papers. Two of those share Correll, two share Kosara, so the three names recur as one cluster across the correlation, truncation, embellishment and connected-scatterplot results here. [michael-correll.md](michael-correll.md) and [robert-kosara.md](robert-kosara.md) record the same overlap from their sides.

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| Harrison, Yang, Franconeri & Chang (2014), "Ranking Visualizations of Correlation Using Weber's Law," *TVCG* | `primary-read`, [PDF](http://www.cs.tufts.edu/~remco/publications/2014/InfoVis2014-JND.pdf) | [studies/harrison-2014-ranking-correlation.md](../studies/harrison-2014-ranking-correlation.md) |
| Haroz, Kosara & Franconeri (2015), "ISOTYPE Visualization," CHI | `primary-read`, [PDF](https://media.eagereyes.org/papers/2015/Haroz-CHI-2015.pdf) | No page. Belongs beside [studies/bateman-2010-useful-junk.md](../studies/bateman-2010-useful-junk.md) and [studies/skau-2015-embellished-bars.md](../studies/skau-2015-embellished-bars.md) |
| Haroz, Kosara & Franconeri (2016), "The Connected Scatterplot for Presenting Paired Time Series," *TVCG* | `primary-read`, [PDF](https://media.eagereyes.org/papers/2016/Haroz-TVCG-2016.pdf) | No page. Its results are on [chart-types/connected-scatterplot.md](../chart-types/connected-scatterplot.md) |
| Correll, Bertini & Franconeri (2020), "Truncating the Y-Axis: Threat or Menace?", CHI | `primary-read` | [studies/correll-2020-truncating-the-y-axis.md](../studies/correll-2020-truncating-the-y-axis.md) |
| Bertini, Correll & Franconeri (2020), "Why Shouldn't All Charts Be Scatter Plots?", arXiv 2008.11310 | `primary-read`, preprint | [people/michael-correll.md](michael-correll.md), [concepts/channels.md](../concepts/channels.md) |
| Franconeri et al. (2021), "The Science of Visual Data Communication: What Works," *Psychological Science in the Public Interest* | `not-reached`. Closed access at the publisher, no repository copy found | No page. The synthesis most often cited to him |

## See also

- [../studies/harrison-2014-ranking-correlation.md](../studies/harrison-2014-ranking-correlation.md): the correlation result and its reanalysis
- [../studies/correll-2020-truncating-the-y-axis.md](../studies/correll-2020-truncating-the-y-axis.md): the truncation result
- [michael-correll.md](michael-correll.md) and [robert-kosara.md](robert-kosara.md): the two collaborators his results are shared with
- [../chart-types/connected-scatterplot.md](../chart-types/connected-scatterplot.md): where the 2016 paper's numbers land
- [../refutations.md](../refutations.md): the chartjunk split his ISOTYPE paper supports
