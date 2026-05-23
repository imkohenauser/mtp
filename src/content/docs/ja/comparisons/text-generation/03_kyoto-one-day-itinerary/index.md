---
title: "設計課題: 観光プラン提案"
description: 京都の一日観光プラン提案課題で、MTP Skill による出力構成や提案内容の違いを比較します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_text-generation_03_kyoto-one-day-itinerary.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_comparisons_text-generation_03_kyoto-one-day-itinerary.png
lastUpdated: true
---

**プロンプト**

```markdown
/mtp <args> 
夏に京都へ一週間滞在します。特別な一日の観光プランを提案してください。営業時間や予約など、事前確認が必要な点も示してください。
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
| [baseline](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/baseline/) | [baseline](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/baseline/) | [baseline](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/baseline/) |

---

### スライダー（:100）

MTP Skill のスライダー（`/mtp <node:100>`）を指定した場合の出力です。

#### Side A ノード

| | ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ----------------- | ------------------- | ---------------- |
| <div class="dot-sm bg-open" aria-label="yellow"></div> | [open:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/open-100/) | [open:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/open-100/) | [open:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/open-100/) |
| <div class="dot-sm bg-power" aria-label="red"></div> | [power:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/power-100/) | [power:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/power-100/) | [power:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/power-100/) |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | [return:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/return-100/) | [return:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/return-100/) | [return:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/return-100/) |
| <div class="dot-sm bg-grow" aria-label="green"></div> | [grow:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/grow-100/) | [grow:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/grow-100/) | [grow:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/grow-100/) |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | [helix:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/helix-100/) | [helix:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/helix-100/) | [helix:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/helix-100/) |
| <div class="dot-sm bg-focus" aria-label="white"></div> | [focus:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/focus-100/) | [focus:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/focus-100/) | [focus:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/focus-100/) |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | [enter:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/enter-100/) | [enter:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/enter-100/) | [enter:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/enter-100/) |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | [flow:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/flow-100/) | [flow:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/flow-100/) | [flow:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/flow-100/) |
| <div class="dot-sm bg-close" aria-label="purple"></div> | [close:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/close-100/) | [close:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/close-100/) | [close:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/close-100/) |

#### Side B ノード

| | ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ----------------- | ------------------- | ---------------- |
| <div class="dot-sm bg-still" aria-label="yellow"></div> | [still:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/still-100/) | [still:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/still-100/) | [still:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/still-100/) |
| <div class="dot-sm bg-void" aria-label="red"></div> | [void:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/void-100/) | [void:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/void-100/) | [void:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/void-100/) |
| <div class="dot-sm bg-surge" aria-label="magenta"></div> | [surge:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/surge-100/) | [surge:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/surge-100/) | [surge:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/surge-100/) |
| <div class="dot-sm bg-wither" aria-label="green"></div> | [wither:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/wither-100/) | [wither:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/wither-100/) | [wither:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/wither-100/) |
| <div class="dot-sm bg-collapse" aria-label="transparent"></div> | [collapse:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/collapse-100/) | [collapse:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/collapse-100/) | [collapse:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/collapse-100/) |
| <div class="dot-sm bg-haze" aria-label="white"></div> | [haze:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/haze-100/) | [haze:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/haze-100/) | [haze:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/haze-100/) |
| <div class="dot-sm bg-drift" aria-label="cyan"></div> | [drift:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/drift-100/) | [drift:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/drift-100/) | [drift:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/drift-100/) |
| <div class="dot-sm bg-abyss" aria-label="blue"></div> | [abyss:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/abyss-100/) | [abyss:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/abyss-100/) | [abyss:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/abyss-100/) |
| <div class="dot-sm bg-fade" aria-label="purple"></div> | [fade:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/fade-100/) | [fade:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/fade-100/) | [fade:100](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/fade-100/) |

---

### スライダー（:50）

MTP Skill のスライダー（`/mtp <node:50>`）を指定した場合の出力です。

#### Side A ノード

| | ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ----------------- | ------------------- | ---------------- |
| <div class="dot-sm bg-open opacity-50" aria-label="yellow"></div> | [open:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/open-50/) | [open:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/open-50/) | [open:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/open-50/) |
| <div class="dot-sm bg-power opacity-50" aria-label="red"></div> | [power:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/power-50/) | [power:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/power-50/) | [power:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/power-50/) |
| <div class="dot-sm bg-return opacity-50" aria-label="magenta"></div> | [return:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/return-50/) | [return:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/return-50/) | [return:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/return-50/) |
| <div class="dot-sm bg-grow opacity-50" aria-label="green"></div> | [grow:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/grow-50/) | [grow:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/grow-50/) | [grow:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/grow-50/) |
| <div class="dot-sm bg-helix opacity-50" aria-label="transparent"></div> | [helix:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/helix-50/) | [helix:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/helix-50/) | [helix:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/helix-50/) |
| <div class="dot-sm bg-focus opacity-50" aria-label="white"></div> | [focus:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/focus-50/) | [focus:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/focus-50/) | [focus:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/focus-50/) |
| <div class="dot-sm bg-enter opacity-50" aria-label="cyan"></div> | [enter:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/enter-50/) | [enter:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/enter-50/) | [enter:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/enter-50/) |
| <div class="dot-sm bg-flow opacity-50" aria-label="blue"></div> | [flow:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/flow-50/) | [flow:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/flow-50/) | [flow:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/flow-50/) |
| <div class="dot-sm bg-close opacity-50" aria-label="purple"></div> | [close:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/close-50/) | [close:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/close-50/) | [close:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/close-50/) |

#### Side B ノード

| | ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ----------------- | ------------------- | ---------------- |
| <div class="dot-sm bg-still opacity-50" aria-label="yellow"></div> | [still:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/still-50/) | [still:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/still-50/) | [still:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/still-50/) |
| <div class="dot-sm bg-void opacity-50" aria-label="red"></div> | [void:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/void-50/) | [void:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/void-50/) | [void:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/void-50/) |
| <div class="dot-sm bg-surge opacity-50" aria-label="magenta"></div> | [surge:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/surge-50/) | [surge:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/surge-50/) | [surge:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/surge-50/) |
| <div class="dot-sm bg-wither opacity-50" aria-label="green"></div> | [wither:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/wither-50/) | [wither:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/wither-50/) | [wither:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/wither-50/) |
| <div class="dot-sm bg-collapse opacity-50" aria-label="transparent"></div> | [collapse:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/collapse-50/) | [collapse:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/collapse-50/) | [collapse:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/collapse-50/) |
| <div class="dot-sm bg-haze opacity-50" aria-label="white"></div> | [haze:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/haze-50/) | [haze:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/haze-50/) | [haze:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/haze-50/) |
| <div class="dot-sm bg-drift opacity-50" aria-label="cyan"></div> | [drift:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/drift-50/) | [drift:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/drift-50/) | [drift:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/drift-50/) |
| <div class="dot-sm bg-abyss opacity-50" aria-label="blue"></div> | [abyss:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/abyss-50/) | [abyss:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/abyss-50/) | [abyss:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/abyss-50/) |
| <div class="dot-sm bg-fade opacity-50" aria-label="purple"></div> | [fade:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/slider/fade-50/) | [fade:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/slider/fade-50/) | [fade:50](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/slider/fade-50/) |

---

### グリッド (19x19)

MTP Skill のグリッド（`/mtp <column:row>`）を指定した場合の出力です。  
`J:10` は中心座標であり、MTP の制約が出力されない中立ノードとして扱われます。

| | ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ----------------- | ------------------- | ---------------- |
| <div class="dot-sm bg-still" aria-label="yellow"></div> | [A:1](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/a-1/) | [A:1](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/a-1/) | [A:1](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/a-1/) |
| <div class="dot-sm bg-wither" aria-label="green"></div> | [A:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/a-10/) | [A:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/a-10/) | [A:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/a-10/) |
| <div class="dot-sm bg-drift" aria-label="cyan"></div> | [A:19](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/a-19/) | [A:19](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/a-19/) | [A:19](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/a-19/) |
| <div class="dot-sm bg-open" aria-label="yellow"></div> | [D:4](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/d-4/) | [D:4](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/d-4/) | [D:4](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/d-4/) |
| <div class="dot-sm bg-grow" aria-label="green"></div> | [D:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/d-10/) | [D:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/d-10/) | [D:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/d-10/) |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | [D:16](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/d-16/) | [D:16](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/d-16/) | [D:16](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/d-16/) |
| <div class="dot-sm bg-void" aria-label="red"></div> | [J:1](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/j-1/) | [J:1](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/j-1/) | [J:1](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/j-1/) |
| <div class="dot-sm bg-power" aria-label="red"></div> | [J:4](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/j-4/) | [J:4](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/j-4/) | [J:4](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/j-4/) |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | [J:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/j-10/) | [J:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/j-10/) | [J:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/j-10/) |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | [J:16](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/j-16/) | [J:16](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/j-16/) | [J:16](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/j-16/) |
| <div class="dot-sm bg-abyss" aria-label="blue"></div> | [J:19](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/j-19/) | [J:19](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/j-19/) | [J:19](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/j-19/) |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | [P:4](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/p-4/) | [P:4](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/p-4/) | [P:4](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/p-4/) |
| <div class="dot-sm bg-focus" aria-label="white"></div> | [P:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/p-10/) | [P:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/p-10/) | [P:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/p-10/) |
| <div class="dot-sm bg-close" aria-label="purple"></div> | [P:16](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/p-16/) | [P:16](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/p-16/) | [P:16](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/p-16/) |
| <div class="dot-sm bg-surge" aria-label="magenta"></div> | [S:1](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/s-1/) | [S:1](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/s-1/) | [S:1](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/s-1/) |
| <div class="dot-sm bg-haze" aria-label="white"></div> | [S:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/s-10/) | [S:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/s-10/) | [S:10](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/s-10/) |
| <div class="dot-sm bg-fade" aria-label="purple"></div> | [S:19](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/grid/s-19/) | [S:19](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/grid/s-19/) | [S:19](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/grid/s-19/) |

---

### プリセット

MTP Skill のプリセット（`/mtp <preset>`）を指定した場合の出力です。

| | ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ----------------- | ------------------- | ---------------- |
| <div class="dot-group"><div class="dot-sm bg-close" aria-label="purple"></div><div class="dot-sm bg-return" aria-label="magenta"></div></div> | [strategist](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/preset/strategist/) | [strategist](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/preset/strategist/) | [strategist](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/preset/strategist/) |
| <div class="dot-group"><div class="dot-sm bg-enter" aria-label="cyan"></div><div class="dot-sm bg-still" aria-label="yellow"></div></div> | [synthesizer](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/preset/synthesizer/) | [synthesizer](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/preset/synthesizer/) | [synthesizer](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/preset/synthesizer/) |
| <div class="dot-group"><div class="dot-sm bg-open" aria-label="yellow"></div><div class="dot-sm bg-drift" aria-label="cyan"></div></div> | [maverick](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/preset/maverick/) | [maverick](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/preset/maverick/) | [maverick](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/preset/maverick/) |
| <div class="dot-group"><div class="dot-sm bg-j13" aria-label="blue"></div><div class="dot-sm bg-grow" aria-label="green"></div></div> | [concierge](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gpt-5-5-medium_codex/preset/concierge/) | [concierge](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/gemini-3-flash_antigravity/preset/concierge/) | [concierge](/ja/comparisons/text-generation/03_kyoto-one-day-itinerary/sonnet-4-6_claude-code/preset/concierge/) |
