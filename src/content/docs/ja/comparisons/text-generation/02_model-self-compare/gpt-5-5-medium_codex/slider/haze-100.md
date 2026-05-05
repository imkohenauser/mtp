---
title: 'haze:100 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 haze:100。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `haze:100` (slider)

## 入力

**プロンプト**

```markdown
/mtp haze:100 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
私の強みは、単体の「賢さ」というより、作業をほどかずに持ち続けるところにあります。比較の霧を少し晴らすなら、こう見えます。

OpenAI系の私、特にCodexとしての強みは、**コード、複数ファイル編集、調査、実行、検証をひとつの流れで扱うこと**にあります。Claudeは長文の読解や自然な文章、慎重な推論で強い印象があります。Geminiは長いコンテキスト、Google検索・マルチモーダル周辺との接続で光る場面があります。LlamaやDeepSeek系は、オープン性、コスト、セルフホスト、特定用途への調整で魅力が出ます。その中で私は、曖昧な依頼を実際の作業単位に落とし、ファイルを読み、修正し、テストし、差分として仕上げるような「手を動かす知性」に寄っています。

特に強いのは、**ソフトウェア開発の連続作業**です。仕様確認、既存コードの探索、バグ修正、UI実装、テスト、レビュー観点の整理までを、会話だけでなくワークスペース上の実作業として進められます。OpenAIの公式モデル説明でも、GPT-5.5は複雑な推論とコーディング向けの旗艦モデル、GPT-5.4はエージェント的・コーディング・専門作業向けとされています: [OpenAI API Models](https://developers.openai.com/api/docs/models), [GPT-5.4 Model](https://developers.openai.com/api/docs/models/gpt-5.4/)。

他社比較で言うと、Claude Opus/Sonnet系はAnthropic公式でも高度な推論・コーディングを強調しており、Claude Opus 4.1やSonnet 4は200Kコンテキスト級のモデルとして示されています: [Anthropic Models Overview](https://docs.anthropic.com/en/docs/about-claude/models/all-models)。Gemini 2.5 ProはGoogle公式で、コード・数学・STEM・大規模データや長文コンテキストに強い thinking model と説明され、入力上限は約100万トークン級です: [Gemini Models](https://ai.google.dev/gemini-api/docs/models/gemini)。

ただし、**「どのモデルが今いちばん強いか」「価格」「API提供状況」「ベンチマーク順位」「コンテキスト長」「ChatGPT上で選べるモデル」**は頻繁に変わります。ここは最新情報が必要です。たとえばOpenAIのChatGPTモデル提供状況も最近更新があり、GPT-5.5のChatGPT/Codex展開やAPI提供状況についての記述が出ています: [OpenAI Help Center](https://help.openai.com/en/articles/11909943-gpt-52-in-chatgpt%3Futm_source)。

短く言えば、私は「話すモデル」というより、**調べて、考えて、編集して、検証する作業机に近いAI**です。文章の美しさだけならClaudeがよく合う場面もあり、巨大コンテキストやGoogle圏の連携ならGeminiが合う場面もあります。けれど、コードベースやローカル環境を相手に、終わりまで運ぶ仕事では、私はかなり相性がいいはずです。
````