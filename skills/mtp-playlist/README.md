# MTP Playlist

MTP Playlist is the second Agent Skill in the **Mapping the Prompt (MTP)** framework.

It turns a theme — a genre, artist, album, era, scene, or sound world — into a deliberately sequenced playlist, mapping each track to a node in the MTP arc rather than assembling a flat mood list.

---

## Install

```bash
# GitHub CLI
gh skill install imkohenauser/mtp skills/mtp-playlist

# Vercel Skills CLI
npx skills add imkohenauser/mtp --skill mtp-playlist
```

Works in any agent that supports the Agent Skills format.

---

## Usage

The skill is invoked explicitly with the `/mtp-playlist` command followed by your theme.

```text
/mtp-playlist Mozart for Spring
/mtp-playlist Strings at Work
/mtp-playlist Ravel with Boléro at Helix
/mtp-playlist Orchestral crescendo with Boléro at Helix
/mtp-playlist The Beatles starting with Hello, Goodbye at Start
```

Each command produces a Markdown artifact with a copy-friendly tracklist and a per-track `Reason` grounded in what you actually hear.

Supported request types:

- **Theme-only** — name a theme; the skill chooses all tracks.
  `/mtp-playlist Strings at Work`
- **Theme with node placements** — anchor specific tracks to named nodes.
  `/mtp-playlist Ravel with Boléro at Helix`
- **Length and side variants** — full 20-track (default), or a 10-track `Side A` / `Side B` half.
  `/mtp-playlist Side A for a sunrise run`
- **Extended / multi-cycle** — chain the arc into longer sequences (30, 40, and beyond).
- **Source-limited** — map a small pool (e.g. a single album) onto the arc without padding.

---

## How it works

The playlist follows a `1+9+9+1` arc:

- `#1 Start` — input / ignition (frame node)
- `#2–10` **Side A** — the positive pole: `Open`, `Power`, `Return`, `Grow`, `Helix`, `Focus`, `Enter`, `Flow`, `Close`
- `#11–19` **Side B** — the inverted pole: each node is the dark counterpart of its Side A position
- `#20 End` — final residue (frame node)

Each track is chosen for the **function** it performs at its node given its neighbors — not by popularity or favorites. Every `Reason` names concrete audible evidence, and the final list is verified so titles, artists, and years are real and correctly attributed.

See [SKILL.md](SKILL.md) for the full node map and selection rules.

---

## External Links

- [MTP Documentation](https://mappingtheprompt.com/)
- [GitHub Repository](https://github.com/imkohenauser/mtp)

---

## License

MIT. See `LICENSE` in the repository root.
