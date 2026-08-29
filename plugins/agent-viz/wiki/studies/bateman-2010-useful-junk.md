---
type: study
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Bateman et al. 2010: Useful Junk?

Scott Bateman, Regan L. Mandryk, Carl Gutwin, Aaron Genest, David McDine, Christopher Brooks. *Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts.* CHI 2010, pp. 2573-2582. DOI [10.1145/1753326.1753716](https://doi.org/10.1145/1753326.1753716).

Twenty participants described fourteen charts, half Nigel Holmes cartoon-embellished and half stripped plain, then were asked to recall them either immediately or two to three weeks later. Description accuracy was no worse for the embellished charts; long-term recall was significantly better. It is the single most-cited counterweight to the chartjunk orthodoxy.

**How this was read.** PDF retrieved from the MIT 6.859 readings mirror, [vis.csail.mit.edu/classes/6.859/readings/pdfs/Bateman-UsefulJunk.pdf](https://vis.csail.mit.edu/classes/6.859/readings/pdfs/Bateman-UsefulJunk.pdf), and re-extracted with `pdftotext -layout`. The `hci.usask.ca` copy referenced in older citations now 404s.

## Two reachability improvements over what refutations.md records

[refutations.md](../refutations.md) notes that a methodological critique of Bateman was unreachable (HTTP 403). Both of these are new as of this page.

1. **The critique is Li & Moacdieh 2014**, *Is "chart junk" useful? An extended examination of visual embellishment*, Proc. HFES 58(1), DOI [10.1177/1541931214581316](https://doi.org/10.1177/1541931214581316). The full text is still paywalled, but the publisher-deposited abstract is retrievable verbatim through the Crossref API. Summarized below and marked `secondary-only`.
2. **There is now a four-way replication.** Syeda, South, Raynor, Panavas, Saffo, Morriss, Dunne & Borkin, *More Useful Junk? Replicating the Effects of Visual Embellishment on Description and Recall of Charts* (2023), DOI [10.31219/osf.io/dferj](https://doi.org/10.31219/osf.io/dferj), open access at [osf.io/dferj/download](https://osf.io/dferj/download). `primary-read`, retrieved and extracted the same way. It changes how much weight the original finding can carry.

## What it is good for

Establishing that the minimalist position is a position rather than a finding, and that memorability is a real axis data-ink discipline does not price in. It is the paper that makes "maximize the data-ink ratio" indefensible as a *settled* rule.

## What it does not settle

Almost everything people use it for. n = 20 with ten per recall condition, one extreme embellishment style, unlimited viewing time, and a high-level description task. The authors decline to make a recommendation in either direction, in those words.

## The finding

The abstract, verbatim:

> "We found that people's accuracy in describing the embellished charts was no worse than for plain charts, and that their recall after a two-to-three-week gap was significantly better. Although we are cautious about recommending that all charts be produced in this style, our results question some of the premises of the minimalist approach to chart design."

Broken out by measure, because "no worse" and "significantly better" are both compressions.

**Description phase (n = 20, paired t-tests).** No difference on subject (t₁₉ = 0.84, p = .412), categories (t₁₉ = 1.38, p = .185) or trend (t₁₉ = 0.23, p = .818). **A difference on value message** (t₁₉ = 3.37, p = .003), *favoring the Holmes charts*. No difference in completion time (t₁₉ = 1.834, p = .082; Holmes mean 2.60 min, plain 2.43 min).

That fourth result is not "no worse." It is an advantage for embellishment on the description task, and it is usually dropped from summaries of this paper in both directions.

**Immediate recall (n = 10).** No difference on subject (p = .124), categories (p = .129) or trend (p = .369). A difference on value message (t₉ = 2.24, p = .026).

**Long-term recall, two to three weeks (n = 10).** Significant differences on all four: subject (t₉ = 2.56, p = .015), categories (t₉ = 5.03, p < .001), trend (t₉ = 1.95, p = .042), value message (t₉ = 2.41, p = .020). Long-term participants also needed significantly more prompting to recall the plain charts.

The tests were **one-tailed at α = 0.05** where the hypothesis was directional, which the paper states plainly. Several of the long-term results (p = .042, p = .015) would not survive two-tailed testing or any correction for the dozen-plus comparisons run.

**Eye tracking.** Participants spent 67% of on-screen time on data or data-plus-embellishment regions with Holmes charts, versus 78% with plain charts. 13% went to pure embellishment and 27% to dual-coded regions. Despite 40% of gaze time going to embellishment, description time did not increase, which is the mechanism the authors propose for why accuracy held.

## Method

Fourteen charts, each existing in a Holmes version taken directly from *Designer's Guide to Creating Charts and Diagrams* and a plain version the authors built to match on data, chart type and positioning. Each participant saw only one version of each chart. Two charts were training. Order was counterbalanced across two conditions.

Participants were **not told about the recall phase**, to prevent intentional learning. Ten went into immediate recall (after a five-minute distractor task designed to disrupt visual and linguistic memory) and ten into long-term recall, scheduled 12 to 22 days later.

Responses were coded 0 to 2 by a single primary coder, with a second independent coder on a subset and a re-coding by the primary coder. Disagreements were rare and never more than one point.

## Sample size and population

Twenty participants (9 male, 11 female), aged 18 and up, 13 of them undergraduates. 17 said they at least occasionally read charts. Ten per recall condition.

## Limits the authors state themselves

The paper is much more careful than its citation record. On whether to recommend embellishment:

> "This is a potentially contentious issue, and there is no way to make a clear recommendation either in favour or against visual imagery."

On task scope:

> "it could be that a task that required detailed analysis of charts is hampered more by embellishments, rather than the high-level description task that we asked of our participants. One could imagine that in some safety-critical systems, such as those used by flight control systems, limiting the presentation to the salient information would likely be the preferred course."

On viewing time, which is the limit the 2014 critique goes after:

> "It is important to note that we did not constrain the amount of time participants had to examine the charts. If viewing time was limited, it is possible that people could spend less time on the data elements."

On the stimuli being a deliberate extreme:

> "In our study we intentionally chose the most extreme type of visual embellishment that we could -- namely, the full cartoon imagery used by Holmes."

They also concede a **confound they cannot rule out**: the Holmes images are tightly coupled to the data. The monster's mouth and teeth trace the rising trend, and the word "monstrous" is in the title. So the imagery is not decoration in the chartjunk sense, it is partly a redundant encoding of the message. Their own explanation for the value-message advantage is that "the images do often convey values, and this was likely the intention of the designer," and that a monster would not fit a story about rising life expectancy. That means the result may be about *well-designed integrated imagery by a professional* rather than about embellishment as a category. The paper says as much: "Finding an accompanying graphic that fits the story ... and finding a way to integrate the image into the representation of data, are likely to be difficult tasks that cannot be done well without a skilled designer."

Their closing observation, weaker than the way the paper gets cited:

> "there may be more to the usability and utility of charts than is currently captured by minimalist design approaches."

Plus a fair point against the minimalist claim to neutrality: both versions of the chart "tell the same story ... and both characterize this trend as 'monstrous.' There is therefore no guarantee that minimalist charts are free from bias."

## The 2023 replication

Syeda et al. ran **four** conceptual replications, each with 20 participants, matching the original's sample size exactly (one dropped in Study 1 for invalid responses, so 19 there). No overlap between studies. University students, as in the original. Two were synchronous over Zoom (Studies 2 and 4) and two asynchronous over Google Forms (Studies 1 and 3). Study 3 dropped long-term recall; Study 4 dropped short-term.

What held and what did not:

- **Description phase.** The synchronous studies (2 and 4) reproduced the original's value-message advantage. The asynchronous studies (1 and 3) only partially replicated it.
- **Short-term recall.** Study 1 found **no significant differences**. Study 2 matched the original. Study 3 did not run statistics and reported a qualitative trend favoring embellishment.
- **Long-term recall**, the original's headline result. Study 1 (asynchronous) **found no significant differences on any of the four questions**, though embellished charts scored higher on average throughout. Study 4 (synchronous) "aligned almost completely" with the original. Study 2 found the value-message effect only.
- **Preference.** The most robust result across all five studies. The original and three replications agreed that embellished charts were significantly faster and easier to remember, more attractive, and more enjoyable.

The authors' framing is careful, and it cuts against a lazy reading in either direction:

> "It must be noted that failing to reproduce the original findings does not indicate that the replications were not successful. Rather it is an indication of more investigation as to whether the difference in findings is due to the differences in the experimental procedures."

> "Our comparison-analysis shows that many of the findings from the original paper were confirmed by one or more of the replication studies."

The pattern, synchronous replicates and asynchronous does not, points at experimenter presence and prompting as moderators rather than at the effect being absent. **The long-term recall advantage is not a stable finding at n = 20.**

## The 2014 critique

`secondary-only`. Abstract verified verbatim from the publisher's Crossref deposit; body not reached.

> "Researchers have examined the effects of visual embellishment on comprehension and memorability of charts under specific conditions, such as charts with a small number of data points that were viewed with no time limit (Bateman et al., 2010). This paper extends previous studies and investigates the effects of visual embellishment given different time limits for viewing these charts. Similar to the Bateman et al. (2010) study, we compared embellished charts (selected from the work of Nigel Holmes) and plain, grayscale charts, but we limited our selection to those that consisted of larger data sets (10 or more data points). Results showed that the presence of a time limit affected comprehension and short-term recall performance, while the type of chart significantly affected short-term recall. In addition, the type of chart affected the time needed to review the chart while answering the questions. Participants found Holmes charts more attractive and memorable."

So the critique targets exactly the two limits Bateman et al. named themselves: unlimited viewing time, and small data sets. The abstract does not report the *direction* of the chart-type effects, so no direction can be attributed to it. Anything drawn from this paper beyond the abstract is unverified.

## What this result does not license

"Chartjunk is fine." What survives replication is that description accuracy is not damaged by imagery placed around a correctly drawn chart, and that people prefer such charts. What does not survive cleanly is the long-term recall advantage. And none of it extends to embellishment that touches the mark encoding the value, which is [Skau et al. 2015](skau-2015-embellished-bars.md)'s territory and goes the other way.

## Where this leaves the debate

Nowhere clean, which is the honest answer and matches [refutations.md](../refutations.md). Adding this page's material: description accuracy holding up is the most replicated part of Bateman, preference is the most robust, long-term recall is the least stable, and the charts in question were built by a professional who encoded the message into the imagery.

Against all of it, Skau et al. show that when the embellishment touches the *mark that encodes the value*, error rates go up. Those two are not actually in conflict. Holmes puts imagery around and behind a correctly drawn bar; Skau's triangles and rounded tops change the bar itself.

## Links

- Replication: [osf.io/dferj](https://osf.io/dferj/)
- [skau-2015-embellished-bars.md](skau-2015-embellished-bars.md), the counterweight, and not actually contradictory
- [gillan-richman-1994-data-ink.md](gillan-richman-1994-data-ink.md), the other empirical attack on maximal data-ink
- [refutations.md](../refutations.md), "Chartjunk and the data-ink ratio as settled"
- [inventory.md](../inventory.md), topics 67 (data-ink discipline and its contested status) and 88 (memorability)
