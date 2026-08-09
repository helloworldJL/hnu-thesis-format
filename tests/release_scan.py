from __future__ import annotations

import re
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_ROOT_NAMES = {".codegraph", ".omo", ".private", ".work"}
TEXT_SUFFIXES = {"", ".cff", ".html", ".json", ".md", ".py", ".toml", ".txt", ".yaml", ".yml"}
FORBIDDEN_PATTERNS = (
    ("home-directory path", re.compile(r"/" + r"Users/", re.IGNORECASE)),
    ("local account name", re.compile(r"jason" + r"lee", re.IGNORECASE)),
    ("desktop path", re.compile(r"Desk" + r"top/", re.IGNORECASE)),
    ("student-number-like sequence", re.compile(r"(?<![A-Za-z0-9])\d{10,12}(?![A-Za-z0-9])")),
    (
        "private report text",
        re.compile(
            r"(?:student number\s*[:：]\s*\d+|begin private " + r"thesis|begin private " + r"report)",
            re.IGNORECASE,
        ),
    ),
)
FORBIDDEN_ARTIFACT_SUFFIXES = {
    ".bin",
    ".docm",
    ".docx",
    ".dotm",
    ".dotx",
    ".gif",
    ".heic",
    ".jpeg",
    ".jpg",
    ".pdf",
    ".png",
    ".pyc",
    ".pyo",
    ".tif",
    ".tiff",
    ".tmp",
    ".zip",
}


def release_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    files = []
    for raw_name in result.stdout.split(b"\0"):
        if not raw_name:
            continue
        path = ROOT / os.fsdecode(raw_name)
        files.append(path)
    return sorted(files)


def scan_release_tree() -> list[str]:
    violations: list[str] = []
    for path in release_files():
        relative = path.relative_to(ROOT)
        relative_text = relative.as_posix()
        if relative.parts[0] in FORBIDDEN_ROOT_NAMES:
            violations.append(f"private root not permitted: {relative}")
            continue
        for label, pattern in FORBIDDEN_PATTERNS:
            if pattern.search(relative_text):
                violations.append(f"{label} in filename: {relative}")
        if path.is_symlink():
            violations.append(f"symlink not permitted: {relative}")
        elif not path.is_file():
            violations.append(f"non-regular artifact: {relative}")
        elif path.suffix.lower() in FORBIDDEN_ARTIFACT_SUFFIXES or "__pycache__" in path.parts:
            violations.append(f"generated artifact: {relative}")
        elif path.suffix.lower() in TEXT_SUFFIXES:
            content = path.read_text(encoding="utf-8")
            for label, pattern in FORBIDDEN_PATTERNS:
                if pattern.search(content):
                    violations.append(f"{label}: {relative}")
        else:
            violations.append(f"unreviewed artifact type: {relative}")
    return violations


def main() -> int:
    violations = scan_release_tree()
    if violations:
        print("Public release scan failed:")
        print("\n".join(violations))
        return 1
    print("Public release scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
