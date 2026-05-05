---
title: 'focus:100 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 focus:100。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `focus:100` (slider)

## 入力

**プロンプト**

```markdown
/mtp focus:100 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
2026年4月30日時点で確認できる範囲では、私の強みは「会話だけでなく、実際の作業環境で調査・編集・検証まで進めるコーディング／作業エージェントとしての実務性能」です。

| 比較軸 | 私の強み |
|---|---|
| ソフトウェア開発 | 既存コードを読み、局所修正、テスト、差分確認、レビューまで一連で進めやすい。単発回答より「作業完了」に寄せられる。 |
| 長い作業の継続 | 複数ファイル、曖昧な不具合、段階的な実装、検証ループに強い。OpenAIはGPT-5.5で特に「agentic coding」「computer use」「knowledge work」が伸びたと説明しています。 |
| 指示遵守と実務判断 | 既存の設計・慣習を尊重し、不要な大改造を避け、検証可能な形で進めるのが得意。 |
| ツール利用 | ローカルファイル、ターミナル、ブラウザ、Web検索、画像・文書・表計算系のツールを使い分けられる。 |
| 日本語での技術整理 | 実装方針、リスク、比較、レビュー指摘を日本語で短く構造化して出せる。 |

他社モデルとの相対比較では、断定は避けます。Anthropicは2026年4月16日にClaude Opus 4.7を出し、 coding・agents・vision・multi-step tasks の強化を公表しています。GoogleはGemini 3系でマルチモーダル理解、推論、Google製品連携を強く打ち出しています。xAIはGrok 4.20系やGrok 4.1 Fastで、長文コンテキスト、リアルタイム検索、ツール呼び出し、低コスト構成を前面に出しています。

要するに、Claudeはコード・長文推論・安全寄りの対話、GeminiはマルチモーダルとGoogleエコシステム、GrokはX/リアルタイム情報と長コンテキスト・速度/コスト面が比較対象として強い領域です。私の差別化点は、回答品質だけでなく「ユーザーの作業ディレクトリで、コードや資料を実際に動かしながら終わらせる」方向に最適化されていることです。

最新情報が必要な比較は、特に以下です。モデル順位、ベンチマーク、価格、コンテキスト長、API提供状況、安全性評価は数週間単位で変わるため、毎回確認が必要です。今回参照した主な公式情報は、[OpenAI GPT-5.5発表](https://openai.com/ms-BN/index/introducing-gpt-5-5/)、[Anthropic Newsroom](https://www.anthropic.com/news)、[Google Gemini 3発表](https://blog.google/products-and-platforms/products/gemini/gemini-3/)、[xAI APIモデル一覧](https://x.ai/api)です。
````