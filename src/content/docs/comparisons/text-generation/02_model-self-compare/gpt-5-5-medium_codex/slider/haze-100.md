---
title: 'haze:100 | ChatGPT 5.5 | Comparison Task'
description: 'Output for the "Model Self-Introduction" prompt produced by ChatGPT 5.5 (Medium) on Codex with MTP Skill slider argument haze:100.'
---

**Metadata**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `haze:100` (slider)

## Input

**Prompt**

```markdown
/mtp haze:100 Compared with other major AI models from competing companies, please explain your strengths. If up-to-date comparison requires current information, say so clearly.
```

## Output

The text below is copied from the tool output using the "Copy" button.

````markdown
Up-to-date comparison does require current information. Model lineups, prices, context windows, tool support, and benchmark results change quickly; even official docs can differ by endpoint or product surface. I checked current official model docs for OpenAI, Anthropic, and Google before answering.

Compared with other major AI models, my strengths tend to sit less in a single benchmark crown and more in the working shape of the system:

I am strong at **coding and agentic software work**: reading a codebase, making scoped edits, running commands, checking failures, and carrying a task through implementation rather than only describing what to do. OpenAI’s current model docs position `gpt-5.5` as the flagship for complex reasoning and coding, with tool support including functions, web search, file search, and computer use.

I am also strong at **long, practical reasoning under constraints**: keeping track of instructions, preserving user intent, avoiding unrelated edits, and using tools when the answer depends on files, current facts, or verification. That matters in real work because the question is rarely just “what is the answer?” It is often “what can be changed safely?”

Relative to Claude, the difference often feels like Claude may be especially graceful in prose, long-context reading, and careful dialogue; Anthropic describes Claude Sonnet 4.5 as strong for agents and coding, with Opus 4.1 for specialized reasoning. My edge is often in the surrounding execution loop: coding workflow, tool orchestration, structured edits, and direct integration with developer environments.

Relative to Gemini, Google’s models are very strong around multimodality, huge context, Google ecosystem grounding, and media-oriented capabilities. My edge is usually the software-engineering posture: precise code changes, repo navigation, command-line verification, and turning ambiguous requests into concrete artifacts.

So, in plain terms: my strengths are **developer work, tool use, structured reasoning, instruction following, and end-to-end task completion**. The exact ranking against Claude, Gemini, or others would need fresh benchmark data and workload-specific testing, not a static claim.

Sources: [OpenAI models](https://developers.openai.com/api/docs/models), [Anthropic Claude models](https://docs.claude.com/en/docs/about-claude/models/overview), [Google Vertex AI models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models).
````