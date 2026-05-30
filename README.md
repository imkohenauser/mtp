![MTP Doc OGP Image](public/ogp.png)

# MTP (Mapping the Prompt)

MTP is a framework for steering LLM output with grids, sliders, and presets instead of long natural-language behavior instructions.
It is designed to make the ideas and concepts in a prompt easier to express intuitively, helping the user and the LLM align with fewer instructions.


## What is MTP?

Traditionally, changing an AI's tone or behavior often relies on natural-language instructions such as "Act as an expert," "Be more concise," or "Think step by step." These instructions can be ambiguous and may add prompt-side noise that is unrelated to the core task.

MTP moves that behavioral steering into non-verbal parameters such as color, position, and intensity. The MTP Skill makes this framework available through the `/mtp` command, compiling those settings into structured constraints that act as a reasoning-steering filter.

- **Adjust like an EQ** — e.g. `power:100`, `flow:70`, or a grid coordinate such as `J:10`
- **Blend like a Mixer** — named presets (`synthesizer`, `strategist`, …) or explicit multi-grid tokens (e.g. `D:16 A:1`)
- **Change the vibe, not the task** — shift depth, structure, and tone while keeping the base prompt intent intact

```text
/mtp power:100 Summarize this article
/mtp flow:70 Explain this concept
/mtp strategist Compare these options
```

MTP does not change the task itself. It adjusts qualities such as force, flow, depth, structure, openness, and focus.

### How MTP arguments map visually

MTP currently works through the `/mtp` command, but its arguments can be understood visually.

The slider form, `/mtp <node:intensity>`, sets the intensity of a named node such as `power:70` or `flow:100`. The grid form, `/mtp <column:row>`, selects a point on the 19×19 MTP coordinate plane, such as `J:4` or `D:16`.

Both forms describe the same underlying node system: sliders express movement by named direction and intensity, while grid coordinates express position.

---

## MTP Skill quick start

### Install

```bash
# GitHub CLI
gh skill install imkohenauser/mtp skills/mtp

# Vercel Skills CLI
npx skills add imkohenauser/mtp --skill mtp
```

Any **Agent Skills**–compatible host can load the skill; **import steps** differ by vendor — follow your client’s current documentation.

**Requirement:** Python 3 (standard library only — no extra packages).

### Usage

Control the model with sliders, grid coordinates, or presets.

```text
/mtp power:100                  → Moderate force; clearer, more assertive output
/mtp flow:70                    → Full flow; smooth, connected prose
/mtp J:4                        → Equivalent steering to /mtp power:100 (grid coordinate)
/mtp D:16 A:1                   → Multi-grid coordinates
/mtp strategist                 → Preset blend
```

For platform notes, `/mtp` syntax reference, and **References** (CLI docs), see [skills/mtp/README.md](./skills/mtp/README.md).

---

## Documentation

Product documentation, reference, and optional reading are on the documentation site below.

**[MTP Docs (Mapping the Prompt documentation site)](https://mappingtheprompt.com/)** ↗

---

## Roadmap

- [x] MTP Framework concept [alpha] — 2025-09-01
- [x] MTP Skill [beta] — 2026-03-15
- [x] MTP Docs (Mapping the Prompt documentation site) — 2026-05-05
- [ ] MTP Playlist Skill [in progress]
- [ ] MTP Interactive UI [planned]

---

## License

MIT — [LICENSE](./LICENSE).
