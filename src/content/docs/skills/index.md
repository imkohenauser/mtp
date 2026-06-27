---
title: Skills Installation
description: MTP offers several Agent Skills. Add one by downloading the official zip file or installing it from the command line. Shared installation steps for MTP Skill and MTP Playlist Skill.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/skills.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/skills.png
lastUpdated: true
---

MTP offers several Agent Skills, and this page covers installation for all of them. The same steps apply to [MTP Skill](/skills/mtp/) and [MTP Playlist Skill](/skills/mtp-playlist/). Choose the method supported by the host where the skill will run.

## ZIP

Download the skill you want to add.

- [Download `mtp-skill.zip`](/downloads/mtp-skill.zip)
- [Download `mtp-playlist-skill.zip`](/downloads/mtp-playlist-skill.zip)

Each ZIP contains the Skill package built from its directory under `skills/` in the repository.

### Hosts that support ZIP upload

A growing number of hosts support uploaded custom Agent Skills, including Claude, Manus, Grok, and ChatGPT. The exact labels and entry points differ by host and may change, so check the host's official help when installing.

Basic flow:

1. Download the ZIP for the skill you want.
2. Open the host's custom skill settings, such as `Customize > Skills`.
3. Add a custom skill and upload the ZIP file.
4. Confirm that the skill appears in the skill list and is enabled.
5. In chat, run a prompt that invokes the skill.

[Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) ↗

ZIP upload is usually performed in a desktop or web client. After the skill is added and enabled for the account, mobile availability depends on the host's skill sync behavior and supported clients.

## CLI

### GitHub CLI (`gh`)

```bash
gh skill install imkohenauser/mtp skills/mtp
```

```bash
gh skill install imkohenauser/mtp skills/mtp-playlist
```

[GitHub CLI `gh skill` documentation](https://cli.github.com/manual/gh_skill) ↗

### Vercel Skills CLI (`npx skills`)

`npx skills` clones the entire repository. GitHub CLI, which fetches only the files under the skill directory, is faster to install and is recommended.

```bash
npx skills add imkohenauser/mtp --skill mtp
```

```bash
npx skills add imkohenauser/mtp --skill mtp-playlist
```

[Vercel Skills CLI documentation](https://www.skills.sh/docs/cli) ↗

## Check

After adding a skill, run a prompt that invokes it.

```text
/mtp power:100
Compared with other major AI models from competing companies, please explain your strengths.
```

```text
/mtp-playlist Madonna from present to past
```

## Next

- [MTP Skill](/skills/mtp/)
- [MTP Playlist Skill](/skills/mtp-playlist/)
