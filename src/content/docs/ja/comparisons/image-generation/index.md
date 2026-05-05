---
title: 画像生成
description: 同じ画像生成プロンプトに異なる /mtp 引数を指定したときの出力結果を比較します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_image-generation.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_image-generation.png
---

以下の各ブロックは、「テキスト生成」と同様に、同一のプロンプトと `/mtp <args>` コマンドを使った画像生成の出力結果を比較します。各コマンドの挙動と、MTP のノード（Power や Flow など）ごとの違いを確認できます。いくつかの異なるプロンプトで、モデルごとにテストを行っています。

> [!NOTE]
> MTP Skill は画像生成に最適化されていません。MTP Skill は、入力されたテキストに適応されるもので、画像生成で Skill を適応するためには工夫が必要です。どのように Skill を適応するか具体的に示す必要があります。また、モデルやツールごとに、画像生成と Agent Skills の適応状況は異なります。以下のプロンプトでは、一例として、`<agent_instruction>` を前に置き、MTP Skill の実行を強制しています。

---

### 1. モナ・リザのポートレート

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

[「モナ・リザのポートレート」の画像生成結果へ](/ja/comparisons/image-generation/01_mona-lisa-portrait/) →

---

### 2. ファッション雑誌の写真

**プロンプト**  

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

[「ファッション雑誌の写真」の画像生成結果へ](/ja/comparisons/image-generation/02_editorial-fashion-photography/) →

---

### 3. 幾何学的なビリヤードの絵画

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

[「幾何学的なビリヤードの絵画」の画像生成結果へ](/ja/comparisons/image-generation/03_geometric-billiards-painting/) →