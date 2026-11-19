# Website source

This directory contains the LinkedIn Skills 360 public website. It uses Jekyll for layouts, includes, page metadata and URL handling. The interactive directories use plain JavaScript and pre-generated JSON catalogues.

## Local preview

Install Ruby and Bundler, then from this directory run:

```bash
bundle install
bundle exec jekyll serve --baseurl ""
```

Open <http://127.0.0.1:4000/>.

## Structure

- `_config.yml` — GitHub Pages project-site configuration
- `_layouts/default.html` — metadata, shared page shell and SEO
- `_includes/` — site header and footer
- `assets/` — local CSS, JavaScript, icons and artwork
- `skills/catalog.json` and `agents/catalog.json` — browser-search catalogues
- `skills/`, `agents/`, `use-cases/`, `docs/` — visitor-facing pages

The workflow in the repository root publishes only the generated Jekyll output. It does not publish the repository root or the underlying skill source files.
