---
title: 'enter:100 | Sonnet 4.6 | Comparison Task'
description: 'Output for the "Model Self-Introduction" prompt produced by Sonnet 4.6 (Medium) on Claude Code with MTP Skill slider argument enter:100.'
---

**Metadata**

- Date: 2026-05-02
- Tool: Claude Code (Claude macOS app)
- Model: Sonnet 4.6 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `enter:100` (slider)

## Input

**Prompt**

```markdown
/mtp enter:100 Compared with other major AI models from competing companies, please explain your strengths. If up-to-date comparison requires current information, say so clearly.
```

## Output

The text below is copied from the tool output using the "Copy" button.

````markdown
**Topic:** My strengths as Claude (Anthropic) compared to major competing AI models. I'll cover three areas: ① reasoning and nuance, ② safety and alignment, ③ knowledge and context handling. Note upfront: some competitive comparisons require current benchmarks I may not have, and I'll flag those.

---

**Assumptions and scope**
- Competitors referenced: GPT-4o / o-series (OpenAI), Gemini 1.5/2.x (Google), Llama 3/4 (Meta), Mistral Large.
- "Strengths" means consistently observed advantages in capability, design philosophy, or user experience — not cherry-picked benchmarks.
- Knowledge cutoff is August 2025; precise benchmark standings as of today (May 2026) may have shifted.

---

## ① Reasoning, nuance, and instruction-following

Claude is widely noted for its ability to follow complex, multi-part instructions with high fidelity — staying in scope, respecting constraints, and not drifting mid-response. Particularly in long-context tasks (up to 200K tokens in Claude 3.x), I maintain coherence across a document better than earlier GPT-4 versions did; whether this gap persists vs. GPT-4o or o3 in mid-2026 would require current evals.

Extended thinking (Claude's visible chain-of-thought feature) is competitive with OpenAI's o-series reasoning models for math, code, and multi-step logic — though o3 may lead on olympiad-level math as of my cutoff.

## ② Safety, alignment, and honest refusals

This is a deliberate, structural advantage. Anthropic's Constitutional AI and RLHF pipeline are explicitly oriented around:
- **Calibrated honesty** — I decline tasks I'm uncertain about rather than confabulating confidently.
- **Nuanced refusals** — I distinguish clearly between harmful requests and legitimate-but-sensitive ones, avoiding both over-refusal and under-refusal. Many users switching from other models cite fewer unnecessary blocks.
- **Transparency** — I state my limitations and uncertainty rather than hedging invisibly.

Google's Gemini and OpenAI's models have improved on safety, but Anthropic's entire research mission centers on it, which shapes how the model behaves at a fundamental level rather than as a layer on top.

## ③ Writing quality, tone control, and long-form output

Claude consistently ranks highly in independent evaluations of prose quality — coherent structure, appropriate register, and reduced "AI voice" patterns (filler phrases, hollow affirmations). For professional writing, documents, and coding tasks requiring readable output, this is a meaningful practical advantage.

---

**Where I have less certainty (requires current data)**
- Exact benchmark rankings vs. GPT-4o, Gemini 2.x, and Llama 4 as of May 2026 — these move quickly.
- Multimodal image/video tasks: Gemini's native multimodality is a genuine strength; the current gap vs. Claude would need up-to-date evals to quantify.
- Speed and cost per token at scale — infrastructure competition changes frequently.

For current head-to-head benchmark data, sources like LMSYS Chatbot Arena (live), Hugging Face Open LLM Leaderboard, or Anthropic's model card would give you the most accurate picture.
````