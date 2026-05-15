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

## Installation

MTP Skill is distributed as an Agent Skill. You can install it from the CLI, or download the official zip and upload it to tools that support zipped Agent Skills.

### Download zipped Skill

You can download the latest packaged MTP Skill as a zip file:

[Download MTP Skill zip](/downloads/mtp-skill.zip) ↓

This zip contains the `mtp` Skill package built from the repository directory `skills/mtp`.

<!-- For versioned packages and release notes, see GitHub Releases:

[View MTP Skill releases on GitHub](https://github.com/imkohenauser/mtp/releases) ↗

MTP Skill release tags use the `mtp-vX.Y.Z` format. The `v1` family label groups MTP-related Skills that share the same major release line.

Release metadata is also available as JSON:

[`/downloads/release.json`](/downloads/release.json) -->

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


**Slider**

```markdown
/mtp power:100 Please summarize the document.
```

This sets slider `power` to intensity `100`. The output tends toward a decisive, conclusions-first shape.
The three modes can be used alone or combined. Typical patterns:

![Diagram explaining MTP slider arguments using /mtp node:intensity. The left panel shows node sliders for Side A and Side B with Power set to 70. The right panel shows node intensity as 3D Chebyshev distance, with labeled directions such as Open, Power, Focus, Flow, Close, Surge, Collapse, and Fade.](/images/pages/mtp-slider-arguments-mtp-node-intensity.png)

**Grid**

```markdown
/mtp J:4 Please summarize the document.
```

This selects a single point on the 19×19 grid. The compiler derives axis and intensity from distance and polarity from position. (`J:4` compiles the same as `power:100`.)

![Diagram explaining MTP grid arguments using /mtp column:row. The left panel shows a simplified 3×3 color grid projected onto a 19×19 coordinate grid, with example coordinates such as J:4, D:10, P:10, and J:16. The right panel shows RGBA color values across the full 19×19 grid.](/images/pages/mtp-grid-arguments-mtp-column-row.png)

**Preset**

```markdown
/mtp strategist Please summarize the document.
```

Presets expand to predefined coordinate sets before interpretation. The current presets are:

| Color | Preset | Expansion |
| --- | --- | --- |
| <div class="dot-sm bg-close" aria-label="purple"></div><div class="dot-sm bg-return" aria-label="magenta"></div> | `strategist` | `P:16 P:4` |
| <div class="dot-sm bg-enter" aria-label="cyan"></div><div class="dot-sm bg-still" aria-label="yellow"></div> | `synthesizer` | `D:16 A:1` |
| <div class="dot-sm bg-open" aria-label="yellow"></div><div class="dot-sm bg-drift" aria-label="cyan"></div> | `maverick` | `D:4 A:19` |
| <div class="dot-sm bg-j13" aria-label="blue"></div><div class="dot-sm bg-grow" aria-label="green"></div> | `concierge` | `J:13 D:10` |

Definitions are maintained in `references/presets.yaml`.

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

## Output comparisons

The examples below use the same base prompt while changing only the `/mtp` argument. They are not benchmark results; they are qualitative comparisons intended to show how different nodes and intensities shift the model’s output style.

For text generation, the comparison uses a short prompt about *Alice’s Adventures in Wonderland*. The Japanese version uses *Sanshirō* by Natsume Sōseki. For image generation, the prompt keeps the portrait composition constant while varying only the MTP intensity.

Pages under **Comparisons** show longer records of how outputs change when MTP Skill is applied, for both text generation and image generation.

[Go to the Comparisons section](/comparisons/) →

### Intensity comparison: Power

Increasing `power` makes the output more assertive and interpretive. At lower intensity, the response remains close to a conventional summary. At higher intensity, it becomes more declarative, opinionated, and editorial.

![Output comparison for Alice’s Adventures in Wonderland showing how increasing /mtp power changes the response style.](/images/examples/mtp-examples-claude-ai-story-of-alice-power.png)

### Intensity comparison: Surge

Increasing `surge` changes the rhythm more than the argument. The output becomes more kinetic, compressed, and forward-driving, with shorter beats and stronger movement through the scene.

![Output comparison for Alice’s Adventures in Wonderland showing how increasing /mtp surge changes rhythm and pacing.](/images/examples/mtp-examples-claude-ai-story-of-alice-surge.png)

### Node comparison at 70%

With intensity fixed at `70`, different nodes produce different output tendencies. `open` expands entry points, `focus` stabilizes the explanation, `void` strips the premise down, and `abyss` darkens the interpretive frame.

![Output comparison for Alice’s Adventures in Wonderland showing several MTP nodes at intensity 70.](/images/examples/mtp-examples-claude-ai-story-of-alice-various.png)

### Combined arguments and presets

Multiple arguments can be composed. Presets such as `maverick` and `concierge` package predefined coordinate patterns, producing more recognizable high-level behaviors than a single node alone.

![Output comparison for Alice’s Adventures in Wonderland showing combined MTP arguments and presets.](/images/examples/mtp-examples-claude-ai-story-of-alice-multiple.png)

### Image comparison: Portrait

The same argument style can also be used in image-generation prompts. Here, `power` is varied while the portrait composition is held constant, making the change appear mainly in the intensity of the eyes and expression.

![Image-generation comparison for a portrait of Mozart showing changes from different /mtp power intensities.](/images/examples/mtp-examples-gpt-image-2-portrait-of-mozart.png)

### Image comparison: Small bouquet

Here, the bouquet subject and occasion are held constant while the MTP node is varied, making the change appear mainly in the bouquet’s openness, density, pruning, wrapping, and overall mood.

![Image-generation comparison for a small bouquet showing changes from different MTP arguments.](/images/examples/mtp-examples-gpt-image-2-small-bouquet.png)

---

## License

MIT
