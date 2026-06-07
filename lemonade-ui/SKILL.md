---
name: lemonade-ui
description: Lemonade UI design skill for creating modern, animated, tactile websites and frontend components that avoid generic AI-looking design, excessive copy, weak hierarchy, bad responsive composition, and buggy frontend output. Use when the user asks for Lemonade UI style, animated shadcn-style components, premium landing pages, startup/SaaS/product sites, dashboards, interactive web app surfaces, or when a frontend looks AI-ish, text-heavy, generic, broken, buggy, visually sloppy, poorly responsive, over-animated, or not polished enough.
---

# Lemonade UI

## Purpose

Build web experiences with useful product surfaces, strong composition, sharp copy, real product evidence, tactile structure, and restrained motion. Interaction is a finishing layer, not the design itself.

## Reference Router

Load only the files needed for the current problem:

- `references/design-spine.md`: start here for new pages, broad redesigns, or unclear visual direction.
- `references/lemonade-visual-dna.md`: use when the page needs Lemonade vibe, stronger art direction, memorable composition, or positive taste guidance.
- `references/saas-hero-escape-system.md`: use before SaaS/product/startup landing heroes to avoid the generic AI SaaS hero stack.
- `references/product-artifact-selection.md`: use before product proof to choose the right artifact, workflow fragment, or operational surface.
- `references/calibration-overcopy-and-scale.md`: use when the design is mostly giant text, yapping, weak copy rhythm, or hero-scale type doing too much.
- `references/calibration-product-proof.md`: use when the page says what the product does but does not show credible product evidence.
- `references/calibration-responsive-composition.md`: use when desktop and mobile feel like the same layout awkwardly stretched or stacked.
- `references/calibration-operational-ui.md`: use when dashboards, admin panels, internal tools, or work surfaces feel too decorative, sparse, or marketing-like.
- `references/copy-compression.md`: use when the UI feels text-heavy, salesy, explainy, or full of big headline/paragraph blocks.
- `references/visual-hierarchy.md`: use for typography, spacing, layout, color/material, and first-viewport composition.
- `references/responsive-composition.md`: use for mobile/desktop strategy, stacked layouts, clipped content, and breakpoint polish.
- `references/product-evidence.md`: use when the design lacks credible product UI, real media, proof, or domain-specific detail.
- `references/anti-ai-slop.md`: use when the design feels generic, AI-ish, card-heavy, blob-heavy, or template-like.
- `references/motion-recipes.md`: use only after the static design works and motion has a clear job.
- `references/review-checklist.md`: use before final delivery.

If files exist locally, run `scripts/audit_lemonade_design.py <path>` before final delivery and fix high-signal issues. The script is a smoke test; browser review is still required.

## Working Loop

1. Inspect first.
   - Read local instructions, framework docs required by the repo, existing components, CSS, assets, and dependencies.
   - Find existing brand, assets, screenshots, components, and layout conventions before inventing anything.

2. Create the design spine.
   - Decide product evidence, layout lane, type relationship, material system, content rhythm, and interaction budget.
   - The static screenshot must already work before animation.

3. Apply Lemonade visual DNA.
   - Load `lemonade-visual-dna.md` when visual direction is open or the work should feel distinctly Lemonade.
   - Choose one memorable stage, frame, crop, object, material, or spatial idea.
   - Do not rely on correct product logic alone; the page needs a positive visual point of view.

4. Escape the default SaaS hero when relevant.
   - For SaaS, startup, AI tool, CRM, devtool, and product landing heroes, load `saas-hero-escape-system.md`.
   - Choose a product moment and at least one non-default composition move before coding.
   - Do not let the hero become headline, paragraph, CTA pair, stats, framed UI preview, and soft background by default.

5. Select the product artifact.
   - Load `product-artifact-selection.md` when product proof is needed.
   - Prefer real screenshots/media, workflow fragments, selected objects, before/after outputs, or operational surfaces.
   - Use dashboards only when the product is genuinely dashboard-first and the dashboard behaves like a real work surface.

6. Calibrate by failure mode.
   - Pick a calibration reference by the design problem, not by product category.
   - Use calibration files as taste correction, not templates to copy.
   - Do not invent fake product names for examples unless the user provided the product.

7. Compress the message.
   - If the UI can show it, do not explain it in a paragraph.
   - Replace generic marketing copy with product nouns, verbs, states, counts, and outcomes.

8. Build visual hierarchy.
   - Make the first read obvious.
   - Use type, spacing, alignment, contrast, and material before motion.
   - Keep hero-scale type out of compact cards, dashboards, and controls.

9. Prove the product.
   - Use credible UI, real screenshots/media, generated bitmap scenes, product artifacts, workflow states, or proof.
   - If hiding the logo makes the page feel like any random SaaS, redesign the visual anchor.

10. Design responsive composition.
   - Mobile is a rewritten story, not desktop stacked vertically.
   - Desktop should use space intentionally, not just bigger cards.
   - Fix clipping, overlap, horizontal scroll, tap targets, and text fit while building.

11. Spend motion carefully.
   - Add at most one signature interaction per section.
   - Motion must reveal, confirm, select, complete, navigate, or clarify state.
   - Respect reduced motion and keep the static layout beautiful.

12. Prove it in browser.
   - Check desktop and mobile.
   - Run relevant checks and the Lemonade audit script.
   - Do not call frontend design complete from code inspection alone when a preview can run.

## Hard Fails

Do not ship while any are true:

- The design only becomes interesting when animated.
- The page is mostly huge text and explanatory paragraphs.
- The hero is text over a blob, orb, mesh gradient, or vague abstract background.
- The main product artifact is a fake dashboard with generic Analytics/Growth/Automation/Insights cards.
- The page defaults to a generic split hero with a framed app preview, loose stats, placeholder branding, and no stronger composition idea.
- Mobile first viewport is mostly brand, badge, oversized headline, paragraph, and stacked CTAs before product proof.
- The guidance or output is quietly copying one sample product category instead of solving the current user's product.
- The page is correct but has no memorable stage, frame, crop, object, material, or spatial idea.
- Mobile is just a cramped stacked desktop layout.
- Type hierarchy, content rhythm, or art direction is unclear.
- Hover states move surrounding layout.
- Motion exists without reduced-motion behavior.
- Icon-only controls lack accessible names.
- The page looks acceptable in only one viewport.

## Delivery Standard

Ship working files, not design commentary. Report what changed, what checks passed, what was visually verified, and any blocker that prevented full verification.
