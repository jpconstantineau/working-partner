# Resume Natural Planning purpose and principles

## Workspace and file names

Resolve work-state paths from the user's chosen **work workspace**, never from the installed skill directory. Reuse an established private project workspace or explicitly designated private store. If none is established, ask where to keep the work before creating files. In chat-only environments, provide an unsaved checkpoint instead.

Within that workspace, use:

- `.working-partner/INDEX.md`: one-line entries linking each effort's checkpoint; the index helps select an effort, not duplicate its contents.
- `.working-partner/efforts/YYYY-MM-DD-<topic-slug>/CHECKPOINT.md`: current outcome, progress, decisions, evidence gaps, and next step.

Use the local date on which the effort starts and a short lowercase, hyphen-separated topic slug, for example `2026-11-09-workshop-venue`. Keep that directory name on later sessions. Reuse the same effort when continuing; for a distinct effort with a colliding name, choose the next unused suffix `-02`, `-03`, and create without overwriting. Do not rename an effort just because the wording of its title changes.

Create files only when there is useful state to preserve. Copy the blank [checkpoint template](templates/CHECKPOINT.md), then fill them from actual work. Template links resolve from this skill; the populated copies belong in the work workspace. Never place personal work state in this public collection, installed skills, or published `docs/`. A hidden folder is not private by itself: verify the destination is not shared, committed, or automatically published before storing personal work. Use the selected store's permissions rather than altering them implicitly.

If an established store uses different paths or document IDs, retain its convention. Record the exact index/checkpoint/support locators in the checkpoint and the conversation handoff; do not create a second local copy merely to match this layout.

## Save a checkpoint

1. Read the current checkpoint and any linked supporting work. Preserve user edits; reread if another writer changed them.
2. Update CHECKPOINT.md with the current stage, accepted output, tentative proposals, unresolved decisions, evidence gaps and exact next useful move. Record an ISO 8601 timestamp with timezone. Link existing support rather than copying it.
3. Read back and verify the checkpoint, then update the index entry: title linked to `efforts/<effort-id>/CHECKPOINT.md`, status (active, paused, completed or superseded), timestamp and next step. Verify the index too.
4. Return the exact verified locator. Report partial failures precisely; an index entry alone is not proof of saved work.

Completing this stage does not complete the project. Preserve other stages’ accepted output in the same effort. Do not overwrite an existing idea pool or plan when switching stages. Keep factual summaries, not transcripts or reasoning dumps.

## Find and resume

1. Prefer an explicit checkpoint link/path from the user or current handoff. Otherwise, in the known work workspace, open `.working-partner/INDEX.md`.
2. Select the entry matching the current project/question. If multiple entries fit, ask which effort to resume rather than choosing by recency alone.
3. If the index is absent, stale, or has a broken link, list only `.working-partner/efforts/*/CHECKPOINT.md` within that workspace and inspect the candidate headers. Do not scan unrelated directories. If nothing matches or the workspace is unknown, ask for the workspace/checkpoint or continue without claiming to have recovered state.
4. Read the selected `CHECKPOINT.md`, then linked support and only the evidence needed for the next move. Confirm the workspace/project identity, current status, and facts marked for refresh.
5. Resume the recorded next move only if it still fits the current request. Load the recorded stage skill if available, or continue directly. For this stage use [SKILL.md](SKILL.md). Do not restart earlier stages solely because the user entered here. Preserve superseded decisions and reasons for change.
6. For completed or superseded efforts, reuse the useful output without automatically reopening purpose and principles. An explicit new objective can start a new effort linked to the previous one.

An orphan checkpoint can be added back to the index after its identity and contents are verified. Resolve disagreement between the index and checkpoint from the actual work and latest user direction, not a timestamp alone.
