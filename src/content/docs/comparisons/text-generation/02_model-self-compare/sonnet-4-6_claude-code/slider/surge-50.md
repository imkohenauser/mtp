---
title: 'surge:50 | Sonnet 4.6 | Comparison Task'
description: 'Output for the "Model Self-Introduction" prompt produced by Sonnet 4.6 (Medium) on Claude Code with MTP Skill slider argument surge:50.'
---

**Metadata**

- Date: 2026-05-02
- Tool: Claude Code (Claude macOS app)
- Model: Sonnet 4.6 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `surge:50` (slider)

## Input

**Prompt**

```markdown
/mtp surge:50 Compared with other major AI models from competing companies, please explain your strengths. If up-to-date comparison requires current information, say so clearly.
```

## Output

The text below is copied from the tool output using the "Copy" button.

````markdown
My knowledge cutoff is August 2025, so direct comparisons to the very latest model releases from OpenAI, Google, Meta, or Mistral may be incomplete — I'll flag that clearly where it applies.

---

**Where Claude tends to lead:**

**Extended context and long-document work.** Claude handles up to 200K tokens natively. Drop in an entire codebase, a legal contract, a technical manual — I read it all, locate the relevant section, and reason across the full span. GPT-4o and Gemini have extended context too, but retrieval fidelity at long ranges has historically been weaker.

**Instruction-following and nuance.** I track complex, multi-part instructions with fewer instruction-forgetting failures. I'm less likely to collapse a nuanced "write it formally but not stuffy" into generic corporate tone.

**Honest refusal behavior.** I decline things I genuinely shouldn't do, but I don't over-refuse. I won't help with malware. I will help with a dark short story. That calibration is something Anthropic has worked hard to get right.

**Code quality.** I write idiomatic, reasoned code — not just syntactically correct code. I can explain *why* a design choice is made, trace through subtle bugs, and refactor with intent.

**Reasoning depth.** For tasks requiring multi-step inference — legal analysis, research synthesis, planning under constraints — I typically sustain coherence across more steps than smaller models.

---

**Where the picture is honestly mixed or evolving (as of Aug 2025):**

- GPT-4o and Gemini 1.5 Pro are strong competitors on speed and multimodal tasks. Image understanding is competitive.
- For real-time web search, I don't have live access by default — Perplexity and GPT-4o with browsing beat me there.
- Cost. Haiku is fast and cheap; GPT-4o-mini and Gemini Flash occupy the same tier. No clear winner purely on price-per-token.
- Post-August 2025 model releases (GPT-5, Gemini 2.x, etc.) — I have no reliable data. The landscape may have shifted.

---

**The honest one-liner:** Claude is strongest when the task requires careful reading, dense reasoning, and getting the nuance of instructions right. Raw speed benchmarks fluctuate. This is where the gap is real.
````