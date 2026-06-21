---
title: ノードリファレンス
description: MTP の 9 つの軸と Side A / Side B の各ノードについて、ノードが表す方向と MTP Skill による出力傾向を整理します。
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

従来のプロンプトエンジニアリングでは、トーンや振る舞いを調整する際に「専門家として振る舞って」「ステップ・バイ・ステップで考えて」といった自然言語の修飾表現に頼ることがよくあります。  
こうした表現は曖昧になりやすく、タスクそのものとは別に、プロンプトの不要なノイズを持ち込みがちです。

**MTP** では、その種の制御の多くを、**座標と軸ラベル**という非言語的なメタデータに置き換え、段階的な制約としてコンパイルします。  
このページでは、Side A / Side B の各ノードについて、**ノードが表す方向**と、現在の **MTP Skill による出力傾向**を分けて示します。

ノードが表す方向は、プロンプト制御だけでなく、概念の分類や順序づけにも使えます。  
MTP Skill による出力傾向は、その方向を LLM の応答へ反映したときの振る舞いです。

---

## ノードクイックリファレンス

MTP の各色軸には、Side A と Side B の2つの「ノード（`<node>`）」があります。  
強度（`<intensity>`）は `0` から `100` の範囲で指定できます。

Side A は正方向のノードで、`power:70`（`<node>:<intensity>`）のようにノード名で指定できます。  
Side B は逆方向のノードで、`void:70` のようにノード名で指定できます。

色名で指定する場合は、正の値が Side A、負の値が Side B に対応します。  
たとえば `red:70` は Power、`red:-70` は Void として働きます。  
同じ極性の規則はノード名にも適用され、`power:-70` も Red 軸を Void 側として有効化します。

### Side A クイックリファレンス

| | 色 / 軸 | ノード | 指定例 | ノードが表す方向 | MTP Skill による出力傾向 |
|---|---|---|---|---|---|
| <div class="dot-sm bg-open" aria-label="yellow"></div> | Yellow | `open` | `open:100` / `yellow:100` / `D:4` | 開放、可能性、拡張 | 発想を広げ、選択肢を増やし、判断の余地を残す |
| <div class="dot-sm bg-power" aria-label="red"></div> | Red | `power` | `power:100` / `red:100` / `J:4` | 力、主張、推進力 | 主張を強め、判断を示し、結論へ押し進める |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | Magenta | `return` | `return:100` / `magenta:100` / `P:4` | 回帰、反転、反復、再解釈 | 前提を問い直し、別の読みや枠組みへ切り替える |
| <div class="dot-sm bg-grow" aria-label="green"></div> | Green | `grow` | `grow:100` / `green:100` / `D:10` | 成長、展開、広がり | 説明を広げ、情報を重ね、関連する枝を伸ばす |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | Transparent | `helix` | `helix:100` / `transparent:100` | 統合、構造の展開、要素間の結び付き | 手順をつなぎ、構造と理由を追える形で示す |
| <div class="dot-sm bg-focus" aria-label="white"></div> | White | `focus` | `focus:100` / `white:100` / `P:10` | 精度、明瞭さ、定義 | 対象を絞り、曖昧さを除き、根拠を添える |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | Cyan | `enter` | `enter:100` / `cyan:100` / `D:16` | 境界、導入、枠組み | 前提、範囲、入口を示し、読み手を内容へ導く |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | Blue | `flow` | `flow:100` / `blue:100` / `J:16` | 連続、接続、リズム | 文や段落を滑らかにつなぎ、読み進めやすくする |
| <div class="dot-sm bg-close" aria-label="purple"></div> | Purple | `close` | `close:100` / `purple:100` / `P:16` | 終結、完了、収束 | 要点を収束させ、結論や次の行動で締める |

### Side B クイックリファレンス

