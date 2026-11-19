# Hybrid RAG for Banking — Execution Plan

## Scope and delivery assumptions

Deliver four read-only decision-support workspaces for authorized bank employees. Service provides customer, account and loan facts. Loan flags missing evidence and compares policy thresholds. Fraud presents source-backed investigative leads and uncertainty. Docs retrieves cited passages and attributed fields. Bank staff retain authority for consequential decisions.

Plan for 16 relative weeks with 2–3 engineers and a part-time banking SME. Confirm staffing and decision owners at kickoff. Treat the handbook's sample configurations and proposed thresholds as planning inputs. Use synthetic fixtures in development and CI. Any pilot use of masked or live data requires explicit approval for that data and environment.

Use the [task completion tracker](Hybrid_RAG_Task_Completion_Tracker.md) to record ownership, evidence, blockers and phase acceptance.

## Weekly delivery sequence

| Week | Work and suggested lead | Review evidence |
|---|---|---|
| 1 | Platform and backend bootstrap the monorepo, lock dependencies, start local Postgres and Neo4j, configure CODEOWNERS, required reviews and stable `merge-gate`, and establish the Actor contract. | Fresh-clone health checks, a reviewed green PR, and rejected direct push, force push, failing PR and stale-review attempts. Establish branch protection and its required check together. |
| 2 | Backend and QA implement initial migrations, RLS, deterministic two-tenant fixtures, API health and a scoped customer or loan lookup. Start the threat model and bank approval log. Draft 40 gold cases, 10 per domain, including denials. | Authenticated API-to-SQL demo and wrong-tenant denial. Two reviewed PRs and a failing authorization fixture prove the required gate. |
| 3 | Backend completes domain schemas, audited parameterized SQL tools, deterministic loan policy checks, and initial identity, chat and source contracts. Start the authenticated web shell. | FK and exact-fact assertions, policy effective-date tests, and role/object denial tests. |
| 4 | Data engineering implements page-aware parsing, versioned chunks, ACL inheritance, embeddings, lexical and dense retrieval, and RRF. | Deterministic rerun, approved source scope, and recall results from 20 labeled document questions. |
| 5 | Backend adds scoped Cohere rerank with fallback, the typed OpenAI tool loop, gated routing, citation validation, abstention and SSE. Frontend connects chat to the source viewer. | Service and Docs answers with authorized resolvable citations. Simulate missing evidence, reranker failure and interrupted streams. |
| 6 | Frontend and QA complete Service, Loan and Docs workflows. Expand to 100+ gold cases and capture a graph-disabled baseline with pinned versions. | Exact facts, loan checklist, citation and denial suites, per-domain retrieval metrics, latency and cost. Required PR checks cover the API, UI and deterministic evaluation lanes. |
| 7 | Data engineering defines Neo4j ontology and provenance, builds the repeatable SQL-to-graph loader and resolves authorized roots. | Constraints, expected counts, cross-store identifiers and idempotent reload. |
| 8 | Backend and frontend add bounded graph tools and the fraud case panel with source-linked paths. Enable required graph security tests as graph code lands. | Wrong tenant, denied role, hidden intermediate node and out-of-case path checks. |
| 9 | Data engineering adds typed mention extraction, source-span checks, conservative resolution and reviewer workflow. Begin integrating the refresh pipeline. | SME review sample, ambiguous entities left unresolved and versioned provenance. |
| 10 | Backend and QA complete Fraud and run a paired graph experiment on 30+ pre-registered multi-hop cases. | Matched SQL/hybrid and SQL/hybrid/graph runs with fixed model and data. Report correctness, false links, citations, latency and cost. Record lift or approved scope narrowing. |
| 11 | Backend and data engineering add approved mixed-domain routes, shared evidence, budgets and Airflow staged refresh with atomic publish and request version pinning. | Deduplicated authorized evidence, bounded tool calls, idempotent retry and rejected bad build. |
| 12 | Security, QA and platform exercise isolation, prompt injection, PII redaction, stale versions, source revocation and provider fallbacks. Configure redacted Langfuse traces and immutable staging promotion. | Negative-suite evidence, security review, green main SHA mapped to a signed digest, and staging health/ACL smoke. |
| 13 | Platform and QA run load, outage and rollback drills, verify audit completeness and freeze release candidate versions. | Full gold-set report, SLO and cost measurements, rollback record and any approved performance exceptions. |
| 14 | Product, SME and QA start a limited role-based pilot after staging and required pilot approvals. Verify accessibility and support escalation. | UAT scripts and results for four workspaces, approved participant and data scope, and documented feedback. |
| 15 | Engineering resolves pilot findings by severity. Governance reviews model and provider inventory, data lifecycle, security controls and release evidence. | Retested regression cases, refreshed full evaluation and signed review notes. |
| 16 | Operations rehearses restore, rollback, outage and source revocation. Governance records go/no-go and accepts the handover. | Signed release manifest, restricted production approval evidence, runbooks, dashboards, training and named support owners. Production promotion is conditional on approval. |

## Phase acceptance

| Gate | Required result | Suggested acceptance owners |
|---|---|---|
| P0 · Week 2 | Protected main enforcement proven, reproducible synthetic setup, authenticated SQL vertical slice, 40 draft cases and a documented security approval plan. | Platform, backend, security |
| P1 · Week 6 | Scoped Service, Loan and Docs usable end to end, citations validated, 100+ baseline gold cases and measured quality/cost/latency. | Product, QA, banking SME |
| P2 · Week 10 | Fraud paths are scoped and source-linked. Paired evaluation shows useful multi-hop lift or governance accepts a narrower graph scope. | Data/AI lead, security, fraud SME |
| P3 · Week 13 | Hard quality and authorization gates pass, failed refresh stays unpublished, immutable staging artifact passes smoke, rollback proven, and performance exceptions approved where applicable. | Platform, QA, security, operations |
| P4 · Week 16 | UAT and evidence package reviewed, support ownership accepted, and written go/no-go records scope and outstanding risk. | Product, operations, banking governance |

Zero unauthorized evidence and zero forbidden actions are hard gates. Invalid or inaccessible citations, failed exact structured-fact assertions and failed mandatory CI checks block promotion. Proposed targets for bank sign-off are faithfulness ≥0.90, document recall@8 ≥0.85, Service first-token p95 ≤2 seconds at agreed load, and 100% audited authorized and denied tool calls. Agree Fraud p95 after baseline. Review results by workflow and access scope. A hard security or governance failure means no-go.

## Scheduling dependencies and open decisions

- The critical sequence runs from repository gates and trusted synthetic data through SQL authorization, document ACL and retrieval, evidence validation, then the baseline. Graph scope and provenance precede Fraud activation. Staging, rollback and governance precede any production promotion.
- Start the web shell, evaluation fixtures, security reviews and operations work as soon as their first inputs exist. Establish the initial evaluation set before complete specialist delivery and add graph cases later. Split staging prerequisites from final handover so staging can be exercised before the handover gate.
- Before enabling provider calls with controlled data, security and governance approve vendors, residency, retention, redaction and data flows. Until then use synthetic fixtures and mock adapters as appropriate.
- At kickoff, assign approvers for OIDC issuer and roles, customer and case entitlement rules, source classification and jurisdiction, loan policy and fraud definitions, hosting and release authority, pilot scope, budget and service targets. Record due dates before their dependent work.
- Review blockers and evidence weekly. Raise access-control or data-exposure findings immediately, pause affected promotion, and require verified remediation or a formally narrowed eligible scope before proceeding.

Source basis is the uploaded v2 handbook, especially §§17–18, 22, 24 and 27–30.
