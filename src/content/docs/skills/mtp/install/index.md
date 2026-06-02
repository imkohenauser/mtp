---
title: MTP Skill Installation
description: Add MTP Skill by downloading the official zip file or by installing it from the command line.
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/skills_mtp_install.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/skills_mtp_install.png
lastUpdated: true
---

MTP Skill can be added as a ZIP file or from the command line. Choose the method supported by the host where the skill will run.

## ZIP

[Download `mtp-skill.zip`](/downloads/mtp-skill.zip)

Use the ZIP file with hosts that support uploaded custom Agent Skills. The ZIP contains the `mtp` Skill package built from `skills/mtp` in the repository.

### Claude.ai

Claude.ai supports uploaded custom skills. The exact labels may change, so check the official help page when installing.

Basic flow:

1. Download `mtp-skill.zip`.
2. Open `Customize > Skills` in Claude desktop or the web app.
3. Add a custom skill and upload the ZIP file.
4. Confirm that MTP Skill appears in the skill list and is enabled.
5. In chat, run a prompt that includes `/mtp`.

[Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) ↗

ZIP upload is usually performed in a desktop or web client. After the skill is added and enabled for the account, mobile availability depends on the host's skill sync behavior and supported clients.

## CLI

### GitHub CLI (`gh`)

The GitHub CLI `gh skill` command is a preview feature and may change.

```bash
gh skill install imkohenauser/mtp skills/mtp
```

[GitHub CLI `gh skill` documentation](https://cli.github.com/manual/gh_skill) ↗

### Vercel Skills CLI (`npx skills`)

```bash
npx skills add imkohenauser/mtp --skill mtp
```

[Vercel Skills CLI documentation](https://www.skills.sh/docs/cli) ↗

## Check

After adding MTP Skill, try this prompt:

```text
/mtp power:70
Summarize this text in a shorter form.
```

If the host exposes skill execution logs, confirm that the MTP compiler ran and that the response does not mention the internal constraint application process.

## Next

- [Command reference](/skills/mtp/reference/)
- [Customization](/skills/mtp/customize/)
- [MTP Skill overview](/skills/mtp/)
