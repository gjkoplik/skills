---
name: test-review
description: 'Review a whole test suite for cruft and write one report: tests and fixtures whose subject is gone, fixtures and helpers nothing uses, test code that remakes what the suite already has, and tests that repeat another test. Reads the tests, the code and git history; runs nothing and changes nothing but the report. Findings are sorted into those safe to act on and those that need a decision, so another agent can act on the file alone. Run it only when the user types /test-review, optionally with a path.'
disable-model-invocation: true
argument-hint: '[path to a directory or file of tests; default is every test in the repo]'
---

# Test review

Tests rot the way code does. This reads a whole suite against the codebase it tests and reports what has become
cruft. It reports and stops: you change nothing in the repo except to write the report, and you do not act on the
report in the same breath. Cleaning is a separate request, made by the user after they have read it.

**A wrong finding is worse than a missed one.** These tests exist so that an agent changing the code finds out when
it broke something. A report that talks someone into deleting a test that was guarding something has done damage; a
report that misses some cruft has only been incomplete. So doubt always moves a finding from "safe" to a question,
and a finding you could not verify yourself is not reported as safe.

You read: the tests, the source, and git history. You do not run the tests, coverage, or mutation tools.

The scope: $ARGUMENTS

## Before reading anything

Stop with a one-line error, and write no report, if any of these holds:

- the working directory is not inside a git repo (`git rev-parse --show-toplevel` fails);
- a path was given and does not exist;
- the scope has no tests in it.

A path is relative to the working directory. It limits which tests are judged. Every search for a use, a subject,
or a surviving test still covers the whole repo.

A report that says it reviewed nothing reads as a clean suite, which is why these are errors.

## 1. Inventory

Work out, by commands and not by impression:

- **The runner**, from the project's configuration, and how it decides what is a test file. If you do not
  recognize the runner, say so in the report; nothing unused can then be called safe.
- **The files in scope.** List them with `git ls-files` plus `git ls-files --others --exclude-standard`, so that
  environments, nested worktrees, submodules and build output never enter. Pick out the test files by the
  runner's own rule, and the shared test support they lean on: fixture modules, helpers, factories, test data.
  Test support means code that exists for the tests. The library's own functions are not test support.
- **What to skip.** Only generated files, vendored files, and files you cannot read. Each goes in the report with
  its reason. Always skip the `test-review/` directory at the repo root, which holds earlier reports.
- **Implicit use.** Every way this runner uses a fixture or helper without the test naming it: automatic fixtures,
  fixtures requested by string, hooks and files found by naming convention, plugins, fixtures consumed only by
  other fixtures, a helper in a test module that shadows a shared fixture's name. Write the list down; step 3
  needs it.
- **How tests are selected.** What the default run leaves out (markers, ignored files, optional dependencies), and
  the command that runs each such group. A safe finding has to name a command that runs the test it touches.
- **The commit**: `git rev-parse --short HEAD`, and whether the tree has uncommitted changes.

Count the test files and the support files, and keep the command that produced the count. Both go in the report.

## 2. Read every test

Every test file in scope gets read in full by someone. Skimming names is not reading.

If the suite fits comfortably in your own context, read it yourself. If not, split the files into lanes by
directory, keeping tests of the same module together, and give each lane to a subagent. A lane's brief carries the
four kinds and what is not a finding (below), the list of shared test support with one line on what each piece
provides, and the instruction to change nothing. It returns:

- candidates, each with its kind, the test or fixture by name and `path:line`, and what it saw;
- the fixtures and helpers defined inside its test files, with one line on what each builds;
- for each test file, which source symbols its tests exercise.

If you cannot dispatch subagents, read the lanes yourself one after another. If something in scope still went
unread, the report says the run is incomplete and names what was not read.

Then do the work that needs the whole suite at once:

- the same fixture or helper built in more than one lane;
- source symbols tested from more than one lane, where you read those tests side by side for repeats;
- shared test support that no lane used.

## The four kinds

Report these and nothing else. Mocking that is too heavy, a test that cannot fail, cases that ought to be
parametrized, weak assertions, slow tests: not findings here, however tempting.

**1. Subject gone.** A test or fixture for code or behavior that no longer exists. The function was deleted, the
option was removed, the branch it exercises cannot be reached because the thing that reached it is gone.

- Not a finding: a test of code that still exists, however rarely that code looks used. Code that looks dead is a
  question about the code, not about its test.
- Not a finding: a test that fails, or is skipped. Say nothing about it unless its subject is gone.

**2. Unused.** A fixture, helper, or piece of test data that nothing uses.

- Not a finding: anything the runner can pick up without being named. Check each mechanism from your inventory.
- Not a finding: a fixture used only by another fixture that is used.
- Unused means the whole thing. A helper that is used but builds something its callers throw away is a question.

**3. Reinvented.** Either of:

- test code that builds by hand what an existing fixture or helper already provides, or the same setup built the
  same way in three or more tests with no fixture for it;
