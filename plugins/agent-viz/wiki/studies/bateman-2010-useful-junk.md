---
type: study
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Bateman et al. 2010: Useful Junk?

Scott Bateman, Regan L. Mandryk, Carl Gutwin, Aaron Genest, David McDine, Christopher Brooks. *Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts.* CHI 2010, pp. 2573-2582. DOI [10.1145/1753326.1753716](https://doi.org/10.1145/1753326.1753716).

**What it is good for.** The most-cited counterweight to the chartjunk orthodoxy. It shows memorability is an axis data-ink discipline does not price in, which makes "maximize the data-ink ratio" indefensible as a *settled* rule.

**What it does not settle.** Most of what it is cited for. Twenty participants, one extreme embellishment style, unlimited viewing time and a high-level description task. The authors decline to recommend for or against embellishment.

**How this was read.** Bateman et al. is `primary-read`: the PDF from the MIT 6.859 readings mirror, [vis.csail.mit.edu/classes/6.859/readings/pdfs/Bateman-UsefulJunk.pdf](https://vis.csail.mit.edu/classes/6.859/readings/pdfs/Bateman-UsefulJunk.pdf), re-extracted with `pdftotext -layout`. The `hci.usask.ca` copy in older citations now 404s. The 2023 replication is `primary-read`, extracted the same way from OSF. The 2014 critique is `secondary-only`: paywalled, with only the publisher-deposited abstract reached, verbatim through the Crossref API.

## The finding

> "We found that people's accuracy in describing the embellished charts was no worse than for plain charts, and that their recall after a two-to-three-week gap was significantly better. Although we are cautious about recommending that all charts be produced in this style, our results question some of the premises of the minimalist approach to chart design."

**Description** (n = 20, paired t-tests). No difference on subject (t₁₉ = 0.84, p = .412), categories (t₁₉ = 1.38, p = .185) or trend (t₁₉ = 0.23, p = .818). Value message favored the Holmes charts (t₁₉ = 3.37, p = .003), an advantage summaries usually drop. No difference in completion time (t₁₉ = 1.834, p = .082; Holmes mean 2.60 min, plain 2.43 min).

**Immediate recall** (n = 10). No difference on subject (p = .124), categories (p = .129) or trend (p = .369). A difference on value message (t₉ = 2.24, p = .026).

**Long-term recall**, two to three weeks (n = 10). Significant on all four: subject (t₉ = 2.56, p = .015), categories (t₉ = 5.03, p < .001), trend (t₉ = 1.95, p = .042), value message (t₉ = 2.41, p = .020). They needed more prompting to recall the plain charts.

Directional tests were one-tailed at α = 0.05, as the paper states. Several long-term results (p = .042, p = .015) would not survive correction for the dozen-plus comparisons, and the first would not survive two-tailed testing.

**Eye tracking.** With Holmes charts, 67% of on-screen time went to data or data-plus-embellishment regions, against 78% with plain charts. 13% went to pure embellishment and 27% to dual-coded regions. Description time did not rise despite the gaze spent on embellished regions, the authors' proposed reason accuracy held.

## Method

Fourteen charts, two for training, each in a Holmes version from *Designer's Guide to Creating Charts and Diagrams* and a matched plain version. Participants saw one version of each, counterbalanced, and were not told about recall. Ten recalled after a five-minute distractor task, ten 12 to 22 days later. Responses were coded 0 to 2, with a second coder on a subset. Disagreements never exceeded one point.

## Sample size and population

Twenty participants (9 male, 11 female), aged 18 and up, 13 of them undergraduates. 17 said they at least occasionally read charts.

## Limits the authors state themselves

> "This is a potentially contentious issue, and there is no way to make a clear recommendation either in favour or against visual imagery."

> "it could be that a task that required detailed analysis of charts is hampered more by embellishments, rather than the high-level description task that we asked of our participants. One could imagine that in some safety-critical systems, such as those used by flight control systems, limiting the presentation to the salient information would likely be the preferred course."

> "It is important to note that we did not constrain the amount of time participants had to examine the charts. If viewing time was limited, it is possible that people could spend less time on the data elements."

> "In our study we intentionally chose the most extreme type of visual embellishment that we could -- namely, the full cartoon imagery used by Holmes."

They concede a confound. The monster's teeth trace the rising trend, and the word "monstrous" is in the title, so the imagery is partly a redundant encoding of the message rather than decoration in the chartjunk sense. Their own explanation for the value-message advantage is that "the images do often convey values, and this was likely the intention of the designer," and that a monster would not fit a story about rising life expectancy. That means the result may be about *well-designed integrated imagery by a professional* rather than about embellishment as a category. The paper says as much: "Finding an accompanying graphic that fits the story ... and finding a way to integrate the image into the representation of data, are likely to be difficult tasks that cannot be done well without a skilled designer."

Their conclusion:

> "there may be more to the usability and utility of charts than is currently captured by minimalist design approaches."

Both versions of the chart "tell the same story ... and both characterize this trend as 'monstrous.' There is therefore no guarantee that minimalist charts are free from bias."

## The 2023 replication

Syeda, South, Raynor, Panavas, Saffo, Morriss, Dunne & Borkin, *More Useful Junk? Replicating the Effects of Visual Embellishment on Description and Recall of Charts* (2023), DOI [10.31219/osf.io/dferj](https://doi.org/10.31219/osf.io/dferj), open access at [osf.io/dferj/download](https://osf.io/dferj/download).

Four conceptual replications, each with 20 university students and no overlap (19 in Study 1 after one invalid response). Studies 2 and 4 ran synchronously over Zoom, Studies 1 and 3 asynchronously over Google Forms. Study 3 skipped long-term recall, Study 4 short-term.

- **Description.** Studies 2 and 4 reproduced the value-message advantage. Studies 1 and 3 only partially replicated it.
- **Short-term recall.** Study 1: no significant differences. Study 2 matched the original. Study 3 ran no statistics and saw a trend favoring embellishment.
- **Long-term recall.** Study 1: no significant differences on any of the four questions, though embellished charts averaged higher. Study 4 "aligned almost completely" with the original. Study 2 found the value-message effect only.
- **Preference.** The most robust result across the original and its three replications, which all found embellished charts significantly faster and easier to remember, more attractive and more enjoyable.

> "It must be noted that failing to reproduce the original findings does not indicate that the replications were not successful. Rather it is an indication of more investigation as to whether the difference in findings is due to the differences in the experimental procedures."

> "Our comparison-analysis shows that many of the findings from the original paper were confirmed by one or more of the replication studies."

Synchronous studies replicate and asynchronous ones do not, pointing at experimenter presence and prompting as moderators. The long-term recall advantage is not stable at n = 20.

## The 2014 critique

Li & Moacdieh 2014, *Is "chart junk" useful? An extended examination of visual embellishment*, Proc. HFES 58(1), DOI [10.1177/1541931214581316](https://doi.org/10.1177/1541931214581316). `secondary-only`: abstract only.

> "Researchers have examined the effects of visual embellishment on comprehension and memorability of charts under specific conditions, such as charts with a small number of data points that were viewed with no time limit (Bateman et al., 2010). This paper extends previous studies and investigates the effects of visual embellishment given different time limits for viewing these charts. Similar to the Bateman et al. (2010) study, we compared embellished charts (selected from the work of Nigel Holmes) and plain, grayscale charts, but we limited our selection to those that consisted of larger data sets (10 or more data points). Results showed that the presence of a time limit affected comprehension and short-term recall performance, while the type of chart significantly affected short-term recall. In addition, the type of chart affected the time needed to review the chart while answering the questions. Participants found Holmes charts more attractive and memorable."

It tests the two limits Bateman et al. named, viewing time and data-set size. The abstract gives no direction for the chart-type effects.

## What this result does not license

- **Not "chartjunk is fine."** What replicates is narrower: imagery around a correctly drawn chart does not hurt description accuracy, and people prefer it.
- **Not a long-term memorability advantage.** That headline result does not replicate cleanly.
- **Not embellishment that changes the mark encoding the value.** [Skau et al. 2015](skau-2015-embellished-bars.md) found deformed bars raise error. Holmes draws around a correct bar, so the two do not conflict.
- **Not embellishment as a category.** A professional encoded the message into these images.

## Links

- Replication: [osf.io/dferj](https://osf.io/dferj/)
- [skau-2015-embellished-bars.md](skau-2015-embellished-bars.md): the counterweight, which does not contradict this one
- [gillan-richman-1994-data-ink.md](gillan-richman-1994-data-ink.md): the other empirical attack on maximal data-ink
- [refutations.md](../refutations.md), "Chartjunk and the data-ink ratio as settled"
- [inventory.md](../inventory.md), topics 67 (data-ink discipline and its contested status) and 88 (memorability)
