---
title: Grid and Coordinate System
description: Define MTP's 19x19 grid, 3x3 macro zones, and coordinate model for resolving intensity and polarity.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/foundational_grid-and-coordinate-system.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/foundational_grid-and-coordinate-system.png
lastUpdated: true
---

MTP (Mapping the Prompt) is a framework for shaping prompt behavior **without** relying on explicit instructive prose, using a **dynamic model with two formal layers: Space and Intensity**. **Space** determines axis and zone from grid position; **Intensity** determines strength, polarity, and tiered constraint extraction (Volcano mapping for coordinates).

**Multiple tokens** in one `/mtp` payload (including preset expansion) add **ordered** constraint blocks: each token is still mapped through the same Space and Intensity rules; order is **not** a third parameter space or dedicated transform layer.


| Layer         | Controls                           | Key concept                                    |
| ------------- | ---------------------------------- | ---------------------------------------------- |
| **Space**     | *Where* — which axis/zone          | 19×19 grid, 3×3 macro zones, hue cycle         |
| **Intensity** | *How much* — strength and polarity | 0–100 slider, Side A / Side B duality, Volcano |


This document defines the mathematical and geometric structures that make up MTP, along with the internal parameter model used to inject metadata into prompts.

---

## Spatial structure: 19×19 grid system

The core MTP interface uses an integer coordinate system at line intersections, similar to a Go board. The grid is **19×19**.

### Symmetrical three-way division model

The space is always divided into a **geometrically balanced 3×3 macro-zone structure**. Rather than simply splitting the number of elements into three uneven groups, MTP treats the whole surface as continuous space and places grid lines and boundaries in a fully symmetrical arrangement.

**Structure from 19 grid lines**

There are 19 grid lines in total. Four of them are boundaries (outer frame and between zones); inside them lie three equal-width macro zones in sequence, each containing five grid lines.

```text
        A – F        G – L        M – S
 1–6   Yellow    |    Red      | Magenta
 7–12  Green     | Transparent | White
13–19  Cyan      |    Blue     | Purple
```

- **Line 1:** Boundary line (outer frame)
- **Lines 2–6:** Zone 1 (5 grid lines)
- **Line 7:** Boundary line (inner boundary)
- **Lines 8–12:** Zone 2 (5 grid lines)
- **Line 13:** Boundary line (inner boundary)
- **Lines 14–18:** Zone 3 (5 grid lines)
- **Line 19:** Boundary line (outer frame)

### Boundary lines and zone assignment

Boundary lines are not sharp partitions; conceptually—like a gradient—they are transition regions between macro zones. The compiler assigns each coordinate (including boundary coordinates) to **exactly one** of the nine macro-zone cells (zone bounds are defined by the compiler) and computes intensity with the same Chebyshev distance formula as for interior coordinates.

### Hue cycle and Z-order

The nine macro zones correspond to a hue cycle and also carry a generation transition order, or Z-order. Together they suggest the order in which concepts unfold and which phases processing passes through.

|                                                              | Color           | Node        | Keywords                                      |
| ------------------------------------------------------------ | --------------- | ----------- | --------------------------------------------- |
| <div class="dot-sm bg-open" aria-label="yellow"></div>       | **Yellow**      | `open`      | divergence, openness, margin                  |
| <div class="dot-sm bg-power" aria-label="red"></div>         | **Red**         | `power`     | force, assertion, rise                        |
| <div class="dot-sm bg-return" aria-label="magenta"></div>    | **Magenta**     | `return`    | return, flip, cycle                           |
| <div class="dot-sm bg-grow" aria-label="green"></div>        | **Green**       | `grow`      | growth, proliferation, layering               |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | **Transparent** | `helix`     | helix, unfold, neutral structure              |
| <div class="dot-sm bg-focus" aria-label="white"></div>       | **White**       | `focus`     | focus, convergence, precision                 |
| <div class="dot-sm bg-enter" aria-label="cyan"></div>        | **Cyan**        | `enter`     | entry, landing, structure                     |
| <div class="dot-sm bg-flow" aria-label="blue"></div>         | **Blue**        | `flow`      | flow, connection, rhythm                      |
| <div class="dot-sm bg-close" aria-label="purple"></div>      | **Purple**      | `close`     | close, completion, wrap                       |

