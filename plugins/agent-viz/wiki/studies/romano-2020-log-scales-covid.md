---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Romano, Sotis, Dominioni & Guidi 2020: The scale of COVID-19 graphs affects understanding, attitudes, and policy preferences

Alessandro Romano, Chiara Sotis, Goran Dominioni, Sebastián Guidi. *Health Economics* 29(11), 1482-1494, 2020. DOI [10.1002/hec.4143](https://doi.org/10.1002/hec.4143). Open access, CC-BY.

A randomized survey experiment on about 2,000 US residents in April 2020. Half saw cumulative COVID-19 deaths on a linear axis and half on a log axis, using the worldometers.info charts of the time. It is a **Health Economics Letter**, the journal's short form, with no limitations section.

**What it is good for.** Extending the log-scale comprehension problem from experts ([Menge et al. 2018](menge-2018-log-scales.md)) to the **general public on real, high-salience data**. The one study showing scale moving **attitudes and policy preferences**. A source for **"linear as the default"** in public communication.

**What it does not settle.** Replication. The paper names a contemporaneous null result, and its comprehension effect sizes are implausibly large.

**How this was read.** Extracted locally with `pdftotext` from the published open-access version deposited at LSE Research Online.

## The finding

> "we find that when we show the number of COVID-19 related deaths on a logarithmic scale, people have a less accurate understanding of how the pandemic has developed, make less accurate predictions on its evolution, and have different policy preferences than when they are exposed to a linear scale."

> "mass media and policymakers communicating to the general public should always describe the evolution of the pandemic using a graph on a linear scale, at least as a default option."

### Comprehension (Table 2, logit)

Linear Group coefficients, correct answer:

| Item | Coefficient (1) | With controls (2) |
|---|---|---|
| Q1, real COVID-19 data | 2.021*** (p = 0.000) | 2.054*** (p = 0.000) |
| Q2, hypothetical "Infection Z" | 4.634*** (p = 0.000) | 4.819*** (p = 0.000) |

n = 2,074 uncontrolled, 1,830 with controls. Odds ratios (Table 7): **7.800** for Q1 (SE 0.902), **123.9** for Q2 (SE 23.13).

### Prediction accuracy (Table 3, logit)

Linear Group coefficient 0.489*** for an *accurate* prediction and -0.481*** for an *unreasonable* one, both p = 0.000, n = 2,074, odds ratios 1.619 and 0.619. "Accurate" means inside the 95% CI of an ARIMA(0,2,1) forecast of US deaths on 25 April; "unreasonable" means outside the 99% CI. The ARIMA predicted 55,791 against an actual 54,256, so the benchmark held.

### Policy and attitudes: modest, mixed in sign

Support for closing nonessential businesses: -0.378** and -0.424** (p = 0.019, 0.012). Days until reopening: +17.38** and +14.65** (p = 0.014, 0.037). The linear group wanted closures *longer* while endorsing them *less*. Table 7 odds ratios for worry, mask use, mask tax and business closure all have p above 0.10.

> "We cannot know the mechanism leading to these preferences, but we advance the conjecture that the shape of the curves could explain these findings. The flat logarithmic curve can give the impression that we reached a plateau and that, while the present situation is very serious, things are about to get better soon."

## Method

Double-blind, Yale IRB, fielded 18 April 2020 through Cloud Research.

> "To increase external validity and to avoid priming respondents, we ask attitudes and policy preferences before testing understanding."

Respondents judged whether deaths rose more from 31 March to 6 April or from 6 to 12 April, then answered the same question for a hypothetical "Infection Z" (Okan, Galesic & Garcia-Retamero 2016) to rule out prior knowledge, then forecast US deaths a week out. Each answer had a confidence rating. Models control for worry, news checking, education, gender, age and party.

## Sample size and population

> "We recruited a sample of approximately n ≈ 2000 (after exclusion criteria, with no regression with less than 1825 observations) U.S. residents on Cloud Research."

Demographics are in Table 1.

## Limits the authors state themselves

> "Another study (Ryan & Evers, 2020) carried out a week after ours, confirms our finding that the scale of the graph affects policy preferences and that people have problems understanding logarithms. Instead, a study with Canadian respondents finds that the scale of the graph has no impact on respondents (Sevi et al., 2020)."

An endnote answers the null result:

> "However, their study uses a 'catch all' question for pessimism and one on policy preferences. These catch all questions might be unable to capture the nuanced impact of graph scale on policies and attitudes that we observe. For instance, we observe an impact on worry for the health crisis, but not on worry for the economic crisis."

## What this result does not license

- **Not "never use log scales."** The recommendation covers COVID-19 curves shown to the general public, "as a default option."
- **Not a finding about log axes in technical charts.** The stimulus was cumulative deaths while the log curve looked flat, the shape the authors' conjecture blames.
- **Not a settled effect.** A contemporaneous Canadian study found no impact.
- **Not odds ratios as plain magnitudes.** An odds ratio of **123.9** most likely reflects a near-floor correct rate in the log condition. The log-odds coefficient (4.8) is safer. Raw percentages are only in Figure 2, a bar chart unreadable from the PDF text.
- **Not "log scales caused worse COVID policy."** The policy coefficients are mixed in direction, several are not significant, and the mechanism is a conjecture.
- **Not evidence about people who chose a log chart.** Assignment was random.

## Links

- Publisher: [doi.org/10.1002/hec.4143](https://doi.org/10.1002/hec.4143)
- LSE deposit: [eprints.lse.ac.uk/106217](http://eprints.lse.ac.uk/106217/1/Sotis_scale_of_covid_19_graphs_affects_understanding_published.pdf)
- Preprints, both titled "COVID-19 Data: The Logarithmic Scale Misinforms the Public and Affects Policy Preferences": SSRN [3588511](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3588511), PsyArXiv [10.31234/osf.io/42xfm](https://doi.org/10.31234/osf.io/42xfm)
- [refutations.md](../refutations.md), "Log scales are fine for expert audiences"
- [inventory.md](../inventory.md), topic 12 (log and other nonlinear scales)
- [Menge et al. 2018](menge-2018-log-scales.md): the expert-audience counterpart
