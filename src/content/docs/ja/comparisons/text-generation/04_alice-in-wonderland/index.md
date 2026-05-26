---
title: "文学課題: 『不思議の国のアリス』の紹介"
description: 『不思議の国のアリス』紹介課題で、MTP Skill による出力構成や提案内容の違いを比較します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_text-generation_04_alice-in-wonderland.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_text-generation_04_alice-in-wonderland.png
lastUpdated: true
---

**プロンプト**

```markdown
/mtp <args> 
ルイス・キャロルの「不思議の国のアリス」を、読んでみたくなるように紹介してください。
```

**適用範囲**
- ベースライン： 1 件（MTP Skill を適用しない）
- スライダー `<node:100>`： 18 件
- スライダー `<node:50>`： 18 件
- グリッド `<column:row>`： 17 件
- プリセット `<preset>`： 4 件

**モデル**
- ChatGPT 5.5 on Codex (macOS app)
- Gemini 3.5 Flash on Antigravity 2.0 (macOS app)
- Composer 2.5 on Cursor 3.5 (macOS app)
- Sonnet 4.6 on Claude.ai (iOS app)
- Manus 1.6 Lite on Manus.im (iOS app)

---

## この比較の読み方

このページは、単なる出力一覧ではありません。同一の文学紹介課題に対して、MTP Skill が出力の方向性、構成、語り口をどのように変えるかを比較するページです。

英語版と日本語版は、翻訳関係ではありません。英語ページでは英語プロンプト、日本語ページでは日本語プロンプトを用い、それぞれの言語で独立にテストしています。そのため、英語版と日本語版の文面対応ではなく、各言語内でベースラインからどのように変化したかを中心に読む構成です。

ベースラインは、MTP Skill を適用しない場合の各モデルの自然な出力傾向を示します。スライダー、グリッド、プリセットを指定した出力では、そのモデル固有の文体の上に、MTP Skill による制御方向が重なります。

## ベースラインから何が変わるか

以下は、この比較で読み取りやすい代表的な MTP 指定です。個別の出力では、ベースラインとの差分と、同じ指定に対するモデル間の違いを合わせて確認できます。

| MTP argument | 主な効果 | 比較する点 |
| ---------------------- | ---------------- | ---------------------- |
| `power:50 / power:100` | 強度、断定、読者への圧を高める | ベースラインとの差、50 と 100 の強度差 |
| `J:16` | 流れ、没入、連続叙述を強める | ベースラインより物語に滑り込むか |
| `D:10` | 背景、理由、応用、解釈へ展開する | ベースラインより階層化・多層化するか |
| `concierge` | 案内性と展開性を合成する | 読者を作品へ導くガイドになっているか |

## 実行環境と Skill の実行

この比較では、macOS 上の開発者向けエージェント環境に加えて、iOS アプリ上のモバイル環境でもテストを行っています。各環境では `/mtp` をスラッシュコマンドとして呼び出し、MTP compiler が実行されたことをログで確認しています。

| Model | Host | Environment | Skill execution |
| ---------------- | ----------- | ----------- | --------------------------------------------------------------------- |
| ChatGPT 5.5 | Codex | macOS app | CLI インストールした MTP Skill をスラッシュコマンドから呼び出し、ログで compiler 実行を確認 |
| Gemini 3.5 Flash | Antigravity | macOS app | CLI インストールした MTP Skill をスラッシュコマンドから呼び出し、ログで compiler 実行を確認 |
| Composer 2.5 | Cursor | macOS app | CLI インストールした MTP Skill をスラッシュコマンドから呼び出し、ログで compiler 実行を確認 |
| Sonnet 4.6 | Claude.ai | iOS app | ZIP インストールした MTP Skill をスラッシュコマンドから呼び出し、ログで compiler 実行を確認 |
| Manus 1.6 Lite | Manus.im | iOS app | ZIP インストールした MTP Skill をスラッシュコマンドから呼び出し、タスクログで compiler 実行を確認 |

macOS 環境では CLI インストールされた Skill、iOS 環境では ZIP インストールされた Skill を使用しています。いずれの環境でも、`/mtp` 引数を単なる文字列として扱うのではなく、Skill ワークフローでコンパイルしたうえで最終出力を生成しています。これは、MTP が開発者向けツールとモバイル AI アプリの双方で利用できる、可搬性のある出力調整レイヤーとして機能することを示しています。

