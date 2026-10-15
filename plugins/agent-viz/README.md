# agent-viz

A quality bar for figures, written for coding agents, plus the research it came from.

Most visualization advice is written for humans, and most rubrics grade a finished chart. Neither covers the moment an agent is about to draw something, or is handed a dataset and asked which chart to use. This plugin does both.

## Install

```
/plugin marketplace add gjkoplik/skills
/plugin install agent-viz@gjkoplik
```

This is one plugin inside the [gjkoplik/skills](https://github.com/gjkoplik/skills) monorepo. Paths below are relative to `plugins/agent-viz/`.

The skill loads by description when you are about to produce or review a figure, and can be invoked directly as `/agent-viz`.

## What's here

**[The skill](SKILL.md)** is the bar itself. Three ideas do most of the work:

- **A floor and a ceiling.** Quantitative honesty, statistical honesty and accessibility bind on every figure. Narrative titles, emphasis palettes and annotation scale with the figure's job. A deliberately minimal figure that clears the floor is correct, not unfinished, which is what stops a review of a two-line API demo from reading as forty violations.
- **A chart-chooser routine.** Name the reader's question, route it to one data relationship, open that index before any chart page, and say how hard to push: floor violations stay firm, form suggestions are offered once and let go.
- **Confidence labels.** Rules backed by an experiment are stated flatly. Design conventions the evidence contests are stated as defaults with their exceptions named. Nothing is upgraded from convention to finding.

**[The wiki](wiki/)** is the research, kept so it does not have to be redone. One page per source, per study and per author, each recording whether anyone opened the primary and how. The skill routes into it at decision time.

- [chart-types/](wiki/chart-types/README.md): one page per chart type, grouped by index pages for each data relationship (magnitude, ranking, part-to-whole, distribution, correlation, change over time, deviation, spatial, flow, network, tables, qualitative). Each type page says when the form applies, what it costs in perceptual terms, what has been measured about it, and which justifications hold up. [aliases.md](wiki/chart-types/aliases.md) resolves a chart name to its page.
- [refutations.md](wiki/refutations.md): widely repeated rules that changed, weakened or died when someone opened the primary source, with quotes.
- [inventory.md](wiki/inventory.md): the topics a general figure bar owes, derived from the canon, each with a mechanizable-or-judgment verdict and its evidence class. [roll-call.md](wiki/roll-call.md) maps every chapter of every source onto it.
- [sources/](wiki/sources/), [studies/](wiki/studies/), [people/](wiki/people/): what each is good for and where its authority stops.
- [concepts/](wiki/concepts/): the floor-and-ceiling split, the evidence-class discipline, and the perceptual channels the chart pages inherit from.
- [checks/matplotlib.md](wiki/checks/matplotlib.md): runnable versions of the mechanizable rules, every snippet executed against a real figure.

## A sample of what the research found

- **"Bank to 45 degrees" is scope-limited, not general.** A replication with a wider design found slope-ratio error is "not minimized around 45°". The original result holds inside the moderate regime it tested.
- **Axis-break glyphs did not measurably fix truncation.** The tested designs produced no significant reduction in the exaggeration, which persists "even when participants make accurate reports of the numbers they observe."
- **The flat dual-axis ban has no experiment behind it.** The paper usually cited studied dual-*scale* focus-plus-context charts, not two variables on two axes.
- **"Log scales are fine for experts" does not hold.** 623 professional ecologists scored 56% on log-log against 93% on linear-linear.
- **Pies are not read by angle.** The one study that isolated the three cues found angle the least used. Bars still beat pies for value extraction; the usual mechanism given for it does not hold.
- **"Gray plus one accent" has no controlled study behind it.** It is a good default and it is authority-asserted.

## Known gaps

Stated in the wiki rather than hidden. Several canonical sources, Tufte and Munzner among them, were reached only in secondary form. Most chart types have no study that tests the form itself, and their pages say so instead of filling the gap with practitioner advice. The accessibility topics duplicate part of [Chartability](https://chartability.fizz.studio/), which should be imported rather than re-derived. The runnable checks exist for matplotlib only.

## License

MIT. The research files cite their sources; where a third-party work is quoted, the quote is attributed inline.
