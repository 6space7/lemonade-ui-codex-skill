# Lemonade UI Codex Skill

A Codex skill for designing and building modern, animated, tactile websites and frontend components with Lemonade UI taste.

Lemonade UI is for frontend work that should feel alive without becoming noisy: polished landing pages, product surfaces, animated shadcn-style components, SaaS sites, dashboards, portfolios, and premium UI redesigns.

## What It Helps Codex Do

- Design from a real product moment instead of a generic template.
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
  references/anti-ai-slop.md
  references/copy-compression.md
  references/design-spine.md
  references/design-language.md
  references/motion-recipes.md
  references/product-evidence.md
  references/responsive-composition.md
  references/review-checklist.md
  references/visual-hierarchy.md
```

## Skill Design

The main `SKILL.md` is a router so it can load quickly. Detailed guidance is split into small one-purpose references:

- `anti-ai-slop.md` catches generic AI/template aesthetics.
- `copy-compression.md` keeps pages from over-yapping.
- `design-language.md` covers taste, layout, page archetypes, palette, and mistakes to avoid.
- `design-spine.md` forces the core design decisions before motion.
- `motion-recipes.md` covers GSAP/CSS/React interaction patterns and reduced-motion safety.
- `product-evidence.md` helps turn vague claims into visible product proof.
- `responsive-composition.md` handles mobile/desktop composition strategy.
- `review-checklist.md` is the final quality gate before shipping frontend work.
- `visual-hierarchy.md` covers type, spacing, material, and first-read clarity.
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
