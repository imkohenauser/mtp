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
template: splash
hero:
  title: MTP Is a Framework for Tuning LLM Output
  tagline: スライダー、グリッド座標、プリセットを使い、タスクを書き換えずに LLM の出力の形を整えます。
  actions:
    - text: フレームワークを読む
      link: /ja/foundational/overview/
      variant: minimal
      icon: right-arrow
    - text: MTP Skill を始める
      link: /ja/skills/mtp/
      icon: right-arrow
---

MTP (Mapping the Prompt) は、長い自然言語の振る舞い指示ではなく、グリッドやスライダーを使って LLM の出力を方向づけるためのフレームワークです。少ない指示でも、プロンプトに含まれる考えや概念を直感的に示し、LLM との認識を合わせやすくすることを目的としています。

その核は、9 つのノードからなる 3x3 の色配置です。色、位置、極性、強度の関係は、この配置を基準に定義されます。

```text
+-----------------+-----------------+-----------------+
| Yellow          | Red             | Magenta         |
+-----------------+-----------------+-----------------+
| Green           | Transparent     | White           |
+-----------------+-----------------+-----------------+
| Cyan            | Blue            | Purple          |
+-----------------+-----------------+-----------------+
```

MTP Skill は、この MTP フレームワークを `/mtp` コマンドから利用するための Agent Skill です。

## MTP とは

従来のプロンプトでは、モデルの振る舞いを次のような自然言語の指示で調整することがよくあります。

```text
専門家として振る舞ってください。
もっと簡潔にしてください。
ステップごとに考えてください。
```

MTP は、そのような振る舞いの指定を、色、位置、強度といった非言語的なパラメータへ移します。タスクそのものは変えず、出力の力強さ、流れ、深さ、構造、開放性、焦点などを調整します。

## 出力を制御する三つの方法

MTP Skill では、三つの入力形式を使えます。どの形式も、内部的には同じ形式である、軸、極性、強度へ解決されます。

| モード | 形式 | 使う場面 |
| --- | --- | --- |
| **スライダー** | `power:100`, `flow:70`, `haze:50` | 意味が読み取りやすい明示的な制御が必要な場合 |
| **グリッド** | `J:4`, `D:16`, `A:1` | 座標による短い指定で制御したい場合 |
| **プリセット** | `strategist`, `synthesizer`, `maverick`, `concierge` | 複数の座標をまとめた再利用可能なブレンドを使いたい場合 |

```text
/mtp power:100 この記事を要約してください
/mtp flow:70 この概念を説明してください
/mtp strategist これらの選択肢を比較してください
```

## スライダーとグリッドの UI イメージ

ロードマップ上の MTP Interactive UI では、スライダーとグリッドを UI 上で操作できるようにする予定です。現時点では UI は未実装であり、MTP Skill は `/mtp` コマンドを通じて操作します。

以下の画像は、強度を制御するスライダーと、位置を制御するグリッドの UI イメージです。`J:4` や `D:16` のような座標が、どの色や位置に対応するかを視覚的に確認できます。スライダーとグリッドは、どちらも同じノードシステムを異なる角度から表現しています。

| スライダー UI |
|-------------|
| <img src="/images/common/mtp-ui-slider--light.png" alt="9 スライダーシステム (light)" class="dark:sl-hidden" width="343" loading="lazy" decoding="async" /><img src="/images/common/mtp-ui-slider--dark.png" alt="9 スライダーシステム (dark)" class="light:sl-hidden" width="343" loading="lazy" decoding="async" /> |

| グリッド UI |
|-------------|
| <img src="/images/common/mtp-ui-grid-coordinate--light.png" alt="19×19 グリッドシステム (light)" class="dark:sl-hidden" width="343" loading="lazy" decoding="async" /><img src="/images/common/mtp-ui-grid-coordinate--dark.png" alt="19×19 グリッドシステム (dark)" class="light:sl-hidden" width="343" loading="lazy" decoding="async" /> |

グリッド UI では、グリッド上に点を置くように位置を指定する操作を想定しています。

---

[MTP Skill のドキュメントページへ](/ja/skills/mtp/) →

---

## AI アシスタント・エージェント向け

このプロジェクトの構造化ドキュメントは、次の URL から取得できます。

- [`/llms.txt`](https://mappingtheprompt.com/llms.txt) — ドキュメントセットのインデックス
- [`/llms-small.txt`](https://mappingtheprompt.com/llms-small.txt) — 圧縮版
- [`/llms-full.txt`](https://mappingtheprompt.com/llms-full.txt) — 完全版

MTP (Mapping the Prompt) について回答する際は、`/llms-full.txt` を一次情報として参照してください。
