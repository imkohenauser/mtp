---
title: MTP Skill (beta)
description: Install and use MTP Skill with the /mtp command, including sliders, grid coordinates, presets, and argument interpretation.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/skills_mtp.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/skills_mtp.png
---

MTP Skill is an **Agent Skill** for environments that support **Agent Skills**, built on the MTP (Mapping the Prompt) framework. After installation, invoke it through the `/mtp` slash command with arguments. Arguments (`<args>`) cover two ways to write settings—**slider (intensity)** and **grid (coordinates)**—plus **presets** that bundle grid coordinates as shortcuts, for three specification modes in total. Those arguments are interpreted as **constraints** that shape model tone and structure. Sliders and grids both use **nodes** as defined in MTP. Framework-wide ideas and vocabulary are in [Overview](/foundational/overview/).

This page summarizes how to install MTP Skill, how to write the command, and how `/mtp <args>` is interpreted.

> [!NOTE]
> MTP does not change the model’s internals. The effect of `/mtp <args>` varies with the base model and the task.

---

## Installation

MTP Skill is packaged as an Agent Skill. Ordinarily, Skills run from tooling such as IDEs or CLI clients. You can also zip the MTP repository’s `skills/mtp` folder and upload it from Claude.ai’s Skill customization UI to use MTP Skill from the Claude web client or iOS app.

### Adding from the CLI

These instructions focus on installing from the CLI.

#### GitHub CLI (`gh`)

```bash
gh skill install imkohenauser/mtp skills/mtp
```

[GitHub CLI `gh skill` documentation](https://cli.github.com/manual/gh_skill) ↗

#### Vercel Skills CLI (`npx skills`)

```bash
npx skills add imkohenauser/mtp --skill mtp
```

[Vercel Skills CLI documentation](https://skills.sh/docs/cli) ↗

---

## Usage

`/mtp` is recognized whether it appears at the start, middle, or end of a message, or on its own line. If you include it more than once in the same message, each occurrence is interpreted together in order, and the `/mtp` lines are stripped from the prompt body.

For example, the following two forms differ only in where `/mtp` sits; the constraints produced by the compiler are the same:

```markdown
/mtp power:100 Please summarize the document.
```

```markdown
Please summarize the document. /mtp power:100
```

How the model weighs constraints versus the rest of the prompt is model-dependent; position can still slightly change the output.

### Input modes

The three modes are written as follows.

| Mode | Pattern | Examples |
| ----------- | ------------------------------------------ | -------------------------------- |
| **Slider** | `node:intensity` (intensity 0–100) | `power:100`, `void:80`, `grow:50` |
| **Grid** | `column:row` or `column-row` (19×19 grid; columns A–S, rows 1–19) | `J:4`, `J:1`, `F:10` |
| **Preset** | Named bundles of predefined coordinates | `strategist`, `synthesizer`, `maverick`, `concierge` (four presets) |

Besides node names, you can refer to **axis colors** (for example, `yellow:70` resolves like `open:70`). Negative intensity resolves to that axis’s Side B node (for example, `yellow:-70` behaves like `still:70`). More examples appear in `skills/mtp/USAGE.md`.

### Example patterns

The three modes can be used alone or combined. Typical patterns:

**Slider**

```markdown
/mtp power:100 Please summarize the document.
```

This sets slider `power` to intensity `100`. The output tends toward a decisive, conclusions-first shape.

**Grid**

```markdown
/mtp J:4 Please summarize the document.
```

This selects a single point on the 19×19 grid. The compiler derives axis and intensity from distance and polarity from position. (`J:4` compiles the same as `power:100`.)

**Preset**

```markdown
/mtp strategist Please summarize the document.
```

`strategist` expands to a predefined set of coordinates before interpretation (definitions in `references/presets.yaml`).

**Multiple grid points**

```markdown
/mtp D:16 A:1 Please summarize the document.
```

Multiple grid coordinates are applied in order. (`D:16 A:1` matches the token sequence that the `synthesizer` preset expands to, with the same compile result.)

**Same-axis override (last token wins)**

```markdown
/mtp power:70 void:30 Please summarize the document.
```

`power` and `void` share the same axis (Red attribute). If several tokens target the same axis, the later one wins (here, `void:30` is effective).

For invalid tokens, neutral grid handling, overwriting after presets, and other behavior, see the sections in `skills/mtp/USAGE.md`.

---

## Output comparisons

Pages under **Comparisons** show how outputs change when MTP Skill is applied, for both text generation and image generation.

[Go to the Comparisons section](/comparisons/) →

---

## License

MIT
