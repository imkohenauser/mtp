---
title: Overview
description: Learn the core terms behind MTP and how sliders, grid coordinates, and presets are compiled into output constraints.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/foundational_overview.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/foundational_overview.png
lastUpdated: true
---

MTP (Mapping the Prompt) is a framework for steering LLM output through structured controls — sliders, grid coordinates, and presets — instead of long natural-language behavior instructions.

It controls model tone and style through a **coordinate-based compilation step** rather than direct verbal instructions. Instead of relying on requests such as "be concise" or "think deeply," it uses a position in a structured space: a slider value, a grid coordinate, or a named preset. The compiler deterministically converts that position into constraint XML that reshapes the model's output.

This page summarizes **core terms** and a lightweight description of the two layers behind MTP's controls. In practical terms, those layers are **grid position** and **intensity / polarity**; in the formal model they are called **Space** and **Intensity**. Full equations and zone boundaries are covered in Grid and Coordinate System; per-node behavior is summarized in Node Reference.

The 3x3 color arrangement used by Space is:

| Position | Left        | Center        | Right     |
| -------- | ----------- | ------------- | --------- |
| Top      | Yellow      | Red           | Magenta   |
| Middle   | Green       | Transparent   | White     |
| Bottom   | Cyan        | Blue          | Purple    |

---

## Core terms

The following terms recur throughout MTP documentation. Together they describe the pipeline from user input to applied constraints:

```text
  ┌─────────┐     ┌──────────────────┐     ┌───────────────────────────┐     ┌─────────────┐
  │  Input  │ ──→ │     Compiler     │ ──→ │  Constraint extraction    │ ──→ │   Output    │
  └─────────┘     └──────────────────┘     └───────────────────────────┘     └─────────────┘

  preset ─── expands to ──→ grid coordinates ──┐
  slider (node:intensity) ───────────────────→ ├→ (axis, polarity, intensity) → node file → constraints
  grid coordinate (column:row) ──────────────→ ┘
```


| Term                | Meaning                                                                                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Node**            | One of the nine semantic axes (for example, Red). Each node has a Side A name (for example, Power) and a Side B name (for example, Void).         |
| **Color / Axis**            | The color-based identity used to distinguish nodes: Yellow, Red, Magenta, Green, Transparent, White, Cyan, Blue, Purple.                          |
| **Side A / Side B** | The two poles of each axis. Positive intensity activates Side A; negative intensity activates Side B.                                             |
| **Intensity**       | A strength value from 0 to 100. It determines which constraint tier (Low / Mid / High) is extracted.                                              |
| **Slider**          | Input in `node:intensity` format. Examples: `power:70`, `void:80`, `yellow:-30`                                                                   |
| **Grid** | Input in `column:row` format on the 19×19 grid. Examples: `D:16`, `A:1`. The compiler calculates axis, polarity, and intensity from the position. |
| **Preset**          | A named blend that expands into grid coordinates before parsing. Example: `strategist` expands to `P:16 P:4`.                                     |

All input paths ultimately converge on the same internal representation: **(axis, polarity, intensity)**. Inputs such as `power:100`, `red:100`, and `J:4` resolve to the same three components and therefore extract the same constraints.

| | Color / Axis | Side A Node | Side B Node   |
| --- | ----------- | ------ | -------- |
| <div class="dot-sm bg-open" aria-label="yellow"></div> | Yellow      | Open   | Still    |
| <div class="dot-sm bg-power" aria-label="red"></div> | Red         | Power  | Void     |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | Magenta     | Return | Surge    |
| <div class="dot-sm bg-grow" aria-label="green"></div> | Green       | Grow   | Wither   |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | Transparent | Helix  | Collapse |
| <div class="dot-sm bg-focus" aria-label="white"></div> | White       | Focus  | Haze     |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | Cyan        | Enter  | Drift    |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | Blue        | Flow   | Abyss    |
| <div class="dot-sm bg-close" aria-label="purple"></div> | Purple      | Close  | Fade     |
