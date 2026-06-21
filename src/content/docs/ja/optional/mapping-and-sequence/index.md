---
title: 分類と順序
description: MTP を概念マッピングのグリッドや、Side A / Side B の順序列として読む補足的な見方を説明します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_optional_mapping-and-sequence.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_optional_mapping-and-sequence.png
lastUpdated: true
---

> [!NOTE]
> 分類と順序に関する補足資料です。
>
> 現行の MTP スキルはテキストベースで、`/mtp <args>` によるスライダー、座標指定、プリセットから利用します。

MTP は、プロンプトをステアリング（方向づける）手段としてだけでなく、**概念を 3×3 のグリッドに配置する枠組み**として、また**順序列**として読むこともできます。  
これは、MTP のノード配置が、色や方位に関するイメージを手がかりに設計されているためです。

このページでは、次の 2 つの補足的な読み方を扱います。

1. **グリッドへマッピング**：キャラクター、アーキタイプ、プロンプト傾向、出力傾向などを MTP ノード上に配置する読み方
2. **シーケンス（Z-order）**：入力と出力をフレームとして、その間の 18 ノード極を線形アークとして読む読み方

---

## グリッド上の概念マッピング

MTP のグリッドは、他の概念体系を配置するための枠組みとして利用できます。  
たとえば、次のようなマッピングが考えられます。

### 参照用の基本グリッド

```text
3×3 色マップ（macro zones）:
+-------------+-------------+-------------+
| Yellow      | Red         | Magenta     |
+-------------+-------------+-------------+
| Green       | Transparent | White       |
+-------------+-------------+-------------+
| Cyan        | Blue        | Purple      |
+-------------+-------------+-------------+

ノードマップ（Side A）:
+-------------+-------------+-------------+
| Open        | Power       | Return      |
+-------------+-------------+-------------+
| Grow        | Helix       | Focus       |
+-------------+-------------+-------------+
| Enter       | Flow        | Close       |
+-------------+-------------+-------------+

ノードマップ（Side B）:
+-------------+-------------+-------------+
| Still       | Void        | Surge       |
+-------------+-------------+-------------+
| Wither      | Collapse    | Haze        |
+-------------+-------------+-------------+
| Drift       | Abyss       | Fade        |
+-------------+-------------+-------------+
```

### 例: キャラクターのマッピング

