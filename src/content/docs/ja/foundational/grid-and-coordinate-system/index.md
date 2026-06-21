---
title: グリッドと座標系
description: MTP の 19×19 グリッド、3×3 マクロゾーン、強度と極性の座標変換モデルを定義します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_foundational_grid-and-coordinate-system.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_foundational_grid-and-coordinate-system.png
lastUpdated: true
---

MTP (Mapping the Prompt) は、長い自然言語による振る舞い指示の代わりに、**Space と Intensity の二つのレイヤーからなる動的モデル**として扱うフレームワークです。  
**Space** はグリッド上の位置から軸とゾーンを決めます。  
**Intensity** は強度、極性と段階的な制約抽出を決めます（座標入力では Volcano マッピングを使用）。

一つの `/mtp` コマンドに**複数トークン**が含まれる場合（プリセット展開を含む）、制約ブロックは**書いた順**に追加されます。  
各トークンは同じ Space / Intensity の規則で解決され、順序は第三のパラメータ空間や専用の変換レイヤーにはなりません。


| レイヤー                 | 制御するもの                  | 主な考え方                               |
| -------------------- | ----------------------- | ----------------------------------- |
| **Space**     | *グリッド上の位置*。どの軸、どのゾーンか   | 19×19 グリッド、3×3 マクロゾーン、色相環           |
| **Intensity** | *強度、極性*。どれくらい強いか、どちらの極か | 0〜100 スライダー、Side A / Side B、Volcano |


このドキュメントでは、MTP の数理と幾何の構造と、プロンプトへメタデータを注入する際の内部パラメータモデルを定義します。

---

## 空間構造: 19×19 グリッドシステム

MTP の基本インターフェースは、囲碁の「碁盤」に近い線の交点からなる整数座標系を使います。（19路盤）  
グリッドの大きさは **19×19** です。

### 対称的な三分割モデル

19×19 グリッドの空間は、**3×3 のマクロゾーン構造**に分割されます。  
要素数を三つの不均等なグループに分けるのではなく、盤面全体を連続した空間として扱い、グリッド線と境界を完全に対称な形で配置します。

**19 本のグリッド線による構造**

グリッド線は合計 19 本です。  
外枠およびゾーン間を区切る境界線が 4 本あり、その内側に等幅のマクロゾーンが 3 つ並び、それぞれにグリッド線が 5 本ずつ含まれます。

```text
        A – F        G – L        M – S
 1–6   Yellow    |    Red      | Magenta
 7–12  Green     | Transparent | White
13–19  Cyan      |    Blue     | Purple
```

- **1 本目の線:** 境界線（外枠）
- **2–6 本目:** ゾーン 1（グリッド線 5 本）
- **7 本目:** 境界線（内側の境界）
- **8–12 本目:** ゾーン 2（グリッド線 5 本）
- **13 本目:** 境界線（内側の境界）
- **14–18 本目:** ゾーン 3（グリッド線 5 本）
- **19 本目の線:** 境界線（外枠）

### 境界線とゾーン割り当て

境界線は分割ではなく、概念上はマクロゾーン間の遷移領域です。  
コンパイラは境界上の座標も含め、各座標を 9 つのマクロゾーンの**いずれか 1 つ**に割り当てます（ゾーン境界の定義はコンパイラの実装に従います）。  
強度の計算には、内部座標と同じチェビシェフ距離の式を使います。

### 色相環と Z-order

9 つのマクロゾーンは色相環に対応し、生成の遷移順序（Z-order）も持っています。  
概念がどの順に展開し、処理がどの相を通って進むかを示唆します。

| | 色              | ノード      | キーワード                 |
| --- | --------------- | ----------- | ---------------------- |
| <div class="dot-sm bg-open" aria-label="yellow"></div> | **Yellow**      | `open`      | 分岐、開放、余白               |
| <div class="dot-sm bg-power" aria-label="red"></div> | **Red**         | `power`     | 力、断定、高揚                |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | **Magenta**     | `return`    | 回帰、反転、循環               |
| <div class="dot-sm bg-grow" aria-label="green"></div> | **Green**       | `grow`      | 成長、増殖、積層               |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | **Transparent** | `helix`     | 螺旋、展開、中立構造             |
| <div class="dot-sm bg-focus" aria-label="white"></div> | **White**       | `focus`     | 焦点、収束、精密               |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | **Cyan**        | `enter`     | 入口、着地、構造               |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | **Blue**        | `flow`      | 流れ、接続、リズム              |
| <div class="dot-sm bg-close" aria-label="purple"></div> | **Purple**      | `close`     | 結び、完了、締めくくり            |

