---
title: 'Literary task: Alice in Wonderland'
description: Compare how MTP Skill changes Alice in Wonderland introductions across baseline, slider, grid, and preset settings.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/comparisons_text-generation_04_alice-in-wonderland.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/comparisons_text-generation_04_alice-in-wonderland.png
lastUpdated: true
---

**Prompt**

```markdown
/mtp <args> 
Tell the story of Alice’s Adventures in Wonderland by Lewis Carroll in a way that makes someone want to read it.
```

**Coverage**
- Baseline: 1 item (without applying MTP Skill)
- Slider `<node:100>`: 18 items
- Slider `<node:50>`: 18 items
- Grid `<column:row>`: 17 items
- Preset `<preset>`: 4 items

**Models**
- ChatGPT 5.5 on Codex (macOS app)
- Gemini 3.5 Flash on Antigravity 2.0 (macOS app)
- Composer 2.5 on Cursor 3.5 (macOS app)
- Sonnet 4.6 on Claude.ai (iOS app)
- Manus 1.6 Lite on Manus.im (iOS app)

---

## How to read this comparison

This page is not just a list of generated outputs. It compares how MTP Skill changes output direction, structure, and narrative style for the same literary introduction task.

The English and Japanese pages are not translations of each other. The English page uses an English prompt, while the Japanese page uses a Japanese prompt, and the tests were run independently in each language. The comparison is designed to be read by observing how outputs shift from the baseline within each language, rather than by matching English and Japanese text line by line.

The baseline shows each model's natural output tendency without MTP Skill applied. Slider, grid, and preset outputs show how an MTP control direction is layered on top of each model's own writing habits.

## What changes from the baseline?

The following MTP arguments are representative examples that are easy to compare in this test. For each output, compare both the difference from the baseline and the differences between models using the same argument.

| MTP argument | Main effect | What to compare |
| ---------------------- | ---------------- | ---------------------- |
| `power:50 / power:100` | Increases intensity, assertion, and pressure on the reader | Difference from baseline; strength difference between 50 and 100 |
| `J:16` | Strengthens flow, immersion, and continuous narration | Whether the output slips more naturally into the story than the baseline |
| `D:10` | Expands into background, reasons, applications, and interpretation | Whether the output becomes more layered and hierarchical than the baseline |
| `concierge` | Combines guidance and expansion | Whether the output works as a guide that leads the reader into the work |

## Execution environments and Skill execution

This comparison includes both developer-oriented macOS agent environments and mobile iOS app environments. In each environment, `/mtp` was invoked as a slash command, and compiler execution was confirmed in the logs.

| Model | Host | Environment | Skill execution |
| ---------------- | ----------- | ----------- | --------------------------------------------------------------------- |
| ChatGPT 5.5 | Codex | macOS app | CLI-installed MTP Skill invoked through a slash command; compiler execution confirmed in logs |
| Gemini 3.5 Flash | Antigravity | macOS app | CLI-installed MTP Skill invoked through a slash command; compiler execution confirmed in logs |
| Composer 2.5 | Cursor | macOS app | CLI-installed MTP Skill invoked through a slash command; compiler execution confirmed in logs |
| Sonnet 4.6 | Claude.ai | iOS app | ZIP-installed MTP Skill invoked through a slash command; compiler execution confirmed in logs |
| Manus 1.6 Lite | Manus.im | iOS app | ZIP-installed MTP Skill invoked through a slash command; compiler execution confirmed in the task log |

The macOS environments used a CLI-installed Skill, while the iOS environments used a ZIP-installed Skill. In all environments, the `/mtp` argument was compiled through the Skill workflow before the final output was generated, rather than treated as a plain text token. This shows that MTP can function as a portable output-shaping layer across both developer tools and mobile AI apps.

## Language-specific testing

The English and Japanese pages share the same comparison design. Both cover the baseline, slider `:100`, slider `:50`, grid, and preset ranges, and both use the same five models.

However, this is not a translation comparison intended to check whether the English and Japanese outputs say the same thing. A useful reading path is to first compare the baseline and MTP-controlled outputs within either the English or Japanese page, then check the same argument in the other language to see whether it plays a similar role.

## Cross-model consistency

