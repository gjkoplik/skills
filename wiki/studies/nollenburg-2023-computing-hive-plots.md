# Nöllenburg & Wallinger (2023), *Computing Hive Plots*

**What it is.** Martin Nöllenburg and Markus Wallinger, "Computing Hive Plots: A Combinatorial Framework," Graph Drawing and Network Visualization (GD 2023), Springer LNCS. The first formalization of hive plot construction as an optimization problem.

**Status.** `primary-read`. arXiv:2309.02273, extracted locally.

**What it is good for.** Establishing that the hive plot's three design choices are each an instance of a computationally hard problem, which is why they are made by a human rather than solved.

**What it does not settle.** Anything perceptual. Like [Krzywinski et al. (2012)](krzywinski-2012-hive-plots.md), this paper contains no user study. Its empirical component is a co-authorship case study and a small computational experiment on crossing minimization.

---

## The framework

Hive plot construction decomposes into three steps:

1. **Partition the vertices** into groups, one per axis.
2. **Order the axes cyclically**, to bring strongly connected groups near each other and minimize total inter-axis edge length.
3. **Order the vertices on each axis**, to minimize edge crossings.

## The complexity result, stated precisely

The authors' own sentence:

> "Each of the three steps is related to a well-studied, but NP-complete computational problem."

**Read "related to" literally.** The paper does not prove hive-plot-specific NP-completeness. It identifies each step with a known-hard problem from the literature and cites the existing results:

- Step 2 is essentially the **circular arrangement problem**, whose minimum is NP-complete for undirected and directed graphs, with a known polynomial-time O(log n) approximation for the undirected case. Minimizing crossings in a circular arrangement is separately NP-complete.
- Step 3 reduces to repeated **2-layer crossing minimization**, which "is already NP-hard, even if one layer is fixed."

The distinction matters for citation hygiene. "All three subproblems are shown to be NP-complete" is a slightly stronger claim than the paper makes, and it is the phrasing that tends to appear in summaries. The correct version is that each step is an instance of, or reduces to, a problem already known to be hard, which is enough to support the practical conclusion without overstating what was proved here.

## Why this matters for the type page

It supplies the reason the hive plot's central design decision is human-made. The partition and the ordering are not choices somebody has failed to automate. **Automating them optimally is intractable in general**, so the framework adapts heuristics (a constrained barycenter algorithm for crossing minimization) rather than solving anything exactly.

That reframes the "you have to choose a partition" property. It is not a rough edge; it is where the hardness lives.

## Evidence class

- **Evidence-backed, by citation to prior results.** Each of the three construction steps corresponds to a problem that is NP-complete or NP-hard.
- **Authority-asserted.** That the specific heuristics chosen produce good hive plots in practice, supported by one case study.
- **Absence of evidence.** Reader performance, again.

## See also

- [krzywinski-2012-hive-plots.md](krzywinski-2012-hive-plots.md) — the original method this formalizes
- [../chart-types/hive-plot.md](../chart-types/hive-plot.md)
