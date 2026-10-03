"""Regression checks for the public curriculum navigation and readiness claims."""

from pathlib import Path
import sys
import tempfile
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "tools"))

from check_course_integrity import (  # noqa: E402
    check_internal_markdown_links,
    check_ready_to_assign_modules,
    validate_repository,
)


class CourseIntegrityTests(unittest.TestCase):
    def test_public_curriculum_navigation_and_readiness_claims_are_consistent(self):
        """Learners should not encounter a broken internal route or an incomplete ready claim."""
        findings = validate_repository(REPOSITORY_ROOT)
        self.assertEqual(findings, [])

    def test_reports_a_missing_relative_markdown_target(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "README.md").write_text("[Missing](missing.md)\n", encoding="utf-8")

            findings = check_internal_markdown_links(root)

        self.assertEqual(findings, ["README.md:1: missing internal link target: missing.md"])

    def test_allows_external_links_without_network_access(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "README.md").write_text("[Reference](https://example.com/resource)\n", encoding="utf-8")

            findings = check_internal_markdown_links(root)

        self.assertEqual(findings, [])

    def test_ready_to_assign_claim_requires_a_current_assignment_file(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            module = root / "module"
            module.mkdir()
            (root / "MODULE_STATUS.md").write_text(
                "| [Example](module/) | Foundations | 1 week | CPU | Ready to assign | Use now |\n",
                encoding="utf-8",
            )

            findings = check_ready_to_assign_modules(root)

        self.assertEqual(
            findings,
            ["MODULE_STATUS.md:1: ready-to-assign module lacks a current assignment file"],
        )

    def test_ready_to_assign_claim_accepts_a_current_assignment_file(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            module = root / "module"
            module.mkdir()
            (module / "ASSIGNMENT.md").write_text("# Assignment\n", encoding="utf-8")
            (root / "MODULE_STATUS.md").write_text(
                "| [Example](module/) | Foundations | 1 week | CPU | Ready to assign | Use now |\n",
                encoding="utf-8",
            )

            findings = check_ready_to_assign_modules(root)

        self.assertEqual(findings, [])
