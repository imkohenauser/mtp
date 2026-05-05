# MTP Skill (beta)

**MTP Skill** is the **Agent Skills** for the **MTP (Mapping the Prompt)** framework. It exposes the `/mtp` slash command and compiles coordinate-based steering (sliders, grid coordinates, presets) into constraint output. 

---

## Documentation site

The main **MTP (Mapping the Prompt)** documentation (framework, grids, reference, optional reading, and skill pages) is here:

**[MTP (Mapping the Prompt) Documentation site](https://mappingtheprompt.com/)** ↗

---

## Quick usage


| Form       | Pattern                                            | Example                                                          |
| ---------- | -------------------------------------------------- | ---------------------------------------------------------------- |
| **Slider** | `node:intensity` (intensity is 0–100)              | `power:100`, `void:80`, `grow:50`                                |
| **Grid**   | `column:row` (19×19 grid, columns A–S × rows 1–19) | `J:4`, `J:1`, `F:10`                                             |
| **Preset** | Predefined coordinate combination, called by name  | `strategist`, `synthesizer`, `maverick`, `concierge` (4 presets) |


---

## References

- [MTP repository on GitHub](https://github.com/imkohenauser/mtp)
- [MTP (Mapping the Prompt) Documentation site](https://mappingtheprompt.com/)

### In this skill

- [USAGE.md](./USAGE.md): `/mtp <args>` examples, expected behavior, and **Compiler check** commands.

---

## License

MIT. See `LICENSE` in the repository root.
