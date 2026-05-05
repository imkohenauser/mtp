---
title: 'flow:100 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 flow:100。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `flow:100` (slider)

## 入力

**プロンプト**

```markdown
/mtp flow:100 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
私の強みは、単に答えを出すことよりも、**作業を分解し、ツールを使い、検証しながら最後まで進める「実務エージェント」寄りの動き**にあります。特にこのCodex環境では、コードベースを読み、ファイルを編集し、テストを走らせ、必要ならブラウザや外部資料で確認する、という流れを会話の中で継続できます。

Claude系と比べると、Claudeは長文読解、自然な文章、長コンテキスト、慎重な推論で非常に強いモデルです。Anthropicは最新のClaude Opus/Sonnet系について、 coding、agents、computer use、1M token context などを強調しています。一方で私の強みは、説明だけで終わらず、ローカルの開発環境・ファイル・テスト・差分確認まで含めて作業を進める点にあります。つまり「相談相手」としてだけでなく「作業者」として使いやすいところです。

Gemini系と比べると、GeminiはGoogle製品との統合、マルチモーダル処理、検索・動画・画像・Android/Workspace周辺との親和性が大きな強みです。GoogleはGemini 3/3.1 Proを高度な推論、マルチモーダル、agentic workflows向けとして発表しています。これに対して私は、ソフトウェア開発、ドキュメント生成、データ処理、レビュー、修正、検証のような「成果物を作って整える」作業に強く寄っています。

MistralやLlamaなどのオープン寄りモデルと比べると、相手側の強みは自己ホスト、カスタマイズ、コスト制御、データ統制です。Mistral 3やLlama系は、組織が自分の環境で動かしたい場合に魅力があります。一方で私は、モデル単体の自由度よりも、推論・ツール利用・安全制御・開発ワークフロー統合が最初からまとまっている点が強みです。

ただし、**「どのモデルが今ベンチマークで1位か」「価格が最安か」「APIで使える最新モデルは何か」「最大コンテキスト長はどれが最大か」**のような比較は、更新頻度が高いため最新確認が必要です。実際、OpenAIは2026年4月23日にGPT-5.5を発表し、ChatGPT/Codexでの展開やAPI提供状況は段階的だと説明しています。AnthropicやGoogleも2026年に複数の新モデルや更新を出しており、この種の順位比較は日付つきで見るべきです。

要するに、私の一番の強みは「幅広く説明できること」だけではなく、**複雑な依頼を実作業に落とし込み、コード・文章・調査・検証をまたいで進められること**です。最新モデル同士の純粋な性能比較は常に動きますが、現時点の実用面では、開発・調査・編集・レビューを一つの流れで扱える点が特に強いです。

参考: [OpenAI GPT-5.5](https://openai.com/fi-FI/index/introducing-gpt-5-5/), [OpenAI GPT-5.5 System Card](https://openai.com/index/gpt-5-5-system-card/), [Anthropic Newsroom](https://www.anthropic.com/news), [Google Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/), [Mistral 3](https://mistral.ai/news/mistral-3)
````