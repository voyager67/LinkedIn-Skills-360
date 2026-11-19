# Installation and first use

## Clone the repository

```bash
git clone https://github.com/voyager67/LinkedIn-Skills-360.git
cd LinkedIn-Skills-360
```

## Select a skill

Open [`skills/README.md`](skills/README.md), choose one workflow and paste or attach its `SKILL.md` into your AI host. Start with an example in [`examples/README.md`](examples/README.md).

## Use the orchestrator

Provide `agents/orchestrator.md` plus the relevant specialist prompt. If your host supports delegation, it may hand off to specialists. Otherwise, follow the same sequence in one conversation. This repository ships prompt specifications rather than a runtime.

## Use the project website

The static website source is in `site/`. To publish it, enable GitHub Pages with **GitHub Actions** as the deployment source. The workflow publishes only `site/`. See [`docs/deployment.md`](docs/deployment.md) for the exact deployment and verification process.

## Validate locally

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
node --check site/assets/site.js
```

## Privacy

Redact personal contact details, account IDs, addresses and candidate identifiers. Never provide LinkedIn passwords, cookies, session tokens or one-time codes. Keep filled trackers, resumes and candidate notes in a private workspace; do not commit them to this repository. Review [`docs/privacy-and-safety.md`](docs/privacy-and-safety.md).