キャラクター体系をグリッドに直感的に配置できます。  
ひとつの例として、ピクサーの映画作品「[インサイド・ヘッド](https://ja.wikipedia.org/wiki/%E3%82%A4%E3%83%B3%E3%82%B5%E3%82%A4%E3%83%89%E3%83%BB%E3%83%98%E3%83%83%E3%83%89)（原題：Inside Out）」は感情機能を中心に構成された作品なので、MTP グリッドに対応づけて読むことができます。

キャラクターを固定した分類として読むのではなく、文脈に応じて配置を入れ替えてよい読み方です。

**Side A** （インサイド・ヘッドより）:

```text
| ヨロコビ     | イカリ       | ヨロコビ      |
| ムカムカ     | ライリー     | ビビリ        |
| ヨロコビ     | カナシミ     | ヨロコビ      |
```

ヨロコビは、ライリーの経験をめぐる統合的な動きとして Open, Return, Enter, Close に配置されます。  
MTP の四隅は、可能性を開く、経験を意味へ戻す、状況へ入る、出来事を完了へ運ぶ、という閾値的な運動として読めます。

『Inside Out』では、ヨロコビが内面世界の物語的な連続性と感情的な生きやすさを保つため、必要に応じて役割を変えます。  
この対応は性格特徴の一致を意味せず、ヨロコビを Side A 的な運動として読む配置です。

対応づけの例:

| | ノード | キャラクター | キャラクター説明 |
| --- | --- | --- | --- |
| <div class="dot-group" role="img" aria-label="Open、Return、Enter、Close（MTP グリッドの四隅ノード）"><div class="dot-sm bg-open" aria-hidden="true"></div><div class="dot-sm bg-return" aria-hidden="true"></div><div class="dot-sm bg-enter" aria-hidden="true"></div><div class="dot-sm bg-close" aria-hidden="true"></div></div> | `open`, `return`, `enter`, `close` | ヨロコビ   | ヨロコビは可能性を開き、体験を希望で捉え直し、明るい完了へ運んでいく。 |
| <div class="dot-sm bg-power" aria-label="red"></div>         | `power` | イカリ    | 怒りと主張が、衝動的だが推進力の強い行動を駆動する。 |
| <div class="dot-sm bg-grow" aria-label="green"></div>        | `grow`  | ムカムカ   | 嫌悪と選別が、快・不快の境界と自己防衛を整える。 |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | `helix` | ライリー   | 複数の感情が通り抜ける、本人を司る中立的な中枢。 |
| <div class="dot-sm bg-focus" aria-label="white"></div>       | `focus` | ビビリ    | 不安と警戒が、危険や不確実性へ注意を向ける。 |
| <div class="dot-sm bg-flow" aria-label="blue"></div>         | `flow`  | カナシミ   | 悲しみと受容が、感情の流れと意味づけを深める。 |


**Side B** （インサイド・ヘッド2より）:

```text
| ブルーフィー       | ランス・スラッシュブレード  | シンパイ           |
| ハズカシ          | ライリー                | ダリィ             |
| イイナー          | クライヒミツ             | ナツカシ           |
```

対応づけの例:

| | ノード | キャラクター | キャラクター説明 |
| --- | --- | --- | --- |
| <div class="dot-sm bg-still" aria-label="yellow"></div>         | `still`   | ブルーフィー         | 幼少期の空想キャラが、現実の動きを止めて慰めに置き換える。 |
| <div class="dot-sm bg-void" aria-label="red"></div>             | `void`    | ランス・スラッシュブレード | 英雄的ファンタジーが、使えない力の空洞として固定化する。 |
| <div class="dot-sm bg-surge" aria-label="magenta"></div>        | `surge`   | シンパイ           | 不安が最高点に達し、思考と身体反応を過剰に高める。 |
| <div class="dot-sm bg-wither" aria-label="green"></div>         | `wither`  | ハズカシ           | 恥が境界防衛を弱め、自己意識のもとで身を縮こまらせる。 |
| <div class="dot-sm bg-collapse" aria-label="transparent"></div> | `collapse` | ライリー           | 中立の中枢が過負荷で崩れ、感情の統合が一時的に破綻する。 |
| <div class="dot-sm bg-haze" aria-label="white"></div>           | `haze`    | ダリィ            | 無関心と皮肉が警戒を拡散し、関心を曇らせる。 |
| <div class="dot-sm bg-drift" aria-label="cyan"></div>           | `drift`   | イイナー           | 渇望が方向を失い、他人のものへの未充足を繰り返す。 |
| <div class="dot-sm bg-abyss" aria-label="blue"></div>           | `abyss`   | クライヒミツ         | 封じた秘密が沈み、自己理解の底へ引きずり込む。 |
| <div class="dot-sm bg-fade" aria-label="purple"></div>          | `fade`    | ナツカシ           | 閉じた後も未練が薄く残り、過去へ憧憬を寄せる。 |

各マスは、同じ座標の Side A ノードを**反転極**として読むこともできます（たとえば Open の楽観が Still の停止へ、Power の推進が Void の空洞化へ）。

---

## 順序列としての読み

MTP は本来、グリッド位置、極性、強度によって定義されますが、ノードは順序列として読むこともできます。  
3×3 グリッドを左上から右下へ、行方向のジグザグ（Z 字）でたどると、次の色の並びになります。

```text
Yellow → Red → Magenta → Green → Transparent → White → Cyan → Blue → Purple
```

### 20 ノードのシーケンス: 1+9+9+1

これをノードに置き換えます。  
**9 つの Side A ノード**と**9 つの Side B ノード**に、**Start（Input）** と **End（Output）** を加え、線形アークとして並べます。

```text
 1. Start (Input)          ← はじまり（入力）
 2. Open                   ┐
 3. Power                  │
 4. Return                 │
 5. Grow                   │
 6. Helix                  │  Side A: 陽性
 7. Focus                  │
 8. Enter                  │
 9. Flow                   │
10. Close                  ┘
11. Still                  ┐
12. Void                   │
13. Surge                  │
14. Wither                 │
15. Collapse               │  Side B: 陰性
16. Haze                   │
17. Drift                  │
18. Abyss                  │
19. Fade                   ┘
20. End (Output)           ← 終わり（出力）
```

この読み方での順序は、[設計上の背景](/ja/optional/design-background/)で説明したグリッドの Z-order に従います。  
**Start** と **End** は、グリッド上のノードではなく、順序で読む際に追加した仮想の枠です。  
これらは順序列の開始と終了を示します。  
Side A と Side B の 18 ノードが、それぞれの意味の枠を構成します。

テキストでは **1+9+9+1** の内訳になります。

- **1** : Start (Input)
- **9** : Side A の 9 つのノード
- **9** : Side B の 9 つのノード
- **1** : End (Output)

全体としては、このシーケンスは二部構成のアークを形成します。

- **Side A**: 拡張、エネルギー、展開、到達
- **Side B**: 反転、枯渇、解体、減衰

---

## 分類と順序の汎用性

こうした読み方は、次のような場面で役立ちます。

- キャラクター配置から **MTP Skill** の利用イメージを掴む
- 20 ノードのシーケンスに、20 曲の AI の選曲の音楽プレイリストを作成する
