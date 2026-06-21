---
title: Image Generation
description: Compare image generation outputs produced from the same prompts using different /mtp arguments.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/comparisons_image-generation.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/comparisons_image-generation.png
lastUpdated: true
---

Each block below compares image generation outputs produced with the same prompt and `/mtp <args>` commands, similar to the text-generation comparisons. You can inspect each command’s behavior and differences across MTP nodes (such as `power` and `flow`). Tests use several distinct prompts across different models.

> [!NOTE]
> MTP Skill is not optimized for image generation. MTP Skill adapts to input text, so image-generation use requires extra care. The prompt must clearly define how the Skill should affect image composition, lighting, style, or framing. Interoperation between image generation and Agent Skills also varies by model and tool. In the prompt records below, `<agent_instruction>` represents that bridge text.

---

## MTP effects in images

These two image comparisons provide a quick read before the full prompt records. The subject and composition stay fixed while only the MTP argument changes, making the visible effect easier to compare.

### Portrait

The same argument style can also be used in image-generation prompts. Here, `power` is varied while the portrait composition is held constant, making the change appear mainly in the intensity of the eyes and expression.

![Image-generation comparison for a portrait of Mozart showing changes from different /mtp power intensities.](/images/examples/mtp-examples-gpt-image-2-portrait-of-mozart.png)

### Small bouquet

Here, the bouquet subject and occasion are held constant while the MTP node is varied, making the change appear mainly in the bouquet's openness, density, pruning, wrapping, and overall mood.

![Image-generation comparison for a small bouquet showing changes from different MTP arguments.](/images/examples/mtp-examples-gpt-image-2-small-bouquet.png)

---

## Comparison prompts

Below are the prompts in descending order (implementation order).

### 3. Geometric billiards painting

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

[Go to image generation results for "Geometric billiards painting"](/comparisons/image-generation/03_geometric-billiards-painting/) →

---

### 2. Editorial fashion photography

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

[Go to image generation results for "Editorial fashion photography"](/comparisons/image-generation/02_editorial-fashion-photography/) →

---

### 1. Mona Lisa portrait

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

[Go to image generation results for "Mona Lisa portrait"](/comparisons/image-generation/01_mona-lisa-portrait/) →
