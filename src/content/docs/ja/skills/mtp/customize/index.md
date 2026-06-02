---
title: MTP Skill のカスタマイズ
description: ノード Markdown、プリセット定義、コンパイラ出力の確認を通じて MTP Skill をカスタマイズする方法を説明します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp_customize.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp_customize.png
lastUpdated: true
---

このページは、MTP Skill の挙動をカスタマイズしたい開発者向けの資料です。通常の利用では、これらのファイルを編集しなくても `/mtp` を利用できます。

## 対象ファイル

```text
skills/mtp/nodes/*
skills/mtp/references/presets.yaml
skills/mtp/scripts/mtp_compiler.py
```

ノード定義とプリセットは、コンパイラが読むソースです。これらを編集すると、MTP Skill が出力する制約が変わります。

## ノード定義

各軸は `skills/mtp/nodes/` 配下の Markdown ファイルで定義されています。これらのファイルは説明資料であるだけでなく、コンパイラが読み取る制約ソースです。

ファイル先頭には、単純な frontmatter を置きます。

```yaml
---
axis: red
node_positive: power
node_negative: void
description: "Axis of force and void. Controls whether to push output and assert strongly or strip it back to create margin."
---
```

必須キー:

- `axis`
- `node_positive`
- `node_negative`

推奨キー:

- `description`

frontmatter は単純な形式にしてください。1 行につき `key: value` を 1 つだけ書きます。リスト、ネストした YAML、複数行の値は使わないでください。

## 本文構造

コンパイラは、次の見出し構造を前提にしています。

```md
## Side A

### Low

- ...

### Mid

- ...

### High

- ...

## Side B

### Low

- ...

### Mid

- ...

### High

- ...
```

tier の抽出は累積されます。

| 強度 | 抽出される tier |
| --- | --- |
| `1-30` | Low |
| `31-70` | Low + Mid |
| `71-100` | Low + Mid + High |

上位 tier は、下位 tier を強めるか補足する内容にしてください。下位 tier と矛盾する制約は避けてください。

## Preset

Preset は `skills/mtp/references/presets.yaml` で定義します。

```yaml
synthesizer: "D:16 A:1"
strategist: "P:16 P:4"
maverick: "D:4 A:19"
concierge: "J:13 D:10"
```

各値は、空白区切りの MTP トークン列です。Slider と Grid を組み合わせることもできます。Preset はパース前に展開されるため、同一軸の競合解決は展開後の最後のトークン順に従います。

## 検証

Skill ルートからコンパイラを実行します。

```bash
python3 scripts/mtp_compiler.py --args "power:100"
python3 scripts/mtp_compiler.py --args "D:16 A:1"
python3 scripts/mtp_compiler.py --args "synthesizer yellow:30"
```

コンパイラは stdout に制約 XML を出力します。警告と短い要約は stderr に出力されます。

詳しいテストケースは GitHub の [`skills/mtp/USAGE.md`](https://github.com/imkohenauser/mtp/blob/main/skills/mtp/USAGE.md) を参照してください。
