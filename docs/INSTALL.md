# Installing ARCHON

ARCHON is a Claude Code plugin — a `skills/` + `agents/` + `commands/` bundle following the `.claude-plugin/plugin.json` convention. It is not a standalone binary; it runs inside the `claude` CLI.

## Requirements

- The `claude` CLI (Claude Code) installed and authenticated.
- Git, to clone this repository.

## Option 1 — Local Plugin Directory (recommended for now)

Claude Code loads plugins from a local directory. Clone ARCHON and point Claude Code at it:

```bash
git clone https://github.com/Pouya-Mansournia/ARCHON.git
cd ARCHON
```

Then load it as a local plugin per your Claude Code version's plugin-loading mechanism (consult `claude --help` or your Claude Code settings for the current local-plugin flag/path — this varies across Claude Code releases and is intentionally not hardcoded here to avoid documenting a flag that drifts out of date).

## Option 2 — Plugin Marketplace

If you maintain a private or team plugin marketplace, add this repository as a marketplace entry pointing at the `.claude-plugin/plugin.json` manifest in this repo's root, then install ARCHON the same way you install any other marketplace plugin.

## Verifying the Install

Once loaded, confirm ARCHON is available:

```bash
claude
> /archon what's the right default backend stack for a B2B SaaS MVP?
```

If the `/archon` command and its siblings (`/archon-cto`, `/archon-principal`, `/archon-robotics`, `/archon-ai`, `/archon-review`, `/archon-plan`, `/archon-reflect`) autocomplete and respond, the plugin is correctly installed. See `docs/QUICKSTART.md` for a guided first session.

## Updating

```bash
cd ARCHON
git pull origin main
```

Check `CHANGELOG.md` after updating for any behavior changes, and `VERSIONING.md` for how ARCHON's versioning works.

## Uninstalling

Remove ARCHON from wherever your Claude Code plugin configuration points (the local directory or marketplace entry) and delete the cloned repository. ARCHON does not write any state outside this repository directory — there's no separate cleanup step.
