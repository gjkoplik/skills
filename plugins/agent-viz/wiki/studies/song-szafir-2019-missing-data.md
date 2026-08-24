# Song & Szafir 2019: Where's My Data? Evaluating Visualizations with Missing Data

Hayeong Song, Danielle Albers Szafir. IEEE TVCG 25(1):914-924, January 2019. DOI [10.1109/TVCG.2018.2864914](https://doi.org/10.1109/TVCG.2018.2864914).

## What it is

Two crowdsourced studies, 303 participants total, measuring how 14 ways of drawing missing or imputed values in time series affect three things: response accuracy, perceived data quality, and confidence in the conclusion. It is the closest thing to a controlled experiment behind the rule that missing data should be shown as missing.

## Status

**`primary-read`.** PDF retrieved from the NSF Public Access Repository, [par.nsf.gov/servlets/purl/10111567](https://par.nsf.gov/servlets/purl/10111567), and re-extracted with `pdftotext -layout`. The lab's own project page at `cmci.colorado.edu/visualab/MissingData/` no longer serves the PDF at the obvious path.

Retrieval date: **2026-08-23**.

## What it is good for

[inventory.md](../inventory.md) topic 55 flags missing data as weakly sourced in the visualization canon, and this is the paper that fixes it. Come here for the ordering result, **highlighting beats downplaying beats removal**, and for the specific finding that removal can produce outright wrong answers when it breaks visual continuity. Also come here for the framing that "less reader confidence" is not automatically the goal.

## What it does not settle

Time series only, line graphs and bar charts only, low-stakes tasks, and a deliberately small slice of the imputation space. It also does not test the case a plotting library hits most often, which is a caller who never noticed rows were dropped at all.

## The finding

The paper's own four-bullet summary:

> - "Perceived data quality and confidence generally degrade as the amount of missing data increases."
> - "Data visualized by highlighting missing values tends to be seen as higher quality than downplay or information removal."
> - "Information removal can significantly degrade perceptions of data quality, and confidence. These methods even lead to incorrect responses if missing values break the visual continuity of a visualization."
> - "Linear interpolation leads to higher perceptions of quality and confidence in analysis."

The third bullet is the one carrying a hard consequence. Everything else on the list is about perception; that one is about **accuracy**. Silently dropping a point is not a neutral act when the surrounding mark implies continuity.

Two structural results are more useful than the headline.

**Continuity, not uncertainty-marking, is what the encoding has to preserve.** Error bars helped when connected and hurt when not:

> "we found that error bars that do not preserve continuity -- disconnected error bars in line graphs and point with errors bars in bar charts -- lead to low perceived confidence, credibility, and data quality, which indicate critical factors beyond the integration of uncertainty."

So "annotate the imputed values with uncertainty" is underspecified as advice. The same annotation helps or hurts depending on whether it breaks the line.

**Zero-filling is the worst imputation method tested.** Linear interpolation and marginal means both produced higher accuracy than zero-filling. Zero-filling is also the default behavior of a great many aggregation pipelines, which is why this result travels.

## Method

Two studies, each a 7 (visualization type) × 3 (imputation method) × 4 (percentage of missing data) full factorial, within-participants. Study one used line graphs, study two used bar charts. Imputation methods were ad-hoc zero-filling, local linear interpolation, and marginal means. Missing-data levels included a 0% control.

The seven line-graph conditions spanned four categories: highlight (bright color on imputed points), downplay (reduced salience, unfilled points, gaps in the line), annotation (error bars, connected and disconnected), and information removal. The seven bar-chart conditions mapped the same categories onto bars: color bars, bars with error bars, gradient bars, sketched bars, dashed outlines, and simply not drawing the value.

Tasks were average estimation and trend detection ("which half-hour had the larger overall rate of change"), plus five subjective questions per stimulus covering completeness, credibility and reliability. Perceived completeness and reliability correlated strongly (Cronbach's α > 0.70), so the two were combined into a data-quality scale.

Participants were screened for color vision deficiency with four Ishihara plates, given a tutorial explaining that some values were "guessed," and required to pass engagement checks. They were **not** told which imputation method was used.

## Sample size and population

**303 U.S. participants on Amazon Mechanical Turk** across four experiments (66, 80, 80, 77). Exclusions were reported per experiment; the 66-participant line-graph experiment dropped two, the bar-chart trend experiment dropped three.

## Limits the authors state themselves

They are unusually explicit that degrading confidence is not the universal goal:

> "While we commonly expect that missing data should optimally degrade perceived quality, there are many cases that run counter to this assumption. For example, we may not wish to degrade perceived quality when we can closely approximate missing values or when quality may interfere with decision speed in low-risk scenarios."

and

> "Whether ideal perceptions of quality are high or low is likely dependent on parameters of the data, problem, and domain."

That matters for how the result becomes a rule. This paper supports "the encoding choice moves perceived quality in a predictable direction." It does not support "always maximize visible doubt."

Their stated limitations:

> "Our narrative scenario used familiar but simple and low-risk tasks (i.e., the cost of getting the wrong answer is minimal). While these choices allowed us strong control over our tested conditions to encourage general understanding, future testing should extend our work to real-world datasets and scenarios."

> "we tested a small set of possible imputation and visualization methods, drawing inspiration from visualization tools that actively manage missing data. However, we found few tools explicitly discuss missing data management."

They also want future work on "more subtle amounts of missing data" and on multiple imputation and machine-learning-based methods, neither of which was tested.

The authors describe their own contribution as "preliminary evidence" and "preliminary guidance" more than once. That is the right weight to give it. It is a real experiment and it is the only one of its kind in this cluster, which is a statement about the field's coverage rather than about the paper's strength.

One conflict they surface themselves: the finding that highlighting is preferred "runs somewhat contrary to prior work on preference in decision support" (Andreasson & Riveiro 2014). They reconcile it with the visual-selection and trust literature rather than dismissing the earlier result.

## Links

- Open copy: [par.nsf.gov/servlets/purl/10111567](https://par.nsf.gov/servlets/purl/10111567)
- [inventory.md](../inventory.md), topics 55 (missing data is shown as missing) and 56, both flagged there as thin
- [checks/matplotlib.md](../checks/matplotlib.md) for the mechanizable version: compare input row count to plotted point count
- [weissgerber-2015-beyond-bar-line.md](weissgerber-2015-beyond-bar-line.md), the other paper in this cluster about a figure hiding what the reader would need to evaluate it
