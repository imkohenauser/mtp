---
title: MTP Skill (beta)
description: Add MTP Skill and run your first /mtp command, with links to installation, command reference, customization, and output comparisons.
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
- [Installation guide](/skills/mtp/install/)
- [Command reference](/skills/mtp/reference/)

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

All three modes resolve to the same internal shape: MTP axis, polarity, and intensity. More detailed behavior is covered in the [command reference](/skills/mtp/reference/).

## Next pages

- [Installation](/skills/mtp/install/): add MTP Skill by ZIP or CLI.
- [Command reference](/skills/mtp/reference/): sliders, grid coordinates, presets, multiple arguments, neutral values, and invalid input.
- [Customization](/skills/mtp/customize/): edit node definitions and presets for custom skill behavior.
- [MTP overview](/foundational/overview/): learn the framework terms behind MTP.
- [Comparisons](/comparisons/): review qualitative output comparisons.

## Beta

MTP Skill is in beta. The basic `/mtp <arguments>` formats are usable, but node definitions and constraint expressions may change as comparison tests accumulate.

For strict comparison records, save the MTP Skill version, model name, prompt, and `/mtp` arguments together.

## License

MIT License
