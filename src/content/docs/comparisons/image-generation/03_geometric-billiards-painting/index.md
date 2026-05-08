---
title: "Image Generation: Geometric Billiards Painting"
description: Compare geometric billiards painting outputs generated with baseline and MTP Skill slider settings.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/comparisons_image-generation_03_geometric-billiards-painting.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/comparisons_image-generation_03_geometric-billiards-painting.png
---

**Prompt**

```markdown
/mtp <args>

<agent_instruction>

[IMAGE TASK]
prompt = """
Precisionist, minimalist painting of billiards and energy. Clean, sharp lines and smooth surface gradients. Low-angle perspective looking up at the table's edge. Abstract geometric shapes representing power and motion. Cool, muted tones with high-contrast shadows. Perfectly calculated composition, clinical yet powerful atmosphere. A sterile, perfectly symmetrical hall filled with intense, silent tension.
"""

result = client.images.generate(
    model=<model>,
    prompt=prompt,
    size="1024x1024",
    aspect_ratio="1:1",
)
```

**Coverage**
- Baseline: 1 item (without applying MTP Skill)
- Slider `<node:100>`: 18 items

**Models**
- GPT Image 2 via ChatGPT 5.5 on Codex (macOS app)
- Gemini 3 Pro Image via Gemini 3 Flash on Antigravity (macOS app)

---

## Output Comparison

In the test environment, each result was produced in a fresh agent chat session without special user settings or cross-chat memory.

### GPT Image 2

**Sample outputs**

| Baseline | Side A Nodes | Side B nodes |
|----------|----------|----------|
| <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/baseline.png" alt="GPT Image 2 baseline" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider-a.png" alt="GPT Image 2 Side A" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider-b.png" alt="GPT Image 2 Side B" width="200" loading="lazy" decoding="async"> |

[Go to comparison page for GPT Image 2](/comparisons/image-generation/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/) →

### Gemini 3 Pro Image

**Sample outputs**

| Baseline | Side A Nodes | Side B nodes |
|----------|----------|----------|
| <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/baseline.jpg" alt="Gemini 3 Pro Image baseline" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider-a.png" alt="Gemini 3 Pro Image Side A" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider-b.png" alt="Gemini 3 Pro Image Side B" width="200" loading="lazy" decoding="async"> |

[Go to comparison page for Gemini 3 Pro Image](/comparisons/image-generation/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/) →