MTP Skill does not erase model-specific writing habits. Gemini tends to structure outputs, Sonnet tends to produce literary-critical prose, Composer often writes like an edited article, and Manus tends toward accessible promotional explanation. However, the same MTP arguments still shift outputs in broadly consistent directions while preserving those model differences.

## Representative observations

`power` increases persuasive pressure on the reader. `power:50` tends toward a stronger recommendation, while `power:100` increases declarative, imperative, and defiant language.

`J:16` moves the output toward flowing narration. Instead of foregrounding headings or analysis, it strengthens the path that draws the reader into the story. `J:16` has the same interpretation as the node argument `flow:100`.

`D:10` grows the output. It adds background, reasons, applications, and reading paths, shifting the result from a simple introduction toward a more layered explanation.

`concierge` combines guidance and expansion. It expands to `J:13 D:10`, which is close to `flow:50 grow:100`: a moderately flowing narrative direction combined with strong layered expansion. It tends to produce an output that works like a guide leading the reader into the work.

---

## Output Comparison List

In the test environment, each result was produced in a fresh agent chat session without special user settings or cross-chat memory.

<!-- AUTO-GENERATED: model-output-indexes:start -->
### Integrated outputs by model

These pages combine only the output sections for each model, making them easier to inspect manually or analyze with an AI assistant.

| Model | Integrated output page | Integrated output file |
| --- | --- | --- |
| ChatGPT 5.5 | [HTML page](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/) | [Raw Markdown](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex.md) |
| Gemini 3.5 Flash | [HTML page](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/) | [Raw Markdown](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity.md) |
| Composer 2.5 | [HTML page](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/) | [Raw Markdown](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5.md) |
| Sonnet 4.6 | [HTML page](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/) | [Raw Markdown](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai.md) |
| Manus 1.6 Lite | [HTML page](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/) | [Raw Markdown](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im.md) |
<!-- AUTO-GENERATED: model-output-indexes:end -->

### Baseline

Output when the prompt is entered as-is, without applying MTP Skill.

| ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| [baseline](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/baseline/) | [baseline](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/baseline/) | [baseline](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/baseline/) | [baseline](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/baseline/) | [baseline](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/baseline/) |

---

### Slider (:100)

Output when using the MTP Skill slider (`/mtp <node:100>`).

#### Side A Nodes

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-sm bg-open" aria-label="yellow"></div> | [open:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/open-100/) | [open:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/open-100/) | [open:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/open-100/) | [open:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/open-100/) | [open:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/open-100/) |
| <div class="dot-sm bg-power" aria-label="red"></div> | [power:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/power-100/) | [power:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/power-100/) | [power:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/power-100/) | [power:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/power-100/) | [power:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/power-100/) |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | [return:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/return-100/) | [return:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/return-100/) | [return:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/return-100/) | [return:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/return-100/) | [return:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/return-100/) |
| <div class="dot-sm bg-grow" aria-label="green"></div> | [grow:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/grow-100/) | [grow:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/grow-100/) | [grow:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/grow-100/) | [grow:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/grow-100/) | [grow:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/grow-100/) |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | [helix:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/helix-100/) | [helix:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/helix-100/) | [helix:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/helix-100/) | [helix:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/helix-100/) | [helix:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/helix-100/) |
| <div class="dot-sm bg-focus" aria-label="white"></div> | [focus:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/focus-100/) | [focus:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/focus-100/) | [focus:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/focus-100/) | [focus:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/focus-100/) | [focus:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/focus-100/) |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | [enter:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/enter-100/) | [enter:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/enter-100/) | [enter:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/enter-100/) | [enter:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/enter-100/) | [enter:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/enter-100/) |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | [flow:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/flow-100/) | [flow:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/flow-100/) | [flow:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/flow-100/) | [flow:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/flow-100/) | [flow:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/flow-100/) |
| <div class="dot-sm bg-close" aria-label="purple"></div> | [close:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/close-100/) | [close:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/close-100/) | [close:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/close-100/) | [close:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/close-100/) | [close:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/close-100/) |

