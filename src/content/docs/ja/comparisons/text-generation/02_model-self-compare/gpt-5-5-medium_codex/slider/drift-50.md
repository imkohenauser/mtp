---
title: 'drift:50 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 drift:50。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `drift:50` (slider)

## 入力

**プロンプト**

```markdown
/mtp drift:50 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
私の強みは、ざっくり言うと **「実務を進めるための推論・コーディング・ツール利用の統合」** です。単発の回答より、コードベースを読み、変更し、検証し、途中で判断を更新するような作業で強みが出ます。

他社モデルとの比較で安定して言えるのは次のあたりです。

- **Claude系との比較**: Claudeは長文読解、文章品質、慎重な対話、知識作業で強い印象があります。私はそれに対して、開発環境内でのコード探索、修正、テスト、差分説明のような「作業完了型」の流れに強みがあります。なお、Claudeの最新ラインナップや性能順位は頻繁に変わるため、厳密な最新比較には最新ベンチマーク確認が必要です。Anthropic公式ではClaude Opus/Sonnet/Haiku系が用途別に整理されています。[Anthropic product](https://www.anthropic.com/product)

- **Gemini系との比較**: Geminiは巨大コンテキスト、マルチモーダル入力、Google検索・Google系エコシステムとの親和性が強い領域です。Google公式ではGemini 3 Pro PreviewやGemini 2.5系に、100万トークン級コンテキストや画像・音声・動画・PDF入力対応が示されています。[Gemini models](https://ai.google.dev/gemini-api/docs/models) 私の強みは、長いコンテキストそのものより、指示を分解して実装・検証まで進めるエージェント作業です。

- **Grok系との比較**: Grokはリアルタイム性、X周辺の情報アクセス、速い応答、広い文脈取得を打ち出しています。xAI公式ではGrok 4.20をフラッグシップとして説明しています。[xAI docs](https://docs.x.ai/) ただし「幻覚率が最も低い」「最速」などの順位主張は、測定条件次第なので最新の独立評価が必要です。

- **Llama / Meta系との比較**: LlamaやMetaの強みは、オープンソース／オープンウェイト寄りの展開、自前ホスティング、カスタム微調整、コスト管理です。MetaもオープンソースAIの価値を前面に出しています。[Meta open source AI](https://ai.meta.com/opensourceAI/) 私はモデル重みをユーザーが自由にホストできるタイプではない一方、会話・ツール・コード編集・検証が統合された作業支援に寄っています。

私自身については、OpenAI公式のモデル一覧ではGPT-5系やCodex系が「coding and agentic tasks」に強いモデル群として説明されています。[OpenAI models](https://platform.openai.com/docs/models) この会話環境での実用上の強みは、特に **コード修正、リファクタ、バグ調査、設計判断、テスト実行、変更内容の説明** です。

最新情報が必要な比較は、具体的には **ベンチマーク順位、価格、コンテキスト長、API対応機能、最新モデル名、速度、幻覚率、コーディング性能ランキング** です。これらは数週間単位で変わるので、厳密に選定するなら、その時点の公式ドキュメントと独立ベンチマークを確認すべきです。
````