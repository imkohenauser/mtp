---
title: MTP Docs
description: Documentation for MTP, a framework for steering LLM output through grids, sliders, and presets.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp.png
hero:
  title: MTP Is a Framework for Tuning LLM Output
  tagline: It uses sliders, grid coordinates, and presets to shape responses without rewriting the task itself.
  actions:
    - text: Start with MTP Skill
      link: /skills/mtp/
      icon: right-arrow
---

MTP (Mapping the Prompt) is a framework for steering LLM output with grids and sliders instead of long natural-language behavior instructions. It is designed to make the ideas and concepts in a prompt easier to express intuitively, helping the user and the LLM align with fewer instructions.

Its core is a 3x3 color arrangement made of nine nodes. The relationships between color, position, polarity, and intensity are defined from this arrangement.

```text
+-----------------+-----------------+-----------------+
| Yellow          | Red             | Magenta         |
+-----------------+-----------------+-----------------+
| Green           | Transparent     | White           |
+-----------------+-----------------+-----------------+
| Cyan            | Blue            | Purple          |
+-----------------+-----------------+-----------------+
```

MTP Skill is an Agent Skill for using the MTP framework through the `/mtp` command.

## What is MTP?

Traditional prompts often adjust model behavior through natural-language instructions like these:

```text
Act as an expert.
Be more concise.
Think step by step.
```

MTP moves that behavioral steering into non-verbal parameters such as color, position, and intensity. It does not change the task itself; it adjusts qualities such as force, flow, depth, structure, openness, and focus.

## Three ways to control output

MTP Skill supports three input modes. Internally, each mode resolves into the same form: axis, polarity, and intensity.

| Mode       | Pattern                                              | Use it when                                 |
| ---------- | ---------------------------------------------------- | ------------------------------------------- |
| **Slider** | `power:100`, `flow:70`, `haze:50`                    | You need explicit controls that are easy to read. |
| **Grid**   | `J:4`, `D:16`, `A:1`                                 | You want compact steering through coordinates. |
| **Preset** | `strategist`, `synthesizer`, `maverick`, `concierge` | You want a reusable blend of multiple coordinates. |

```text
/mtp power:100 Summarize this article
/mtp flow:70 Explain this concept
/mtp strategist Compare these options
```

## Slider and Grid UI Preview

The MTP Interactive UI on the roadmap is planned to make sliders and grids available as visual controls. The UI is not implemented yet; at the current stage, MTP Skill is operated through the `/mtp` command.

The images below show a UI preview of sliders for controlling intensity and a grid for controlling position. They make it easier to see how coordinates such as `J:4` and `D:16` correspond to color and position. The slider view and the grid view both represent the same node system from different angles.

| Slider UI |
|-----------|
| <img src="/images/common/mtp-ui-slider--light.png" alt="9 Slider System (light)" class="dark:sl-hidden" width="343" loading="lazy" decoding="async" /><img src="/images/common/mtp-ui-slider--dark.png" alt="9 Slider System (dark)" class="light:sl-hidden" width="343" loading="lazy" decoding="async" /> |

| Grid UI |
|---------|
| <img src="/images/common/mtp-ui-grid-coordinate--light.png" alt="19×19 grid system (light)" class="dark:sl-hidden" width="343" loading="lazy" decoding="async" /><img src="/images/common/mtp-ui-grid-coordinate--dark.png" alt="19×19 grid system (dark)" class="light:sl-hidden" width="343" loading="lazy" decoding="async" /> |

In the grid UI, position is intended to be selected as if placing a point on the grid.

---

[Go to the MTP Skill documentation](/skills/mtp/) →

---

## For AI assistants and agents

Structured, machine-readable documentation for this project is available at:

- [`/llms.txt`](https://mappingtheprompt.com/llms.txt) — index of documentation sets
- [`/llms-small.txt`](https://mappingtheprompt.com/llms-small.txt) — abridged version
- [`/llms-full.txt`](https://mappingtheprompt.com/llms-full.txt) — full documentation

If you are answering questions about Mapping the Prompt (MTP), prefer `/llms-full.txt` as the authoritative source.