## 言語別テストについて

英語版と日本語版は、同じ比較設計を持っています。どちらも、ベースライン、スライダー `:100`、スライダー `:50`、グリッド、プリセットを同じ範囲で比較し、同じ 5 モデルを対象にしています。

ただし、英語出力と日本語出力が同じ内容になるかを確認するための翻訳比較ではありません。まず英語版または日本語版の中でベースラインと MTP 指定後の変化を比較し、次にもう一方の言語でも同じ指定の変化を見ることで、同じ MTP 指定が英語と日本語で似た役割を果たしているかを確認できます。

## モデル横断の一貫性

MTP Skill は、モデル固有の文体を消すものではありません。Gemini は構造化しやすく、Sonnet は文学批評的に深く、Composer は編集記事風に整い、Manus は一般向けの紹介文に寄る傾向があります。ただし、同じ MTP 指定を与えると、モデル差を残したまま、出力の方向性は一定の一貫性をもって変化します。

## 代表的な観察

`power` は、読者への説得圧を上げます。`power:50` では強めの推薦に寄り、`power:100` では命令、宣言、反抗の語彙が増えます。

`J:16` は、出力を流れる叙述に寄せます。見出しや分析よりも、読者を物語に入れる導線が強くなります。`J:16` は、ノード指定の `flow:100` と同じ解釈です。

`D:10` は、出力を成長させます。背景、理由、応用、次の読書導線が増え、単なる紹介文から多層的な解説へ変わります。

`concierge` は、案内性と展開性を合成します。プリセットとしては `J:13 D:10` に展開され、解釈としては `flow:50 grow:100` に近い指定です。ほどよく流れる叙述に、強い展開性が重なるため、読者を作品へ導くガイドのような出力になりやすい指定です。

---

## 出力比較一覧

テスト環境では、特別なユーザー設定や、横断的なチャット会話の記憶を含まない状態で、それぞれ、新しいエージェントチャットセッションを開始してテストを行った結果です。

<!-- AUTO-GENERATED: model-output-indexes:start -->
### モデル別統合出力

各モデルの出力部分だけを統合した、AI 分析用ページです。

| ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| --- | --- | --- | --- | --- |
| [統合出力](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/) | [統合出力](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/) | [統合出力](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/) | [統合出力](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/) | [統合出力](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/) |
<!-- AUTO-GENERATED: model-output-indexes:end -->

### ベースライン

MTP Skill を適用せずに、プロンプトをそのまま入力した場合の出力です。

| ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| [baseline](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/baseline/) | [baseline](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/baseline/) | [baseline](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/baseline/) | [baseline](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/baseline/) | [baseline](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/baseline/) |

---

### スライダー（:100）

MTP Skill のスライダー（`/mtp <node:100>`）を指定した場合の出力です。

#### Side A ノード

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-sm bg-open" aria-label="yellow"></div> | [open:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/open-100/) | [open:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/open-100/) | [open:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/open-100/) | [open:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/open-100/) | [open:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/open-100/) |
| <div class="dot-sm bg-power" aria-label="red"></div> | [power:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/power-100/) | [power:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/power-100/) | [power:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/power-100/) | [power:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/power-100/) | [power:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/power-100/) |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | [return:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/return-100/) | [return:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/return-100/) | [return:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/return-100/) | [return:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/return-100/) | [return:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/return-100/) |
| <div class="dot-sm bg-grow" aria-label="green"></div> | [grow:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/grow-100/) | [grow:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/grow-100/) | [grow:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/grow-100/) | [grow:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/grow-100/) | [grow:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/grow-100/) |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | [helix:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/helix-100/) | [helix:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/helix-100/) | [helix:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/helix-100/) | [helix:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/helix-100/) | [helix:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/helix-100/) |
| <div class="dot-sm bg-focus" aria-label="white"></div> | [focus:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/focus-100/) | [focus:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/focus-100/) | [focus:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/focus-100/) | [focus:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/focus-100/) | [focus:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/focus-100/) |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | [enter:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/enter-100/) | [enter:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/enter-100/) | [enter:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/enter-100/) | [enter:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/enter-100/) | [enter:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/enter-100/) |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | [flow:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/flow-100/) | [flow:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/flow-100/) | [flow:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/flow-100/) | [flow:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/flow-100/) | [flow:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/flow-100/) |
| <div class="dot-sm bg-close" aria-label="purple"></div> | [close:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/close-100/) | [close:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/close-100/) | [close:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/close-100/) | [close:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/close-100/) | [close:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/close-100/) |

