---
title: カラーグリッドの可視化
description: MTP のカラーグリッド SVG を生成するスクリプトと、グリッドサイズごとの可視化アセットを説明します。
head:
  - tag: meta
    attrs:
      property: og:image
      content: https://mappingtheprompt.com/ogp/ja_optional_color-grid-visualization.png
  - tag: meta
    attrs:
      name: twitter:image
      content: https://mappingtheprompt.com/ogp/ja_optional_color-grid-visualization.png
lastUpdated: true
---

このドキュメントで説明するスクリプトは、MTP のカラーグリッドの SVG を出力します。これは、グリッドと座標系で解説した空間モデルと強度モデルを可視化し、将来予定するインタラクティブな生成 UIへ展開するためのものです。

## グリッドのバリアント

複数の SVG が `public/images/grids/` に置かれています。`package.json` の `scripts` には `build:grid`、`build:grid-10x10`、`build:grid-28x28`、`build:grid-37x37` が定義されており、`scripts/mtp_grid_generator.py` からパスを手で書き換えずに再生成できます。

ファイル名の数字は、一辺あたりの **線（格子線の本数）** に対応します。*N*×*N* セルの市松は (*N*+1)×(*N*+1) 本の線で囲まれるため、既定の 18×18 セルは `mtp-grid-19x19.svg` になります。

| プレビュー | 線（一辺） | セル | パス |
| :---: | :--- | :--- | :--- |
| <img src="../../../images/grids/mtp-grid-37x37.svg" alt="MTP カラーグリッド（37×37 線、36×36 セル）" width="200"> | 37×37 | 36×36 | `public/images/grids/mtp-grid-37x37.svg`（`build:grid-37x37`） |
| <img src="../../../images/grids/mtp-grid-28x28.svg" alt="MTP カラーグリッド（28×28 線、27×27 セル）" width="200"> | 28×28 | 27×27 | `public/images/grids/mtp-grid-28x28.svg`（`build:grid-28x28`） |
| <img src="../../../images/grids/mtp-grid-19x19.svg" alt="MTP カラーグリッド（19×19 線、18×18 セル）" width="200"> | 19×19 | 18×18 | `public/images/grids/mtp-grid-19x19.svg`（`build:grid`） |
| <img src="../../../images/grids/mtp-grid-10x10.svg" alt="MTP カラーグリッド（10×10 線、9×9 セル）" width="200"> | 10×10 | 9×9 | `public/images/grids/mtp-grid-10x10.svg`（`build:grid-10x10`） |

## 仕組み

ジェネレータは空間モデルと配色セットを 1 組だけ使い、プリセット間ではグリッドのサイズ（とセルあたりのピクセル幅）だけが変わります。既定の成果物は **18×18 セル** のグリッドです（**19×19** の線の交点に挟まれたセル部分）。

- **セルの色** は **色相環** に由来します。各セルについて、中心からの角度によって決まります。
- **不透明度 / 明るさ** は **チェビシェフ距離**（Volcano モデル）に由来します。距離 6 で強度が最大になり、中心と外枠へ向かうにつれて弱まります。
- 色付きグリッドの下には、透明度を示すための **市松模様（チェッカーボード）のレイヤー** が描かれます。背景矩形、市松模様の色、配色ペアは、スクリプト冒頭で定義されています。

原色や色相環の色の厳格な指定は必須ではありませんが、このスクリプトはグリッドの配色関係を守るように設計されています。`inner_palette` と `outer_palette` は、1 枚の SVG 内での内側と外側の色アンカーです。

## SVG の生成

リポジトリのルートで次を実行します。

```bash
npm run build:grid
npm run build:grids
```

`npm` スクリプトは、対応する `public/images/grids/` 配下のファイルへ直接書き出します。標準出力へ生の SVG を出したい場合は、Python スクリプトを直接呼び出します。

```bash
python3 scripts/mtp_grid_generator.py --grid-28x28
python3 scripts/mtp_grid_generator.py --grid-37x37
```

---

## MTP Interactive UI プレビュー

予定している **MTP Interactive UI** では、生成された 19×19 の SVG カラーグリッドを中央の座標面として使います。以下の画像は、グリッドを中央に配置し、周囲に座標ラベルを加えた UI プレビューです。現在は、グリッド座標と色の対応関係を確認するために掲載しています。

| バリエーション A | バリエーション B | バリエーション C |
| :---: | :---: | :---: |
| <img src="../../../images/pages/mtp-ui-grid-guide--a.png" alt="MTP Interactive UI バリエーション A" width="320" loading="lazy" decoding="async"> | <img src="../../../images/pages/mtp-ui-grid-guide--b.png" alt="MTP Interactive UI バリエーション B" width="320" loading="lazy" decoding="async"> | <img src="../../../images/pages/mtp-ui-grid-guide--c.png" alt="MTP Interactive UI バリエーション C" width="320" loading="lazy" decoding="async"> |

この UI プレビュー A の中央にある画像は、`scripts/mtp_grid_generator.py` から既定の `mtp-grid-19x19.svg` として生成されたものです。UI フレーム側で列ラベル `A`–`S` と行ラベル `1`–`19` を加えているため、同じ表示を `/mtp <column:row>` の位置確認用シートとしても利用できます。

たとえば、`J:10` はニュートラルな中心を示し、`J:4`、`D:16`、`P:16` のような座標は、ラベル付きグリッド上で位置を確認してから `/mtp` に渡せます。