---
title: MTP Skill (beta)
description: MTP Skill のインストール方法、/mtp コマンドの書き方、スライダー、グリッド、プリセットの解釈を説明します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp.png
---

MTP Skill は、MTP (Mapping the Prompt) フレームワークを用いた **Agent Skills（エージェント スキル）** です。インストールの後、`/mtp` スラッシュコマンドに引数を指定して使います。引数（`<args>`）には、「スライダー：強度」と「グリッド：座標」の 2 つの指定方法があります。さらに、グリッド座標の組み合わせをショートカットとしてまとめた「プリセット」も用意されており、合わせて 3 種類の指定方法が使えます。これらの引数は、モデル出力のトーンや構造を整える**制約**として解釈されます。「スライダー」と「グリッド」はいずれも、MTP フレームワーク上の「ノード」という単位として定義されています。フレームワーク全体の考え方や用語は [概要](/ja/foundational/overview/) で扱います。

このページでは、MTP Skill のインストール、コマンドの書き方、`/mtp <args>` がどう解釈されるかを整理します。

> [!NOTE]
> MTP はモデル内部の仕組みを操作するものではありません。`/mtp <args>` の効果はベースモデルやタスクによって変動します。

---

## インストール

MTP Skill は Agent Skills に対応した Skill です。通常、Skills は、IDE や CLI などの開発者向けツールから利用します。ただし現時点では、Claude.ai のカスタマイズ設定から、ZIP 圧縮した Skill をアップロードすることで、Claude（Web 版）や iOS アプリからも利用できます。MTP リポジトリの `skills/mtp` ディレクトリを ZIP 圧縮してアップロードすることで、MTP Skill を利用できます。

### CLI からの追加手順

このページでは、CLI からインストールする手順を中心に扱います。

#### GitHub CLI (`gh`)

```bash
gh skill install imkohenauser/mtp skills/mtp
```

[GitHub CLI `gh skill` ドキュメント](https://cli.github.com/manual/gh_skill) ↗

#### Vercel Skills CLI (`npx skills`)

```bash
npx skills add imkohenauser/mtp --skill mtp
```

[Vercel Skills CLI ドキュメント](https://skills.sh/docs/cli) ↗

---

## 使い方

`/mtp` は、メッセージの先頭・中間・末尾、独立した行のいずれに書いても解釈されます。同じメッセージに複数書いた場合は、書いた順にまとめて解釈され、`/mtp` の行は本文（プロンプト）から取り除かれます。

たとえば、次の 2 つの書き方は、`/mtp` の位置が違うだけで、コンパイラが生成する制約は同じです。

```markdown
/mtp power:100 ドキュメントの内容を要約してください
```

```markdown
ドキュメントの内容を要約してください /mtp power:100
```

ただし、モデルが制約とプロンプトをどう優先するかはモデル依存で、書く位置によって出力に多少の差が出ることがあります。

### 入力の種別

3 種類の指定方法は、それぞれ次のパターンで書きます。

| 種別          | パターン                                       | 例                                |
| ----------- | ------------------------------------------ | -------------------------------- |
| **スライダー**  | `node:intensity`（強度は 0 – 100）          | `power:100`、`void:80`、`grow:50`  |
| **グリッド**    | `列:行` または `列-行`（19×19 グリッド、列 A–S × 行 1–19）          | `J:4`, `J:1`, `F:10`              |
| **プリセット**  | あらかじめ定義された座標の組み合わせを、名前で呼び出す             | `strategist`、`synthesizer`、`maverick`、`concierge`（4 種類） |

ノード名のほか、**軸の色名**で書くこともできます（例: `yellow:70` は `open:70` と同じ対応）。負の強度はその軸の Side B のノードに解決されます（例: `yellow:-70` は `still:70` と同じ扱い）。これらの例は `skills/mtp/USAGE.md` にあります。

### 書き方の例

ここまで紹介した 3 種類の指定方法は、単独でも組み合わせても使えます。代表的なパターンを抜粋します。

**スライダー**

```markdown
/mtp power:100 ドキュメントの内容を要約してください
```

スライダー `power` を強度 `100` で指定しています。この例では、結論先行で断定的な構造の出力に寄ります。

**グリッド**

```markdown
/mtp J:4 ドキュメントの内容を要約してください
```

19×19 グリッド上の 1 点を指定します。位置から軸が決まり、中心からの距離で強度と極性が決まります。（`J:4` は `power:100` とコンパイル結果が同じです。）

**プリセット**

```markdown
/mtp strategist ドキュメントの内容を要約してください
```

`strategist` は、あらかじめ定義された座標の組み合わせに展開されてから解釈されます（プリセットの定義は `references/presets.yaml`）。

**複数グリッドの指定**

```markdown
/mtp D:16 A:1 ドキュメントの内容を要約してください
```

複数のグリッド座標を並べて指定すると、それぞれが順に解釈されます。（`D:16 A:1` は `synthesizer` プリセットが展開するトークン列と同じで、コンパイル結果も同じです。）

**同一軸の上書き（last-token-wins）**

```markdown
/mtp power:70 void:30 ドキュメントの内容を要約してください
```

`power` と `void` は同じ軸（Red 属性）を指します。同じ軸に対して複数のトークンを書いた場合、後に書いた方が採用されます（この例では `void:30` が有効）。

無効トークン、中立グリッド、プリセットに続く上書きなど、その他の挙動は `skills/mtp/USAGE.md` の各セクションを参照してください。

---

## 出力比較

MTP Skill を適用すると出力がどのように変わるかは、比較ページで確認できます。「テキスト生成」と「画像生成」の比較を以下にまとめています。

[「比較」ページへ](/ja/comparisons/) →

---

## License

MIT