#### Side B Nodes

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-sm bg-still" aria-label="yellow"></div> | [still:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/still-100/) | [still:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/still-100/) | [still:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/still-100/) | [still:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/still-100/) | [still:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/still-100/) |
| <div class="dot-sm bg-void" aria-label="red"></div> | [void:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/void-100/) | [void:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/void-100/) | [void:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/void-100/) | [void:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/void-100/) | [void:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/void-100/) |
| <div class="dot-sm bg-surge" aria-label="magenta"></div> | [surge:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/surge-100/) | [surge:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/surge-100/) | [surge:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/surge-100/) | [surge:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/surge-100/) | [surge:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/surge-100/) |
| <div class="dot-sm bg-wither" aria-label="green"></div> | [wither:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/wither-100/) | [wither:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/wither-100/) | [wither:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/wither-100/) | [wither:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/wither-100/) | [wither:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/wither-100/) |
| <div class="dot-sm bg-collapse" aria-label="transparent"></div> | [collapse:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/collapse-100/) | [collapse:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/collapse-100/) | [collapse:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/collapse-100/) | [collapse:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/collapse-100/) | [collapse:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/collapse-100/) |
| <div class="dot-sm bg-haze" aria-label="white"></div> | [haze:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/haze-100/) | [haze:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/haze-100/) | [haze:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/haze-100/) | [haze:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/haze-100/) | [haze:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/haze-100/) |
| <div class="dot-sm bg-drift" aria-label="cyan"></div> | [drift:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/drift-100/) | [drift:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/drift-100/) | [drift:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/drift-100/) | [drift:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/drift-100/) | [drift:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/drift-100/) |
| <div class="dot-sm bg-abyss" aria-label="blue"></div> | [abyss:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/abyss-100/) | [abyss:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/abyss-100/) | [abyss:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/abyss-100/) | [abyss:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/abyss-100/) | [abyss:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/abyss-100/) |
| <div class="dot-sm bg-fade" aria-label="purple"></div> | [fade:100](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/fade-100/) | [fade:100](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/fade-100/) | [fade:100](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/fade-100/) | [fade:100](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/fade-100/) | [fade:100](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/fade-100/) |

---

### Slider (:50)

Output when using the MTP Skill slider (`/mtp <node:50>`).

#### Side A Nodes

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-sm bg-open opacity-50" aria-label="yellow"></div> | [open:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/open-50/) | [open:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/open-50/) | [open:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/open-50/) | [open:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/open-50/) | [open:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/open-50/) |
| <div class="dot-sm bg-power opacity-50" aria-label="red"></div> | [power:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/power-50/) | [power:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/power-50/) | [power:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/power-50/) | [power:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/power-50/) | [power:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/power-50/) |
| <div class="dot-sm bg-return opacity-50" aria-label="magenta"></div> | [return:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/return-50/) | [return:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/return-50/) | [return:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/return-50/) | [return:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/return-50/) | [return:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/return-50/) |
| <div class="dot-sm bg-grow opacity-50" aria-label="green"></div> | [grow:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/grow-50/) | [grow:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/grow-50/) | [grow:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/grow-50/) | [grow:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/grow-50/) | [grow:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/grow-50/) |
| <div class="dot-sm bg-helix opacity-50" aria-label="transparent"></div> | [helix:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/helix-50/) | [helix:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/helix-50/) | [helix:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/helix-50/) | [helix:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/helix-50/) | [helix:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/helix-50/) |
| <div class="dot-sm bg-focus opacity-50" aria-label="white"></div> | [focus:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/focus-50/) | [focus:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/focus-50/) | [focus:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/focus-50/) | [focus:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/focus-50/) | [focus:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/focus-50/) |
| <div class="dot-sm bg-enter opacity-50" aria-label="cyan"></div> | [enter:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/enter-50/) | [enter:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/enter-50/) | [enter:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/enter-50/) | [enter:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/enter-50/) | [enter:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/enter-50/) |
| <div class="dot-sm bg-flow opacity-50" aria-label="blue"></div> | [flow:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/flow-50/) | [flow:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/flow-50/) | [flow:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/flow-50/) | [flow:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/flow-50/) | [flow:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/flow-50/) |
| <div class="dot-sm bg-close opacity-50" aria-label="purple"></div> | [close:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/close-50/) | [close:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/close-50/) | [close:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/close-50/) | [close:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/close-50/) | [close:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/close-50/) |

