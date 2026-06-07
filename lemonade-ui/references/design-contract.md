# Design Contract

Use this before coding open-ended frontend work: landing pages, hero sections, product pages, dashboards, pricing pages, app surfaces, and redesigns.

The contract exists because models often agree with taste guidance, then fall back to trained template habits during CSS and layout. The contract makes the visual decision explicit before implementation starts.

## Required Contract

Write a compact contract in working notes:

```text
Design contract:
Moment: ...
Artifact: ...
Composition: ...
DNA move: ...
Mobile proof: ...
Copy budget: ...
Avoiding: ...
```

## Field Rules

- **Moment:** one specific job, state, workflow, or object. Avoid broad category claims.
- **Artifact:** the visible proof object. Prefer selected records, editors, files, media, rows, messages, outputs, timelines, tables, objects, or real screenshots.
- **Composition:** choose one layout lane or recipe. Do not default to a generic split hero.
- **DNA move:** one memorable stage, frame, crop, object, material, glow, dimensional layer, or spatial gesture.
- **Mobile proof:** what the first mobile viewport shows before the user scrolls far.
- **Copy budget:** set limits before writing copy.
- **Avoiding:** name the lazy pattern being rejected.

## Copy Budget Defaults

For landing heroes:

- Headline: 2 to 4 short lines, not a paragraph disguised as type.
- Supporting copy: 12 to 28 words.
- CTAs: one primary action; one secondary only if it has a different real job.
- Stats: only when attached to a visible artifact or product state.
- Badge/eyebrow: optional; remove it if it delays proof.

For product sections:

- Heading: one clear claim.
- Body: one short sentence or no body if the artifact explains it.
- Microcopy: move details into the product artifact whenever possible.

## Vague Prompt Rescue

When the prompt only names a category, invent a small believable moment:

- CRM: stale deal, follow-up approval, call note, email draft, contact detail, handoff, pipeline action.
- AI tool: source input, generated output, edit controls, confidence, citation, export.
- Devtool: failing log, diff, deploy trace, CLI command, config, alert.
- Finance/ops: exception queue, reconciliation row, approval, ledger item, audit trail.
- Commerce: product detail, cart state, variant selector, checkout, shipping issue.
- Creative/media: canvas, timeline, layer stack, clip, render, export state.

Do not invent an elaborate fake company story. Invent the smallest user job that can be shown clearly.

## Bad Contracts

Reject contracts like:

- Moment: "AI productivity for teams"
- Artifact: "dashboard mockup"
- Composition: "modern split hero"
- DNA move: "gradient background"
- Mobile proof: "mockup below text"
- Copy budget: "normal SaaS copy"
- Avoiding: "none"

They are not specific enough to protect the design.

## Better Contracts

Example:

```text
Design contract:
Moment: Turn a stale renewal note into an approved follow-up.
Artifact: Selected account record, call note, draft reply, and approval action.
Composition: Dark product theatre with the selected record cropped large.
DNA move: Lit work surface with two floating proof chips and a side annotation.
Mobile proof: Selected account card and approval button appear before secondary copy.
Copy budget: 3-line headline, 18-word paragraph, one primary CTA, no loose stats.
Avoiding: generic split hero, framed dashboard wallpaper, floating metrics row.
```

## Use The Contract During Review

After the browser screenshot:

- If the artifact does not dominate, enlarge, crop, or move it earlier.
- If mobile proof is late, rewrite mobile order instead of shrinking desktop.
- If the DNA move is invisible, strengthen the stage, frame, crop, material, or object.
- If the avoided default is still visible, redesign the structure before adding polish.
