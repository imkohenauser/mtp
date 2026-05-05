---
title: "Gemini 3 Pro Image | Geometric Billiards Painting"
description: '「幾何学的なビリヤードの絵画」プロンプトに対する Gemini 3 Pro Image via Gemini 3 Flash (Google Antigravity) のベースラインと MTP Skill スライダー出力を比較します。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Google Antigravity (macOS app)
- Model: Gemini 3 Pro Image via Gemini 3 Flash

## ベースライン

**プロンプト**

```markdown
[IMAGE TASK]
prompt = """
Precisionist, minimalist painting of billiards and energy. Clean, sharp lines and smooth surface gradients. Low-angle perspective looking up at the table's edge. Abstract geometric shapes representing power and motion. Cool, muted tones with high-contrast shadows. Perfectly calculated composition, clinical yet powerful atmosphere. A sterile, perfectly symmetrical hall filled with intense, silent tension.
"""

result = client.images.generate(
    model="gemini-3-pro-image-preview",
    prompt=prompt,
    size="1024x1024",
    aspect_ratio="1:1",
)
```

**出力**

<img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/baseline.jpg" alt="Gemini 3 Pro Image の baseline" width="200" loading="lazy" decoding="async">

---

## 入力

**プロンプト**

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
    model="gemini-3-pro-image-preview",
    prompt=prompt,
    size="1024x1024",
    aspect_ratio="1:1",
)
```

### 制約

`composition, lighting, style, subject framing, and subjects`


## 出力


### スライダー（Side A）

| 左側ノード | 中央ノード | 右側ノード |
| ---------- | ---------- | ---------- |
| <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/open-100.jpg" alt="Gemini 3 Pro Image の open:100" width="200" loading="lazy" decoding="async">  `open:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/power-100.jpg" alt="Gemini 3 Pro Image の power:100" width="200" loading="lazy" decoding="async">  `power:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/return-100.jpg" alt="Gemini 3 Pro Image の return:100" width="200" loading="lazy" decoding="async">  `return:100` |
| <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/grow-100.jpg" alt="Gemini 3 Pro Image の grow:100" width="200" loading="lazy" decoding="async">  `grow:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/helix-100.jpg" alt="Gemini 3 Pro Image の helix:100" width="200" loading="lazy" decoding="async">  `helix:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/focus-100.jpg" alt="Gemini 3 Pro Image の focus:100" width="200" loading="lazy" decoding="async">  `focus:100` |
| <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/enter-100.jpg" alt="Gemini 3 Pro Image の enter:100" width="200" loading="lazy" decoding="async">  `enter:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/flow-100.jpg" alt="Gemini 3 Pro Image の flow:100" width="200" loading="lazy" decoding="async">  `flow:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/close-100.jpg" alt="Gemini 3 Pro Image の close:100" width="200" loading="lazy" decoding="async">  `close:100` |

### スライダー（Side B）

| 左側ノード | 中央ノード | 右側ノード |
| ---------- | ---------- | ---------- |
| <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/still-100.jpg" alt="Gemini 3 Pro Image の still:100" width="200" loading="lazy" decoding="async">  `still:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/void-100.jpg" alt="Gemini 3 Pro Image の void:100" width="200" loading="lazy" decoding="async">  `void:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/surge-100.jpg" alt="Gemini 3 Pro Image の surge:100" width="200" loading="lazy" decoding="async">  `surge:100` |
| <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/wither-100.jpg" alt="Gemini 3 Pro Image の wither:100" width="200" loading="lazy" decoding="async">  `wither:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/collapse-100.jpg" alt="Gemini 3 Pro Image の collapse:100" width="200" loading="lazy" decoding="async">  `collapse:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/haze-100.jpg" alt="Gemini 3 Pro Image の haze:100" width="200" loading="lazy" decoding="async">  `haze:100` |
| <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/drift-100.jpg" alt="Gemini 3 Pro Image の drift:100" width="200" loading="lazy" decoding="async">  `drift:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/abyss-100.jpg" alt="Gemini 3 Pro Image の abyss:100" width="200" loading="lazy" decoding="async">  `abyss:100` | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/fade-100.jpg" alt="Gemini 3 Pro Image の fade:100" width="200" loading="lazy" decoding="async">  `fade:100` |
