---
title: 'focus:100 | ChatGPT 5.5 | Comparison Task'
description: 'Output for the "Model Self-Introduction" prompt produced by ChatGPT 5.5 (Medium) on Codex with MTP Skill slider argument focus:100.'
---

**Metadata**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `focus:100` (slider)

## Input

**Prompt**

```markdown
/mtp focus:100 Compared with other major AI models from competing companies, please explain your strengths. If up-to-date comparison requires current information, say so clearly.
```

## Output

The text below is copied from the tool output using the "Copy" button.

````markdown
Yes: an up-to-date cross-model comparison requires current information. Model rankings change quickly, and public benchmarks are often vendor-run, harness-dependent, and not directly comparable. As of April 30, 2026, the defensible comparison is by task profile, not a universal “best model” claim.

My main strengths versus other major AI models are:

| Strength | What it means in practice |
|---|---|
| **Agentic software engineering** | I am strongest when I can inspect a repo, edit files, run commands, test, debug failures, and iterate until the task is actually done. |
| **Long-running coding work** | Codex models are optimized for extended engineering tasks: refactors, migrations, code review, test repair, and multi-step implementation. OpenAI reports GPT-5.3-Codex at **77.3% on Terminal-Bench 2.0** in its Codex harness. |
| **Tool-grounded execution** | I work well when answers can be checked against files, terminal output, tests, browsers, documents, spreadsheets, or APIs rather than produced from memory alone. |
| **Pragmatic code review and debugging** | I am tuned to look for concrete failure modes: regressions, edge cases, missing tests, unsafe operations, and mismatches with existing code patterns. |
| **Interactive collaboration** | A key advantage is not just raw answer quality, but steering: you can redirect me mid-task, ask for narrower changes, or have me continue from the current workspace state. |
| **General professional work on a computer** | Beyond code, I can help produce and verify documents, spreadsheets, slides, research summaries, and workflow outputs when tools are available. |

Compared with **Claude**, Anthropic’s latest Opus line is also very strong for long-context coding, agent workflows, careful instruction-following, and enterprise tasks; Anthropic advertises Claude Opus 4.7 with a **1M context window** and strong coding/agent positioning. Compared with **Gemini**, Google’s Gemini 3 family emphasizes multimodality, very long context, reasoning, and strong benchmark results across text, image, video, audio, and coding. Those are real competing strengths.

So the concise answer is: my strongest position is **end-to-end, tool-using professional work, especially software engineering in a real workspace**. I should be judged less as a chatbot giving isolated answers and more as an agent that can read the environment, make changes, run verification, and report exactly what happened.

Sources: [OpenAI GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex), [OpenAI GPT-5.5](https://openai.com/ms-BN/index/introducing-gpt-5-5/), [Anthropic Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7), [Google Gemini 3](https://deepmind.google/models/gemini/).
````