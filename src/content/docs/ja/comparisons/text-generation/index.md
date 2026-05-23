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

以下の各ブロックは、同一のプロンプトと `/mtp <args>` コマンドを使ったテキストの出力結果を比較します。各コマンドの挙動と、MTP のノード（Power や Flow など）ごとの違いを確認できます。いくつかの異なるプロンプトで、モデルごとにテストを行っています。

> [!NOTE]
> 「テキスト生成」は言語ごとのプロンプトで行なっています。結果は翻訳ではなく、英語サイトでは英語での入出力、日本語サイトでは日本語での入出力を掲載しています。よければ、英語での結果もあわせてご覧ください。

---

## 1. 説明課題: 言語の成り立ち

**プロンプト**

```markdown
/mtp <args> 
日本語の起源と歴史的な発展について説明してください。
```

[「説明課題: 言語の成り立ち」のテスト結果へ](/ja/comparisons/text-generation/01_origins-of-language/)  →

---

## 2. 比較課題: モデルの自己紹介

**プロンプト**

```markdown
/mtp <args> 
他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

[「比較課題: モデルの自己紹介」のテスト結果へ](/ja/comparisons/text-generation/02_model-self-compare/)  →

---

## 3. 設計課題: 観光プラン提案

**プロンプト**

```markdown
/mtp <args> 
夏に京都へ一週間滞在します。特別な一日の観光プランを提案してください。営業時間や予約など、事前確認が必要な点も示してください。
```

[「設計課題: 観光プラン提案」のテスト結果へ](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/)  →

---

## 4. 文学課題: 『不思議の国のアリス』の紹介

**プロンプト**

```markdown
/mtp <args> 
ルイス・キャロルの「不思議の国のアリス」を、読んでみたくなるように紹介してください。
```

[「文学課題: 『不思議の国のアリス』の紹介](/ja/comparisons/text-generation/04_alice-in-wonderland/)  →
