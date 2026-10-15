---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Nöllenburg & Wallinger (2023), *Computing Hive Plots*

Martin Nöllenburg and Markus Wallinger, "Computing Hive Plots: A Combinatorial Framework," Graph Drawing and Network Visualization (GD 2023), Springer LNCS. The first formalization of hive plot construction as an optimization problem.

**What it is good for.** Showing that each of the hive plot's three design choices is an instance of a computationally hard problem, which is why a human makes them rather than a solver.

**What it does not settle.** Anything perceptual. Like [Krzywinski et al. (2012)](krzywinski-2012-hive-plots.md), the paper has no user study. Its empirical component is a co-authorship case study and a small computational experiment on crossing minimization.

**How this was read.** arXiv:2309.02273, extracted locally.

## The framework

Hive plot construction decomposes into three steps:

1. **Partition the vertices** into groups, one per axis.
2. **Order the axes cyclically**, to bring strongly connected groups near each other and minimize total inter-axis edge length.
3. **Order the vertices on each axis**, to minimize edge crossings.

## The complexity result

> "Each of the three steps is related to a well-studied, but NP-complete computational problem."

"Related to" is literal. The paper does not prove hive-plot-specific NP-completeness. It identifies each step with a known-hard problem and cites the existing results:

- Step 2 is essentially the **circular arrangement problem**, whose minimum is NP-complete for undirected and directed graphs, with a known polynomial-time O(log n) approximation for the undirected case. Minimizing crossings in a circular arrangement is separately NP-complete.
- Step 3 reduces to repeated **2-layer crossing minimization**, which "is already NP-hard, even if one layer is fixed."

"All three subproblems are shown to be NP-complete" is the phrasing summaries tend to use, and it is stronger than the paper's claim. Each step is an instance of, or reduces to, a problem already known to be hard. That supports the practical conclusion without claiming a new proof.

## Where the hardness lives

The partition and the orderings are not choices somebody has failed to automate. Automating them optimally is intractable in general, so the framework adapts heuristics (a constrained barycenter algorithm for crossing minimization) rather than solving anything exactly. The "you have to choose a partition" property is where the hardness lives, not a rough edge.

## Evidence class

- **Evidence-backed, by citation to prior results.** Each of the three construction steps corresponds to a problem that is NP-complete or NP-hard.
- **Authority-asserted.** That the chosen heuristics produce good hive plots in practice, supported by one case study.
- **Absence of evidence.** Reader performance.

## See also

- [krzywinski-2012-hive-plots.md](krzywinski-2012-hive-plots.md): the original method this formalizes
- [../chart-types/hive-plot.md](../chart-types/hive-plot.md)
