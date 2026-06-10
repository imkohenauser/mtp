---
title: MTP (Mapping the Prompt)
description: MTP は、グリッド、スライダー、プリセットを使って LLM の出力を方向づけるためのフレームワークです。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp.png
hero:
  title: MTP Is a Framework for Tuning LLM Output
  tagline: スライダー、グリッド座標、プリセットを使い、タスクを書き換えずに LLM の出力の形を整えます。
  actions:
    - text: MTP Skill を始める
      link: /ja/skills/mtp/
      icon: right-arrow
lastUpdated: true
---

MTP (Mapping the Prompt) は、長い自然言語の振る舞い指示ではなく、グリッドやスライダーを使って LLM の出力を方向づけるためのフレームワークです。少ない指示でも、プロンプトに含まれる考えや概念を直感的に示し、LLM との認識を合わせやすくすることを目的としています。

![MTP のキービジュアル。左のパネルには Open–Still や Power–Void などの Side A / Side B のノードスライダーが示され、Power は 70 に設定されています。右のパネルには A–S と 1–19 のラベルが付いた 19x19 の column:row カラーグリッドが示されています。](/ogp.png)

その核は、9 つのノードからなる 3x3 の色配置です。色、位置、極性、強度の関係は、この配置を基準に定義されます。3x3 の各色には、Side A と Side B の極性に対応するノードが定義されています。たとえば、左上の Yellow は Side A では Open、Side B では Still に対応します。

MTP Skill は、この MTP フレームワークを `/mtp` コマンドから利用するための Agent Skill です。

## MTP とは

従来のプロンプトでは、モデルの振る舞いを次のような自然言語の指示で調整することがよくあります。

> 専門家として振る舞ってください。  
> もっと簡潔にしてください。  
> ステップごとに考えてください。

MTP は、そのような振る舞いの指定を、色、位置、強度といった非言語的なパラメータへ移します。タスクそのものは変えず、出力の力強さ、流れ、深さ、構造、開放性、焦点などを調整します。

## 出力を制御する三つの方法

MTP Skill では、三つの入力形式を使えます。どの形式も、内部的には同じ形式である、軸、極性、強度へ解決されます。

| モード | 形式 | 使う場面 |
| --- | --- | --- |
| **スライダー** | `power:100`, `flow:70`, `haze:50` | 意味が読み取りやすい明示的な制御が必要な場合 |
| **グリッド** | `J:4`, `D:16`, `A:1` | 座標による短い指定で制御したい場合 |
| **プリセット** | `strategist`, `synthesizer`, `maverick`, `concierge` | 複数の座標をまとめた再利用可能なブレンドを使いたい場合 |

```text
# スライダー
/mtp power:100 この記事を要約してください

# グリッド
/mtp J:4 この概念を説明してください

# プリセット
/mtp strategist これらの選択肢を比較してください
```

## スライダーとグリッドの UI イメージ

ロードマップ上の MTP Interactive UI では、スライダーとグリッドを UI 上で操作できるようにする予定です。現時点では UI は未実装であり、MTP Skill は `/mtp` コマンドを通じて操作します。

以下の画像は、強度を制御するスライダーと、位置を制御するグリッドの UI イメージです。`J:4` や `D:16` のような座標が、どの色や位置に対応するかを視覚的に確認できます。スライダーとグリッドは、どちらも同じノードシステムを異なる角度から表現しています。

### スライダー

![/mtp node:intensity によるMTP Slider Argumentsを説明する図。左はSide AとSide Bのノードスライダーを示し、Powerが70に設定されている。右はOpen、Power、Focus、Flow、Close、Surge、Collapse、Fadeなどの方向を、3Dチェビシェフ距離として示している。](/images/pages/mtp-slider-arguments-mtp-node-intensity.png)
*Slider Argumentsは、ノード名と強度値を組み合わせ、MTP空間の中心からSide AまたはSide Bの方向へ移動する指定方法です。*

### グリッド

![/mtp column:row によるMTP Grid Argumentsを説明する図。左は3×3の色グリッドを19×19座標上に単純化して示し、J:4、D:10、P:10、J:16などの例を表示している。右は19×19全体のRGBA値の分布を示している。](/images/pages/mtp-grid-arguments-mtp-column-row.png)
*Grid Argumentsは、19×19のMTP座標の平面上の一点を指定し、その位置をノード方向とRGBAの色値に対応させる指定方法です。*

グリッド UI では、グリッド上に点を置くように位置を指定する操作を想定しています。

---

## AIエージェントへ

ドキュメントサイトのビルド時に、主要なページが単一の `llms.txt` ファイルへ集約されます。このファイルを AI エージェントに渡すことで、本サイトを理解し説明するために必要なコンテキストを提供できます。

**AI エージェント向け:**  
[mappingtheprompt.com/llms.txt](https://mappingtheprompt.com/llms.txt)