---
title: MTP Skill のインストール
description: MTP Skill を公式 zip ファイルまたは CLI から追加する方法を説明します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp_install.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp_install.png
lastUpdated: true
---

MTP Skill は、ZIP ファイルまたは CLI から追加できます。利用するホストが対応している方法を選択してください。

## ZIP

[`mtp-skill.zip` をダウンロード](/downloads/mtp-skill.zip)

ZIP 形式のカスタム Agent Skill に対応したホストで利用できます。この ZIP には、リポジトリ内の `skills/mtp` から生成された `mtp` Skill パッケージが含まれています。

### Claude.ai

Claude.ai は、アップロード形式のカスタム Skill に対応しています。UI ラベルは変更される可能性があるため、導入時には公式ヘルプも確認してください。

基本的な流れは次のとおりです。

1. `mtp-skill.zip` をダウンロードします。
2. Claude のデスクトップアプリまたは Web 版で `Customize > Skills` を開きます。
3. カスタム Skill の追加画面から ZIP ファイルをアップロードします。
4. MTP Skill がスキル一覧に表示され、有効になっていることを確認します。
5. チャットで `/mtp` を含むプロンプトを実行します。

[Claudeでスキルを使用する](https://support.claude.com/ja/articles/12512180-claude%E3%81%A7%E3%82%B9%E3%82%AD%E3%83%AB%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B) ↗

ZIP の追加操作は、通常デスクトップアプリまたは Web 版で行います。Skill をアカウントへ追加して有効化した後にモバイルアプリで利用できるかは、各ホストの同期仕様と対応クライアントに依存します。

詳しい手順と iOS アプリでの利用例は、紹介記事でも説明しています。

[AIの出力を調整する「Mapping the Prompt」の紹介と、ZIP追加したMTP SkillをClaude iOSアプリで使う](https://zenn.dev/imkohenauser/articles/llm-output-tuning-mtp-and-skills-zip-guide) ↗

## CLI

### GitHub CLI (`gh`)

GitHub CLI の `gh skill` は preview 扱いの機能であり、変更される可能性があります。

```bash
gh skill install imkohenauser/mtp skills/mtp
```

[GitHub CLI `gh skill` ドキュメント](https://cli.github.com/manual/gh_skill) ↗

### Vercel Skills CLI (`npx skills`)

```bash
npx skills add imkohenauser/mtp --skill mtp
```

[Vercel Skills CLI ドキュメント](https://www.skills.sh/docs/cli) ↗

## 動作確認

MTP Skill を追加した後、次のプロンプトを試してください。

```text
/mtp power:70
この文章を短く要約してください。
```

ホストが Skill 実行ログを表示する場合は、MTP コンパイラが実行されていることと、応答内で内部の制約適用処理に言及していないことを確認してください。

## 次に読む

- [コマンド仕様](/ja/skills/mtp/reference/)
- [カスタマイズ](/ja/skills/mtp/customize/)
- [MTP Skill 概要](/ja/skills/mtp/)
