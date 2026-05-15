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

プリセットは、解釈前にあらかじめ定義された座標列へ展開されます。現在のプリセットは次の 4 種類です。

| 色 | プリセット | 展開 |
| --- | --- | --- |
| <div class="dot-sm bg-close" aria-label="purple"></div><div class="dot-sm bg-return" aria-label="magenta"></div> | `strategist` | `P:16 P:4` |
| <div class="dot-sm bg-enter" aria-label="cyan"></div><div class="dot-sm bg-still" aria-label="yellow"></div> | `synthesizer` | `D:16 A:1` |
| <div class="dot-sm bg-open" aria-label="yellow"></div><div class="dot-sm bg-drift" aria-label="cyan"></div> | `maverick` | `D:4 A:19` |
| <div class="dot-sm bg-j13" aria-label="blue"></div><div class="dot-sm bg-grow" aria-label="green"></div> | `concierge` | `J:13 D:10` |

定義は `references/presets.yaml` にあります。

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

## 出力比較

以下の例では、基本プロンプトを固定し、`/mtp` 引数だけを変更しています。これはベンチマークではなく、ノードや強度の違いが出力の文体・構成・解釈の踏み込みにどう現れるかを示すための定性的な比較です。

英語版では *Alice’s Adventures in Wonderland* を題材にした短いプロンプトを使い、日本語版では夏目漱石『三四郎』を題材にしています。画像生成の例では、構図を固定し、MTP の強度だけを変えて目の表情の変化を比較しています。

MTP Skill を適用すると出力がどのように変わるかは、比較ページでも確認できます。「テキスト生成」と「画像生成」の比較を以下にまとめています。

[「比較」ページへ](/ja/comparisons/) →

### 強度比較: Power

`power` を高めると、出力はより断定的で解釈的になります。低い強度では一般的な要約に近く、高い強度では、より明示的で主張が強く、編集的な文体になります。

![夏目漱石『三四郎』を題材に、/mtp power の強度を上げたときの出力文体の変化を示す比較画像。](/images/examples/mtp-examples-claude-ai-story-of-sanshiro-power.png)

### 強度比較: Surge

`surge` を高めると、論旨そのものよりもリズムが変化します。出力はより動的で圧縮され、短い拍と強い推進力を持つ文体になります。

![夏目漱石『三四郎』を題材に、/mtp surge の強度を上げたときのリズムと速度感の変化を示す比較画像。](/images/examples/mtp-examples-claude-ai-story-of-sanshiro-surge.png)

### 70% でのノード比較

強度を `70` に固定すると、ノードごとの出力傾向が比較しやすくなります。`open` は入口を広げ、`focus` は説明を安定させ、`void` は前提を削ぎ落とし、`abyss` は解釈の枠組みを暗く深い方向へ寄せます。

![夏目漱石『三四郎』を題材に、複数の MTP ノードを強度70で比較した画像。](/images/examples/mtp-examples-claude-ai-story-of-sanshiro-various.png)

### 複数引数とプリセット

複数の引数は組み合わせて使えます。`maverick` や `concierge` のようなプリセットは、あらかじめ定義された座標パターンをまとめたもので、単一ノードよりも認識しやすい高次の振る舞いを生みます。

![夏目漱石『三四郎』を題材に、複数の MTP 引数とプリセットによる出力の違いを示す比較画像。](/images/examples/mtp-examples-claude-ai-story-of-sanshiro-multiple.png)

### 画像比較: 肖像

同じ引数の考え方は、画像生成プロンプトにも使えます。ここでは `power` を変化させながら肖像の構図を固定し、目と表情の強度に変化が現れるようにしています。

![モーツァルトの肖像を題材に、/mtp power の強度による画像生成結果の変化を示す比較画像。](/images/examples/mtp-examples-gpt-image-2-portrait-of-mozart.png)

### 画像比較: 小さな花束

ここでは花束の題材と用途を固定しながら MTP ノードを変化させ、開き方、密度、剪定、包装、全体のムードに違いが現れるようにしています。

![小さな花束を題材に、MTP 引数による画像生成結果の変化を示す比較画像。](/images/examples/mtp-examples-gpt-image-2-small-bouquet.png)

---

## License

MIT
