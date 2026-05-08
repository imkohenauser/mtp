---
title: "Gemini 3 Pro Image | Mona Lisa Portrait"
description: 'Compare baseline and MTP Skill slider outputs for the Mona Lisa Portrait prompt with Gemini 3 Pro Image via Gemini 3 Flash on Google Antigravity.'
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/comparisons_image-generation_01_mona-lisa-portrait_gemini-3-pro-image.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/comparisons_image-generation_01_mona-lisa-portrait_gemini-3-pro-image.png
---

**Metadata**

- Date: 2026-04-30
- Tool: Google Antigravity (macOS app)
- Model: Gemini 3 Pro Image via Gemini 3 Flash

## Baseline

**Prompt**

```markdown
[IMAGE TASK]
prompt = """
A captivating, hyper-realistic close-up portrait photograph reimagining the Mona Lisa as a real woman. Her skin is luminous, with flawless texture and natural makeup, revealing subtle pores. She possesses delicate, refined features and that iconic, enigmatic smile with a gentle gaze. Illuminated by flattering, soft studio lighting, creating a perfect balance. Captured with a shallow depth of field and a beautifully soft bokeh background. Cinematic clarity, ultra-high detail, photorealistic masterpiece.
"""

result = client.images.generate(
    model="gemini-3-pro-image-preview",
    prompt=prompt,
    size="1024x1024",
    aspect_ratio="1:1",
)
```

**Output**

<img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/baseline.jpg" alt="Gemini 3 Pro Image, baseline" width="200" loading="lazy" decoding="async">

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
A captivating, hyper-realistic close-up portrait photograph reimagining the Mona Lisa as a real woman. Her skin is luminous, with flawless texture and natural makeup, revealing subtle pores. She possesses delicate, refined features and that iconic, enigmatic smile with a gentle gaze. Illuminated by flattering, soft studio lighting, creating a perfect balance. Captured with a shallow depth of field and a beautifully soft bokeh background. Cinematic clarity, ultra-high detail, photorealistic masterpiece.
"""

result = client.images.generate(
    model="gemini-3-pro-image-preview",
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
| <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/open-100.jpg" alt="Gemini 3 Pro Image, open:100" width="200" loading="lazy" decoding="async">  `open:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/power-100.jpg" alt="Gemini 3 Pro Image, power:100" width="200" loading="lazy" decoding="async">  `power:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/return-100.jpg" alt="Gemini 3 Pro Image, return:100" width="200" loading="lazy" decoding="async">  `return:100` |
| <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/grow-100.jpg" alt="Gemini 3 Pro Image, grow:100" width="200" loading="lazy" decoding="async">  `grow:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/helix-100.jpg" alt="Gemini 3 Pro Image, helix:100" width="200" loading="lazy" decoding="async">  `helix:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/focus-100.jpg" alt="Gemini 3 Pro Image, focus:100" width="200" loading="lazy" decoding="async">  `focus:100` |
| <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/enter-100.jpg" alt="Gemini 3 Pro Image, enter:100" width="200" loading="lazy" decoding="async">  `enter:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/flow-100.jpg" alt="Gemini 3 Pro Image, flow:100" width="200" loading="lazy" decoding="async">  `flow:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/close-100.jpg" alt="Gemini 3 Pro Image, close:100" width="200" loading="lazy" decoding="async">  `close:100` |

### Sliders (Side B)

| Left node | Center node | Right node |
| --------- | ----------- | ---------- |
| <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/still-100.jpg" alt="Gemini 3 Pro Image, still:100" width="200" loading="lazy" decoding="async">  `still:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/void-100.jpg" alt="Gemini 3 Pro Image, void:100" width="200" loading="lazy" decoding="async">  `void:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/surge-100.jpg" alt="Gemini 3 Pro Image, surge:100" width="200" loading="lazy" decoding="async">  `surge:100` |
| <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/wither-100.jpg" alt="Gemini 3 Pro Image, wither:100" width="200" loading="lazy" decoding="async">  `wither:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/collapse-100.jpg" alt="Gemini 3 Pro Image, collapse:100" width="200" loading="lazy" decoding="async">  `collapse:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/haze-100.jpg" alt="Gemini 3 Pro Image, haze:100" width="200" loading="lazy" decoding="async">  `haze:100` |
| <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/drift-100.jpg" alt="Gemini 3 Pro Image, drift:100" width="200" loading="lazy" decoding="async">  `drift:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/abyss-100.jpg" alt="Gemini 3 Pro Image, abyss:100" width="200" loading="lazy" decoding="async">  `abyss:100` | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider/fade-100.jpg" alt="Gemini 3 Pro Image, fade:100" width="200" loading="lazy" decoding="async">  `fade:100` |
