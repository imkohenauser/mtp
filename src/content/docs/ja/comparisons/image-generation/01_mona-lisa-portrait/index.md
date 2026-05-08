---
title: "画像生成: モナ・リザのポートレート"
description: モナ・リザのポートレート生成で、ベースラインと MTP Skill のスライダー指定による出力を比較します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_image-generation_01_mona-lisa-portrait.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_image-generation_01_mona-lisa-portrait.png
---

**プロンプト**

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

| ベースライン | Side A ノード | Side B ノード |
|----------|----------|----------|
| <img src="/images/comparisons/01_mona-lisa-portrait/gpt-image-2_gpt-5-5-medium_codex/baseline.png" alt="GPT Image 2 ベースライン" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/01_mona-lisa-portrait/gpt-image-2_gpt-5-5-medium_codex/slider-a.png" alt="GPT Image 2 サイド A" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/01_mona-lisa-portrait/gpt-image-2_gpt-5-5-medium_codex/slider-b.png" alt="GPT Image 2 サイド B" width="200" loading="lazy" decoding="async"> |

[「GPT Image 2」の結果比較ページへ](/ja/comparisons/image-generation/01_mona-lisa-portrait/gpt-image-2_gpt-5-5-medium_codex/) →


### Gemini 3 Pro Image

**出力の抜粋**

| ベースライン | Side A ノード | Side B ノード |
|----------|----------|----------|
| <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/baseline.jpg" alt="Gemini 3 Pro Image ベースライン" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider-a.png" alt="Gemini 3 Pro Image サイド A" width="200" loading="lazy" decoding="async"> | <img src="/images/comparisons/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/slider-b.png" alt="Gemini 3 Pro Image サイド B" width="200" loading="lazy" decoding="async"> |

[「Gemini 3 Pro Image」の結果比較ページへ](/ja/comparisons/image-generation/01_mona-lisa-portrait/gemini-3-pro-image_gemini-3-flash_antigravity/) →
