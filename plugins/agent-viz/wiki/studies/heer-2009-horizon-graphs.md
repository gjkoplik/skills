---
type: study
status: primary-read
retrieved: 2026-10-16
author: jeffrey-heer
---

# Heer, Kong & Agrawala 2009: Sizing the Horizon

Jeffrey Heer (Stanford), Nicholas Kong and Maneesh Agrawala (UC Berkeley), "Sizing the Horizon: The Effects of Chart Size and Layering on the Graphical Perception of Time Series Visualizations," CHI 2009. PDF: [vis.stanford.edu/files/2009-TimeSeries-CHI.pdf](http://vis.stanford.edu/files/2009-TimeSeries-CHI.pdf).

**What it is good for.** The one experiment in this corpus on horizon graphs: value comparison on line charts, mirrored charts and banded horizon graphs at heights from 48 pixels down to 2. Whether mirroring costs anything, how many bands is too many, and at what height bands start to pay.

**What it does not settle.** Reading slopes, trends or rates of change, which were not measured. Chart width and the distance between compared points. Charts larger than 48 pixels, or with tick labels and gridlines. Five or more bands. Whether the optimal heights survive a different accuracy target.

**How this was read.** The Stanford Vis Group PDF, byte-identical to the copy at idl.cs.washington.edu. Text extracted locally with `pypdf` in plain and layout modes, cross-checked against each other. The result figures print no values, so every number below is from the running text.

## The finding

Mirroring, from the Design Implications section:

> "One unexpected result was that mirroring a chart—flipping the negative values around zero—neither slowed estimation time nor hurt estimation accuracy. As mirroring cuts the size of the chart in half without any observed downside, we advocate its use when space constraints warrant, so long as the viewer knows how to interpret the chart."

In Experiment 1, mirrored and offset horizon graphs did not differ (F(2,16) = 0.367, p = 0.699). In Experiment 2, one-band mirror charts matched line charts of the same pixel height on time (p = 0.632) and had lower error at every height:

> "Contrary to our hypothesis, 1-band mirror charts exhibited equal or better speed and accuracy than normal line charts that were twice as tall."

Layering:

> "We found that dividing a chart into layered bands reliably increased estimation time and increased estimation error at constant chart heights. However, we also found that 2-band mirrored charts led to better estimation accuracies for chart heights less than 24 pixels (6.8 mm on our displays). For larger chart sizes, we advise scaling 1-band mirrored charts. For smaller sizes, we advise adding layered bands."

"Better" is against line charts and one-band mirror charts of the same pixel height. The Results section says so:

> "Estimation error for 2-band mirror charts stayed relatively stable, equaling or beating the line and 1-band mirror charts at scales of 1/4 (12 pixels) and lower."

The main experiment tested 48, 24, 12 and 6 pixels, so "less than 24 pixels" means 12 and 6. At 12 the Discussion calls the error "comparable across charts", which leaves the advantage at 6. No pairwise test of the crossover is reported, and the RM-MANOVA on (error, time) found no chart-by-height interaction (F(12,348) = 0.921, p = 0.526). Two-band charts were slower than line charts by 2.05 s and than one-band charts by 1.91 s (both p < 0.001), a reading of an ambiguous sentence that the Figure 10 caption settles.

The authors explain the crossover by virtual resolution, the unfolded height: twice the pixel height for a one-band mirror chart, four times for two bands. At 24 virtual pixels and below, error rose linearly as it halved (R² = 0.986, slope -4.1 units per log2 pixel). The follow-up at 6, 4 and 2 pixels found "nearly identical error levels at matching virtual resolution values" (R² = 0.980).

Band count, Experiment 1, at a fixed 40 pixels. Mean error was 4.12 units with two bands, 4.04 with three and 5.64 with four. Four bands were less accurate than two (p = 0.042) and three (p = 0.026). Time rose at every step, by 2.89 s from two to three bands and 1.91 s from three to four (p < 0.001). No more than four bands were tested:

> "We discourage the use of 4 or more bands, as this resulted in increased time and error, and subjects complained that interpreting 4-band charts was difficult and tiring."

Size:

> "For both normal line charts and 1-band mirror charts, we found a chart height of 24 pixels (6.8 mm on our 14.1” 1024 × 768 pixel displays) to be optimal. For 2-band line charts, we found optima at 12 and 6 pixels (3.4 and 1.7 mm) – performance is about equal at both these sizes."

"Optimal" means the size that "minimized estimation time while preserving accuracy". At 24 pixels charts were 1.1 s faster than at 48 and error rose less than 2 units, with no test of that difference reported.

## Method

Each trial showed two charts, 500 pixels wide, with a point marked on each, always in different bands. Subjects said which was larger, then estimated the absolute difference on a -100 to 100 range, "as quickly as possible while trying to make estimates accurate to within 5 values." Series were smoothed random walks. Practice with feedback preceded each block. Analysis used per-subject 80% trimmed means of estimation, since discrimination accuracy was at least 96% everywhere.

Experiment 1 crossed mirrored and offset graphs with two, three and four bands at 40 pixels, run in a Flash applet on subjects' own machines with no control of resolution. Experiment 2 crossed line, one-band and two-band mirror charts with 48, 24, 12 and 6 pixels on a 14.1-inch LCD at 1024 × 768. The follow-up crossed the two mirror charts with 6, 4 and 2 pixels.

Two Experiment 1 statistics do not match their p values, in both extractions: F(2,34) = 58.27 is printed with p = 0.013 (that F gives p below 0.001), and F(4,68) = 0.211 with p = 0.163 (it gives about 0.93). The Design Implications place the three-band comparison at 48 pixels, though Experiment 1 charts were 40.

## Sample size and population

- **Experiment 1:** 18 unpaid subjects (13 male, 5 female), graduate or undergraduate engineering students recruited through campus mailing lists.
- **Experiment 2:** 30 paid undergraduates (17 male, 13 female) from a variety of majors, recruited through a research participation pool.
- **Follow-up:** 8 paid graduate engineering students (6 male, 2 female), 6 of whom had taken part in Experiment 1. Baseline error was "substantially less", which the authors attribute to the different subject pool.

## Limits the authors state themselves

> "One limitation of the present work is that we only measured the results of value comparison tasks. Graphical perception of time series typically involves observing rates of change in addition to comparing values."

> "Another limitation of our study is that we only varied chart heights and did not investigate the effects of chart width or of distance between comparison points."

> "However, our subjects were instructed to make estimates accurate within 5 values. Future work is needed to ascertain if similar results occur under different target accuracies."

> "In our experiments we discovered that accuracy stabilized at the larger chart heights we investigated. However, we did not determine if those accuracy rates would hold at still larger chart sizes."

They also did not vary physical pixel size, and their model's prediction that three bands help below 6 pixels is untested.

## What this result does not license

- **Not "horizon graphs show trends well."** Only value comparison was measured.
- **Not "two bands beat line charts."** At constant height, bands added time and error. In the main experiment the two-band accuracy advantage appears at 6 pixels, and at 12 the charts were comparable.
- **Not a measured penalty for five or more bands.** Four was the most tested.
- **Not a measured optimum in general.** The 24-pixel optimum is relative to 48, 12 and 6 pixels, the within-5-values target, and charts without the tick marks and gridlines the authors expect larger charts to carry.
- **Not a population estimate.** Engineering students in two of three samples, and repeat subjects in the follow-up.
- **Not a test of many series at once.** Each trial compared two charts.

## Links

- PDF: [vis.stanford.edu/files/2009-TimeSeries-CHI.pdf](http://vis.stanford.edu/files/2009-TimeSeries-CHI.pdf), also at [idl.cs.washington.edu/files/2009-TimeSeries-CHI.pdf](https://idl.cs.washington.edu/files/2009-TimeSeries-CHI.pdf)
- [../chart-types/horizon-graph.md](../chart-types/horizon-graph.md): the type page this supports
- [../people/jeffrey-heer.md](../people/jeffrey-heer.md): the first author across his work
- [../concepts/channels.md](../concepts/channels.md): where layering sits relative to position and saturation
