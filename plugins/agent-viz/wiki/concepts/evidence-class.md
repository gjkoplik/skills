---
type: concept
---

# Evidence class

**What it is.** Labeling each rule in a quality bar by its warrant: **evidence-backed** (a study, an experiment, a published standard) or **authority-asserted** (a design book or style guide asserts it). Both are usable. Conflating them is the characteristic failure of visualization advice.

**Status.** Synthesis of a practice ordinary in other fields, applied here rule by rule to a visualization bar.

**What it is good for.** Deciding how hard to push a rule, and which rules fail when challenged by someone who has read the sources.

**What it does not settle.** Whether a rule is right. An authority-asserted rule can be excellent, and the label describes the warrant, not the quality.

---

## Where received wisdom degrades

Roughly a third of the received wisdom this project checked did not survive contact with its primary source. The usual failure is the citation chain, where careful papers become confident rules without their caveats. Cases from [refutations.md](../refutations.md):

- "Bank to 45 degrees" is a scope-limited result reported as a general one.
- The axis-break remedy for truncation did not measurably work, but the test is a knife-edge null that does not license "placebo" either.
- The flat dual-axis ban has no supporting experiment. The paper usually cited studied something adjacent.
- "Maximize data-ink" is element-conditional. Removing axis lines *hurt* reading speed.
- "Gray plus one accent", a rule this project uses and likes, has no controlled study behind it.

## The labels

- **Evidence-backed.** A study, experiment or published standard, with the source and number cited. WCAG's contrast ratios are the cleanest case. Stated flatly: "Truncation inflates perceived effect size."
- **Authority-asserted.** A practitioner or design book asserts it without an experiment. A usable default, with the status visible: "Default to gray plus one accent. This is convention, not a measured result."
- **Contested.** The record disagrees with itself, as the chartjunk literature does, and a bar that picks a side misrepresents the field. Stated as the rule, the contest, and what survives: "Strip decoration, keep orientation" survives the data-ink argument once removing axis lines is known to hurt.
- **Absence of evidence.** Nobody has tested it, which is neither refutation nor contest. The dual-axis ban sits here. Stated as the caution and its reason: "The correlation a reader sees is a free parameter of your scaling choice" can be acted on, and "never use dual axes" cannot.

## What is exempt, and why the exemption matters

Definitional content carries no label, because a statement of what something is could not turn out false. The structural decomposition on every page in [../chart-types/](../chart-types/) is the clearest case: a pie chart normalizing to shares and drawing wedges in polar coordinates describes the chart, not its readers. So does "force-directed layouts are not reproducible," which follows from their being stochastic. Labeling these would dilute the labels on real claims and make the most secure statements on a page look unsupported.

The risk is the step into an empirical claim. "A hive plot puts node position on a real data scale" is definitional and secure. "Therefore readers read it more accurately" has no study behind it. The hinge word is *therefore*.

## Where the degradation happens

A convention becomes a finding in quotation: someone reads "default to gray plus one accent, this is convention", cites it as "research shows single-accent emphasis improves comprehension", and a fabricated finding circulates under the bar's name. So the label belongs in the sentence, where it survives quotation. Consistent labeling makes a bar sound less authoritative, and its unhedged rules mean more.

## See also

- [floor-and-ceiling.md](floor-and-ceiling.md): the other axis a rule should carry
- [../refutations.md](../refutations.md): the specific cases that motivated this
- [../inventory.md](../inventory.md): every topic carries its evidence class
