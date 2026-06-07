# Design Language

Use this reference when choosing the visual direction for a Lemonade UI-style page, component, or redesign.

## Taste Targets

- Start from a real product moment: booking, paying, organizing, browsing, selecting, editing, shipping, comparing, uploading, monitoring, or presenting.
- Give the interface a tangible object: folder, card stack, dock, slider, board, keyboard, phone pill, control bar, floating note, payment card, gallery strip, or product mockup.
- Use a restrained structure with one expressive hook. If everything is loud, nothing feels premium.
- Make text, media, controls, and motion feel composed as one scene.
- Build controls users recognize. Style them richly, but do not make common actions mysterious.

## Composition Patterns

### Product Landing

Lead with a product surface, not a slogan alone. Show the workflow through a dashboard, timeline, editor, inbox, canvas, kanban board, automation map, or believable mockup.

Good first-viewport ingredients:

- Brand and concise navigation.
- One sharp headline and one clear primary action.
- Inspectable product UI with real labels and states.
- Trust or proof that does not crowd the hero.
- A visible next section edge.

### Component Lab

Make each component installable in spirit even when it is not a package. Use typed props, defaults, accessible labels, and no demo-only assumptions.

Good components have:

- A clear real-world role.
- One primary interaction.
- Good fallback content.
- Stable sizing under hover, loading, and long text.
- A static state that still looks intentional.

### Dashboard or Admin

Keep it quiet and useful. Put navigation, filters, tables, detail panes, status chips, and repeated actions in predictable places. Use motion for continuity and confirmation, not spectacle.

Avoid marketing-style hero sections in operational tools.

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
