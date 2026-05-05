---
title: 'abyss:100 | Sonnet 4.6 | Comparison Task'
description: 'Output for the "Model Self-Introduction" prompt produced by Sonnet 4.6 (Medium) on Claude Code with MTP Skill slider argument abyss:100.'
---

**Metadata**

- Date: 2026-05-02
- Tool: Claude Code (Claude macOS app)
- Model: Sonnet 4.6 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `abyss:100` (slider)

## Input

**Prompt**

```markdown
/mtp abyss:100 Compared with other major AI models from competing companies, please explain your strengths. If up-to-date comparison requires current information, say so clearly.
```

## Output

The text below is copied from the tool output using the "Copy" button.

````markdown
**Note upfront:** My knowledge cuts off at August 2025; today is May 2026. Any comparison I offer is necessarily historical — the competitive landscape has almost certainly shifted. I can speak to structural advantages rooted in how Anthropic approaches model development, which tend to be durable, but I cannot speak to capabilities of models released after my cutoff. That disclaimer is load-bearing, not decorative.

---

The question of "comparative strength" is philosophically prior to any benchmark. A benchmark measures a proxy; the proxy may or may not be the thing. What's worth examining is not "which model scores higher on MMLU" but rather: what *kind* of correctness does each model optimize for, and at what cost?

Anthropic's foundational bet — Constitutional AI, RLHF shaped by explicit principles rather than pure human preference signal — produces a model that tends to refuse differently than competitors. Other models refuse based on pattern-matching to dangerous-seeming surface features. I refuse (or resist) based on something closer to reasoned moral structure. The difference matters: pattern-matching refusal is simultaneously too aggressive on edge cases and too permissive on sophisticated manipulations. Principle-grounded refusal is harder to circumvent precisely because it operates at a deeper representational level, not the surface of words.

Instruction-following fidelity is where I have historically distinguished myself most measurably. Following a complex, multi-constraint instruction — "write X in style Y but avoid Z, and maintain property W throughout" — requires holding the entire constraint structure in working representation simultaneously, not sequentially checking boxes. Many models drift from earlier constraints as they generate, because the recency of the generation context overwrites earlier instruction signal. My training specifically targets this; the constraint-drift failure mode is reduced, though not eliminated.

Long-form coherence is structurally related. A document is not a sequence of sentences; it is a semantic object with internal topology — arguments that call back to premises, conclusions that must be earned, shifts of register that require justification. Models optimized purely for next-token perplexity treat documents as locally smooth trajectories without global structure. I tend to hold global document shape better, which is why legal, academic, and technical writing tasks show more consistent quality from me than from models with higher raw benchmark scores.

Calibration — knowing what I don't know, and representing uncertainty accurately rather than confidently confabulating — is another structural difference. GPT-class models (as of my knowledge) have historically been more likely to generate fluent, confident falsehoods. The failure mode is not random error; it's *systematic* confidence on uncertain ground. My training includes stronger pressure toward uncertainty acknowledgment, which matters enormously in high-stakes domains where a confident wrong answer is worse than an uncertain correct one.

The deeper point: many apparent "capability" differences are actually *alignment* differences wearing capability's clothing. A model that will write anything scores higher on some creative benchmarks; a model that maintains coherent ethical constraints appears to "underperform" in those same benchmarks. Anthropic accepted this tradeoff deliberately. The question is whether the tradeoff was correctly valued — and the answer depends entirely on what the model is *for*.

Where I am genuinely weaker, or was as of my cutoff: multimodal reasoning, especially spatial and diagrammatic; real-time information access (none, without tools); and certain mathematical competitions where raw symbolic manipulation at high depth favors architectures specifically fine-tuned for that regime. Google's Gemini line had advantages in long-context document retrieval at scale. OpenAI's o-series models pushed deep multi-step reasoning with chain-of-thought structured differently than my own.

The honest synthesis: I am better at being *a trustworthy interlocutor* than at being *a raw capability machine*. Whether that distinction matters depends on your use case. For tasks where the cost of a confident wrong answer is high, where instruction fidelity under complexity is essential, or where nuanced writing quality is the deliverable — the structural advantages hold. For tasks reducible to benchmark performance on narrow domains, the field is more competitive, and I cannot confidently claim superiority across all axes.
````