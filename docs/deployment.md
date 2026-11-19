# GitHub Pages and Jekyll deployment

The public website is maintained in `site/` and built with GitHub's supported Jekyll Pages action.

## Site architecture

- `site/_config.yml` — title, description, project-site URL and base path
- `site/_layouts/default.html` — shared document shell, canonical URL, Open Graph, Twitter Card and structured-data metadata
- `site/_includes/header.html` and `footer.html` — shared navigation and footer
- `site/assets/` — local CSS, JavaScript, brand icon and image assets
- `site/skills/catalog.json` and `site/agents/catalog.json` — static catalogues for the searchable directories
- `site/skills/`, `site/agents/`, `site/use-cases/`, `site/docs/` — visitor-facing pages

The design uses Jekyll for templates and metadata and plain HTML, CSS, JavaScript and JSON for the visitor experience. It does not require a JavaScript framework, remote fonts, analytics SDK or runtime server.

## Deployment workflow

The workflow is `.github/workflows/pages.yml`. It:

1. Checks out the repository without persisting checkout credentials.
2. Configures Pages.
3. Builds only the `site/` directory with the official `actions/jekyll-build-pages` action.
4. Uploads only the generated `_site/` directory.
5. Deploys the Pages artifact.

The action dependencies are pinned to full commit SHAs. The repository root, skill source files, evaluation cases and maintainer documentation are not published as the website artifact.

## Enable GitHub Pages

1. Open **Repository → Settings → Pages**.
2. Set the build and deployment source to **GitHub Actions**.
3. Push a change under `site/` or manually run **Deploy Jekyll site to GitHub Pages** from the Actions tab.
4. Confirm the workflow completes and GitHub reports the deployment URL.

Expected project URL: <https://voyager67.github.io/LinkedIn-Skills-360/>.

Public availability depends on repository visibility, account plan and organization policy. Check GitHub's current Pages visibility rules before publishing material that should remain private. The website directory is designed for public display.

## Local preview

Install Ruby and Bundler, then run:

```bash
cd site
bundle install
bundle exec jekyll serve --baseurl ""
```

Open <http://127.0.0.1:4000/>. The production base path is defined in `_config.yml`; the local `--baseurl ""` override removes the project path for local preview.

## Maintenance checks

From the repository root:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
node --check site/assets/site.js
```

Also test the deployed site at desktop and mobile widths, check the skill and agent search results, inspect page metadata and verify the sitemap and image URLs. Do not claim a deployment is live until the Actions run succeeds.
