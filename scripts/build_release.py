#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import re
import shutil
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skill-optimizer"
DIST_DIR = ROOT / "dist"
VERSION_FILE = ROOT / "VERSION"

REQUIRED_FILES = [
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "agents" / "openai.yaml",
    SKILL_DIR / "references" / "report-schema.md",
    SKILL_DIR / "evals" / "evals.json",
]


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def load_version() -> str:
    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    ensure(bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), f"Invalid VERSION: {version}")
    return version


def validate_skill() -> None:
    for path in REQUIRED_FILES:
        ensure(path.exists(), f"Missing required file: {path}")

    content = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    ensure(content.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
    ensure("name: skill-optimizer" in content, "SKILL.md must define name: skill-optimizer")
    ensure("description:" in content, "SKILL.md must define a description")


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def make_claude_variant(src_dir: Path) -> None:
    skill_md = src_dir / "SKILL.md"
    claude_md = src_dir / "Skill.md"
    ensure(skill_md.exists(), f"Missing source skill file: {skill_md}")
    temp_md = src_dir / "__skill_tmp__.md"
    skill_md.rename(temp_md)
    temp_md.rename(claude_md)


def zip_dir(source_dir: Path, zip_path: Path) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as zf:
        for file_path in sorted(source_dir.rglob("*")):
            if file_path.is_dir():
                continue
            arcname = file_path.relative_to(source_dir)
            zf.write(file_path, arcname.as_posix())


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build() -> None:
    validate_skill()
    version = load_version()

    staging = DIST_DIR / "staging"
    clawhub_stage = staging / "clawhub"
    claude_stage = staging / "claude"
    reset_dir(staging)

    clawhub_root = clawhub_stage / "skill-optimizer"
    claude_root = claude_stage / "skill-optimizer"
    copy_tree(SKILL_DIR, clawhub_root)
    copy_tree(SKILL_DIR, claude_root)
    make_claude_variant(claude_root)

    clawhub_zip = DIST_DIR / "clawhub" / f"skill-optimizer-v{version}-clawhub.zip"
    claude_zip = DIST_DIR / "claude" / f"skill-optimizer-v{version}-claude.zip"
    zip_dir(clawhub_stage, clawhub_zip)
    zip_dir(claude_stage, claude_zip)

    print(f"Built: {clawhub_zip}")
    print(f"SHA256: {sha256(clawhub_zip)}")
    print(f"Built: {claude_zip}")
    print(f"SHA256: {sha256(claude_zip)}")


if __name__ == "__main__":
    try:
        build()
    except SystemExit:
        raise
    except Exception as exc:  # pragma: no cover
        raise SystemExit(f"Build failed: {exc}") from exc
