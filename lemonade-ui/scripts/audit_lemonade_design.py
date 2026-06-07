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


RULES = [
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
