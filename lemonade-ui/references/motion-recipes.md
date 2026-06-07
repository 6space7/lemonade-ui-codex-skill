# Motion Recipes

Use this reference when adding Lemonade UI-style interaction, especially in React components.

## Principles

- Animate feedback, not decoration.
- Keep the main text stable while surrounding surfaces move.
- Prefer one signature motion per section.
- Make hover and focus states equivalent where possible.
- Provide a reduced-motion path for pointer-reactive, looping, or entrance motion.
- Never use motion to compensate for weak layout or vague product content.
- Do not animate dimensions that can reflow surrounding content unless the container is explicitly reserved.

## Recipes

### Entrance Reveal

Use for hierarchy when content enters the viewport or mounts.

```tsx
useGSAP(
  () => {
    if (!rootRef.current || reducedMotion) return

    const context = gsap.context(() => {
      gsap.fromTo(
        "[data-reveal]",
        { y: 22, opacity: 0, filter: "blur(8px)" },
        { y: 0, opacity: 1, filter: "blur(0px)", duration: 0.7, stagger: 0.07, ease: "power3.out" }
      )
    }, rootRef)

    return () => context.revert()
  },
  { dependencies: [reducedMotion], scope: rootRef }
)
```

### Magnetic Button

Use for a primary CTA or compact action. Move the shell subtly; keep the label readable.

- Track pointer position relative to the button.
- Translate the surface no more than 6-12px.
- Snap back with `elastic.out` or a spring-like CSS transition.
- Reset on pointer leave, blur, and reduced motion.

### Hover-Open Object

Use for folders, stacks, drawers, cards, panels, or product previews.

- Animate the object open on hover/focus.
- Reveal useful secondary content, not decoration only.
- Close with a slower elastic settle.
- Preserve layout size so surrounding content does not jump.

### Drag To Complete

Use for booking, payment, upload, or confirmation.

- Provide a click or keyboard equivalent.
- Show progress while dragging.
- Complete at a clear threshold.
- Animate completion with a color/state change, then expose the final label.

### Marquee With Pause

Use for logo rows, galleries, or cards that can loop without becoming noise.

- Duplicate content for a seamless loop.
- Pause or slow on hover/focus so items can be inspected.
- Disable continuous movement for reduced-motion users.

### Elastic Divider

Use sparingly for editorial/contact surfaces.

- Use SVG path control points or CSS transform.
- Bend toward pointer movement.
- Return to center with an elastic ease.
- Keep it decorative and nonessential.

## React + GSAP Safety

- Use `useRef` for animated roots.
- Scope selectors with `gsap.context`.
- Clean up with `context.revert()`.
- Kill or overwrite tweens when repeated pointer events can stack.
- Keep dependencies explicit.
- Do not animate layout-critical dimensions unless the container is stable.
- Use `overwrite: true` for pointer-following tweens.
- Reset transformed elements on pointer leave, blur, unmount, and reduced-motion changes.
- Keep animated selectors scoped to the component root to avoid cross-component collisions.

## Bug Traps

- Hover animation changes width/height and pushes siblings.
- A loop keeps running after unmount.
- Reduced-motion disables animation but leaves content hidden at opacity `0`.
- Pointer math assumes the element never moves.
- Touch devices require hover to reveal important content.
- Scroll-triggered reveals hide content when JavaScript fails.

## Reduced Motion

For `prefers-reduced-motion`, keep:

- Static visible content.
- Immediate state changes.
- Focus styles.
- Final positions without looping or pointer chasing.

Do not remove important information just because animation is disabled.
