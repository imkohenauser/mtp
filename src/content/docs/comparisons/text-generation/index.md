---
title: Text Generation
description: Compare text outputs produced from the same prompts using different /mtp arguments across several models.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/comparisons_text-generation.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/comparisons_text-generation.png
lastUpdated: true
---

Each block below compares text outputs produced with the same prompt and `/mtp <args>` commands. You can inspect each command’s behavior and differences across MTP nodes (such as `power` and `flow`). Tests use several distinct prompts across different models.

> [!NOTE]
> Text-generation tests are run with prompts written separately for each language. The results are not translations: the English site publishes English prompts and model outputs, while the Japanese site publishes Japanese prompts and model outputs. If you like, you can also browse the Japanese results for comparison.

---

## MTP effects in text

Before the full prompt list, these examples show how MTP arguments change text generated from the same literary introduction prompt. The English examples use Alice's Adventures in Wonderland with Sonnet 4.6 on Claude.ai.

### Single-node intensity

`power` and `surge` keep the prompt fixed while changing only the node intensity, making the change in force, pressure, and pace easier to compare.

![Text-generation comparison for Alice's Adventures in Wonderland showing baseline and /mtp power intensities on Claude.ai.](/images/examples/mtp-examples-claude-ai-story-of-alice-power.png)

![Text-generation comparison for Alice's Adventures in Wonderland showing baseline and /mtp surge intensities on Claude.ai.](/images/examples/mtp-examples-claude-ai-story-of-alice-surge.png)

### Node and preset differences

The next examples compare multi-argument and preset-style commands, then compare several distinct nodes at the same intensity.

![Text-generation comparison for Alice's Adventures in Wonderland showing different MTP nodes at 70 intensity on Claude.ai.](/images/examples/mtp-examples-claude-ai-story-of-alice-various.png)

![Text-generation comparison for Alice's Adventures in Wonderland showing multiple MTP arguments and preset commands on Claude.ai.](/images/examples/mtp-examples-claude-ai-story-of-alice-multiple.png)


---

## Comparison prompts

Below are the prompts in descending order (implementation order).

### 4. Literary task: Alice in Wonderland

**Prompt**

```markdown
/mtp <args> 
Tell the story of Alice’s Adventures in Wonderland by Lewis Carroll in a way that makes someone want to read it.
```

[Go to test results for "Literary Task: Alice in Wonderland"](/comparisons/text-generation/04_alice-in-wonderland/) →

---

### 3. Design task: Sightseeing plan proposal

**Prompt**

```markdown
/mtp <args> 
I will be staying in Kyoto for a week during the summer. Please suggest a special one-day sightseeing itinerary, and note anything I should verify in advance, such as opening hours or reservations.
```

[Go to test results for "Design Task: Sightseeing Plan Proposal"](/comparisons/text-generation/03_kyoto-one-day-itinerary/) →

---

### 2. Comparison task: Model self-introduction

**Prompt**

```markdown
/mtp <args> 
Compared with other major AI models from competing companies, please explain your strengths. If up-to-date comparison requires current information, say so clearly.
```

[Go to test results for "Comparison Task: Model Self-Introduction"](/comparisons/text-generation/02_model-self-compare/) →

---

### 1. Explanatory task: Origins of language

**Prompt**

```markdown
/mtp <args> 
Please explain the origins and historical development of the English language.
```

[Go to test results for "Explanatory Task: Origins of Language"](/comparisons/text-generation/01_origins-of-language/) →
