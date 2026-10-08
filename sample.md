---
marp: true
theme: aoao-midori
paginate: true
size: 16:9
---

<!-- _class: title -->
<!-- _paginate: false -->

# プレゼンテーションタイトル

## サブタイトルをここに記述

所属 
発表者名

---

# アジェンダ

- 背景と目的
- 提案手法
- 実験と結果
- まとめ

---

<!-- _class: section -->

# 1. 背景と目的

---

# 見出しと本文

本文は **スレートカラー** で表示され、強調は *青* と **紺** を使い分けます。

- 第1階層の箇条書き（青緑のマーカー）
  - 第2階層の箇条書き（青のマーカー）
    - 第3階層
- もう一つの項目

## 小見出し（h2）

段落テキストのサンプルです。読みやすさを優先したライン高に設定しています。

---

# 表とコード

| 項目 | 値 | 備考 |
|------|-----|------|
| 精度 | 92.3% | ベースライン比 +4.1pt |
| 速度 | 12ms | リアルタイム動作 |
| メモリ | 1.2GB | GPU使用時 |

```python
def greet(name: str) -> str:
    return f"こんにちは、{name}さん"
```

インラインコードは `like_this` のように表示されます。

---

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

<div class="card"><span class="tag">論文 2</span>
<p class="paper-title">Deep Residual Learning for Image Recognition</p>
<p class="paper-title-ja">残差学習による深層画像認識（ResNet）</p>
<div class="cite-row">
<span class="cite">He et al., <em>CVPR</em>, 2016.</span>
<span class="badge">200k+ Citations</span>
</div>
</div>

</div>

---

<!-- _class: ochiai -->

# 落合フォーマット — 論文紹介

<div class="grid">

<div class="card"><span class="tag">① どんなもの？</span>
<p>RNN/CNN を使わず <strong>Attention のみ</strong> で系列変換を行う Transformer を提案。</p>
</div>

<div class="card"><span class="tag">② 先行研究より何がすごい？</span>
<p>並列計算が可能で <strong>学習が高速</strong>、長距離依存も捉えやすい。翻訳で SOTA を達成。</p>
</div>

<div class="card"><span class="tag">③ 技術・手法のキモ</span>
<p>Self-Attention と Multi-Head、位置情報を与える <em>Positional Encoding</em>。</p>
</div>

<div class="card"><span class="tag">④ どう検証した？</span>
<p>WMT 英独・英仏翻訳で BLEU を評価し、既存手法を上回る精度を確認。</p>
</div>

</div>

---

<!-- _class: gantt -->

# 研究計画（ガントチャート）

| タスク | 10月 | 11月 | 12月 | 1月 |
|---|---|---|---|---|
| 文献調査 | ■■■■ | ■■.. | | |
| *予備実験* | ...■ | ■■■■ | ■■.. | |
| *本実験* | | | ■■■■ | ■■.. |
| **論文執筆** | | | ...■ | ■■■■ |
| | **▲ 今日** | | ▲ 中間発表 | |

計画・調査 *実験* **執筆** `その他`

---

<!-- _class: section -->

# 4. まとめ

---

# まとめ

- 表紙 / セクション扉 / 本文の主要レイアウトに対応
- 文献調査・落合フォーマットのスライドも用意
- フォントは Noto Sans JP / Roboto を使用

ご清聴ありがとうございました。
