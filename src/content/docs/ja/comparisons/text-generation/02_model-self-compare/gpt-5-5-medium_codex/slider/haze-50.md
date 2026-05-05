---
title: 'haze:50 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 haze:50。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `haze:50` (slider)

## 入力

**プロンプト**

```markdown
/mtp haze:50 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
私の強みは、単体の「答えるAI」というより、**作業を最後まで進める実務型のAI**として出やすいです。

特に強いのは、コードベースを読んで、変更方針を立て、実装し、テストや検証まで回すような仕事です。OpenAIのCodex/GPT系は、公式にも「agentic coding」「computer use」「knowledge work」への最適化が強調されています。つまり、曖昧な依頼を受けて、ファイルを調べ、必要な編集をし、壊れていないか確認する流れで力を出しやすい、ということです。  
参考: [OpenAI GPT-5.5](https://openai.com/ms-BN/index/introducing-gpt-5-5/), [Codex upgrades](https://openai.com/index/introducing-upgrades-to-codex/)

他社モデルと比べるなら、ざっくりこうです。

**Claude系**は、長文読解、自然な文章、慎重な推論、設計相談に強い印象があります。AnthropicもClaude Opus/Sonnet系を複雑推論や高度なコーディング向けとして位置づけています。私の側は、会話だけでなくローカル環境の操作、ファイル編集、検証を一体で進める場面で強みが出やすいです。  
参考: [Anthropic Models Overview](https://docs.anthropic.com/en/docs/models-overview)

**Gemini系**は、Google製品との接続、マルチモーダル、長いコンテキスト、検索・動画・画像・Googleエコシステム寄りの作業に強い地形があります。GoogleはGemini 3/3.1 Proで推論、マルチモーダル、エージェント的作業を強調しています。私の強みは、特に開発環境の中で「調べる、直す、確認する」を粘り強く回す部分に寄ります。  
参考: [Gemini 3](https://blog.google/products/gemini/gemini-3), [Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)

**Llama/Meta系やMistral系**は、オープンウェイト、自己ホスト、コスト管理、カスタマイズ性が魅力になりやすいです。企業が自前環境に置きたい場合には、この自由度が大きな価値になります。私はその代わり、OpenAI/Codex側の統合された推論・編集・検証ワークフローで勝負するタイプです。

最新情報が必要な比較は、**ベンチマーク順位、価格、利用可能地域、API制限、最新モデル名、企業向け機能、コンテキスト長、画像・動画・音声対応範囲**です。このあたりは数週間で景色が変わるので、断定するなら都度確認が必要です。

短く言えば、私の強みは「きれいな一問一答」より、**現場の机の上に散らばった資料やコードを拾い集めて、実際に形にしていくこと**にあります。
````