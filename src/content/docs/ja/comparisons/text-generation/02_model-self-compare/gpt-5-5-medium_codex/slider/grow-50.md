---
title: 'grow:50 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 grow:50。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `grow:50` (slider)

## 入力

**プロンプト**

```markdown
/mtp grow:50 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
**結論**
私の強みは、単発の回答性能よりも「実務タスクを最後まで進めるためのエージェント性」です。特にコードベースを読み、編集し、テストし、失敗を直し、作業内容を説明するような開発ワークフローでは強みが出ます。

**強みの枝分かれ**
1. **ソフトウェア開発の実行力**
   OpenAIのCodex系モデルは、長時間の実装、リファクタ、テスト修正、レビュー、端末操作を前提に最適化されています。OpenAIはGPT-5.3-Codexについて、SWE-Bench ProやTerminal-Benchで強い性能を示すと説明しています。  
   参照: [OpenAI GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex)

2. **作業環境との結合**
   私はこの会話内で、ローカルファイルを読んで、パッチを当て、コマンドを実行し、結果を踏まえて次の修正に進めます。これは「知識を答えるAI」より「作業するAI」に近い強みです。

3. **慎重な実務判断**
   既存コードの流儀を読み、不要な大改造を避け、テストや検証まで含めて進めるのが得意です。コードレビュー、バグ修正、設計整理、PR準備のような場面では、単純な生成力より重要になります。

4. **マルチステップ推論と説明**
   要件が曖昧なときに、仮定を置き、リスクを明示し、必要なら調査してから実装できます。単に「それっぽい答え」を返すより、作業可能な判断に落とす方向が強いです。

**他社主要モデルとの比較**
- **Claude系**: Claude Opus 4.5 / Sonnet 4.5 は、Anthropic自身が coding, agents, computer use に非常に強いと発表しています。特に長時間の自律作業やClaude Code文脈では強力な競合です。  
  参照: [Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5), [Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5)

- **Gemini系**: Gemini 3.1 Pro は、Googleが複雑な推論、マルチモーダル、大規模データ理解に向けた上位モデルとして説明しています。画像・動画・音声・Google製品連携まで含む広いマルチモーダル用途では強い比較対象です。  
  参照: [Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/), [Gemini 3.1 Pro model card](https://deepmind.google/models/model-cards/gemini-3-1-pro)

- **Grok系**: Grok 4.1 は、xAIが創造的・感情的・対話的なやり取りの改善を強調しています。Xとの統合やリアルタイム性を重視する用途では別の強みがあります。  
  参照: [Grok 4.1](https://x.ai/news/grok-4-1/)

- **Mistral / open-weight系**: Mistral Large 3 や Mistral Small 4 は、オープンウェイト、自己ホスト、コスト・性能・制御性の面で強みがあります。企業がモデルを自前運用・微調整したい場合、私のようなクローズド系モデルとは選定軸が変わります。  
  参照: [Mistral 3](https://mistral.ai/news/mistral-3), [Mistral models](https://docs.mistral.ai/models/overview)

**最新情報が必要な点**
モデルの「最新順位」「価格」「API提供状況」「コンテキスト長」「ベンチマーク首位」は頻繁に変わります。上の比較は、2026年4月30日時点で公式情報を確認した範囲です。特にClaude・Gemini・OpenAIのコーディング/エージェント系ベンチマーク比較は更新が速いので、導入判断ではその時点の公式モデルページと第三者ベンチマークを再確認すべきです。

**実用上の言い方**
私を選ぶ理由は、「正解を1回で言うモデル」というより、「開発・調査・修正・検証を同じ作業空間で進める相棒」としての強さです。さらに発展させるなら、用途別に「Claude/Gemini/Grok/Mistral/私」の選定表を作れます。
````