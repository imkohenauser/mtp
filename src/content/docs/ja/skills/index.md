---
title: スキルのインストール
description: MTP にはいくつかの Agent Skill があります。各スキルを公式 zip ファイルまたは CLI から追加する方法を説明します。MTP Skill と MTP Playlist Skill に共通の手順です。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_skills.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_skills.png
lastUpdated: true
---

MTP にはいくつかの Agent Skill があり、このページではそのインストール方法をまとめて説明します。  
手順は [MTP Skill](/ja/skills/mtp/) と [MTP Playlist Skill](/ja/skills/mtp-playlist/) で共通です。  
利用するホストが対応している方法を選択してください。

## ZIP ファイル

追加したいスキルをダウンロードします。

- [`mtp-skill.zip` をダウンロード](/downloads/mtp-skill.zip)
- [`mtp-playlist-skill.zip` をダウンロード](/downloads/mtp-playlist-skill.zip)

各 ZIP には、リポジトリ内の `skills/` 配下の各ディレクトリから生成された Skill パッケージが含まれています。

### ZIP のアップロードに対応するホスト

アップロード形式のカスタム Agent Skill に対応するホストは増えています。  
Claude、Manus、Grok、ChatGPT などが該当します。  
UI ラベルや導線はホストによって異なり、変更される可能性もあるため、導入時には各ホストの公式ヘルプも確認してください。

基本的な流れは次のとおりです。

1. 追加したいスキルの ZIP をダウンロードします。
2. ホストのカスタム Skill 設定（例: `Customize > Skills`）を開きます。
3. カスタム Skill の追加画面から ZIP ファイルをアップロードします。
4. スキルが一覧に表示され、有効になっていることを確認します。
5. チャットで、そのスキルを呼び出すプロンプトを実行します。

[Claudeでスキルを使用する](https://support.claude.com/ja/articles/12512180-claude%E3%81%A7%E3%82%B9%E3%82%AD%E3%83%AB%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B) ↗

ZIP の追加操作は、通常デスクトップアプリまたは Web 版で行います。  
Skill をアカウントへ追加して有効化した後にモバイルアプリで利用できるかは、各ホストの同期仕様と対応クライアントに依存します。

## コマンドライン

### GitHub CLI (`gh`)

```bash
gh skill install imkohenauser/mtp skills/mtp
```

```bash
gh skill install imkohenauser/mtp skills/mtp-playlist
```

[GitHub CLI `gh skill` ドキュメント](https://cli.github.com/manual/gh_skill) ↗

### Vercel Skills CLI (`npx skills`)

`npx skills` はリポジトリ全体を clone します。  
スキル配下のファイルだけを取得する GitHub CLI は追加が早く、推奨です。

```bash
npx skills add imkohenauser/mtp --skill mtp
```

```bash
npx skills add imkohenauser/mtp --skill mtp-playlist
```

[Vercel Skills CLI ドキュメント](https://www.skills.sh/docs/cli) ↗

## 動作確認

スキルを追加した後、そのスキルを呼び出すプロンプトを試してください。

```text
/mtp power:100
他社の主要な AI モデルと比較して、このモデルの強みを教えてください。
```

```text
/mtp-playlist 松任谷由実を過去から現在まで
```

## 次に読む

- [MTP Skill](/ja/skills/mtp/)
- [MTP Playlist Skill](/ja/skills/mtp-playlist/)
