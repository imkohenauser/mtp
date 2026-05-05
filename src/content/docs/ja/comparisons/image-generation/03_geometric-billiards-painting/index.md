---
title: "画像生成: 幾何学的なビリヤードの絵画"
description: 幾何学的なビリヤードの絵画生成で、ベースラインと MTP Skill のスライダー指定による出力を比較します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_image-generation_03_geometric-billiards-painting.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_image-generation_03_geometric-billiards-painting.png
---

**プロンプト**

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

**適用範囲**
- ベースライン： 1 件（MTP Skill を適用しない）
- スライダー `<node:100>`： 18 件

**モデル**
- GPT Image 2 via ChatGPT 5.5 on Codex (macOS app)
- Gemini 3 Pro Image via Gemini 3 Flash on Antigravity (macOS app)

---

## 出力比較

テスト環境では、特別なユーザー設定や、横断的なチャット会話の記憶を含まない状態で、それぞれ、新しいエージェントチャットセッションを開始してテストを行った結果です。

### GPT Image 2

**出力の抜粋**

| ベースライン | `power:100` | `flow:100` |
|----------|----------|----------|
| <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/baseline.png" alt="GPT Image 2 baseline" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/power-100.png" alt="GPT Image 2 power:100" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/slider/flow-100.png" alt="GPT Image 2 flow:100" width="200" loading="lazy" decoding="async"> |

[「GPT Image 2」の結果比較ページへ](/ja/comparisons/image-generation/03_geometric-billiards-painting/gpt-image-2_gpt-5-5-medium_codex/) →


### Gemini 3 Pro Image

**出力の抜粋**

| ベースライン | `power:100` | `flow:100` |
|----------|----------|----------|
| <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/baseline.jpg" alt="Gemini 3 Pro Image の baseline" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/power-100.jpg" alt="Gemini 3 Pro Image の power:100" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/slider/flow-100.jpg" alt="Gemini 3 Pro Image の flow:100" width="200" loading="lazy" decoding="async"> |

[「Gemini 3 Pro Image」の結果比較ページへ](/ja/comparisons/image-generation/03_geometric-billiards-painting/gemini-3-pro-image_gemini-3-flash_antigravity/) →
