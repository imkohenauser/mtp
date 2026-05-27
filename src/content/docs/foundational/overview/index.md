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
---

MTP (Mapping the Prompt) is a framework for steering LLM output through structured controls — sliders, grid coordinates, and presets — instead of long natural-language behavior instructions.

It controls model tone and style through a **coordinate-based compilation step** rather than direct verbal instructions. Instead of relying on requests such as "be concise" or "think deeply," it uses a position in a structured space: a slider value, a grid coordinate, or a named preset. The compiler deterministically converts that position into constraint XML that reshapes the model's output.

This page summarizes **core terms** and a lightweight description of the two layers behind MTP's controls. In practical terms, those layers are **grid position** and **intensity / polarity**; in the formal model they are called **Space** and **Intensity**. Full equations and zone boundaries are covered in Grid and Coordinate System; per-node behavior is summarized in Node Reference.

The 3x3 color arrangement used by Space is:

```text
+-----------------+-----------------+-----------------+
| Yellow          | Red             | Magenta         |
+-----------------+-----------------+-----------------+
| Green           | Transparent     | White           |
+-----------------+-----------------+-----------------+
| Cyan            | Blue            | Purple          |
+-----------------+-----------------+-----------------+
```

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
| **Axis**            | The color-based identity used to distinguish nodes: Yellow, Red, Magenta, Green, Transparent, White, Cyan, Blue, Purple.                          |
| **Side A / Side B** | The two poles of each axis. Positive intensity activates Side A; negative intensity activates Side B.                                             |
| **Intensity**       | A strength value from 0 to 100. It determines which constraint tier (Low / Mid / High) is extracted.                                              |
| **Slider**          | Input in `node:intensity` format. Examples: `power:70`, `void:80`, `yellow:-30`                                                                   |
| **Grid** | Input in `column:row` format on the 19×19 grid. Examples: `D:16`, `A:1`. The compiler calculates axis, polarity, and intensity from the position. |
| **Zone**            | One of the nine large cells created by dividing the grid into 3×3. Each zone maps to one axis.                                                    |
| **Preset**          | A named blend that expands into grid coordinates before parsing. Example: `strategist` expands to `P:16 P:4`.                                     |
| **Constraint**      | Instructions extracted from a node file according to the resolved intensity tier. These instructions shape output behavior.                       |


All input paths ultimately converge on the same internal representation: **(axis, polarity, intensity)**. Inputs such as `power:100`, `red:100`, and `J:4` resolve to the same three components and therefore extract the same constraints.

---

## Two layers

At a formal level, MTP consists of two layers: **Space** and **Intensity**. This overview introduces them in concrete terms as **grid position** and **intensity / polarity**. **Space** is where something sits on the grid: axis and zone. **Intensity** is how strong it is and which pole is active; resolving grid coordinates involves **Volcano** mapping and tier extraction. The design background behind the 3×3 layout is covered in Design Background.

### Layers at a glance


| Layer         | Controls                                         | Key idea                                                                            |
| ------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------- |
| **Space**     | *Grid position*: which axis and zone             | 19×19 grid, 3×3 macro zones, hue cycle                                              |
| **Intensity** | *Intensity / polarity*: strength and active pole | 0–100 slider, Side A / Side B, strength and polarity mapped from distance to center |


For each token, the compiler resolves **(axis, polarity, intensity)** and extracts tiered constraints from node files.

### Space (grid position)

The interface uses an integer coordinate system based on **19×19 line intersections**, which is the current default implementation. The surface is divided into **nine macro zones** in a symmetric 3×3 layout, and each zone maps to one color axis. The design rationale behind that arrangement is covered in Design Background.

### Intensity (strength / polarity)

Each node has a continuous strength value from **0 to 100**. **Polarity** determines whether Side A (positive) or Side B (negative / inverted pole) is active. Macro-zone color names can also be used as slider aliases (for example, `yellow:50` ≡ `open:50` on the Yellow axis). Strength and polarity from a grid position are computed with a **Chebyshev-based radial rule**, defined in Grid and Coordinate System. Qualitatively: neutral at the center, Side A peaks on the surrounding ring, Side B on the outer frame.

When several MTP tokens are present, the compiler emits one `<constraints>` block **per token in parse order** (not a separate layer). Optional design readings of token order (for example trajectory metaphors) are in Design Background; per-node summaries are in Node Reference.
