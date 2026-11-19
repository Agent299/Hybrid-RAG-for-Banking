# Hybrid RAG for Banking — Task Completion Tracker

[Execution plan](Hybrid_RAG_Execution_Plan.md)

All tasks start unchecked because this tracker records planned work. Assign one accountable owner when work starts. Use GitHub-compatible checkboxes and edit the corresponding **Log** with `Owner | Status | Evidence | Blocker or next action | Completed date`. Status values are Planned, In progress, Blocked, In review and Done. Keep the box unchecked until the acceptance evidence is reviewed. Dates use YYYY-MM-DD.

For engineering tasks, evidence should include the reviewed PR and passing required CI, relevant tests and documentation, and release or rollback notes for operational changes. For administrative and review tasks, attach the configuration, decision or drill evidence. Protect sensitive evidence through access-controlled links.

Ticket IDs follow handbook §28 where applicable. EVAL-00, EVAL-02, AGT-06, OPS-00, SEC-03 and UAT-01 make milestones and hardening work trackable. Dependencies are sequenced to support the baseline and staged rollout.

## P0 · Weeks 1–2

- [ ] **FND-01** — Bootstrap monorepo + lockfiles
  - **Dependencies** — none
  - **Acceptance** — Fresh clone works
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **FND-02** — Local Compose and migration bootstrap
  - **Dependencies** — FND-01
  - **Acceptance** — Health checks pass
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **FND-03** — Enforce protected main, required reviews and CODEOWNERS
  - **Dependencies** — FND-01; coordinate with CICD-01
  - **Acceptance** — Direct/force push, stale review, red PR and unauthorized bypass blocked
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **CICD-01** — Create mandatory GitHub Actions merge gate
  - **Dependencies** — FND-01; coordinate with FND-03
  - **Acceptance** — Green reviewed PR merges; red or skipped mandatory lane blocks merge
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **CICD-02** — Require Postgres/pgvector integration and denial checks; add Neo4j lane by week 8
  - **Dependencies** — CICD-01, DATA-03; Neo4j checks build on GRA-03
  - **Acceptance** — Denial failures block merge in each active store
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **SEC-01** — OIDC Actor derivation
  - **Dependencies** — FND-01
  - **Acceptance** — Bad JWT blocked
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **DATA-01** — Synthetic generator
  - **Dependencies** — FND-02
  - **Acceptance** — Seed deterministic
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **DATA-02** — Bootstrap normalized domain tables; finish schemas in week 3
  - **Dependencies** — FND-02
  - **Acceptance** — Migrations cleanly apply and FK tests pass
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **DATA-03** — RLS + document ACL views
  - **Dependencies** — DATA-02, SEC-01
  - **Acceptance** — 0 leakage tests
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **API-01** — FastAPI health /v1/me /errors
  - **Dependencies** — SEC-01
  - **Acceptance** — OpenAPI contract
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **EVAL-00** — Draft provisional gold set
  - **Dependencies** — DATA-01
  - **Acceptance** — 40 labeled cases across four domains, including denied requests
  - **Log** — Unassigned | Planned | — | — | —

## P1 · Weeks 3–6

- [ ] **SEC-02** — Permissions catalog / tool allowlist
  - **Dependencies** — SEC-01
  - **Acceptance** — Denied roles tested
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **TOOL-01** — Service SQL tools
  - **Dependencies** — DATA-03
  - **Acceptance** — Exact data + evidence
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **TOOL-02** — Loan SQL/missing-doc tools
  - **Dependencies** — DATA-03
  - **Acceptance** — Correct checklist
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **DOC-01** — Parser + page metadata
  - **Dependencies** — DATA-01
  - **Acceptance** — Coverage tests
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **DOC-02** — Deterministic chunker
  - **Dependencies** — DOC-01
  - **Acceptance** — Stable chunk IDs
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **DOC-03** — Embeddings + vector index
  - **Dependencies** — DOC-02
  - **Acceptance** — Dimension/index checks
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **RET-01** — Auth-scoped lexical/vector search
  - **Dependencies** — DOC-03, DATA-03
  - **Acceptance** — Two branches tested
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **RET-02** — RRF merge
  - **Dependencies** — RET-01
  - **Acceptance** — Order deterministic
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **RET-03** — Cohere rerank + fallback
  - **Dependencies** — RET-02
  - **Acceptance** — Index mapping verified
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **EVI-01** — Evidence/citation schema
  - **Dependencies** — TOOL-01, RET-03
  - **Acceptance** — Invalid cite rejected
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **AGT-01** — Router and typed tool registry
  - **Dependencies** — SEC-02
  - **Acceptance** — Unauthorized route blocked
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **AGT-02** — Service agent
  - **Dependencies** — AGT-01, EVI-01
  - **Acceptance** — Exact facts + cites
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **AGT-03** — Loan agent
  - **Dependencies** — AGT-01, TOOL-02
  - **Acceptance** — No decisions issued
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **AGT-04** — Docs agent
  - **Dependencies** — AGT-01, RET-03
  - **Acceptance** — Cited policy response
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **API-02** — SSE protocol
  - **Dependencies** — EVI-01
  - **Acceptance** — Event E2E test
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **UI-01** — Shared shadcn shell + auth
  - **Dependencies** — API-01
  - **Acceptance** — Four scoped views
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **UI-02** — Chat/citation/source viewer
  - **Dependencies** — API-02
  - **Acceptance** — Auth source fetch
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **CICD-03** — Frontend lint/type/unit/build and locked dependencies
  - **Dependencies** — CICD-01, UI-01
  - **Acceptance** — Next.js failure blocks main
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **EVAL-01** — Build graph-disabled baseline and DeepEval/fixture runner
  - **Dependencies** — EVAL-00, AGT-02, AGT-03, AGT-04
  - **Acceptance** — 100+ gold cases and reproducible baseline metrics with frozen versions
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **CICD-04** — Offline golden-set/citation regression as a mandatory check
  - **Dependencies** — CICD-01, EVAL-01
  - **Acceptance** — Incorrect route/citation/denial fails PR
  - **Log** — Unassigned | Planned | — | — | —

