# Releasing

There is no build and no publish step. A marketplace reads a git ref directly, so **a release is a tag**.

Two kinds of plugin live here and they release differently.

## A plugin in this repo (`plugins/<name>/`)

Tags are per plugin, `{name}--v{version}`, because one repo ships several plugins on their own clocks.

1. Bump `version` in `plugins/<name>/.claude-plugin/plugin.json`.
2. Commit.
3. Tag and push:

   ```
   claude plugin tag ./plugins/<name> --push
   ```

`claude plugin tag` validates that `plugin.json` and the enclosing marketplace entry agree before it writes anything,
and refuses to tag a dirty tree.

## A plugin in its own repo

The tag is cut in that repo. Here you only move the pin:

1. Confirm the tag exists and was pushed: `git ls-remote --tags https://github.com/<owner>/<repo> v<version>`.
2. Set `ref` on that plugin's entry in `.claude-plugin/marketplace.json`.
3. Commit.

## Why every entry is pinned

An entry can point at a default branch, and plenty do. It means every push reaches every user with auto-update on,
within about ten minutes, with no review and no way for anyone to stay on a known-good version. Fine for a scratch
plugin, wrong for a public one.

The failure worth guarding against is a **pin to a tag nobody pushed**. It validates locally and fails at install time
for everyone. CI checks each pinned ref against the remote for exactly this reason.

## Versions

Semantic versioning, per plugin. Below `0.1.0` means the shape is still moving and anything can change without
ceremony.
