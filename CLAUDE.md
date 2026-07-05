# CLAUDE.md

このリポジトリで Claude が作業するときの基本ルール。最初に必ず読むこと。

## サイト概要

- 綿岡晃輝（Koki Wataoka）の個人サイト。
- GitHub Pages でホストされている。
- 公開URL: https://wataoka.github.io
- リポジトリ: `git@github.com:wataoka/wataoka.github.io.git`
- デフォルトブランチ: `master`
- GitHub Pages の公開ディレクトリは `docs/`。`master` に push すれば自動デプロイされる。

## 編集対象

トップページは引き続き **`docs/index.html`**（単一ファイル構成: HTML + `<style>` + 末尾の `<script>`）を直接編集する。ブログ記事は Jekyll のブログコレクション（`docs/_blog/`）に Markdown ファイルを追加する形に変わった。詳細は下記「ブログ投稿の追加方法」を参照。

ディレクトリ構成:

- `docs/` — 公開対象（Jekyll のソースルート）。
  - `index.html` — トップページ。front matter なし、Jekyll のレイアウトシステムの外にある静的ファイルとして扱う（今まで通り手編集）。
  - `ai-safety-2025.html` — 講演スライド系の単発ページ。front matter なし、静的ファイルのまま。今回のブログ移行では対象外（今後もブログコレクションには含めない）。
  - `_config.yml` / `Gemfile` — Jekyll の設定と依存 gem。
  - `_layouts/post.html` — ブログ記事用のページテンプレート。
  - `_includes/site-style.html` / `_includes/lang-toggle.html` / `_includes/ad.html` — ブログ記事が使う CSS・EN/JA トグル JS・広告枠。`index.html` の `<style>`/`<script>` の内容をコピーしたもので、`index.html` 側は変更していない（意図的な重複。`ai-safety-2025.html` が CSS を丸ごとコピーしている既存の慣習と同じ考え方）。
  - `_blog/` — ブログ記事の Markdown ファイルを置くコレクション。`/blog/:title/` という URL になる。
  - `blog/index.html` — ブログ記事一覧ページ（`/blog/`）。
  - 画像（`wataoka2025.jpg` 等）、`favicon.ico`、SNS アイコン SVG も同じ階層。
- `README.md` — リポジトリ全体の説明。サイトのレイアウト変更時に整合性が崩れたら更新する。

過去バージョンの `v1/` / `v2/` / `public/`、および Markdown 下書き（`docs/index-en.md` / `docs/index-ja.md` / `docs/ai-safety-2025.md`）は整理済みでリポジトリには存在しない。git history からは参照可能だが、現行運用では参照しない。

## コンテンツ更新の作法（トップページ）

`index.html` / `ai-safety-2025.html` については、**Markdown 下書きを介さず、Claude が直接ファイルを編集する。** ユーザーは自然言語で依頼するだけで良い:

- 「ICML 2026 のこの論文を業績に追加して。URLは...」 → Claude が業績セクションに同じ HTML 構造で挿入し、`data-en` / `data-ja` も埋める。
- 「経歴の所属を変えて」 → 該当 `data-en` / `data-ja` を両方更新。
- 「文章を書き直したい」 → 必要なら Markdown でチャット内に草案を出して推敲してから HTML に反映する。ファイルとしての MD 下書きは持たない。

ブログ記事の追加は下記「ブログ投稿の追加方法」を参照（こちらは Markdown ファイルとして `docs/_blog/` に置く）。

## `docs/index.html` の構造（要点）

- 単一ファイルに HTML / CSS / JS が同居。`index.html` 自体はこの方針を維持し、front matter や Jekyll のレイアウトは使わない。
- カラーは `:root` の CSS 変数で定義され、`@media (prefers-color-scheme: light)` でライトテーマに切り替わる。新しい色は変数を経由する。
- セクション構成: `#about` → `#career` → `#books` → `#appointments` → `#publications` → `#lectures` → `#patents` → `#contact` → `<footer>`。
- フォントは Google Fonts の Inter。

### 多言語対応（EN / JA）

EN/JA はクライアント側 JS で `data-en` / `data-ja` 属性を読み替えて切り替えている。**新しい文言を追加するときは EN と JA の両方を必ず用意する**。仕組みは2系統:

1. **短いテキスト（インライン）** — 同じ要素に両方を持たせる:
   ```html
   <h2 data-en="Career" data-ja="経歴">Career</h2>
   ```
   要素の `innerHTML` が表示中の言語の値で上書きされる。タグ内の初期テキストは EN を入れておくのが慣例。

2. **長文ブロック（段落単位）** — 言語ごとに別要素を置き、`data-lang-content` で切り替える:
   ```html
   <p class="lead" data-lang-content="en">English paragraph...</p>
   <p class="lead" data-lang-content="ja" style="display:none;">日本語段落...</p>
   ```
   非表示側は `style="display:none;"` を必ず付ける（初期表示で両方見えてしまうため）。

