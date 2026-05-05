---
title: "Image Generation: Mona Lisa Portrait"
description: Compare Mona Lisa portrait image outputs generated with baseline and MTP Skill slider settings.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/comparisons_image-generation_01_mona-lisa-portrait.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/comparisons_image-generation_01_mona-lisa-portrait.png
---

**Prompt**

```markdown
/mtp <args>

<agent_instruction>

[IMAGE TASK]
prompt = """
A captivating, hyper-realistic close-up portrait photograph reimagining the Mona Lisa as a real woman. Her skin is luminous, with flawless texture and natural makeup, revealing subtle pores. She possesses delicate, refined features and that iconic, enigmatic smile with a gentle gaze. Illuminated by flattering, soft studio lighting, creating a perfect balance. Captured with a shallow depth of field and a beautifully soft bokeh background. Cinematic clarity, ultra-high detail, photorealistic masterpiece.
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

| Baseline | `power:100` | `flow:100` |
|----------|----------|----------|
| <img src="/images/comparisons/01_mona-lisa-portrait/gpt-image-2_gpt-5-5-medium_codex/baseline.png" alt="GPT Image 2 baseline" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/01_mona-lisa-portrait/gpt-image-2_gpt-5-5-medium_codex/slider/power-100.png" alt="GPT Image 2 power:100" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/01_mona-lisa-portrait/gpt-image-2_gpt-5-5-medium_codex/slider/flow-100.png" alt="GPT Image 2 flow:100" width="200" loading="lazy" decoding="async"> |

[Go to comparison page for GPT Image 2](/comparisons/image-generation/01_mona-lisa-portrait/gpt-image-2_gpt-5-5-medium_codex/) →

### Gemini 3 Pro Image

**Sample outputs**

| Baseline | `power:100` | `flow:100` |
|----------|----------|----------|
| <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/baseline.jpg" alt="Gemini 3 Pro Image baseline" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/power-100.jpg" alt="Gemini 3 Pro Image power:100" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/flow-100.jpg" alt="Gemini 3 Pro Image flow:100" width="200" loading="lazy" decoding="async"> |

[Go to comparison page for Gemini 3 Pro Image](/comparisons/image-generation/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/) →
