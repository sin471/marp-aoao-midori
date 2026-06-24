# aoao-midori — Marp テーマ

ブルー＆ティールを基調にした、落ち着いた配色の [Marp](https://marp.app/) 用スライドテーマです。
表紙・セクション扉・本文に加え、**文献調査**スライドと**落合フォーマット**スライドのレイアウトを同梱しています。

## 特徴

- 上端左寄せの2色アクセントバー（ブルー → ティール）
- 表紙（`title`）／セクション扉（`section`）／本文の3種レイアウト
- 研究発表向けの追加レイアウト
  - **文献調査**（`lit`）— 論文タイトル・和訳・出典・被引用数バッジを並べるカード
  - **落合フォーマット**（`ochiai`）— 「どんなもの？／先行研究比／手法のキモ／検証」を 2×2 グリッドで提示
- 表・コードブロック・引用・ラベル付きカードのスタイル付き
- フォントは Web 入手可能な Noto Sans JP / Roboto を使用

## ファイル構成

```
.
├── themes/
│   └── aoao-midori.css   # Marp テーマ本体
├── sample.md             # 全レイアウトを使ったサンプル
├── out.html              # sample.md のビルド結果（生成物）
└── .vscode/
    └── settings.json     # VS Code の Marp 拡張向け設定
```

## 使い方

### VS Code（Marp for VS Code 拡張）

1. [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) を入れる
2. このリポジトリの `.vscode/settings.json` でテーマ登録と HTML 有効化を済ませてあります
   ```json
   {
     "markdown.marp.themes": ["./themes/aoao-midori.css"],
     "markdown.marp.enableHtml": true
   }
   ```
   ※ 文献調査・落合フォーマットのカードは HTML を使うため `enableHtml: true` が必要です
3. `sample.md` を開き、プレビュー（右上のプレビューアイコン）で確認

### marp-cli

```bash
# HTML に変換
npx @marp-team/marp-cli sample.md --theme themes/aoao-midori.css --html -o out.html

# PDF に変換（要 Chrome / Chromium）
npx @marp-team/marp-cli sample.md --theme themes/aoao-midori.css --html --pdf
```

## レイアウトの書き方

Markdown 先頭の frontmatter でテーマを指定します。

```markdown
---
marp: true
theme: aoao-midori
paginate: true
size: 16:9
---
```

各スライドは `<!-- _class: ... -->` で種類を切り替えます。

### 表紙

```markdown
<!-- _class: title -->
<!-- _paginate: false -->

# プレゼンテーションタイトル
## サブタイトルをここに記述

所属
発表者名
```

### セクション扉

```markdown
<!-- _class: section -->

# 1. 背景と目的
```

### 本文

`<!-- _class: ... -->` を付けなければ通常の本文レイアウトになります。
見出し・箇条書き・表・コードブロックがそのまま使えます。

### 文献調査（lit）

```markdown
<!-- _class: lit -->

# 文献調査

<div class="stack">

<div class="card"><span class="tag">論文 1</span>
<p class="paper-title">Attention Is All You Need</p>
<p class="paper-title-ja">アテンションこそ全て —— Transformer による系列変換</p>
<div class="cite-row">
<span class="cite">Vaswani et al., <em>NeurIPS</em>, 2017.</span>
<span class="badge">120k+ Citations</span>
</div>
</div>

</div>
```

### 落合フォーマット（ochiai）

```markdown
<!-- _class: ochiai -->

# 落合フォーマット — 論文紹介

<div class="grid">

<div class="card"><span class="tag">① どんなもの？</span>
<p>RNN/CNN を使わず <strong>Attention のみ</strong> で系列変換を行う Transformer を提案。</p>
</div>

<!-- ② 先行研究より何がすごい？ / ③ 技術・手法のキモ / ④ どう検証した？ を同様に追加 -->

</div>
```

完全な例は [`sample.md`](./sample.md) を参照してください。

## カスタマイズ

配色は `themes/aoao-midori.css` 冒頭の CSS 変数で一括変更できます。

```css
:root {
  --aoao-teal:  #5A9F8A; /* ティール（アクセント） */
  --aoao-blue:  #136095; /* ブルー（アクセント） */
  --aoao-navy:  #003356; /* ネイビー（見出し） */
  --aoao-slate: #3A5365; /* スレート（本文） */
  --aoao-ink:   #1A1A1A; /* 濃い文字 */
  --aoao-bg:    #FFFFFF; /* 背景 */
}
```

アクセントバーの太さ・長さは `section` の `background-size`（例: `360px 14px`）で調整できます。

## クレジット

配色とレイアウトの着想は [Canva のテンプレート](https://www.canva.com/ja_jp/templates/EAGYmB5SFVs/) から得ています。本リポジトリには Canva の素材ファイルは含まれておらず、見た目を独自の CSS で再構築したものです。
