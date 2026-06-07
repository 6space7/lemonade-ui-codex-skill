---
name: lemonade-ui
description: Lemonade UI design skill for creating modern, animated, tactile websites and frontend components with premium visual direction, real product utility, responsive polish, accessible interactions, and tasteful motion. Use when the user asks for Lemonade UI style, Lemonade components, animated shadcn-style components, modern website design, premium landing pages, startup/SaaS/product sites, interactive web app surfaces, or making a frontend feel more alive, polished, distinctive, or high-end.
---

# Lemonade UI

## Purpose

Use this skill to design and build web experiences with Lemonade UI energy: useful product surfaces, tactile motion, bold composition, and a polished modern feel without drifting into generic gradient/card templates.

Load references only as needed:

- `references/design-language.md` for visual taste, composition, page archetypes, and common mistakes.
- `references/motion-recipes.md` for GSAP/CSS/React motion patterns and reduced-motion handling.
- `references/review-checklist.md` before final delivery or when polishing an existing page.

## Working Loop

1. Inspect the project before designing.
   - Read local instructions, framework docs required by the repo, existing components, CSS, assets, and dependencies.
   - Use the stack already present. Add animation or UI libraries only when they match the project.

2. Define the product moment.
   - Identify the audience, the thing being sold or used, the first action, and the screen's job.
   - Pick one concrete visual anchor: product UI, dashboard, editor, checkout flow, file object, event gallery, portfolio media, map, timeline, device, board, dock, keyboard, or other real interface object.

3. Design the first viewport to prove the idea.
   - Show the brand/product/place/object immediately.
   - Put the primary action in reach.
   - Leave a hint of the next section visible on landing pages.
   - For apps, tools, dashboards, and games, make the actual usable interface the first screen.

4. Build with tactile structure.
   - Use stable dimensions for controls, tiles, boards, previews, counters, and cards.
   - Use icons for icon-worthy actions, segmented controls for modes, toggles for booleans, menus for option sets, sliders/inputs for numbers, and tabs for views.
   - Keep cards for repeated items, framed tools, and modals. Avoid nested cards and decorative section cards.
   - Use real assets, screenshots, generated bitmap imagery, or product UI where inspection matters.

5. Add one memorable interaction.
   - Choose one signature behavior per section: magnetic CTA, hover-open object, elastic divider, drag-to-complete, dock magnification, marquee pause, card stack spread, preview switcher, or state transition.
   - Make motion communicate feedback, hierarchy, or continuity.
   - Respect reduced motion. Keep the static layout beautiful.

6. Polish like it will be screenshotted.
   - Check mobile and desktop. Fix overlap, clipping, awkward wrapping, contrast issues, blank media, layout shift, and cramped controls.
   - Keep letter spacing at `0` unless an existing design system says otherwise.
   - Avoid visible text explaining how the UI works. Make the UI understandable.

## Lemonade Bar

A Lemonade UI result should feel:

- **Specific:** It belongs to the product category, not a generic SaaS template.
- **Useful:** The component or page could live in a real workflow.
- **Tactile:** Hover, press, drag, focus, and selected states have physical presence.
- **Alive:** Motion is crisp, restrained, and tied to meaning.
- **Accessible:** Semantic markup, focus states, labels, contrast, and reduced-motion behavior are present.
- **Finished:** It survives build checks and visual inspection at real viewport sizes.

## Strong Defaults

- Prefer `lucide-react` icons in React projects when available.
- Prefer GSAP for pointer-reactive or timeline-heavy motion when the project already uses it; otherwise use the local motion stack or CSS transitions.
- Prefer a few saturated accents against neutral surfaces over one-note purple, blue-slate, beige, brown/orange, or dark-gradient themes.
- Prefer product mockups, real media, or generated bitmap images over SVG-only hero decoration.
- Prefer direct implementation over long planning when the user asks to build or improve a design.

## Delivery Standard

Ship working files, not design commentary. Before final response, run relevant checks and visually inspect the page or component when possible. Report what changed, what passed, and any blocker that prevented full verification.
