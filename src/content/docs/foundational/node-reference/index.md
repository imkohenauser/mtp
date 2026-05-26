---
title: Node Reference
description: Reference the nine MTP axes and their Side A / Side B node behaviors through design intent and observed output tendencies.
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

**MTP** replaces much of that control with non-verbal metadata: **coordinates and axis labels** compiled into **tiered constraints**. This page explains **how each Side A / Side B node label is intended to be interpreted** within the framework.

---

## Node quick reference

MTP has nine color axes. Each axis has two usable node labels: Side A and Side B.
Side A is the positive-side node and can be called directly with a node slider, such as `power:70`.
Side B is the inverse-side node and can also be called directly, such as `void:70`.

When using a color name instead of a node name, positive values activate Side A and negative values activate Side B.
For example, `red:70` activates Power, while `red:-70` activates Void.
The same polarity rule applies to node names: `power:-70` also activates the Red axis through Void.

### Side A quick reference

| | Color / Axis | Node | Example | Main behavior | Good for |
|---|---|---|---|---|---|
| <div class="dot-sm bg-open" aria-label="yellow"></div> | Yellow | Open | `open:70` / `yellow:70` | Possibility, divergence, margin | Brainstorming, option generation, early planning, expanding a question |
| <div class="dot-sm bg-power" aria-label="red"></div> | Red | Power | `power:70` / `red:70` | Assertion, judgment, drive | Proposals, decisions, presentations, answers that need a firm conclusion |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | Magenta | Return | `return:70` / `magenta:70` | Reversal, critique, reframing | Critique, reframing, contrarian review, perspective shifts |
| <div class="dot-sm bg-grow" aria-label="green"></div> | Green | Grow | `grow:70` / `green:70` | Expansion, layering, development | Explanations, learning, planning, developing an idea |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | Transparent | Helix | `helix:70` / `transparent:70` | Structure, traceability, path | Complex explanations, review notes, design decisions, traceable reasoning summaries |
| <div class="dot-sm bg-focus" aria-label="white"></div> | White | Focus | `focus:70` / `white:70` | Precision, definition, evidence | Research, specification checks, reviews, accuracy-sensitive answers |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | Cyan | Enter | `enter:70` / `cyan:70` | Entry, framing, scope | Tutorials, onboarding, procedures, beginner-friendly explanations |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | Blue | Flow | `flow:70` / `blue:70` | Continuity, rhythm, readability | Essays, articles, natural explanations, prose where readability matters |
| <div class="dot-sm bg-close" aria-label="purple"></div> | Purple | Close | `close:70` / `purple:70` | Closure, summary, next action | Summaries, proposals, closing sections, answers that need a CTA |

### Side B quick reference

| | Color / Axis | Node | Example | Main behavior | Good for |
|---|---|---|---|---|---|
| <div class="dot-sm bg-still" aria-label="yellow"></div> | Dark Yellow | Still | `still:70` / `yellow:-70` | Restraint, preservation, stillness | Formatting, proofreading, conversion, tasks where extra suggestions are unwanted |
| <div class="dot-sm bg-void" aria-label="red"></div> | Dark Red | Void | `void:70` / `red:-70` | Reduction, silence, minimum | Shortening, removing noise, dry answers, minimal responses |
| <div class="dot-sm bg-surge" aria-label="magenta"></div> | Dark Magenta | Surge | `surge:70` / `magenta:-70` | Momentum, density, force | High-energy writing, forceful drafts, intense expression, dense output |
| <div class="dot-sm bg-wither" aria-label="green"></div> | Dark Green | Wither | `wither:70` / `green:-70` | Pruning, core, reserve | Key-point summaries, concise explanations, short conclusions, minimal prose |
| <div class="dot-sm bg-collapse" aria-label="transparent"></div> | Transparent | Collapse | `collapse:70` / `transparent:-70` | Compression, simplification, endpoint | Compressing long text, direct answers, simplified summaries |
| <div class="dot-sm bg-haze" aria-label="white"></div> | Dark Grey (White) | Haze | `haze:70` / `white:-70` | Ambiguity, softness, atmosphere | Poetic language, atmosphere, abstract writing, impression-driven expression |
| <div class="dot-sm bg-drift" aria-label="cyan"></div> | Dark Cyan | Drift | `drift:70` / `cyan:-70` | Deviation, association, tangent | Essays, creative writing, free association, lateral idea development |
| <div class="dot-sm bg-abyss" aria-label="blue"></div> | Dark Blue | Abyss | `abyss:70` / `blue:-70` | Depth, weight, reflection | Deep analysis, criticism, theoretical writing, non-surface-level reflection |
| <div class="dot-sm bg-fade" aria-label="purple"></div> | Dark Purple | Fade | `fade:70` / `purple:-70` | Resonance, taper, afterimage | Literary endings, open-ended prose, afterimage, mood-focused writing |

---

## Axis structure

This section briefly organizes **how each axis relates** within the taxonomy.

- **Vertical (Red ↔ Blue):** The axis where directions that stress assertion and structure face directions that preserve receptivity and continuity.
- **Horizontal (Green ↔ White):** The axis where outward expansion while holding outline faces narrowing the subject for rigorous scrutiny.
- **Corners (Yellow, Magenta, Cyan, Purple):** Transitional **gradient** regions that connect **adjacent nodes** of the cross.
- **Center (Transparent):** A **neutral node** placed between opposing directions.

![MTP coordinate system and node layout diagram showing the unified Side A/B color and node map, plus coordinate pairs such as D:4 and A:19.](/images/pages/mtp-coordinate-system-and-node-layout.png)

*The axis layout can be read both as a 3x3 Side A / Side B map and as coordinate positions on the 19x19 grid.*

---

## Side A / Side B

As an output tendency, Side A often appears as a force that moves the response forward. In an introduction, for example, it may invite the reader in, add reasons, structure the material, sharpen focus, or carry the text toward a conclusion.

Side B is not simply a weaker Side A. As the inverted pole of the same axis, it often shifts output away from construction toward reduction, away from clarity toward ambiguity, away from expansion toward descent, and away from closure toward afterimage. Side B is not the "bad" or "low" side; it functions as the shadow or reverse face of the axis.

---

## Side B interpretation

Under the **Chebyshev-based radial rule**, coordinates on the **outer perimeter frame** flip to **Side B** for that zone. In constraint design, Side B is expressed as an **inverted pole** of the same axis: a **paired opposite** in a yin-yang sense (for example, Power → Void, Focus → Haze, Grow → Wither).

Side B suits cases that call for a **stronger extreme** along that axis or **more compressed** surface wording, with the same model-to-model variability as Side A.

---

## Combining nodes and presets

MTP can also specify multiple nodes at the same time to blend output tendencies. Instead of switching output with a single node, it can layer several axes like a gradient, such as combining assertion (`power:20`) with precision (`focus:30`), or development (`grow:20`) with readability (`flow:50`).

The idea is to reduce the burden of operation by combining MTP nodes intuitively, while still changing the model's output tendency in a controlled way.

When several MTP tokens are present, **each token** is still resolved under the same **Space / Intensity** rules; the compiler emits one constraint block **per token in parse order** (the order they appear in the payload).

That order is **not** a third parameter space or a dedicated “motion” layer. The sequence *may* be read as a **semantic trajectory** on the grid, but that is an **optional design reading** only.

**Named sliders** (`power:100`, `flow:70`) are an easy starting point when meaning should stay readable; **grid coordinates** suit cases where the visible message should remain short.

**Named presets** expand to fixed coordinate sequences defined in `skills/mtp/references/presets.yaml`; they can be applied to reproducible multi-step blends.
