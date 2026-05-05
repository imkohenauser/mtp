---
title: 'collapse:100 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 collapse:100。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `collapse:100` (slider)

## 入力

**プロンプト**

```markdown
/mtp collapse:100 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
私はGPT-5系のCodexとして見ると、強みは「実作業を最後まで進める力」です。コードベースを読み、ファイルを編集し、テストを走らせ、失敗を見て直す、という開発ワークフローに強いです。単発の回答より、調査、実装、検証、説明までを同じ文脈で続ける用途に向いています。

Claude系と比べると、強みは開発環境との統合、リポジトリ作業、ツール実行、長めの実装タスクです。Claude Opus 4.5などは公式に「coding, agents, computer use」に強いとされており、純粋なモデル比較は最新ベンチマーク確認が必要です。https://www.anthropic.com/news/claude-opus-4-5

Gemini系と比べると、Geminiは巨大なマルチモーダル入力や長文コンテキストで強みがあります。Google公式ではGemini 2.5 Proが100万トークン級の入力、音声・画像・動画・PDF対応を示しています。私の強みは、その広い入力処理そのものより、ローカル作業・コード変更・検証を実行するエージェント性です。https://ai.google.dev/gemini-api/docs/models

OpenAI内で言えば、Codex系は通常の会話モデルより「実際のソフトウェアエンジニアリング」に寄っています。OpenAI公式でもGPT-5.3-Codexは長時間タスク、ツール利用、複雑な実行に焦点があると説明されています。https://openai.com/index/introducing-gpt-5-3-codex

最新情報が必要なのは、「どのモデルが今ベンチマーク1位か」「料金」「コンテキスト長」「API提供状況」「企業向け制限」「最新モデル名」です。これらは頻繁に変わるため、厳密比較では必ず当日の公式情報確認が必要です。
````