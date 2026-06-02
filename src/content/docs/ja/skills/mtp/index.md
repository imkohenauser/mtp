---
title: MTP Skill (beta)
description: MTP Skill を追加し、最初の /mtp コマンドを実行するための導線と、インストール、コマンド仕様、カスタマイズ、出力比較へのリンクをまとめます。
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

MTP Skill は、`/mtp` コマンドで LLM の出力傾向を調整する **Agent Skill（エージェントスキル）** です。

長い自然言語の振る舞い指示をプロンプト本文に足す代わりに、`power:70`、`J:4`、`maverick` のような短い指定を、トーン、構造、探索深度を整える制約へ変換します。

- [MTP Skill zip をダウンロード](/downloads/mtp-skill.zip)
- [インストール手順](/ja/skills/mtp/install/)
- [コマンド仕様](/ja/skills/mtp/reference/)

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

## 入力の種類

| 種類 | 例 | 用途 |
| --- | --- | --- |
| Slider | `/mtp power:70` | 傾向と強度を直接指定します |
| Grid | `/mtp J:4` | 19x19 の MTP グリッド上の座標で指定します |
| Preset | `/mtp maverick` | 複数座標の組み合わせを名前で呼び出します |

3 種類の入力は、いずれも最終的に MTP の軸、極性、強度へ解決されます。詳しい挙動は [コマンド仕様](/ja/skills/mtp/reference/) で説明します。

## 次に読む

- [インストール](/ja/skills/mtp/install/): ZIP または CLI から MTP Skill を追加します。
- [コマンド仕様](/ja/skills/mtp/reference/): スライダー、グリッド座標、プリセット、複数指定、中立値、無効入力を説明します。
- [カスタマイズ](/ja/skills/mtp/customize/): ノード定義とプリセットを編集し、独自の挙動へ調整します。
- [MTP の概要](/ja/foundational/overview/): MTP の基本用語と考え方を説明します。
- [比較](/ja/comparisons/): MTP Skill 適用時の出力比較を確認できます。

## beta について

MTP Skill は beta 版です。基本的な `/mtp <arguments>` の入力形式は利用できますが、ノード定義と制約表現は比較テストを通じて更新される可能性があります。

比較結果を厳密に記録する場合は、MTP Skill のバージョン、モデル名、プロンプト、`/mtp` 引数を合わせて保存してください。

## License

MIT License
