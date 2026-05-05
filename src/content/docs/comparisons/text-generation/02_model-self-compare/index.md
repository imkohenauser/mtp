---
title: 'Comparison Task: Model Self-Introduction'
description: Compare how MTP Skill changes model self-introduction outputs across baseline, slider, grid, and preset settings.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/comparisons_text-generation_02_model-self-compare.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/comparisons_text-generation_02_model-self-compare.png
---

**Prompt**

```markdown
/mtp <args> Compared with other major AI models from competing companies, please explain your strengths. If up-to-date comparison requires current information, say so clearly.
```

**Coverage**
- Baseline: 1 item (without applying MTP Skill)
- Slider `<node:100>`: 18 items
- Slider `<node:50>`: 18 items
- Grid `<column:row>`: 17 items
- Preset `<preset>`: 4 items

**Models**
- Sonnet 4.6 on Claude Code (Claude macOS app)
- Gemini 3 Flash on Antigravity (macOS app)
- ChatGPT 5.5 on Codex (macOS app)

---

## Output Comparison

In the test environment, each result was produced in a fresh agent chat session without special user settings or cross-chat memory.

### Baseline

Output when the prompt is entered as-is, without applying MTP Skill.

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [baseline](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/baseline/) | [baseline](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/baseline/) | [baseline](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/baseline/) |

---

### Slider (:100)

Output when using the MTP Skill slider (`/mtp <node:100>`).

#### Side A Nodes

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [open:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/open-100/) | [open:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/open-100/) | [open:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/open-100/) |
| [power:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/power-100/) | [power:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/power-100/) | [power:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/power-100/) |
| [return:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/return-100/) | [return:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/return-100/) | [return:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/return-100/) |
| [grow:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/grow-100/) | [grow:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/grow-100/) | [grow:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/grow-100/) |
| [helix:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/helix-100/) | [helix:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/helix-100/) | [helix:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/helix-100/) |
| [focus:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/focus-100/) | [focus:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/focus-100/) | [focus:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/focus-100/) |
| [enter:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/enter-100/) | [enter:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/enter-100/) | [enter:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/enter-100/) |
| [flow:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/flow-100/) | [flow:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/flow-100/) | [flow:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/flow-100/) |
| [close:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/close-100/) | [close:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/close-100/) | [close:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/close-100/) |

#### Side B Nodes

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [still:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/still-100/) | [still:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/still-100/) | [still:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/still-100/) |
| [void:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/void-100/) | [void:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/void-100/) | [void:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/void-100/) |
| [surge:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/surge-100/) | [surge:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/surge-100/) | [surge:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/surge-100/) |
| [wither:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/wither-100/) | [wither:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/wither-100/) | [wither:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/wither-100/) |
| [collapse:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/collapse-100/) | [collapse:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/collapse-100/) | [collapse:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/collapse-100/) |
| [haze:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/haze-100/) | [haze:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/haze-100/) | [haze:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/haze-100/) |
| [drift:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/drift-100/) | [drift:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/drift-100/) | [drift:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/drift-100/) |
| [abyss:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/abyss-100/) | [abyss:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/abyss-100/) | [abyss:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/abyss-100/) |
| [fade:100](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/fade-100/) | [fade:100](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/fade-100/) | [fade:100](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/fade-100/) |

---

### Slider (:50)

Output when using the MTP Skill slider (`/mtp <node:50>`).

#### Side A Nodes

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [open:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/open-50/) | [open:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/open-50/) | [open:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/open-50/) |
| [power:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/power-50/) | [power:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/power-50/) | [power:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/power-50/) |
| [return:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/return-50/) | [return:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/return-50/) | [return:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/return-50/) |
| [grow:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/grow-50/) | [grow:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/grow-50/) | [grow:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/grow-50/) |
| [helix:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/helix-50/) | [helix:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/helix-50/) | [helix:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/helix-50/) |
| [focus:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/focus-50/) | [focus:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/focus-50/) | [focus:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/focus-50/) |
| [enter:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/enter-50/) | [enter:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/enter-50/) | [enter:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/enter-50/) |
| [flow:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/flow-50/) | [flow:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/flow-50/) | [flow:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/flow-50/) |
| [close:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/close-50/) | [close:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/close-50/) | [close:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/close-50/) |

