# Contributing

## Naming and routing

Name method skills **class-use-method-tool**, ordered along the selection path: `productivity-brainstorming-gtd-npm`. Category routers use the matching prefix: `productivity`, then `productivity-brainstorming`. The interactive entry point is `working-partner`.

Keep the work-class catalogue in the entry-point skill, the use-case catalogue in the class router, and the method catalogue in the use-case router. Name exact target skills and explain when they fit. If a target is unavailable, consider another suitable available catalogue entry before falling back to direct assistance.

Category routers describe the full use case, not only the first listed method. Brainstorming includes non-project work; keep project prerequisites on project-specific methods.

## Audiences and placement

- Write agent skills as concise operational instructions, with references loaded at the point of need. Keep identity and invocation metadata in frontmatter.
- Label unfinished human learning pages simply “Work in progress.”
- Write README for people discovering and using Working Partner. Put implementation status, test limitations, migration history, and PR-specific details in the PR.
- Put human learning HTML in `docs/`; GitHub Pages deploys `main` / `docs`. Keep source-assessment and attribution notes in page footers.
- Put attribution in `Attributions.md`, source details with the method reference, and license explanations in `Licenses.md`. Keep one root `LICENSE`; distribution tooling must include that notice.
- Treat Working Partner as the product's home. Avoid references to earlier repository packaging and redundant machine-readable source records.
- Keep maintenance tooling and skills separate from the distributed collection. Stable and experimental distribution must be explicit; folder names alone do not enforce installer discovery boundaries.

## Continuity conventions

Stateful skills must identify their work workspace, exact state filenames, naming format, saved content, and resume lookup order. Use `.working-partner/INDEX.md` and stable dated effort directories by default; preserve an established store instead of duplicating it. Keep blank templates inside the skill and populated state in the user’s private work workspace. A resume path should handle missing indexes, multiple matches, and incomplete saves.

## Checks

Run `python3 scripts/check.py` for metadata, naming, layout, and local-link checks, then `npx skills@latest add . --list` for installer discovery. Test real installation and host behavior separately; discovery alone proves neither.
