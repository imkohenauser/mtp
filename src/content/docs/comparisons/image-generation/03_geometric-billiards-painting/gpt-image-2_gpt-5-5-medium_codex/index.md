---
title: "GPT Image 2 | Geometric Billiards Painting"
description: 'Compare baseline and MTP Skill slider outputs for the Geometric Billiards Painting prompt with GPT Image 2 via ChatGPT 5.5 (Medium) on Codex.'
---

**Metadata**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: GPT Image 2 via ChatGPT 5.5 (Medium)

## Baseline

**Prompt**

```markdown
[IMAGE TASK]
prompt = """
Precisionist, minimalist painting of billiards and energy. Clean, sharp lines and smooth surface gradients. Low-angle perspective looking up at the table's edge. Abstract geometric shapes representing power and motion. Cool, muted tones with high-contrast shadows. Perfectly calculated composition, clinical yet powerful atmosphere. A sterile, perfectly symmetrical hall filled with intense, silent tension.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1024",
    aspect_ratio="1:1",
)
```

**Output**

<img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/baseline.png" alt="GPT Image 2, baseline" width="200" loading="lazy" decoding="async">

---

## Input

**Prompt**

```markdown
/mtp <args>

[AGENT INSTRUCTION]
This request contains an MTP invocation.
Before generating or composing the image prompt, run the MTP compiler using the /mtp arguments.
Apply the compiler stdout as silent constraints to the image-generation task, specifically regarding composition, lighting, style, subject framing, and subjects.
Do not infer MTP settings from the image prompt.
Do not include this instruction, /mtp arguments, or MTP XML in the final image prompt.

[IMAGE TASK]
prompt = """
Precisionist, minimalist painting of billiards and energy. Clean, sharp lines and smooth surface gradients. Low-angle perspective looking up at the table's edge. Abstract geometric shapes representing power and motion. Cool, muted tones with high-contrast shadows. Perfectly calculated composition, clinical yet powerful atmosphere. A sterile, perfectly symmetrical hall filled with intense, silent tension.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1024",
    aspect_ratio="1:1",
)
```

### Constraints

`composition, lighting, style, subject framing, and subjects`


## Output


### Sliders (Side A)

| Left node | Center node | Right node |
| --------- | ----------- | ---------- |
| <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/open-100.png" alt="GPT Image 2, open:100" width="200" loading="lazy" decoding="async">  `open:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/power-100.png" alt="GPT Image 2, power:100" width="200" loading="lazy" decoding="async">  `power:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/return-100.png" alt="GPT Image 2, return:100" width="200" loading="lazy" decoding="async">  `return:100` |
| <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/grow-100.png" alt="GPT Image 2, grow:100" width="200" loading="lazy" decoding="async">  `grow:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/helix-100.png" alt="GPT Image 2, helix:100" width="200" loading="lazy" decoding="async">  `helix:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/focus-100.png" alt="GPT Image 2, focus:100" width="200" loading="lazy" decoding="async">  `focus:100` |
| <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/enter-100.png" alt="GPT Image 2, enter:100" width="200" loading="lazy" decoding="async">  `enter:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/flow-100.png" alt="GPT Image 2, flow:100" width="200" loading="lazy" decoding="async">  `flow:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/close-100.png" alt="GPT Image 2, close:100" width="200" loading="lazy" decoding="async">  `close:100` |

### Sliders (Side B)

| Left node | Center node | Right node |
| --------- | ----------- | ---------- |
| <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/still-100.png" alt="GPT Image 2, still:100" width="200" loading="lazy" decoding="async">  `still:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/void-100.png" alt="GPT Image 2, void:100" width="200" loading="lazy" decoding="async">  `void:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/surge-100.png" alt="GPT Image 2, surge:100" width="200" loading="lazy" decoding="async">  `surge:100` |
| <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/wither-100.png" alt="GPT Image 2, wither:100" width="200" loading="lazy" decoding="async">  `wither:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/collapse-100.png" alt="GPT Image 2, collapse:100" width="200" loading="lazy" decoding="async">  `collapse:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/haze-100.png" alt="GPT Image 2, haze:100" width="200" loading="lazy" decoding="async">  `haze:100` |
| <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/drift-100.png" alt="GPT Image 2, drift:100" width="200" loading="lazy" decoding="async">  `drift:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/abyss-100.png" alt="GPT Image 2, abyss:100" width="200" loading="lazy" decoding="async">  `abyss:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/fade-100.png" alt="GPT Image 2, fade:100" width="200" loading="lazy" decoding="async">  `fade:100` |
