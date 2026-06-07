---
name: lemonade-ui
description: Lemonade UI design skill for creating modern, animated, tactile websites and frontend components that avoid generic AI-looking design and buggy frontend output. Use when the user asks for Lemonade UI style, animated shadcn-style components, premium landing pages, startup/SaaS/product sites, dashboards, interactive web app surfaces, or when a frontend looks AI-ish, generic, broken, buggy, visually sloppy, poorly responsive, over-animated, or not polished enough.
---

# Lemonade UI

## Purpose

Use this skill to design and build web experiences with Lemonade UI energy: useful product surfaces, tactile motion, bold composition, and a polished modern feel. Treat generic AI-looking design and buggy responsive behavior as defects, not taste differences.

Load references only as needed:

- `references/design-language.md` for visual taste, composition, page archetypes, and common mistakes.
- `references/motion-recipes.md` for GSAP/CSS/React motion patterns and reduced-motion handling.
- `references/review-checklist.md` before final delivery or when polishing an existing page.

If files exist locally, run `scripts/audit_lemonade_design.py <path>` before final delivery and fix high-signal issues. The script is only a smoke test; visual browser review is still required.

## Working Loop

1. Inspect before touching design.
   - Read local instructions, framework docs required by the repo, existing components, CSS, assets, and dependencies.
   - Use the stack already present. Add animation or UI libraries only when they match the project.
   - Find existing brand, assets, screenshots, components, and layout conventions. Do not invent a new visual system before checking what is already there.

2. Define the product moment.
   - Identify the audience, the thing being sold or used, the first action, and the screen's job.
   - Pick one concrete visual anchor: product UI, dashboard, editor, checkout flow, file object, event gallery, portfolio media, map, timeline, device, board, dock, keyboard, or other real interface object.
   - If the visual anchor could belong to any startup, it is too generic. Replace it with domain-specific content or UI.

3. Design the first viewport to prove the idea.
   - Show the brand/product/place/object immediately.
   - Put the primary action in reach.
   - Leave a hint of the next section visible on landing pages.
   - For apps, tools, dashboards, and games, make the actual usable interface the first screen.

4. Build the boring correctness first.
   - Establish responsive grid, stable dimensions, readable type, real content, focus states, and no-overlap constraints before adding motion.
   - Avoid layout that only works at the current viewport. Check mobile assumptions while building.
   - Make controls functionally obvious before styling them.

5. Add tactile structure.
   - Use stable dimensions for controls, tiles, boards, previews, counters, and cards.
   - Use icons for icon-worthy actions, segmented controls for modes, toggles for booleans, menus for option sets, sliders/inputs for numbers, and tabs for views.
   - Keep cards for repeated items, framed tools, and modals. Avoid nested cards and decorative section cards.
   - Use real assets, screenshots, generated bitmap imagery, or product UI where inspection matters.

6. Add one memorable interaction.
   - Choose one signature behavior per section: magnetic CTA, hover-open object, elastic divider, drag-to-complete, dock magnification, marquee pause, card stack spread, preview switcher, or state transition.
   - Make motion communicate feedback, hierarchy, or continuity.
   - Respect reduced motion. Keep the static layout beautiful.

7. Kill the AI-ish parts.
   - Remove vague glowing blobs, mesh-gradient hero filler, fake dashboards with generic cards, repeated three-card grids, empty "AI-powered" claims, and over-rounded nested surfaces.
   - Replace abstract decoration with product evidence: real UI, specific data, credible states, useful controls, media, proof, or workflow.
   - If hiding the logo makes the page feel like any other AI SaaS template, redesign the visual anchor.

8. Prove it in browser.
   - Check mobile and desktop. Fix overlap, clipping, awkward wrapping, contrast issues, blank media, layout shift, and cramped controls.
   - Keep letter spacing at `0` unless an existing design system says otherwise.
   - Avoid visible text explaining how the UI works. Make the UI understandable.
   - Do not call the design finished from code inspection alone when a dev server or static preview can run.

## Lemonade Bar

A Lemonade UI result should feel:

- **Specific:** It belongs to the product category, not a generic SaaS template.
- **Useful:** The component or page could live in a real workflow.
- **Tactile:** Hover, press, drag, focus, and selected states have physical presence.
- **Alive:** Motion is crisp, restrained, and tied to meaning.
- **Accessible:** Semantic markup, focus states, labels, contrast, and reduced-motion behavior are present.
- **Finished:** It survives build checks and visual inspection at real viewport sizes.

## Hard Fails

Do not ship while any of these are true:

- The hero is mostly text over a gradient, blob, orb, or vague abstract background.
- The main product artifact is a fake dashboard made of generic "Analytics", "Growth", "Automation", or "Insights" cards.
- Mobile has clipped buttons, overlapping text, horizontal scroll, or unreadable controls.
- Motion is present but no reduced-motion path exists.
- Icon-only buttons lack accessible names.
- Hover states change layout size or move surrounding content.
- The page looks acceptable only in one viewport.
- The design relies on visible instructions instead of clear controls.

## Strong Defaults

- Prefer `lucide-react` icons in React projects when available.
- Prefer GSAP for pointer-reactive or timeline-heavy motion when the project already uses it; otherwise use the local motion stack or CSS transitions.
- Prefer a few saturated accents against neutral surfaces over one-note purple, blue-slate, beige, brown/orange, or dark-gradient themes.
- Prefer product mockups, real media, or generated bitmap images over SVG-only hero decoration.
- Prefer direct implementation over long planning when the user asks to build or improve a design.

## Delivery Standard

Ship working files, not design commentary. Before final response, run relevant checks, run the Lemonade audit script when files are local, and visually inspect the page or component when possible. Report what changed, what passed, what was visually verified, and any blocker that prevented full verification.
