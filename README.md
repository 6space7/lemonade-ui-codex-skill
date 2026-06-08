# Lemonade UI Codex Skill

A Codex skill for designing and building modern, animated, tactile websites and frontend components with Lemonade UI taste.

Lemonade UI is for frontend work that should feel alive without becoming noisy: polished landing pages, product surfaces, animated shadcn-style components, SaaS sites, dashboards, portfolios, and premium UI redesigns.

## What It Helps Codex Do

- Create a mandatory design contract before open-ended frontend coding.
- Force spacing rhythm and interaction briefs instead of eyeballed gaps and decorative motion.
- Default vague SaaS/CRM heroes away from dashboard/app-window mockups.
- Prevent no-dashboard overcorrection into noisy poster-collage concepts.
- Design from a real product moment instead of a generic template.
- Apply Lemonade visual DNA: cinematic contrast, shaped frames, layered product objects, and a memorable visual idea.
- Use concrete composition recipes instead of vague "modern premium" adjectives.
- Calibrate from screenshots and moodboards by extracting structure, crop, contrast, object treatment, and mobile lessons.
- Escape the default SaaS hero stack before coding.
- Choose product artifacts, workflows, selected objects, or operational surfaces instead of decorative app previews.
- Create a design spine before coding: product evidence, layout, type, material, content rhythm, and interaction budget.
- Build first viewports that clearly show the product, object, workflow, or place.
- Build a memorable visual idea that can come from composition, product UI, media, typography, material, or interaction.
- Keep motion accessible with reduced-motion behavior.
- Avoid common AI design traps like nested cards, decorative blobs, vague gradients, and components that only work with short demo copy.
- Verify responsive layout, text fit, contrast, interaction states, and build quality before calling work complete.
- Run a small audit script that flags common AI-ish and buggy frontend patterns.

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R lemonade-ui ~/.codex/skills/lemonade-ui
```

Restart Codex or reload skills if your environment requires it.

## Use

Invoke it explicitly:

```text
Use $lemonade-ui to design and build a modern animated landing page for my SaaS product.
```

For best results, expect Codex to create a short design contract before coding:

```text
Design contract:
Moment: ...
Artifact: ...
Dashboard/app screen: ...
Composition: ...
Composition discipline: ...
DNA move: ...
Mobile proof: ...
Spacing: ...
Copy budget: ...
Interaction: ...
Avoiding: ...
```

Or ask for work that naturally matches the skill:

```text
Make this website feel more premium and animated, like a Lemonade UI component.
```

```text
Build a tactile shadcn-style pricing section with one polished interaction.
```

```text
Redesign this dashboard so it feels modern but still useful for operators.
```

## Repo Layout

```text
lemonade-ui/
  SKILL.md
  agents/openai.yaml
  scripts/audit_lemonade_design.py
  references/design-contract.md
  references/anti-ai-slop.md
  references/calibration-operational-ui.md
  references/calibration-overcopy-and-scale.md
  references/calibration-product-proof.md
  references/calibration-responsive-composition.md
  references/composition-discipline.md
  references/copy-compression.md
  references/design-spine.md
  references/design-language.md
  references/interaction-quality.md
  references/lemonade-visual-dna.md
  references/motion-recipes.md
  references/no-dashboard-proof.md
  references/product-artifact-selection.md
  references/product-evidence.md
  references/responsive-composition.md
  references/review-checklist.md
  references/saas-hero-escape-system.md
  references/spacing-and-rhythm.md
  references/visual-reference-calibration.md
  references/visual-hierarchy.md
  references/recipes/artifact-collage.md
  references/recipes/dark-product-theatre.md
  references/recipes/editorial-product-story.md
  references/recipes/operational-work-surface.md
  references/recipes/shaped-poster-frame.md
```

## Skill Design

The main `SKILL.md` is a fast router with a hard design-contract gate. Detailed guidance is split into small one-purpose references:

- `anti-ai-slop.md` catches generic AI/template aesthetics.
- `calibration-overcopy-and-scale.md` fixes huge type, yapping, and weak copy rhythm.
- `calibration-product-proof.md` moves vague claims into credible visible product evidence.
- `calibration-responsive-composition.md` prevents desktop-to-mobile stacking mistakes.
- `composition-discipline.md` keeps bold no-dashboard art direction legible, restrained, and product-plausible.
- `calibration-operational-ui.md` keeps dashboards and tools dense, useful, and calm.
- `copy-compression.md` keeps pages from over-yapping.
- `design-contract.md` forces product moment, artifact, composition, DNA move, mobile proof, spacing, copy budget, interaction, and avoided default before coding.
- `design-language.md` covers taste, layout, page archetypes, palette, and mistakes to avoid.
- `design-spine.md` forces the core design decisions before motion.
- `interaction-quality.md` forces a motion brief and stateful interaction rules before adding animation.
- `lemonade-visual-dna.md` captures the positive Lemonade look: cinematic stages, shaped frames, layered objects, strong material, and deliberate type.
- `motion-recipes.md` covers GSAP/CSS/React interaction patterns and reduced-motion safety.
- `no-dashboard-proof.md` keeps vague landing heroes from becoming dashboard or app-window mockups.
- `product-artifact-selection.md` chooses the right visible artifact before product proof is designed.
- `product-evidence.md` helps turn vague claims into visible product proof.
- `responsive-composition.md` handles mobile/desktop composition strategy.
- `review-checklist.md` is the final quality gate before shipping frontend work.
- `saas-hero-escape-system.md` breaks the generic SaaS hero pattern.
- `spacing-and-rhythm.md` defines page rhythm, section padding, container widths, component gaps, control sizes, and spacing review.
- `visual-reference-calibration.md` turns screenshots and moodboards into reusable visual decisions without copying a single product.
- `visual-hierarchy.md` covers type, spacing, material, and first-read clarity.
- `references/recipes/` contains executable composition recipes: dark product theatre, shaped poster frame, artifact collage, editorial product story, and operational work surface.
- `scripts/audit_lemonade_design.py` is a lightweight smoke test for common design and interaction traps.

## Audit A Local Frontend

```bash
python3 lemonade-ui/scripts/audit_lemonade_design.py /path/to/frontend
```

The audit catches obvious problems only. It does not replace browser screenshots, mobile checks, or taste judgment.

## Suggested GitHub Description

```text
Codex skill for Lemonade UI-style modern, animated, tactile website and frontend design.
```

## Validate

From a machine with the Codex skill creator validator available:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py lemonade-ui
```
