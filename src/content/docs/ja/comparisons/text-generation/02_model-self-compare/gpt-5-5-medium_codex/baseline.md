---
title: 'baseline | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) のベースライン出力（MTP Skill 未適用）。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill: (none)

## 入力

**プロンプト**

```markdown
他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
2026年4月30日時点の公式情報ベースで言うと、私の強みは「単なるチャット回答」よりも、**開発環境の中で調査、編集、実行、検証まで進めるエージェント作業**にあります。

**私の強み**
- **実装まで進める能力**: コードを読んで、差分を作り、テストやコマンド実行で確認し、結果を要約できます。相談役というより、作業者として動けます。
- **長めの開発タスクへの適性**: OpenAIはGPT-5.3-Codexについて、長時間の研究、ツール利用、複雑な実行を伴うタスク向けで、SWE-Bench ProやTerminal-Benchで強いと説明しています。参考: [OpenAI GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex)
- **対話しながら軌道修正しやすい**: 作業中に方針変更や追加指示を受けても、文脈を保ったまま進める設計です。
- **実務寄りの堅さ**: 既存コードの流儀、差分の小ささ、テスト、破壊的操作の回避、ユーザー変更の尊重など、ソフトウェア開発の実務ルールに寄せて動きます。
- **ローカル作業との統合**: このCodex環境では、ファイル操作、ターミナル、場合によってはブラウザ検証やドキュメント生成まで扱えます。

**他社モデルとの比較**
- **Claude Opus 4.7**: Anthropicは、Claude Opus 4.7をコーディング、AIエージェント、長いマルチステップ作業に強いモデルとして説明しており、1Mコンテキストや高解像度ビジョンも強みです。比較対象として非常に強いです。参考: [Anthropic Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- **Gemini 3**: GoogleはGemini 3を、推論、マルチモーダル理解、Google製品・Vertex AI連携に強いモデルとして出しています。画像、動画、Googleエコシステム重視なら有力です。参考: [Google Gemini 3](https://blog.google/products/gemini/gemini-3)
- **Mistral / DeepSeek / Llama系**: オープンウェイト、自己ホスト、低コスト、カスタマイズ性が重要なら強みがあります。Mistral Large 3はApache 2.0のオープンモデルとして発表されています。DeepSeekもV4を公開モデルとして掲載しています。参考: [Mistral Large 3](https://mistral.ai/news/mistral-3), [DeepSeek Transparency](https://www.deepseek.com/en/transparency/)

**最新情報が必要な比較**
ベンチマーク順位、価格、API提供状況、コンテキスト長、利用制限、企業向け機能は頻繁に変わります。特に「どれが今いちばん賢いか」「コーディングで最強か」「一番安いか」を判断するには、導入直前に各社の公式モデルページ、料金表、第三者ベンチマークを再確認する必要があります。

要するに、私の強みは**実務開発を会話だけで終わらせず、手元の環境で前に進めること**です。一方で、純粋な最大コンテキスト、特定ベンチマーク、完全オープン運用では、Claude、Gemini、Mistral、DeepSeek、Llama系が用途によって勝つ場面があります。
````