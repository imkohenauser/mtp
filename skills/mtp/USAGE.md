# Usage

Test prompts, compiler checks, and expected behavior for the MTP skill.

## Test prompts

Realistic test cases based on actual user input. Use for both compiler script checks and chat behavior verification.

### 1. Single slider

**Input:**
```
/mtp power:100 Summarize this article
```

**Expected behavior:**
- Red axis High (intensity=100): conclusion-first, assertive structure
- No meta-mention of constraints

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "power:100"
```

---

### 2. Grid coordinate (outer frame — maximum Side B)

**Input:**
```
/mtp A:1 Talk about the future of AI
```

**Expected behavior:**
- Yellow axis Side B (intensity=100): outer frame = maximum Side B
- Low+Mid+High all applied for Side B (still)
- Minimal output, no new suggestions, fixed state

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "A:1"
```

---

### 3. Named preset (`presets.yaml`)

**Input:**
```
/mtp strategist Summarize this article
```

**Expected behavior:**
- `strategist` expands per `references/presets.yaml` (e.g. `P:16 P:4`) before parsing
- No meta-mention of constraints

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "strategist"
```

---

### 4. Multi-grid (explicit expansion)

**Input:**
```
/mtp D:16 A:1 Summarize this article
```

**Expected behavior:**
- Same token sequence as the `synthesizer` preset in `references/presets.yaml`
- No meta-mention of constraints

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "D:16 A:1"
```

---

### 5. Side B negative (high-intensity minimalism)

**Input:**
```
/mtp void:80 Review this code
```

**Expected behavior:**
- Red axis Side B High (intensity=80): minimal output
- No greetings, preamble, or closing
- Only findings, in minimal sentences

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "void:80"
```

---

### 6. Axis color slider (alias for Side A / Side B nodes)

**Input:**
```
/mtp yellow:70 Summarize this in fewer words
```

**Expected behavior:**
- Same linear mapping as `/mtp open:70` on the Yellow axis (Side A)
- Negative values use the Side B node on that axis (e.g. `yellow:-70` ≡ `still:70`)

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "yellow:70"
```

---

### 7. Preset (named expansion from presets.yaml)

**Input:**
```
/mtp synthesizer Outline the key points
```

**Expected behavior:**
- Preset expands to the MTP command string defined in `references/presets.yaml` (e.g. grid coordinates)

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "synthesizer"
```

---

### 8. `/mtp` at the end of the message

**Input:**
```
Summarize this article /mtp power:100
```

**Expected behavior:**
- Args extracted: `"power:100"`, prompt: `"Summarize this article"`
- Red axis High (intensity=100): conclusion-first, assertive structure
- No meta-mention of constraints

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "power:100"
```

---

### 9. `/mtp` in the middle of the message

**Input:**
```
Summarize /mtp G:10 this article
```

**Expected behavior:**
- Args extracted: `"G:10"`, prompt: `"Summarize this article"`
- Grid coordinate G:10 applied

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "G:10"
```

---

### 10. Multiple `/mtp` tokens (merged in order)

**Input:**
```
Summarize this /mtp power:70 /mtp haze:30
```

**Expected behavior:**
- Args merged: `"power:70 haze:30"`, prompt: `"Summarize this"`
- Both sliders applied simultaneously

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "power:70 haze:30"
```

---

### 11. Multiple `/mtp` tokens — grid coordinates

**Input:**
```
/mtp D:16 Summarize this /mtp A:1
```

**Expected behavior:**
- Args merged: `"D:16 A:1"`, prompt: `"Summarize this"`
- Same result as the `synthesizer` preset expansion

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "D:16 A:1"
```

---

### 12. Multi-line input with `/mtp` on its own line

**Input:**
```
Summarize this article.
/mtp power:70
Focus on the conclusion.
/mtp haze:30
```

**Expected behavior:**
- Args merged: `"power:70 haze:30"`, prompt: `"Summarize this article.\nFocus on the conclusion."`
- Line breaks preserved in prompt; `/mtp` lines removed

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "power:70 haze:30"
```

---

### 13. Invalid input (graceful degradation)

**Input:**
```
/mtp G:10foo
```

**Expected behavior:**
- `G:10foo` matches neither grid nor slider format
- Compiler writes a warning to `stderr`
- Compiler returns empty `<mtp_node_shot>` tags
- Agent responds as usual (no constraints)

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "G:10foo"
```

---

### 14. Same-axis conflict

**Input:**
```
/mtp power:70 void:30 Review this code
```

**Expected behavior:**
- Both tokens target the Red axis
- The last token wins, so the effective result is `void:30`
- `stdout` contains one Red-axis `<constraints>` block only

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "power:70 void:30"
```

---

### 15. Partial invalid token

**Input:**
```
/mtp power:70 haze:xx Summarize this
```

**Expected behavior:**
- `power:70` is valid
- `haze:xx` is ignored
- `stderr` includes a warning for the ignored token
- `stdout` contains only the valid Red-axis constraints

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "power:70 haze:xx"
```

---

### 16. Preset plus override

**Input:**
```
/mtp synthesizer yellow:30 Outline this
```

**Expected behavior:**
- `synthesizer` expands first
- The later `yellow:30` token targets the same Yellow axis as `A:1` from the preset
- The later token wins, so the effective Yellow-axis result is `yellow:30`

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "synthesizer yellow:30"
```

---

### 17. Duplicate axis across multiple `/mtp` segments

**Input:**
```
Summarize this /mtp power:70 /mtp void:80
```

**Expected behavior:**
- Args merge in order: `power:70 void:80`
- Both tokens target the Red axis
- The last token wins, so the effective result is `void:80`

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "power:70 void:80"
```

---

### 18. Unknown node

**Input:**
```
/mtp foobar:20 Explain this
```

**Expected behavior:**
- `foobar:20` is not a known slider or axis color
- `stderr` includes an ignored-token warning
- `stdout` returns an empty `<mtp_node_shot>` envelope

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "foobar:20"
```

---

### 19. Neutral no-op

**Input:**
```
/mtp J:10 Summarize this
```

**Expected behavior:**
- `J:10` is the grid center, so intensity resolves to 0
- The token is valid, but it produces no active constraint
- `stdout` returns an empty `<mtp_node_shot>` envelope without a warning

**Compiler check** (run from skill root):
```bash
python3 scripts/mtp_compiler.py --args "J:10"
```
