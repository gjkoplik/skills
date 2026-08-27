---
type: concept
---

# Evidence class

**What it is.** Labeling every rule in a quality bar as either **evidence-backed** (a study, an experiment, a published standard) or **authority-asserted** (a design book or style guide asserting it). Both are usable. Conflating them is the characteristic failure of visualization advice.

**Status.** Synthesis. The practice is ordinary in other fields; applying it rule-by-rule to a viz bar is what this project did.

**What it is good for.** Deciding how hard to push a rule, and knowing which rules will not survive being challenged by someone who has read the sources.

**What it does not settle.** Whether a rule is *right*. An authority-asserted rule can be excellent and an evidence-backed one can be narrow. The label describes the warrant, not the quality.

---

## Why it matters here specifically

Roughly a third of the received wisdom this project checked did not survive contact with its primary source. Not because the sources were bad, but because the *citation chain* degraded: careful papers get summarized into confident rules, and the confidence survives the summarization while the caveats do not.

Concrete instances, all in [refutations.md](../refutations.md):

- "Bank to 45 degrees" is a scope-limited result reported as a general one.
- The axis-break remedy for truncation was tested and did not measurably work, but the test is a knife-edge null that does not license "placebo" either.
- The flat dual-axis ban has no supporting experiment at all; the paper usually cited studied something adjacent.
- "Maximize data-ink" turns out to be element-conditional, with removing axis lines *hurting* reading speed.
- "Gray plus one accent", a rule this project uses and likes, has **no controlled study behind it**.

That last one is the useful test of whether you are applying this honestly. It is easy to label the rules you dislike as authority-asserted. Labeling a rule you rely on is the part that costs something.

## The three states, not two

Two labels are not quite enough. In practice a rule sits in one of:

- **Evidence-backed.** A study, experiment or published standard supports it. Cite the source and the number. WCAG's contrast ratios are the cleanest case: a standard, unambiguous, and checkable.
- **Authority-asserted.** A practitioner or design book asserts it, plausibly and without an experiment. Perfectly usable as a default. Say so and move on.
- **Contested.** The record disagrees with itself. The chartjunk literature is the canonical case, with results in both directions from competent people. A bar that picks a side here is misrepresenting the field.

A fourth state worth naming: **absence of evidence**, which is not evidence of absence and is not the same as contested. The dual-axis ban lives here. Nobody has shown it is harmful; nobody has shown it is fine.

## What is exempt, and why the exemption matters

**Definitional content carries no label.** A statement that describes what something *is*, rather than asserting something that could turn out to be false, is not a claim and does not take a warrant.

The clearest case is the structural decomposition on every page in [../chart-types/](../chart-types/): that a pie chart normalizes to shares and draws wedges in polar coordinates is not a finding about readers, it is a description of the chart. Likewise "force-directed layouts are not reproducible," which follows from their being stochastic optimizations rather than from anyone having measured it.

Labeling these would be worse than leaving them unlabeled, for two reasons. It dilutes the labels on the rows that *are* claims, and it invites the reverse error: an unlabeled definitional statement reads as unsupported when it is actually the most secure kind of statement on the page.

**The trap is the hinge.** Definitional statements are often true and load-bearing, and it is tempting to run one into an empirical conclusion without noticing the transition. "A hive plot puts node position on a real data scale" is definitional and secure. "Therefore readers read it more accurately" is an empirical claim with no study behind it. Same sentence, two different warrants, and the security of the first half is doing unearned work for the second. Watch for *therefore*.

## How to write a rule under each label

- Evidence-backed: state it flatly. "Truncation inflates perceived effect size."
- Authority-asserted: state it as a default with the status visible. "Default to gray plus one accent. This is convention, not a measured result."
- Contested: state the rule, then the contest, then what survives. "Strip decoration, keep orientation" is what survives the data-ink argument once you know removing axis lines hurts.
- Absence of evidence: state the caution and its *reason*, not a prohibition. "The correlation a reader sees is a free parameter of your scaling choice" is actionable in a way "never use dual axes" is not.

## The rule that makes this operational

**Do not upgrade a convention into a finding when quoting the bar.**

This is where the degradation happens. Someone reads "default to gray plus one accent, this is convention", cites it downstream as "research shows single-accent emphasis improves comprehension", and now a fabricated finding is in circulation with your name on it. The label has to survive the quotation, which means it belongs in the sentence rather than in a footnote.

## The uncomfortable corollary

Applying this consistently means your bar gets **less** authoritative-sounding, not more. Several rules that read as settled become hedged. That is the correct direction, and it is the thing that makes the unhedged rules mean something.

## See also

- [floor-and-ceiling.md](floor-and-ceiling.md): the other axis a rule should carry
- [../refutations.md](../refutations.md): the specific cases that motivated this
- [../inventory.md](../inventory.md): every topic carries its evidence class
