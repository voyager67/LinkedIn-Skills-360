# Installation and first use

## Clone the final repository

```bash
git clone https://github.com/voyager67/LinkedIn-Skills-360.git
cd LinkedIn-Skills-360
```

## Select a skill

Open [`skills/README.md`](skills/README.md), choose one workflow and paste or attach its `SKILL.md` into your AI host. Start with an example in [`examples/README.md`](examples/README.md).

## Use the orchestrator

Provide `agents/orchestrator.md` plus the relevant specialist prompt. If your host supports delegation, it may hand off to specialists. Otherwise, follow the same sequence in one conversation. This repository ships prompt specifications rather than a runtime.

## Use the GitHub Pages site

The static website is in `site/` and is deployed by `.github/workflows/pages.yml`. In repository Settings → Pages, select **GitHub Actions** as the source. A public visitor-facing site requires repository visibility and account-plan settings that permit public Pages.

## Validate locally

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

## Privacy

Redact personal contact details, account IDs, addresses and candidate identifiers. Never provide LinkedIn passwords, cookies, session tokens or one-time codes. Keep filled trackers, resumes and candidate notes in a private workspace; do not commit them to this repository. Review `docs/privacy-and-safety.md`.
