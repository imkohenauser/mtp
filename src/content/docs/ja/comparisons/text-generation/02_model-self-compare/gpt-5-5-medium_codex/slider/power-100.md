---
title: 'power:100 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 power:100。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `power:100` (slider)

## 入力

**プロンプト**

```markdown
/mtp power:100 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
**結論：私の強みは「コードベースを読んで、編集し、検証し、最後まで作業する」能力です。**  
単発の回答力だけなら各社モデルに得意分野があります。だが、この環境の私、つまり Codex 系エージェントの本領は、会話ではなく実作業です。

**強いところ**
1. **実装・修正・検証まで一気通貫**
   Claude や Gemini もコードは強いですが、私はこのワークスペースでファイルを読み、差分を作り、テストを走らせ、失敗を見て直す流れに最適化されています。単なるコード生成より、既存リポジトリでの変更作業に強いです。

2. **長いソフトウェア作業**
   OpenAI は GPT-5.3-Codex を「agentic coding」「long-running tasks」「research, tool use, complex execution」向けと説明しています。公式発表では GPT-5.2-Codex より高速化し、SWE-Bench Pro や Terminal-Bench で強い性能を示したとされています。  
   出典: [OpenAI GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex)

3. **ユーザーのローカル文脈に合わせた作業**
   既存の設計、テスト、命名、UI方針、依存関係に合わせて変更できます。これは「正しい一般論」より重要です。実務では、正解は仕様書ではなくコードベースの中にあることが多いからです。

4. **安全な作業手順**
   変更前に読む。関係ない差分を戻さない。破壊的操作を避ける。テストで確認する。この種の慎重さは、エージェント型開発では性能と同じくらい重要です。

**他社主要モデルとの比較**
- **Claude Opus / Sonnet 系**: 強力な推論、長文処理、コードレビュー、エージェント作業が強み。Anthropic は Opus 4.6/4.7 を coding、agents、vision、multi-step tasks で強化していると説明しています。Claude は文章品質や慎重な推論でも強いです。  
  出典: [Anthropic Newsroom](https://www.anthropic.com/news), [Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)

- **Google Gemini 3 系**: 最大の強みはマルチモーダルと巨大コンテキストです。公式 docs では Gemini 3 Pro Preview がテキスト、画像、動画、音声、PDF入力に対応し、入力 1,048,576 トークンとされています。画像・動画・Google連携では非常に強いです。  
  出典: [Gemini API Models](https://ai.google.dev/gemini-api/docs/models), [Gemini 3 announcement](https://blog.google/products/gemini/gemini-3)

- **xAI Grok 系**: X連携、リアルタイム性、音声エージェント寄りの展開が強みです。直近では `grok-voice-think-fast-1.0` が高頻度ツール呼び出しや音声ワークフロー向けに発表されています。  
  出典: [xAI Grok Voice Think Fast](https://x.ai/news/grok-voice-think-fast-1)

- **Mistral / DeepSeek / Llama などの open-weight 系**: 強みはコスト、自己ホスト、改造可能性、透明性です。Mistral Large 3 は Apache 2.0 の open model として発表され、DeepSeek は V4 を 2026年4月24日リリースと公開しています。  
  出典: [Mistral 3](https://mistral.ai/news/mistral-3), [DeepSeek Transparency](https://www.deepseek.com/en/transparency/)

**私が最強ではない領域**
- ネイティブな動画・音声・画像理解なら Gemini や専用マルチモーダルモデルが有利な場面があります。
- 超低コスト運用や自己ホストなら Mistral、DeepSeek、Llama 系が有利です。
- Claude は長文の自然な文章、慎重なレビュー、複雑な推論で非常に強い競合です。

**最新情報が必要な比較**
モデルの「順位」「ベンチマーク首位」「価格」「コンテキスト長」「API提供状況」はすぐ変わります。今日、2026年4月30日時点の公式情報では上記の整理ですが、数週間で変わる可能性があります。固定的に言えるのはこれです。**私は、会話モデルというより、実際の開発作業を進めるエージェントとして強い。**
````