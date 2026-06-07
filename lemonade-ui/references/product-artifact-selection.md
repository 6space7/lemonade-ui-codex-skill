# Product Artifact Selection

Use this before building product proof. The goal is to choose the right visible artifact, not a decorative software preview.

## Artifact Ladder

Prefer the highest truthful artifact available:

1. Real screenshot, real media, or real product object.
2. Workflow fragment with input, state, and output.
3. Selected object detail: record, contact, ticket, clip, order, file, task, deal, job, deployment.
4. Before/after artifact.
5. Operational surface: table/list, filters, selected detail, actions, statuses.
6. Dashboard only when the product is genuinely dashboard-first.

## Dashboard Rule

Dashboard views are allowed when they are the actual product surface. They must include real work:

- Filters or navigation.
- Rows, objects, events, or records.
- Selected state or detail pane.
- Actions attached to the objects.
- Status, empty, loading, warning, or completed states.

If the dashboard is only charts, cards, and summary numbers, reject it.

## Domain Defaults

- **CRM:** contact, deal, follow-up task, call note, email approval, stale account, handoff, pipeline action.
- **AI product:** source input, generated output, edit controls, confidence, citations, export.
- **Developer tool:** log, trace, diff, CLI output, config, deploy, alert, error state.
- **Commerce:** product detail, configurator, cart, variant, review, shipping, checkout.
- **Admin/ops:** table/detail/actions, exception queue, approval, status lane, audit log.
- **Media/creative:** timeline, canvas, layer stack, clip, asset, render/export state.
- **Finance:** transaction, invoice, reconciliation row, approval, forecast delta, ledger state.

## Label-Swap Test

Replace the product labels with generic SaaS labels. If the artifact still works, it is too generic.

Fix it by adding a selected object, domain-specific data, a real action, or an outcome that belongs to this product.

## Hero Artifact Checklist

- Does the artifact show a job being done?
- Is one object selected or one action clearly pending?
- Does it contain real states, not just labels?
- Are metrics attached to the object or workflow?
- Does mobile show a useful crop or object instead of a tiny full preview?
