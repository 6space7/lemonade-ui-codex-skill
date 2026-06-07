#!/usr/bin/env python3
"""Lightweight smoke test for common Lemonade UI design failures."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


TEXT_EXTENSIONS = {
    ".css",
    ".html",
    ".js",
    ".jsx",
    ".mdx",
    ".svelte",
    ".ts",
    ".tsx",
    ".vue",
}

SKIP_PARTS = {
    ".git",
    ".next",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
}


@dataclass(frozen=True)
class Rule:
    code: str
    severity: str
    pattern: re.Pattern[str]
    message: str


def phrase(*parts: str) -> str:
    return "".join(parts)


SCREENSHOT_SPECIFIC_PATTERNS = [
    r"\b" + phrase("Map", "Harvest") + r"\b",
    r"\b" + phrase("map ", "search ", "scraper") + r"\b",
    r"\b" + phrase("profile-", "panel ", "scraper") + r"\b",
    r"\b" + phrase("Turn ", "map ", "searches ", "into ", "verified ", "business ", "data") + r"\b",
    r"\b" + phrase("Verified ", "leads ", "from ", "map ", "search") + r"\b",
    r"\b" + phrase("Scrape ", "maps") + r"\b",
]

VERTICAL_SPECIFIC_PATTERNS = [
    r"\b" + phrase("map/", "profile/", "export") + r"\b",
    r"\b" + phrase("map ", "search") + r"\b",
    r"\b" + phrase("opened ", "profile") + r"\b",
]

SAAS_HERO_WALLPAPER_PATTERNS = [
    r"\b" + phrase("mock ", "dashboard") + r"\b",
    r"\b" + phrase("dashboard ", "preview") + r"\b",
    r"\b" + phrase("analytics ", "dashboard") + r"\b",
    r"\b" + phrase("framed ", "app ", "preview") + r"\b",
    r"\b" + phrase("app ", "window") + r"\b",
    r"\b" + phrase("browser ", "chrome") + r"\b",
]

PLACEHOLDER_BRAND_PATTERNS = [
    r"\b" + phrase("your ", "logo") + r"\b",
    r"\b" + phrase("company ", "name") + r"\b",
    r"\b" + phrase("placeholder ", "brand") + r"\b",
    r"\b" + phrase("logo ", "here") + r"\b",
    r">\s*[A-Z]\s*</(?:span|div|button|a)>",
]

GENERIC_METRIC_PATTERNS = [
    r"\b" + phrase("demos ", "booked") + r"\b",
    r"\b" + phrase("tasks ", "scheduled") + r"\b",
    r"\b" + phrase("first-", "reply ", "average") + r"\b",
    r"\b" + phrase("time ", "saved") + r"\b",
    r"\b" + phrase("faster ", "workflow") + r"\b",
]

GENERIC_SPLIT_HERO_PATTERNS = [
    r"\b" + phrase("hero-", "copy") + r"\b",
    r"\b" + phrase("hero-", "mockup") + r"\b",
    r"\b" + phrase("split-", "hero") + r"\b",
    r"\b" + phrase("right-", "preview") + r"\b",
    r"\b" + phrase("left-", "content") + r"\b",
]


RULES = [
    Rule(
        "CAL001",
        "error",
        re.compile("|".join(SCREENSHOT_SPECIFIC_PATTERNS), re.I),
        "Screenshot-specific calibration language leaked into the skill or UI.",
    ),
    Rule(
        "CAL002",
        "warn",
        re.compile("|".join(VERTICAL_SPECIFIC_PATTERNS), re.I),
        "Avoid product-category-specific examples in general calibration guidance.",
    ),
    Rule(
        "AI001",
        "warn",
        re.compile(r"\b(orb|blob|bokeh|mesh gradient|gradient blob)\b", re.I),
        "Generic decorative blob/orb language often leads to AI-looking design.",
    ),
    Rule(
        "AI002",
        "warn",
        re.compile(r"\bAI-powered\b|\bpowered by AI\b", re.I),
        "Replace vague AI claims with concrete product actions, states, or proof.",
    ),
    Rule(
        "AI003",
        "warn",
        re.compile(r"\b(Analytics|Insights|Automation|Growth)\b"),
        "Generic dashboard labels are fine only when surrounded by domain-specific data.",
    ),
    Rule(
        "AI004",
        "warn",
        re.compile("|".join(SAAS_HERO_WALLPAPER_PATTERNS), re.I),
        "Decorative software previews need real task flow, selected state, or object-level proof.",
    ),
    Rule(
        "AI005",
        "warn",
        re.compile("|".join(PLACEHOLDER_BRAND_PATTERNS), re.I),
        "Placeholder identity weakens the design; create a small deliberate brand treatment.",
    ),
    Rule(
        "AI006",
        "warn",
        re.compile("|".join(GENERIC_METRIC_PATTERNS), re.I),
        "Metrics should connect to visible product state, not float as generic proof.",
    ),
    Rule(
        "AI007",
        "warn",
        re.compile("|".join(GENERIC_SPLIT_HERO_PATTERNS), re.I),
        "Default two-column hero structure needs a stronger composition move or earlier product proof.",
    ),
    Rule(
        "CNT001",
        "warn",
        re.compile(r"\b(seamless|powerful|supercharge|boost productivity|unlock|revolutionize)\b", re.I),
        "Generic marketing words need concrete product behavior or proof.",
    ),
    Rule(
        "CNT002",
        "warn",
        re.compile(r"\b(Get Started|Learn More|Features|Solutions)\b"),
        "Generic CTA/navigation copy is acceptable only when the surrounding product story is specific.",
    ),
    Rule(
        "CNT003",
        "warn",
        re.compile(r"<p[^>]*>[^<]{180,}</p>", re.I | re.S),
        "Long paragraph detected; compress copy or move proof into the UI.",
    ),
    Rule(
        "CMP001",
        "warn",
        re.compile(r"\bgrid-cols-3\b|\bmd:grid-cols-3\b|\blg:grid-cols-3\b"),
        "Three-column grids are common AI defaults; verify the section rhythm is not generic card soup.",
    ),
    Rule(
        "TYP001",
        "warn",
        re.compile(r"\btext-(?:7xl|8xl|9xl)\b|text-\[[^\]]*(?:5rem|6rem|7rem|8rem|9rem)[^\]]*\]", re.I),
        "Huge type detected; verify it is not overpowering product evidence, especially on mobile.",
    ),
    Rule(
        "LAY001",
        "error",
        re.compile(r"tracking-\[?-|letter-spacing\s*:\s*-", re.I),
        "Negative letter spacing is fragile and often looks cramped.",
    ),
    Rule(
        "LAY002",
        "warn",
        re.compile(r"text-\[[^\]]*(?:vw|svw|dvw|lvw)[^\]]*\]|font-size\s*:[^;]*(?:vw|svw|dvw|lvw)", re.I),
        "Viewport-width font sizing often breaks at extreme widths.",
    ),
    Rule(
        "LAY003",
        "warn",
        re.compile(r"rounded-(?:2xl|3xl|full)|rounded-\[[^\]]*(?:2rem|3rem|999)", re.I),
        "Large radii can look AI-ish when overused; make sure the shape has a reason.",
    ),
    Rule(
        "MOT001",
        "error",
        re.compile(r"\b(?:gsap|framer-motion|motion\.)\b", re.I),
        "Motion code detected; verify cleanup and reduced-motion behavior.",
    ),
    Rule(
        "A11Y001",
        "warn",
        re.compile(r"<button(?:(?!aria-label|aria-labelledby).)*>\s*<(?:[A-Z][A-Za-z0-9]*|svg)\b", re.S),
        "Icon-only buttons need accessible names.",
    ),
]


def iter_files(root: Path):
    if root.is_file():
        if root.suffix in TEXT_EXTENSIONS:
            yield root
        return

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_EXTENSIONS:
            continue
        if SKIP_PARTS.intersection(path.parts):
            continue
        yield path


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def audit(root: Path) -> int:
    findings: list[tuple[str, str, Path, int, str]] = []

    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for rule in RULES:
            for match in rule.pattern.finditer(text):
                findings.append((rule.severity, rule.code, path, line_number(text, match.start()), rule.message))

    for severity, code, path, line, message in findings:
        print(f"{severity.upper()} {code} {path}:{line} {message}")

    errors = sum(1 for severity, *_ in findings if severity == "error")
    warnings = len(findings) - errors

    if findings:
        print(f"\nFound {errors} error(s), {warnings} warning(s). Fix errors; inspect warnings with design judgment.")
    else:
        print("No Lemonade design smoke-test findings.")

    return 1 if errors else 0


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: audit_lemonade_design.py <file-or-directory>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).expanduser().resolve()
    if not root.exists():
        print(f"Path not found: {root}", file=sys.stderr)
        return 2

    return audit(root)


if __name__ == "__main__":
    raise SystemExit(main())
