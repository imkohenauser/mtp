---
title: MTP Skill (beta)
description: MTP Skill を追加して最初の /mtp コマンドを実行し、スライダー、グリッド座標、プリセット、複数指定、中立値、無効入力までの入力仕様をまとめて参照できます。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp.png
lastUpdated: true
---

MTP Skill は、`/mtp` コマンドで LLM の出力を方向づける **Agent Skill（エージェントスキル）** です。

長い自然言語の振る舞い指示をプロンプト本文に足す代わりに、`power:70`、`J:4`、`maverick` のような短い指定を、トーン、構造、探索の深さを整える制約へ変換します。

- [MTP Skill zip をダウンロード](/downloads/mtp-skill.zip)
- [インストール手順](/ja/skills/)

---

## 最初に試すコマンド

MTP Skill を追加した後、まず次のいずれかを試してください。

```text
/mtp power:70
この文章を短く要約してください。
```

```text
/mtp focus:70
この仕様変更の重要な影響を整理してください。
```

```text
/mtp maverick
この企画の可能性を広げてください。
```

## 入力形式

| 形式 | 例 | 用途 |
| --- | --- | --- |
| スライダー | `/mtp power:70` | 傾向と強度を直接指定します |
| グリッド | `/mtp J:4` | 19×19 の MTP グリッド上の座標で指定します |
| プリセット | `/mtp maverick` | 複数座標の組み合わせを名前で呼び出します |

三つの入力形式は、いずれも最終的に MTP の軸、極性、強度へ解決されます。  
以降のセクションで、各入力形式の詳細を説明します。

## 基本形式

```text
/mtp <arguments>
<prompt>
```

`/mtp` は、メッセージの先頭、中間、末尾のいずれにも書けます。

```text
/mtp power:70
この文章を要約してください。
```

```text
この文章を要約してください。 /mtp power:70
```

同じメッセージに複数の `/mtp` セグメントがある場合は、引数が書かれた順にまとめられ、`/mtp <arguments>` 部分はプロンプト本文から取り除かれます。

## ノード名

MTP の各軸には、Side A と Side B のノードがあります。  
正の値は Side A を有効にし、負の値は反対側を有効にします。

| 軸 | Side A | Side B |
| --- | --- | --- |
| Yellow | `open` | `still` |
| Red | `power` | `void` |
| Magenta | `return` | `surge` |
| Green | `grow` | `wither` |
| Transparent | `helix` | `collapse` |
| White | `focus` | `haze` |
| Cyan | `enter` | `drift` |
| Blue | `flow` | `abyss` |
| Purple | `close` | `fade` |

各ノードの概念的な説明は [ノードリファレンス](/ja/foundational/node-reference/) を参照してください。

## スライダー

```text
/mtp <node>:<intensity>
```

`<intensity>` は `0` から `100` の値です。

```text
/mtp power:70
/mtp focus:30
/mtp flow:50
```

負の値は、同じ軸の反対側として解釈されます。

```text
/mtp power:-70
```

軸の色名でも指定できます。  
色名を使う場合、正の値は Side A、負の値は Side B を有効にします。

```text
/mtp yellow:70
/mtp yellow:-70
```

Yellow 軸では、`yellow:70` は `open:70` と同じ扱いで、`yellow:-70` は `still:70` と同じ扱いです。

## グリッド

```text
/mtp <column>:<row>
```

MTP のグリッドは 19×19 です。

- 列: `A` から `S`
- 行: `1` から `19`
- 中心: `J:10`

```text
/mtp J:4
/mtp D:16
/mtp A:1
```

ハイフン形式も使えます。

```text
/mtp G-10
```

コンパイラは、座標から軸、極性、強度を計算します。  
`J:10` は中立中心であり、アクティブな制約を生成しません。

座標モデルの詳細は [グリッドと座標系](/ja/foundational/grid-and-coordinate-system/) を参照してください。

## プリセット

プリセットは、パース前に定義済みの MTP トークンへ展開されます。

| プリセット | 展開 |
| --- | --- |
| `synthesizer` | `D:16 A:1` |
| `strategist` | `P:16 P:4` |
| `maverick` | `D:4 A:19` |
| `concierge` | `J:13 D:10` |

```text
/mtp synthesizer
要点を整理してください。
```

プリセット定義は `skills/mtp/references/presets.yaml` で管理されています。

## 複数指定

異なる軸は組み合わせられます。

```text
/mtp open:30 flow:30
この原稿を読みやすく調整してください。
```

基本形式と同様、複数の `/mtp` セグメントは書いた順にまとめられます。

```text
この文章を要約してください。 /mtp power:70 /mtp haze:30
```

## 同一軸の競合

同じ軸を複数回指定した場合は、プリセット展開後の最後のトークンが優先されます。

```text
/mtp power:70 void:30
```

この例では、どちらも Red 軸を指すため、Red 軸では `void:30` が有効です。

## 中立値

次の入力は有効ですが、アクティブな制約を生成しません。

```text
/mtp power:0
/mtp yellow:0
/mtp J:10
```

## 無効な入力

無効なトークンは無視されます。

```text
/mtp foobar:20
/mtp haze:xx
/mtp G:10foo
```

実行環境によっては、実行ログに警告が表示される場合があります。

## ヘルプコマンド

ホストがコマンド出力を表示する場合、次のヘルプコマンドを利用できます。

```text
/mtp help
/mtp help sliders
/mtp help grid
/mtp help presets
/mtp list
/mtp list presets
```

## 実装資料

詳しい例とコンパイラ確認コマンドは、GitHub の [`skills/mtp/USAGE.md`](https://github.com/imkohenauser/mtp/blob/main/skills/mtp/USAGE.md) を参照してください。

## 次に読む

- [インストール](/ja/skills/): ZIP または CLI から MTP Skill を追加します。
- [カスタマイズ](/ja/skills/mtp/customize/): ノード定義とプリセットを編集し、独自の挙動へ調整します。
- [MTP の概要](/ja/foundational/overview/): MTP の基本用語と考え方を説明します。
- [比較](/ja/comparisons/): MTP Skill 適用時の出力比較を確認できます。

## ベータ版について

MTP Skill はベータ版です。基本的な `/mtp <arguments>` の入力形式は利用できますが、ノード定義と制約表現は比較テストを通じて更新される可能性があります。

比較結果を厳密に記録する場合は、MTP Skill のバージョン、モデル名、プロンプト、`/mtp` 引数を合わせて保存してください。

## ライセンス

MIT License