選択言語は `localStorage.lang` に保存され、初回はブラウザ設定から判定される。

### コンテンツ追加時のチェックリスト

新しい論文 / 講演 / 経歴を足すときは:

1. 該当セクション内に既存項目と**同じ HTML 構造**で挿入（年代の新しい順）。
2. タイトル・所属・期間など切り替えが必要な箇所はすべて `data-en` / `data-ja` を埋める。
3. リンクは `target="_blank" rel="noopener"`。
4. 著者名のうち本人は `<b>` でハイライト（既存の表記に合わせる: EN は "Koki Wataoka"、JA は "綿岡晃輝"）。
5. 画像を追加する場合は `docs/` 直下に置き、相対パスで参照する。
6. ブラウザで EN / JA 両方を切り替えて表示崩れがないか確認するよう促す（Claude は `python3 -m http.server` などで `docs/` を起点に簡易サーバを立てて確認できる）。`index.html` に front matter はないので、これは Jekyll のビルドを介さない従来通りの確認方法で問題ない。

## ブログ投稿の追加方法

ブログは Jekyll の `blog` コレクションとして実装されている（`_config.yml` の `collections.blog`）。新しい記事を追加する手順:

1. `docs/_blog/YYYY-MM-DD-slug.md` というファイル名で作成する（`slug` は英数字とハイフン）。URL は `/blog/slug/` になる（日付部分はファイル名のソート用で、URL には出ない）。
2. 先頭に front matter を書く:
   ```yaml
   ---
   title_en: "Post Title in English"
   title_ja: "投稿タイトル（日本語）"
   date: 2026-07-05
   description: "一行の説明（SEO 用、英語で可）"
   ---
   ```
   `layout: post` は `_config.yml` の `defaults` で自動的に適用されるので書かなくてよい。
3. 本文は EN/JA をそれぞれ `data-lang-content` で囲んだブロックとして両方書く（`index.html` の長文ブロックと同じ考え方）。**Markdown を効かせるには各 `<div>` に `markdown="1"` を付け、開始タグの直後と終了タグの直前に必ず空行を入れる**（このどちらかを忘れると `**太字**` などが正しく変換されずそのまま表示されてしまう。エラーにはならないので注意）:
   ```markdown
   <div data-lang-content="en" markdown="1">

   ## Heading

   English **Markdown** content, `code`, [links](https://example.com).

   </div>

   <div data-lang-content="ja" style="display:none;" markdown="1">

   ## 見出し

   日本語の **Markdown** コンテンツです。

   </div>
   ```
4. 画像は `docs/assets/blog/` に置く（`index.html` 用の画像とは分けて管理する）。記事数が増えてきたらファイル名衝突を避けるため `docs/assets/blog/<slug>/` のようにサブフォルダに分けることも検討する。
5. 広告は `_layouts/post.html` が `_includes/ad.html` を自動的に記事の先頭と末尾に挿入するので、記事ファイル側で広告を意識する必要はない。広告ネットワークのスクリプトを設定する際は `_includes/ad.html` の中身だけを書き換える（`index.html` や `ai-safety-2025.html` には絶対に広告を追加しない）。
6. ローカルで確認する場合は `docs/` で `bundle install` の後 `bundle exec jekyll serve` を実行し、`http://localhost:4000/blog/slug/` を開く（`index.html` だけを直したときは、これまで通り `python3 -m http.server` で十分で、フル Jekyll ビルドは不要）。

## ワークフロー

1. 該当ファイルを編集する（トップページなら `docs/index.html` / `docs/ai-safety-2025.html`、ブログ記事なら `docs/_blog/` 配下、レイアウトや広告枠を触るなら `_layouts/` / `_includes/` / `_config.yml`）。
2. 差分を確認する（`git diff`）。
3. ユーザーに変更内容を要約して見せ、コミットしてよいか確認する。**勝手に commit / push しない**。
4. ユーザーの承認後、コミットメッセージは既存の慣例（`Add: ...` / `Update: ...` / `Fix: ...` の形式）に揃える。push 後に GitHub Pages へ自動反映される（GitHub Pages が Jekyll のビルドも自動で行うので、ビルド用の GitHub Actions は不要）。

## やらないこと

- `index.html` / `ai-safety-2025.html` に front matter を付けたり、Jekyll のレイアウトシステムに載せたりすること（この2ファイルは今まで通り手編集の静的ファイルのまま）。
- ブログ以外の目的でビルドツールやフレームワークを追加すること（Jekyll はブログ機能のためだけに導入している。それ以外の用途で新しいビルドステップを増やさない）。
- GitHub Actions などのカスタムビルドワークフローの追加（GitHub Pages 標準の Jekyll ビルドで十分なので、必要になるまで追加しない）。
- `.DS_Store` や `__pycache__` 等のコミット（`.gitignore` 済み）。
- 確認なしの `git commit` / `git push`。
- 過去バージョン（`v1/` / `v2/`）の復活。必要なら git history を参照する。
