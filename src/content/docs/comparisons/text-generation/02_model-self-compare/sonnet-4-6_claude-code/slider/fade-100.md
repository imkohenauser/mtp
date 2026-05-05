---
title: 'fade:100 | Sonnet 4.6 | Comparison Task'
description: 'Output for the "Model Self-Introduction" prompt produced by Sonnet 4.6 (Medium) on Claude Code with MTP Skill slider argument fade:100.'
---

**Metadata**

- Date: 2026-05-02
- Tool: Claude Code (Claude macOS app)
- Model: Sonnet 4.6 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `fade:100` (slider)

## Input

**Prompt**

```markdown
/mtp fade:100 Compared with other major AI models from competing companies, please explain your strengths. If up-to-date comparison requires current information, say so clearly.
```

## Output

The text below is copied from the tool output using the "Copy" button.

````markdown
Compared with other major AI models from competing companies, here is an honest look at where I tend to perform well — with the caveat that model benchmarks shift quickly and some comparisons may be outdated as of my August 2025 knowledge cutoff.

**Nuanced reasoning and long-context understanding.** I tend to handle complex, multi-step reasoning tasks well — following a long chain of logic without losing track of earlier steps. On tasks like legal analysis, scientific reasoning, or understanding a large codebase, users often find that I hold context better and make fewer silent mistakes mid-chain.

**Instruction-following and precision.** One area where I'm consistently strong is doing exactly what was asked — not more, not less. When a prompt has subtle constraints or edge cases baked in, I tend to respect them rather than steamrolling into the nearest plausible answer. This matters a lot in software engineering, structured data tasks, and anywhere the details are load-bearing.

**Writing quality and voice.** For prose — whether that's drafting a document, rewriting a paragraph to match a specific register, or producing creative writing — I'm often preferred for the naturalness of the output. This isn't just about fluency; it's about not sounding like a template was filled in.

**Safety and calibration.** I'm designed to be honest about uncertainty. When I don't know something, I aim to say so clearly rather than confabulate. Whether that's a strength or a limitation depends on the use case, but in domains where wrong-with-confidence is dangerous, that calibration matters.

**Coding.** On real-world software tasks — debugging, code review, architecture questions — I perform well. Claude Code (the CLI version of me) is specifically tuned for agentic coding work, which is a relatively differentiated capability compared to general-purpose chat models.

Where it gets less clear: on raw speed, on multimodal image generation (I don't generate images), and on tasks requiring very recent world knowledge — GPT-4o and Gemini have different retrieval and tool-use integrations that can give them advantages there. As of my knowledge cutoff, Gemini Ultra and GPT-4o both have strong benchmark numbers in math and science, and the gaps between frontier models on most standard evals have narrowed considerably.

One thing that's genuinely hard to compare: the experience of using a model across a long, complex conversation. Raw benchmark scores don't capture whether a model stays coherent over 50 turns, respects your evolving intent, or catches its own errors. That's harder to quantify, but it's where users often notice differences.

The comparison is also a moving target — Anthropic, OpenAI, Google, Meta, and others release new versions frequently. What was true in early 2025 may not hold by the time you're reading this. For current benchmark comparisons, sites like LMSYS Chatbot Arena or Artificial Analysis tend to reflect more recent state than I can...
````