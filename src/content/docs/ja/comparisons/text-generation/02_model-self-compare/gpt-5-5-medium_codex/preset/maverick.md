---
title: 'maverick | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill preset maverick。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `maverick` (preset)

## 入力

**プロンプト**

```markdown
/mtp maverick 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
2026年4月30日時点で公式情報を確認した前提です。とはいえ、AIモデル比較は更新が速いので、**最新情報が特に必要なのは、ベンチマーク順位、価格、利用可能プラン、API提供状況、コンテキスト長、各社の最新モデル名**です。

私、つまりこのCodex系のOpenAIモデルの相対的な強みは、ざっくり言うと「実務を最後まで進める力」に寄っています。

**強み**
- **複雑な作業の分解と継続実行**  
  コード修正、調査、ファイル編集、テスト、結果説明のような複数ステップの仕事を、会話だけでなく実際のツール操作まで含めて進めやすいです。OpenAIはGPT-5.5について、コード、オンライン調査、データ分析、文書やスプレッドシート作成、ツール横断作業を強調しています。  
  出典: [OpenAI GPT-5.5](https://openai.com/ta-IN/index/introducing-gpt-5-5/)

- **コーディングとエージェント作業**  
  Anthropic Claudeもコードでは非常に強いですが、Codex環境ではリポジトリを読んで、パッチを当て、テストし、ユーザーに差分を説明する流れに最適化されています。OpenAIのモデル一覧でもGPT-5.2系は「coding and agentic tasks」を主用途として掲げています。  
  出典: [OpenAI Models](https://platform.openai.com/docs/models)

- **指示追従と作業スタイルの調整**  
  会話のトーン、出力形式、制約、段階的な進め方に合わせるのが得意です。これはClaudeの自然な文章力やGeminiのGoogle連携とは別方向で、実務ワークフローに合わせ込む強みです。

- **安全性と慎重な境界管理**  
  医療、法務、セキュリティ、バイオなど高リスク領域では、断定しすぎず、必要に応じて確認や制限を入れる設計が強めです。OpenAIはGPT-5.5のシステムカードで、安全性評価やレッドチーミングを明記しています。  
  出典: [GPT-5.5 System Card](https://openai.com/index/gpt-5-5-system-card/)

**他社モデルが強そうな領域**
- **Claude**: 長文読解、自然な文章、慎重な推論、コードレビューや設計相談で強い印象があります。Anthropic公式ではClaude Opus 4.1を複雑推論と高度なコーディング向けとしています。  
  出典: [Anthropic Models](https://docs.anthropic.com/en/docs/about-claude/models/all-models)

- **Gemini**: Google製品、検索、マルチモーダル、巨大なエコシステム統合が強みになりやすいです。GoogleはGemini 3を reasoning、multimodality、coding の強化として説明しています。  
  出典: [Google Gemini 3](https://blog.google/products/gemini/gemini-3)

- **Grok**: X連携、リアルタイム検索、長いコンテキスト、ツール利用を前面に出しています。xAIはGrok 4.1 Fastで2MコンテキストやAgent Tools APIを強調しています。  
  出典: [xAI Grok 4.1 Fast](https://x.ai/news/grok-4-1-fast/)

- **Llama / オープンモデル系**: 自社ホスト、改変、コスト管理、データ統制では強い選択肢です。MetaはオープンソースAIの価値を、広い開発者参加と透明性の観点で説明しています。  
  出典: [Meta Open Source AI](https://ai.meta.com/opensourceAI/)

別の見方をすると、単純な「一番賢いモデル」比較より、**閉じた実務を任せるならOpenAI/Codex、文章や読解の相棒ならClaude、Google環境ならGemini、リアルタイムX/検索ならGrok、自社管理ならLlama系**という選び方が近そうです。どの用途で比べたいですか。
````