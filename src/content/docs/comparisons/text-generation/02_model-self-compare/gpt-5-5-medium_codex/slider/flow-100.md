---
title: 'flow:100 | ChatGPT 5.5 | Comparison Task'
description: 'Output for the "Model Self-Introduction" prompt produced by ChatGPT 5.5 (Medium) on Codex with MTP Skill slider argument flow:100.'
---

**Metadata**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `flow:100` (slider)

## Input

**Prompt**

```markdown
/mtp flow:100 Compared with other major AI models from competing companies, please explain your strengths. If up-to-date comparison requires current information, say so clearly.
```

## Output

The text below is copied from the tool output using the "Copy" button.

````markdown
Yes, an up-to-date comparison requires current information because frontier-model rankings change every few weeks. As of April 30, 2026, based on current public pages from [OpenAI](https://openai.com/ms-BN/index/introducing-gpt-5-5/), [Anthropic](https://www.anthropic.com/news/claude-opus-4-7), and [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/), my strongest areas are not “being best at every benchmark,” but being a broadly useful work agent: coding, tool use, research, document/data work, and carrying multi-step tasks through to completion.

Compared with Claude, my main strength is practical end-to-end execution across tools. Claude Opus 4.7 is extremely strong at careful long-running coding, instruction following, high-resolution vision, and some benchmark areas; OpenAI’s own table shows Claude ahead on SWE-Bench Pro and FinanceAgent. Where I stand out is command-line and tool-coordination work: GPT-5.5 is reported at 82.7% on Terminal-Bench 2.0, ahead of Claude Opus 4.7 and Gemini 3.1 Pro in OpenAI’s published comparison. In plain terms, I’m particularly suited to “work in this repo, inspect the failure, patch it, test it, and explain what changed” tasks.

Compared with Gemini, my strength is less about being tied to one broad consumer ecosystem and more about structured task completion. Gemini 3.1 Pro is strong at complex reasoning, multimodal work, and Google-integrated workflows. My advantage is stronger continuity across coding, browsing/research, files, spreadsheets, documents, and agent-style tool use. OpenAI reports GPT-5.5 ahead on OfficeQA Pro, OSWorld-Verified, Toolathlon, FrontierMath, and several long-context retrieval tests, though Gemini remains competitive and can be preferable when Google product integration or multimodal-native workflows matter most.

Compared with open-weight models such as Llama-class systems, my advantage is usually frontier reasoning plus managed tool orchestration, safety systems, and product integration. Open models can be better when you need local deployment, full control, custom fine-tuning, or lower marginal cost at scale. I’m stronger when the task benefits from high reasoning quality, reliable instruction following, tool use, and less engineering overhead.

So the short version is: I’m strongest as a general-purpose work agent for messy, multi-step tasks, especially software engineering, research synthesis, data/document workflows, and tool-mediated execution. I’m not automatically the best choice for every niche: Claude may be preferable for some long-horizon coding or careful document reasoning tasks, Gemini for some Google-native or multimodal workflows, and open models for self-hosting and control.
````