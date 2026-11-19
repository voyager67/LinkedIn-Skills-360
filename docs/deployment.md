# GitHub Pages deployment

## Site structure

- Static site source: `site/`
- Entry point: `site/index.html`
- Asset directory: `site/assets/`
- Deployment workflow: `.github/workflows/pages.yml`

The site is plain HTML, CSS, JavaScript and static JSON. It has no package manager, build service, analytics SDK or runtime server dependency.

## Deployment behavior

The Pages workflow runs on changes under `site/` or when manually dispatched. It uploads only the `site/` directory as the Pages artifact. It must never upload the repository root (`.`), because the repository contains source skills, evaluation material and maintainer documentation that are not website content.

Action dependencies are pinned to full commit SHAs. Workflow permissions are limited to repository read access plus the Pages deployment permissions on the deployment job. Checkout credentials are not persisted.

## Enable Pages

1. Open repository **Settings → Pages**.
2. Select **GitHub Actions** as the build and deployment source.
3. Run **Deploy GitHub Pages** from the Actions tab, or push a change under `site/`.
4. Confirm that the deployment job completes and that the environment reports its published URL.

Public availability depends on repository visibility, account plan and organization policy. A private repository does not automatically mean the published Pages site is private; check GitHub's current Pages visibility rules before publishing sensitive material. This repository's site directory is designed for public display.

## Forks and custom domains

A fork should update repository links, canonical URLs and Open Graph image URLs in the `site/` HTML before publishing. Custom domains must be configured in repository Pages settings; adding a `CNAME` file alone does not activate a domain.

## Maintenance checks

Before publishing, run:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
node --check site/assets/site.js
```

Also inspect the rendered pages at mobile and desktop widths, confirm the searchable catalogue loads, and verify that all image/GIF assets resolve.