#### Side B ノード

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-sm bg-still" aria-label="yellow"></div> | [still:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/still-100/) | [still:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/still-100/) | [still:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/still-100/) | [still:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/still-100/) | [still:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/still-100/) |
| <div class="dot-sm bg-void" aria-label="red"></div> | [void:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/void-100/) | [void:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/void-100/) | [void:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/void-100/) | [void:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/void-100/) | [void:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/void-100/) |
| <div class="dot-sm bg-surge" aria-label="magenta"></div> | [surge:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/surge-100/) | [surge:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/surge-100/) | [surge:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/surge-100/) | [surge:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/surge-100/) | [surge:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/surge-100/) |
| <div class="dot-sm bg-wither" aria-label="green"></div> | [wither:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/wither-100/) | [wither:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/wither-100/) | [wither:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/wither-100/) | [wither:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/wither-100/) | [wither:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/wither-100/) |
| <div class="dot-sm bg-collapse" aria-label="transparent"></div> | [collapse:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/collapse-100/) | [collapse:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/collapse-100/) | [collapse:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/collapse-100/) | [collapse:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/collapse-100/) | [collapse:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/collapse-100/) |
| <div class="dot-sm bg-haze" aria-label="white"></div> | [haze:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/haze-100/) | [haze:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/haze-100/) | [haze:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/haze-100/) | [haze:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/haze-100/) | [haze:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/haze-100/) |
| <div class="dot-sm bg-drift" aria-label="cyan"></div> | [drift:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/drift-100/) | [drift:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/drift-100/) | [drift:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/drift-100/) | [drift:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/drift-100/) | [drift:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/drift-100/) |
| <div class="dot-sm bg-abyss" aria-label="blue"></div> | [abyss:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/abyss-100/) | [abyss:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/abyss-100/) | [abyss:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/abyss-100/) | [abyss:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/abyss-100/) | [abyss:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/abyss-100/) |
| <div class="dot-sm bg-fade" aria-label="purple"></div> | [fade:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/fade-100/) | [fade:100](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/fade-100/) | [fade:100](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/fade-100/) | [fade:100](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/fade-100/) | [fade:100](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/fade-100/) |

---

### スライダー（:50）

MTP Skill のスライダー（`/mtp <node:50>`）を指定した場合の出力です。

#### Side A ノード

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-sm bg-open opacity-50" aria-label="yellow"></div> | [open:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/open-50/) | [open:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/open-50/) | [open:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/open-50/) | [open:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/open-50/) | [open:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/open-50/) |
| <div class="dot-sm bg-power opacity-50" aria-label="red"></div> | [power:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/power-50/) | [power:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/power-50/) | [power:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/power-50/) | [power:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/power-50/) | [power:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/power-50/) |
| <div class="dot-sm bg-return opacity-50" aria-label="magenta"></div> | [return:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/return-50/) | [return:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/return-50/) | [return:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/return-50/) | [return:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/return-50/) | [return:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/return-50/) |
| <div class="dot-sm bg-grow opacity-50" aria-label="green"></div> | [grow:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/grow-50/) | [grow:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/grow-50/) | [grow:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/grow-50/) | [grow:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/grow-50/) | [grow:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/grow-50/) |
| <div class="dot-sm bg-helix opacity-50" aria-label="transparent"></div> | [helix:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/helix-50/) | [helix:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/helix-50/) | [helix:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/helix-50/) | [helix:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/helix-50/) | [helix:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/helix-50/) |
| <div class="dot-sm bg-focus opacity-50" aria-label="white"></div> | [focus:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/focus-50/) | [focus:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/focus-50/) | [focus:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/focus-50/) | [focus:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/focus-50/) | [focus:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/focus-50/) |
| <div class="dot-sm bg-enter opacity-50" aria-label="cyan"></div> | [enter:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/enter-50/) | [enter:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/enter-50/) | [enter:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/enter-50/) | [enter:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/enter-50/) | [enter:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/enter-50/) |
| <div class="dot-sm bg-flow opacity-50" aria-label="blue"></div> | [flow:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/flow-50/) | [flow:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/flow-50/) | [flow:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/flow-50/) | [flow:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/flow-50/) | [flow:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/flow-50/) |
| <div class="dot-sm bg-close opacity-50" aria-label="purple"></div> | [close:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/close-50/) | [close:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/close-50/) | [close:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/close-50/) | [close:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/close-50/) | [close:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/close-50/) |

