---
title: MTP Skill (beta)
description: Understand what MTP Skill changes, what beta means, and how to install and use the /mtp command with sliders, grid coordinates, presets, and argument interpretation.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/skills_mtp.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/skills_mtp.png
lastUpdated: true
---

MTP Skill is an **Agent Skill** for using the MTP (Mapping the Prompt) framework through the `/mtp` command.

Instead of writing long natural-language meta-instructions in the prompt body, MTP Skill converts short settings such as `power:100`, `J:4`, or `synthesizer` into **constraints** that shape model tone, structure, and depth of exploration. Arguments (`<args>`) can be written in three modes: **sliders**, **grid coordinates**, and **presets**. Regardless of the format, they ultimately resolve to an MTP axis, polarity, and intensity. Framework-wide ideas and vocabulary are covered in [Overview](/foundational/overview/).

This page explains what changes when you use MTP Skill, what `(beta)` means, how to install it, how to write the command, and how `/mtp <args>` is interpreted.

> [!NOTE]
> MTP does not change the model’s internals. The effect of `/mtp <args>` varies with the base model and the task. MTP Skill also continues to update its node definitions and constraint expressions.

---

## What MTP Skill changes

MTP Skill lets you steer output in a separate layer from the prompt body. For example, with the same task, “Please summarize this article,” adding `/mtp power:100` tends to move the answer toward a conclusion-first, strongly structured form, while `/mtp void:80` tends to strip the answer down to a minimal form.

This gives you a way to control output through MTP coordinates and node names instead of repeatedly writing natural-language additions such as “make this more assertive,” “make it shorter,” “open up the possibilities,” or “focus the scope.” The task and the output style control are separated, so you can keep the same prompt while comparing how the output changes. It can also be applied to persona control for subagents and similar agent patterns.

In MTP, nodes such as Power, Flow, Focus, and Open can be understood as meaningful types: clusters of tone and style. `power:50` or `focus:70` passes an intensity value for how strongly the output should lean toward that type. You can switch output tendencies with a single node, or blend tendencies by combining multiple nodes.

MTP uses color as a visual coordinate system for representing how these types are arranged and related. Rather than assigning fixed meanings to colors themselves, it treats color as a cue for understanding output tendencies on a map. For more detail, see [Design Background](/optional/design-background/).

| Setting | Output tendency |
| --- | --- |
| `/mtp power:100` | Conclusion-first, assertive output with a clear claim |
| `/mtp void:80` | Concise, minimal output with less explanation |
| `/mtp open:70` | Output that expands possibilities and alternatives |
| `/mtp focus:70` | Output that narrows the target and prioritizes precision |
| `/mtp D:16 A:1` | Output shaped by multiple grid coordinates |

To adjust strength, combine a node name with `:intensity`, such as `power:50` or `power:100`. The actual change depends on the model, task, and prompt body. Intensity is also handled differently across models, so the same `:intensity` value can surface differently in the output.

MTP Skill does not fully lock the output. It is a layer for connecting constraints passed to the model with reusable types: meanings and concepts that can be invoked again.

---

## Installation

MTP Skill is distributed as an Agent Skill. Ordinarily, Skills are used from developer tools such as IDEs and CLI clients. At the moment, you can also upload a zipped Skill through Claude.ai’s customization settings or the Skills management page in Manus.im, which makes Agent Skills available from web and iOS app surfaces. To use MTP Skill this way, zip the `skills/mtp` directory from the MTP repository and upload it.

### Adding from the CLI

These instructions focus on installing from the CLI.

#### GitHub CLI (`gh`)

The GitHub CLI `gh skill` command is a preview feature. Check whether your installed `gh` version has `gh skill` enabled.

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

`/mtp` is recognized whether it appears at the start, middle, or end of a message, or on its own line. If you include it more than once in the same message, each occurrence is interpreted together in order, and the `/mtp <args>` parts are stripped from the prompt body.

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

## About beta

The `(beta)` label means that MTP Skill, and especially the core descriptions in `skills/mtp/nodes/*`, will continue to be tested and updated.

The current node definitions describe each color axis and its Side A / Side B behavior in Markdown. The basic `/mtp <args>` input formats, preset expansion, and same-axis override behavior work today, but node-level descriptions and constraint expressions are expected to evolve as comparison tests accumulate.

Future adjustments will focus less on adding direct text instructions and more on expressing the character of each color and node in a more universal way. In other words, instead of fixed commands like “use this ending” or “write in this exact format,” the goal is to make qualities such as Power, Flow, Focus, and Open carry more consistently across models and tasks.

If you need strict comparison records, save the MTP Skill version, model name, prompt, and `/mtp <args>` together. The comparison pages follow that assumption when placing baselines next to MTP Skill outputs.

---

## Customizing node definitions

MTP Skill’s output tendency can be adjusted through the node definitions in `skills/mtp/nodes/*`. These files are not just documentation; they are source material that the compiler reads and uses as constraints.

Users who want to customize MTP Skill can edit `skills/mtp/nodes/*` to change the behavior of MTP Skill itself, much like changing a theme. For example, even with the same `/mtp power:100`, changing the Power-side text in `skills/mtp/nodes/RED.md` can move the output in a different direction.

When customizing nodes, keep each node file’s basic structure intact. The frontmatter, `## Side A`, `## Side B`, and each side’s `### Low`, `### Mid`, and `### High` headings are part of the structure the compiler expects to read.

---

## Output comparisons

Pages under **Comparisons** show how outputs change when MTP Skill is applied, for both text generation and image generation.

[Go to the Comparisons section](/comparisons/) →

---

## License

MIT
