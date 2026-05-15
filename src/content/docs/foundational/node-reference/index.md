---
title: Node Reference
description: Reference the nine MTP nodes and their Side A / Side B behaviors through design intent and observed output tendencies.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/foundational_node-reference.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/foundational_node-reference.png
lastUpdated: true
---

## Introduction

In conventional prompt engineering, adjusting tone and behavior often relies on natural-language modifier phrasing (“act as an expert,” “think step by step”). Such phrasing tends to be ambiguous and often introduces **meta-instruction noise** alongside the task itself.

**MTP** replaces much of that control with non-verbal metadata — **coordinates and axis labels** — compiled into **tiered constraints**. This page explains **how each node is intended to be interpreted** within the framework.

> [!NOTE]
> MTP does **not** guarantee anything about model internals, nor identical behavior across every model and prompt.

---

## Axis structure

This section briefly organizes **how each axis relates** within the taxonomy.

- **Vertical (Red ↔ Blue):** The axis where directions that stress assertion and structure face directions that preserve receptivity and continuity.
- **Horizontal (Green ↔ White):** The axis where outward expansion while holding outline faces narrowing the subject for rigorous scrutiny.
- **Corners (Yellow, Magenta, Cyan, Purple):** Transitional **gradient** regions that connect **adjacent nodes** of the cross.
- **Center (Transparent):** A **neutral node** placed between opposing directions.

---

## Per-node characteristics

Each node corresponds to **constraint text** the compiler inserts. What follows describes **design intent** and **observation-based tendency** only; actual output still depends on the base model, task, and prompt.

The nine nodes are laid out as follows:

```text
+-----------------+-----------------+-----------------+
| Yellow          | Red             | Magenta         |
+-----------------+-----------------+-----------------+
| Green           | Transparent     | White           |
+-----------------+-----------------+-----------------+
| Cyan            | Blue            | Purple          |
+-----------------+-----------------+-----------------+
```

### Primary axes (cross skeleton)

#### <div class="dot-md bg-power" aria-label="red"></div> Red (Power)

- **Traits:** Assertion, conclusion-first ordering, structural clarity.
- **Tendency:** Tends toward a more direct, crisp voice; hedging may appear less often than under a neutral setting.

#### <div class="dot-md bg-flow" aria-label="blue"></div> Blue (Flow)

- **Traits:** Continuity, context maintenance, holding multiple viewpoints open.
- **Tendency:** Makes connections between ideas and topic shifts read more smoothly.

#### <div class="dot-md bg-grow" aria-label="green"></div> Green (Grow)

- **Traits:** Gradual unfolding, preserving outline, cautious expansion.
- **Tendency:** Stays within the stated task frame while, where it fits, favoring flowing prose over bullet lists.

#### <div class="dot-md bg-focus" aria-label="white"></div> White (Focus)

- **Traits:** Concentration, scrutiny, logical tightness.
- **Tendency:** Narrows scope for accuracy and tends to curb casual digression.

### Corner nodes

#### <div class="dot-md bg-open" aria-label="yellow"></div> Yellow (Open)

- **Traits:** Exploration, relaxed stance, breadth of view.
- **Tendency:** Tends to surface more options or wider, brainstorming-style ideation.

#### <div class="dot-md bg-close" aria-label="purple"></div> Purple (Close)

- **Traits:** Convergence, closure, summary.
- **Tendency:** Tends to pull content toward a single conclusion or a closing stance.

#### <div class="dot-md bg-return" aria-label="magenta"></div> Magenta (Return)

- **Traits:** Contrast, inversion, unsettling the default line.
- **Tendency:** Where appropriate, easier to add rebuttals, shifts of view, or “on the other hand”-style counterpoint.

#### <div class="dot-md bg-enter" aria-label="cyan"></div> Cyan (Enter)

- **Traits:** Depth-first bent, specialist stance.
- **Tendency:** Tends toward domain-specific detail and a perspective that moves inside the subject.

### Center node

#### <div class="dot-md bg-helix" aria-label="transparent"></div> Transparent (Helix)

- **Traits:** A neutral go-between bridging extremes.
- **Tendency:** When paired with strong nodes on the opposite side, works to soften wording and dampen extremity.

---

## Side B nodes

Under the **Chebyshev-based radial rule**, coordinates on the **outer perimeter frame** flip to **Side B** for that zone. In constraint design, Side B is expressed as an **inverted pole** of the same axis — a **paired opposite** in a yin–yang sense (for example, Power → Void, Focus → Haze, Grow → Wither).

Examples:

- **Void (inversion of Power):** Tends toward compressing the surface text toward a minimum.
- **Haze (inversion of Focus):** When the inverted pole is strong, tends toward a deliberately diffuse, hard-to-focus tone.
- **Wither (inversion of Grow):** Tends toward a quite conservative, reserved voice.

Side B suits cases that call for a **stronger extreme** along that axis or **more compressed** surface wording, with the same model-to-model variability as Side A.

---

## Combining nodes and presets

When several MTP tokens are present, **each token** is still resolved under the same **Space / Intensity** rules; the compiler emits one constraint block **per token in parse order** (the order they appear in the payload).

That order is **not** a third parameter space or a dedicated “motion” layer. The sequence *may* be read as a **semantic trajectory** on the grid, but that is an **optional design reading** only.

**Named sliders** (`power:100`, `flow:70`) are an easy starting point when meaning should stay readable; **grid coordinates** suit cases where the visible message should remain short.

**Named presets** expand to fixed coordinate sequences defined in `skills/mtp/references/presets.yaml`; they can be applied to reproducible multi-step blends.

