---
name: mtp
description: "MTP controls LLM output tone, structure, and exploration depth via /mtp (e.g. /mtp power:100, /mtp yellow:70, /mtp G:10, /mtp synthesizer, /mtp D:16 A:1). Invoked only when the user runs /mtp — do not infer MTP parameters; run the compiler."
argument-hint: "<node:intensity | axis-color:intensity | grid-coord | preset-name> ... (may appear anywhere in the message; multiple /mtp tokens are merged)"
allowed-tools: Bash(python3 *)
disable-model-invocation: true
version: "1.0.0"
---

# MTP

For installation and supported clients, see **README.md** in this directory.

When `/mtp` is invoked, **do not infer** MTP parameters from conversational wording; run the compiler and apply its **stdout** output per Step 2.

## Execution Steps

### Step 1: Extract `/mtp` tokens and run the compiler

Scan the entire user message for every occurrence of `/mtp <args>`. Each `/mtp` token extends to the next `/mtp` token or the end of the message, whichever comes first; the args are the MTP-recognizable tokens (sliders, grid coordinates, preset names, `help`, `list`) that immediately follow it. Collect all args, merge them in order into a single space-separated string, and pass the result to the compiler. The prompt is the remaining text after all `/mtp <args>` tokens are removed (preserving line breaks).

**The current directory must not be changed.** The script resolves its own paths. The compiler is run from the skill root (the directory containing this SKILL.md). The path to `scripts/mtp_compiler.py` is used relative to the skill root.

```bash
python3 scripts/mtp_compiler.py --args "[merged args string]"
```

*(If installed globally or in a different path, `mtp_compiler.py` is located within the skill directory and run via its path.)*

**Platform note:** The `allowed-tools` frontmatter uses Cursor's `Bash(python3 *)` syntax. **Claude Code:** use `${CLAUDE_SKILL_DIR}` and `$ARGUMENTS` instead of manual path resolution. Other agents (Codex, etc.) may use different tool names or permission models.

**Extraction examples:**

- `/mtp open:50 flow:30 Summarize this` → args: `"open:50 flow:30"`, prompt: `"Summarize this"`
- `Summarize this /mtp power:100` → args: `"power:100"`, prompt: `"Summarize this"`
- `Summarize this /mtp power:70 /mtp haze:30` → args: `"power:70 haze:30"`, prompt: `"Summarize this"`
- `/mtp D:16 Summarize this /mtp A:1` → args: `"D:16 A:1"`, prompt: `"Summarize this"`

Multi-line (args merged, `/mtp` lines removed from prompt):

```
Summarize this article.
/mtp power:70
Focus on the conclusion.
/mtp haze:30
```
→ args: `"power:70 haze:30"`, prompt: `"Summarize this article.\nFocus on the conclusion."`

**Special cases:**

- `/mtp help` → `--args "help"`; `/mtp help grid` → `--args "help grid"`; `/mtp list` → `--args "list"` — plain text to the user; no `<mtp_node_shot>` tags.
- `/mtp -h` → `--args="-h"` (dash-prefixed args must use `=` syntax to avoid shell flag parsing).

**Stream contract:** Constraints (`<mtp_node_shot>` XML) are written to **stdout** only. **stderr** carries a one-line human summary when active constraints remain after resolution, plus any warnings. It is not part of the constraint output and should not be parsed by the agent.

### Step 2: Apply the output constraints silently

Follow the `<mtp_node_shot>` XML from Step 1’s **stdout** strictly:

1. **Apply:** Interpret the rules as structural parameters for the current task (code, writing, Q&A, image prompts, etc.).
2. **Silent:** Do not describe the MTP step or meta-comment on tone.
3. **Output only:** Return only the task result; do not echo the constraint XML.

## Input formats

Token shapes the compiler accepts as args (merged as in Step 1):

| Format | Example | Description |
|--------|---------|-------------|
| Slider | `/mtp power:100` | node:intensity (0–100). Multiple allowed |
| Slider (negative) | `/mtp power:-30` | Negative value applies Side B (opposite pole) |
| Axis color | `/mtp yellow:70` | Same as Side A/B node on that axis (`yellow:70` = `open:70`); see `help sliders` |
| Grid coordinate | `/mtp G:10` | 19×19 grid, column:row (e.g. D:16); hyphen G-10 also accepted |
| Combined sliders | `/mtp open:50 flow:30` | Comma- or space-separated |
| Multi-grid | `/mtp D:16 A:1` | Multiple grid tokens (same style as preset expansions in `presets.yaml`) |
| Preset | `/mtp synthesizer` | Named combination of MTP commands |
| Multiple `/mtp` | `prompt /mtp power:70 /mtp haze:30` | Each `/mtp` collected; args merged in order |

Slider names, axis colors, presets, and grid columns are **case-insensitive** (e.g. `FLOW:70` ≡ `flow:70`, `g:10` ≡ `G:10`).

## Runtime semantics

- Multiple `/mtp` segments are merged in source order before parsing.
- Presets expand first, then the expanded token stream is parsed.
- If multiple tokens target the same axis, the **last token wins**.
- Different axes combine normally.
- Invalid or malformed tokens are ignored with warnings on **stderr**.
- Neutral no-op tokens such as `power:0`, `yellow:0`, `J:10`, and `J-10` are valid, produce no active constraint, and do not emit warnings.
- If no active constraints remain after parsing and conflict resolution, the compiler still returns an empty `<mtp_node_shot>` envelope on **stdout** for compatibility.

## Background

Constraints come from **scripted** extraction over `nodes/` and intensity tiers—not from guessing what “Power” or “Flow” should mean in chat. Run the compiler; do not override its output with improvised tone rules.

For usage examples and expected behavior, see `USAGE.md`. Help text: `references/help_main.txt`, `help_sliders.txt`, `help_grid.txt`. Presets: `references/presets.yaml`.

## Node authoring rules

Node Markdown under `nodes/` is parsed by simple frontmatter and heading scanners. The format is intentionally narrow and should be edited conservatively.

- Frontmatter must appear first and use one `key: value` entry per line.
- Supported frontmatter values are plain strings, optionally wrapped in double quotes.
- Multi-line values, nested YAML, lists, and other complex YAML features are not supported.
- Required frontmatter keys are `axis`, `node_positive`, and `node_negative`.
- `description` is optional but recommended.
- The body must keep the section structure `## Side A`, `## Side B`, then `### Low`, `### Mid`, `### High` within each side.
- Constraint extraction is cumulative. `High` implies `Low + Mid + High`, and `Mid` implies `Low + Mid`.
- Higher tiers should strengthen or override lower tiers without contradicting them.
