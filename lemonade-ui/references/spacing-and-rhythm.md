# Spacing And Rhythm

Use this before coding layout and again during browser review. Good Lemonade UI should feel intentionally spaced, not eyeballed.

## Rhythm Contract

For open-ended frontend work, add spacing to the design contract:

```text
Spacing: page shell ..., section padding ..., container max ..., grid gap ..., component padding ..., control height ...
```

If you cannot state the spacing system, do not start sprinkling random gaps.

## Spacing Scale

Use a small scale and repeat it with intent:

- **4px:** hairline offsets, icon nudges, dense control interiors.
- **8px:** micro gaps, icon-label gaps, status chip interiors.
- **12px:** compact form/control gaps.
- **16px:** default component padding and tight groups.
- **24px:** card/work-surface padding and related group gaps.
- **32px:** section groups, hero copy stacks, artifact gutters.
- **48px:** major desktop group separation.
- **64px:** compact section padding.
- **96px:** roomy desktop section padding.
- **128px:** only for large editorial or poster stages.

Avoid making every level use the same gap. The page needs hierarchy: outer breath > section rhythm > group rhythm > component rhythm > micro rhythm.

## Page Rhythm

- Use a real container max width; do not let content drift across the whole viewport.
- Align hero copy and artifact on a shared axis unless the composition intentionally breaks it.
- Keep the first viewport composed; avoid giant top/bottom gaps that make the artifact feel lost.
- Let landing heroes hint at the next section without forcing the hero to become a full empty screen.
- Make one vertical rhythm decision per section: compact utility, poster stage, editorial breath, or dense work surface.

## Component Rhythm

- Buttons: usually 44-52px tall; icon-only buttons should be square.
- Compact chips: 28-36px tall.
- Table/list rows: 44-64px depending on density.
- Cards/panels: 16-24px internal padding for normal UI; 32px only for hero surfaces.
- Product artifacts: reserve space for selected, hover, loading, and expanded states.
- Text stacks: headline to body gap should usually be smaller than body to CTA/artifact gap.

## Desktop

- Use wide space to create contrast, not emptiness.
- If copy and artifact sit side by side, make one visibly dominant.
- Large artifacts need tighter surrounding copy; large copy needs a lighter artifact or stronger crop.
- Repeated cards need different internal density from the hero, or the page becomes card soup.

## Mobile

- Page side padding: usually 16-24px.
- Section padding: usually 48-72px vertical unless the hero needs a tighter first viewport.
- Group gaps: usually 16-24px.
- Avoid stacked CTA buttons that consume the first viewport.
- Move or crop proof before increasing vertical gaps.
- If mobile feels too tall, reduce copy, secondary controls, and decorative fragments before shrinking the artifact into illegibility.

## Spacing Review

Check screenshots for:

- One obvious first read.
- No equal-gap monotony.
- No accidental dead zones.
- No cramped control clusters.
- No text touching borders, icons, or adjacent content.
- No hover/selected state that changes surrounding layout.
- No mobile first viewport consumed by whitespace, nav, copy, and CTAs before proof.

If spacing feels wrong, fix rhythm before adding shadow, blur, glow, or motion.
