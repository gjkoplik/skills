# Releasing

There is no build and no publish step. A marketplace reads this repo live from a git ref, so a release is a tag.

**Two levels, answering different questions.**

| | Versioned by | Recorded in | Answers |
| --- | --- | --- | --- |
| A plugin | semver | `plugins/<name>/CHANGELOG.md` | what changed in this skill, and is it breaking |
| This repo | calendar | `CHANGELOG.md` | what shipped, and when |

The plugin version is the one that matters to a user. The repo version is bookkeeping.

## Every plugin is pinned to its own tag

Each entry in `marketplace.json` is a `git-subdir` source pointing at this repo, one plugin subdirectory, at a tag:

```json
{ "source": "git-subdir", "url": "https://github.com/gjkoplik/skills.git",
  "path": "plugins/what-if", "ref": "what-if--v0.0.1" }
```

**Not a relative path.** A relative-path source resolves against whatever the marketplace repo's default branch is at,
so a fresh install pulls unreleased work straight off `main`. The `version` field gates *updates* for someone already
installed, but it does not protect a first install. Pinning does. `main` can be as far ahead as you like and nobody
sees it until a ref moves.

## Releasing a plugin

1. Land the change on `main`. CI has to be green.
2. Add the entry to `plugins/<name>/CHANGELOG.md`.
3. In one commit: bump `version` in `plugins/<name>/.claude-plugin/plugin.json`, **and** set that plugin's `ref` in
   `.claude-plugin/marketplace.json` to the matching `<name>--v<version>`.
4. Tag and push:

   ```
   claude plugin tag ./plugins/<name> --push
   ```

`claude plugin tag` validates that `plugin.json` and the marketplace entry agree before writing anything, and refuses
to tag a dirty tree, so step 3 landing as one commit is what makes step 4 work.

Users never see the tag. They type `/plugin install <name>@gjkoplik` and see `Version: 0.0.1`.

The `pins` CI job fails if a ref does not exist, if a ref and a version disagree, or if any plugin has drifted back to
a relative path. It also prints a notice for each plugin whose files have changed on `main` since its pin, so unshipped
work is visible rather than assumed.

## Cutting a repo release

Calendar versioned, `vYYYY.MM.DD`. It carries no meaning of its own: it records which plugin versions were current.

1. Add a dated section to the root `CHANGELOG.md` listing each plugin at its version, and what moved since the last one.
2. Commit, then `git tag v2026.08.24 && git push origin v2026.08.24`.

Nothing pins to these tags and no manifest holds a repo version. They exist so a point in time has a name.

## What users get

Verified against this repo, not assumed.

```
/plugin marketplace add gjkoplik/skills
/plugin install agent-viz@gjkoplik
/plugin install what-if@gjkoplik
```

They then see the plugin's semver and nothing else:

```
❯ what-if@gjkoplik
  Version: 0.0.2
```

**Users never see a tag.** `what-if--v0.0.2` appears only in your git history and in `marketplace.json`.

The `@gjkoplik` suffix names the marketplace, not the repo, and it is only needed to disambiguate: `/plugin install
what-if` works when nothing else offers that name. The marketplace is named for the handle rather than something like
`skills` because **a user can only have one marketplace per name**, and a generic name is the one most likely to
collide with someone else's.

### The two halves, because they behave differently

| | Tracks | Decides |
| --- | --- | --- |
| `marketplace.json` on `main` | the default branch, live | **which tag** each plugin sits at |
| the tag it names | frozen | **what content** ships |

So the two things you can push have opposite effects:

- **Pushing plugin code to `main` reaches nobody.** Confirmed: `plugins/what-if/CHANGELOG.md` sat on `main` for several
  commits while every install lacked it, because the pin still named an older tag.
- **Pushing a changed pin to `main` is the act of releasing.** That is the whole release, and it is why the version bump
  and the pin move belong in one commit.

### What an existing user does

Auto-update handles this, but by hand it is two steps, and the first is the one people forget:

```
/plugin marketplace update gjkoplik
/plugin update what-if@gjkoplik
```

Observed: `Plugin "what-if" updated from 0.0.1 to 0.0.2 for scope user. Restart to apply changes.` A new install on the
same commit lands on `0.0.2` directly. Old versions stay in the cache side by side (`cache/skills/what-if/0.0.1` and
`.../0.0.2`), so a rollback is a version pin away rather than a re-download.

## Versioning a plugin

Semantic versioning, with the wrinkle that these ship prose rather than code. Below `0.1.0` means the shape is still
moving and anything can change without ceremony.
