# spain2027

Planning workspace for a 2027 relocation to Spain and graduate program applications.

## Agent

`.claude/agents/relocation-grad-advisor.md` defines the `relocation-grad-advisor` subagent. Claude Code picks it up automatically for relocation and application tasks, or invoke it directly by asking for the relocation-grad-advisor agent.

## Layout

- `plan/profile.md`: who, target, decisions made, hard rules for programs
- `plan/relocation/`: timeline, document checklist, budget, Spanish plan, providers, reading
- `plan/programs/`: one file per program, `tracker.md`, `eliminated.md`
- `plan/documents/`: drafts of application materials
- `plan/context/`: exports of prior chats the agent reads for background
- `plan/deadlines.md`: every dated item, with confidence and source
- `plan/monthly-plan.md`, `plan/daily-template.md`, `plan/daily/`: monthly and daily action items
- `plan/workstreams/`, `plan/trip/`, `plan/outreach/`: income continuity, October 2026 trip, Salesforce partner outreach
- `plan/decisions.md`: decision log

## Shared project table

Notion database "Spain 2027 Project Plan" under the "Project Spain 2027" page: https://app.notion.com/p/1fe2872fe1794e5f9b03460f0c861c30. One row per dated item, mirrored from `plan/deadlines.md` and the workstream target tables. The agent updates both.

## Commands

`/today`, `/month`, `/deadlines`, `/status` in Claude Code, defined in `.claude/commands/`.
