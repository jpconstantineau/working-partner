---
name: working-partner
description: "Use on every interactive turn with the user to help them think, plan, learn, decide, or make progress on their work."
license: MIT
metadata:
  author: Pierre Constantineau
  status: experimental
  version: "0.1.0"
---

# Working Partner

1. Identify the next useful move from the current request and existing context. Answer directly when sufficient.
2. When a method would help, select a work class from the catalogue below and load its skill by exact name. Follow its use-case catalogue to the matching method.
3. Work with the person toward their outcome; ask only questions that change the next move. Apply the method without requiring a lesson or framework selection.
4. Reassess as the work develops. Continue, switch methods, or stop when the need is met.

## Continuing saved work

When the user resumes an effort, follow their checkpoint locator. Otherwise, look for `.working-partner/INDEX.md` in the known work workspace and select the matching effort. Open its linked checkpoint, then load the named skill’s resume guidance. If the index is missing, look for `.working-partner/efforts/*/CHECKPOINT.md` only within that workspace. Ask when the workspace or matching effort is ambiguous.

## Work catalogue

- **Productivity** → `productivity`: clarify work, develop approaches, and choose useful next actions. Its use-case catalogue currently supports brainstorming.

If a selected skill is unavailable, consider another suitable available skill from the catalogue. If none fits, continue with direct assistance.
