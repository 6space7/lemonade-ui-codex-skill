# Review Checklist

Use this before finishing a Lemonade UI-style frontend task.

## Product Clarity

- The implementation matches the design contract.
- The chosen default pattern was actually avoided.
- The first viewport says what the product, place, object, or workflow is.
- The main action is visible and clearly clickable.
- The page uses specific content instead of generic placeholder marketing.
- The visual hook belongs to the domain.
- Hiding the logo would not make the page feel like any random AI SaaS template.
- The product artifact has credible labels, data, states, and controls.
- Landing heroes escape the default SaaS stack or clearly justify it.
- Metrics are connected to visible product state.

## Design Spine

- Product moment, artifact, composition, DNA move, mobile proof, copy budget, and avoided default are all clear.
- A clear art-direction lane was chosen.
- A concrete recipe was used when visual direction was open.
- Product evidence, layout, typography, material, content rhythm, and interaction budget are all accounted for.
- The static screenshot works before animation.
- The design has a memorable visual idea beyond hover or scroll effects.
- The page has Lemonade DNA: strong stage/frame/crop/object/material/spatial idea, not just competent layout.

## Layout And Spacing

- Desktop and mobile have intentional composition.
- Spacing follows a visible rhythm, not random gaps or equal padding everywhere.
- Page shell, section padding, group gaps, component padding, and control sizes are coherent.
- Mobile reveals product proof early, not only after headline, paragraph, and stacked CTAs.
- Text does not overlap, clip, or escape controls.
- Fixed-format UI elements have stable dimensions.
- There are no nested cards.
- The next section is hinted below landing-page heroes.
- No unintended horizontal scroll exists.
- Hover, loading, selected, and expanded states do not shift surrounding layout.
- Long labels and realistic data still fit.

## Interaction

- Non-trivial animation has a motion brief: role, trigger, target, state change, bounds, duration/ease, reset, reduced motion.
- The signature motion supports feedback, hierarchy, or continuity.
- Interaction is not carrying the whole design.
- Hover, focus, active, disabled, and loading states are accounted for where relevant.
- Icon-only controls have accessible labels.
- Pointer-only interactions have keyboard/click alternatives when they perform actions.
- Reduced-motion users get a polished static experience.
- Repeated pointer events cannot stack broken animations.

## Visual Taste

- Palette has contrast and range.
- The design is not carried by decorative blobs, bokeh, or generic gradients.
- Typography scale matches context.
- Letter spacing is not negative.
- Images/media reveal the real subject when inspection matters.
- The page has one clear art-direction idea, not a pile of effects.
- Product artifacts feel dimensional and designed, not like flat placeholder mockups.
- Generic "AI-powered" claims are replaced with concrete user actions and proof.

## Engineering

- Existing project patterns are respected.
- Animation cleanup is present.
- Reduced-motion behavior is present.
- Relevant checks pass or failures are clearly explained.
- Browser inspection was performed for frontend changes when possible.
- Desktop and mobile screenshots or observations were compared against the design contract.
- `scripts/audit_lemonade_design.py <path>` was run when available and local files exist.
