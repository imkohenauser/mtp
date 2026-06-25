---
title: MTP Skill (beta)
description: Add MTP Skill, run your first /mtp command, and reference the full input formats for sliders, grid coordinates, presets, multiple arguments, neutral values, and invalid input.
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

MTP Skill is an **Agent Skill** for steering LLM output through the `/mtp` command.

Instead of adding long natural-language behavior instructions to the prompt body, MTP Skill converts short settings such as `power:70`, `J:4`, or `maverick` into constraints that shape tone, structure, and exploration depth.

- [Download MTP Skill zip](/downloads/mtp-skill.zip)
- [Installation guide](/skills/)

---

## First commands

Try one of these prompts after adding MTP Skill.

```text
/mtp power:70
Summarize this text in a shorter form.
```

```text
/mtp focus:70
List the important effects of this specification change.
```

```text
/mtp maverick
Expand the possibilities for this plan.
```

## Input modes

| Mode | Example | Use |
| --- | --- | --- |
| Slider | `/mtp power:70` | Specify a tendency and intensity directly |
| Grid | `/mtp J:4` | Specify a point on the 19x19 MTP grid |
| Preset | `/mtp maverick` | Call a named combination of coordinates |

All three modes resolve to the same internal shape: MTP axis, polarity, and intensity. The sections below describe the full input formats.

## Basic form

```text
/mtp <arguments>
<prompt>
```

`/mtp` can appear at the start, middle, or end of a message.

```text
/mtp power:70
Summarize this text.
```

```text
Summarize this text. /mtp power:70
```

If several `/mtp` segments appear in one message, their arguments are merged in source order and the `/mtp <arguments>` parts are removed from the prompt body.

## Node names

Each MTP axis has a Side A node and a Side B node. Positive values activate Side A. Negative values activate the opposite side.

| Axis | Side A | Side B |
| --- | --- | --- |
| Yellow | `open` | `still` |
| Red | `power` | `void` |
| Magenta | `return` | `surge` |
| Green | `grow` | `wither` |
| Transparent | `helix` | `collapse` |
| White | `focus` | `haze` |
| Cyan | `enter` | `drift` |
| Blue | `flow` | `abyss` |
| Purple | `close` | `fade` |

For conceptual descriptions of the nodes, see [Node Reference](/foundational/node-reference/).

## Slider

```text
/mtp <node>:<intensity>
```

`<intensity>` is a value from `0` to `100`.

```text
/mtp power:70
/mtp focus:30
/mtp flow:50
```

Negative values activate the opposite side of the same axis.

```text
/mtp power:-70
```

The same axis can also be specified by color name. A positive color value activates Side A, and a negative color value activates Side B.

```text
/mtp yellow:70
/mtp yellow:-70
```

For the Yellow axis, `yellow:70` is equivalent to `open:70`, and `yellow:-70` is equivalent to `still:70`.

## Grid

```text
/mtp <column>:<row>
```

The MTP grid is 19x19.

- Columns: `A` to `S`
- Rows: `1` to `19`
- Center: `J:10`

```text
/mtp J:4
/mtp D:16
/mtp A:1
```

Hyphen form is also accepted.

```text
/mtp G-10
```

The compiler calculates axis, polarity, and intensity from the coordinate. `J:10` is the neutral center and does not emit an active constraint.

For the full coordinate model, see [Grid and Coordinate System](/foundational/grid-and-coordinate-system/).

## Preset

Presets expand to predefined MTP tokens before parsing.

| Preset | Expansion |
| --- | --- |
| `synthesizer` | `D:16 A:1` |
| `strategist` | `P:16 P:4` |
| `maverick` | `D:4 A:19` |
| `concierge` | `J:13 D:10` |

```text
/mtp synthesizer
Outline the key points.
```

Preset definitions are maintained in `skills/mtp/references/presets.yaml`.

## Multiple arguments

Different axes can be combined.

```text
/mtp open:30 flow:30
Adjust this draft for readability.
```

Multiple `/mtp` segments are merged in order.

```text
Summarize this text. /mtp power:70 /mtp haze:30
```

## Same-axis conflicts

If several tokens target the same axis, the last token wins after preset expansion.

```text
/mtp power:70 void:30
```

In this example, both tokens target the Red axis, so `void:30` is effective for that axis.

## Neutral values

These inputs are valid, but they do not generate active constraints.

```text
/mtp power:0
/mtp yellow:0
/mtp J:10
```

## Invalid input

Invalid tokens are ignored.

```text
/mtp foobar:20
/mtp haze:xx
/mtp G:10foo
```

Depending on the host, warnings may appear in execution logs.

## Help commands

When the host exposes command output, these helper commands can be used.

```text
/mtp help
/mtp help sliders
/mtp help grid
/mtp help presets
/mtp list
/mtp list presets
```

## Implementation references

Detailed examples and compiler checks are available in [`skills/mtp/USAGE.md`](https://github.com/imkohenauser/mtp/blob/main/skills/mtp/USAGE.md).

## Next pages

- [Installation](/skills/): add MTP Skill by ZIP or CLI.
- [Customization](/skills/mtp/customize/): edit node definitions and presets for custom skill behavior.
- [MTP Playlist Skill](/skills/mtp-playlist/): build a node-mapped music sequence from a theme.
- [MTP overview](/foundational/overview/): learn the framework terms behind MTP.
- [Comparisons](/comparisons/): review qualitative output comparisons.

## Beta

MTP Skill is in beta. The basic `/mtp <arguments>` formats are usable, but node definitions and constraint expressions may change as comparison tests accumulate.

For strict comparison records, save the MTP Skill version, model name, prompt, and `/mtp` arguments together.

## License

MIT License