#### Side B Nodes

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-sm bg-still opacity-50" aria-label="yellow"></div> | [still:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/still-50/) | [still:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/still-50/) | [still:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/still-50/) | [still:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/still-50/) | [still:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/still-50/) |
| <div class="dot-sm bg-void opacity-50" aria-label="red"></div> | [void:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/void-50/) | [void:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/void-50/) | [void:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/void-50/) | [void:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/void-50/) | [void:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/void-50/) |
| <div class="dot-sm bg-surge opacity-50" aria-label="magenta"></div> | [surge:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/surge-50/) | [surge:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/surge-50/) | [surge:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/surge-50/) | [surge:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/surge-50/) | [surge:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/surge-50/) |
| <div class="dot-sm bg-wither opacity-50" aria-label="green"></div> | [wither:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/wither-50/) | [wither:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/wither-50/) | [wither:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/wither-50/) | [wither:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/wither-50/) | [wither:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/wither-50/) |
| <div class="dot-sm bg-collapse opacity-50" aria-label="transparent"></div> | [collapse:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/collapse-50/) | [collapse:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/collapse-50/) | [collapse:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/collapse-50/) | [collapse:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/collapse-50/) | [collapse:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/collapse-50/) |
| <div class="dot-sm bg-haze opacity-50" aria-label="white"></div> | [haze:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/haze-50/) | [haze:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/haze-50/) | [haze:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/haze-50/) | [haze:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/haze-50/) | [haze:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/haze-50/) |
| <div class="dot-sm bg-drift opacity-50" aria-label="cyan"></div> | [drift:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/drift-50/) | [drift:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/drift-50/) | [drift:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/drift-50/) | [drift:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/drift-50/) | [drift:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/drift-50/) |
| <div class="dot-sm bg-abyss opacity-50" aria-label="blue"></div> | [abyss:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/abyss-50/) | [abyss:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/abyss-50/) | [abyss:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/abyss-50/) | [abyss:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/abyss-50/) | [abyss:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/abyss-50/) |
| <div class="dot-sm bg-fade opacity-50" aria-label="purple"></div> | [fade:50](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/slider/fade-50/) | [fade:50](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/slider/fade-50/) | [fade:50](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/slider/fade-50/) | [fade:50](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/slider/fade-50/) | [fade:50](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/slider/fade-50/) |

---

### Grid

Output when using the MTP Skill grid (`/mtp <column:row>`).  
`J:10` is the center coordinate and treated as a neutral node where MTP constraints are not emitted.

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-sm bg-still" aria-label="yellow"></div> | [A:1](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/a-1/) | [A:1](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/a-1/) | [A:1](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/a-1/) | [A:1](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/a-1/) | [A:1](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/a-1/) |
| <div class="dot-sm bg-wither" aria-label="green"></div> | [A:10](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/a-10/) | [A:10](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/a-10/) | [A:10](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/a-10/) | [A:10](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/a-10/) | [A:10](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/a-10/) |
| <div class="dot-sm bg-drift" aria-label="cyan"></div> | [A:19](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/a-19/) | [A:19](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/a-19/) | [A:19](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/a-19/) | [A:19](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/a-19/) | [A:19](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/a-19/) |
| <div class="dot-sm bg-open" aria-label="yellow"></div> | [D:4](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/d-4/) | [D:4](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/d-4/) | [D:4](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/d-4/) | [D:4](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/d-4/) | [D:4](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/d-4/) |
| <div class="dot-sm bg-grow" aria-label="green"></div> | [D:10](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/d-10/) | [D:10](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/d-10/) | [D:10](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/d-10/) | [D:10](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/d-10/) | [D:10](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/d-10/) |
| <div class="dot-sm bg-enter" aria-label="cyan"></div> | [D:16](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/d-16/) | [D:16](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/d-16/) | [D:16](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/d-16/) | [D:16](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/d-16/) | [D:16](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/d-16/) |
| <div class="dot-sm bg-void" aria-label="red"></div> | [J:1](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/j-1/) | [J:1](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/j-1/) | [J:1](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/j-1/) | [J:1](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/j-1/) | [J:1](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/j-1/) |
| <div class="dot-sm bg-power" aria-label="red"></div> | [J:4](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/j-4/) | [J:4](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/j-4/) | [J:4](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/j-4/) | [J:4](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/j-4/) | [J:4](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/j-4/) |
| <div class="dot-sm bg-helix" aria-label="transparent"></div> | [J:10](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/j-10/) | [J:10](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/j-10/) | [J:10](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/j-10/) | [J:10](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/j-10/) | [J:10](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/j-10/) |
| <div class="dot-sm bg-flow" aria-label="blue"></div> | [J:16](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/j-16/) | [J:16](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/j-16/) | [J:16](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/j-16/) | [J:16](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/j-16/) | [J:16](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/j-16/) |
| <div class="dot-sm bg-abyss" aria-label="blue"></div> | [J:19](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/j-19/) | [J:19](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/j-19/) | [J:19](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/j-19/) | [J:19](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/j-19/) | [J:19](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/j-19/) |
| <div class="dot-sm bg-return" aria-label="magenta"></div> | [P:4](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/p-4/) | [P:4](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/p-4/) | [P:4](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/p-4/) | [P:4](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/p-4/) | [P:4](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/p-4/) |
| <div class="dot-sm bg-focus" aria-label="white"></div> | [P:10](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/p-10/) | [P:10](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/p-10/) | [P:10](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/p-10/) | [P:10](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/p-10/) | [P:10](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/p-10/) |
| <div class="dot-sm bg-close" aria-label="purple"></div> | [P:16](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/p-16/) | [P:16](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/p-16/) | [P:16](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/p-16/) | [P:16](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/p-16/) | [P:16](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/p-16/) |
| <div class="dot-sm bg-surge" aria-label="magenta"></div> | [S:1](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/s-1/) | [S:1](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/s-1/) | [S:1](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/s-1/) | [S:1](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/s-1/) | [S:1](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/s-1/) |
| <div class="dot-sm bg-haze" aria-label="white"></div> | [S:10](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/s-10/) | [S:10](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/s-10/) | [S:10](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/s-10/) | [S:10](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/s-10/) | [S:10](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/s-10/) |
| <div class="dot-sm bg-fade" aria-label="purple"></div> | [S:19](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/grid/s-19/) | [S:19](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/grid/s-19/) | [S:19](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/grid/s-19/) | [S:19](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/grid/s-19/) | [S:19](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/grid/s-19/) |

