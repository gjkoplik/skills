# agent-viz

A quality bar for figures, written for coding agents, plus the research it came from.

There is a lot of visualization advice in the world and almost all of it is written for humans. There is also a growing pile of rubrics for *grading* a finished chart. What there was not, when this was put together, is guidance aimed at the moment an agent is about to draw something. That gap is what this repo is for.

## Install

```
/plugin marketplace add gjkoplik/agent-viz
/plugin install agent-viz
```

The skill loads by description when you are about to produce or review a figure, and can be invoked directly as `/agent-viz`.

## What's here

**[The skill](SKILL.md).** The bar itself. Two ideas do most of the work:

*A floor and a ceiling.* Quantitative honesty, statistical honesty and accessibility bind on **every** figure. Narrative titles, emphasis palettes and annotation scale with the figure's job. A deliberately minimal figure that clears the floor is **correct**, not unfinished, which matters because the alternative produces review that reads as forty violations against a two-line API demo.

*Confidence labels.* Rules backed by an experiment are stated flatly. Design conventions the evidence contests are stated as defaults with their exceptions named. Nothing is upgraded from convention to finding.

**[The wiki](wiki/).** The research, kept so it does not have to be redone. **41 pages**: one per source, one per study, plus the synthesis. 27 are `primary-read`, meaning someone opened the actual source and quotes come from a local extraction. 5 are `secondary-only` and say so.

- [inventory.md](wiki/inventory.md): 92 topics a general figure bar owes, derived from the canon by an agent working blind to any existing bar, each with a mechanizable-or-judgment verdict and its evidence class.
- [refutations.md](wiki/refutations.md): the highest-value page. Widely repeated rules that changed, weakened or died when someone opened the primary source, with quotes.
- [roll-call.md](wiki/roll-call.md): the audit trail. Every chapter of every source mapped to a topic or to a stated exclusion, plus the four errors the per-source pages found in it.
- [sources/](wiki/sources/): 16 pages. What each source is *actually good for*, and where it is contested.
- [studies/](wiki/studies/): 16 pages. Each with the finding, the method, the sample, and the limits the authors state themselves.
- [concepts/](wiki/concepts/): the two ideas that took the research to arrive at.
- [checks/matplotlib.md](wiki/checks/matplotlib.md): runnable versions of the mechanizable rules, every snippet executed against a real figure.

## A sample of what the research found

- **"Bank to 45 degrees" is scope-limited, not general.** A replication with a wider experimental design found slope-ratio error is "not minimized around 45°", and that the original result holds only within the moderate regime it tested.
- **Axis-break glyphs did not measurably fix truncation.** The remedy everyone recommends was tested and produced no significant difference in perceived severity. Truncation's exaggeration persists "even when participants make accurate reports of the numbers they observe."
- **The flat dual-axis ban has no experiment behind it.** The paper usually cited studied dual-*scale* focus-plus-context charts, not dual-*variable* twin axes.
- **"Log scales are fine for experts" does not hold.** 623 professional ecologists scored 56% on log-log against 93% on linear-linear.
- **A widely cited deception paper contradicts itself.** Its table and its discussion disagree about which condition produced which error rate, and the discussion's figure is off by roughly 7x. The conclusion survives; the number does not.
- **"Gray plus one accent" has no controlled study behind it.** It is a good default and it is authority-asserted. That is worth knowing before treating it as evidence.

## Two hazards worth stealing

Both were caught only by cross-checking, and both would have shipped confident nonsense:

- **A web-fetch summarizer fabricated a quoted result from a PDF**, returning in quotation marks the reverse of the paper's stated conclusion. Do not use a fetch summary as a quote source for a PDF; re-extract locally.
- **A PDF text layer misattributed table values**, assigning benchmark numbers to the wrong models. A `pdftotext -layout` dump of that table produces confidently wrong attributions; the HTML rendering does not.

## Provenance and honesty about limits

This came out of an adversarially reviewed research run: six disjoint lenses, two of them seated specifically to argue against the conclusion, independent verification vouchers with default-refuted, and a cold convergence gate.

The gate earned its place. It killed the run's original headline recommendation, caught that the synthesis had silently dropped **both** dissenting lenses, and the vouchers then refuted or materially corrected five more claims. Where a source was reachable only in secondary form, it is labeled as such rather than laundered into a quote.

Known gaps are stated in the files themselves rather than hidden: several canonical sources were unreachable at the primary level, the accessibility topics substantially duplicate an existing licensed inventory that should be imported rather than re-derived, and the derivation proves its own mapping but not the wording of every rule it produced.

## License

MIT. The research files cite their sources; where a third-party work is quoted, the quote is attributed inline.