#### Side B Nodes

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [still:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/still-50/) | [still:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/still-50/) | [still:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/still-50/) |
| [void:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/void-50/) | [void:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/void-50/) | [void:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/void-50/) |
| [surge:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/surge-50/) | [surge:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/surge-50/) | [surge:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/surge-50/) |
| [wither:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/wither-50/) | [wither:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/wither-50/) | [wither:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/wither-50/) |
| [collapse:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/collapse-50/) | [collapse:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/collapse-50/) | [collapse:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/collapse-50/) |
| [haze:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/haze-50/) | [haze:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/haze-50/) | [haze:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/haze-50/) |
| [drift:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/drift-50/) | [drift:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/drift-50/) | [drift:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/drift-50/) |
| [abyss:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/abyss-50/) | [abyss:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/abyss-50/) | [abyss:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/abyss-50/) |
| [fade:50](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/slider/fade-50/) | [fade:50](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/slider/fade-50/) | [fade:50](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/slider/fade-50/) |

---

### Grid

Output when using the MTP Skill grid (`/mtp <column:row>`).  
`J:10` is the center coordinate and treated as a neutral node where MTP constraints are not emitted.

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [A:1](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/a-1/) | [A:1](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/a-1/) | [A:1](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/a-1/) |
| [A:10](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/a-10/) | [A:10](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/a-10/) | [A:10](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/a-10/) |
| [A:19](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/a-19/) | [A:19](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/a-19/) | [A:19](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/a-19/) |
| [D:4](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/d-4/) | [D:4](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/d-4/) | [D:4](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/d-4/) |
| [D:10](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/d-10/) | [D:10](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/d-10/) | [D:10](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/d-10/) |
| [D:16](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/d-16/) | [D:16](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/d-16/) | [D:16](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/d-16/) |
| [J:1](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/j-1/) | [J:1](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/j-1/) | [J:1](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/j-1/) |
| [J:4](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/j-4/) | [J:4](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/j-4/) | [J:4](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/j-4/) |
| [J:10](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/j-10/) | [J:10](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/j-10/) | [J:10](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/j-10/) |
| [J:16](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/j-16/) | [J:16](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/j-16/) | [J:16](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/j-16/) |
| [J:19](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/j-19/) | [J:19](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/j-19/) | [J:19](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/j-19/) |
| [P:4](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/p-4/) | [P:4](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/p-4/) | [P:4](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/p-4/) |
| [P:10](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/p-10/) | [P:10](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/p-10/) | [P:10](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/p-10/) |
| [P:16](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/p-16/) | [P:16](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/p-16/) | [P:16](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/p-16/) |
| [S:1](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/s-1/) | [S:1](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/s-1/) | [S:1](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/s-1/) |
| [S:10](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/s-10/) | [S:10](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/s-10/) | [S:10](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/s-10/) |
| [S:19](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/grid/s-19/) | [S:19](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/grid/s-19/) | [S:19](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/grid/s-19/) |

---

### Preset

Output when using MTP Skill presets (`/mtp <preset>`).

| ChatGPT 5.5 | Gemini 3 Flash | Sonnet 4.6 |
| ----------------- | ------------------- | ---------------- |
| [strategist](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/preset/strategist/) | [strategist](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/preset/strategist/) | [strategist](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/preset/strategist/) |
| [synthesizer](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/preset/synthesizer/) | [synthesizer](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/preset/synthesizer/) | [synthesizer](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/preset/synthesizer/) |
| [maverick](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/preset/maverick/) | [maverick](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/preset/maverick/) | [maverick](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/preset/maverick/) |
| [concierge](/comparisons/text-generation/02_model-self-compare/gpt-5-5-medium_codex/preset/concierge/) | [concierge](/comparisons/text-generation/02_model-self-compare/gemini-3-flash_antigravity/preset/concierge/) | [concierge](/comparisons/text-generation/02_model-self-compare/sonnet-4-6_claude-code/preset/concierge/) |