---
title: ノードリファレンス
description: MTP の 9 つの軸と Side A / Side B のノードの振る舞いを、設計意図と出力傾向に沿って整理します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_foundational_node-reference.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_foundational_node-reference.png
lastUpdated: true
---

## はじめに

従来のプロンプトエンジニアリングでは、トーンや振る舞いを調整する際に「専門家として振る舞って」「ステップ・バイ・ステップで考えて」といった自然言語の修飾表現に頼ることがよくあります。こうした表現は曖昧になりやすく、タスクそのものとは別に、プロンプトの不要なノイズを持ち込みがちです。

**MTP** では、その種の制御の多くを、**座標と軸ラベル** という非言語的なメタデータに置き換え、段階的な制約としてコンパイルします。このページでは、フレームワーク内で**Side A / Side B の各ノードラベルをどう解釈する想定か**を説明します。

---

## ノードクイックリファレンス

MTP の各色軸には、Side A と Side B の2つの「ノード（`<node>`）」があります。  
強度（`<intensity>`）は `0` から `100` の範囲で指定できます。  

Side A は正方向のノードで、`power:70`（`<node>:<intensity>`） のようにノード名で指定できます。Side B は逆方向のノードで、`void:70` のようにノード名で指定できます。

色名で指定する場合は、正の値が Side A、負の値が Side B に対応します。たとえば `red:70` は Power、`red:-70` は Void として働きます。
同じ極性の規則はノード名にも適用され、`power:-70` も Red 軸を Void 側として有効化します。

### Side A クイックリファレンス

| | 色 / Axis | ノード | 指定例 | 主な特徴 | 向いている用途 |
|---|---|---|---|---|---|
| <div class="dot-md bg-open" aria-label="yellow"></div> | Yellow | Open | `open:100` / `yellow:100` / `D:4` | 可能性、発散、余白 | ブレスト、選択肢出し、企画初期、問いの拡張 |
| <div class="dot-md bg-power" aria-label="red"></div> | Red | Power | `power:100` / `red:100` / `J:4` | 主張、判断、推進力 | 提案、意思決定、プレゼン、強い結論が必要な回答 |
| <div class="dot-md bg-return" aria-label="magenta"></div> | Magenta | Return | `return:100` / `magenta:100` / `P:4` | 反転、批評、再構成 | 批評、リフレーミング、逆張り検討、思考の転換 |
| <div class="dot-md bg-grow" aria-label="green"></div> | Green | Grow | `grow:100` / `green:100` / `D:10` | 拡張、層化、展開 | 解説、学習、企画展開、アイデアの肉付け |
| <div class="dot-md bg-helix" aria-label="transparent"></div> | Transparent | Helix | `helix:100` / `transparent:100` | 構造、追跡性、道筋 | 複雑な説明、検討メモ、設計判断、推論過程の可視化 |
| <div class="dot-md bg-focus" aria-label="white"></div> | White | Focus | `focus:100` / `white:100` / `P:10` | 精度、定義、根拠 | 調査、仕様確認、レビュー、正確性が必要な回答 |
| <div class="dot-md bg-enter" aria-label="cyan"></div> | Cyan | Enter | `enter:100` / `cyan:100` / `D:16` | 導入、枠組み、範囲 | チュートリアル、オンボーディング、手順書、初学者向け説明 |
| <div class="dot-md bg-flow" aria-label="blue"></div> | Blue | Flow | `flow:100` / `blue:100` / `J:16` | 連続性、リズム、読みやすさ | エッセイ、記事、自然な説明文、読み心地を重視する文章 |
| <div class="dot-md bg-close" aria-label="purple"></div> | Purple | Close | `close:100` / `purple:100` / `P:16` | 収束、要約、次の行動 | 要約、提案書、締めの文章、CTA が必要な回答 |

### Side B クイックリファレンス

