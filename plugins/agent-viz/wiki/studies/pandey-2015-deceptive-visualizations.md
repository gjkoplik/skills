---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Pandey et al. 2015: How Deceptive are Deceptive Visualizations?

Anshul Vikram Pandey, Katharina Rall, Margaret L. Satterthwaite, Oded Nov, Enrico Bertini. *How Deceptive are Deceptive Visualizations?: An Empirical Analysis of Common Distortion Techniques.* CHI 2015, pp. 1469-1478. DOI [10.1145/2702123.2702608](https://doi.org/10.1145/2702123.2702608).

The first controlled experiment measuring how much four common chart distortions actually move a reader's interpretation. Four distortions: truncated axis (bar chart), area-as-quantity (bubble chart), aspect ratio (line chart), and inverted axis (line-area chart). Crowdsourced on Mechanical Turk.

**How this was read.** Extracted locally with `pdftotext` from the authors' own preprint, hosted at [enrico.bertini.io/s/deceptive-chi2015.pdf](http://enrico.bertini.io/s/deceptive-chi2015.pdf), which is also NYU School of Law Public Law & Legal Theory Working Paper 15-03 and carries the line "Preprint of the full paper published at ACM CHI 2015." The ACM camera-ready was paywalled. Every number below is from that preprint. If a figure ever needs to be quoted in a context where a one-digit difference matters, re-check against the ACM version.

## What it is good for

Two things, and only two.

1. **A magnitude for how far distortion moves a Likert-scale judgment**, on charts where the true values were printed on the chart. The 58.5%-to-129.5% figure.
2. **A worked demonstration that inverted axes reverse conclusions**, with a control group that gets it right almost universally.

## What it does not settle

Anything about *why*. The individual-differences analysis, which was a stated goal of the study, returned nothing: "Despite our expectations the analysis on individual differences did not provide definite conclusions." It also does not settle relative severity across distortions in any careful way, because the three exaggeration conditions differ in chart type and distortion simultaneously, with no factorial separation.

---

## The finding

### Message exaggeration

Table 2, average response on a 1-to-5 Likert scale to a "how much bigger" question:

| Chart | Distortion | Control | Deceptive | Increase |
|---|---|---|---|---|
| Line | Aspect ratio | 1.39, 95% CI [1.23, 1.55] | 3.19, 95% CI [2.76, 3.62] | +129.5% |
| Bar | Truncated axis | 1.45, 95% CI [1.27, 1.62] | 2.77, 95% CI [2.26, 3.28] | +91.0% |
| Bubble | Area as quantity | 1.71, 95% CI [1.45, 1.98] | 2.71, 95% CI [2.27, 3.15] | +58.5% |

The Discussion summarizes this as "the distorted charts lead to responses between 58.5% and 129.5% bigger than the control condition." That recomputes exactly: 3.19/1.39 = 2.295 and 2.71/1.71 = 1.585.

Mann-Whitney U, one-tailed, per pair: aspect ratio U = 1409, Z = 5.88, p < 0.0001, r = 0.66; area U = 1121, Z = 3.08, p = 0.0007, r = 0.34; truncated axis U = 1144, Z = 3.36, p = 0.0003, r = 0.37.

### Message reversal

Table 3, the inverted-axis condition:

| Treatment | Selected | Correct | Incorrect | Uncertain |
|---|---|---|---|---|
| Control | 40 | 39 (97.50%) | 1 (2.5%) | 0 |
| Deceptive | 38 | 7 (18.42%) | 30 (78.95%) | 1 (0.02%) |

Freeman-Halton extension of Fisher's Exact Test, p < 0.0001.

## The paper contradicts itself

The Discussion says:

> "the deceptive condition led to 97.5% incorrect responses whereas the control condition led to only 18.4% incorrect responses"

That sentence took the two **correct**-column percentages, relabeled them incorrect, *and* swapped which condition each belongs to. The table is right and the Discussion is wrong, and a third passage in the Results body agrees with the table:

> "Out of the 38 selected participants who saw the deceptive visualization, 30 responded incorrectly, 7 correctly and one chose the uncertain response. For the 40 participants who saw the control condition, 39 responded correctly, 1 responded incorrectly and no participant reported uncertainty."

So it is two body passages against one Discussion sentence. The error is direction-preserving, so the paper's conclusion survives intact. But **anyone quoting 18.4% as a control error rate is off by roughly 7x**; the real control error rate is 2.5%.

Table 3 also misprints the deceptive-condition Uncertain cell as 1 (0.02%). 1/38 is 2.63%.

**Not established:** that the field propagates the wrong figure. A search for secondary sources repeating 97.5%/18.4% found none. Do not ship that claim without naming specific offenders.

## Method

Between-subjects, Amazon Mechanical Turk. Participants self-reported a US location and had a previous approval rate at or above 99%. Five stages: demographics, a visual ability test, a chart familiarity test (5-point Likert), the treatment with one deception-test question plus an attention check, then the 18-item Need for Cognition short scale. 5-10 minutes, paid $0.30.

Exaggeration was measured by asking a "how much" question ("How much better do you think the condition of safe drinking water access in Silvatown is as compared to that in Wilowtown?") answered on a 5-point Likert scale. Reversal was measured by a "what" question with three choices: a correct interpretation, the interpretation the distortion pushes toward, and "I do not know."

**One design choice does a lot of work:** "in each of the presented treatments, the actual numbers/data were presented on the chart as we were interested in detecting deception due to visual representation even in the presence of accurate data." The effect is not a failure to read numbers. The numbers were right there.

Two pilot studies preceded the final study, one on a real-world deceptive chart and one on synthetic data. The pilots found no noticeable difference between real and artificial scenarios.

## Sample size and population

- **330 unique MTurk participants total**, split into two experiments.
- **Exaggeration experiment: 250 recruited**, six treatment cells. After removing participants who failed or skipped the attention check, 240 remained: truncated axis 37 control / 43 deceptive; area 40 / 40; aspect ratio 38 / 42.
- **Reversal experiment: 80 recruited**, 78 retained, 40 control / 38 deceptive.

Population is US-located Mechanical Turk workers in late 2014, not a general or representative public.

## Limits the authors state themselves

The paper has no Limitations section. What it does concede, in its own words:

> "This paper presents a first step in empirically studying deceptive visualizations, and will pave the way for more research in this direction."

> "Our analysis of the individual differences did not provide any conclusive information. However, some of the individual differences attributes seemed to have en effect for a particular type of chart. Further research is needed to disentangle the relationship between deception technique, chart type and individual differences. More precisely, it is necessary to understand if the effects depend on the chart type or only on distortion technique used."

> "While our study includes an elements that can be considered a proxy for literacy, e.g., chart familiarity, an objective measure of literacy may lead to more interesting results."

On the platform, they cite prior work rather than claim it away: "While conducting behavioral research based on self-reported measures on a crowdsourced platform may be considered problematic, several researchers have demonstrated the viability of MT as a reliable data collection platform."

They also scope the definition deliberately: the working definition of deceptive visualization is "designed with or without an intent to deceive," and they "do not explore the boundary of intentional vs. unintentional deceptiveness."

## What this result does not license

- **Do not cite 18.4% as a control-group error rate.** It is the deceptive group's *correct* rate. The control error rate is 2.5%.
- **Do not use this to rank distortion techniques.** Line/aspect-ratio produced the largest effect and bubble/area the smallest, but chart type and distortion are confounded one-to-one. The paper never varies distortion within a chart type.
- **Do not cite it as evidence that labeling values fixes distortion.** The opposite: values were printed on every chart and the effect appeared anyway. If anything this is evidence against the labeling remedy, which is [Correll 2020](correll-2020-truncating-the-y-axis.md)'s conclusion too.
- **Do not cite it as measuring "deception" in the intentional sense.** The construct measured is a shift in a rating-scale response, on a single trial, from a single chart, per participant.
- **Do not treat n=38 versus n=40 as a well-powered reversal experiment.** The effect is enormous and the test is exact, so the conclusion holds, but this is one chart in one scenario.
- **Do not extend the 129.5% figure to charts without printed values, to other domains, or to decision-making tasks.** It is a between-subjects difference in mean Likert response for one water-access scenario.

## Extraction trap

Table 2's "Distortion Technique" column is vertically centered across each control/deceptive pair, so `pdftotext -layout` shifts the technique labels down one row and appears to pair Bar with "Area as Quantity." The correct mapping is stated in the Methods text (truncated axis = bar, area = bubble, aspect ratio = line) and is confirmed by the Discussion's ordering of effect sizes ("the line chart is the one with the biggest effect, followed by the bars and then bubble"), which matches +129.5% > +91.0% > +58.5% only under the correct mapping.

## Links

- Authors' preprint PDF: [enrico.bertini.io/s/deceptive-chi2015.pdf](http://enrico.bertini.io/s/deceptive-chi2015.pdf)
- SSRN record: [abstract 2566968](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2566968)
- ACM DL: [10.1145/2702123.2702608](https://doi.org/10.1145/2702123.2702608)
- [refutations.md](../refutations.md), "A published paper that contradicts itself"
- [inventory.md](../inventory.md), topics 10 (axis truncation) and 11 (inverted axis)
- Related: [Correll 2020 on y-axis truncation](correll-2020-truncating-the-y-axis.md), which builds directly on this design
