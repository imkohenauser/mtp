---
title: MTP Skill Customization
description: Customize MTP Skill by editing node Markdown files, preset definitions, and checking compiler output.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/skills_mtp_customize.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/skills_mtp_customize.png
lastUpdated: true
---

This page is for developers who want to customize MTP Skill behavior. General users do not need to edit these files to use `/mtp`.

## Files

```text
skills/mtp/nodes/*
skills/mtp/references/presets.yaml
skills/mtp/scripts/mtp_compiler.py
```

Node definitions and presets are source material for the compiler. Editing them changes the constraints that MTP Skill emits.

## Node definitions

Each axis is defined by a Markdown file under `skills/mtp/nodes/`. These files are not only documentation; the compiler reads them as constraint sources.

The file must start with simple frontmatter.

```yaml
---
axis: red
node_positive: power
node_negative: void
description: "Axis of force and void. Controls whether to push output and assert strongly or strip it back to create margin."
---
```

Required keys:

- `axis`
- `node_positive`
- `node_negative`

Recommended key:

- `description`

Keep frontmatter simple. Use one `key: value` entry per line. Do not use lists, nested YAML, or multi-line values.

## Body structure

The compiler expects this heading structure.

```md
## Side A

### Low

- ...

### Mid

- ...

### High

- ...

## Side B

### Low

- ...

### Mid

- ...

### High

- ...
```

Tier extraction is cumulative.

| Intensity | Extracted tiers |
| --- | --- |
| `1-30` | Low |
| `31-70` | Low + Mid |
| `71-100` | Low + Mid + High |

Higher tiers should strengthen or extend lower tiers. They should not contradict lower-tier constraints.

## Presets

Presets are defined in `skills/mtp/references/presets.yaml`.

```yaml
synthesizer: "D:16 A:1"
strategist: "P:16 P:4"
maverick: "D:4 A:19"
concierge: "J:13 D:10"
```

Each value is a space-separated sequence of MTP tokens. Sliders and grid coordinates can be combined. Presets expand before parsing, so same-axis conflict resolution still follows the final expanded token order.

## Checks

Run the compiler from the skill root.

```bash
python3 scripts/mtp_compiler.py --args "power:100"
python3 scripts/mtp_compiler.py --args "D:16 A:1"
python3 scripts/mtp_compiler.py --args "synthesizer yellow:30"
```

The compiler writes constraint XML to stdout. Warnings and short summaries are written to stderr.

Detailed test cases are listed in [`skills/mtp/USAGE.md`](https://github.com/imkohenauser/mtp/blob/main/skills/mtp/USAGE.md).