| | 色 / Axis | ノード | 指定例 | 主な特徴 | 向いている用途 |
|---|---|---|---|---|---|
| <div class="dot-md bg-still" aria-label="yellow"></div> | Dark Yellow | Still | `still:100` / `yellow:-100` / `A:1` | 抑制、保持、静止 | 整形、校正、変換、余計な提案を避けたい作業 |
| <div class="dot-md bg-void" aria-label="red"></div> | Dark Red | Void | `void:100` / `red:-100` / `J:1` | 削減、沈黙、最小化 | 短縮、無駄の削除、淡々とした回答、最小応答 |
| <div class="dot-md bg-surge" aria-label="magenta"></div> | Dark Magenta | Surge | `surge:100` / `magenta:-100` / `S:1` | 勢い、密度、圧力 | 熱量のある文章、勢いのある草稿、強い表現、詰め込み型の出力 |
| <div class="dot-md bg-wither" aria-label="green"></div> | Dark Green | Wither | `wither:100` / `green:-100` / `A:10` | 刈り込み、核心、抑制 | 要点整理、簡潔な説明、短い結論、ミニマルな文章 |
| <div class="dot-md bg-collapse" aria-label="transparent"></div> | Transparent | Collapse | `collapse:100` / `transparent:-100` | 圧縮、簡略化、終点 | 長文の圧縮、結論だけ欲しい回答、構造を簡略化した要約 |
| <div class="dot-md bg-haze" aria-label="white"></div> | Dark Grey (White) | Haze | `haze:100` / `white:-100` / `S:10` | 曖昧さ、柔らかさ、雰囲気 | 詩的表現、雰囲気づくり、抽象的な文章、印象重視の表現 |
| <div class="dot-md bg-drift" aria-label="cyan"></div> | Dark Cyan | Drift | `drift:100` / `cyan:-100` / `A:19` | 逸脱、連想、寄り道 | 随筆、創作、自由連想、発想の横展開 |
| <div class="dot-md bg-abyss" aria-label="blue"></div> | Dark Blue | Abyss | `abyss:100` / `blue:-100` / `J:19` | 深さ、重み、内省 | 深い考察、批評、思想的文章、表層ではない分析 |
| <div class="dot-md bg-fade" aria-label="purple"></div> | Dark Purple | Fade | `fade:100` / `purple:-100` / `S:19` | 余韻、減衰、残像 | 文芸的な終わり方、余白のある文章、読後感を重視する出力 |

---

## 軸の構造

ここでは、分類体系の中で**各軸がどう関係しているか**を簡潔に整理します。

- **縦軸（Red ↔ Blue）:** 断定や構造化を強める方向と、受容や連続性を保つ方向が向かい合う軸。
- **横軸（Green ↔ White）:** 輪郭を保ちながら外へ広がる方向と、対象を絞って厳密に見る方向が向かい合う軸。
- **四隅（Yellow, Magenta, Cyan, Purple）:** 十字の隣接するノードをつなぐ、移行的なグラデーション領域。
- **中央（Transparent）:** 対立する方向性のあいだに置かれた、中立的なノード。

![MTP の座標系とノード配置を示す図。左に Side A / Side B の色とノードの対応、右に D:4 や A:19 などの座標ペアの例が示されています。](/images/pages/mtp-coordinate-system-and-node-layout.png)

*軸配置は、3x3 の Side A / Side B マップとしても、19x19 グリッド上の座標位置としても読むことができます。*

---

## Side A / Side B の違い

出力上の傾向として、Side A は「前へ進める力」として現れやすいです。紹介文であれば、読者を誘う、理由を増やす、構造化する、焦点を合わせる、結論へ運ぶ、といった方向に働きます。

一方で、Side B は単に弱い Side A ではありません。同じ軸の反転極として、構築よりも削ぎ落とし、明快化よりも曖昧化、展開よりも沈み込み、完結よりも余韻へ寄せる傾向があります。Side B は「悪い」または「低い」側ではなく、その軸の影や裏面として機能します。

---

## Side B の解釈

**チェビシェフ距離に基づく径方向のルール**では、外周フレーム上の座標は、そのゾーンにおいて **Side B** に反転します。制約設計では、Side B は同じ軸の**反転極**（陰陽の対極）として表現されます（例: Power → Void、Focus → Haze、Grow → Wither）。

Side B は、その軸で極端に強めたい場合、または圧縮した表現を生成したい場合に向いています。ただし、Side A と同様に、モデルごとの差や揺れは残ります。

---

## ノードとプリセットの組み合わせ

MTP では、複数のノードを同時に指定して出力傾向をブレンドすることもできます。単一のノードで出力を切り替えるだけでなく、たとえば断定性（`power:20`）と精度（`focus:30`）を組み合わせたり、展開（`grow:20`）と読みやすさ（`flow:50`）を組み合わせたりするように、複数の軸を重ねてグラデーションのように調整できます。

MTP のノードを感覚的に組み合わせることで、操作の負荷を下げながら、モデルの出力傾向を変えられるという発想です。

複数の MTP トークンがあるとき、**各トークンは同じ Space / Intensity の規則**で個別に解決され、コンパイラは **書いた順（パース順）** に、トークンごとの制約ブロックを出力します。

この順序は、第三のパラメータ空間や「動き」専用レイヤーとしては扱われません。並びをグリッド上の**意味的な軌跡**のように読むことはできますが、**設計上の任意の読み方**にすぎません。

**名前付きスライダー**（`power:100`, `flow:70`）は意味が追いやすい出発点、**グリッド座標指定**はメッセージを短く保ちたいときに向いています。

**名前付きプリセット**は、`skills/mtp/references/presets.yaml` で定義された固定の座標列に展開され、再現性のある複数ステップのブレンドに応用できます。
