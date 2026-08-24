# Releasing

There is no build and no publish step. A marketplace reads this repo live from a git ref, so a release is a tag.

**Two levels, answering different questions.**

| | Versioned by | Recorded in | Answers |
| --- | --- | --- | --- |
| A plugin | semver | `plugins/<name>/CHANGELOG.md` | what changed in this skill, and is it breaking |
| This repo | calendar | `CHANGELOG.md` | what shipped, and when |

The plugin version is the one that matters to a user. The repo version is bookkeeping.

## Releasing a plugin

1. Land the change on `main`. CI has to be green.
2. Add the entry to `plugins/<name>/CHANGELOG.md`.
3. Bump `version` in `plugins/<name>/.claude-plugin/plugin.json` and commit.
4. Tag and push:

   ```
   claude plugin tag ./plugins/<name> --push
   ```

That writes `<name>--v<version>`. `claude plugin tag` validates that `plugin.json` and the marketplace entry agree
before it writes anything, and refuses to tag a dirty tree.

**The version bump is the gate, not the tag.** Verified: a content change pushed to `main` without a version bump does
not reach an installed user, who is told they are already at the latest version. Bumping delivers it. So a push that
forgets step 3 reaches nobody, which is the safe direction to fail, but it also means the changelog and the version
have to move together or a real change silently does not ship.

Users never see the tag. They type `/plugin install <name>@skills` and see `Version: 0.0.1`.

## Cutting a repo release

Calendar versioned, `vYYYY.MM.DD`. It carries no meaning of its own: it records which plugin versions were current.

1. Add a dated section to the root `CHANGELOG.md` listing each plugin at its version, and what moved since the last one.
2. Commit, then `git tag v2026.08.24 && git push origin v2026.08.24`.

Nothing pins to these tags and no manifest holds a repo version. They exist so a point in time has a name.

## What users get

```
/plugin marketplace add gjkoplik/skills
/plugin install agent-viz@skills
/plugin install what-if@skills
```

Adding the marketplace without a ref tracks the default branch, so a version bump reaches users on auto-update within
about ten minutes. Anyone who wants to be explicit can pin the marketplace itself:

```
/plugin marketplace add gjkoplik/skills#v2026.08.24
```

## Versioning a plugin

Semantic versioning, with the wrinkle that these ship prose rather than code. Below `0.1.0` means the shape is still
moving and anything can change without ceremony.
