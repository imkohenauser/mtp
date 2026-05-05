---
title: 'still:100 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 still:100。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `still:100` (slider)

## 入力

**プロンプト**

```markdown
/mtp still:100 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
2026年4月30日時点の公開情報ベースです。モデル名、価格、ベンチマーク順位は頻繁に変わるため、そこは最新確認が必要です。

私の強みは、単なる回答モデルというより、**作業を完了するためのエージェント性**です。

- **コード作業の実行力**: ローカルのコードを読み、編集し、テストし、差分をまとめる流れに強い。OpenAIはGPT-5.5について、コーディング、オンライン調査、データ分析、ドキュメント・スプレッドシート作成、ツール横断作業が強いと説明しています。出典: [OpenAI GPT-5.5](https://openai.com/ta-IN/index/introducing-gpt-5-5/)
- **曖昧な依頼の分解と完了**: 「何を調べ、何を直し、どう検証するか」を自走しやすい。これはClaudeやGeminiも強い領域ですが、私はこのCodex環境ではファイル操作・検証・実装の一連作業に寄っています。
- **実務寄りの慎重さ**: 既存コードの流儀、テスト、差分、壊してはいけない変更を重視する。文章生成だけでなく、ソフトウェアエンジニアリングの進め方に最適化されています。
- **OpenAIツール群との統合**: Web検索、コード実行、画像、ドキュメント、スプレッドシート、ローカル開発補助などを一つの作業文脈で扱いやすい。

他社との大まかな比較:

| 相手 | 相手の強み | 私の相対的な強み |
|---|---|---|
| Claude Opus 4.7 / Sonnet 4.6 | 長時間の推論、コーディング、指示追従、1M context。Opus 4.7は2026年4月16日公開で、複雑な長時間タスクや高解像度 vision を強調。出典: [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7), [Claude Sonnet 4.6](https://www.anthropic.com/research/claude-sonnet-4-6) | Codex環境での実装、修正、検証、作業完了までの一体感 |
| Gemini 3 Pro / Flash | マルチモーダル、1M context、Google検索・PDF・音声・動画入力などの広い対応。出典: [Gemini models](https://ai.google.dev/gemini-api/docs/models/gemini), [Gemini 3 guide](https://ai.google.dev/gemini-api/docs/gemini-3?hl=en) | ローカル開発・コードベース作業・変更管理に寄った実務遂行 |
| Grok 4.20 / 4.1 | 2M context、速度、低価格、X/検索連携、ツール呼び出し。出典: [xAI API](https://x.ai/api), [xAI Docs](https://docs.x.ai/overview?src=aicpb) | 回答の制御、実装作業、検証込みの堅実な開発支援 |
| Llama系 open-weight | 自前ホスト、カスタム、データ管理、コスト制御。Llama 4系は公開・自前運用の利点が大きい。 | 運用不要で高度な推論・ツール利用・作業代行をすぐ使える |

結論:  
私の一番の強みは、**「考える」だけでなく、コードやファイルを触って実務を進める能力**です。最新のベンチマークだけで見ればClaude、Gemini、Grokが特定領域で上回る可能性は常にありますが、Codex環境では「調査、実装、検証、報告」を一つの流れで処理できる点が中核の強みです。
````