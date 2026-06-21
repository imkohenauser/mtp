---
title: テキスト生成
description: 同じプロンプトに異なる /mtp 引数を指定したときのテキスト生成結果を、複数のモデルで比較します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_text-generation.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_text-generation.png
lastUpdated: true
---

以下の各ブロックは、同一のプロンプトと `/mtp <args>` コマンドを使ったテキストの出力結果を比較します。  
各コマンドの挙動と、MTP のノード（`power` や `flow` など）ごとの違いを確認できます。  
いくつかの異なるプロンプトで、モデルごとにテストを行っています。

> [!NOTE]
> 「テキスト生成」は言語ごとのプロンプトで行っています。  
> 結果は翻訳ではなく、英語サイトでは英語での入出力、日本語サイトでは日本語での入出力を掲載しています。  
> よければ、英語での結果もあわせてご覧ください。

---

## MTP 引数によるテキストの変化

詳細な比較用プロンプトに入る前に、同じ文学紹介プロンプトへ MTP 引数を加えたときの変化を確認します。  
日本語の例では、Claude.ai 上の Sonnet 4.6 でルイス・キャロル『不思議の国のアリス』の紹介文を生成しています。

### 単一ノードの強度

`power` と `surge` は、プロンプトを固定したままノードの強度だけを変えています。  
文の押し出し、緊張感、速度感の違いを比較しやすくしています。

![ルイス・キャロル『不思議の国のアリス』の紹介文を題材に、Claude.ai 上で /mtp power の強度によるテキスト生成結果の変化を示す比較画像。](/images/examples/mtp-examples-claude-ai-story-of-alice-power-ja.png)

![ルイス・キャロル『不思議の国のアリス』の紹介文を題材に、Claude.ai 上で /mtp surge の強度によるテキスト生成結果の変化を示す比較画像。](/images/examples/mtp-examples-claude-ai-story-of-alice-surge-ja.png)

### ノードとプリセットの違い

次の例では、複数引数やプリセット形式の指定を比較し、さらに同じ強度で異なるノードを指定したときの差分を示しています。

![ルイス・キャロル『不思議の国のアリス』の紹介文を題材に、Claude.ai 上で異なる MTP ノードを同じ強度で指定したときの違いを示す比較画像。](/images/examples/mtp-examples-claude-ai-story-of-alice-various-ja.png)

![ルイス・キャロル『不思議の国のアリス』の紹介文を題材に、Claude.ai 上で複数の MTP 引数とプリセット形式の指定による違いを示す比較画像。](/images/examples/mtp-examples-claude-ai-story-of-alice-multiple-ja.png)

---

## 比較用プロンプト

以下に、比較用プロンプトを降順（実施順）で掲載します。

### 4. 文学課題：『不思議の国のアリス』の紹介

**プロンプト**

```markdown
/mtp <args> 
ルイス・キャロルの「不思議の国のアリス」を、読んでみたくなるように紹介してください。
```

[「文学課題：『不思議の国のアリス』の紹介」のテスト結果へ](/ja/comparisons/text-generation/04_alice-in-wonderland/)  →

---

### 3. 設計課題：観光プラン提案

**プロンプト**

```markdown
/mtp <args> 
夏に京都へ一週間滞在します。特別な一日の観光プランを提案してください。営業時間や予約など、事前確認が必要な点も示してください。
```

[「設計課題：観光プラン提案」のテスト結果へ](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/)  →

---

### 2. 比較課題：モデルの自己紹介

**プロンプト**

```markdown
/mtp <args> 
他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

[「比較課題：モデルの自己紹介」のテスト結果へ](/ja/comparisons/text-generation/02_model-self-compare/)  →

---

### 1. 説明課題：言語の成り立ち

**プロンプト**

```markdown
/mtp <args> 
日本語の起源と歴史的な発展について説明してください。
```

[「説明課題：言語の成り立ち」のテスト結果へ](/ja/comparisons/text-generation/01_origins-of-language/)  →
