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

**唯一の編集対象は `docs/index.html`**（単一ファイル構成: HTML + `<style>` + 末尾の `<script>`）。

ディレクトリ構成:

- `docs/` — 公開対象。`index.html` のほか、画像（`wataoka2025.jpg` 等）、`favicon.ico`、SNS アイコン SVG、`ai-safety-2025.html`（講演スライド系の単発ページ）が同じ階層に置かれている。
- `README.md` — リポジトリ全体の説明。サイトのレイアウト変更時に整合性が崩れたら更新する。

過去バージョンの `v1/` / `v2/` / `public/`、および Markdown 下書き（`docs/index-en.md` / `docs/index-ja.md` / `docs/ai-safety-2025.md`）は整理済みでリポジトリには存在しない。git history からは参照可能だが、現行運用では参照しない。

## コンテンツ更新の作法

**Markdown 下書きを介さず、Claude が直接 `index.html`（や `ai-safety-2025.html`）を編集する。** ユーザーは自然言語で依頼するだけで良い:

- 「ICML 2026 のこの論文を業績に追加して。URLは...」 → Claude が業績セクションに同じ HTML 構造で挿入し、`data-en` / `data-ja` も埋める。
- 「経歴の所属を変えて」 → 該当 `data-en` / `data-ja` を両方更新。
- 「文章を書き直したい」 → 必要なら Markdown でチャット内に草案を出して推敲してから HTML に反映する。ファイルとしての MD 下書きは持たない。

## `docs/index.html` の構造（要点）

- 単一ファイルに HTML / CSS / JS が同居。外部 CSS・JS ファイルは作らない方針。
- カラーは `:root` の CSS 変数で定義され、`@media (prefers-color-scheme: light)` でライトテーマに切り替わる。新しい色は変数を経由する。
- セクション構成: `#about` → `#career` → 業績 → `#talks` → `#patents` → `#contact` → `<footer>`。
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
6. ブラウザで EN / JA 両方を切り替えて表示崩れがないか確認するよう促す（Claude は `python3 -m http.server` などで `docs/` を起点に簡易サーバを立てて確認できる）。

## ワークフロー

1. `docs/index.html` を編集する。
2. 差分を確認する（`git diff docs/index.html`）。
3. ユーザーに変更内容を要約して見せ、コミットしてよいか確認する。**勝手に commit / push しない**。
4. ユーザーの承認後、コミットメッセージは既存の慣例（`Add: ...` / `Update: ...` / `Fix: ...` の形式）に揃える。push 後に GitHub Pages へ自動反映される。

## やらないこと

- 外部 CSS / JS ファイルへの分割、フレームワーク導入、ビルドツール追加（現状はビルド不要の素の HTML/CSS/JS という方針を維持）。
- `.DS_Store` や `__pycache__` 等のコミット（`.gitignore` 済み）。
- 確認なしの `git commit` / `git push`。
- 過去バージョン（`v1/` / `v2/`）の復活。必要なら git history を参照する。
