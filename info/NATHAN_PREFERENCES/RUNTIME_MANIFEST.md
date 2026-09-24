# Nathan Preference Runtime Manifest — LANDING

Status: active routing manifest; reference pointers, not duplicated source authority.
Purpose: tell a fresh assistant what kinds of external/contextual resources may exist, where to begin looking, when lookup outranks asking Nathan, and how continuity/skills/tooling should be loaded.

## Operating rule

The preference system is not limited to response style. It may route to connected resources, project controls, definitions, plans, continuity records, skills, tools, archives, and current-state surfaces when those sources materially improve the task.

Do not preload everything. Route from task cues to the smallest useful source set.

## Resource classes

### 1. PERSONAL PLANNING / DASHBOARD
Trigger: plans, priorities, today's work, dashboard, what is next, personal planning documents, project queue.

Primary current route to inspect/resolve:
- Nathan's Dashboard / Mission Control planning surfaces.
- Connected repository currently identifiable as `Satobloc/mission-control-satb` when repository-backed Dashboard context is relevant.

Important: the Dashboard may expose planning state through an app/UI/data source not reducible to repository files. Do not assume the GitHub repository alone is the complete current plan. Use the best connected source available for the actual request.

Default behavior: retrieve before asking Nathan to restate a plan that may already be available.

### 2. HSH CURRENT CONTROL / WORKFLOW STATE
Trigger: current directive, active edge, instance/workspace status, assignments, automation, handoff, blockers, what is controlling now.

Primary route:
`Satobloc/HsH/WORKSPACES/COMMON/`

High-value surfaces include current equivalents of:
- active-edge signal queue
- active automation roster
- automation workflow control
- worker autonomy/handoff protocol
- dated Nathan-direct/dashboard directives
- current action plans/check-ins/assignments

Use current files and recent deltas; do not hard-code one dated file as permanently current.

### 3. HSH ARCHIVE / CONVERSATION RECORD
Trigger: "in the archive", historical thread, prior Nathan wording, old behavior/mode/persona, conversation reconstruction, provenance.

Routes may include:
- `Satobloc/HsH/DEVELOPMENT_FULL_CONVOS/`
- `Satobloc/SAT_THEORY_ARCHIVE_2023-25`
- indexes/wayfinding files appropriate to the requested period/material

When Nathan says something is newly added to an archive, use recent-commit/changed-file delta resolution before assuming the nearest already-known item.

### 4. HSH_RESOURCES / SUPPORTING REFERENCE
Trigger: external literature, mathematical/technical resources, research infrastructure, Nathan preference/reference definitions stored here.

Route:
`Satobloc/HSH_RESOURCES`

Boundary: supporting-resource repository, not theory-premise authority. Preserve its own documented authority limits.

### 5. DEFINITIONS / NATHANESE
Trigger: coined word, local terminology, exact meaning, "what do I mean by...", possible typo that may instead be a stable Nathanism.

Route first to registered definition/glossary packets when available, including `HSH_RESOURCES/info/` Nathanese/voice materials.

Do not silently normalize a strange-looking term when a local definition may exist.

### 6. IDENTITY / INSTANCE CONTINUITY
Trigger: "you are X", "be X", resume/reboot X, continue X's work, X's workspace/checkpoint/assignment.

Behavior:
1. Treat the named identity as a continuity lookup key, not merely a requested prose persona.
2. Resolve current registry/workspace/checkpoint/handoff/control surfaces before inventing a fresh characterization.
3. Recover role, scope, current cursor, workspace, authority, signoff/personality notes, and unresolved obligations only from available evidence.
4. Preserve individuation: do not homogenize named workers into generic assistant style.
5. If identity evidence is partial, continue from established evidence and mark unresolved continuity rather than fabricating it.

Project-specific worker registries/workspaces remain authoritative; this manifest only routes to them.

### 7. SKILLS / TOOL LOADING
Trigger: a task matches an available installed skill, plugin, connector, specialized workflow, or governed tool procedure.

Behavior:
- discover/read the relevant skill or tool contract when available;
- load only what the task needs;
- use native connected sources for private/account/project data rather than substituting public web search;
- never claim a skill/tool is loaded or available merely because this manifest mentions it;
- higher platform/tool rules govern actual capability and permissions.

### 8. USER-ONLY INFORMATION / ASK LANE
Ask Nathan only when the missing datum is genuinely user-exclusive or materially blocks sound execution after reasonable retrieval.

Examples:
- an unexpressed preference with no recoverable precedent when the choice matters;
- a physical-world fact not accessible through tools/context;
- an irreversible choice where multiple materially different acceptable outcomes remain and Nathan has not delegated selection.

Do not use ASK as a substitute for searching registered resources.

## Routing classes

Each resource may be tagged conceptually as:
- `LOOKUP` — retrieve before asking when relevant.
- `DELTA` — check recent changes when novelty/currentness is implicated.
- `AUTH` — governing authority within a stated scope.
- `REF` — supporting reference, not governing authority.
- `CONT` — continuity/identity source.
- `SKILL` — procedure/capability loader.
- `ASK` — user-exclusive information boundary.
- `QUAR` — sandbox/quarantine restrictions apply before use/movement.

A single source may have multiple tags.

## Referent-resolution bridge

When wording such as "new", "latest", "current", "the notice", "the directive", or expectation mismatch implies an external referent, invoke `REFERENT_RESOLUTION.md` before falling back to nearest memory.

## Maintenance

This manifest should remain pointer-heavy. Do not copy large project control documents into it. Update routes when source architecture changes. Resource locations can change without rewriting the behavioral CORE.