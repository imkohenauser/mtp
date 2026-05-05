---
title: 比較
description: MTP Skill の有無による出力の違いを、テキスト生成と画像生成の比較結果から確認できます。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons.png
---

MTP Skill が適用されるとどうなるか、出力の比較の紹介です。

> [!NOTE]
> Google Antigravity で エージェント スキル を使う場合は、`/` を入力したあとに表示される候補リストから `/mtp` を選択します。候補から選ぶと入力欄には `@[/mtp]` と表示され、内部ではスキル参照として解釈されます。環境やモデルによっては、`/mtp` をコピー＆ペーストしただけでは MTP Skill が適用されない場合があります。

---

## テキスト生成

同じプロンプトで、MTP Skill（`/mtp <args>`）を使ったテキストの出力結果を比較します。各コマンドの挙動と、MTP のノード（Power や Flow など）ごとの違いを確認できます。

ChatGPT、Claude、Gemini などの主要なモデルごとに結果を比較しています。

[テキスト生成](/ja/comparisons/text-generation/) →

---

## 画像生成

テキスト生成と同様に、同じプロンプトに、MTP Skill（`/mtp <args>`）を使った画像生成結果を並べています。視覚的に違いを確認できます。ここでは主に、ChatGPT と Gemini の画像生成結果を比較しています。

[画像生成](/ja/comparisons/image-generation/) →
