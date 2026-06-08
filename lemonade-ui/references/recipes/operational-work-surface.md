# Recipe: Operational Work Surface

Use for dashboards, admin tools, finance ops, support queues, internal tools, and dense SaaS surfaces when the user asked for an operational interface or the product is clearly dashboard-first.

Do not use this as the default hero recipe for vague SaaS, CRM, AI, devtool, or product landing prompts. In those cases, use `../no-dashboard-proof.md` first and choose a standalone artifact.

## Structure

- Show real work, not decorative analytics.
- Use rows, filters, selected state, detail panes, actions, statuses, and exceptions.
- Let one object be selected so the viewer understands the job.
- Attach metrics to visible objects or workflow state.

## Layout Moves

- Table/list on one side, selected detail on the other.
- Queue with action drawer.
- Exception lane with review/approve controls.
- Timeline with selected event and next action.
- Split workbench: source input, processing state, output/action.

For landing heroes, crop this into one selected object or action artifact unless the user explicitly wants the full app surface.

## Type

- Use compact labels and strong object names.
- Keep body copy out of the work surface unless it is real note/message content.
- Use numbers as object properties, not loose hero stats.

## Material

- Calm background, precise dividers, restrained color, selected rows, status pills.
- Density should feel useful, not cramped.
- Buttons should attach to the selected object or row.

## Mobile

- Show a selected object card first.
- Collapse rows into a short queue only if the selected action remains visible.
- Hide secondary filters, not primary status/action.
- Avoid shrinking a full desktop table into unreadable mini UI.

## Avoid

- Using this recipe as automatic hero proof for vague SaaS/CRM prompts.
- Four KPI cards as proof.
- Fake charts without controls or selected state.
- Dashboard wallpaper beside marketing copy.
- Rows with generic labels that could belong to any SaaS.
- Decorative density with no action.
