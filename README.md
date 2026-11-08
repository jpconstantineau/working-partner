# working-partner

Skills and methods for humans and AI to think, plan, and work together.

## First experimental skills

**Working Partner** is the lightweight [interactive entry-point/router](skills/working-partner/SKILL.md). It invites selection each interactive turn, answers directly when sufficient, and chooses a task method only when useful. Host activation is not guaranteed by its description.

**Natural Planning: brainstorming** is a GTD skill for expanding project options before organizing or selecting them. It is an independent adaptation of David Allen's Natural Planning Model, not official GTD training.

- Agent package: [productivity-gtd-npm-brainstorm](skills/productivity-gtd-npm-brainstorm/SKILL.md)
- Human learning material: [learning page on GitHub Pages](https://jpconstantineau.github.io/working-partner/gtd-npm-brainstorm.html) ([HTML source](docs/gtd-npm-brainstorm.html)). Pages is configured to publish `main` / `docs`; this page becomes available after this PR is merged and deployment succeeds.
- Attribution, sources and limits: [method reference](skills/productivity-gtd-npm-brainstorm/REFERENCE.md)

This seed contains exactly two experimental skills: the router and one GTD method. No stable release, native plugin or release pipeline is published yet.

## Preview skill discovery

After cloning and checking out the branch containing this skill:

```sh
npx skills@latest add . --list
```

To select both skills from that checkout, use the CLI's agent/scope selection:

```sh
npx skills@latest add . --skill working-partner productivity-gtd-npm-brainstorm
```

Discovery was tested on the local package. Installation, upgrades and host invocation still need testing. Do not assume a successful file copy guarantees agent invocation. Each skill can also be selected alone; the router handles an unavailable companion without broken local references or automatic installation.

Only `skills/` is intended to hold distributed human–AI work skills. Future repository-maintenance skills must remain separate and must not enter release manifests or distributed packages.

## License

Original Working Partner material is [MIT licensed](LICENSE). Method attribution and third-party source limits are recorded with the skill. Linked third-party works retain their own rights.