---

## Intensity structure: three-state model and bipolarity

Each node is not a simple on/off switch, but a continuous intensity slider from 0 to 100. Polarity—positive or negative—determines whether Side A’s behavior is active or Side B’s **inverted** behavior is active.

The compiler also accepts **macro-zone color names** as slider aliases (for example, `yellow:50` ≡ `open:50`, `yellow:-50` ≡ `still:50`), using the same linear intensity mapping as the paired Side A / Side B nodes.

### Node symmetry (D4 symmetry) and pairing

Negative values activate Side B, while positive values activate Side A. Across the central baseline of `0`, they form the following dual pairs.


| Side B (-1)  | Center (0)  | Side A (+1) | Spatial Position |
| ------------ | ----------- | ----------- | ---------------- |
| `still`      | Yellow      | `open`      | Upper left       |
| `void`       | Red         | `power`     | Top              |
| `surge`      | Magenta     | `return`    | Upper right      |
| `wither`     | Green       | `grow`      | Left             |
| `collapse`   | Transparent | `helix`     | Center           |
| `haze`       | White       | `focus`     | Right            |
| `drift`      | Cyan        | `enter`     | Lower left       |
| `abyss`      | Blue        | `flow`      | Bottom           |
| `fade`       | Purple      | `close`     | Lower right      |


---

## Coordinate-to-intensity transformation model

Coordinates such as `A:1` or `J:10` on the 19×19 grid (hyphen form `A-1` is also accepted) are mapped by the MTP compiler to **polarity** (Side A / Side B) and **intensity** (0–100) using Chebyshev distance from the grid center `J:10`.

### Polarity and intensity calculation algorithm (Volcano model, Chebyshev distance)

This transformation follows a **Volcano model**: the center is neutral, the mid-ring reaches Side A peak, and the outer frame inverts into Side B. The model uses Chebyshev distance so all macro-zone centers at the same distance share the same signed value.

**Volcano model cross-section (example: row 10, from A to S):**

```text
Signed value
        Side A
 +100 |          /\                 /\
      |         /  \               /  \
      |        /    \             /    \
    0 |-------/------\-----0-----/------\-------
      |      /     Neutral Center        \
      |     /                             \
 -100 |----/                               \----
        Side B

Distance:  9      6        0        6      9
Coord:    A:10   D:10     J:10     P:10   S:10
```

Note: this is a one-dimensional cross-section (row 10). In full, the field is a 2D Chebyshev-distance ring around `J:10`—visually, a donut-shaped ring around the center.

- **Center (distance 0):** `J:10` -> signed value `0` (neutral, no constraint emitted)
- **Peak ring (distance 6):** for example, `D:10`, `D:4`, `P:16` -> Side A maximum (`+100`)
- **Outer frame (distance 9):** for example, `A:10`, `A:1`, `S:19` -> Side B maximum (`-100`)

Compiler formulas:

```text
Center (J:10)      = neutral (signed 0; no constraint)
Peak (distance 6)  = Side A maximum (signed +100)
Outer (distance 9) = Side B maximum (signed -100)

distance  = max(|x - 10|, |y - 10|)   (Chebyshev, integer 0–9)
Inner (distance ≤ 6):  signed = (distance / 6) * 100
Outer (distance > 6):  signed = 100 - 200 * (distance - 6) / 3

polarity  = +1 if signed >= 0 else -1
intensity = abs(signed), clamped to 1-100; 0 -> no constraint emitted
```

From center distance and macro-zone direction (axis), this mapping uniquely determines polarity and intensity; those values are injected into prompt metadata.

> The grid model is visualized with `scripts/mtp_grid_generator.py`. Regeneration steps and SVG details are covered in Color Grid Visualization.

