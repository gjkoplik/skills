# Scheduled tasks (canonical source)

Version-controlled source of truth for the desktop **scheduled tasks** (routines) run against this repo. The Claude desktop app keeps its own runtime copy of each task in its internal store (`~/.claude/scheduled-tasks/<id>/SKILL.md` plus an internal record of the schedule and notify flag). These files are the canonical copies, so the routines are versioned, reviewable, and travel with the repo.

Same convention as the hiveplotlib harness, minus the submodule: agent-viz has no harness dependency, so `.claude/` is tracked directly here rather than synced in and gitignored.

Task bodies are written to be machine-agnostic: they derive the repo from the current working directory (`git rev-parse`) and everything else from `~/.claude` plus a glob. Porting to another machine should need no edits.

## How a task file is structured

Each `<task-id>/SKILL.md` has YAML frontmatter and a prompt body:

```yaml
---
name: <task-id>
description: <one-line summary>
schedule: "<5-field cron, local time>"   # documentation of the live schedule
notifyOnCompletion: true                  # documentation of the live notify flag
---
<the prompt body the routine runs>
```

The frontmatter is **documentation only**. The desktop app does not read these files; it reads its own store. The bridge is the `scheduled-tasks` MCP tool.

- **`name` / `description`** match what the app shows.
- **`schedule` / `notifyOnCompletion`** record the live registration so the file is self-describing. Nothing enforces them; if you change them here, push the change live.
- **The body** (everything after the frontmatter) is the literal `prompt` argument passed to the MCP tool.

## Push-live ritual (MCP push, manual)

After editing a task file and committing it:

- **New task:** `create_scheduled_task(taskId=<name>, description=<description>, cronExpression=<schedule>, notifyOnCompletion=<flag>, prompt=<body>)`
- **Prompt-only change:** `update_scheduled_task(taskId=<name>, prompt=<body>)`
- **Schedule / notify change:** `update_scheduled_task(taskId=<name>, cronExpression=<schedule>)` or `(notifyOnCompletion=<flag>)`

Ask Claude in any session to "push the agent-viz-sweep task live" and it will read the body here and make the call. The cron and notify flag live only in the app store, so they must go through the tool.

## Notes

- Tasks run only while the desktop app is open. If it was closed when a task was due, it runs on next launch.
- Each run is a fresh session with no memory of prior runs or of the conversation that created it. **The prompt body must be fully self-contained.**
- Routines never commit. They leave edits in the working tree for review (`git diff`).
- **Run mode must be set in the desktop UI, per task, per machine.** Unattended running needs auto / bypass-permissions mode, or it stalls on permission prompts mid-run. This is app-local state, not captured here and not settable through the MCP tools, so it does not travel with the repo. Set it in the app's Scheduled section after registering.
- **The app applies random jitter of a few hundred seconds**, so the time it displays will not match the cron minute in the frontmatter. `7 4 * * 6` currently shows as 04:16. The cron is the source of truth; the displayed time is not a discrepancy to fix.
- Tool approvals granted during a run are stored on the task and reused. Clicking "Run now" once pre-approves what the routine needs, which stops later unattended runs pausing on prompts.

## Tasks

- **`agent-viz-sweep`** — weekly research sweep. Finds **one** paper, **one** chart type, and **one** person or style guide worth a page, plus a light staleness check against changed norms and standards. Deliberately capped at one of each. Saturday 4:07am local (`7 4 * * 6`), an hour after the hiveplotlib routines so the three do not compete, and inside the same pre-token-reset window.
