---
title: MTP Playlist Skill
description: MTP Playlist を使い、テーマ、ジャンル、アーティスト、アルバム、時代、シーン、音世界を、MTP に基づく意図的な音楽シーケンスへ変換します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp-playlist.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_skills_mtp-playlist.png
lastUpdated: true
---

MTP Playlist は、Mapping the Prompt（MTP）フレームワークで音楽シーケンスを作る **Agent Skill（エージェントスキル）** です。

単なるムード別の曲リストではありません。  
各曲を MTP のノードへ対応させ、「なぜこの曲か」「なぜこのノードか」「なぜこの順番か」を説明できるプレイリストとして構成します。  
Markdown で読めるプレイリスト成果物を出力します。

- [MTP Playlist Skill zip をダウンロード](/downloads/mtp-playlist-skill.zip)
- [インストール手順](/ja/skills/)

---

## 基本的な使い方

`/mtp-playlist` の後にテーマを書いて、スキルを明示的に呼び出します。

### アーティスト、曲、テーマを指定する

ジャンル、グループやレーベル、時代、シーン、さまざまなキーワードで、プレイリストの方向を指定します。

```text
/mtp-playlist Morning 6AM
/mtp-playlist Mozart for Spring, 60-tracks
/mtp-playlist Madness in Classical Music
/mtp-playlist Mephistophelean Classics
/mtp-playlist Modern Jazz with Vibraphone
/mtp-playlist Melancholic Bossa Nova and Saudade
/mtp-playlist Movie Drive Songs
/mtp-playlist Moonlit 80s Heavy Metal
/mtp-playlist Motown Deep Cuts
/mtp-playlist Michael Jackson, Minor Songs
/mtp-playlist Mic Relay 1970s–1980s Rap
/mtp-playlist Marley’s Rock
/mtp-playlist MDR, Berghain Techno
/mtp-playlist Marilyn Manson Side B, David Bowie Side A
/mtp-playlist Madonna 2026
```

### 特定の曲を特定のノードにアンカーする

特定の曲を MTP ノードに固定し、そこから全体の流れを組み立てる使い方です。  
好きな曲や象徴的な曲を Start、Helix、Abyss、Collapse などに置くと、同じ曲でも周辺の選曲と全体の印象が変わります。

```text
/mtp-playlist Marvin Gaye "Inner City Blues" at Abyss, 70s Soul
/mtp-playlist MJB "Real Love" at Helix, 90s R&B
/mtp-playlist Mobb Deep "Shook Ones Pt. II" at Start, 90s New York Rap
/mtp-playlist Missy Elliott "Get Ur Freak On" at Start, Y2K Hip-Hop
/mtp-playlist Merry Christmas Mr. Lawrence at Collapse, Piano
```

---

## プレイリストの形式

デフォルトでは、`1+9+9+1` の構成で 20 曲のシーケンスを作ります。

* `#1 Start`
* `#2–10` Side A
* `#11–19` Side B
* `#20 End`

指定すれば、ほかの長さや範囲にもできます。  
10 曲の Side A / Side B、30 曲、40 曲、60 曲、または元のアルバムや候補曲が少ない場合の短いマッピングを指定できます。

この順序モデルについては、[分類と順序](/ja/optional/mapping-and-sequence/) を参照してください。

---

## 出力されるもの

このスキルは Markdown の **プレイリスト成果物** を作ります。  
スキル単体では、音楽アプリ上で再生できるプレイリストは作りません。

Apple Music アカウントを連携した ChatGPT では、成果物の曲リストから Apple Music 上のプレイリストを作れます。  
そのときは、成果物に含まれる「コピーしやすい曲リスト」をそのまま渡せます。

内容は次のとおりです。

* タイトルと短い説明
* 元のプロンプト
* プレイリストのメタデータ
* コピーしやすい曲リスト
* 曲目とノードの対応表
* 選曲理由と説明

各行では、その曲が割り当てられたノードをどのように機能させているかを説明します。  
説明は、音、リズム、編曲、歌唱、歌詞、プロダクション、歴史的役割、シーン上の機能、文化的効果など、実際に聴こえる根拠に基づきます。

---

## MTP Playlist が扱う課題

プレイリストは、曲の集合にはなっても、曲順を持つ一つの体験にはなりにくいです。  
MTP Playlist は、ノード配置と説明によってそのずれを扱います。

### 曲順の意図

多くのプレイリストでは、選曲理由も曲順の意図も見えにくくなります。

MTP Playlist では各曲に位置と理由を与えるため、曲順とその意図を、聴くだけでなく読んでも追えます。

### 条件と音楽体験の違い

AI 生成プレイリストは、ジャンル、ムード、時代、活動、アーティストなどの条件に合う曲を集めることを得意とします。  
しかし、条件に合う曲を集めることと、曲順を持つ音楽体験を作ることは同じではありません。

MTP Playlist は、曲を選ぶだけではなく、その曲がシーケンスの中でどの役割を担うのかを決めます。

### 定番と発見のバランス

プレイリストは、定番曲に寄りすぎると既視感が強くなり、発見を増やしすぎると流れが壊れやすくなります。

MTP Playlist では、曲の知名度よりも、その位置での役割を重視します。  
有名曲は、アンカーや中心として使われます。  
知名度の低い曲や周辺的な曲も、その位置に必要であれば選ばれます。

### シャッフルとの違い

シャッフルは、曲順の既視感を崩すことができます。  
しかし、曲順そのものの意味も壊します。

MTP Playlist は、曲順をランダム化して新鮮さを作るのではありません。  
同じ構造の中に別の曲を配置することで、新しい解釈を作ります。

### モデルごとの解釈

MTP Playlist は、すべてのモデルに同じ正解を出させるためのスキルではありません。

同じテーマでも、モデルやキュレーターによって選曲は変わります。  
軽量のモデルでは、探索時間が短く、文脈の保持も限られるため、前後の曲との整合を十分に見直せず、選曲が狭くなりやすいです。

学習データのカットオフにより、最新のリリース状況や流行を反映できないことがあります。  
制約自体を厳密に守る出力もあれば、物語性を重視する出力や、代表曲を多めに使う出力もあります。

この違いは、DJ ごとの違いに近いものです。  
MTP Playlist は、同じテーマでも選曲と説明がどう変わるかを比較するためのスキルです。

---

## 免責事項

MTP Playlist は、選曲、曲順、配置理由の説明を支援するスキルです。  
音楽再生環境やストリーミングサービスに関する問題まで扱うものではありません。

- 曲ごとの音量差、マスタリング差、録音差の補正
- DJ ミックス、クロスフェード、BPM 同期、キー合わせ、音量オートメーションの実行
- Apple Music、Spotify、YouTube Music などでの各曲の利用可否の保証

楽曲情報の正確性は、利用できるモデル、検索環境、音楽データベースへのアクセスに依存します。  
ユーザーの再生履歴、ライブラリ、いいね、スキップ傾向を自動的に読むことも前提にしていません。
