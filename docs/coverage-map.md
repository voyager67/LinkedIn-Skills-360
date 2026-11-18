# Coverage map

LinkedIn's product surfaces, UI, access tiers and available features change. This map describes workflow coverage in this repository, not a promise that every feature is available to every account or region. For the full skill inventory, see [`../skills/README.md`](../skills/README.md).

## By audience

| Audience | Start here | Expand into |
|---|---|---|
| Student / fresher | `student-career-launch`, `fresher-positioning`, `internship-search-campaign` | `portfolio-project-story`, `campus-placement-interview-prep`, `alumni-networking-planner`, `skills-gap-and-learning-plan` |
| Job seeker | `job-search-strategist`, `boolean-job-search-builder`, `job-fit-analyzer` | `job-alert-search-setup-planner`, `application-question-response-coach`, `application-final-review`, `interview-thank-you-and-followup` |
| Career switcher / returner | `career-switch-narrative`, `career-break-returner-positioning` | `skills-gap-and-learning-plan`, `career-development-roadmap`, `informational-interview-coach` |
| Working professional | `profile-audit`, `profile-keyword-mapper` | `promotion-case-builder`, `internal-mobility-strategy`, `mentor-relationship-plan`, `first-90-days-planner` |
| Creator / community operator | `personal-brand-strategist`, `linkedin-post-writer` | `linkedin-newsletter-strategy`, `linkedin-longform-article-writer`, `linkedin-event-strategy`, `linkedin-group-community-playbook` |
| Freelancer / consultant | `service-page-positioning-builder`, `service-business-lead-conversion` | `client-proof-and-case-study-writer`, `account-intelligence-brief`, `partnership-outreach-plan` |
| Sales / business development | `sales-navigator-query-planner`, `account-intelligence-brief` | `social-selling-account-plan`, `b2b-prospecting-sequence`, `lead-qualification-discovery`, `sales-meeting-followup` |
| Recruiter | `recruiter-role-intake`, `talent-boolean-search-builder` | `talent-market-map`, `recruiter-pipeline-review`, `candidate-experience-journey`, `candidate-pool-reengagement` |
| Hiring manager / panel | `competency-framework-designer`, `interview-plan-and-panel-designer` | `work-sample-assessment-designer`, `interview-panel-calibration`, `hiring-debrief`, `inclusive-accessible-hiring-review` |
| Employer brand / Page admin | `company-page-audit`, `employer-page-and-reputation-audit` | `company-page-editorial-planner`, `page-analytics-diagnostic`, `employee-advocacy-program`, `employer-value-proposition-editor` |
| Advertiser / performance marketer | `linkedin-ads-objective-and-budget-planner`, `linkedin-audience-targeting-review` | `linkedin-lead-gen-form-designer`, `linkedin-ads-creative-brief`, `linkedin-campaign-performance-diagnostic`, `linkedin-conversion-tracking-readiness` |
| Learner / L&D team | `linkedin-learning-path-curator` | `linkedin-learning-program-designer`, `linkedin-learning-creator-content-plan`, `career-development-roadmap` |

## By LinkedIn surface or adjacent workflow

| Surface / workflow area | Coverage | Important limitation |
|---|---|---|
| Personal profile | Headline, About, experience, skills, Featured, recommendations, privacy, visibility and Services positioning | The AI cannot see or edit live settings unless the user supplies a permitted view; it does not change the account. |
| LinkedIn Jobs | Search strategy, Boolean queries, alerts, job-risk review, role fit, applications, tracker and follow-up | Listings can expire or be duplicated; users verify current status and eligibility. |
| Network and inbox | Connections, cold outreach, referrals, alumni, mentoring, recruiter replies, inbox triage | Drafts only; no sending, scraping or bulk outreach. |
| Content and creator | Posts, comments, replies, carousels, articles, newsletters, events and groups | No auto-publication, auto-engagement or performance promises. |
| Company Pages | Page audit, editorial planning, analytics, employee advocacy and EVP | Admin access and product features vary; metrics need definitions and dates. |
| Sales Navigator / social selling | Lead/account query planning, Boolean syntax, account intelligence and engagement planning | Query plans only; no scraping, prohibited exports or automation. |
| Campaign Manager / paid promotion | Objectives, audience review, lead forms, ad creative, job campaigns and performance diagnosis | Plans and copy only; no campaign launch, spend, account access or lead export. |
| LinkedIn Learning | Individual learning paths, employer learning programs and instructional outlines | Catalogues and licenses vary; verify course availability and rights. |
| Showcase / Product / Career / University Pages | Page architecture, product positioning, employer content and alumni engagement | Verify Page eligibility, admin roles and current product behaviour. |
| Recruiting / hiring | Intake, sourcing, candidate messaging, interviews, work samples, debriefs, offers and handoffs | Human decisions only; no protected-trait inference or automated selection. |
| Career development | Learning, mentoring, internal mobility, promotion, career breaks and onboarding | Career outcomes cannot be guaranteed; local employment rules require expert advice. |

## Workflow chains

**From profile to opportunity**

`profile-audit` → `profile-keyword-mapper` → `job-search-strategist` → `job-fit-analyzer` → `resume-tailor` → `application-final-review` → `interview-research-brief` → `mock-interview-coach` → `offer-comparison-worksheet`.

**From requisition to onboarding**

`recruiter-role-intake` → `competency-framework-designer` → `talent-boolean-search-builder` → `candidate-outreach-writer` → `interview-plan-and-panel-designer` → `interview-panel-calibration` → `hiring-debrief` → `offer-brief-and-approval` → `onboarding-handoff`.

**From professional expertise to audience**

`personal-brand-strategist` → `linkedin-newsletter-strategy` → `linkedin-post-writer` / `linkedin-longform-article-writer` → `document-carousel-storyboard` → `linkedin-event-strategy` → `page-analytics-diagnostic`.

**From account research to a sales conversation**

`sales-navigator-query-planner` → `account-intelligence-brief` → `social-selling-account-plan` → `b2b-prospecting-sequence` → `lead-qualification-discovery` → `sales-meeting-followup`.

## Scope exclusions

This repository intentionally does not implement LinkedIn API clients, login/session management, web scraping, browser automation, auto-posting, auto-messaging, connection automation, campaign launch or spend, lead export, prohibited bulk exports, job application submission, or automated employment decisions. It is a workflow and reasoning toolkit, not a LinkedIn integration or ATS/CRM replacement.
