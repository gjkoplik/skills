---
name: agent-viz-sweep
description: Weekly agent-viz research sweep. Finds one paper, one chart type, and one person or style guide worth a wiki page, plus a staleness check against changed norms. Leaves uncommitted edits for review.
schedule: "7 4 * * 6"
notifyOnCompletion: true
---
Weekly research sweep for the **agent-viz** wiki. Fresh session: assume no memory of prior runs.

## Setup

1. `cd` to the **`plugins/agent-viz` directory of the `skills` monorepo** and work from there, so every `wiki/...` path below resolves as written. Find the repo root with `git rev-parse --show-toplevel`; if the working directory is not the `skills` repo, locate it (it is under `~/repos`) and `cd` into `plugins/agent-viz`. agent-viz used to be its own repo and no longer is.
2. **Load the `agent-viz-wiki` skill** at `../../.claude/skills/agent-viz-wiki/SKILL.md` (repo root, not the plugin). It carries the page schema, the evidence-class discipline, the flat-chart-types structure, the extraction rules, and the house prose style. Everything below assumes it.
3. Read `wiki/README.md` for the current state: the source and study tables, the page counts, and the stated gaps. Read `wiki/refutations.md`, which is the highest-value page and the best guide to what this project considers a good find.
4. `git status` first. If the working tree already has uncommitted wiki edits from a previous run the maintainer has not reviewed yet, **do not pile on**. Note it in the digest, do the staleness check only, and stop.

## The sweep: one of each, and no more

The cap is the point. Three good pages a week compounds; twenty thin ones make the wiki worse. If a hunt turns up nothing that clears the bar, **write nothing and say so in the digest.** A quiet week is a real outcome.

### 1. One paper

Search for empirical work on graphical perception, chart reading, or visualization evaluation, published or newly surfaced since roughly the last run.

**Rank candidates by what they do to claims the wiki already makes**, highest first:

1. Refutes, qualifies, or scope-limits something the wiki currently asserts. These are the most valuable finds in the project and belong in `wiki/refutations.md`.
2. Supplies evidence where the wiki currently says `absence of evidence`. Check the chart-type pages for these; several name exactly what would move them.
3. Replicates or fails to replicate an existing study page.
4. Merely new and relevant.

**Reach it at primary or do not write it up.** Download, extract locally, verify the title matches what you meant to fetch, and quote only from the extraction. If it is paywalled, search the filesystem including sibling repos for a local copy before recording `not-reached`. A scanned PDF with no text layer is still readable by rendering pages to images.

Write a study page, update the `wiki/README.md` study table and counts, and add a refutations entry if it earned one.

### 2. One chart type

Add one type page under `wiki/chart-types/`, flat, with its `**Relationships.**` header line and the six-slot structural decomposition.

Prefer, in order: a type named as absent in an existing index; a type that would let an unwritten relationship index get started; a form encountered in the wild that the wiki cannot currently say anything about.

**Write it for someone making a choice.** Open with when to reach for this form and when not, before any structural description. Close with the sentences that justify choosing it, including the commonly repeated justifications the evidence does not support. Keep all process narration off the page.

**Apply the inheritance rule strictly.** Evidence attaches to channels, not to types. If there is nothing to inherit and no type-level study, the page will be short and mostly `authority-asserted`, and that is the correct output. Write it short. Do not pad.

If the type belongs to a group with no index yet, either start the index page or add the type and leave its relationship unlinked, which is the documented signal for "index not written yet."

### 3. One person or style guide

Two destinations, and they are not interchangeable:

- **`wiki/people/`** for a person across their work, using the person schema ("What they are known for", "What they are good for", "What they do not settle"). Not a biography, not a summary of their views: what coming to this person actually buys you, and where their authority stops.
- **`wiki/sources/`** for one specific work, style guide, design system, or library's documentation.

A prolific author can warrant both. Prefer whichever covers a gap the wiki names in its own Coverage section, and prefer people already cited across several pages without having one.

Same reachability discipline. If you only reached a summary, the page is `secondary-only` and says so.

**Do not link to a person page that does not exist yet.** This wiki uses plain markdown relative links, so a forward link is a broken link. Name the person in prose instead.

## Staleness check (always run, even on a quiet week)

Light pass, not a full audit:

- Have any **standards** the wiki cites moved? WCAG contrast criteria and any published accessibility standard are the live ones.
- Do any wiki claims now read as stale against changed norms or tooling defaults? Library defaults shift, and several pages cite specific ones.
- Any broken internal links or anchors. Check every markdown link under `wiki/` resolves, including anchors, and that every type page appears in at least one index. Note that links may point above `wiki/` (for example to `CONTRIBUTING.md`), so resolve anchors in those files too rather than assuming a link outside `wiki/` is broken.
- Any page whose `Status` is now wrong, most often a `not-reached` or `secondary-only` source that has since become reachable.
- **Contradictions between pages.** Two pages disagreeing is a finding, not a nuisance: it is usually one of them citing the wrong source. Reconcile both, and put the reconciliation in `refutations.md` if a widely repeated claim was involved.

Fix what is mechanical. For anything that is a judgment call, note it in the digest and leave it.

## Output

- **Never commit.** Leave all edits in the working tree for the maintainer to review with `git diff`.
- Write a digest to `~/.claude/reflections/agent-viz-sweep-<YYYY-MM-DD>.md` containing: what each of the three hunts found or why it came up empty, what the staleness check turned up, every file touched, and any judgment calls left for the maintainer.
- Keep the digest short enough to read in two minutes. Review time is the scarce resource here, not research time.
