---
title: MTP Skill (beta)
description: MTP Skill の効果、beta の位置づけ、インストール方法、/mtp コマンド、スライダー、グリッド、プリセットの解釈を説明します。
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

MTP Skill は、MTP (Mapping the Prompt) フレームワークを `/mtp` コマンドから使うための **Agent Skills（エージェント スキル）** です。

長い自然言語のメタ指示をプロンプト本文に書く代わりに、`power:100`、`J:4`、`synthesizer` のような短い指定を、モデル出力のトーン、構造、探索の深さを整える**制約**へ変換します。引数（`<args>`）には、**スライダー**、**グリッド座標**、**プリセット**の 3 種類があり、どの形式で書いても、最終的には MTP の軸、極性、強度へ解決されます。フレームワーク全体の考え方や用語は [概要](/ja/foundational/overview/) で扱います。

このページでは、MTP Skill を使うと何が変わるのか、`(beta)` の位置付け、インストール方法、コマンドの書き方、`/mtp <args>` の解釈を説明しています。

> [!NOTE]
> MTP はモデル内部の仕組みを操作するものではありません。`/mtp <args>` の効果はベースモデルやタスクによって変動します。また、MTP Skill はノード定義や制約表現を継続的に更新しています。

---

## MTP Skill を使うとどうなるか

MTP Skill を使うと、プロンプト本文とは別のレイヤーで、出力の方向づけを指定できます。たとえば「この記事を要約してください」という同じタスクに対して、`/mtp power:100` を足すと結論先行で強い構造に寄り、`/mtp void:80` を足すと説明を削った最小限の出力に寄ります。

これは、毎回「もっと断定的に」「もっと短く」「可能性を広げて」「焦点を絞って」と自然文で書き足す代わりに、MTP の座標やノード名で制御するための仕組みです。タスクそのものと、出力スタイルの制御を分離できるので、同じプロンプトを保ったまま、出力の違いを比較しやすくなります。また、サブエージェント等のペルソナ制御への応用も期待できます。

MTP では、Power、Flow、Focus、Open などのノードを、意味付けされた「型（トーンやスタイルのまとまり）」として考えることができます。`power:50` や `focus:70` は、その型にどれだけ寄せるかを強度として渡す指定です。単一のノードで出力傾向を切り替えることも、複数のノードを組み合わせて傾向をブレンドすることもできます。

MTP では、これらの型どうしの配置や関係を表すために、色を視覚的な座標体系として利用しています。色そのものに固定的な意味を押しつけるというより、出力傾向を地図上で把握するための手がかりとして扱います。詳細は [設計上の背景](/ja/optional/design-background/) で扱います。

| 指定例 | 出力傾向 |
| --- | --- |
| `/mtp power:100` | 結論先行、断定的、主張が明確な出力 |
| `/mtp void:80` | 簡潔、最小限、説明を抑えた出力 |
| `/mtp open:70` | 可能性や選択肢を広げる出力 |
| `/mtp focus:70` | 対象を絞り、精度や具体性を重視する出力 |
| `/mtp D:16 A:1` | 複数のグリッド座標を組み合わせた出力 |

強さを調整したい場合は、`power:50` や `power:100` のように、ノード名と `:intensity` の強度を組み合わせて指定します。実際の変化は、モデル、タスク、プロンプト本文によって変わります。強度の取り扱いもモデルごとに異なるため、同じ `:intensity` でも出力への出方が変わることがあります。

MTP Skill は出力を完全に固定するものではなく、モデルに渡す制約を「型（意味や概念）」として結びつけ、再利用しやすくするためのレイヤーです。

---

## インストール

MTP Skill は Agent Skill として配布されています。CLI からインストールできるほか、zip 形式の Agent Skills をサポートするツールには、公式 zip をダウンロードしてアップロードできます。

### zip 版のダウンロード

パッケージ済みの最新版 MTP Skill は、次のリンクから zip ファイルとしてダウンロードできます。

[MTP Skill zip をダウンロード](/downloads/mtp-skill.zip) ↓

この zip は、リポジトリ内の `skills/mtp` から生成された `mtp` Skill パッケージです。