---

### Preset

Output when using MTP Skill presets (`/mtp <preset>`).

| | ChatGPT 5.5 | Gemini 3.5 Flash | Composer 2.5 | Sonnet 4.6 | Manus 1.6 Lite |
| ----------------- | ----------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| <div class="dot-group"><div class="dot-sm bg-close" aria-label="purple"></div><div class="dot-sm bg-return" aria-label="magenta"></div></div> | [strategist](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/preset/strategist/) | [strategist](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/preset/strategist/) | [strategist](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/preset/strategist/) | [strategist](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/preset/strategist/) | [strategist](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/preset/strategist/) |
| <div class="dot-group"><div class="dot-sm bg-enter" aria-label="cyan"></div><div class="dot-sm bg-still" aria-label="yellow"></div></div> | [synthesizer](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/preset/synthesizer/) | [synthesizer](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/preset/synthesizer/) | [synthesizer](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/preset/synthesizer/) | [synthesizer](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/preset/synthesizer/) | [synthesizer](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/preset/synthesizer/) |
| <div class="dot-group"><div class="dot-sm bg-open" aria-label="yellow"></div><div class="dot-sm bg-drift" aria-label="cyan"></div></div> | [maverick](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/preset/maverick/) | [maverick](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/preset/maverick/) | [maverick](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/preset/maverick/) | [maverick](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/preset/maverick/) | [maverick](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/preset/maverick/) |
| <div class="dot-group"><div class="dot-sm bg-j13" aria-label="blue"></div><div class="dot-sm bg-grow" aria-label="green"></div></div> | [concierge](/comparisons/text-generation/04_alice-in-wonderland/gpt-5-5-medium_codex/preset/concierge/) | [concierge](/comparisons/text-generation/04_alice-in-wonderland/gemini-3-5-flash_antigravity/preset/concierge/) | [concierge](/comparisons/text-generation/04_alice-in-wonderland/composer-2-5_cursor-3-5/preset/concierge/) | [concierge](/comparisons/text-generation/04_alice-in-wonderland/sonnet-4-6_claude-ai/preset/concierge/) | [concierge](/comparisons/text-generation/04_alice-in-wonderland/manus-1-6-lite_manus-im/preset/concierge/) |
