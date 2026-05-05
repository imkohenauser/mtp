---
title: 'collapse:50 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 collapse:50。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `collapse:50` (slider)

## 入力

**プロンプト**

```markdown
/mtp collapse:50 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
私の強みは、単純な「一問一答の賢さ」よりも、**実作業を最後まで進めるエージェント性能**にあります。

特に強いところは次です。

1. **コード作業の完遂力**
   既存コードを読んで、方針を立て、編集し、テストし、結果を報告する一連の作業が得意です。OpenAIのGPT-5.2系は公式に「coding and agentic tasks」に強いモデルとして説明されています。  
   参考: [OpenAI GPT-5.2 model](https://platform.openai.com/docs/models/gpt-5.2/), [Introducing GPT-5.2-Codex](https://openai.com/index/introducing-gpt-5-2-codex/)

2. **長い文脈と複数ファイルの整理**
   大きなコードベース、長文資料、仕様、ログをまたいで「何が問題か」「どこを直すべきか」をまとめるのが得意です。GPT-5.2は長文脈・ツール利用・複雑な多段タスクで改善が説明されています。  
   参考: [Introducing GPT-5.2](https://openai.com/index/introducing-gpt-5-2)

3. **ツール利用を前提にした実務**
   ターミナル、ファイル編集、ブラウザ確認、外部情報確認などを組み合わせて進められます。単に答えるだけでなく、同じワークスペースで実際に変更できます。

4. **指示追従と安全寄りの応答**
   危険な操作、曖昧な依頼、最新確認が必要な話題を切り分けて扱う設計です。これはスピードよりも、実務での失敗を減らす方向の強みです。

他社モデルとのざっくり比較では、**Claude Opus/Sonnet系**はコード・エージェント・文章品質で非常に強く、AnthropicもOpus 4.5を「coding, agents, computer use」に強いと説明しています。  
参考: [Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)

**Gemini 3 Pro**は特にマルチモーダル、長い入力、Google検索・Google製品連携まわりで強いです。公式ドキュメントでは100万トークン級の入力や画像・音声・動画・PDF入力が示されています。  
参考: [Gemini models](https://ai.google.dev/gemini-api/docs/models)

**Grok系**はX連携、リアルタイム性、長文脈、会話の個性を強く打ち出しています。xAIの公式ドキュメントではGrok 4.20に200万トークン文脈などが示されています。  
参考: [xAI Docs](https://docs.x.ai/docs)

明確に言うと、**ベンチマーク順位、価格、利用可能モデル、文脈長、各社の最新リリース状況は頻繁に変わるため、最新比較には都度確認が必要**です。今回もその前提で公式情報中心に確認しました。
````