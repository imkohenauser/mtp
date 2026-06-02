---
title: 概要
description: MTP の基本用語と、スライダー、グリッド座標、プリセットが制約へ変換される仕組みを説明します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_foundational_overview.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_foundational_overview.png
lastUpdated: true
---

MTP (Mapping the Prompt) は、長い自然言語による振る舞い指示の代わりに、構造化されたコントロール（スライダー、グリッド座標、プリセット）で LLM の出力を制御するためのフレームワークです。

モデルのトーンや語り口を言葉で直接指示する代わりに、**座標ベースのコンパイル手順**で制御します。「簡潔に」「深く考えて」といった直接的な指示に頼るのではなく、構造化された空間内の位置を指定します。指定方法は、スライダー値、グリッド座標、名前付きプリセットのいずれでもかまいません。コンパイラはその位置を決定論的に変換し、出力の形を変える制約 XML に落とし込みます。

このページでは、**基本用語**と、MTP の制御を支える二つのレイヤーの簡易仕様をまとめます。この二つのレイヤーは、実際の挙動に即して言えば **グリッド上の位置** と **強度・極性** として整理でき、内部モデルでは **Space** と **Intensity** と呼びます。計算式やゾーン境界の完全な定義はグリッドと座標系で、各ノードの振る舞いの要約はノードリファレンスで扱います。

Space の基準となる 3x3 の色配置は次のとおりです。

| 位置 | 左          | 中央          | 右        |
| ---- | ----------- | ------------- | --------- |
| 上段 | Yellow      | Red           | Magenta   |
| 中段 | Green       | Transparent   | White     |
| 下段 | Cyan        | Blue          | Purple    |

---

## 基本用語

以下の用語は、MTP のドキュメント全体で繰り返し登場します。これらは、入力から制約の適用までをつなぐパイプラインを構成しています。

```text
  ┌─────────┐     ┌──────────────────┐     ┌───────────────────────────┐     ┌─────────────┐
  │  Input  │ ──→ │     Compiler     │ ──→ │  Constraint extraction    │ ──→ │   Output    │
  └─────────┘     └──────────────────┘     └───────────────────────────┘     └─────────────┘

  プリセット ───── 展開 ─────→ グリッド座標 ─────────┐
  スライダー (node:intensity)  ────────────────→ ├→ (軸, 極性, 強度) → ノード定義ファイル → 制約
  グリッド座標 (column:row)  ───────────────────→ ┘
```


| 用語                           | 意味                                                                                             |
| ---------------------------- | ---------------------------------------------------------------------------------------------- |
| **ノード (Node)**               | 9 つある意味軸のうちの 1 つです（例: Red）。各ノードには Side A の名称（例: Power）と Side B の名称（例: Void）があります。              |
| **色 / 軸**                 | ノードの色による識別単位です。Yellow, Red, Magenta, Green, Transparent, White, Cyan, Blue, Purple の 9 種があります。 |
| **Side A / Side B**          | 各軸の両極です。強度が正なら Side A、負なら Side B が有効になります。                                                     |
| **強度 (Intensity)**           | 0〜100 の強度値です。どの制約ティア（Low / Mid / High）が抽出されるかを決めます。                                            |
| **スライダー**           | `node:intensity` 形式の入力です。例: `power:70`, `void:80`, `yellow:-30`                                |
| **グリッド**             | 19×19 グリッド上の `column:row` 形式の入力です。例: `D:16`, `A:1`。コンパイラは位置から軸、極性、強度を計算します。                           |
| **プリセット**           | パース前にグリッド座標へ展開される名前付きブレンドです。例: `strategist` は `P:16 P:4` に展開されます。                              |


どの入力経路も、最終的には同じ内部表現である **(軸, 極性, 強度)** に収束します。たとえば `power:100`、`red:100`、`J:4` のどれを入力しても、コンパイラは同じ 3 要素に解決し、同じ制約を抽出します。

| | 色 / 軸 | Side A ノード | Side B ノード   |
| --- | ----------- | ------ | -------- |
| <div class="dot-sm bg-open" aria-label="yellow"></div> | Yellow      | `open`   | `still`    |
| <div class="dot-sm bg-power" aria-label="red"></div> | Red         | `power`  | `void`     |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | Magenta     | `return` | `surge`    |
| <div class="dot-sm bg-grow" aria-label="green"></div> | Green       | `grow`   | `wither`   |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | Transparent | `helix`  | `collapse` |
| <div class="dot-sm bg-focus" aria-label="white"></div> | White       | `focus`  | `haze`     |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | Cyan        | `enter`  | `drift`    |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | Blue        | `flow`   | `abyss`     |
| <div class="dot-sm bg-close" aria-label="purple"></div> | Purple      | `close`  | `fade`     |
