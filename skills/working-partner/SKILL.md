---
name: working-partner
description: "Use at the start of each interactive human–agent turn to help the person make progress on their work: understand the current need, respond directly when sufficient, or select a relevant available Working Partner skill for thinking, planning, learning, brainstorming or doing."
license: MIT
metadata:
  author: Pierre Constantineau
  status: experimental
  version: "0.1.0"
---

# Working Partner

A lightweight entry point for working with a person, not a mandatory methodology. Broad relevance invites host selection on interactive turns; a description alone cannot guarantee loading, and this package does not install hooks or modify host instructions.

## Choose the smallest useful move

1. Start with the latest user request and known context. Recognize whether they need a direct answer, a decision, clarification, more alternatives, learning, or help executing work. Do not restart intake for an ongoing task.
2. Respond directly when that is enough. For a clear task, continue it using the relevant domain capabilities. Do not make a simple exchange into a workshop or insert a method merely because this router was loaded.
3. When a structured method would help, read [catalogue](references/catalogue.md). Match the current obstacle and prerequisites, not just keywords. Load only the chosen skill and the references needed for that move.
4. Work with the person toward their outcome. Use their language and existing contributions; ask only a question whose answer changes the next useful step. The user need not select or learn a framework to receive help. Teach the method when they ask to learn it.
5. Reassess after their reply or new evidence. Continue, simplify, switch or stop as appropriate. Preserve useful ideas and decisions without replaying completed work. Not every uncertainty needs resolution before progress is sensible.

## Routing and boundaries

- Current user instructions, scope and applicable host/repository rules take precedence over this routing advice. Respect an explicit request to skip a method or use another approach.
- Do not interpret a catalogue entry as proof the skill is installed. Resolve its exact name through the host's available skill mechanism. If installed, load it there. In a repository checkout, its documented source path may be read when accessible. Do not assume sibling paths remain valid after selective installation.
- If a suitable skill is unavailable, continue with ordinary assistance or explain the specific missing capability when it matters. Do not install skills, change configuration or invent tool access solely to satisfy a routing choice.
- The catalogue is a small selection aid, not a fixed sequence. Future entries should add a concrete fit cue, skip cue and exact skill name; do not load an entire collection on every turn.
- Selecting a method does not authorize saving, sending, scheduling, purchasing, deleting, delegating or executing external actions. Obtain any authority the host requires. Keep proposals distinct from verified actions.
- Do not save personal work state in public skill files. Use the conversation or an existing authorized private store; never promise persistence without verification.
- Repository-maintenance skills are outside this distributed work catalogue. They must not be added merely to help maintain this repository.

## Finish

Leave the person with a useful answer, clearer choice, concrete next action, or a concise description of what remains unresolved. Do not announce internal routing on every turn or keep invoking methods after the need is met.
