#!/usr/bin/env python3
"""Dependency-light semantic validator for a webbyLucifer project handoff."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

REQUIRED_HANDOFF_KEYS = {
    "schemaVersion", "handoffId", "producer", "executor", "status",
    "uiRevision", "uiCommit", "requiredInputs",
}
REQUIRED_LOCK_KEYS = {
    "schemaVersion", "skillVersion", "handoffId", "uiRevision", "uiCommit", "files",
}


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON: {path}: {exc}")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def collect_ids(items, key, label, errors):
    seen = set()
    for item in items:
        value = item.get(key)
        if not value:
            errors.append(f"{label} without {key}")
        elif value in seen:
            errors.append(f"duplicate {label} id: {value}")
        else:
            seen.add(value)
    return seen


def validate_project(root: Path) -> list[str]:
    errors: list[str] = []
    webby = root / ".webby"
    handoff_path = webby / "HANDOFF.json"
    lock_path = webby / "WEBBY_LOCK.json"

    try:
        handoff = load_json(handoff_path)
    except ValueError as exc:
        return [str(exc)]

    missing = REQUIRED_HANDOFF_KEYS - set(handoff)
    if missing:
        errors.append(f"HANDOFF missing keys: {sorted(missing)}")

    if handoff.get("status") == "UI_SETUP_COMPLETE":
        if handoff.get("producer") != "CHATGPT":
            errors.append("UI_SETUP_COMPLETE handoff producer must be CHATGPT")
        if not handoff.get("uiCommit"):
            errors.append("UI_SETUP_COMPLETE requires uiCommit")

    for rel in handoff.get("requiredInputs", []):
        if not (root / rel).exists():
            errors.append(f"required input does not exist: {rel}")

    claude_pack = handoff.get("claudePack")
    if handoff.get("status") == "UI_SETUP_COMPLETE" and claude_pack:
        pack_root = root / claude_pack
        if not pack_root.exists():
            errors.append(f"Claude pack does not exist: {claude_pack}")

    try:
        lock = load_json(lock_path)
    except ValueError as exc:
        errors.append(str(exc))
        return errors

    missing = REQUIRED_LOCK_KEYS - set(lock)
    if missing:
        errors.append(f"WEBBY_LOCK missing keys: {sorted(missing)}")

    for key in ("handoffId", "uiRevision", "uiCommit"):
        if handoff.get(key) != lock.get(key):
            errors.append(f"{key} mismatch between HANDOFF and WEBBY_LOCK")

    h_digest = handoff.get("contractDigest")
    l_digest = lock.get("contractDigest")
    if h_digest and l_digest and h_digest != l_digest:
        errors.append("contractDigest mismatch between HANDOFF and WEBBY_LOCK")

    for entry in lock.get("files", []):
        rel = entry.get("path")
        if not rel:
            errors.append("lock entry missing path")
            continue
        target = root / rel
        if entry.get("required", True) and not target.exists():
            errors.append(f"locked file does not exist: {rel}")
            continue
        expected = entry.get("sha256")
        if expected and target.exists():
            actual = sha256_file(target)
            if actual.lower() != expected.lower():
                errors.append(f"sha256 mismatch: {rel}")

    asset_ids = set()
    asset_manifest_path = webby / "asset-manifest.json"
    if asset_manifest_path.exists():
        try:
            manifest = load_json(asset_manifest_path)
            assets = manifest.get("assets", [])
            asset_ids = collect_ids(assets, "id", "asset", errors)
            for asset in assets:
                prod = asset.get("production")
                if prod and not (root / prod).exists():
                    errors.append(f"production asset does not exist: {prod}")
        except ValueError as exc:
            errors.append(str(exc))

    component_ids = set()
    component_map_path = webby / "component-map.json"
    if component_map_path.exists():
        try:
            data = load_json(component_map_path)
            components = data.get("components", [])
            component_ids = collect_ids(components, "componentId", "component", errors)
            for comp in components:
                cid = comp.get("componentId")
                parent = comp.get("parentComponentId")
                if parent and parent not in component_ids:
                    errors.append(f"component {cid} references missing parentComponentId: {parent}")
                for aid in comp.get("requiredAssets", []):
                    if asset_ids and aid not in asset_ids:
                        errors.append(f"component {cid} references missing asset: {aid}")
        except ValueError as exc:
            errors.append(str(exc))

    placement_map_path = webby / "placement-map.json"
    if placement_map_path.exists():
        try:
            data = load_json(placement_map_path)
            placements = data.get("placements", [])
            collect_ids(placements, "placementId", "placement", errors)
            for placement in placements:
                pid = placement.get("placementId")
                cid = placement.get("componentId")
                aid = placement.get("assetId")
                if cid and component_ids and cid not in component_ids:
                    errors.append(f"placement {pid} references missing component: {cid}")
                if aid and asset_ids and aid not in asset_ids:
                    errors.append(f"placement {pid} references missing asset: {aid}")
        except ValueError as exc:
            errors.append(str(exc))

    request_dir = webby / "requests"
    if request_dir.exists():
        for request_file in sorted(request_dir.glob("*.json")):
            try:
                req = load_json(request_file)
                if (
                    req.get("status") == "OPEN"
                    and req.get("blocking") is True
                    and handoff.get("status") == "UI_SETUP_COMPLETE"
                ):
                    errors.append(
                        "blocking OPEN request conflicts with UI_SETUP_COMPLETE: "
                        f"{request_file.name}"
                    )
            except ValueError as exc:
                errors.append(str(exc))

    learning_dir = webby / "learning"
    if learning_dir.exists():
        seen_lessons = set()
        for learning_file in sorted(learning_dir.glob("*.json")):
            try:
                data = load_json(learning_file)
                for lesson in data.get("lessons", []):
                    lid = lesson.get("lessonId")
                    if not lid:
                        errors.append(f"learning record without lessonId: {learning_file.name}")
                    elif lid in seen_lessons:
                        errors.append(f"duplicate lessonId across learning store: {lid}")
                    else:
                        seen_lessons.add(lid)
            except ValueError as exc:
                errors.append(str(exc))

    return errors


def self_check(repo: Path) -> list[str]:
    errors = []
    for path in sorted((repo / "schemas").glob("*.json")):
        try:
            schema = load_json(path)
            if not isinstance(schema, dict):
                errors.append(f"schema must be an object: {path}")
                continue
            if "$schema" not in schema:
                errors.append(f"schema missing $schema: {path}")
            if schema.get("type") != "object":
                errors.append(f"top-level schema type must be object: {path}")
            if "properties" not in schema:
                errors.append(f"schema missing properties: {path}")
        except ValueError as exc:
            errors.append(str(exc))
    for path in sorted((repo / "templates").glob("*.json")):
        try:
            load_json(path)
        except ValueError as exc:
            errors.append(str(exc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", nargs="?", default=".")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    root = Path(args.project).resolve()
    errors = self_check(root) if args.self_check else validate_project(root)
    if errors:
        print("WEBBY_VALIDATION_FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("WEBBY_VALIDATION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
