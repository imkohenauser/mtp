---
title: "比較課題: モデルの自己紹介"
description: モデルの自己紹介課題で、ベースライン、スライダー、グリッド、プリセットごとの出力を比較します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_text-generation_02_model-self-compare.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_text-generation_02_model-self-compare.png
---

**プロンプト**

```markdown
/mtp <args> 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

**適用範囲**
- ベースライン： 1 件（MTP Skill を適用しない）
- スライダー `<node:100>`： 18 件
- スライダー `<node:50>`： 18 件
- グリッド `<column:row>`： 17 件
- プリセット `<preset>`： 4 件

**モデル**
- Sonnet 4.6 on Claude Code (Claude macOS app)
- Gemini 3 Flash on Antigravity (macOS app)
- ChatGPT 5.5 on Codex (macOS app)

---

## 出力比較

テスト環境では、特別なユーザー設定や、横断的なチャット会話の記憶を含まない状態で、それぞれ、新しいエージェントチャットセッションを開始してテストを行った結果です。

### ベースライン

MTP Skill を適用せずに、プロンプトをそのまま入力した場合の出力です。

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [baseline](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/baseline/) | [baseline](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/baseline/) | [baseline](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/baseline/) |

---

### スライダー（:100）

MTP Skill のスライダー（`/mtp <node:100>`）を指定した場合の出力です。

#### Side A ノード

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [open:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/open-100/) | [open:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/open-100/) | [open:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/open-100/) |
| [power:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/power-100/) | [power:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/power-100/) | [power:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/power-100/) |
| [return:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/return-100/) | [return:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/return-100/) | [return:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/return-100/) |
| [grow:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/grow-100/) | [grow:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/grow-100/) | [grow:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/grow-100/) |
| [helix:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/helix-100/) | [helix:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/helix-100/) | [helix:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/helix-100/) |
| [focus:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/focus-100/) | [focus:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/focus-100/) | [focus:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/focus-100/) |
| [enter:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/enter-100/) | [enter:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/enter-100/) | [enter:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/enter-100/) |
| [flow:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/flow-100/) | [flow:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/flow-100/) | [flow:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/flow-100/) |
| [close:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/close-100/) | [close:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/close-100/) | [close:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/close-100/) |

#### Side B ノード

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [still:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/still-100/) | [still:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/still-100/) | [still:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/still-100/) |
| [void:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/void-100/) | [void:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/void-100/) | [void:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/void-100/) |
| [surge:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/surge-100/) | [surge:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/surge-100/) | [surge:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/surge-100/) |
| [wither:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/wither-100/) | [wither:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/wither-100/) | [wither:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/wither-100/) |
| [collapse:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/collapse-100/) | [collapse:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/collapse-100/) | [collapse:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/collapse-100/) |
| [haze:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/haze-100/) | [haze:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/haze-100/) | [haze:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/haze-100/) |
| [drift:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/drift-100/) | [drift:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/drift-100/) | [drift:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/drift-100/) |
| [abyss:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/abyss-100/) | [abyss:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/abyss-100/) | [abyss:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/abyss-100/) |
| [fade:100](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/fade-100/) | [fade:100](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/fade-100/) | [fade:100](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/fade-100/) |

---

### スライダー（:50）

MTP Skill のスライダー（`/mtp <node:50>`）を指定した場合の出力です。

#### Side A ノード

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [open:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/open-50/) | [open:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/open-50/) | [open:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/open-50/) |
| [power:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/power-50/) | [power:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/power-50/) | [power:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/power-50/) |
| [return:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/return-50/) | [return:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/return-50/) | [return:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/return-50/) |
| [grow:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/grow-50/) | [grow:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/grow-50/) | [grow:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/grow-50/) |
| [helix:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/helix-50/) | [helix:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/helix-50/) | [helix:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/helix-50/) |
| [focus:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/focus-50/) | [focus:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/focus-50/) | [focus:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/focus-50/) |
| [enter:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/enter-50/) | [enter:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/enter-50/) | [enter:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/enter-50/) |
| [flow:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/flow-50/) | [flow:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/flow-50/) | [flow:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/flow-50/) |
| [close:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/close-50/) | [close:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/close-50/) | [close:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/close-50/) |

#### Side B ノード

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [still:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/still-50/) | [still:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/still-50/) | [still:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/still-50/) |
| [void:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/void-50/) | [void:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/void-50/) | [void:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/void-50/) |
| [surge:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/surge-50/) | [surge:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/surge-50/) | [surge:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/surge-50/) |
| [wither:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/wither-50/) | [wither:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/wither-50/) | [wither:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/wither-50/) |
| [collapse:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/collapse-50/) | [collapse:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/collapse-50/) | [collapse:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/collapse-50/) |
| [haze:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/haze-50/) | [haze:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/haze-50/) | [haze:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/haze-50/) |
| [drift:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/drift-50/) | [drift:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/drift-50/) | [drift:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/drift-50/) |
| [abyss:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/abyss-50/) | [abyss:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/abyss-50/) | [abyss:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/abyss-50/) |
| [fade:50](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/fade-50/) | [fade:50](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/fade-50/) | [fade:50](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/fade-50/) |

---

### グリッド (19x19)

MTP Skill のグリッド（`/mtp <column:row>`）を指定した場合の出力です。  
`J:10` は中心座標であり、MTP の制約が出力されない中立ノードとして扱われます。

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [A:1](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/a-1/) | [A:1](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/a-1/) | [A:1](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/a-1/) |
| [A:10](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/a-10/) | [A:10](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/a-10/) | [A:10](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/a-10/) |
| [A:19](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/a-19/) | [A:19](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/a-19/) | [A:19](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/a-19/) |
| [D:4](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/d-4/) | [D:4](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/d-4/) | [D:4](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/d-4/) |
| [D:10](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/d-10/) | [D:10](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/d-10/) | [D:10](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/d-10/) |
| [D:16](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/d-16/) | [D:16](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/d-16/) | [D:16](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/d-16/) |
| [J:1](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/j-1/) | [J:1](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/j-1/) | [J:1](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/j-1/) |
| [J:4](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/j-4/) | [J:4](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/j-4/) | [J:4](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/j-4/) |
| [J:10](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/j-10/) | [J:10](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/j-10/) | [J:10](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/j-10/) |
| [J:16](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/j-16/) | [J:16](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/j-16/) | [J:16](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/j-16/) |
| [J:19](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/j-19/) | [J:19](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/j-19/) | [J:19](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/j-19/) |
| [P:4](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/p-4/) | [P:4](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/p-4/) | [P:4](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/p-4/) |
| [P:10](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/p-10/) | [P:10](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/p-10/) | [P:10](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/p-10/) |
| [P:16](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/p-16/) | [P:16](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/p-16/) | [P:16](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/p-16/) |
| [S:1](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/s-1/) | [S:1](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/s-1/) | [S:1](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/s-1/) |
| [S:10](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/s-10/) | [S:10](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/s-10/) | [S:10](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/s-10/) |
| [S:19](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/s-19/) | [S:19](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/s-19/) | [S:19](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/s-19/) |

---

### プリセット

MTP Skill のプリセット（`/mtp <preset>`）を指定した場合の出力です。

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [strategist](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/preset/strategist/) | [strategist](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/preset/strategist/) | [strategist](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/preset/strategist/) |
| [synthesizer](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/preset/synthesizer/) | [synthesizer](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/preset/synthesizer/) | [synthesizer](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/preset/synthesizer/) |
| [maverick](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/preset/maverick/) | [maverick](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/preset/maverick/) | [maverick](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/preset/maverick/) |
| [concierge](/ja/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/preset/concierge/) | [concierge](/ja/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/preset/concierge/) | [concierge](/ja/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/preset/concierge/) |