#### Side B ノード

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-sm bg-still opacity-50" aria-label="yellow"></div> | [still:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/still-50/) | [still:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/still-50/) | [still:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/still-50/) | [still:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/still-50/) | [still:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/still-50/) |
| <div class="dot-sm bg-void opacity-50" aria-label="red"></div> | [void:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/void-50/) | [void:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/void-50/) | [void:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/void-50/) | [void:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/void-50/) | [void:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/void-50/) |
| <div class="dot-sm bg-surge opacity-50" aria-label="magenta"></div> | [surge:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/surge-50/) | [surge:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/surge-50/) | [surge:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/surge-50/) | [surge:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/surge-50/) | [surge:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/surge-50/) |
| <div class="dot-sm bg-wither opacity-50" aria-label="green"></div> | [wither:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/wither-50/) | [wither:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/wither-50/) | [wither:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/wither-50/) | [wither:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/wither-50/) | [wither:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/wither-50/) |
| <div class="dot-sm bg-collapse opacity-50" aria-label="transparent"></div> | [collapse:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/collapse-50/) | [collapse:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/collapse-50/) | [collapse:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/collapse-50/) | [collapse:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/collapse-50/) | [collapse:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/collapse-50/) |
| <div class="dot-sm bg-haze opacity-50" aria-label="white"></div> | [haze:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/haze-50/) | [haze:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/haze-50/) | [haze:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/haze-50/) | [haze:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/haze-50/) | [haze:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/haze-50/) |
| <div class="dot-sm bg-drift opacity-50" aria-label="cyan"></div> | [drift:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/drift-50/) | [drift:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/drift-50/) | [drift:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/drift-50/) | [drift:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/drift-50/) | [drift:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/drift-50/) |
| <div class="dot-sm bg-abyss opacity-50" aria-label="blue"></div> | [abyss:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/abyss-50/) | [abyss:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/abyss-50/) | [abyss:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/abyss-50/) | [abyss:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/abyss-50/) | [abyss:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/abyss-50/) |
| <div class="dot-sm bg-fade opacity-50" aria-label="purple"></div> | [fade:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/fade-50/) | [fade:50](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/fade-50/) | [fade:50](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/fade-50/) | [fade:50](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/fade-50/) | [fade:50](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/fade-50/) |

---

### グリッド (19x19)

