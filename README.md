# Mapping the Prompt

> 🌐 原文は「[日本語](./ja/README.md)」で記述されています。この英語版は翻訳です。  
> The original document is written in Japanese. This English version is a translation.

**Mapping the Prompt (MTP)** is a **lightweight, general-purpose framework** for visualizing conversational states with generative AI (LLM) as coordinates, enabling alignment of intent and prompt adjustment.  
It assumes a minimal implementation with SVG/CSS/JS, and treats dialogue as a “coordinate space,” replacing fine-grained textual instructions with **UI operations (points + averages)**.  
For details, see [Concept](./CONCEPT.md) and the [Official Website](https://imkohenauser.com/mtp).

![Screenshot of MTP](/assets/svg/screenshot.svg)

**Features**

- 🤝 **A shared framework between generative AI and users**

  - MTP is not a new NLP algorithm but a **lightweight coordinate framework** shareable by both users and generative AI.
  - Abstract or intuitive intent can be expressed not through text input but through **coordinate specification**.

- ☯️ **20-node classification (like A/B sides of a record or cassette)**

  - Side A: Start, Open, Power, Return, Grow, Helix, Focus, Enter, Flow, Close.
  - Side B: Still, Void, Surge, Wither, Collapse, Haze, Drift, Abyss, Fade, End.

- 🚀 **Model-agnostic and adaptive**

  - Usable without large-scale retraining—only lightweight mapping learning, prompt tuning, or fine-tuning.
  - Applicable to major LLMs (OpenAI / Anthropic / DeepMind / xAI, etc.).
  - Mapping can be adjusted to match each model’s **principles and safety policies**.

- 🫧 **Positioned as a lightweight UI layer**

  - Placed near the input form: a “coordinate UI” toggle next to the chat box.
  - As part of multimodal output: generative AI can render the coordinate UI, which the user then adjusts.

> [!WARNING]  
> This project is in its early (alpha) stage.  
> The goal is a shared UI usable across major generative AI models. Collaboration and feedback are welcome.

---

## Introduction

Generative AI users routinely seek diverse intentions such as:

- Specifying tone/context precisely in prompt design
- Inspiring creative stories, poetry, or free-form writing
- Producing clear, persuasive summaries or business documents
- Delivering bold, powerful proposals or copy
- Explaining complex information in smooth, accessible prose

But issuing exact textual instructions each time is cumbersome, and ambiguity or mismatched interpretation often arises.  
**MTP** provides a UI to specify abstract or intuitive intent as **coordinates**, enabling trial-and-error adjustment **visually in an instant** (e.g., divergence ⇄ convergence, force ⇄ flow).

---

## Concept (Overview)

### Classification Concept — 20-Node Structure

MTP is designed as a classification of 20 nodes, arranged like cassette tape sides: 10 on Side A and 10 on Side B.

- One unique feature is treating the UI handle, the “Gizmo,” as independent nodes (Start / End).
- **Side A** covers clarity and forward movement. **Side B** provides **depth, reverse aspects, and complementary nuances**.
- Side B is not “negative,” but an extension of nuance and expression.

![20-node structure](/assets/svg/readme-20-node-structure.svg)

> [!NOTE]  
> For detailed definitions of the 20 nodes, see the **“CONCEPT”** doc in this repo or the **official website**.
>
> - [Concept](./CONCEPT.md)
> - [Official Website](https://imkohenauser.com/mtp)

---

<details>
<summary>View the “20-node structure reference table”</summary>

#### 🌅 Side A: 10 Nodes (1 + 9 in 3×3)

| #   | Label      | Kanji | Color       | Role              | Keywords             |
| --- | ---------- | ----- | ----------- | ----------------- | -------------------- |
| 1   | **Start**  | 始    | chosen      | Gizmo             | Intro, spring, start |
| 2   | **Open**   | 開    | Yellow      | Top-left node     | Opening, release     |
| 3   | **Power**  | 力    | Red         | Top node          | Force, fire, uplift  |
| 4   | **Return** | 還    | Magenta     | Top-right node    | Return, cycle, yield |
| 5   | **Grow**   | 生    | Green       | Left node         | Growth, layering     |
| 6   | **Helix**  | 螺    | Transparent | Center node       | Spiral, neutral      |
| 7   | **Focus**  | 集    | White       | Right node        | Focus, blank slate   |
| 8   | **Enter**  | 入    | Cyan        | Bottom-left node  | Entry, arrival       |
| 9   | **Flow**   | 流    | Blue        | Bottom node       | Rhythm, water, link  |
| 10  | **Close**  | 閉    | Purple      | Bottom-right node | Margin, closure      |

#### 🌌 Side B: 10 Nodes (9 in 3×3 + 1)

| #   | Label        | Kanji | Color        | Role              | Keywords           |
| --- | ------------ | ----- | ------------ | ----------------- | ------------------ |
| 11  | **Still**    | 静    | Dark Yellow  | Top-left node     | Stillness, peace   |
| 12  | **Void**     | 虚    | Dark Red     | Top node          | Emptiness, void    |
| 13  | **Surge**    | 詰    | Dark Magenta | Top-right node    | Explosion, thunder |
| 14  | **Wither**   | 枯    | Dark Green   | Left node         | Fading, decay      |
| 15  | **Collapse** | 崩    | Translucent  | Center node       | Collapse, fall     |
| 16  | **Haze**     | 霞    | Gray         | Right node        | Blur, faintness    |
| 17  | **Drift**    | 漂    | Dark Cyan    | Bottom-left node  | Drift, float       |
| 18  | **Abyss**    | 深    | Dark Blue    | Bottom node       | Depth, abyss       |
| 19  | **Fade**     | 衰    | Dark Purple  | Bottom-right node | Fading, twilight   |
| 20  | **End**      | 終    | chosen       | Transformed Gizmo | End, prayer, stop  |

</details>

---

### UI Operation — Style by Coordinates

On the UI, behavior is adjusted by **coordinate specification**:

- **Vertex**: Anchor points representing features of a prompt.
- **Gizmo**: **Average coordinate** of multiple vertices; the session’s center of gravity and main UI handle.
- **Transformed Gizmo**: The user’s **target coordinate** to directly control output tone/behavior.

![UI operation by coordinates](/assets/svg/readme-ui-operation.svg)

### Grid and Abstraction

Internally, states are tracked on a strict grid (e.g., 19×19), while the UI can abstract into **color wheels or simplified palettes**.  
Grid configuration can adapt to devices or display areas.

![Grid and abstraction](/assets/svg/readme-grid-and-abstraction.svg)

### Session State Visualization

User–AI session states (history, phase) can be visualized as **coordinate transitions**.  
Session drift (deviation from intent) can be spotted at a glance, enabling return to or alignment with past “good states.”

![Session state visualization](/assets/svg/readme-visualization-of-session-state.svg)

---

## Use Cases

Enhancing creative tasks and long-form dialogues, while enabling finer control of tone and style, within model design/constraints.

### Tone Context (Instant Style Switching)

Controls **attitude, affect, and tone** axes in generated text.

- Example: empathetic listener, robotic, passionate, calm — adjustable as hues or vector directions.
- Users can combine tones, e.g., “polite but dry,” “friendly and passionate.”

#### Intuitive Style Switching

- _Open × Grow_: Idea generation, brainstorming, poetic openings
- _Power × Void_: Strong persuasion (marketing copy)
- _Return × Focus_: Summaries, executive digests, proposal outlines

![Instant style switching](/assets/svg/readme-persona-and-response-style.svg)

### Visualizing ChatGPT Personas

Simple persona styles (e.g., Cynic, Listener, Robot, Nerd) can be mapped, adjusted, and drift-controlled.

![Persona visualization](/assets/svg/readme-chatgpts-persona.svg)

### Reasoning Level (Depth and Granularity)

Controls **thinking cost and structure** in output:

- Center: quick answers, low-cost, key points only.
- Outer coordinates: multi-step reasoning, comparisons, counterarguments, explicit intentions.

<details>
<summary>Node examples and tendencies</summary>

| Node      | Reasoning Tendency    |
| --------- | --------------------- |
| **Power** | Active reasoning      |
| **Flow**  | Minimal, concise      |
| **Grow**  | Divergent exploration |
| **Focus** | Narrow, deep probing  |

</details>

### Multi-Step Reasoning (Process Visualization)

Multi-step reasoning (chain-of-thought) can be visualized and adjusted via **coordinates and color**:

- Internal steps of the LLM (prompt reasoning transitions) shown as color trails or phases.
- Keywords anchored as vertices (coordinates/colors).
- Users can revisit vertices (past steps) to **revise course**.

This makes LLM outputs transparent and debuggable via **UI-based, non-verbal instructions**.

### Branching Conversations (Branch into a New Chat)

By combining ChatGPT's new feature _Branching Conversations_ with MTP, it becomes possible to handle conversation branching more intuitively.

MTP maps the flow of each chat (tone and nuance) into 20 nodes and calculates an average color. Visualizing this as a label color on the chat list allows you to:

- Intuitively grasp the relationship between the main chat (trunk) and each branch by color
- Visually compare differences in conversational tone (logical/emotional, divergent/convergent, etc.)
- Organize each branch visually to understand "what direction of thought" it represents

This mechanism provides a level of understanding beyond a simple text list, especially for nonlinear exploration and brainstorming.

---

## Implementation Policy (Minimal Setup)

- **Rendering**: SVG base; CSS for color; JS for events (drag, click, hover).
- **State/Coordinates**: Vertex (classified points), Gizmo (session centroid), Transformed Gizmo (target).
- **External Integration**: Prompt/parameter conversion to AI APIs via loose adapters.
- **Fallback**: Functions as a **standalone UI** (color/graphics only) for demo/learning purposes.

---

## Conclusion — Between Intent and Plausibility

Getting “plausible” responses from AI has become easy with technical advances.  
But reflecting **personal nuance and affective subtlety** remains a challenge.

Long, detailed prompts can introduce ambiguity, losing subtle intent.  
**Mapping the Prompt (MTP)** offers a new approach to resolve this mismatch.

Instead of retraining AI, MTP **converts users’ intuitive mental maps into coordinates AI can interpret**, replacing trial-and-error with direct manipulation.  
Vague requests like “more passionate” or “a bit quieter” become vectors in coordinate space, enabling **a visually shared interface** that elevates dialogue quality.

MTP adds an “intent-sharing” layer to human–AI dialogue.  
It is not merely a UI but a **cultural and cognitive proposal**, aiming to become a **future standard interface** for generative AI.

---

## Contribution & Feedback

MTP thrives on **attention and feedback**. Join in:

- ⭐ Star on GitHub
- 🏴 Share/comment on [X (Twitter) @imkohenauser](https://x.com/imkohenauser)
- 💬 Participate in OpenAI Developer Forum topics
- 🛠 Propose via Issues/PRs (UI, terminology, translations, new use cases)

---

## License

Copyright © 2025 **Kohen**

This project is licensed under the [MIT License](./LICENSE).

---

[**Go to “Concept” →**](./CONCEPT.md)

↳ [Playlist (optional)](./PLAYLIST.md)  
↳ [Assets (optional)](./ASSETS.md)
