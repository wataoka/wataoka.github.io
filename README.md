# 🌐 Homepage

This is the source for my personal website. The homepage (`index.html`) is pure hand-written HTML/CSS (with a huge help from AI tools); the blog section is built with Jekyll, which GitHub Pages builds automatically. Hosted on GitHub Pages.

**Live site:** [wataoka.github.io](https://wataoka.github.io)

## 📂 Structure
`docs/`                → Live site content (served by GitHub Pages, also the Jekyll source root)  
`docs/index.html`      → Main page — edit this directly for content changes  
`docs/ai-safety-2025.html` → Standalone article page — edit directly, not part of the blog collection  
`docs/_blog/`          → Blog post Markdown files (Jekyll collection, served at `/blog/:title/`)  
`docs/blog/index.html` → Blog listing page  
`docs/_layouts/`, `docs/_includes/` → Jekyll layout/include files used only by the blog  
`docs/_config.yml`, `docs/Gemfile` → Jekyll configuration  
`CLAUDE.md`            → Working rules for AI assistants editing this repo  

## 🚀 Editing & Publishing
1. Clone the repo:  
   ```bash
   git clone https://github.com/wataoka/wataoka.github.io.git
   ```

2. Edit `docs/index.html` to update the homepage, or add a Markdown file under `docs/_blog/` for a new blog post.

3. To preview the blog locally: `cd docs && bundle install && bundle exec jekyll serve`, then open `http://localhost:4000`.

4. Push changes — they go live automatically via GitHub Pages (which builds the Jekyll site for you, no CI setup needed).
