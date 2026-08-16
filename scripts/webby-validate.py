#!/usr/bin/env python3
"""Dependency-light semantic validator for webbyLucifer project handoffs.

v3.1 distinguishes full-pipeline NEW_REDESIGN work from fast-path EXISTING_POLISH
and BUG_FIX tasks. It also treats Drive access as session-scoped and validates
required icon inventory against actual role=ICON assets.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

REQUIRED_HANDOFF_KEYS = {
    "schemaVersion", "handoffId", "producer", "executor", "status",
    "uiRevision", "uiCommit", "requiredInputs",
}
REQUIRED_LOCK_KEYS = {
    "schemaVersion", "skillVersion", "handoffId", "uiRevision", "uiCommit", "files",
}
FULL_READY_FLAGS = {
    "userVisualApproved",
    "assetCountReported",
    "assetsComplete",
    "highResMastersPass",
    "deliveryComplete",
    "transportReadyForSession",
    "mappingComplete",
    "iconInventoryComplete",
    "layoutModeLocked",
    "typographyLocked",
    "semanticGeometryLocked",
    "responsiveLocked",
    "statesLockedOrNA",
    "motionFeelLockedOrNA",
    "noBlockingSpecOrAssetGap",
}
FAST_READY_FLAGS = {
    "baselineKnown",
    "targetScoped",
    "newAssetsReadyOrNA",
    "motionMechanismScopeSafeOrReported",
    "noBlockingSpecGap",
}
V3_ASSET_CLASSES = {
    "BRAND", "AUTHENTIC", "DEMO", "EDITORIAL", "DECORATIVE", "PLACEHOLDER", "DATA_VISUAL"
}
V3_MASTER_QUALITY = {"FHD_CLASS", "4K_CLASS", "VECTOR"}
TASK_MODES = {"NEW_REDESIGN", "EXISTING_POLISH", "BUG_FIX"}


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


def is_external_ref(value: str) -> bool:
    if value.startswith(("drive://", "gdrive://")):
        return True
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"}


def ready_state(handoff: dict, lock: dict) -> tuple[bool, bool]:
    v3 = handoff.get("schemaVersion") == 3 or version_tuple(lock.get("skillVersion")) >= (3, 0, 0)
    status = handoff.get("status")
    return v3, status == ("IMPLEMENTATION_READY_UI" if v3 else "UI_SETUP_COMPLETE")


def task_mode(handoff: dict, lock: dict) -> str:
    v31 = version_tuple(lock.get("skillVersion")) >= (3, 1, 0) or handoff.get("protocolVersion") == "3.1.0"
    mode = handoff.get("taskMode")
    if v31:
        return mode or ""
    return mode or "NEW_REDESIGN"


def validate_intake(root: Path, handoff: dict, lock: dict, errors: list[str], strict: bool) -> None:
    v3, ready = ready_state(handoff, lock)
    intake_cfg = handoff.get("intake") or {}
    intake_rel = intake_cfg.get("file", ".webby/PROJECT_INTAKE.json")
    intake_path = root / intake_rel
    required = strict and ready and (v3 or version_tuple(lock.get("skillVersion")) >= (2, 2, 0))

    if not intake_path.exists():
        if required:
            errors.append(f"full-pipeline ready handoff requires project intake file: {intake_rel}")
        return

    try:
        intake = load_json(intake_path)
    except ValueError as exc:
        errors.append(str(exc))
        return

    actual_status = intake.get("status")
    declared_status = intake_cfg.get("status")
    if declared_status and declared_status != actual_status:
        errors.append("intake status mismatch between HANDOFF and PROJECT_INTAKE")

    hard_gaps = [
        gap.get("field", "<unknown>")
        for gap in intake.get("gaps", [])
        if isinstance(gap, dict) and gap.get("status") == "HARD_GAP"
    ]
    if strict and ready and actual_status != "INTAKE_COMPLETE":
        errors.append("full-pipeline ready handoff requires PROJECT_INTAKE status INTAKE_COMPLETE")
    if strict and ready and hard_gaps:
        errors.append(f"INTAKE_COMPLETE cannot contain HARD_GAP items: {hard_gaps}")

    if required:
        project = intake.get("project") or {}
        goal = intake.get("goal") or {}
        audience = intake.get("audience") or {}
        scope = intake.get("scope") or {}
        personalization = intake.get("personalizationSignals") or []
        if not project.get("businessOrOffer"):
            errors.append("intake requires project.businessOrOffer")
        if not (goal.get("primary") or goal.get("conversion")):
            errors.append("intake requires a primary or conversion goal")
        if not audience.get("primary"):
            errors.append("intake requires audience.primary")
        if not (scope.get("routes") or scope.get("features")):
            errors.append("intake requires route or feature scope")
        if not personalization:
            errors.append("intake requires at least one personalization signal")
        layout = intake.get("layout") or {}
        if not layout.get("mode"):
            errors.append("full-pipeline ready intake requires layout.mode")
        environment = intake.get("environment")
        if not isinstance(environment, dict):
            errors.append("full-pipeline ready intake requires environment readiness state")


def validate_asset_plan(root: Path, handoff: dict, errors: list[str]) -> None:
    cfg = handoff.get("assetPlan") or {}
    rel = cfg.get("file", ".webby/ASSET_COUNT_PLAN.json")
    path = root / rel
    if not path.exists():
        errors.append(f"NEW_REDESIGN IMPLEMENTATION_READY_UI requires asset count plan: {rel}")
        return
    try:
        plan = load_json(path)
    except ValueError as exc:
        errors.append(str(exc))
        return
    if plan.get("status") not in {"REPORTED", "APPROVED"}:
        errors.append("asset count plan must be REPORTED or APPROVED before full-pipeline implementation")
    if plan.get("reportedToUser") is not True:
        errors.append("asset count plan must be reported to the user before production/implementation")
    totals = plan.get("totals") or {}
    if not isinstance(totals.get("all"), int) or totals.get("all", -1) < 0:
        errors.append("asset count plan totals.all must be a non-negative integer")


def validate_full_ready_flags(handoff: dict, errors: list[str]) -> None:
    flags = handoff.get("implementationReady") or {}
    missing = sorted(FULL_READY_FLAGS - set(flags))
    if missing:
        errors.append(f"implementationReady missing flags: {missing}")
    false_flags = sorted(key for key in FULL_READY_FLAGS if flags.get(key) is not True)
    if false_flags:
        errors.append(f"NEW_REDESIGN IMPLEMENTATION_READY_UI requires true readiness flags: {false_flags}")


def validate_fast_ready_flags(handoff: dict, errors: list[str]) -> None:
    flags = handoff.get("fastPathReady") or {}
    missing = sorted(FAST_READY_FLAGS - set(flags))
    if missing:
        errors.append(f"fastPathReady missing flags: {missing}")
    false_flags = sorted(key for key in FAST_READY_FLAGS if flags.get(key) is not True)
    if false_flags:
        errors.append(f"fast-path ready handoff requires true readiness flags: {false_flags}")


def validate_asset_manifest_v31(root: Path, handoff: dict, errors: list[str]) -> None:
    cfg = handoff.get("assetManifest") or {}
    rel = cfg.get("file", ".webby/asset-manifest.json")
    path = root / rel
    if not path.exists():
        errors.append(f"NEW_REDESIGN IMPLEMENTATION_READY_UI requires asset manifest: {rel}")
        return
    try:
        manifest = load_json(path)
    except ValueError as exc:
        errors.append(str(exc))
        return

    if manifest.get("version") != 3:
        errors.append("v3.1 ready handoff requires asset-manifest version 3")
    if manifest.get("protocolVersion") not in {None, "3.1.0"}:
        errors.append("asset-manifest protocolVersion must be 3.1.0 when declared")

    store = manifest.get("assetStore") or {}
    transport = store.get("transportMode")
    if transport not in {"DRIVE", "GIT", "HYBRID"}:
        errors.append("asset manifest assetStore.transportMode must be DRIVE, GIT or HYBRID")

    session_id = handoff.get("workSessionId")
    if transport in {"DRIVE", "HYBRID"}:
        if not session_id:
            errors.append("DRIVE/HYBRID handoff requires workSessionId")
        if store.get("accessProofStatus") != "VERIFIED_THIS_SESSION":
            errors.append("DRIVE/HYBRID access must be proven in the current work session")
        if store.get("verifiedForSessionId") != session_id:
            errors.append("Drive access proof verifiedForSessionId must match HANDOFF workSessionId")
        if not store.get("sessionVerifiedAt"):
            errors.append("DRIVE/HYBRID access proof requires sessionVerifiedAt")
        if not store.get("folderRef"):
            errors.append("DRIVE/HYBRID asset store requires folderRef")
    elif transport == "GIT" and store.get("accessProofStatus") not in {"NOT_REQUIRED", None}:
        errors.append("GIT transport should mark Drive access proof NOT_REQUIRED")

    seen = set()
    role_by_id = {}
    for asset in manifest.get("assets", []):
        aid = asset.get("id")
        if not aid:
            errors.append("asset without id")
            continue
        if aid in seen:
            errors.append(f"duplicate asset id: {aid}")
        seen.add(aid)
        role_by_id[aid] = asset.get("role")

        cls = asset.get("classification")
        if cls not in V3_ASSET_CLASSES:
            errors.append(f"asset {aid} has invalid classification: {cls}")
        if cls in {"AUTHENTIC", "DATA_VISUAL"} and not asset.get("item"):
            errors.append(f"asset {aid} classification {cls} requires ITEM mapping")
        if asset.get("identityRequired") is True and not asset.get("item"):
            errors.append(f"identity-bearing asset missing ITEM: {aid}")

        master = asset.get("master") or {}
        if master.get("qualityClass") not in V3_MASTER_QUALITY:
            errors.append(f"asset {aid} master qualityClass must be FHD_CLASS, 4K_CLASS or VECTOR")
        if master.get("nativeOrAuthoritativeHighRes") is not True:
            errors.append(f"asset {aid} master is not confirmed authoritative/high-resolution")
        if master.get("derivedFromLowRes") is True:
            errors.append(f"asset {aid} master is derivedFromLowRes and cannot be authoritative high-res")
        if transport in {"DRIVE", "HYBRID"} and not master.get("driveFileRef"):
            errors.append(f"asset {aid} master missing Drive reference for {transport} transport")

        allowed = set(asset.get("allowedUsage") or [])
        delivery = asset.get("delivery") or []
        if not delivery:
            errors.append(f"asset {aid} has no web delivery file")
        for item in delivery:
            usage = item.get("usage")
            if not usage:
                errors.append(f"asset {aid} delivery missing usage")
            elif allowed and usage not in allowed:
                errors.append(f"asset {aid} delivery usage not in allowedUsage: {usage}")
            if not item.get("destinationPath"):
                errors.append(f"asset {aid} delivery missing destinationPath for usage {usage}")
            if item.get("runtimeSourceType") not in {"PROJECT_PATH", "REMOTE_DECLARED"}:
                errors.append(f"asset {aid} delivery missing/invalid runtimeSourceType for usage {usage}")
            if item.get("runtimeSourceType") == "REMOTE_DECLARED" and not item.get("runtimeSource"):
                errors.append(f"asset {aid} remote delivery requires runtimeSource for usage {usage}")
            if transport == "DRIVE" and not item.get("driveFileRef"):
                errors.append(f"asset {aid} delivery missing Drive reference for DRIVE transport usage {usage}")
            size = item.get("byteSize")
            limit = item.get("maxWeight")
            if isinstance(size, int) and isinstance(limit, int) and size > limit:
                errors.append(f"asset {aid} delivery exceeds maxWeight for usage {usage}: {size} > {limit}")

    required_icons = [
        entry.get("id")
        for entry in manifest.get("iconInventory", [])
        if isinstance(entry, dict) and entry.get("required") is True
    ]
    for icon_id in required_icons:
        if not icon_id:
            errors.append("required icon inventory entry missing id")
            continue
        if icon_id not in seen:
            errors.append(f"required icon inventory asset missing: {icon_id}")
        elif role_by_id.get(icon_id) != "ICON":
            errors.append(f"required icon inventory asset must use role=ICON: {icon_id}")


def validate_legacy_asset_manifest(root: Path, errors: list[str]) -> None:
    path = root / ".webby/asset-manifest.json"
    if not path.exists():
        return
    try:
        manifest = load_json(path)
    except ValueError as exc:
        errors.append(str(exc))
        return
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
        if prod and not is_external_ref(prod) and not (root / prod).exists():
            errors.append(f"production asset does not exist: {prod}")


def validate_visual_handoff(root: Path, handoff: dict, errors: list[str]) -> None:
    visual = handoff.get("visualHandoff")
    if not visual:
        return
    routes_rel = visual.get("routesFile")
    if not routes_rel:
        return
    routes_path = root / routes_rel
    if not routes_path.exists():
        errors.append(f"visual handoff routes file does not exist: {routes_rel}")
        return
    try:
        route_data = load_json(routes_path)
    except ValueError as exc:
        errors.append(str(exc))
        return
    routes = route_data.get("routes")
    if not isinstance(routes, dict) or not routes:
        errors.append("visual handoff routes file must contain a non-empty routes object")
        return
    base = routes_path.parent
    for route, viewports in routes.items():
        if not isinstance(viewports, dict) or not viewports:
            errors.append(f"visual route has no viewport references: {route}")
            continue
        for viewport, render_ref in viewports.items():
            if not isinstance(render_ref, str) or not render_ref.strip():
                errors.append(f"visual route reference invalid: {route} [{viewport}]")
                continue
            if is_external_ref(render_ref):
                continue
            target = Path(render_ref)
            if not target.is_absolute():
                target = base / target
            if not target.exists():
                errors.append(f"visual reference does not exist: {route} [{viewport}] -> {render_ref}")


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

    try:
        lock = load_json(lock_path)
    except ValueError as exc:
        errors.append(str(exc))
        return errors
    missing = REQUIRED_LOCK_KEYS - set(lock)
    if missing:
        errors.append(f"WEBBY_LOCK missing keys: {sorted(missing)}")

    v3, ready = ready_state(handoff, lock)
    mode = task_mode(handoff, lock)
    v31 = version_tuple(lock.get("skillVersion")) >= (3, 1, 0) or handoff.get("protocolVersion") == "3.1.0"

    if v31 and mode not in TASK_MODES:
        errors.append("v3.1 handoff taskMode must be NEW_REDESIGN, EXISTING_POLISH or BUG_FIX")

    if handoff.get("producer") != "CHATGPT" and ready:
        errors.append("ready handoff producer must be CHATGPT")
    if ready and not handoff.get("uiCommit"):
        errors.append("ready handoff requires uiCommit/state id")

    for rel in handoff.get("requiredInputs", []):
        if is_external_ref(rel):
            continue
        if not (root / rel).exists():
            errors.append(f"required input does not exist: {rel}")

    if handoff.get("handoffId") != lock.get("handoffId"):
        errors.append("handoffId mismatch between HANDOFF and WEBBY_LOCK")
    if handoff.get("uiRevision") != lock.get("uiRevision"):
        errors.append("uiRevision mismatch between HANDOFF and WEBBY_LOCK")
    if handoff.get("uiCommit") != lock.get("uiCommit"):
        errors.append("uiCommit mismatch between HANDOFF and WEBBY_LOCK")

    full_pipeline = mode == "NEW_REDESIGN"
    validate_intake(root, handoff, lock, errors, strict=full_pipeline)
    validate_visual_handoff(root, handoff, errors)

    if v3 and ready:
        if handoff.get("status") != "IMPLEMENTATION_READY_UI":
            errors.append("v3 ready handoff status must be IMPLEMENTATION_READY_UI")
        if handoff.get("finalAcceptanceAuthority") != "USER":
            errors.append("v3 handoff must declare USER as finalAcceptanceAuthority")
        if full_pipeline:
            validate_full_ready_flags(handoff, errors)
            validate_asset_plan(root, handoff, errors)
            validate_asset_manifest_v31(root, handoff, errors)
        elif mode in {"EXISTING_POLISH", "BUG_FIX"}:
            validate_fast_ready_flags(handoff, errors)
        else:
            errors.append("ready v3.1 handoff has no valid taskMode")
    else:
        validate_legacy_asset_manifest(root, errors)

    for entry in lock.get("files", []):
        rel = entry.get("path")
        if not rel:
            errors.append("lock entry missing path")
            continue
        if is_external_ref(rel):
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

    request_dir = webby / "requests"
    if request_dir.exists():
        for request_file in sorted(request_dir.glob("*.json")):
            try:
                req = load_json(request_file)
                if req.get("status") == "OPEN" and req.get("blocking") is True and ready:
                    errors.append(f"blocking OPEN request conflicts with ready handoff: {request_file.name}")
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
