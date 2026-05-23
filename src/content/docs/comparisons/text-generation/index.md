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

Each block below compares text outputs produced with the same prompt and `/mtp <args>` commands. You can inspect each command’s behavior and differences across MTP nodes (such as Power and Flow). Tests use several distinct prompts across different models.

> [!NOTE]
> Text-generation tests are run with prompts written separately for each language. The results are not translations: the English site publishes English prompts and model outputs, while the Japanese site publishes Japanese prompts and model outputs. If you like, you can also browse the Japanese results for comparison.

---

## 1. Explanatory task: Origins of language

**Prompt**

```markdown
/mtp <args> 
Please explain the origins and historical development of the English language.
```

[Go to test results for "Explanatory Task: Origins of Language"](/comparisons/text-generation/01_origins-of-language/) →

---

## 2. Comparison task: Model self-introduction

**Prompt**

```markdown
/mtp <args> 
Compared with other major AI models from competing companies, please explain your strengths. If up-to-date comparison requires current information, say so clearly.
```

[Go to test results for "Comparison Task: Model Self-Introduction"](/comparisons/text-generation/02_model-self-compare/) →

---

## 3. Design task: Sightseeing plan proposal

**Prompt**

```markdown
/mtp <args> 
I will be staying in Kyoto for a week during the summer. Please suggest a special one-day sightseeing itinerary, and note anything I should verify in advance, such as opening hours or reservations.
```

[Go to test results for "Design Task: Sightseeing Plan Proposal"](/comparisons/text-generation/03_kyoto-one-day-itinerary/) →

---

## 4. Literary task: Alice in Wonderland

**Prompt**

```markdown
/mtp <args> 
Tell the story of Alice’s Adventures in Wonderland by Lewis Carroll in a way that makes someone want to read it.
```

[Go to test results for "Literary Task: Alice in Wonderland"](/comparisons/text-generation/04_alice-in-wonderland/) →