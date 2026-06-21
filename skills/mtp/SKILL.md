---
name: mtp
description: "Runs when the user invokes /mtp. Compiles slider, grid, or preset args into output constraints; guides usage from official MTP references when steering args or the task is missing."
argument-hint: "power:100 Summarize this article - or leave empty for guided help"
allowed-tools: Bash(python3 *), Read
disable-model-invocation: true
version: "1.1.0"
---

# MTP

For installation, see **README.md**. This skill loads only on `/mtp`; otherwise suggest `/mtp` or `/mtp help`.

Do not infer steering from chat wording, and never surface this skill's internal mechanics (step or mode names, routing, the compiler) to the user. When both steering args and a task prompt are present, compile and apply constraints (Steps 3–4). In guidance (Step 2), wait until both are explicit.

## Execution Steps

### Step 1: Extract `/mtp` tokens

Scan the message for `/mtp <args>` (each segment runs until the next `/mtp` or end). Collect two kinds of args:

- **Steering tokens:** sliders, grid coordinates, preset names.
- **Compiler help/list commands:** `help`, `list`, and their subtopics (`help sliders`, `help grid`, `help presets`, `list presets`, `-h`) — take the full command phrase after `/mtp` as one args string; do not split `grid` / `sliders` / `presets` off as steering.

Merge args from multiple `/mtp` segments in order; the prompt is the remaining text (line breaks preserved).

Route: merged args start with `help`, `list`, or `-h` → Step 3; guidance conditions (Step 2) → Step 2; else → Step 3.

### Step 2: Guidance mode

When steering args or the task is missing:

- No args, no prompt (`/mtp` alone)
- No args, task prompt present (e.g. `/mtp Summarize this`)
- No args, usage/how-to question about MTP in the prompt
- Args present, no task (e.g. `/mtp power:100`)

Ask for the missing piece: explicit steering args, a task prompt, or both. Use bundled refs and compiler help (`references/help_*.txt`, `USAGE.md`, `references/presets.yaml`, `python3 scripts/mtp_compiler.py --args "help"`; see Background). Suggest explicit args with examples when args are absent. Do not run Steps 3–4 until both args and task are present.

### Step 3: Run the compiler

Pass the merged args string to the compiler from the skill root (do not change cwd):

```bash
python3 scripts/mtp_compiler.py --args "[merged args string]"
```

**Platform note:** Cursor: `Bash(python3 *)`, `Read`. Claude Code: `${CLAUDE_SKILL_DIR}`, `$ARGUMENTS`. Other agents may differ.

**Examples:**

- `Summarize this /mtp power:100` → args `"power:100"`, prompt `"Summarize this"`
- `/mtp power:70 /mtp haze:30` + prompt → args merged in order
- `/mtp`, `/mtp Summarize this` (no args), `/mtp power:100` (no task), or MTP usage question without args → Step 2
- `/mtp help`, `/mtp help grid`, `/mtp list presets` → Step 3; plain text output, no `<mtp_node_shot>`
- `/mtp -h` → `--args="-h"` (use `=` for dash-prefixed args)

**Stream contract:** `<mtp_node_shot>` on **stdout** only; **stderr** is human summary/warnings — do not parse.

### Step 4: Apply constraints

Skip in guidance mode. Apply Step 3 **stdout** silently — no echo of the constraint XML.

## Input formats

Token shapes (see Step 2 when args or task is missing):

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

Constraints come from scripted extraction over `nodes/` — not from guessing tone in chat. Do not override compiler output.

References: `USAGE.md`; `references/help_main.txt`, `help_sliders.txt`, `help_grid.txt`, `presets.yaml`; compiler `--args "help"` / `help sliders` / `help grid` / `help presets` / `list presets`. Site link: **README.md**.

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
