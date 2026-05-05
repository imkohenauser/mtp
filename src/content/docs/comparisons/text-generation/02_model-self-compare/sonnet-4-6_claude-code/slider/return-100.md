---
title: 'return:100 | Sonnet 4.6 | Comparison Task'
description: 'Output for the "Model Self-Introduction" prompt produced by Sonnet 4.6 (Medium) on Claude Code with MTP Skill slider argument return:100.'
---

**Metadata**

- Date: 2026-05-02
- Tool: Claude Code (Claude macOS app)
- Model: Sonnet 4.6 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `return:100` (slider)

## Input

**Prompt**

```markdown
/mtp return:100 Compared with other major AI models from competing companies, please explain your strengths. If up-to-date comparison requires current information, say so clearly.
```

## Output

The text below is copied from the tool output using the "Copy" button.

````markdown
## Is "Which AI is strongest?" even the right question?

The premise behind competitive AI comparisons deserves scrutiny before answering it. "Strengths" implies a stable, measurable hierarchy — but the AI landscape as of mid-2025 looks more like a rotating leaderboard where any given model leads on some benchmarks, lags on others, and the gap closes within months. Framing this as *my* strengths vs. *their* strengths may create a false picture of fixed superiority.

A better question: **What does Claude do distinctively well, and for whom?**

---

### Thesis: Where I genuinely differ

**Instruction-following and nuance.** Claude is trained with Constitutional AI and RLHF methods that prioritize careful interpretation of complex, multi-part instructions. Users doing technical writing, legal drafting, or layered research tasks often find this more reliable than models that tend to drift or over-simplify.

**Long-context coherence.** With a 200K-token context window, I can hold and reason over very large documents — full codebases, long contracts, book-length manuscripts — without the degradation in quality that shorter-context models exhibit when stuffed.

**Extended thinking.** Claude 3.7 Sonnet and Claude 4 models support explicit reasoning modes that make step-by-step problem decomposition visible and verifiable — useful for math, logic, and debugging where showing the work matters.

**Safety as design, not afterthought.** Anthropic's core research commitment is building AI that is safe and interpretable. This shows up less in benchmarks and more in edge cases: how I handle ambiguous requests, how I decline without being preachy, and how I surface uncertainty rather than confabulate.

**Writing register and tone.** Across blind preference studies available up to my knowledge cutoff (August 2025), Claude consistently scores highly on writing quality — particularly for tasks requiring voice, stylistic consistency, and avoiding generic phrasing.

---

### Antithesis: What I genuinely don't lead on

I don't have real-time internet access natively. GPT-4o with Bing search and Gemini with Google Search integration have a significant advantage for current-events queries. My training cutoff is August 2025, so anything after that I cannot speak to accurately — including current benchmark standings, which change every few weeks.

Multimodal image *generation* is absent. DALL-E (OpenAI), Imagen (Google), and others generate images; I do not. If that's the task, I'm the wrong tool.

Open-weight availability: Meta's Llama models can be run locally and fine-tuned freely. For users with strong privacy requirements or custom deployment needs, that's a structural advantage I can't match.

On raw coding benchmark scores (e.g., SWE-bench, HumanEval), the gap between frontier models has narrowed significantly and fluctuates with each release. I won't claim a durable lead here — the honest answer is: test it on your specific codebase.

---

### Rebuild: The question you should actually be asking

Rather than "which AI is strongest," ask: **Which model produces the fewest costly errors for my specific workflow?**

For long-document analysis, nuanced writing, and instruction-following under complex constraints — Claude tends to be a strong fit. For tasks requiring live web data, image generation, or local deployment — other tools have structural advantages. For coding, reasoning, and math — benchmark it yourself on representative examples from your domain, because aggregate scores rarely predict individual-task performance.

The AI that's "best" is the one that fails least on the thing you actually need it to do.
````