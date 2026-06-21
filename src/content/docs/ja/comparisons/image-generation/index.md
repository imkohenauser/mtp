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
lastUpdated: true
---

以下の各ブロックは、「テキスト生成」と同様に、同一のプロンプトと `/mtp <args>` コマンドを使った画像生成の出力結果を比較します。  
各コマンドの挙動と、MTP のノード（`power` や `flow` など）ごとの違いを確認できます。  
いくつかの異なるプロンプトで、モデルごとにテストを行っています。

> [!NOTE]
> MTP Skill は画像生成に最適化されていません。  
> 入力テキストに適応する Skill のため、画像生成で使う場合は追加の工夫が必要です。
>
> プロンプトでは、Skill を画像の構図、光、スタイル、フレーミングなどへどう反映するかを明示する必要があります。  
> 画像生成と Agent Skills の連携状況は、モデルやツールによって異なります。
>
> 以下のプロンプト記録では、`<agent_instruction>` が、MTP Skill の出力を画像生成タスクへ反映するための補助テキストを表します。

---

## MTP Skill による画像生成の変化

詳細なプロンプト記録に入る前に、2 つの作例で MTP の効き方を確認します。  
題材と構図を固定し、MTP 引数だけを変えることで、画像上の差分を比較しやすくしています。

### 肖像

同じ引数の考え方は、画像生成プロンプトにも使えます。  
ここでは `power` を変化させながら肖像の構図を固定し、目と表情の強度に変化が現れるようにしています。

![モーツァルトの肖像を題材に、/mtp power の強度による画像生成結果の変化を示す比較画像。](/images/examples/mtp-examples-gpt-image-2-portrait-of-mozart.png)

### 小さな花束

ここでは花束の題材と用途を固定しながら MTP ノードを変化させ、開き方、密度、剪定、包装、全体のムードに違いが現れるようにしています。

![小さな花束を題材に、MTP 引数による画像生成結果の変化を示す比較画像。](/images/examples/mtp-examples-gpt-image-2-small-bouquet.png)

---

## 比較用プロンプト

以下に、比較用プロンプトを降順（実施順）で掲載します。

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
