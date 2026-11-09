---
name: productivity-purpose-gtd-npm
description: "Use when the project’s reason or guiding standards are unclear."
license: MIT
metadata:
  author: Pierre Constantineau
  status: experimental
  version: "0.1.0"
  method: "David Allen's Getting Things Done (GTD), Natural Planning Model"
  canonical-id: "gtd.npm-purpose-principles"
  invocation: "Agent-invoked or a standalone entry point; no earlier skill is required."
---

# Natural Planning: purpose and principles

Clarify why this undertaking matters and what must remain true about how it is done.

## Start from the user’s work

Reuse current context. Ask only for missing information that materially changes the next move; the user need not name or study the method. Enter here directly when this is the bottleneck, without rerunning earlier stages. Read [REFERENCE.md](REFERENCE.md) on first application or source uncertainty.

## Workflow

1. **Identify the project reason from the user’s actual context. Ask whose need it serves and why it is worth doing.**
   Done when: A short purpose statement is grounded in the user’s intent.
2. **Surface guiding principles, constraints and unacceptable trade-offs. Distinguish agreed standards from tentative or disputed proposals.**
   Done when: Each material principle has a source and agreement status.
3. **Check the purpose and principles against a real planning choice. Preserve disagreements for the appropriate person rather than deciding their values.**
   Done when: The user has a usable decision frame, with unresolved choices visible.

## Branches

- When principles conflict, expose the concrete trade-off and ask for the needed human priority. Separate fixed requirements from preferences.
- When the reason is already clear, apply it to the disputed choice instead of restarting an abstract why-question.

## Boundaries

Project purpose is not a life-purpose exercise. Do not supply the agent’s values or infer agreement from silence.

## Finish and optional next step

Stop when the requested output is useful. If the user wants to continue and the next gap fits, offer `productivity-outcomes-gtd-npm` as the next Natural Planning step. Carry forward the accepted output, constraints and open questions; do not restart intake. Load that skill only when continuing is useful. If the named skill is unavailable, use another fitting available method or help directly. Never require installing the rest of the sequence. A next-step suggestion is not permission to act.

For interrupted work read [STATE.md](STATE.md); use the same effort across stage handoffs. For a fictional worked example read [EXAMPLE.md](EXAMPLE.md).
