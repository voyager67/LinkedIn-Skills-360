# Research notes and design rationale

**Research reviewed:** 18 November 2026. This is a curated design review, not a claim that every LinkedIn feature, agent repository or career resource on the internet was exhaustively audited. Product UI, terms, feature access and documentation can change; verify official sources at the time of use.

## Research question

What would make a LinkedIn skill library genuinely useful across the whole professional lifecycle—not just profile writing and social posts—and maintainable across different AI hosts?

## Reference projects and engineering patterns

| Reference | What was examined | Design lesson adopted | What was not copied |
|---|---|---|---|
| [linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill) | Focused LinkedIn skills, profile rubric, hooks and human approval | Task-specific instructions, clear inputs/outputs, human control | It is an inspiration, not a codebase dependency; no scraping or auto-posting is added |
| [Agent Skills format](https://agentskills.io/) and [Microsoft Skills](https://github.com/microsoft/skills/tree/main/.github/docs) | `SKILL.md`, YAML metadata, discoverability and progressive disclosure | One focused folder per task; metadata explains what and when; supporting docs stay optional | No claim that every host auto-discovers every folder |
| [Anthropic skills](https://github.com/anthropics/skills) | Skill-folder organization and examples | Portable instructions and a clean separation between task guidance and optional assets | No provider-specific prompt syntax in core skills |
| [VoltAgent / awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Discovery catalogue and cross-domain skills collection | Clear categorization, discoverability and contribution review | No unverified quality claims or imported skill text |
| [obra / Superpowers](https://github.com/obra/Superpowers) | Planning, delegation, bounded execution and review patterns | Explicit plan/handoff/review steps; delegate only where useful | This repository is not a tool-executing software-development agent framework |
| [Nodegenie / awesome-agent-skills](https://github.com/nodegenie/awesome-agent-skills) | Skill discovery and repository scanning for risky skill patterns | Treat third-party skills as untrusted content; check scripts, external data flow, credentials and instruction overrides before installing | This repository does not bundle or claim to run that scanner |
| [GitHub Awesome Copilot skills documentation](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md) | Skill organization in another host ecosystem | Keep core content independent from installation mechanics | Host-specific discovery instructions are kept in adapters |

## LinkedIn product and workflow research

| Source | Relevant product/workflow insight | Where reflected |
|---|---|---|
| [LinkedIn Job Search Guide](https://www.linkedin.com/jobsearchguide/) | Search planning, profile readiness, job alerts and application organization are distinct tasks | Job search strategist, alert planner, application tracker and career-stage workflows |
| [LinkedIn Job Tracker help](https://www.linkedin.com/help/linkedin/answer/a8684146) | A job search needs saved roles, stages, notes and follow-up, not only a search query | Application tracker, weekly sprint, alert planner and final-review workflows |
| [Sales Navigator lead filters](https://www.linkedin.com/help/sales-navigator/answer/a1461507) and [Boolean search syntax](https://www.linkedin.com/help/sales-navigator/answer/a168061) | Lead/account discovery uses specific filters and Boolean syntax; surface and access level matter | Sales Navigator query planner and talent Boolean builder explicitly ask which search surface is used |
| [LinkedIn Pages best practices](https://business.linkedin.com/advertise/linkedin-pages/best-practices) and [Page analytics overview](https://www.linkedin.com/help/linkedin/answer/a547077) | Company presence includes Page completeness, content, followers, visitors and analytics definitions | Company Page audit, editorial planner, Page analytics and employer-brand workflows |
| [LinkedIn Services Pages FAQs](https://www.linkedin.com/help/linkedin/answer/a569534) | Service providers need a distinct positioning and enquiry workflow | Services Page positioning, service lead conversion and customer proof skills |
| [LinkedIn Page types](https://www.linkedin.com/help/linkedin/answer/a727893) and [Showcase Pages](https://www.linkedin.com/help/linkedin/answer/a566157) | Company, Showcase, Product, Service, University and Career Pages have distinct purposes and administrative dependencies | Page architecture, Product Page positioning, Career Page content and University/alumni workflows |
| [Campaign objectives](https://www.linkedin.com/help/linkedin/answer/a424570) and [Lead Gen Forms](https://www.linkedin.com/help/linkedin/answer/a422440) | Campaign goals, formats, objectives and lead forms must align to the actual desired action; access and options vary | Paid campaign objectives, audience review, Lead Gen Form design, creative briefs and job-ad campaigns |
| [LinkedIn Learning library](https://www.linkedin.com/help/linkedin/answer/a704863) | Learning content is organized across courses, paths, videos and collections; organizational access may vary | Individual learning-path curation, workforce programs and instructor content plans |
| [Recommendations help](https://www.linkedin.com/help/linkedin/answer/a546682/requesting-a-recommendation) and [Skills endorsements overview](https://www.linkedin.com/help/linkedin/answer/a565106/skill-endorsements-overview) | Recommendations and skills endorsements are different reputation mechanisms | Separate recommendation request/response skills and evidence-led skill curation |
| [LinkedIn User Agreement](https://www.linkedin.com/legal/user-agreement) and [Prohibited software guidance](https://www.linkedin.com/help/linkedin/answer/a1341387/prohibited-software-and-extensions) | Automated scraping, account activity and unapproved tools create platform and account risks | Human-controlled actions, no scraping, no auto-posting, no auto-messaging and no credential handling |

## Career development and student research

- [NACE Career Readiness Competencies](https://www.naceweb.org/career-readiness/competencies/career-readiness-defined/) provides a useful vocabulary for career development that extends beyond technical skills. The student and career-growth workflows translate competencies into evidence and practice instead of treating profile keywords as capability.
- [MIT Career Handbook](https://capd.mit.edu/resources/career-handbook/) and [job/internship search guidance](https://capd.mit.edu/channels/find-a-job-or-internship/) cover exploration, networking, applications, resumes, interviews and offers. This reinforced the need for internship campaigns, alumni outreach, informational interviews, career fairs, and decision workflows.

## Recruiting and structured hiring research

- [Greenhouse Structured Hiring Guide](https://support.greenhouse.io/hc/en-us/articles/360039539772-Structured-hiring-guide) describes role kickoff, scorecards, interview planning, feedback and debrief. This informed the intake → competency → interview → calibration → debrief workflow chain.
- Hiring tools in this repository are decision support for accountable people. They use observable, job-related criteria, consistent question sets and explicit evidence/unknowns. They do not decide who should be hired, infer protected traits, or turn scores into automated rejection rules.

## Gaps identified and added

The initial reference project was strong on profile/content tasks but comparatively narrow in its published scope. This expansion adds workflows for:

1. Job tracker discipline, Boolean search, saved-search/alert planning, risk review, application questions and final checks.
2. Student internships, campus hiring, alumni, career fairs, informational interviews and mentoring.
3. Career breaks, layoffs, internal mobility, promotion cases, learning plans, references, offers and first 90 days.
4. Recommendations, endorsements, public profile privacy, localization, Featured assets and Services Pages.
5. Newsletters, articles, carousels, events, groups, community response and executive/founder voice.
6. Company Page completeness, editorial operations, Page analytics, employee advocacy and EVP.
7. Sales Navigator query planning, account intelligence, discovery, social selling and partnerships.
8. Recruiter intake, talent maps, structured assessment, candidate journey, respectful closure, offer handoff, aggregate funnel metrics, privacy and process retrospectives.
9. Campaign Manager objectives, audience review, Lead Gen Forms, paid creative, job promotion and conversion measurement.
10. Showcase, Product, Career and University Page architecture, plus LinkedIn Learning paths and organizational learning programs.

## Quality principles adopted

- **Progressive disclosure:** load only the activated skill rather than every instruction at once.
- **Small workflow boundaries:** each skill owns a specific task and produces a recognizable artifact.
- **Provenance:** material claims are linked to user evidence or public sources, with dates where freshness matters.
- **Explicit uncertainty:** unknowns remain unknown; estimates and interpretations are labelled.
- **Human authority:** platform actions and employment decisions remain with the user or authorized team.
- **Privacy by design:** minimum necessary information, redaction and local/private records.
- **Maintainability:** index and test data are derived from the actual skill inventory; changes include examples and negative constraints.

## Research limitations

This repository does not reproduce LinkedIn's internal ranking, recommendation, hiring or ad-delivery algorithms. Public help pages do not expose all feature availability or account-specific controls. Search examples require revalidation against the product surface in use. External career resources are context, not universal law or individualized legal/financial advice. No usage benchmark, job-placement lift, recruiter efficiency gain or user adoption figure is asserted.
