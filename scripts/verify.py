"""Verify this development blueprint and its example contracts; never deploy anything."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    raise SystemExit(
        "Install the verification dependencies first: "
        "python -m pip install --require-hashes -r requirements-dev.lock"
    ) from None

ROOT = Path(__file__).resolve().parents[1]


def load(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def verify() -> None:
    manifest = load("project.json")
    series = load("series.json")
    assert manifest["status"] == "blueprint", "Update status checks when implementation starts"
    assert manifest["series"]["name"] == "qez Development Lab Series"
    assert manifest["series"]["total"] == len(series["projects"]) == 18
    names = [p["repo"] for p in series["projects"]]
    assert len(set(names)) == 18, "Duplicate series repository"
    entry = next(p for p in series["projects"] if p["repo"] == manifest["repository"])
    assert entry["number"] == manifest["series"]["number"]
    assert manifest["cloud_deployed"] is False
    assert len(manifest["stack"]) >= 3
    assert len(manifest["labs"]) == 5
    assert len(manifest["certifications"]) >= 1

    for name in ["README.md", "SERIES.md", "docs/STACK.md", "docs/ARCHITECTURE.md",
                 "docs/CERTIFICATIONS.md", "docs/LABS.md", "docs/ROADMAP.md",
                 "docs/SECURITY.md", "docs/COST-AND-CLEANUP.md", "docs/RUNBOOK.md",
                 "docs/LOCAL-DEVELOPMENT.md", "docs/REFERENCES.md", "docs/CONTRACTS.md",
                 "CONTRIBUTING.md", ".github/workflows/verify.yml"]:
        assert (ROOT / name).is_file(), f"Missing {name}"

    # Check local Markdown file links without requesting external URLs.
    link_count = 0
    for file in ROOT.rglob("*.md"):
        if any(p in {".git", ".venv", "node_modules"} for p in file.relative_to(ROOT).parts):
            continue
        content = file.read_text(encoding="utf-8")
        for raw in re.findall(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", content):
            target = raw.strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            path = unquote(target.split("#", 1)[0])
            if not path:
                continue
            resolved = (file.parent / path).resolve()
            assert resolved.is_relative_to(ROOT), f"Link leaves repository: {file}: {raw}"
            assert resolved.exists(), f"Broken local link: {file.relative_to(ROOT)}: {raw}"
            link_count += 1

    # Parse all checked-in JSON, including invalid *domain* fixtures (valid JSON).
    json_count = 0
    for folder in [ROOT, ROOT / "contracts", ROOT / "examples"]:
        for file in folder.glob("*.json"):
            json.loads(file.read_text(encoding="utf-8"))
            json_count += 1

    schema = load("contracts/record.schema.json")
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    validator.validate(load("examples/record.valid.json"))
    for name in ["examples/record.missing-field.json", "examples/record.wrong-type.json"]:
        assert list(validator.iter_errors(load(name))), f"Negative fixture unexpectedly passes: {name}"

    # These are deterministic, network-free repository checks, not product tests.
    print(f"PASS {manifest['repository']}: series identity, {link_count} local links, "
          f"{json_count} JSON files, schema, one valid and two invalid fixtures")
    print("Application behavior and live AWS integration remain unimplemented and untested.")


if __name__ == "__main__":
    try:
        verify()
    except (AssertionError, KeyError, ValueError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1) from error
