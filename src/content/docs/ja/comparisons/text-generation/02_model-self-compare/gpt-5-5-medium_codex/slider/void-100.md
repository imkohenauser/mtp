---
title: 'void:100 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 void:100。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `void:100` (slider)

## 入力

**プロンプト**

```markdown
/mtp void:100 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
この比較は変動が速いです。特に「最新モデル名」「ベンチマーク順位」「価格」「コンテキスト長」「各社ツール連携」は、最新情報確認が必要です。以下は公開情報ベースです。

主な強みは、実務コード作業です。

- 大規模リポジトリを読み、編集し、テストし、差分をまとめる作業に向く
- 長時間の実装、リファクタ、移行、デバッグを継続しやすい
- ターミナル、ファイル編集、テスト実行、ブラウザ確認を組み合わせた「作業完了型」の進め方が得意
- コードレビュー、欠陥発見、セキュリティ寄りの確認に強い
- ユーザーの方針変更を途中で取り込みやすい

比較すると、

Claude Opus/Sonnet系は、コーディング、計画、コンピュータ操作、文書・表計算作業が非常に強い。Anthropic自身もOpus 4.5を「coding, agents, computer use」に強いモデルとして説明している。  
出典: [Anthropic Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)

Gemini 3系は、マルチモーダル理解、視覚・動画・Google製品連携が強い。GoogleはGemini 3を推論、マルチモーダル、コーディングで強いモデルとして発表している。  
出典: [Google Gemini 3](https://blog.google/products/gemini/gemini-3)

Grok系は、巨大コンテキスト、リアルタイム検索、X連携、ツール呼び出しを前面に出している。xAIのAPIページではGrok 4.20に2Mコンテキストなどが示されている。  
出典: [xAI API](https://x.ai/api/)

Codex/GPT-5系の公開情報では、OpenAIはGPT-5.3-Codexを、SWE-Bench Pro、Terminal-Bench、OSWorldなどの実務・エージェント評価で強いモデルとして説明している。  
出典: [OpenAI GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex)

短く言えば、強みは「会話だけでなく、実際の開発環境で読んで、直して、検証して、仕上げる」部分です。最新順位や価格の断定には、その時点の公式ページ確認が必要です。
````