- a test that gets its expected value by repeating the logic of the code it tests, so the two cannot disagree.

Not a finding: an expected value worked out independently, by hand, from a reference implementation, or with a
different tool. That is a test doing its job. Not a finding: setup short enough that a reader would rather see it
than look it up.

Report one finding per thing reinvented, not one per place it happens. Name it for the existing fixture or helper,
or for the first test that builds it, and give the other places as a count with the command that lists them.

**4. Redundant.** A test, or one case of a parametrized test, that checks the same thing as another test, which
you name.

- Not a finding: two tests that reach the same code with inputs that differ in a way the code could care about.

## 3. Check each candidate yourself

A candidate from a lane, or from your own reading, is a claim. Before it goes in the report, try to prove it wrong:

- **Subject gone.** Search the whole repo for the subject, including as a string, since code is looked up by name
  in places a symbol search misses. Find the commit that removed it (`git log -S`). Work out why the test still
  passes if it does. If you cannot show the removal, it is not safe.
- **Unused.** Search the whole repo, not the test directory. Go down the list of implicit mechanisms and record
  what you checked for each.
- **Reinvented.** Open the existing fixture or helper and confirm it builds the same thing, not a near thing.
- **Redundant.** Put the two tests side by side and compare inputs, assertions, and how each is selected to run
  (markers, skips, parameters, fixtures). The evidence is the two line ranges and what differs.
- **Any kind.** A mention in documentation, a plan, or a changelog is not a use.

Run every command you intend to cite, and cite what it returned. Drop any candidate that does not survive.

## 4. Sort into two groups

**Safe to act on** needs all of: evidence the reader can check without you (a command and what it returns, a
commit, a path), a move that removes or replaces test code without changing what is tested, and no remaining doubt.
On top of that, by kind:

- **Subject gone** is safe when the removal is shown in the code or the history.
- **Unused** is safe only when the evidence lists each implicit mechanism and shows it was checked.
- **Reinvented** is never safe. Replacing setup across many tests is a refactor someone should choose.
- **Redundant** is safe only when the surviving test is named, runs under the same selection, uses the same
  inputs, asserts everything the removed test asserts, and is there to test the same behavior. A survivor that
  covers it only in passing, on the way to testing something else, makes it a question: the named test is what
  tells someone which behavior broke. Different inputs make it a question. So does a single parametrized case.
- A surviving test is never itself the target of another safe finding. If it would be, the redundant finding
  becomes a question that says so. Several findings may name the same survivor.

Whatever the kind, a test that names an issue, a bug, or a regression, in its name or its docstring, is never safe
to remove. Neither is a test the default run does not select, unless you can name the command that runs it.

**Needs a decision** is everything else that survived step 3. Write it as a question the user can answer in a
word, with the options. Someone has to answer every one, so group them: redundant pairs in one class or file that
turn on the same question are one finding that lists each pair, named for the first.

Safe findings carry an instruction to whoever acts on them, because you ran nothing and the tree may have moved:
check the evidence still holds, then run the tests before and after, and revert if a test fails or coverage drops.
Name the command. It is the project's own default run when that run selects the test, and the whole of it when
the project gates on total coverage, since one file run alone shows a drop that means nothing. Otherwise it is the
command that selects the test.

## 5. Write the report

One file at `<repo root>/test-review/YYYY-MM-DD-<scope>.md`. The date is today. `<scope>` is `all` for the whole
suite; for a path it is the path with separators turned into hyphens (`tests/unit` becomes `tests-unit`). If the
name is taken, add `-2`, `-3`. Create the directory if needed. Do not stage or commit it.

Use exactly this shape. The name in each heading is the anchor that whoever acts will search for; the line number
is a hint that goes stale as soon as the file above it changes, so every finding has a name.

```
# Test review: YYYY-MM-DD

Reviewed: <scope> (<n> test files, <n> support files) at <short sha>, against <source dirs> and git history.
Counted with: `<command>`
Runner: <name only, or "not recognized">.
Skipped: <path> (<reason>), ... | none
Found: <n> safe to act on, <n> needs a decision. <Complete. | Incomplete: what was not read.>

## Safe to act on

### `<name>` <path>:<line>
Kind: <subject gone | unused | redundant>
Evidence: <what shows it, with the command and what it returned, the commit, or the path>
Cost of leaving it: <one line, concrete>
Move: <the one specific move>. Check the evidence still holds. Run `<command>` before and after; revert if a test fails or coverage drops.

## Needs a decision

### `<name>` <path>:<line>
Kind: <subject gone | unused | reinvented | redundant>
Evidence: <as above>
Cost of leaving it: <one line, concrete>
Question: <what the user has to decide>
Options: <option>; or <option>.
```

Add "(uncommitted changes present)" after the sha if there were any. A group with no findings keeps its heading
and says "None." A review that found nothing is a complete run; do not go looking for something to report.

Then print the report's path and its `Found:` line, and stop. Do not summarize the findings in chat, do not offer
to act on them, and do not act on them.
