---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Romano, Sotis, Dominioni & Guidi 2020: The scale of COVID-19 graphs affects understanding, attitudes, and policy preferences

Alessandro Romano, Chiara Sotis, Goran Dominioni, Sebastián Guidi. *Health Economics* 29(11), 1482-1494, 2020. DOI [10.1002/hec.4143](https://doi.org/10.1002/hec.4143). Open access, CC-BY.

A randomized survey experiment on about 2,000 US residents, run in April 2020. Half saw cumulative COVID-19 deaths on a linear axis, half saw the identical data on a log axis, taken from the worldometers.info charts people were actually reading at the time. The paper then measures comprehension, forecast accuracy, worry, and policy preferences.

**How this was read.** Extracted locally with `pdftotext` from the published open-access version deposited at LSE Research Online. Retrieval date: **2026-08-23**.

Format note: this is a **Health Economics Letter**, the journal's short form, not a full research article. That shapes what is and is not in it.

## What it is good for

- Extending the log-scale comprehension problem from experts (see [Menge et al. 2018](menge-2018-log-scales.md)) to the **general public on real, high-salience data**.
- The one study showing scale choice moving **downstream attitudes and policy preferences**, not just comprehension.
- A defensible source for **"linear as the default"** in public communication, phrased the way the authors phrase it.

## What it does not settle

Whether the effect replicates. The paper itself names a contemporaneous study that found nothing, and its own effect sizes on the comprehension items are implausibly enormous. Both are covered below.

---

## The finding

From the abstract:

> "we find that when we show the number of COVID-19 related deaths on a logarithmic scale, people have a less accurate understanding of how the pandemic has developed, make less accurate predictions on its evolution, and have different policy preferences than when they are exposed to a linear scale."

And the recommendation, whose closing hedge keeps it from being a ban:

> "mass media and policymakers communicating to the general public should always describe the evolution of the pandemic using a graph on a linear scale, at least as a default option."

### Comprehension (Table 2, logit)

Being in the Linear Group predicted a correct answer on both comprehension items:

| Item | Coefficient (1) | With controls (2) |
|---|---|---|
| Q1, real COVID-19 data | 2.021*** (p = 0.000) | 2.054*** (p = 0.000) |
| Q2, hypothetical "Infection Z" | 4.634*** (p = 0.000) | 4.819*** (p = 0.000) |

n = 2,074 for the uncontrolled columns, 1,830 with controls.

As odds ratios (Table 7): **7.800** for Q1 (SE 0.902) and **123.9** for Q2 (SE 23.13).

### Prediction accuracy (Table 3, logit)

Linear Group coefficient 0.489*** for making an *accurate* prediction and -0.481*** for making an *unreasonable* one, both p = 0.000, n = 2,074. Odds ratios 1.619 and 0.619.

"Accurate" means inside the 95% CI of an ARIMA(0,2,1) forecast of US deaths on 25 April; "unreasonable" means outside the 99% CI. The ARIMA predicted 55,791 against an actual 54,256, so the benchmark held up.

### Policy and attitudes

Effects are real but modest and inconsistent in sign across outcomes. Support for closing nonessential businesses: -0.378** and -0.424** for the Linear Group (p = 0.019, 0.012). Days until reopening: +17.38** and +14.65** (p = 0.014, 0.037). So the linear group wanted businesses closed *longer* while endorsing the closure policy *less*. Odds ratios in Table 7 for worry, mask use, mask tax and business closure all carry p values above 0.10.

The authors are candid about not knowing the mechanism:

> "We cannot know the mechanism leading to these preferences, but we advance the conjecture that the shape of the curves could explain these findings. The flat logarithmic curve can give the impression that we reached a plateau and that, while the present situation is very serious, things are about to get better soon."

## Method

Double-blind randomized experiment, approved by the Yale IRB, fielded 18 April 2020. Respondents recruited through Cloud Research. Random assignment to the Linear Group or the Log Group; the two groups saw identical underlying data.

Question order was deliberate and matters:

> "To increase external validity and to avoid priming respondents, we ask attitudes and policy preferences before testing understanding."

Three comprehension probes: (1) with the assigned COVID-19 chart in front of them, whether deaths increased more between 31 March and 6 April or between 6 and 12 April; (2) the same style of question about a hypothetical "Infection Z," taken from Okan, Galesic & Garcia-Retamero 2016, to test whether prior COVID knowledge rather than scale reading was doing the work; (3) a numeric forecast of total US deaths one week out. Confidence was collected for each.

Analysis is ordered logit and logit with demographic controls (worry, news checking, education, gender, age, party).

## Sample size and population

> "We recruited a sample of approximately n ≈ 2000 (after exclusion criteria, with no regression with less than 1825 observations) U.S. residents on Cloud Research."

Regression n ranges from 1,825 to 2,074 depending on specification. Population is US residents on an online panel in mid-April 2020. Demographics are in Table 1.

## Limits the authors state themselves

**There is no Limitations section.** This is a Letter. What the authors do put on the record:

They name a study that contradicts them, in the introduction:

> "Another study (Ryan & Evers, 2020) carried out a week after ours, confirms our finding that the scale of the graph affects policy preferences and that people have problems understanding logarithms. Instead, a study with Canadian respondents finds that the scale of the graph has no impact on respondents (Sevi et al., 2020)."

And they push back on it in an endnote rather than dismissing it:

> "However, their study uses a 'catch all' question for pessimism and one on policy preferences. These catch all questions might be unable to capture the nuanced impact of graph scale on policies and attitudes that we observe. For instance, we observe an impact on worry for the health crisis, but not on worry for the economic crisis."

They hedge the mechanism ("We cannot know the mechanism"), and they hedge the recommendation ("at least as a default option").

## What this result does not license

- **Not "never use log scales."** The recommendation is scoped to mass media and policymakers communicating COVID-19 case and death curves to the general public, and even there it says "as a default option."
- **Not a general finding about log axes in analysis, science, or technical charts.** The stimulus is one specific chart type, cumulative deaths, at a specific moment when the log curve happened to look flat. The authors' own conjecture ties the effect to that shape.
- **Not a settled effect.** One contemporaneous study on Canadian respondents found no impact, and the paper says so itself. Cite Romano and Sevi together or cite neither.
- **Do not quote the odds ratios as effect magnitudes without flagging them.** An odds ratio of **123.9** on the hypothetical-infection comprehension item is not a normal social-science effect size. It most likely reflects a near-floor correct rate in the log condition rather than a stable estimate. The coefficient (4.8 on the log-odds scale) is the safer number, and the raw percentages live only in Figure 2, which is a bar chart and cannot be read out of the PDF text.
- **Do not cite it for "log scales caused worse COVID policy."** The policy coefficients point in mixed directions, several are not significant, and the paper offers a conjecture rather than a mechanism.
- **Not evidence about people who chose to look at a log chart.** Assignment was random. Self-selected log-chart readers are a different population.

## Links

- Publisher: [doi.org/10.1002/hec.4143](https://doi.org/10.1002/hec.4143)
- Open-access deposit used here: [eprints.lse.ac.uk/106217](http://eprints.lse.ac.uk/106217/1/Sotis_scale_of_covid_19_graphs_affects_understanding_published.pdf)
- Earlier preprint of the same work: SSRN [3588511](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3588511) and PsyArXiv [10.31234/osf.io/42xfm](https://doi.org/10.31234/osf.io/42xfm), both titled "COVID-19 Data: The Logarithmic Scale Misinforms the Public and Affects Policy Preferences"
- [refutations.md](../refutations.md), "Log scales are fine for expert audiences"
- [inventory.md](../inventory.md), topic 12 (log and other nonlinear scales)
- Related: [Menge et al. 2018](menge-2018-log-scales.md), the expert-audience counterpart, cited by this paper
