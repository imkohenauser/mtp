#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import zipfile
from argparse import ArgumentParser, Namespace
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
PUBLIC_DOWNLOADS_DIR = ROOT / "public" / "downloads"
RELEASE_ASSETS_DIR = ROOT / "dist" / "release-assets"

REPOSITORY = "https://github.com/imkohenauser/mtp"
DEFAULT_SKILL = "mtp"
DEFAULT_FAMILY = "v1"


def parse_args() -> Namespace:
    parser = ArgumentParser(
        description="Build a packaged Agent Skill zip and release metadata."
    )
    parser.add_argument(
        "--skill",
        default=DEFAULT_SKILL,
        help="Skill directory name under skills/.",
    )
    parser.add_argument(
        "--family",
        default=DEFAULT_FAMILY,
        help="Repository-level major family label, such as v1.",
    )
    return parser.parse_args()


def validate_skill_name(skill: str) -> None:
    if not re.match(r"^[a-z0-9][a-z0-9-]*$", skill):
        raise RuntimeError(
            f"Invalid skill '{skill}'. Expected a directory name such as mtp"
        )


def display_name(skill: str) -> str:
    words = ["MTP" if part == "mtp" else part.capitalize() for part in skill.split("-")]
    return f"{' '.join(words)} Skill"


def read_skill_version(skill_file: Path) -> str:
    text = skill_file.read_text(encoding="utf-8")

    if not text.startswith("---"):
        raise RuntimeError(f"{skill_file} does not start with frontmatter")

    match = re.search(
        r"^---\s*\n(?P<frontmatter>.*?)\n---\s*\n",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise RuntimeError(f"Could not parse frontmatter in {skill_file}")

    frontmatter = match.group("frontmatter")

    version_match = re.search(
        r'^version:\s*["\']?([^"\']+)["\']?\s*$',
        frontmatter,
        flags=re.MULTILINE,
    )
    if not version_match:
        raise RuntimeError(f"Could not find version in {skill_file}")

    version = version_match.group(1).strip()

    if not re.match(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$", version):
        raise RuntimeError(
            f"Invalid version '{version}'. Expected semver-like value such as 1.0.0"
        )

    return version


def list_tracked_skill_files(skill_dir: Path) -> list[Path]:
    rel_skill_dir = skill_dir.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", rel_skill_dir],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    files = [
        ROOT / path.decode("utf-8")
        for path in result.stdout.split(b"\0")
        if path
    ]
    return sorted(path for path in files if path.is_file())


def build_zip(
    skill: str,
    skill_dir: Path,
    tracked_files: list[Path],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.exists():
        output_path.unlink()

    # The zip intentionally contains the skill directory as the top-level folder.
    # This preserves the distribution unit as skills/<skill> while avoiding the
    # repository-specific parent path.
    with zipfile.ZipFile(output_path, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in tracked_files:
            arcname = Path(skill) / file_path.relative_to(skill_dir)
            zf.write(file_path, arcname.as_posix())


def release_metadata(skill: str, family: str, version: str) -> dict[str, str]:
    tag = f"{skill}-v{version}"

    return {
        "skill": skill,
        "name": display_name(skill),
        "family": family,
        "version": version,
        "tag": tag,
        "source": f"skills/{skill}",
        "versionSource": f"skills/{skill}/SKILL.md",
        "zip": f"/downloads/{skill}-skill.zip",
        "release": f"{REPOSITORY}/releases/tag/{tag}",
        "repository": REPOSITORY,
        "updatedAt": datetime.now(timezone.utc).isoformat(),
    }


def write_json(path: Path, data: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    skill = args.skill
    family = args.family

    validate_skill_name(skill)

    skill_dir = SKILLS_DIR / skill
    skill_file = skill_dir / "SKILL.md"

    if not skill_dir.exists():
        raise RuntimeError(f"Skill directory not found: {skill_dir}")

    if not skill_file.exists():
        raise RuntimeError(f"Skill file not found: {skill_file}")

    version = read_skill_version(skill_file)
    tracked_files = list_tracked_skill_files(skill_dir)

    if skill_file not in tracked_files:
        raise RuntimeError(f"Skill file is not tracked by git: {skill_file}")

    latest_zip = PUBLIC_DOWNLOADS_DIR / f"{skill}-skill.zip"
    versioned_zip = RELEASE_ASSETS_DIR / f"{skill}-skill-v{version}.zip"
    skill_release_json = PUBLIC_DOWNLOADS_DIR / f"{skill}-release.json"

    build_zip(skill, skill_dir, tracked_files, latest_zip)
    versioned_zip.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(latest_zip, versioned_zip)

    metadata = release_metadata(skill, family, version)
    write_json(skill_release_json, metadata)

    if skill == DEFAULT_SKILL:
        # release.json is the public default metadata endpoint for the primary
        # MTP Skill. Skill-specific metadata remains available as mtp-release.json.
        write_json(PUBLIC_DOWNLOADS_DIR / "release.json", metadata)

    print(version)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
