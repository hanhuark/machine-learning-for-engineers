"""Check public curriculum routes and readiness claims without network access.

This check is deliberately lightweight.  It verifies links that learners can
follow inside the repository and guards one instructor-facing promise: a
module marked "Ready to assign" must include a current assignment file.
It does not evaluate external URLs, execute notebooks, or judge the
scientific validity of an activity.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
MODULE_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data"}
ASSIGNMENT_FILENAMES = {"ASSIGNMENT.md", "ASSIGNMENT_AI_RESILIENT.md"}


def iter_markdown_files(repository_root: Path) -> list[Path]:
    """Return public Markdown files in deterministic order."""
    return sorted(
        path
        for path in repository_root.rglob("*.md")
        if ".git" not in path.parts and ".pytest_cache" not in path.parts
    )


def is_internal_link(target: str) -> bool:
    """Return whether a Markdown target should resolve within the repository."""
    if not target or target.startswith("#"):
        return False
    parsed = urlsplit(target)
    return parsed.scheme.lower() not in EXTERNAL_SCHEMES and not target.startswith("//")


def resolve_internal_link(source: Path, target: str) -> Path:
    """Resolve the path component of a relative Markdown target."""
    path_text = unquote(urlsplit(target).path).strip("<>")
    return (source.parent / path_text).resolve()


def check_internal_markdown_links(repository_root: Path) -> list[str]:
    """Report broken repository-relative Markdown links with source locations."""
    findings: list[str] = []
    root = repository_root.resolve()

    for markdown_file in iter_markdown_files(root):
        for line_number, line in enumerate(markdown_file.read_text(encoding="utf-8").splitlines(), start=1):
            for match in MARKDOWN_LINK.finditer(line):
                target = match.group(1)
                if not is_internal_link(target):
                    continue
                resolved = resolve_internal_link(markdown_file, target)
                try:
                    resolved.relative_to(root)
                except ValueError:
                    findings.append(
                        f"{markdown_file.relative_to(root)}:{line_number}: "
                        f"internal link leaves repository: {target}"
                    )
                    continue
                if not resolved.exists():
                    findings.append(
                        f"{markdown_file.relative_to(root)}:{line_number}: "
                        f"missing internal link target: {target}"
                    )
    return findings


def check_ready_to_assign_modules(repository_root: Path) -> list[str]:
    """Ensure each module advertised as ready to assign has a current assignment."""
    status_file = repository_root / "MODULE_STATUS.md"
    findings: list[str] = []
    if not status_file.exists():
        return ["MODULE_STATUS.md: missing module-status file"]

    for line_number, line in enumerate(status_file.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.startswith("|") or "Ready to assign" not in line:
            continue
        module_match = MODULE_LINK.search(line)
        if module_match is None:
            findings.append(f"MODULE_STATUS.md:{line_number}: ready-to-assign row has no module link")
            continue
        module_path = resolve_internal_link(status_file, module_match.group(1))
        if not module_path.is_dir():
            findings.append(
                f"MODULE_STATUS.md:{line_number}: ready-to-assign module path is not a directory: "
                f"{module_match.group(1)}"
            )
            continue
        if not any((module_path / filename).is_file() for filename in ASSIGNMENT_FILENAMES):
            findings.append(
                f"MODULE_STATUS.md:{line_number}: ready-to-assign module lacks a current assignment file"
            )
    return findings


def validate_repository(repository_root: Path) -> list[str]:
    """Return all offline curriculum-integrity findings in deterministic order."""
    root = repository_root.resolve()
    return check_internal_markdown_links(root) + check_ready_to_assign_modules(root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root to validate (default: repository containing this script)",
    )
    arguments = parser.parse_args()
    findings = validate_repository(arguments.root)
    if findings:
        print("Course integrity check failed:")
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    print("Course integrity check passed: public internal links and ready-to-assign claims are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
