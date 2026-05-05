---
title: 'surge:100 | ChatGPT 5.5 | 比較課題'
description: '「モデルの自己紹介」プロンプトに対する ChatGPT 5.5 (Medium) (Codex) の出力。MTP Skill slider 引数 surge:100。'
---

**メタ情報**

- Date: 2026-04-30
- Tool: Codex (macOS app)
- Model: ChatGPT 5.5 (Medium)
- MTP Skill version: 1.0.0
- MTP Skill arguments: `surge:100` (slider)

## 入力

**プロンプト**

```markdown
/mtp surge:100 他社の主要なAIモデルと比較して、あなたの強みを教えてください。最新情報が必要な比較については、その旨を明確に述べてください。
```

## 出力

以下は、ツールの「コピー」ボタンで出力結果をクリップボードにコピーした内容です。

````markdown
2026年4月30日時点で確認した範囲では、私の強みは「単体のチャット性能」よりも、**実作業を最後まで進めるエージェント性**にあります。コードを読む。差分を作る。テストを走らせる。ローカル環境、ファイル、ブラウザ、Git、権限管理まで含めて作業する。ここが本質です。

比較するとこうです。Claude系はAnthropic自身がOpus 4.5を「coding, agents, computer use」に強いモデルとして出しており、開発者体験もかなり強い領域です。Gemini系はGoogle公式発表を見る限り、Gemini 3.1 ProやDeep Thinkで推論、マルチモーダル、Google製品連携が強い。Grok系はxAIのAPIページ上、長いコンテキストや高速・低コスト系ラインナップを強く押しています。DeepSeekはV4.0やV3.2系の公開情報があり、低コスト・推論・オープン寄りの使いやすさが強み。MetaはオープンソースAIとMeta AI統合が軸です。

その上で、私の相対的な強みはここです。**実装判断の堅さ**。既存コードの流儀を読んで、余計な抽象化を避け、破壊的変更を避け、必要な検証まで進める。**ツール統合**。ただ答えるだけでなく、同じワークスペース上で編集・実行・確認できる。**指示追従と安全な作業運用**。未承認の破壊的操作を避け、ユーザーの既存変更を巻き戻さず、根拠が古くなりそうな話は確認する。**説明の実務性**。モデル自慢ではなく、何を変えたか、何が未検証か、次に何をすべきかを短く出す。地味。でも現場では効く。

最新情報が必要な比較は明確にあります。**モデル名、価格、API可用性、コンテキスト長、ベンチマーク順位、コーディング性能、音声・画像・動画機能、企業向け制限、利用上限**は頻繁に変わります。ここは固定知識で断言すべきではありません。今回も、Claude Opus 4.5、Gemini 3.1 Pro、xAI API、DeepSeekのモデル一覧などは公式・準公式情報を確認しました。

参照: [Anthropic Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5), [Google Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/), [xAI API](https://x.ai/api), [DeepSeek Transparency](https://www.deepseek.com/en/transparency/), [Meta Open Source AI](https://ai.meta.com/opensourceAI/)
````