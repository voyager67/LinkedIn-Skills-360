# GitHub Pages site

The dedicated static site lives in [`site/`](site/). It includes a landing page, searchable skill catalogue, agent directory, audience use cases and documentation hub.

Expected URL after Pages deployment: https://voyager67.github.io/LinkedIn-Skills-360/

## Enable deployment

1. Open repository Settings → Pages.
2. Set Build and deployment source to **GitHub Actions**.
3. Confirm the account/plan supports the intended Pages visibility. The repository was left private deliberately; a publicly accessible site requires a configuration that permits public Pages.
4. Push a change under `site/` or run the `Deploy GitHub Pages` workflow manually.
5. Confirm the workflow completes and visit the URL above.

The workflow uses GitHub's official Pages actions and publishes only the `site/` directory. The source repository remains the canonical documentation and skill store.
