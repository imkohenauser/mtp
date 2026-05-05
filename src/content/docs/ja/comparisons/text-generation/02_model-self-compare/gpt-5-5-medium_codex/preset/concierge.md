---
title: 'concierge | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill preset concierge。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `concierge` (preset)

## 入力

**プロンプト**

```markdown
/mtp concierge 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
前提として、AIモデル比較はかなり変動します。特に「最新モデル名、ベンチマーク順位、価格、コンテキスト長、利用可能プラン」は最新情報の確認が必要です。以下は、2026年4月30日時点で公式情報を確認したうえでの整理です。

**私の強み**
一番の強みは、単発の回答だけでなく「作業を進める」能力です。コードベースを読んで、編集し、テストし、結果を説明するような実務寄りのタスクに向いています。特にこのCodex環境では、ローカルファイル、ターミナル、テスト、差分確認まで含めて進められる点が強いです。

次に、複雑な依頼を構造化して扱うことです。曖昧な要望を、要件、制約、実装方針、検証手順に分けて進められます。調査、設計、実装、レビュー、文章化をまたぐタスクでは、会話だけで完結するモデルより有利です。

また、OpenAI系の強みとして、コーディング、エージェント的なツール利用、長い文脈、画像理解、スプレッドシートや資料作成などの業務成果物に強いとされています。OpenAIはGPT-5.2について、プロフェッショナル業務、長時間エージェント、コード、画像、長文脈、ツール利用の改善を公式に説明しています。[OpenAI GPT-5.2発表](https://openai.com/index/introducing-gpt-5-2)、[OpenAI APIモデル案内](https://platform.openai.com/docs/guides/latest-model)

**主要モデルとの比較感**
Claude系、特にAnthropicのClaude Opus 4.7は、公式発表では高度なソフトウェアエンジニアリング、長時間タスク、指示遵守、視覚理解、自己検証に強いとされています。したがって、文章の慎重さ、長時間の推論、コードレビュー、複雑な実装では非常に強い競合です。私の優位は、OpenAI/Codex環境での実作業統合、ツール操作、ファイル編集、検証までの一貫性にあります。[Anthropic Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)

Gemini系は、Google公式情報ではGemini 3 Proがマルチモーダル理解、長い入力、Google検索・AI Studio・Vertex AIなどのGoogle基盤との接続に強いです。画像、動画、音声、PDFを大きな文脈で扱う用途やGoogle Workspace連携では強力です。私の強みは、ソフトウェア開発や具体的な成果物作成を会話から実行まで落とす部分です。[Gemini 3](https://blog.google/products/gemini/gemini-3)、[Gemini APIモデル](https://ai.google.dev/gemini-api/docs/models/gemini)

DeepSeek系は、公式情報ではDeepSeek V4 Previewが低コスト、1Mコンテキスト、オープンウェイト、OpenAI/Anthropic互換APIを打ち出しています。コスト効率や自前運用、オープンモデル重視なら魅力があります。一方で、私の強みは、品質管理、対話での要件整理、開発環境との統合、検証込みの実務支援です。[DeepSeek V4 Preview](https://api-docs.deepseek.com/news/news260424)、[DeepSeek価格・モデル](https://api-docs.deepseek.com/quick_start/pricing)

**まとめると**
私を選ぶ価値が出やすいのは、コード修正、調査から実装までの一連の作業、複雑な仕様整理、長文の分析、業務成果物の作成、ツールを使った検証が必要な場面です。

ただし、モデル単体の「最強ランキング」、価格、最新ベンチマーク、各社の最新リリース状況は日々変わるため、その比較は毎回公式情報で確認するのが前提です。
````