| | 色 / 軸 | ノード | 指定例 | ノードが表す方向 | MTP Skill による出力傾向 |
|---|---|---|---|---|---|
| <div class="dot-sm bg-still" aria-label="yellow"></div> | Dark Yellow | `still` | `still:100` / `yellow:-100` / `A:1` | 抑制、保持、静止 | 新しい提案を加えず、変更を抑え、与えられた状態を保つ |
| <div class="dot-sm bg-void" aria-label="red"></div> | Dark Red | `void` | `void:100` / `red:-100` / `J:1` | 不在、削減、空洞化、沈黙 | 情報と装飾を削り、簡素で最小限の応答へ寄せる |
| <div class="dot-sm bg-surge" aria-label="magenta"></div> | Dark Magenta | `surge` | `surge:100` / `magenta:-100` / `S:1` | 放出、過剰、あふれ出し | 情報と感情を高密度に重ね、勢いよく放出する |
| <div class="dot-sm bg-wither" aria-label="green"></div> | Dark Green | `wither` | `wither:100` / `green:-100` / `A:10` | 減衰、刈り込み、衰退 | 枝葉を落とし、説明を短くし、要点だけを残す |
| <div class="dot-sm bg-collapse" aria-label="transparent"></div> | Translucent (Transparent) | `collapse` | `collapse:100` / `transparent:-100` | 圧縮、収束、構造の崩れ | 選択肢と段階を減らし、単純で直接的な回答へ縮める |
| <div class="dot-sm bg-haze" aria-label="white"></div> | Dark Grey (White) | `haze` | `haze:100` / `white:-100` / `S:10` | 曖昧さ、拡散、ぼやけた輪郭 | 区別をぼかし、断定を弱め、雰囲気や含みを残す |
| <div class="dot-sm bg-drift" aria-label="cyan"></div> | Dark Cyan | `drift` | `drift:100` / `cyan:-100` / `A:19` | 逸脱、漂流、方向の揺らぎ | 連想や寄り道を許し、話題を横へ展開する |
| <div class="dot-sm bg-abyss" aria-label="blue"></div> | Dark Blue | `abyss` | `abyss:100` / `blue:-100` / `J:19` | 深さ、下降、重み | 表面的な説明を避け、重く密度の高い考察へ進む |
| <div class="dot-sm bg-fade" aria-label="purple"></div> | Dark Purple | `fade` | `fade:100` / `purple:-100` / `S:19` | 減衰、消失、残像 | 結論を閉じ切らず、情報量を落としながら余韻を残す |

Side B の色名は、軸の色を正反対の色へ反転させたものではなく、ノードの意味に沿って言い換えた呼び名です。  
haze は White が霞んでいく様として「Dark Grey (White)」、collapse は Transparent が崩れた様として「Translucent (Transparent)」と表します。

---

## 軸の構造

ここでは、分類体系の中で**各軸がどう関係しているか**を簡潔に整理します。

- **縦軸（Red ↔ Blue）:** 断定を強め、骨格をはっきりさせる方向と、受容や連続性を保つ方向が向かい合う軸。
- **横軸（Green ↔ White）:** 輪郭を保ちながら外へ広がる方向と、対象を絞って厳密に見る方向が向かい合う軸。
- **四隅（Yellow, Magenta, Cyan, Purple）:** 十字の隣接するノードをつなぐ、移行的なグラデーション領域。
- **中央（Transparent）:** 対立する方向性のあいだに置かれた、中立的なノード。

![MTP の座標系とノード配置を示す図。左に Side A / Side B の色とノードの対応、右に D:4 や A:19 などの座標ペアの例が示されています。](/images/pages/mtp-coordinate-system-and-node-layout.png)

*軸配置は、3×3 の Side A / Side B マップとしても、19×19 グリッド上の座標位置としても読むことができます。*

---

## Side A / Side B の違い

出力上の傾向として、Side A は「前へ進める力」として現れやすいです。  
紹介文であれば、読者を誘う、理由を増やす、骨格をはっきりさせる、焦点を合わせる、結論へ運ぶ、といった方向に働きます。

一方で、Side B は単に弱い Side A ではありません。  
同じ軸の反転極として、構築よりも削ぎ落とし、明快化よりも曖昧化、展開よりも沈み込み、完結よりも余韻へ寄せる傾向があります。  
Side B は「悪い」または「低い」側ではなく、その軸の影や裏面として機能します。

---

## Side B の解釈

**チェビシェフ距離に基づく径方向のルール**では、外周フレーム上の座標は、そのゾーンでは **Side B** に反転します。  
制約設計では、Side B は同じ軸の**反転極**（陰陽の対極）として表現されます（例: Power → Void、Focus → Haze、Grow → Wither）。

ただし、Side A と同様に、モデルごとの差や揺れは残ります。

---

## ノードとプリセットの組み合わせ

MTP では、複数のノードを同時に指定して出力傾向をブレンドすることもできます。  
単一のノードで出力を切り替えるだけでなく、たとえば断定性（`power:20`）と精度（`focus:30`）を組み合わせたり、展開（`grow:20`）と読みやすさ（`flow:50`）を組み合わせたりするように、複数の軸を重ねてグラデーションのように調整できます。

MTP のノードを組み合わせれば、操作の負荷を下げながら、モデルの出力傾向を変えられます。

複数の MTP トークンがあるとき、**各トークンは同じ Space / Intensity の規則**で個別に解決され、コンパイラは **書いた順（パース順）** に、トークンごとの制約ブロックを出力します。

この順序は、第三のパラメータ空間や「動き」専用レイヤーとしては扱われません。  
並びをグリッド上の**意味的な軌跡**のように読むことはできますが、**設計上の任意の読み方**にすぎません。

**名前付きスライダー**（`power:100`, `flow:70`）は意味が追いやすい出発点、**グリッド座標指定**はメッセージを短く保ちたいときに向いています。

**名前付きプリセット**は、`skills/mtp/references/presets.yaml` で定義された固定の座標列に展開され、再現性のある複数ステップのブレンドに応用できます。
