# Checks that actually run

Every snippet here was executed against a real matplotlib figure before being written down. Nothing needs a library beyond `numpy` and `matplotlib`.

**Most of the honesty rules are mechanizable**, and cheaply: the whole battery below runs in well under a second. Several of them catch defects that are **invisible in source review**, because the bug is in the rendered artifact rather than in the code that produced it.

The checks run under `matplotlib.use("Agg")` and assert against the live `Axes` object. There is no static-grep version of most of these: the violation is typically a `set_ylim` call at a distance from the `ax.bar` call.

---

## Color-vision deficiency

The rule "simulate CVD, do not eyeball it" is unfireable in most environments, because no CVD library is installed. It does not need one.

```python
import numpy as np

# Machado, Oliveira & Fernandes (2009), deuteranopia, severity 1.0
DEUTER = np.array([[ 0.367322,  0.860646, -0.227968],
                   [ 0.280085,  0.672501,  0.047413],
                   [-0.011820,  0.042940,  0.968881]])

def simulate_cvd(fig, matrix=DEUTER):
    """Return an (H, W, 3) float array of the figure as a CVD viewer sees it."""
    fig.canvas.draw()
    rgb = np.asarray(fig.canvas.buffer_rgba())[..., :3] / 255.0
    return np.clip(rgb @ matrix.T, 0.0, 1.0)
```

The result is read by diffing it against the original or by eye. **This is an approximation, not a clinical simulation.**

The cheap fallback, for a numeric rather than visual result: convert to luminance and assert the encoded series still separate.

## WCAG contrast

A published standard, and about a dozen lines.

```python
def _lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

def relative_luminance(rgb255):
    r, g, b = (_lin(v) for v in rgb255)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(fg255, bg255):
    a, b = relative_luminance(fg255), relative_luminance(bg255)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)
```

Verified: `#2166AC` on white returns **5.9**, which clears the 4.5:1 floor for normal text.

**The two floors come from different versions of WCAG.** SC 1.4.3 Contrast (Minimum), Level AA, has been 4.5:1 for text and 3:1 for large text since WCAG 2.0. The **3:1 floor for graphical objects is SC 1.4.11 Non-text Contrast, which does not exist in WCAG 2.0**: guideline 1.4 stops at 1.4.9 there, and the criterion arrived in 2.1. It is carried unchanged into WCAG 2.2, the current W3C Recommendation as of 12 December 2024, where its text covers "Parts of graphics required to understand the content". So a mark, a gridline or a series color is checked against a criterion the Urban Institute's WCAG 2.0 framing does not contain. *(Checked against the W3C specs on 2026-08-29.)*

## Zero baseline when area encodes the value

```python
import matplotlib.container

def area_marks_present(ax):
    return bool([c for c in ax.containers
                 if isinstance(c, matplotlib.container.BarContainer)]) or bool(ax.collections)

def zero_baseline_violation(ax):
    return area_marks_present(ax) and ax.get_ylim()[0] != 0
```

Verified: returns `True` on a truncated bar chart with `ylim` starting at 95.

## Axis truncation ratio

The check reports the number rather than auto-failing on it. The literature explicitly refuses a threshold.

```python
def axis_span_ratio(ax, data):
    lo, hi = ax.get_ylim()
    span = hi - lo
    dspan = float(np.max(data) - np.min(data))
    return span / dspan if dspan else float("inf")
```

Near 1.0 means the axis hugs the data, which is aggressive truncation. Much greater than 1 is the opposite failure, an over-expanded scale. Verified: returns `3.0` on a test case.

## Inverted axes

One line, and the failure mode is catastrophic: inversion reverses the conclusion rather than exaggerating it, and readers do not notice.

```python
inverted = ax.yaxis_inverted() or ax.xaxis_inverted()
```

## Log scales, and bars on them

```python
is_log = ax.get_yscale() != "linear"
bars_on_log = is_log and area_marks_present(ax)   # bars on a log scale must start at 1, not 0
labelled = bool(ax.get_ylabel())
```

## Dual axes

Detection is trivial; the verdict is judgment. The check flags the figure for the author to justify rather than failing it.

```python
def twin_axes(fig, ax):
    return [a for a in fig.axes
            if a is not ax and a.get_position().bounds == ax.get_position().bounds]
```

Verified: returns one overlapping axes after `ax.twinx()`.

## Tick label collisions, by rendered geometry

Expected to be judgment; it is not. This is a real geometry test, not a heuristic on label count.

```python
def tick_labels_overlap(fig, ax):
    fig.canvas.draw()
    boxes = [t.get_window_extent() for t in ax.get_xticklabels() if t.get_text()]
    return any(a.overlaps(b) for i, a in enumerate(boxes) for b in boxes[i + 1:])
```

Costs one draw call.

## Raw floats reaching a label

High catch rate per line, and specific to programmatic plotting. `f"threshold {0.1 + 0.2}"` renders `0.30000000000000004`, which looks fine in source review and only appears in the artifact.

```python
import re, matplotlib.text

def raw_floats(fig, min_decimals=8):
    pat = re.compile(rf"\d\.\d{{{min_decimals},}}")
    return [t.get_text() for t in fig.findobj(matplotlib.text.Text)
            if pat.search(t.get_text() or "")]
```

