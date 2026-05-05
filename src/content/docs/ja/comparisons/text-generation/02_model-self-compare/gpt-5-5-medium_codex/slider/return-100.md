---
title: 'return:100 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 return:100。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `return:100` (slider)

## 入力

**プロンプト**

```markdown
/mtp return:100 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
**そもそも正しい問いか？**

「他社モデルと比べて、あなたの強みは何か？」は少し危うい問いです。AIモデルの優劣は、モデル単体ではなく、用途、ツール環境、推論設定、価格、レイテンシ、コンテキスト長、評価ベンチ、UI統合で変わります。

なので、より正確にはこうです。

**このCodex環境の私が強いのは、“単発回答の賢さ”だけでなく、コード・ファイル・ツール・検証を含む作業を最後まで進める場面です。**

**私の主な強み**

1. **実務的なコーディング作業**
   私はコードベースを読んで、既存設計に合わせて変更し、テストやビルド確認まで進める用途に強いです。単にコード片を返すより、リポジトリ内で実際に編集・検証・差分説明する作業に向いています。OpenAIもGPT-5.3-Codexを「agentic coding」向けモデルとして位置づけています。[OpenAI: GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex)

2. **長めの作業を分解して進める力**
   調査、実装、検証、修正、報告のような複数段階の仕事で強みが出ます。特に「曖昧な依頼を、実際に動く成果物へ落とす」タイプの仕事です。OpenAIのGPT-5.2系も、専門的な知識作業、長時間エージェント、ツール利用、複雑な多段タスクを重視して説明されています。[OpenAI: GPT-5.2](https://openai.com/index/introducing-gpt-5-2/)

3. **開発者向けの協調性**
   私は途中経過を説明し、方針を変えられ、ローカルファイルやターミナル結果を踏まえて作業できます。Claude、Gemini、Grok、Mistralなども強力ですが、この環境では「会話AI」より「共同作業する開発エージェント」として振る舞える点が差別化になります。

4. **ツール利用を前提にした正確性**
   不確かなことを記憶だけで断言せず、必要ならファイル、公式ドキュメント、Web、テスト結果を確認して答えられます。特に現在情報、依存関係、API仕様、モデルラインアップのように変わりやすい情報ではこの点が重要です。

5. **汎用知識作業と実装の接続**
   仕様整理、設計判断、PRレビュー、データ分析、ドキュメント作成、UI実装などを分断せずにつなげやすいです。単なる文章生成ではなく、「考えた結果をファイルやコードに反映する」ところまで行けます。

**他社モデルとの比較で見ると**

Claudeは長文読解、文章品質、慎重な推論、コーディングで非常に強い競合です。AnthropicはClaude Opus 4.7を高度なソフトウェアエンジニアリングや長時間タスクで改善したと説明しています。[Anthropic: Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)

GeminiはGoogle製品、長コンテキスト、マルチモーダル、検索・Workspace連携で強みがあります。Google DeepMindのモデルカード一覧を見ると、Gemini 3.1 ProやFlash系など用途別の展開が進んでいます。[Google DeepMind model cards](https://deepmind.google/models/model-cards/)

GrokはxAIのエコシステム、Xとの接続、非常に大きいコンテキストや高速性を打ち出しています。xAI docsではGrok 4.20を最新旗艦モデルとして説明しています。[xAI Docs](https://docs.x.ai/docs)

Mistralはオープンウェイト、自社運用、欧州・企業向け制御性、軽量モデルで強みがあります。Mistral Large 3やMistral Medium系は、自己ホストやカスタム展開を重視する場合に魅力があります。[Mistral models](https://docs.mistral.ai/models/overview)

MetaはLlama系やMeta AI、研究モデル、オープンソース寄りのエコシステムが強みです。最新のMeta AI周辺はMuse Sparkなども含めて急速に変わっています。[Meta AI blog](https://ai.meta.com/blog)

**最新情報が必要な比較**

以下は、今日時点でも変わりやすいので、厳密に比較するなら必ず最新の公式情報と独立ベンチマーク確認が必要です。

- どのモデルが「最強」か
- SWE-bench、Terminal-Bench、GPQA、MMLU、AIMEなどの順位
- API価格、レート制限、コンテキスト長
- ChatGPT、Claude、Gemini、Grok、Mistral、Meta AIの最新モデル名
- 企業向け機能、データ保持、リージョン、セキュリティ条件
- コーディングエージェントとしての実環境性能

**逆向きに言うと**

もし問いを「どのAIが一番賢いか？」にすると、私は必ずしも常に一位とは言えません。Claudeが合う仕事、Geminiが合う仕事、GrokやMistralやLlama系が合う仕事はあります。

ただし、「開発環境の中で、調査し、編集し、検証し、説明しながら成果物を作る」なら、私の強みはかなり明確です。私の価値はモデル単体のIQより、作業を前に進める実行力にあります。
````