# Visual Reference Calibration

Use this when the user provides screenshots, a moodboard, or asks for a stronger Lemonade vibe.

The goal is not to clone a reference. The goal is to extract visual decisions that text guidance cannot carry: scale, crop, contrast, rhythm, object treatment, and atmosphere.

## Extract, Do Not Copy

For each reference, identify:

- **Stage:** dark field, bright shaped panel, editorial page, poster frame, app theatre, gallery wall.
- **Dominant object:** software surface, card, device, file, record, media, illustration, product object.
- **Crop:** full view, oversized slice, angled object, partial reveal, below-fold hint, side cut.
- **Depth:** overlap, shadow, glow, blur, parallax, stacked surfaces, foreground/background.
- **Typography:** centered poster type, quiet utility type, huge display type, small technical labels.
- **Color behavior:** mostly black/white, one electric accent, warm glow, brand field, muted utility palette.
- **Proof density:** one object, row/detail surface, many fragments, narrative sequence, real media.
- **Mobile lesson:** what survives when the screen is narrow.

Use those extracted decisions in the design contract.

## Lemonade Reference Traits

Strong Lemonade-compatible references usually have at least two of these:

- A page that feels like a product poster, not a template.
- One obvious stage or frame that gives the design a silhouette.
- Product UI treated as an object with lighting, crop, depth, or motion.
- Small inspectable details inside the product artifact.
- Copy that is short enough for the artifact to carry meaning.
- Sections that change scene instead of repeating card grids.
- Dark or high-contrast atmosphere when it supports the product.
- A mobile version that shows a useful product crop early.

## Reference-To-Implementation Moves

- Dark product reference -> use one lit artifact, edge atmosphere, minimal copy, and a strong crop.
- Shaped green/brand-field reference -> use one oversized field, carved corners or capsule edges, and a product object floating inside.
- Layered software reference -> choose one dominant panel and two supporting fragments, not a pile of equal cards.
- Editorial long page reference -> make each section a composed scene with a different reading mode.
- Technical dark reference -> use logs, diffs, commands, status lights, and monospace proof, not generic app cards.
- Commerce/object reference -> put the object or configurator first; let purchase state and variants carry proof.

## Calibration Questions

Ask before coding:

- What is the silhouette of the page?
- What is the first object the eye remembers?
- What is cropped or staged in a way that could not belong to every SaaS?
- What product detail rewards a closer look?
- What visual move survives on mobile?

If the answers are vague, choose a recipe before coding.

## Guardrails

- Do not copy logos, exact layouts, proprietary screenshots, brand marks, or distinctive illustration assets.
- Do not reference private user screenshots in public output unless the user asks.
- Do not use a reference as an excuse for illegible text, broken responsive layout, or decorative UI.
- If a reference is visually strong but product proof is weak, keep the composition lesson and replace the proof.
