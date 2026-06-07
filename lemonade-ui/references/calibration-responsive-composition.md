# Calibration: Responsive Composition

Use this when the desktop design is acceptable but mobile feels cramped, over-tall, clipped, or like columns were only stacked.

## Failure Pattern

- Desktop has several panels with equal weight and no clear dominant artifact.
- Mobile repeats the full desktop story in the same order.
- Header, nav, CTA, badge, headline, paragraph, and stats all fight for first-screen space.
- Product proof arrives too late on small screens.

## Better Direction

- Rewrite the mobile story: promise, action, proof, artifact slice, outcome.
- Give desktop one dominant visual anchor instead of multiple equal cards.
- Crop or simplify the product artifact on mobile instead of shrinking the whole thing.
- Remove secondary copy and controls from the first mobile viewport.

## Implementation Cues

- Use breakpoint-specific order, not only grid column changes.
- Let mobile show a focused slice of the product.
- Keep tap targets stable and at least 44px where possible.
- Avoid layout shifts from hover states, labels, badges, and dynamic counters.
- Test narrow mobile, large mobile, tablet, and desktop before final delivery.

## Checklist

- Is mobile a shorter story, not a smaller desktop?
- Does desktop use wide space for contrast and workflow clarity?
- Are buttons, labels, and type contained at every breakpoint?
- Can touch users access every important interaction?
