---
title: Node Reference
description: Reference the core semantics and prompt-output tendencies of the nine MTP axes and their Side A / Side B nodes.
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

**MTP** replaces much of that control with non-verbal metadata: **coordinates and axis labels** compiled into **tiered constraints**. This page separates the **core semantics** of each Side A / Side B node from the **prompt-output tendencies** produced by the current MTP Skill.

Core semantics describe the direction represented by a node across applications. Prompt-output tendencies describe how that direction is currently translated into LLM behavior.

---

## Node quick reference

Each color axis in MTP has two nodes: Side A and Side B (each referred to as `<node>`).
Intensity (`<intensity>`) can be specified in the range `0` to `100`.

Side A is the positive-side node and can be specified by node name, such as `power:70` (`<node>:<intensity>`). Side B is the inverse-side node and can be specified by node name, such as `void:70`.

When using a color name instead of a node name, positive values activate Side A and negative values activate Side B.
For example, `red:70` activates Power, while `red:-70` activates Void.
The same polarity rule applies to node names: `power:-70` also activates the Red axis through Void.

### Side A quick reference

| | Color / Axis | Node | Usage example | Core semantics | Prompt-output tendencies |
|---|---|---|---|---|---|
| <div class="dot-sm bg-open" aria-label="yellow"></div> | Yellow | `open` | `open:100` / `yellow:100` / `D:4` | Opening, possibility, expansion | Divergent ideation, option generation, leaving room for choice |
| <div class="dot-sm bg-power" aria-label="red"></div> | Red | `power` | `power:100` / `red:100` / `J:4` | Force, assertion, drive | Firm claims, decisions, persuasive conclusions |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | Magenta | `return` | `return:100` / `magenta:100` / `P:4` | Return, reversal, recurrence, reframing | Critique, counter-reading, reframing a premise |
| <div class="dot-sm bg-grow" aria-label="green"></div> | Green | `grow` | `grow:100` / `green:100` / `D:10` | Development, layering, widening | Expanded explanations, elaboration, branching ideas |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | Transparent | `helix` | `helix:100` / `transparent:100` | Integration, unfolding structure, interrelation | Traceable reasoning, linked steps, visible structure |
| <div class="dot-sm bg-focus" aria-label="white"></div> | White | `focus` | `focus:100` / `white:100` / `P:10` | Precision, clarity, definition | Specification checks, evidence, narrowed scope |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | Cyan | `enter` | `enter:100` / `cyan:100` / `D:16` | Threshold, entry, framing | Introductions, onboarding, explicit scope and prerequisites |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | Blue | `flow` | `flow:100` / `blue:100` / `J:16` | Continuity, connection, rhythm | Smooth prose, transitions, readable progression |
| <div class="dot-sm bg-close" aria-label="purple"></div> | Purple | `close` | `close:100` / `purple:100` / `P:16` | Closure, completion, sealing | Summaries, conclusions, next actions |

### Side B quick reference

| | Color / Axis | Node | Usage example | Core semantics | Prompt-output tendencies |
|---|---|---|---|---|---|
| <div class="dot-sm bg-still" aria-label="yellow"></div> | Dark Yellow | `still` | `still:100` / `yellow:-100` / `A:1` | Restraint, preservation, suspension | Formatting, proofreading, minimal change, suppressing new suggestions |
| <div class="dot-sm bg-void" aria-label="red"></div> | Dark Red | `void` | `void:100` / `red:-100` / `J:1` | Absence, subtraction, hollowing, silence | Shortening, removing noise, dry or minimal responses |
| <div class="dot-sm bg-surge" aria-label="magenta"></div> | Dark Magenta | `surge` | `surge:100` / `magenta:-100` / `S:1` | Release, excess, eruption, overflow | High-energy writing, dense accumulation, forceful expression |
| <div class="dot-sm bg-wither" aria-label="green"></div> | Dark Green | `wither` | `wither:100` / `green:-100` / `A:10` | Attenuation, pruning, decline | Key-point summaries, concise explanations, reduced branching |
| <div class="dot-sm bg-collapse" aria-label="transparent"></div> | Translucent (Transparent) | `collapse` | `collapse:100` / `transparent:-100` | Compression, convergence, loss of structure | Direct answers, simplified summaries, flattened organization |
| <div class="dot-sm bg-haze" aria-label="white"></div> | Dark Grey (White) | `haze` | `haze:100` / `white:-100` / `S:10` | Ambiguity, diffusion, obscured definition | Poetic language, atmosphere, softened distinctions |
| <div class="dot-sm bg-drift" aria-label="cyan"></div> | Dark Cyan | `drift` | `drift:100` / `cyan:-100` / `A:19` | Deviation, wandering, loosened direction | Free association, tangents, lateral development |
| <div class="dot-sm bg-abyss" aria-label="blue"></div> | Dark Blue | `abyss` | `abyss:100` / `blue:-100` / `J:19` | Depth, descent, weight | Deep reflection, criticism, dense analysis |
| <div class="dot-sm bg-fade" aria-label="purple"></div> | Dark Purple | `fade` | `fade:100` / `purple:-100` / `S:19` | Attenuation, dissolution, afterimage | Open-ended prose, tapering conclusions, lingering resonance |

*Side B color names are not the opposite color (White does not flip to Black); they restate the axis color to match each node's meaning. Haze is White growing hazy toward grey, shown as "Dark Grey (White)," and Collapse is Transparent breaking down, shown as "Translucent (Transparent)."*

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
