---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Pandey et al. 2015: How Deceptive are Deceptive Visualizations?

Anshul Vikram Pandey, Katharina Rall, Margaret L. Satterthwaite, Oded Nov, Enrico Bertini. *How Deceptive are Deceptive Visualizations?: An Empirical Analysis of Common Distortion Techniques.* CHI 2015, pp. 1469-1478. DOI [10.1145/2702123.2702608](https://doi.org/10.1145/2702123.2702608).

The first controlled experiment on how far four distortions move a reader's interpretation: truncated axis (bar chart), area as quantity (bubble chart), aspect ratio (line chart) and inverted axis (line-area chart). Crowdsourced on Mechanical Turk.

**What it is good for.** A magnitude, 58.5% to 129.5%, for how far distortion moves a Likert judgment with the true values printed on the chart. A demonstration that an inverted axis reverses conclusions that a control group gets right.

**What it does not settle.** Why. The individual-differences analysis was a stated goal and found nothing:

> "Despite our expectations the analysis on individual differences did not provide definite conclusions."

**How this was read.** Extracted locally with `pdftotext` from the authors' preprint at [enrico.bertini.io/s/deceptive-chi2015.pdf](http://enrico.bertini.io/s/deceptive-chi2015.pdf), which is also NYU School of Law Public Law & Legal Theory Working Paper 15-03 and carries the line "Preprint of the full paper published at ACM CHI 2015." The ACM camera-ready was paywalled, so no number here is cross-checked against it. Table 2's "Distortion Technique" column is vertically centered across each control/deceptive pair, so `pdftotext -layout` shifts the labels down a row and appears to pair Bar with "Area as Quantity." The correct mapping is stated in the Methods text (truncated axis = bar, area = bubble, aspect ratio = line) and is confirmed by the Discussion's ordering of effect sizes ("the line chart is the one with the biggest effect, followed by the bars and then bubble"), which matches +129.5% > +91.0% > +58.5% only under the correct mapping.

## The finding

### Message exaggeration

Table 2, mean response on a 1-to-5 Likert scale to a "how much bigger" question:

| Chart | Distortion | Control | Deceptive | Increase |
|---|---|---|---|---|
| Line | Aspect ratio | 1.39, 95% CI [1.23, 1.55] | 3.19, 95% CI [2.76, 3.62] | +129.5% |
| Bar | Truncated axis | 1.45, 95% CI [1.27, 1.62] | 2.77, 95% CI [2.26, 3.28] | +91.0% |
| Bubble | Area as quantity | 1.71, 95% CI [1.45, 1.98] | 2.71, 95% CI [2.27, 3.15] | +58.5% |

The Discussion's summary recomputes exactly (3.19/1.39 = 2.295, 2.71/1.71 = 1.585):

> "the distorted charts lead to responses between 58.5% and 129.5% bigger than the control condition."

Mann-Whitney U, one-tailed: aspect ratio U = 1409, Z = 5.88, p < 0.0001, r = 0.66; area U = 1121, Z = 3.08, p = 0.0007, r = 0.34; truncated axis U = 1144, Z = 3.36, p = 0.0003, r = 0.37.

### Message reversal

Table 3, the inverted-axis condition:

| Treatment | Selected | Correct | Incorrect | Uncertain |
|---|---|---|---|---|
| Control | 40 | 39 (97.50%) | 1 (2.5%) | 0 |
| Deceptive | 38 | 7 (18.42%) | 30 (78.95%) | 1 (0.02%) |

Freeman-Halton extension of Fisher's Exact Test, p < 0.0001. The deceptive Uncertain cell is reproduced as the paper's own Table 3 prints it, and the paper misprints it: 1/38 is 2.63%, which makes the row sum to 100%.

## The Discussion misstates Table 3

> "the deceptive condition led to 97.5% incorrect responses whereas the control condition led to only 18.4% incorrect responses"

That sentence takes the two correct-column percentages, labels them incorrect, and swaps the conditions. The Results text agrees with the table:

> "Out of the 38 selected participants who saw the deceptive visualization, 30 responded incorrectly, 7 correctly and one chose the uncertain response. For the 40 participants who saw the control condition, 39 responded correctly, 1 responded incorrectly and no participant reported uncertainty."

The control error rate is 2.5%. The error preserves direction, so the conclusion stands. A search found no secondary source repeating 97.5%/18.4%.

## Method

Between-subjects, with self-reported US workers at an approval rate of 99% or more, paid $0.30 for 5-10 minutes. Around the treatment: demographics, a visual ability test, a 5-point chart familiarity test, an attention check and the 18-item Need for Cognition short scale.

Exaggeration was a "how much" question on a 5-point Likert scale:

> "How much better do you think the condition of safe drinking water access in Silvatown is as compared to that in Wilowtown?"

Reversal was measured by a "what" question with three choices: a correct interpretation, the interpretation the distortion pushes toward, and "I do not know."

The true values were on every chart, so the effect is not a failure to read numbers:

> "in each of the presented treatments, the actual numbers/data were presented on the chart as we were interested in detecting deception due to visual representation even in the presence of accurate data."

Two pilots, on a real-world deceptive chart and on synthetic data, found no noticeable difference between real and artificial scenarios.

## Sample size and population

- **330 unique participants**, US-located Mechanical Turk workers in late 2014, not a representative public.
- **Exaggeration:** 250 recruited into six cells, 240 left after the attention check. Truncated axis 37 control / 43 deceptive; area 40 / 40; aspect ratio 38 / 42.
- **Reversal:** 80 recruited, 78 retained, 40 control / 38 deceptive.

## Limits the authors state themselves

The paper has no Limitations section. What it concedes:

> "This paper presents a first step in empirically studying deceptive visualizations, and will pave the way for more research in this direction."

> "Our analysis of the individual differences did not provide any conclusive information. However, some of the individual differences attributes seemed to have en effect for a particular type of chart. Further research is needed to disentangle the relationship between deception technique, chart type and individual differences. More precisely, it is necessary to understand if the effects depend on the chart type or only on distortion technique used."

> "While our study includes an elements that can be considered a proxy for literacy, e.g., chart familiarity, an objective measure of literacy may lead to more interesting results."

On the platform, they cite prior work:

> "While conducting behavioral research based on self-reported measures on a crowdsourced platform may be considered problematic, several researchers have demonstrated the viability of MT as a reliable data collection platform."

A deceptive visualization is defined as one "designed with or without an intent to deceive," and they "do not explore the boundary of intentional vs. unintentional deceptiveness."

## What this result does not license

- **Not 18.4% as a control error rate.** It is the deceptive group's correct rate.
- **Not a ranking of distortions.** Each exaggeration condition changes chart type and distortion together, one-to-one.
- **Not support for labeling values as the fix.** Values were printed and the effect appeared anyway. [Correll 2020](correll-2020-truncating-the-y-axis.md) points the same way.
- **Not intentional deception.** The construct is a shift in one rating, on one chart, per participant.
- **Not general.** The reversal is one chart in one scenario, at n=38 versus n=40. The 129.5% is a mean Likert difference for one water-access scenario and carries to no other domain or decision task.

## Links

- Authors' preprint PDF: [enrico.bertini.io/s/deceptive-chi2015.pdf](http://enrico.bertini.io/s/deceptive-chi2015.pdf)
- SSRN record: [abstract 2566968](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2566968)
- ACM DL: [10.1145/2702123.2702608](https://doi.org/10.1145/2702123.2702608)
- [refutations.md](../refutations.md), "A published paper that contradicts itself"
- [inventory.md](../inventory.md), topics 10 (axis truncation) and 11 (inverted axis)
- [Correll 2020 on y-axis truncation](correll-2020-truncating-the-y-axis.md), which builds directly on this design
