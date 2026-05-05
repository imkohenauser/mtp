---
title: Mapping and Sequence
description: Explore MTP as a conceptual mapping grid and as an ordered sequence of Side A and Side B node poles.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/optional_mapping-and-sequence.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/optional_mapping-and-sequence.png
---

> [!NOTE]
> This document is supplementary material. It is intended to support understanding of the design background.

MTP can be read not only as a tool for prompt steering, but also as a framework for **mapping concepts onto a 3×3 grid** and as an **ordered sequence** of node poles. That follows from how MTP node placement was designed using widely shared cues from color and direction.

This document covers two extended readings:

1. **Mapping on the grid** — placing characters, archetypes, prompt tendencies, output tendencies, and similar notions onto MTP nodes.
2. **Sequence (Z-order)** — taking input and output as a frame and reading the 18 node poles between them as a linear arc.

---

## Concept mapping on the grid

The MTP grid can be used as a surface for mapping other conceptual systems.
For example, the following kinds of alignment are possible.

### Reference: base grid

```text
3×3 color map (macro zones):
+-------------+-------------+-------------+
| Yellow      | Red         | Magenta     |
+-------------+-------------+-------------+
| Green       | Transparent | White       |
+-------------+-------------+-------------+
| Cyan        | Blue        | Purple      |
+-------------+-------------+-------------+

Node map (Side A):
+-------------+-------------+-------------+
| Open        | Power       | Return      |
+-------------+-------------+-------------+
| Grow        | Helix       | Focus       |
+-------------+-------------+-------------+
| Enter       | Flow        | Close       |
+-------------+-------------+-------------+

Node map (Side B):
+-------------+-------------+-------------+
| Still       | Void        | Surge       |
+-------------+-------------+-------------+
| Wither      | Collapse    | Haze        |
+-------------+-------------+-------------+
| Drift       | Abyss       | Fade        |
+-------------+-------------+-------------+
```

### Example: character mapping

A character system can be placed on the grid in an intuitive way.
As one example, Pixar’s [*Inside Out*](https://en.wikipedia.org/wiki/Inside_Out_(2015_film)) is built around emotional functions, so it can be read against the MTP grid.

**Side A** (*Inside Out*):

```text
+-------------+-------------+-------------+
| Joy         | Anger       | Joy         |
+-------------+-------------+-------------+
| Disgust     | Riley       | Fear        |
+-------------+-------------+-------------+
| Joy         | Sadness     | Joy         |
+-------------+-------------+-------------+
```

Example alignment:

| Position      | Node  | Character | Character reading |
| ------------- | ----- | --------- | ----------------- |
| Top-left      | Open  | Joy       | Optimism and openness widen the doorway to new experience. |
| Top-center    | Power | Anger     | Anger and assertion drive impulsive but forceful action. |
| Middle-left   | Grow  | Disgust   | Disgust and sorting tune pleasant–unpleasant boundaries and self-defense. |
| Center        | Helix | Riley     | Many emotions pass through; the person’s neutral hub. |
| Middle-right  | Focus | Fear      | Anxiety and vigilance turn attention toward danger and uncertainty. |
| Bottom-center | Flow  | Sadness   | Sadness and acceptance deepen emotional flow and meaning. |


**Side B** (*Inside Out 2*):

```text
+------------------+------------------------+------------------+
| Bloofy           | Lance Slashblade       | Anxiety          |
+------------------+------------------------+------------------+
| Embarrassment    | Riley                  | Ennui            |
+------------------+------------------------+------------------+
| Envy             | Deep Dark Secret       | Nostalgia        |
+------------------+------------------------+------------------+
```

Example alignment:

| Position      | Node     | Character          | Character reading |
| ------------- | -------- | ------------------ | ----------------- |
| Top-left      | Still    | Bloofy             | A childhood imaginary comfort character stills real motion into consolation. |
| Top-center    | Void     | Lance Slashblade   | Heroic fantasy hardens into empty, unusable force. |
| Top-right     | Surge    | Anxiety            | Anxiety peaks, heightening thought and bodily response excessively. |
| Middle-left   | Wither   | Embarrassment      | Shame weakens boundary defense, shrinking the self under self-consciousness. |
| Center        | Collapse | Riley              | The neutral hub overloads and collapses; emotional integration briefly fails. |
| Middle-right  | Haze     | Ennui              | Indifference and irony diffuse vigilance and cloud attention. |
| Bottom-left   | Drift    | Envy               | Craving loses direction, repeating insatiable want for what others have. |
| Bottom-center | Abyss    | Deep Dark Secret   | Buried secrets sink, pulling self-understanding toward the bottom. |
| Bottom-right  | Fade     | Nostalgia          | After closure, faint regret lingers, turning toward longing for the past. |

Each cell can also be read as the **inverted pole** of the Side A node at the same coordinates (for example, Open’s optimism becomes Still’s arrest; Power’s thrust becomes Void’s hollowing-out).

---

## Ordered sequence reading

MTP is formally defined by grid position, polarity, and intensity, but the nodes can also be read as a sequence.
Tracing the 3×3 grid from top-left to bottom-right in a row-wise zigzag (Z-order) yields this color order:

```text
Yellow → Red → Magenta → Green → Transparent → White → Cyan → Blue → Purple
```

### 20-node sequence: 1+9+9+1

Replacing colors with nodes, add **Start (Input)** and **End (Output)** to the **nine Side A nodes** and **nine Side B nodes** to form a linear arc:

```text
 1. Start (Input)          ← beginning (input)
 2. Open                   ┐
 3. Power                  │
 4. Return                 │
 5. Grow                   │
 6. Helix                  │  Side A: positive pole
 7. Focus                  │
 8. Enter                  │
 9. Flow                   │
10. Close                  ┘
11. Still                  ┐
12. Void                   │
13. Surge                  │
14. Wither                 │
15. Collapse               │  Side B: negative pole
16. Haze                   │
17. Drift                  │
18. Abyss                  │
19. Fade                   ┘
20. End (Output)           ← end (output)
```

In this reading, the order follows the grid Z-order explained in Design Background.
**Start** and **End** are not nodes on the grid; they are virtual frame nodes added for sequence reading, marking the start and end of the arc.
The eighteen Side A and Side B nodes form their respective semantic frames.
As plain text, that is a **1+9+9+1** structure:

- **1**: Start (Input)
- **9**: Side A nodes
- **9**: Side B nodes
- **1**: End (Output)

Overall, the sequence forms a two-part arc:

- **Side A**: expansion, energy, unfoldment, arrival
- **Side B**: inversion, depletion, dismantling, attenuation

---

## Generality of classification and order

These readings help when:

- building an intuitive picture of **MTP Skill** from character placement
- mapping a 20-track AI-chosen music playlist onto the 20-node sequence

