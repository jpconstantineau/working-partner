# Resume Natural Planning brainstorming

## Workspace and file names

Resolve work-state paths from the user's chosen **work workspace**, never from the installed skill directory. Reuse an established private project workspace or explicitly designated private store. If none is established, ask where to keep the work before creating files. In chat-only environments, provide an unsaved checkpoint instead.

Within that workspace, use:

- `.working-partner/INDEX.md`: one-line entries linking each effort's checkpoint; the index helps select an effort, not duplicate its contents.
- `.working-partner/efforts/YYYY-MM-DD-<topic-slug>/CHECKPOINT.md`: current outcome, progress, decisions, evidence gaps, and next step.
- `.working-partner/efforts/YYYY-MM-DD-<topic-slug>/IDEAS.md`: the idea pool with source, status, and evaluation notes.

Use the local date on which the effort starts and a short lowercase, hyphen-separated topic slug, for example `2026-11-09-workshop-venue`. Keep that directory name on later sessions. Reuse the same effort when continuing; for a distinct effort with a colliding name, choose the next unused suffix `-02`, `-03`, and create without overwriting. Do not rename an effort just because the wording of its title changes.

Create files only when there is useful state to preserve. Copy the blank [checkpoint template](templates/CHECKPOINT.md) and [idea-pool template](templates/IDEAS.md), then fill them from actual work. Template links resolve from this skill; the populated copies belong in the work workspace. Never place personal work state in this public collection, installed skills, or published `docs/`. A hidden folder is not private by itself: verify the destination is not shared, committed, or automatically published before storing personal work. Use the selected store's permissions rather than altering them implicitly.

If an established store uses different paths or document IDs, retain its convention. Record the exact index/checkpoint/ideas locators in the checkpoint and the conversation handoff; do not create a second local copy merely to match this layout.

## Save a checkpoint

1. Read the current checkpoint and idea pool, if present. Preserve user edits and reconcile changes; use conditional writes where supported. If another writer changed them, reread before updating.
2. Update `IDEAS.md` with stable idea IDs (`idea-001`, `idea-002`, …), sources and statuses. Preserve selected, rejected-for-now, and unassessed ideas distinctly.
3. Update `CHECKPOINT.md` with the accepted outcome and constraints, last completed move, decision references, remaining questions, and exact next useful action. Link the idea pool instead of copying it. Record an ISO 8601 update timestamp with timezone.
4. Read back both files and verify their contents. Then add or update the effort's entry in `INDEX.md` using this form: title linked to `efforts/<effort-id>/CHECKPOINT.md`, status (`active`, `paused`, `completed`, or `superseded`), last-updated timestamp, and one-line next step. Read back the index too.
5. Leave the verified workspace and checkpoint locator in the handoff. If a write failed, report which files were saved and which were not; do not present the index as proof of a successful checkpoint.

Keep only information needed to continue the work. Use factual summaries, not transcript or reasoning dumps. Completing brainstorming does not complete the project; retain the next decision separately.

## Find and resume

1. Prefer an explicit checkpoint link/path from the user or current handoff. Otherwise, in the known work workspace, open `.working-partner/INDEX.md`.
2. Select the entry matching the current project/question. If multiple entries fit, ask which effort to resume rather than choosing by recency alone.
3. If the index is absent, stale, or has a broken link, list only `.working-partner/efforts/*/CHECKPOINT.md` within that workspace and inspect the candidate headers. Do not scan unrelated directories. If nothing matches or the workspace is unknown, ask for the workspace/checkpoint or continue without claiming to have recovered state.
4. Read the selected `CHECKPOINT.md`, then its linked `IDEAS.md` and only the evidence needed for the next move. Confirm the workspace/project identity, current status, and facts marked for refresh.
5. Resume the recorded next step in [SKILL.md](SKILL.md) if it still fits the current request. Continue generation only when alternatives remain the gap; otherwise organize the existing ideas or use a better-fitting approach. Preserve superseded decisions and the reason for changing course.
6. For completed or superseded efforts, reuse the useful output without automatically reopening brainstorming. An explicit new objective can start a new effort linked to the previous one.

An orphan checkpoint can be added back to the index after its identity and contents are verified. Resolve disagreement between the index and checkpoint from the actual work and latest user direction, not a timestamp alone.