---

## 強度構造: 三状態モデルと双極性

各ノードは単純なオン / オフではなく、0〜100 の連続的な強度スライダーを持ちます。  
極性の正負によって、Side A の振る舞いを有効にするか、Side B の反転挙動を有効にするかが決まります。

コンパイラは**マクロゾーンの色名**もスライダーの別名として受け付けます（例: `yellow:50` ≡ `open:50`, `yellow:-50` ≡ `still:50`）。  
対応する Side A / Side B ノードと同じ線形の強度マッピングが使われます。

### ノード対称性（D4 対称性）とペアリング

負の値は Side B、正の値は Side A を有効にします。  
中央の `0` を基準に、各ノードは次の双対ペアを構成します。


| Side B (-1)  | Center (0)  | Side A (+1) | 空間上の位置 |
| ------------ | ----------- | ----------- | ------ |
| `still`      | Yellow      | `open`      | 左上     |
| `void`       | Red         | `power`     | 上      |
| `surge`      | Magenta     | `return`    | 右上     |
| `wither`     | Green       | `grow`      | 左      |
| `collapse`   | Transparent | `helix`     | 中央     |
| `haze`       | White       | `focus`     | 右      |
| `drift`      | Cyan        | `enter`     | 左下     |
| `abyss`      | Blue        | `flow`      | 下      |
| `fade`       | Purple      | `close`     | 右下     |


---

## 座標から強度への変換モデル

`A:1` や `J:10` のような 19×19 グリッド座標（ハイフン形式 `A-1` も可）は、MTP コンパイラによってグリッド中心 `J:10` からのチェビシェフ距離をもとに**極性**（Side A / Side B）と**強度**（0〜100）へ変換されます。

### 極性と強度の計算アルゴリズム（Volcano モデル、チェビシェフ距離）

この変換は **Volcano モデル**に従います。  
中心が中立、中間リングで Side A が最大となり、外枠で Side B に反転します。  
チェビシェフ距離を使うため、中心から同じ距離にあるマクロゾーン中心はすべて同じ符号付き値になります。

**Volcano モデルの断面図（例: 10 行目、A〜S）**

```text
Signed value
        Side A
 +100 |          /\                 /\
      |         /  \               /  \
      |        /    \             /    \
    0 |-------/------\-----0-----/------\-------
      |      /     Neutral Center        \
      |     /                             \
 -100 |----/                               \----
        Side B

Distance:  9      6        0        6      9
Coord:    A:10   D:10     J:10     P:10   S:10
```

注: これは 1 次元の断面図（10 行目）です。  
実際には `J:10` を中心とした 2 次元のチェビシェフ距離の同心リングになります。

- **中心（距離 0）:** `J:10` → 符号付き値 `0`（中立、制約なし）
- **ピークリング（距離 6）:** 例: `D:10`, `D:4`, `P:16` → Side A 最大（`+100`）
- **外枠（距離 9）:** 例: `A:10`, `A:1`, `S:19` → Side B 最大（`-100`）

コンパイラの計算式:

```text
Center (J:10)      = neutral (signed 0; no constraint)
Peak (distance 6)  = Side A maximum (signed +100)
Outer (distance 9) = Side B maximum (signed -100)

distance  = max(|x - 10|, |y - 10|)   (Chebyshev, integer 0–9)
Inner (distance ≤ 6):  signed = (distance / 6) * 100
Outer (distance > 6):  signed = 100 - 200 * (distance - 6) / 3

polarity  = +1 if signed >= 0 else -1
intensity = abs(signed), clamped to 1-100; 0 -> no constraint emitted
```

このマッピングにより、中心からの距離とマクロゾーンの方向（軸）から極性と強度が一意に決まり、プロンプトメタデータへ注入されます。

> グリッドモデルは `scripts/mtp_grid_generator.py` で可視化しています。生成手順と SVG の詳細はカラーグリッドの可視化で扱います。