<!-- バージョンごとの zip とリリースノートは GitHub Releases を参照してください。

[GitHub Releases で MTP Skill のリリースを見る](https://github.com/imkohenauser/mtp/releases) ↗

MTP Skill のリリースタグは `mtp-vX.Y.Z` 形式です。`v1` は、同じ major 系統を共有する MTP 関連 Skill 群を表す family ラベルです。

リリース情報は JSON としても公開しています。

[`/downloads/release.json`](/downloads/release.json) -->

### CLI からの追加手順

このページでは、CLI からインストールする手順を中心に扱います。

#### GitHub CLI (`gh`)

GitHub CLI の `gh skill` は preview 扱いの機能です。利用している `gh` のバージョンで `gh skill` が有効か確認してください。

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

`/mtp` は、メッセージの先頭・中間・末尾、独立した行のいずれに書いても解釈されます。同じメッセージに複数書いた場合は、書いた順にまとめて解釈され、`/mtp <args>` 部分は本文（プロンプト）から取り除かれます。

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

![/mtp node:intensity によるMTP Slider Argumentsを説明する図。左はSide AとSide Bのノードスライダーを示し、Powerが70に設定されている。右はOpen、Power、Focus、Flow、Close、Surge、Collapse、Fadeなどの方向を、3Dチェビシェフ距離として示している。](/images/pages/mtp-slider-arguments-mtp-node-intensity.png)

**グリッド**

```markdown
/mtp J:4 ドキュメントの内容を要約してください
```

19×19 グリッド上の 1 点を指定します。位置から軸が決まり、中心からの距離で強度と極性が決まります。（`J:4` は `power:100` とコンパイル結果が同じです。）

![/mtp column:row によるMTP Grid Argumentsを説明する図。左は3×3の色グリッドを19×19座標上に単純化して示し、J:4、D:10、P:10、J:16などの例を表示している。右は19×19全体のRGBA値の分布を示している。](/images/pages/mtp-grid-arguments-mtp-column-row.png)

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

## beta について

タイトルの `(beta)` は、MTP Skill と、その核になる `skills/mtp/nodes/*` の記述が、今後も検証と更新の対象であることを示しています。

現在のノード定義は、各色軸と Side A / Side B の振る舞いを Markdown で記述しています。現時点でも `/mtp <args>` の基本的な入力形式、プリセット展開、同一軸の上書き規則は利用できますが、ノードごとの説明や制約表現は、比較テストを重ねながら更新していく予定です。

今後の調整では、直接的なテキスト指示を増やすよりも、各色・各ノードが持つ特徴をより普遍的に表現する方向を重視します。つまり、「この語尾にする」「この形式で書く」といった固定的な命令ではなく、Power、Flow、Focus、Open などの性質が、モデルやタスクをまたいでより安定して伝わる記述へ近づけていきます。

比較結果を厳密に残したい場合は、MTP Skill のバージョン、モデル名、プロンプト、`/mtp <args>` を合わせて記録してください。比較ページでは、この前提でベースラインと MTP Skill 適用後の出力を並べています。

---

## ノード定義のカスタマイズ

MTP Skill の出力傾向は、`skills/mtp/nodes/*` に含まれるノード定義によって調整できます。これらのファイルは単なる説明文ではなく、コンパイラが読み取り、制約として使うソースです。

カスタマイズを希望する方は `skills/mtp/nodes/*` を編集することで、テーマを変えるように MTP Skill の挙動そのものを変えられます。たとえば、同じ `/mtp power:100` でも、`skills/mtp/nodes/RED.md` の Power 側の記述を変更すれば、異なる方向に寄せることができます。

カスタマイズするときは、各ノードファイルの基本構造を保ってください。frontmatter、`## Side A`、`## Side B`、各 Side の `### Low`、`### Mid`、`### High` という見出し構造は、コンパイラが読み取る前提になっています。

---

## 出力比較

MTP Skill を適用すると出力がどのように変わるかは、比較ページで確認できます。「テキスト生成」と「画像生成」の比較を以下にまとめています。

[「比較」ページへ](/ja/comparisons/) →

---

## License

MIT
