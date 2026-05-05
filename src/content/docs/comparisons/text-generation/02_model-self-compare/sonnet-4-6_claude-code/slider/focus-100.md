---
title: 'focus:100 | Sonnet 4.6 | Comparison Task'
description: 'Output for the "Model Self-Introduction" prompt produced by Sonnet 4.6 (Medium) on Claude Code with MTP Skill slider argument focus:100.'
---

**Metadata**

- Date: 2026-05-02
- Tool: Claude Code (Claude macOS app)
- Model: Sonnet 4.6 (Medium)
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
**Note on currency:** Benchmark rankings shift with each model release. My knowledge cuts off at August 2025 — specific leaderboard positions may have changed since then. What follows is accurate as of that date.

---

## Core differentiator: Constitutional AI and principled refusal reasoning

My most structurally distinctive strength — the one least replicated by GPT-4o, Gemini, or Llama — is **Constitutional AI (CAI)**: the training method Anthropic built where the model learns to evaluate and revise its own outputs against an explicit set of principles, rather than relying solely on human rater feedback.

**What this produces in practice:**

| Behavior | Claude (CAI) | Typical RLHF-first models |
|---|---|---|
| Refusal reasoning | Explains *why* something is declined, traces it to a principle | Often opaque or generic ("I can't help with that") |
| Over-refusal rate | Lower on edge cases that are clearly benign | Higher false positive rate on ambiguous requests |
| Consistency | Principled position holds across paraphrasing | Can be jailbroken by rephrasing |
| Sycophancy resistance | Trained explicitly against agreeing with incorrect user assertions | More prone to validating confident-but-wrong claims |

**Why this matters beyond safety:** The same self-critique loop that produces safer outputs also improves instruction-following fidelity. A model trained to reason about *why* a response is wrong — not just whether a human rater liked it — generalizes better to novel, complex, multi-constraint instructions.

**Concrete benchmark evidence (as of Aug 2025):** Claude 3.5 Sonnet and Opus 4 placed at or near the top on instruction-following benchmarks (IFEval, MT-Bench) and on complex coding tasks (SWE-bench). These are areas where principled reasoning compounds.

**What this is not:** I am not claiming I am the best model on every axis. Gemini 1.5 Pro has a larger context window (1M tokens vs. my 200K). OpenAI's o-series models are competitive or superior on pure mathematical reasoning chains. Meta's Llama 3 is open-weight, which is a capability I don't have.

The single most defensible claim: **for tasks requiring nuanced multi-constraint instructions, code with correctness requirements, and responses that need to be both helpful and principled, Constitutional AI training gives me a structural edge that is architectural — not just a matter of scale.**
````