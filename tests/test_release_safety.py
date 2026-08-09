from __future__ import annotations

from pathlib import Path

import release_scan
from release_scan import scan_release_tree

from conftest import SKILL_ROOT, run_cli


def test_public_release_scan_blocks_private_material_and_generated_artifacts() -> None:
    assert scan_release_tree() == []


def test_skill_entry_points_are_installation_relative() -> None:
    private_root = "/" + "Users" + "/"
    assert private_root not in (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    for module in ("scripts.validate", "scripts.format_thesis"):
        result = run_cli(module, "--help")
        assert result.returncode == 0, result.stderr


def test_release_scan_rejects_synthetic_private_leak(tmp_path: Path) -> None:
    marker = SKILL_ROOT / "references" / "release-scan-synthetic.md"
    marker.parent.mkdir(exist_ok=True)
    private_root = "/" + "Users" + "/fixture"
    synthetic_identifier = "2024" + "12345678"
    marker.write_text(private_root + "\n" + synthetic_identifier, encoding="utf-8")
    try:
        violations = scan_release_tree()
        assert any("home-directory path" in violation for violation in violations)
        assert any("student-number-like sequence" in violation for violation in violations)
    finally:
        marker.unlink()


def test_release_scan_rejects_synthetic_symlink(tmp_path: Path) -> None:
    marker = SKILL_ROOT / "references" / "release-scan-synthetic-link"
    marker.symlink_to(tmp_path / "missing-target")
    try:
        assert any("symlink not permitted" in violation for violation in scan_release_tree())
    finally:
        marker.unlink()


def test_release_scan_rejects_private_filename() -> None:
    marker = SKILL_ROOT / "references" / ("jason" + "lee-private.md")
    marker.write_text("synthetic", encoding="utf-8")
    try:
        assert any("in filename" in violation for violation in scan_release_tree())
    finally:
        marker.unlink()


def test_release_scan_rejects_force_added_private_root(monkeypatch) -> None:
    marker = SKILL_ROOT.parent / ".work" / "synthetic-private.txt"
    marker.parent.mkdir(exist_ok=True)
    marker.write_text("synthetic", encoding="utf-8")
    monkeypatch.setattr(release_scan, "release_files", lambda: [marker])
    try:
        assert scan_release_tree() == ["private root not permitted: .work/synthetic-private.txt"]
    finally:
        marker.unlink()
