"""Regression checks for the public curriculum navigation and readiness claims."""

from pathlib import Path
import sys
import tempfile
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "tools"))

from check_course_integrity import (  # noqa: E402
    check_dataset_manifest,
    check_internal_markdown_links,
    check_ready_to_assign_modules,
    validate_repository,
)


class CourseIntegrityTests(unittest.TestCase):
    def test_dataset_manifest_requires_core_provenance_fields(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            manifest_directory = root / "course_data"
            manifest_directory.mkdir()
            (manifest_directory / "dataset_manifest.csv").write_text(
                "case_id,status,source_url,license,evidence_class\n"
                "coldplate,proposed,https://example.com,data-only,simulated\n",
                encoding="utf-8",
            )

            findings = check_dataset_manifest(root)

        self.assertEqual(
            findings,
            [
                "course_data/dataset_manifest.csv: missing required column: "
                "data_access"
            ],
        )

    def test_dataset_manifest_accepts_complete_course_data_record(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            manifest_directory = root / "course_data"
            manifest_directory.mkdir()
            (manifest_directory / "dataset_manifest.csv").write_text(
                "case_id,status,source_url,license,evidence_class,data_access\n"
                "coldplate,proposed,https://example.com,CC0-1.0,simulated,public\n",
                encoding="utf-8",
            )

            findings = check_dataset_manifest(root)

        self.assertEqual(findings, [])

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
