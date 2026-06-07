# Design Spine

Use this before building a new page, section, component family, or redesign. The goal is to prevent Codex from jumping straight to animation while the actual design stays weak.

## The Six Decisions

Make these decisions before writing UI code:

1. **Product evidence:** What concrete thing proves the product exists?
   Examples: app screen, editor canvas, payment form, schedule, inbox, file object, analytics table, media gallery, location view, device frame, CLI output, physical product, customer quote, or before/after workflow.

2. **Layout lane:** What composition pattern carries the page?
   Examples: editorial split with oversized media, dense product console, full-bleed gallery, left rail plus detail pane, centered commerce configurator, timeline story, magazine grid, board/workspace, stacked comparison, or compact operations dashboard.

3. **Type relationship:** What does typography do?
   Examples: quiet utility sans, editorial display plus functional body, mono for technical proof, condensed labels with roomy body text, large numeric metrics, or understated enterprise hierarchy.

4. **Material system:** What are surfaces made of?
   Examples: paper and ink, glass and chrome, matte panels, dense table rows, soft plastic controls, editorial photo fields, dark technical console, warm hospitality surfaces, or crisp commerce cards.

5. **Content rhythm:** How does the eye move?
   Examples: headline -> product artifact -> CTA, media -> metadata -> case study, filter -> list -> detail, price -> plan -> proof, problem -> workflow -> outcome, gallery -> booking -> location.

6. **Interaction budget:** What one behavior makes the design feel alive?
   Examples: preview switcher, hover-open object, drag completion, card stack reveal, scrubber, dock magnification, elastic divider, or stateful CTA. If the layout is weak, spend zero interaction budget until it is fixed.

## Static-First Rule

The static screenshot must be good before animation. If the page only feels interesting because something moves, the design is not ready.

Check the static design for:

- Clear first read.
- Real product evidence.
- Strong alignment.
- Purposeful whitespace or purposeful density.
- Text hierarchy that works without motion.
- A palette with contrast and restraint.
- Controls that look usable.
- No layout overlap at mobile and desktop widths.

## Section Rhythm

Avoid repeating the same section shape. A good page changes density and reading mode:

- Hero: prove the product.
- Proof: logos, quotes, metrics, or live-looking evidence.
- Workflow: show how the product is used.
- Detail: zoom into a feature or object.
- Comparison: explain why this is different.
- Conversion: make the next action obvious.

Do not default to hero -> three cards -> three cards -> FAQ. Use that only if the product truly needs it.

## Content Quality

Replace generic copy with concrete labels:

- Instead of "Boost productivity with AI", show "Turn 14 missed replies into 3 approved follow-ups."
- Instead of "Advanced analytics", show "17 demos booked, 4 no-shows, 2 contracts awaiting legal."
- Instead of "Automated workflows", show "When invoice is overdue by 7 days, send reminder and open finance task."
- Instead of "Get started", use the actual action: "Import contacts", "Book a demo", "Generate report", "Start recording", "Create workspace".

Use product nouns, verbs, states, counts, dates, names, file types, statuses, and outcomes.

## Art Direction Lanes

Pick one lane and commit:

- **Utility premium:** Dense, calm, work-focused, precise spacing, quiet color, strong tables and panels.
- **Editorial product:** Large media, asymmetry, project metadata, restrained nav, cinematic section changes.
- **Tactile toy:** Soft controls, physical metaphors, saturated accents, press/drag feedback, playful but still usable.
- **Technical console:** Dark or neutral surface, code/log/detail panes, diagrams, status lights, exact labels.
- **Commerce object:** Product inspection, variants, pricing, shipping, reviews, sticky purchase path.
- **Hospitality/place:** Real imagery, booking/menu/schedule/directions, warm surfaces, local details.
- **Creative lab:** Component previews, install affordances, knobs, live states, clear API/use surface.

Avoid mixing more than two lanes on one page.

## Interaction Is Not The Idea

Motion should reinforce a design decision already present:

- If product evidence is weak, add product evidence, not hover effects.
- If hierarchy is unclear, fix type and layout, not entrance animation.
- If content is generic, write better UI copy, not a fancier CTA.
- If mobile is broken, fix constraints, not transitions.
- If the page is boring, choose a stronger art-direction lane before adding motion.
