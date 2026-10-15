---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Song & Szafir 2019: Where's My Data? Evaluating Visualizations with Missing Data

Hayeong Song, Danielle Albers Szafir. IEEE TVCG 25(1):914-924, January 2019. DOI [10.1109/TVCG.2018.2864914](https://doi.org/10.1109/TVCG.2018.2864914).

Two crowdsourced studies, 303 participants total, on how 14 ways of drawing missing or imputed values in time series affect response accuracy, perceived data quality and confidence. It is the closest thing to a controlled experiment behind the rule that missing data should be shown as missing.

**How this was read.** PDF from the NSF Public Access Repository, [par.nsf.gov/servlets/purl/10111567](https://par.nsf.gov/servlets/purl/10111567), re-extracted with `pdftotext -layout`. The lab's project page at `cmci.colorado.edu/visualab/MissingData/` no longer serves the PDF at the obvious path.

## What it is good for

Evidence for [inventory.md](../inventory.md) topic 55, which the visualization canon sources weakly. It carries the ordering **highlighting beats downplaying beats removal**, and the finding that removal can produce wrong answers when it breaks visual continuity.

## What it does not settle

It covers time series, line and bar charts, low-stakes tasks and a small slice of the imputation space. It does not test the case a plotting library hits most often, a caller who never noticed rows were dropped.

## The finding

The paper's own four-bullet summary:

> - "Perceived data quality and confidence generally degrade as the amount of missing data increases."
> - "Data visualized by highlighting missing values tends to be seen as higher quality than downplay or information removal."
> - "Information removal can significantly degrade perceptions of data quality, and confidence. These methods even lead to incorrect responses if missing values break the visual continuity of a visualization."
> - "Linear interpolation leads to higher perceptions of quality and confidence in analysis."

Only the third bullet is about accuracy. Silently dropping a point is not neutral when the surrounding mark implies continuity.

Error bars helped when connected and hurt when not, so continuity, not uncertainty-marking, is what the encoding has to preserve:

> "we found that error bars that do not preserve continuity -- disconnected error bars in line graphs and point with errors bars in bar charts -- lead to low perceived confidence, credibility, and data quality, which indicate critical factors beyond the integration of uncertainty."

Zero-filling was the worst imputation method tested, with lower accuracy than linear interpolation or marginal means. It is also a common default in aggregation pipelines, which no source here has measured.

## Method

Two studies, each a 7 (visualization type) × 3 (imputation method) × 4 (percentage of missing data) within-participants full factorial: line graphs in study one, bar charts in study two. Imputation was ad-hoc zero-filling, local linear interpolation or marginal means, and missing-data levels included a 0% control.

The conditions fell into four categories: highlight (bright color on imputed points), downplay (reduced salience, unfilled points, gaps in the line), annotation (connected and disconnected error bars), and information removal. On bars these became color bars, bars with error bars, gradient bars, sketched bars, dashed outlines, and not drawing the value.

Tasks were average estimation and trend detection ("which half-hour had the larger overall rate of change"), plus five subjective questions per stimulus on completeness, credibility and reliability. Completeness and reliability correlated strongly (Cronbach's α > 0.70) and were combined into a data-quality scale. Participants passed four Ishihara plates for color vision and engagement checks, were told some values were "guessed," and were not told the imputation method.

## Sample size and population

303 U.S. participants on Amazon Mechanical Turk across four experiments (66, 80, 80, 77). Exclusions were reported per experiment: the 66-participant line-graph experiment dropped two, the bar-chart trend experiment three.

## Limits the authors state themselves

On whether degraded confidence is the goal:

> "While we commonly expect that missing data should optimally degrade perceived quality, there are many cases that run counter to this assumption. For example, we may not wish to degrade perceived quality when we can closely approximate missing values or when quality may interfere with decision speed in low-risk scenarios."

> "Whether ideal perceptions of quality are high or low is likely dependent on parameters of the data, problem, and domain."

Their stated limitations:

> "Our narrative scenario used familiar but simple and low-risk tasks (i.e., the cost of getting the wrong answer is minimal). While these choices allowed us strong control over our tested conditions to encourage general understanding, future testing should extend our work to real-world datasets and scenarios."

> "we tested a small set of possible imputation and visualization methods, drawing inspiration from visualization tools that actively manage missing data. However, we found few tools explicitly discuss missing data management."

They call for work on "more subtle amounts of missing data" and on multiple imputation and machine-learning-based methods, none tested, and describe their contribution as "preliminary evidence" and "preliminary guidance." The preference for highlighting "runs somewhat contrary to prior work on preference in decision support" (Andreasson & Riveiro 2014), which they reconcile with the visual-selection and trust literature rather than dismiss.

## What this result does not license

- **Not "always maximize visible doubt."** The paper supports "the encoding choice moves perceived quality in a predictable direction."
- **Not "annotate the imputed values with uncertainty" as a complete rule.** The same annotation helps or hurts depending on whether it breaks the line.
- **Not a mature evidence base.** The authors call it preliminary, and it is the only experiment of its kind in this cluster. The tasks were low-risk.

## Links

- Open copy: [par.nsf.gov/servlets/purl/10111567](https://par.nsf.gov/servlets/purl/10111567)
- [inventory.md](../inventory.md), topics 55 (missing data is shown as missing) and 56, both flagged there as thin
- [checks/matplotlib.md](../checks/matplotlib.md): the mechanizable version, input row count against plotted point count
- [weissgerber-2015-beyond-bar-line.md](weissgerber-2015-beyond-bar-line.md): the other paper in this cluster about a figure hiding what the reader would need to evaluate it
