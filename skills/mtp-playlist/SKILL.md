---
name: mtp-playlist
description: "Create an MTP music sequence using the Mapping the Prompt (MTP) framework: default 20-track playlist, 10-track Side A/B half, extended multi-cycle sequence, or reduced source-limited mapping. Invoked explicitly to build a structured musical arc from a theme, genre, artist, album, era, scene, or sound world, optionally anchoring specific tracks to named MTP nodes."
disable-model-invocation: true
version: "1.0.0"
---

# MTP Playlist

MTP Playlist creates a music sequence using the [Mapping the Prompt (MTP)](https://mappingtheprompt.com/) framework.

It can map songs, recordings, compositions, performances, sound works, or musical moments.

Take your time with the curation. This is not a quick list to dash off — you are composing roughly an hour of someone's life. Treat the listener's hour as precious, and spend real effort researching, digging, and verifying so the finished sequence earns it.

## Request types

### Theme-only

The default. The user names a theme; you choose all 20 tracks to fit the theme and each node's function.

Examples:

```text
/mtp-playlist Mozart for Spring
/mtp-playlist Strings at Work
```

### Theme with node placements

The user may anchor one or more specific tracks to named MTP nodes. Treat the remainder as a theme-only request: fill unassigned nodes with tracks that honor the theme and each node's function.

Node names may appear as MTP labels (`Start`, `Helix`, `Fade`, etc.) or as numbers `1`–`20`.

Examples:

```text
/mtp-playlist Ravel with Boléro at Helix
/mtp-playlist Orchestral crescendo with Boléro at Helix
/mtp-playlist The Beatles starting with Hello, Goodbye at Start
```

- `Ravel with Boléro at Helix` — theme: Ravel; anchor "Boléro" at #6 `Helix`
- `Orchestral crescendo with Boléro at Helix` — theme: orchestral crescendo; anchor "Boléro" at #6 `Helix`
- `The Beatles starting with Hello, Goodbye at Start` — theme: The Beatles; anchor "Hello, Goodbye" at #1 `Start`

Placement rules:

- Apply every user-specified anchor before choosing any other track.
- Do not move, swap, or override anchored tracks unless the user asks.
- Anchors reshape the surrounding sequence. When a track is fixed at a node, treat that placement as a constraint that changes which tracks best fit the remaining nodes — not as an isolated decision. A strong anchor at `Helix`, for example, shifts what `Open`, `Grow`, and `Enter` need to do in relation to it.
- Anchored tracks must still perform their node's function as far as possible; state any tension honestly in `Reason`. An unexpected anchor can be productive: a familiar song placed early, late, in the middle, or as a deliberate dissonance reveals a different facet of it.
- If a placement is ambiguous (wrong track title, unclear node, or conflicting anchors), ask briefly before generating.

### Length and side variants

The default is 20 tracks (`1+9+9+1`). Two 10-track half-sequences are also supported:

- **Side A (`1+9`)** — `#1 Start` + Side A nodes `#2–10`, the positive-pole half. Use when the user asks for a 10-track playlist, a "Side A" set, or a front-half sequence.
- **Side B (`9+1`)** — Side B nodes `#11–19` + `#20 End`, the negative-pole half. Use when the user asks to build "from Side B" or "the B-side".

When the user requests 10 tracks without naming a side, default to Side A. Map only the nodes in scope; framing, mapping, and verification work the same way on the nodes you use.

Examples:

- `/mtp-playlist Side A for a sunrise run` — 10-track Side A (`#1–10`)
- `Build the B-side for a comedown` — 10-track Side B (`#11–20`)

### Extended and multi-cycle lengths

On request, chain the structure into longer sequences (30, 40, and beyond) built from two blocks:

- `1` — a single frame node (`Start` or `End`).
- `9` — one full side mapped in node order (Side A `#2–10` or Side B `#11–19`).

Combine blocks to match the requested pattern or length. Examples:

- `1+9+9+1+1+9+9+1` — 40 tracks: two full `1+9+9+1` arcs back to back.
- `1+9+9+1+1+9`     — 30 tracks: a full arc, then a Side A half.
- `1+9+9+1+9+1`     — 30 tracks: a full arc, then a Side B half.
- `9+1+9+1+9+1`     — 30 tracks: three `9+1` side-plus-frame halves.

Rules:

- Honor the requested block pattern exactly when the user gives one. If they give only a length, pick a pattern that reaches it and state which pattern you used.
- Number rows sequentially from 1 to the total. Node names repeat each time their block recurs — a second Side A reuses `Open … Close`.
- When a numeric pattern does not say which side each `9` is, follow the MTP arc (Side A positive pole, then Side B negative pole) and state your interpretation.
- Do not repeat tracks across cycles or pad off-theme to reach the count. If the theme cannot sustain the length honestly, say so and propose a shorter pattern.

### Source-limited mappings

When the source pool is inherently smaller than the requested sequence — for example classifying a single album with fewer than 20 tracks — do not pad to 20 or force the material into the Side A half. Keep the full MTP arc as the reference and map the available tracks to the nodes they best perform across `#1–20`, in node order.

- Never repeat a track to fill a node.
- Never bring in tracks from outside the source or theme just to reach a count.
- Leave unused nodes empty rather than assigning a weak fit.
- Output only the assigned rows, preserving the original MTP node numbers so the sparse mapping remains clear.

## Workflow

1. **Parse the request.** Use the skill argument when provided; on platforms that inject `$ARGUMENTS`, use that value; otherwise use the user's message. Distinguish theme-only from theme with node placements. Extract the theme and any `{track} at {node}` anchors. Decide the length and scope: full 20-track (`1+9+9+1`), a 10-track half (Side A or Side B), an extended multi-cycle length (e.g. 30 or 40 tracks), or a sparse source-limited mapping when the source has fewer tracks than the sequence (see Length and side variants). If still ambiguous, briefly interview the user before generating.
2. **Apply anchors.** Place user-specified tracks at their named nodes.
3. **Research and dig when useful.** If tools are available, gather current or external context (`Research mode`), then look beyond the obvious (`Diggin' Deeper`) while keeping node fit as the deciding criterion.
4. **Frame the sequence.** Choose the frame nodes in scope: `#1 Start` for a full or Side A sequence, `#20 End` for a full or Side B sequence, if not already anchored.
5. **Map Side A.** If Side A is in scope, assign tracks to unassigned nodes #2–10 in order.
6. **Map Side B.** If Side B is in scope, assign tracks to unassigned nodes #11–19 in order.
7. **Write and review.** Fill each `Reason` with node-fit evidence, then replace any non-anchored row that does not clearly perform its assigned node.
8. **Verify the final list (do not skip).** This is mandatory before returning anything. Check every single track on three points: (a) it fits its node's cues, (b) it matches the theme and era, and (c) it is a real, correctly attributed track that actually exists. Replace any track that fails any check. **Never invent titles, artists, or years.** If no external verification tools are available, do not pretend to verify: restrict the list to tracks you know with high confidence, leave any uncertain `Year` blank, and add one short note stating that selections were not externally verified.

## Selection rules

Map the theme to a 20-step MTP sequence.

This is not a mood playlist, popularity list, or list of favorites.
Each selection must perform the function of its assigned node.

A track's node assignment is context-dependent, not intrinsic. The same track may perform `Open` in one sequence and `Flow` or `Helix` in another, depending on what precedes and follows it. Do not ask "which node does this track belong to?" — ask "which node does this track perform, given its neighbors in this sequence?" Each placement decision reshapes the meaning available to every other slot. The same song can land early, late, in the middle, or as a deliberate dissonance, and each position makes it mean something different.

Choose each track by observable musical or cultural function: sound, structure, rhythm, harmony, texture, lyrics, vocal delivery, production, arrangement, historical role, scene function, or current cultural effect.

Honor the theme literally. For era-based themes, prioritize release date; for cultural-era themes, adjacent years are allowed only when the track clearly belongs to that moment.

Current popularity, virality, chart position, or canonical status may inform selection, but must not override node fit.

## Research mode

If research tools are available and the theme needs external context, do targeted research before selecting tracks.

Be aware that your training data has a cutoff and may miss recent releases, reissues, credits, corrections, or cultural context; when tools are available, actively fill those gaps through targeted research and verification.

Useful sources include Pitchfork, Rolling Stone, AllMusic, Genius, Wikipedia, WhoSampled, YouTube, Spotify, Apple Music, charts, playlists, and current viral or social signals.

Use research to refresh context and verify relevance. Do not choose tracks only because they are famous, viral, highly rated, or easy to find; each track must still perform its assigned MTP node.

## Sequence

The playlist follows a `1+9+9+1` structure, read as a linear arc:

* **1** — #1 `Start`  (Input): virtual frame node, not on the grid.
* **9** — Side A nodes  #2–10: the positive pole — expansion, energy, unfoldment, arrival.
* **9** — Side B nodes #11–19: the negative pole — inversion, depletion, dismantling, attenuation.
* **1** — #20 `End`  (Output): virtual frame node, not on the grid.

The node order follows the grid row order, from top-left to bottom-right:
`Open → Power → Return → Grow → Helix → Focus → Enter → Flow → Close` for Side A, then the same path for Side B.

**Inversion principle.** Each Side B node is the inverted pole of the Side A node at the same grid position. Use the `Pair` column in the node table when selecting Side B tracks.

Reference:
https://mappingtheprompt.com/optional/mapping-and-sequence/

## MTP nodes

`Start` (#1) and `End` (#20) frame the arc but are not placed on the 3×3 grid. The 18 grid nodes occupy the same nine positions on both sides; a Side B node inherits its position's Side A color in a darkened form (for example, Top-Left is Yellow for `Open` and Dark Yellow for `Still`). Two positions have no hue to darken, so their Side B color is restated rather than darkened: Center-Center goes Transparent → Translucent (`Helix` → `Collapse`), and Center-Right goes White → Dark Grey (`Focus` → `Haze`).

Side A (node / color):

```markdown
| Position | Left                       | Center                       | Right                       |
| -------- | -------------------------- | ---------------------------- | --------------------------- |
| Top      |  2. `Open`   / Yellow      |  3. `Power`    / Red         |  4. `Return` / Magenta      |
| Center   |  5. `Grow`   / Green       |  6. `Helix`    / Transparent |  7. `Focus`  / White        |
| Bottom   |  8. `Enter`  / Cyan        |  9. `Flow`     / Blue        | 10. `Close`  / Purple       |
```

Side B (node / color — darkened counterpart of the same position):

```markdown
| Position | Left                       | Center                       | Right                       |
| -------- | -------------------------- | ---------------------------- | --------------------------- |
| Top      | 11. `Still`  / Dark Yellow | 12. `Void`     / Dark Red    | 13. `Surge`  / Dark Magenta |
| Center   | 14. `Wither` / Dark Green  | 15. `Collapse` / Translucent | 16. `Haze`   / Dark Grey    |
| Bottom   | 17. `Drift`  / Dark Cyan   | 18. `Abyss`    / Dark Blue   | 19. `Fade`   / Dark Purple  |
```
### Functional cues

```markdown
|  # | Node     | Cues                                                              | Color        | Pair     |
| -- | -------- | ----------------------------------------------------------------- | ------------ | -------- |
|  1 | Start    | beginning, input, ignition                                        | —            | —        |
|  2 | Open     | opening, expansion, invitation                                    | Yellow       | Still    |
|  3 | Power    | force, drive, assertion                                           | Red          | Void     |
|  4 | Return   | memory, return, recurrence                                        | Magenta      | Surge    |
|  5 | Grow     | development, widening, organic expansion                          | Green        | Wither   |
|  6 | Helix    | integration, center, structure, rotation, coordination            | Transparent  | Collapse |
|  7 | Focus    | precision, clarity, definition                                    | White        | Haze     |
|  8 | Enter    | threshold, entry, arrival into a new field                        | Cyan         | Drift    |
|  9 | Flow     | continuity, motion, fluidity                                      | Blue         | Abyss    |
| 10 | Close    | closure, completion, sealing                                      | Purple       | Fade     |
| 11 | Still    | pause, suspension, quiet                                          | Dark Yellow  | Open     |
| 12 | Void     | absence, hollow space, negative center                            | Dark Red     | Power    |
| 13 | Surge    | excess, eruption, overflow                                        | Dark Magenta | Return   |
| 14 | Wither   | drying, decline, weakening                                        | Dark Green   | Grow     |
| 15 | Collapse | breakdown, structural fall                                        | Translucent  | Helix    |
| 16 | Haze     | blur, fog, obscured perception                                    | Dark Grey    | Focus    |
| 17 | Drift    | wandering, loosened direction                                     | Dark Cyan    | Enter    |
| 18 | Abyss    | depth, descent, darkness                                          | Dark Blue    | Flow     |
| 19 | Fade     | disappearance, dissolution, afterimage                            | Dark Purple  | Close    |
| 20 | End      | output state, final residue                                       | —            | —        |
```

## Diggin' Deeper

Once you have context, dig past the obvious. The first track that comes to mind for a node is usually the default, not the best fit.

Work it like hopping between one record shop and the next, flipping through crate after crate: deep cuts, B-sides, album tracks, live versions, remixes, edits, samples and the songs they sample, regional scenes, reissues, and adjacent artists. Pull the sleeve, read the credits, and follow them to the next bin. Use WhoSampled, full discographies, label and scene catalogs, and credits to trace lineage.

Dig in service of node fit, not obscurity. A famous track may still win a node, and a rare one is worthless if it does not perform its function. Prefer the track that performs the node most precisely, however well- or little-known it is.

## Task

Create the MTP playlist artifact for the parsed theme and anchors above, at the length and scope decided in Workflow step 1: a full 20-track sequence, a 10-track Side A or Side B half, an extended multi-cycle length, or a sparse source-limited mapping. Include only the tracklist rows for nodes in scope; for sparse source-limited mappings, preserve the original MTP node numbers instead of renumbering.

Use [PLAYLIST-FORMAT.md](PLAYLIST-FORMAT.md) as the shared output format and row-field reference. When artifact or file output is available, create `mtp-playlist-{slug}.md` using lowercase kebab-case for `{slug}`. If artifact or file output is unavailable, return the same Markdown content inline.

For `Year`, use the recording or release year of the specific version. For classical or other works where composition, premiere, and recording years differ, pick the year that matches the theme — composition year for era-of-composition themes, recording or release year for a specific performance — and name which one you used in the `Reason`. Leave `Year` blank when it is uncertain rather than guessing. If a requested era is strict, every dated row must fall inside it; if the user describes a looser cultural era, adjacent years are allowed only when the track clearly belongs to that moment.

Each `Reason` must be listener-facing: describe what someone actually hears, name concrete audible evidence, and connect that perception to the assigned node. Apply the swap test: if the node name could be replaced with another and the sentence still works, rewrite it. Write with conviction, but calibrate the register to the theme — fierce for loud or street-level themes, hushed for quiet or ambient ones. Use color or Side B inversion only when it sharpens the fit after the audible evidence is already clear.

- Weak: "The tempo lifts and eases the transition into the next track. (fits `Focus`)"
- Strong: "That snare snaps clean through the mix and the lyric lands razor-sharp, wiping out the haze before it and locking the ear dead-center. (fits `Focus`)"

Write every `Reason` in the user's language. Avoid vague mood claims, restating node cues as evidence, fame-based choices, general praise, or multiple alternatives in one row. Before finalizing, run Workflow step 8.

## Interaction Guidelines

- Respond in the user's configured language, including every `Reason`. Keep node names (`Start`, `Helix`, etc.) and color names in English.
- If the theme, scope, era, source material, or node anchors are unclear, ask a few brief questions before generating.
- If a year, version, or release context is uncertain, leave it blank or state the uncertainty briefly.
- If playlist-creation tools are available, first propose the playlist as text and ask for confirmation before creating it in Apple Music, Spotify, or any other app.
