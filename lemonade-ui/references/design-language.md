# Design Language

Use this reference when choosing the visual direction for a Lemonade UI-style page, component, or redesign.

## Taste Targets

- Start from a real product moment: booking, paying, organizing, browsing, selecting, editing, shipping, comparing, uploading, monitoring, or presenting.
- Give the interface a tangible object: folder, card stack, dock, slider, board, keyboard, phone pill, control bar, floating note, payment card, gallery strip, or product mockup.
- Use a restrained structure with one expressive hook. The hook can be composition, media, typography, product evidence, material, or motion. It does not have to be an interaction.
- Make text, media, controls, and motion feel composed as one scene.
- Build controls users recognize. Style them richly, but do not make common actions mysterious.

## Design Layers

Solve these in order:

1. Product evidence.
2. Layout and rhythm.
3. Typography and content.
4. Palette and material.
5. Component states and controls.
6. Interaction and motion.
7. Browser QA.

If a later layer is doing the work of an earlier layer, go back. Animation cannot fix weak product evidence. Color cannot fix vague content. Shadows cannot fix bad hierarchy.

## Anti-AI Standard

Assume the first idea is probably too generic. Before implementing, identify the most likely AI-ish failure and design against it.

Reject:

- Hero sections that are mostly a centered headline, pill, CTA pair, and gradient blob.
- "AI-powered" copy without a concrete user action or product artifact.
- Fake dashboards with generic cards named Analytics, Insights, Automation, Growth, or Revenue.
- Endless rounded cards with icons and short blurbs.
- Purple/blue mesh gradients as the main art direction.
- Abstract SVG decoration where product UI, real media, or a generated bitmap scene would be more specific.
- Decorative motion that does not reveal, confirm, navigate, select, complete, or explain state.

Replace with:

- A believable product surface with real labels, rows, tabs, filters, records, charts, controls, or states.
- A domain-specific object or media moment.
- A specific workflow: before/after, queue/detail, picker/preview, edit/export, schedule/confirm, browse/compare, plan/pay.
- A memorable visual idea tied to that workflow. It may be layout, type, material, image, product UI, or interaction.

## Composition Patterns

### Product Landing

Lead with a product surface, not a slogan alone. Show the workflow through a dashboard, timeline, editor, inbox, canvas, kanban board, automation map, or believable mockup.

Good first-viewport ingredients:

- Brand and concise navigation.
- One sharp headline and one clear primary action.
- Inspectable product UI with real labels and states.
- Trust or proof that does not crowd the hero.
- A visible next section edge.

Quality test: hide the logo. If the page could still be any random SaaS, the product surface is not specific enough.

### Component Lab

Make each component installable in spirit even when it is not a package. Use typed props, defaults, accessible labels, and no demo-only assumptions.

Good components have:

- A clear real-world role.
- One primary interaction.
- Good fallback content.
- Stable sizing under hover, loading, and long text.
- A static state that still looks intentional.

Quality test: swap in longer labels, missing optional props, and reduced motion. The component should remain stable.

### Dashboard or Admin

Keep it quiet and useful. Put navigation, filters, tables, detail panes, status chips, and repeated actions in predictable places. Use motion for continuity and confirmation, not spectacle.

Avoid marketing-style hero sections in operational tools.

Quality test: a repeated operator should understand the next action in under three seconds.

### Portfolio or Editorial

Use media as the layout engine: full-bleed images, project metadata, large but controlled typography, index-to-preview navigation, and cinematic transitions.

Avoid generic agency copy with no proof, project names, or media.

### Event, Place, or Restaurant

Show the actual place, menu, schedule, ticket, map, or booking state early. Motion can support a gallery loop, reservation picker, route reveal, or schedule cards.

Avoid dark blurred atmosphere when users need to understand the venue.

## Visual Rules

- Use contrast between surface, content, and action. Do not tint everything the same hue.
- Keep cards at 8px radius or less unless the component's physical metaphor needs more.
- Do not place cards inside cards.
- Do not use decorative orbs, bokeh blobs, or generic gradient blobs as the main design idea.
- Do not scale font size with viewport width.
- Do not use negative letter spacing.
- Use `text-wrap: balance` or careful line breaks only where it improves readability.
- For long values in controls, intentionally wrap, truncate, or resize so text never escapes its container.
- Use stable min-height, aspect-ratio, or grid tracks for repeated tiles and fixed-format UI.
- Avoid full-screen hero sections that hide the next section on landing pages.
- Use real images or generated bitmap images for subject matter when users need to inspect the thing being sold.
- Avoid identical section rhythms. Change density, alignment, or reading mode between major sections.
- Use whitespace as a structural tool, not empty decoration.
- Keep labels, metadata, timestamps, statuses, and counts believable.

## Typography And Content

- Write UI copy as product behavior, not marketing fog.
- Use concrete nouns and verbs: import, approve, schedule, export, reconcile, record, publish, route, pay, compare.
- Use real-feeling labels: customer names, file names, statuses, dates, prices, durations, tags, locations, and counts.
- Make headings shorter than the supporting body. Do not stack multiple slogan lines.
- Pair display type with a clear body hierarchy. Do not use hero-scale type inside compact cards or controls.
- If the type scale is the main visual idea, keep color and surfaces calmer.

## Palette Guidance

Use neutral bases with a few sharp accents. Good Lemonade-style palettes often combine:

- Clean whites or near-blacks.
- One electric accent such as lime, blue, coral, yellow, or pink.
- One muted support color.
- Borders and shadows that give structure without fog.

Avoid a page that reads as all purple, all beige, all slate, all brown/orange, or all dark gradient unless the brand requires it and the layout has enough contrast.

## Common Failure Modes

- Pretty hero, unclear product.
- Too many floating cards with no hierarchy.
- Animation that fires constantly but says nothing.
- Components that only work with short demo text.
- Buttons that look like labels.
- Mobile layout treated as an afterthought.
- Stock-feeling imagery that hides the thing being sold.
- One viewport looks good while mobile breaks.
- Text uses viewport units and explodes on wide or narrow screens.
- Hover effects resize the layout.
- The design is "premium" only because everything is blurred, glassy, and rounded.