MTP Skill のグリッド（`/mtp <column:row>`）を指定した場合の出力です。  
`J:10` は中心座標であり、MTP の制約が出力されない中立ノードとして扱われます。

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-sm bg-still" aria-label="yellow"></div> | [A:1](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/a-1/) | [A:1](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/a-1/) | [A:1](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/a-1/) | [A:1](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/a-1/) | [A:1](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/a-1/) |
| <div class="dot-sm bg-wither" aria-label="green"></div> | [A:10](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/a-10/) | [A:10](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/a-10/) | [A:10](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/a-10/) | [A:10](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/a-10/) | [A:10](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/a-10/) |
| <div class="dot-sm bg-drift" aria-label="cyan"></div> | [A:19](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/a-19/) | [A:19](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/a-19/) | [A:19](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/a-19/) | [A:19](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/a-19/) | [A:19](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/a-19/) |
| <div class="dot-sm bg-open" aria-label="yellow"></div> | [D:4](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/d-4/) | [D:4](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/d-4/) | [D:4](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/d-4/) | [D:4](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/d-4/) | [D:4](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/d-4/) |
| <div class="dot-sm bg-grow" aria-label="green"></div> | [D:10](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/d-10/) | [D:10](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/d-10/) | [D:10](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/d-10/) | [D:10](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/d-10/) | [D:10](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/d-10/) |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | [D:16](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/d-16/) | [D:16](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/d-16/) | [D:16](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/d-16/) | [D:16](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/d-16/) | [D:16](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/d-16/) |
| <div class="dot-sm bg-void" aria-label="red"></div> | [J:1](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/j-1/) | [J:1](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/j-1/) | [J:1](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/j-1/) | [J:1](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/j-1/) | [J:1](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/j-1/) |
| <div class="dot-sm bg-power" aria-label="red"></div> | [J:4](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/j-4/) | [J:4](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/j-4/) | [J:4](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/j-4/) | [J:4](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/j-4/) | [J:4](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/j-4/) |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | [J:10](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/j-10/) | [J:10](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/j-10/) | [J:10](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/j-10/) | [J:10](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/j-10/) | [J:10](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/j-10/) |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | [J:16](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/j-16/) | [J:16](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/j-16/) | [J:16](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/j-16/) | [J:16](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/j-16/) | [J:16](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/j-16/) |
| <div class="dot-sm bg-abyss" aria-label="blue"></div> | [J:19](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/j-19/) | [J:19](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/j-19/) | [J:19](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/j-19/) | [J:19](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/j-19/) | [J:19](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/j-19/) |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | [P:4](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/p-4/) | [P:4](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/p-4/) | [P:4](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/p-4/) | [P:4](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/p-4/) | [P:4](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/p-4/) |
| <div class="dot-sm bg-focus" aria-label="white"></div> | [P:10](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/p-10/) | [P:10](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/p-10/) | [P:10](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/p-10/) | [P:10](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/p-10/) | [P:10](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/p-10/) |
| <div class="dot-sm bg-close" aria-label="purple"></div> | [P:16](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/p-16/) | [P:16](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/p-16/) | [P:16](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/p-16/) | [P:16](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/p-16/) | [P:16](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/p-16/) |
| <div class="dot-sm bg-surge" aria-label="magenta"></div> | [S:1](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/s-1/) | [S:1](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/s-1/) | [S:1](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/s-1/) | [S:1](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/s-1/) | [S:1](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/s-1/) |
| <div class="dot-sm bg-haze" aria-label="white"></div> | [S:10](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/s-10/) | [S:10](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/s-10/) | [S:10](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/s-10/) | [S:10](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/s-10/) | [S:10](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/s-10/) |
| <div class="dot-sm bg-fade" aria-label="purple"></div> | [S:19](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/s-19/) | [S:19](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/s-19/) | [S:19](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/s-19/) | [S:19](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/s-19/) | [S:19](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/s-19/) |

---

### プリセット

MTP Skill のプリセット（`/mtp <preset>`）を指定した場合の出力です。

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-group"><div class="dot-sm bg-close" aria-label="purple"></div><div class="dot-sm bg-return" aria-label="magenta"></div></div> | [strategist](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/preset/strategist/) | [strategist](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/preset/strategist/) | [strategist](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/preset/strategist/) | [strategist](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/preset/strategist/) | [strategist](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/preset/strategist/) |
| <div class="dot-group"><div class="dot-sm bg-enter" aria-label="cyan"></div><div class="dot-sm bg-still" aria-label="yellow"></div></div> | [synthesizer](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/preset/synthesizer/) | [synthesizer](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/preset/synthesizer/) | [synthesizer](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/preset/synthesizer/) | [synthesizer](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/preset/synthesizer/) | [synthesizer](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/preset/synthesizer/) |
| <div class="dot-group"><div class="dot-sm bg-open" aria-label="yellow"></div><div class="dot-sm bg-drift" aria-label="cyan"></div></div> | [maverick](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/preset/maverick/) | [maverick](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/preset/maverick/) | [maverick](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/preset/maverick/) | [maverick](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/preset/maverick/) | [maverick](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/preset/maverick/) |
| <div class="dot-group"><div class="dot-sm bg-j13" aria-label="blue"></div><div class="dot-sm bg-grow" aria-label="green"></div></div> | [concierge](/ja/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/preset/concierge/) | [concierge](/ja/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/preset/concierge/) | [concierge](/ja/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/preset/concierge/) | [concierge](/ja/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/preset/concierge/) | [concierge](/ja/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/preset/concierge/) |