Sweeps tick labels, titles and annotations alike. Verified: catches `'threshold 0.30000000000000004'` from an f-string title.

Related and not mechanizable: **significant digits**. A median of five timings supports two significant figures. A label reading `2.3847 s` asserts precision the sampling design cannot deliver, and no regex detects that.

## Colorbars

Four separate assertions, all verified.

```python
# explicit limits rather than autoscale
has_limits = im.norm.vmin is not None and im.norm.vmax is not None

# silent saturation: the sharpest check here, because clipping is invisible in the image
clipped = int((data > im.norm.vmax).sum())
silently_saturating = clipped > 0 and cbar.extend == "neither"

# comparable panels share one scale
shared = len({im.get_clim() for im in images}) == 1

# a diverging map has its midpoint pinned
diverging_centred = abs(norm.vmin + norm.vmax) < tol   # when cmap name is in a known diverging set
```

The colorbar label check must test both `cbar.ax.get_ylabel()` and the axes title. `fig.colorbar(..., label=...)` populates the former, but `cbar.ax.set_title(...)` does not, and a naive `get_ylabel()` check reports a false violation on a perfectly well-labeled figure.

## Interval bounds inside the variable's domain

A symmetric ±SD bar on a bounded quantity eventually crosses the bound: a negative duration, a memory below zero, a proportion above 1. The interval is the wrong shape, not the axis.

```python
def whisker_below(ax, floor=0.0):
    out = []
    for coll in ax.collections:
        for seg in coll.get_segments():
            if seg[:, 1].min() < floor:
                out.append(float(seg[:, 1].min()))
    return out
```

Measured at **0.018 ms per call**. Fires correctly on `ax.bar([...], [3, 1, 2], yerr=[2, 3, 1])`, whose whisker reaches −2.

## Clipped points, with the trap

```python
def clipped_points(ax):
    (x0, x1), (y0, y1) = ax.get_xlim(), ax.get_ylim()
    n = 0
    for ln in ax.lines:
        if ln.get_transform() is not ax.transData:   # <-- the trap
            continue
        xy = ln.get_xydata()
        n += int(((xy[:, 0] < x0) | (xy[:, 0] > x1) |
                  (xy[:, 1] < y0) | (xy[:, 1] > y1)).sum())
    return n
```

Measured at **0.011 ms per call**. **The naive version is wrong**: without the transform filter it reports false positives from `axhline` and `axvline`, whose `get_xydata()` returns x in *axes* coordinates. A first pass reported four clipped points on a clean real figure for this reason.

## Binning and smoothing left implicit

A source-text lint rather than a figure check, so it runs in review without executing anything.

```python
import re

CALLS = r"(hist2d|hexbin|histplot|kdeplot|gaussian_kde|qcut|\bcut\b|\bhist\b)"
PARAMS = r"(bins=|q=|gridsize=|bw_method=|bw_adjust=|cutoffs=)"

def implicit_binning(src):
    return [m.group(1) for line in src.splitlines()
            for m in [re.search(CALLS, line)]
            if m and not re.search(PARAMS, line)]
```

Measured at **0.004 ms per call**. Correctly passes `np.histogram(x, bins=30)`, `pd.qcut(v, q=3)` and `pd.cut(v, bins=b)` while flagging bare `hist` and `kdeplot`.

## Categorical order

```python
def categorical_order(ax):
    labels = [t.get_text() for t in ax.get_xticklabels()]
    heights = [p.get_height() for p in ax.patches]
    if len(labels) != len(heights):
        return "n/a"                      # grouped bars: needs real work
    if heights == sorted(heights) or heights == sorted(heights, reverse=True):
        return "monotone"
    if labels == sorted(labels):
        return "alphabetical"
    return "arbitrary"
```

Measured at **0.037 ms per call**. **Two honest limits.** It returns `n/a` on grouped bars, where 6 patches face 3 tick labels, and a careful version costs real authoring effort. And the tidier form, asserting an explicit `order=` was passed, does not exist on the matplotlib path at all: `order=` is seaborn and plotly vocabulary.

---

## What is not mechanizable, and why

Worth stating so nobody burns time trying.

- **Whether the caption correctly describes the array passed to `yerr`.** Presence of a statistic name is greppable; correctness is not decidable from the figure. A weak proxy exists (flag any figure with an error artist whose caption lacks one of SD, SE, CI, percentile, quartile, min, max, spread) and is trivially defeated.
- **Whether n is material.** The number is not in the artifact. Proxy: flag a figure carrying an error artist whose caption text contains no digit.
- **Whether this is a part-to-whole figure at all.** Not recoverable from a `Figure`.
- **Whether a title states the takeaway.** The negative form is a smell test (regex for "Plot of", "Chart showing", "X vs Y"). The positive form is judgment.
- **Aspect ratio.** A candidate can be computed (Cleveland's closed form, `median(|slope|) * Rx / Ry`, runs in ~0.045 s), but the guideline it implements does not survive replication and banking optimizes for one frequency band by construction. Choosing which trend matters is the whole question. See [refutations.md](../refutations.md).
