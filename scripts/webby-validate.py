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


def version_tuple(value) -> tuple[int, int, int]:
    try:
        parts = str(value).split(".")[:3]
        nums = [int(part) for part in parts]
        while len(nums) < 3:
            nums.append(0)
        return tuple(nums)
    except (TypeError, ValueError):
        return (0, 0, 0)


def validate_intake(root: Path, handoff: dict, lock: dict, errors: list[str]) -> None:
    intake_cfg = handoff.get("intake") or {}
    intake_rel = intake_cfg.get("file", ".webby/PROJECT_INTAKE.json")
    intake_path = root / intake_rel

    v22_or_newer = version_tuple(lock.get("skillVersion")) >= (2, 2, 0)
    ready = handoff.get("status") == "UI_SETUP_COMPLETE"
    required = v22_or_newer and ready

    if not intake_path.exists():
        if required:
            errors.append(f"v2.2+ UI_SETUP_COMPLETE requires project intake file: {intake_rel}")
        return

    try:
        intake = load_json(intake_path)
    except ValueError as exc:
        errors.append(str(exc))
        return

    declared_status = intake_cfg.get("status")
    actual_status = intake.get("status")
    if declared_status and declared_status != actual_status:
        errors.append("intake status mismatch between HANDOFF and PROJECT_INTAKE")

    hard_gaps = [
        gap.get("field", "<unknown>")
        for gap in intake.get("gaps", [])
        if isinstance(gap, dict) and gap.get("status") == "HARD_GAP"
    ]

    if ready and actual_status != "INTAKE_COMPLETE":
        errors.append("UI_SETUP_COMPLETE requires PROJECT_INTAKE status INTAKE_COMPLETE")
    if ready and hard_gaps:
        errors.append(f"INTAKE_COMPLETE cannot contain HARD_GAP items: {hard_gaps}")

    if required:
        project = intake.get("project") or {}
        goal = intake.get("goal") or {}
        audience = intake.get("audience") or {}
        scope = intake.get("scope") or {}
        personalization = intake.get("personalizationSignals") or []

        if not project.get("businessOrOffer"):
            errors.append("v2.2+ intake requires project.businessOrOffer")
        if not (goal.get("primary") or goal.get("conversion")):
            errors.append("v2.2+ intake requires a primary or conversion goal")
        if not audience.get("primary"):
            errors.append("v2.2+ intake requires audience.primary")
        if not (scope.get("routes") or scope.get("features")):
            errors.append("v2.2+ intake requires route or feature scope")
        if not personalization:
            errors.append("v2.2+ intake requires at least one personalization signal")


def validate_visual_handoff(root: Path, handoff: dict, errors: list[str]) -> None:
    visual = handoff.get("visualHandoff")
    if not visual:
        return

    routes_rel = visual.get("routesFile")
    if not routes_rel:
        if visual.get("mode") == "VISUAL_FIRST" and handoff.get("status") == "UI_SETUP_COMPLETE":
            errors.append("VISUAL_FIRST UI_SETUP_COMPLETE handoff requires visualHandoff.routesFile")
        return

    routes_path = root / routes_rel
    try:
        route_data = load_json(routes_path)
    except ValueError as exc:
        errors.append(str(exc))
        return

    route_revision = route_data.get("uiRevision")
    if route_revision is not None and route_revision != handoff.get("uiRevision"):
        errors.append("uiRevision mismatch between HANDOFF and visual handoff routes file")

    route_commit = route_data.get("uiCommit")
    if route_commit is not None and route_commit != handoff.get("uiCommit"):
        errors.append("uiCommit mismatch between HANDOFF and visual handoff routes file")

    routes = route_data.get("routes")
    if not isinstance(routes, dict) or not routes:
        errors.append("visual handoff routes file must contain a non-empty routes object")
        return

    base = routes_path.parent
    for route, viewports in routes.items():
        if not isinstance(viewports, dict) or not viewports:
            errors.append(f"visual route has no viewport renders: {route}")
            continue
        for viewport, render_rel in viewports.items():
            if not isinstance(render_rel, str) or not render_rel.strip():
                errors.append(f"visual route render path is invalid: {route} [{viewport}]")
                continue
            render_path = Path(render_rel)
            target = render_path if render_path.is_absolute() else base / render_path
            if not target.exists():
                errors.append(f"approved visual render does not exist: {route} [{viewport}] -> {render_rel}")


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

    validate_visual_handoff(root, handoff, errors)

    try:
        lock = load_json(lock_path)
    except ValueError as exc:
        errors.append(str(exc))
        return errors

    missing = REQUIRED_LOCK_KEYS - set(lock)
    if missing:
        errors.append(f"WEBBY_LOCK missing keys: {sorted(missing)}")

    if handoff.get("handoffId") != lock.get("handoffId"):
        errors.append("handoffId mismatch between HANDOFF and WEBBY_LOCK")
    if handoff.get("uiRevision") != lock.get("uiRevision"):
        errors.append("uiRevision mismatch between HANDOFF and WEBBY_LOCK")
    if handoff.get("uiCommit") != lock.get("uiCommit"):
        errors.append("uiCommit mismatch between HANDOFF and WEBBY_LOCK")

    validate_intake(root, handoff, lock, errors)

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

    asset_manifest_path = webby / "asset-manifest.json"
    if asset_manifest_path.exists():
        try:
            manifest = load_json(asset_manifest_path)
            seen = set()
            for asset in manifest.get("assets", []):
                aid = asset.get("id")
                if not aid:
                    errors.append("asset without id")
                elif aid in seen:
                    errors.append(f"duplicate asset id: {aid}")
                else:
                    seen.add(aid)
                prod = asset.get("production")
                if prod and not (root / prod).exists():
                    errors.append(f"production asset does not exist: {prod}")
        except ValueError as exc:
            errors.append(str(exc))

    component_map_path = webby / "component-map.json"
    if component_map_path.exists():
        try:
            data = load_json(component_map_path)
            seen = set()
            for comp in data.get("components", []):
                cid = comp.get("componentId") or comp.get("name")
                if not cid:
                    errors.append("component without componentId/name")
                elif cid in seen:
                    errors.append(f"duplicate component id: {cid}")
                else:
                    seen.add(cid)
        except ValueError as exc:
            errors.append(str(exc))

    request_dir = webby / "requests"
    if request_dir.exists():
        for request_file in sorted(request_dir.glob("*.json")):
            try:
                req = load_json(request_file)
                if req.get("status") == "OPEN" and req.get("blocking") is True and handoff.get("status") == "UI_SETUP_COMPLETE":
                    errors.append(f"blocking OPEN request conflicts with UI_SETUP_COMPLETE: {request_file.name}")
            except ValueError as exc:
                errors.append(str(exc))

    return errors


def self_check(repo: Path) -> list[str]:
    errors = []
    for path in sorted((repo / "schemas").glob("*.json")):
        try:
            load_json(path)
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
