# GitHub Pages site

The dedicated static site lives in [`site/`](site/). It includes a landing page, searchable skill catalogue, agent directory, audience use cases and documentation hub.

Expected URL after successful Pages deployment: https://voyager67.github.io/LinkedIn-Skills-360/

## Enable deployment

1. Open repository **Settings → Pages**.
2. Confirm the repository/account plan permits the intended Pages visibility. This repository is currently private and was not made public as part of this task.
3. Set **Build and deployment → Source** to **GitHub Actions**.
4. Run the **Deploy GitHub Pages** workflow from the Actions tab, or push a change under `site/`.
5. Confirm the workflow completes, then visit the URL above.

The workflow uses GitHub's Pages actions and publishes only the `site/` directory. It does not require a Node build step or third-party frontend framework.

## Current activation state

The first deployment attempt failed at the Pages configuration step because GitHub returned “Pages site not found.” The files and workflow are committed, but Pages has not yet been enabled/configured. The project does not claim a live public website until a successful deployment is visible in Actions.
