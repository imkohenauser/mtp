---
title: MTP Skill コマンド仕様
description: /mtp コマンドのスライダー、グリッド座標、プリセット、複数指定、中立値、無効入力を説明します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp_reference.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp_reference.png
lastUpdated: true
---

このページでは、`/mtp` の公開入力仕様を説明します。  
内部向けの `SKILL.md` を転記するのではなく、利用者が入力を組み立てるために必要な情報を載せています。

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
