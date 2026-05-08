---
title: "Image Generation: Editorial Fashion Photography"
description: Compare editorial fashion photography outputs generated with baseline and MTP Skill slider settings.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/comparisons_image-generation_02_editorial-fashion-photography.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/comparisons_image-generation_02_editorial-fashion-photography.png
---

**Prompt**

```markdown
/mtp <args>

<agent_instruction>

[IMAGE TASK]
prompt = """
High-end editorial fashion photography, a professional model wearing haute couture, highly stylized, captured on a Hasselblad 500CM medium format camera, with a 120mm f/4 lens and f/8.0 for sharpness. Precise studio strobe lighting from a beauty dish defines facial structure and highlights every textural detail of the fabric. Photorealistic masterpiece, stunning realism, film grain texture, natural skin tones.
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
| <img src="/images/comparisons/02_editorial-fashion-photography/gpt-image-2_gpt-5-5-medium_codex/baseline.png" alt="GPT Image 2 baseline" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/02_editorial-fashion-photography/gpt-image-2_gpt-5-5-medium_codex/slider-a.png" alt="GPT Image 2 Side A" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/02_editorial-fashion-photography/gpt-image-2_gpt-5-5-medium_codex/slider-b.png" alt="GPT Image 2 Side B" width="200" loading="lazy" decoding="async"> |

[Go to comparison page for GPT Image 2](/comparisons/image-generation/02_editorial-fashion-photography/gpt-image-2_gpt-5-5-medium_codex/) →

### Gemini 3 Pro Image

**Sample outputs**

| Baseline | Side A Nodes | Side B nodes |
|----------|----------|----------|
| <img src="/images/comparisons/02_editorial-fashion-photography/gemini-3-pro-image_gemini-3-flash_antigravity/baseline.jpg" alt="Gemini 3 Pro Image baseline" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/02_editorial-fashion-photography/gemini-3-pro-image_gemini-3-flash_antigravity/slider-a.png" alt="Gemini 3 Pro Image Side A" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/02_editorial-fashion-photography/gemini-3-pro-image_gemini-3-flash_antigravity/slider-b.png" alt="Gemini 3 Pro Image Side B" width="200" loading="lazy" decoding="async"> |

[Go to comparison page for Gemini 3 Pro Image](/comparisons/image-generation/02_editorial-fashion-photography/gemini-3-pro-image_gemini-3-flash_antigravity/) →
