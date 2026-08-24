# Releasing

There is no build and no publish step. A marketplace reads this repo directly from a git ref, so **a release is a tag**.

**The marketplace is not in this repo.** It lives in [gjkoplik/skills](https://github.com/gjkoplik/skills), which
lists this repo alongside plugins that have no subject repo of their own. This repo is the plugin. That split keeps a
research repo from also being a storefront, and it means a release here is two steps in two places.

## Why this is pinned to a tag rather than `main`

A marketplace entry can point at the default branch, and plenty of plugins do. It means every push reaches every user
with auto-update on, within about ten minutes, with no review and no way for them to stay on a known-good version.

That is fine for a personal scratch plugin and wrong for a public one. So this repo is pinned to a tag, and users get
a new version only when the pin moves.

## Cutting a release

1. Land the changes on `main`. CI has to be green: the manifest validates, relative links resolve, house style holds.
2. Bump `version` in `.claude-plugin/plugin.json` and commit.
3. Tag and push:

   ```
   git tag v0.0.1
   git push origin main --follow-tags
   ```

4. In `gjkoplik/skills`, set `ref` on this repo's marketplace entry to `v<version>` and commit.

The `release-tag` CI job enforces steps 2 and 3: it fails if the version has no matching tag in the repo. The pins job
in the marketplace repo enforces step 4 from the other side, checking the pinned tag against this remote. Both exist
because **a marketplace pinned to a tag that was never pushed fails at install time for everyone**, and you would not
notice locally.

## What users get

```
/plugin marketplace add gjkoplik/skills
/plugin install agent-viz@skills
```

They can also pin the marketplace itself to a ref if they want to be explicit:

```
/plugin marketplace add gjkoplik/skills#v0.0.1
```

Claude Code uses `version` in `plugin.json` as its update cache key, which is why bumping it is not optional. Without a bump, users on an older copy are not told there is anything new.

## Where this is in its life, and what the version number means

**It is `0.0.x` on purpose.** The content has had one review pass and plenty of it has not been read closely by a human yet. Shipping early is deliberate, so the number carries the warning: below `0.1.0` means anything can change without ceremony, including rules being reworded, reclassified, or removed outright.

Read `0.0.x` as: usable, honest about its sourcing, and not yet settled. `0.1.0` is the signal that the structure has stopped moving. `1.0.0` would mean the rules themselves are stable enough that changing one is a breaking change for anyone relying on them.

## Versioning

Semantic versioning, with the wrinkle that this ships prose rather than code:

Once past `0.0.x`:

- **Patch**: corrections, better sourcing, a page upgraded from `secondary-only` to `primary-read`.
- **Minor**: new rules, new wiki sections, anything that changes what the skill tells an agent to do.
- **Major**: a change that would make an existing figure that passed now fail, or a restructure of the floor and ceiling.
