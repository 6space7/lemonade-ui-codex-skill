# Interaction Quality

Use this before adding animation or interactive polish. Lemonade interaction should feel stateful, tactile, and useful, not like motion sprinkled over a static template.

## Motion Brief

For any non-trivial animation, write a short motion brief before coding:

```text
Motion brief:
Role: ...
Trigger: ...
Target: ...
State change: ...
Bounds: ...
Duration/ease: ...
Reset: ...
Reduced motion: ...
```

If the motion has no role, remove it.

## Motion Roles

Use motion for one of these jobs:

- **Feedback:** press, hover, focus, selected, success, error, loading.
- **Reveal:** make hierarchy or newly available content clear.
- **Continuity:** connect list/detail, input/output, before/after, open/close.
- **Manipulation:** drag, scrub, reorder, resize, configure.
- **State proof:** show a product action completing or changing status.
- **Navigation:** help the user understand where they moved.

Avoid motion whose only job is "make it modern."

## Timing

- Press/hover feedback: 90-180ms.
- Small state changes: 160-260ms.
- Panel open/close: 220-380ms.
- Entrance reveal: 450-800ms with small stagger.
- Signature hero motion: one restrained loop or pointer response, not many.

Use easing that settles cleanly. Avoid long bouncy motion for serious SaaS, dashboards, finance, health, admin, or operational tools.

## Bounds

- Hover translation: usually 2-8px.
- Magnetic buttons: usually 6-12px max.
- Card lift: usually 2-6px plus shadow/contrast change.
- Scale: avoid above 1.03 for UI surfaces unless the container reserves space.
- Blur: keep low enough that text remains readable during the transition.
- Parallax: should not move content so far that alignment looks broken.

## Tactile Controls

Controls should have at least:

- Default, hover, focus-visible, active, disabled where applicable.
- Click or keyboard alternative for pointer-only behavior.
- Stable dimensions across states.
- Clear selected/current state.
- Loading or pending state when an action implies waiting.

Icon-only controls need accessible names.

## Product Interactions

Prefer interactions that reveal product behavior:

- Selecting a row updates a detail pane.
- Dragging a slider changes an output preview.
- Approving a draft changes status and exposes the next step.
- Scrubbing a timeline changes a frame or transcript state.
- Toggling a filter changes visible rows and count.
- Hovering a file/card reveals metadata, not decoration only.

## Reduced Motion

For `prefers-reduced-motion`:

- Keep content visible.
- Skip entrance hiding.
- Replace loops and pointer chasing with static final states.
- Keep focus, selected, active, and success states.

Reduced motion should still look designed.

## Bug Traps

- `transition-all` animates properties you did not intend.
- Hover scale or translate changes the perceived layout and causes overlap.
- Repeated pointer events stack tweens.
- Touch users cannot reveal important hover content.
- Scroll reveals leave content hidden when JavaScript fails.
- Animation starts before fonts/images/product artifacts are stable.
- Motion hides spacing problems instead of fixing them.

## Interaction Review

Before shipping:

- Test hover, focus, active, selected, disabled, loading, and reduced motion.
- Replay repeated pointer movement quickly.
- Check desktop and mobile screenshots before and after interaction.
- Confirm no layout shift around animated elements.
- Confirm the static design still works with motion disabled.