## P2 · Weeks 7–10

- [ ] **GRA-01** — Neo4j ontology/schema
  - **Dependencies** — DATA-02
  - **Acceptance** — Constraints validated
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **GRA-02** — Deterministic graph loader
  - **Dependencies** — GRA-01
  - **Acceptance** — Idempotent build
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **GRA-03** — Safe graph tools + ACL
  - **Dependencies** — GRA-02, SEC-02
  - **Acceptance** — Hidden paths blocked
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **GRA-04** — Typed entity extraction
  - **Dependencies** — DOC-02
  - **Acceptance** — Provenance + review
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **AGT-05** — Fraud agent + graph UI
  - **Dependencies** — GRA-03, EVI-01
  - **Acceptance** — Source-linked paths
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **EVAL-02** — Evaluate paired GraphRAG lift
  - **Dependencies** — EVAL-01, AGT-05
  - **Acceptance** — 30+ multi-hop cases, matched comparison and scope decision
  - **Log** — Unassigned | Planned | — | — | —

## P3 · Weeks 11–13

- [ ] **AGT-06** — Add mixed-domain orchestration and request budgets
  - **Dependencies** — AGT-05, EVI-01
  - **Acceptance** — Approved cross-domain route with authorized sources and enforced tool/time/token limits
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **PIPE-01** — Implement Airflow refresh and blue/green publish
  - **Dependencies** — DATA-01, DOC-03, GRA-02
  - **Acceptance** — Idempotent retry, pinned versions, failed build blocked and rollback verified
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **CICD-05** — Supply-chain audits, scanning and CODEOWNER controls
  - **Dependencies** — CICD-01
  - **Acceptance** — Unaccepted critical/high findings block PR
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **OPS-00** — Prepare hosting, monitoring, audit and operations controls
  - **Dependencies** — API-02, PIPE-01 for refresh telemetry
  - **Acceptance** — Redacted traces, dashboards, audit coverage, load and outage drill evidence
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **CICD-06** — Promote immutable artifact to staging after green main
  - **Dependencies** — CICD-01, OPS-00
  - **Acceptance** — Signed digest tied to green main SHA; OIDC promotion and staging smoke verified
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **SEC-03** — Complete end-to-end security validation
  - **Dependencies** — AGT-06, PIPE-01, CICD-06
  - **Acceptance** — Isolation, injection, PII and revocation checks pass; security sign-off recorded
  - **Log** — Unassigned | Planned | — | — | —

## P4 · Weeks 14–16

- [ ] **UAT-01** — Run approved role-based pilot and close findings
  - **Dependencies** — CICD-06, SEC-03, P3 gate
  - **Acceptance** — Approved pilot scope, UAT evidence from all four workspaces and regression retest
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **CICD-07** — Demonstrate production release controls and rollback
  - **Dependencies** — CICD-06
  - **Acceptance** — Restricted manual approval and signed digest verification proven; rollback recorded
  - **Log** — Unassigned | Planned | — | — | —

- [ ] **OPS-01** — Complete handover and document go/no-go
  - **Dependencies** — UAT-01, CICD-07, OPS-00
  - **Acceptance** — Runbooks, training, support owners, governance decision and approved exceptions recorded
  - **Log** — Unassigned | Planned | — | — | —

## Phase sign-off

Record an approver, decision date and evidence link beside each accepted gate. Review the detailed criteria in the execution plan.

- [ ] **P0** — Protected main, SQL vertical slice and 40 provisional cases.
- [ ] **P1** — Service, Loan and Docs baseline with 100+ gold cases.
- [ ] **P2** — Scoped Fraud, source-backed paths and GraphRAG decision.
- [ ] **P3** — Hard gates green, staging smoke passed and rollback rehearsed.
- [ ] **P4** — UAT, governed release evidence, handover and written go/no-go.

## Decisions and blockers

| Item | Owner | Needed before | Decision or next action | Evidence |
|---|---|---|---|---|
| OIDC and entitlement model | Unassigned | P0 exit | Confirm issuer, roles and access scope | — |
| Providers and data handling | Unassigned | Controlled-data integration | Approve vendor, residency, retention and redaction controls | — |
| Pilot quality, latency and cost targets | Unassigned | Pilot start | Approve targets and measure against representative load | — |
| Pilot data, participant scope and release authority | Unassigned | Pilot start | Record permitted scope and named approvers | — |

For a conditional pilot decision, record permitted workflows, tenants, and data types. Record no-go if a hard security or governance gate fails.
