#!/usr/bin/env python3
"""
Figma API helper: dump node metadata and export assets to static/assets/.

Requires:
  FIGMA_TOKEN   - personal access token
  FIGMA_FILE_KEY - e.g. RgixkfQjBcvWPRvylxy0u8

Examples:
  export FIGMA_TOKEN=...
  export FIGMA_FILE_KEY=RgixkfQjBcvWPRvylxy0u8
  python scripts/figma_export.py dump --ids 140:4885 140:5405
  python scripts/figma_export.py dump --ids-file design/figma_node_ids.txt
  python scripts/figma_export.py assets --ids 140:4885 --out static/assets
  python scripts/figma_export.py imagefills --out design/figma-imagefills.json
  python scripts/figma_export.py download-imagefills --fills design/figma-imagefills.json --plan design/figma-metrics.json
  python scripts/figma_export.py export --format svg --ids-file design/ready_icons_node_ids.txt --out static/assets/icons
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from dotenv import load_dotenv


API = "https://api.figma.com/v1"

# Load local .env so FIGMA_TOKEN/FIGMA_FILE_KEY can be stored there (do not commit it)
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def _require_env(name: str) -> str:
    v = os.getenv(name, "").strip()
    if not v:
        raise SystemExit(f"Missing env var {name}.")
    return v


def _http_get_json(url: str, token: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"X-Figma-Token": token})
    with urllib.request.urlopen(req) as resp:
        raw = resp.read().decode("utf-8")
    return json.loads(raw)


def _http_download(url: str, token: str, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"X-Figma-Token": token})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    target.write_bytes(data)


def _kebab(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "asset"


def normalize_node_id(node_id: str) -> str:
    """Accepts '140-4885' or '140:4885' and returns '140:4885'."""
    return node_id.replace("-", ":")

def read_ids_file(path: str) -> list[str]:
    p = Path(path)
    raw = p.read_text(encoding="utf-8").splitlines()
    ids = []
    for line in raw:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        ids.append(normalize_node_id(line))
    return ids


def figma_nodes(file_key: str, ids: Iterable[str], token: str) -> dict[str, Any]:
    ids = [normalize_node_id(i) for i in ids]
    query = urllib.parse.urlencode({"ids": ",".join(ids)})
    url = f"{API}/files/{file_key}/nodes?{query}"
    return _http_get_json(url, token)

def figma_image_fills(file_key: str, token: str) -> dict[str, Any]:
    """
    Get Image Fills (maps imageRef hashes to URLs).
    Endpoint: GET /v1/files/{file_key}/images
    """
    url = f"{API}/files/{file_key}/images"
    return _http_get_json(url, token)


@dataclass(frozen=True)
class Exportable:
    node_id: str
    name: str
    formats: list[str]  # e.g. ["svg", "png"]


def _collect_exportables(node: dict[str, Any], out: list[Exportable]) -> None:
    if not isinstance(node, dict):
        return
    export_settings = node.get("exportSettings") or []
    if export_settings:
        formats = []
        for s in export_settings:
            fmt = (s.get("format") or "").lower()
            if fmt in {"png", "jpg", "svg", "pdf", "webp"} and fmt not in formats:
                formats.append(fmt)
        out.append(
            Exportable(
                node_id=str(node.get("id", "")),
                name=str(node.get("name", "")),
                formats=formats or ["png"],
            )
        )
    for child in node.get("children") or []:
        _collect_exportables(child, out)


def export_images(
    file_key: str,
    ids: list[str],
    token: str,
    fmt: str,
    scale: int,
) -> dict[str, str]:
    ids = [normalize_node_id(i) for i in ids]
    query = urllib.parse.urlencode(
        {"ids": ",".join(ids), "format": fmt, "scale": str(scale)}
    )
    url = f"{API}/images/{file_key}?{query}"
    payload = _http_get_json(url, token)
    return payload.get("images") or {}

def cmd_export(args: argparse.Namespace) -> int:
    """
    Export specific nodes via /images endpoint (works for SVG/PNG even without exportSettings).
    """
    token = _require_env("FIGMA_TOKEN")
    file_key = _require_env("FIGMA_FILE_KEY")
    ids = (args.ids or []) + (read_ids_file(args.ids_file) if args.ids_file else [])
    if not ids:
        raise SystemExit("Provide --ids and/or --ids-file.")

    fmt = args.format.lower()
    if fmt not in {"svg", "png", "jpg", "pdf", "webp"}:
        raise SystemExit("Unsupported --format. Use svg/png/jpg/webp/pdf.")

    scale = int(args.scale)
    if fmt == "svg":
        # SVG is vector; scale should be 1
        scale = 1

    # Fetch names to produce stable filenames
    nodes_payload = figma_nodes(file_key, ids, token)
    nodes_map = nodes_payload.get("nodes") or {}

    urls = export_images(file_key, ids, token, fmt=fmt, scale=scale)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    used_names: set[str] = set()
    for nid in ids:
        nid_norm = normalize_node_id(nid)
        url = urls.get(nid_norm)
        if not url:
            continue
        doc = (nodes_map.get(nid_norm) or {}).get("document") or {}
        name = str(doc.get("name") or nid_norm)
        base = _kebab(name)
        # Avoid collisions for generic names (e.g. many nodes named "Frame")
        comp = str(doc.get("componentId") or "").strip()
        if comp:
            base = f"{base}-{comp.replace(':','-')}"
        suffix = "" if fmt == "svg" else ("" if scale == 1 else f"@{scale}x")
        target_name = f"{base}{suffix}.{fmt}"
        # Some nodes share the same name and have no componentId (e.g. many "Vector 295").
        # Ensure we never overwrite previously exported files.
        if target_name in used_names or (out_dir / target_name).exists():
            safe_id = _kebab(nid_norm.replace(":", "-").replace(";", "-"))
            target_name = f"{base}-{safe_id}{suffix}.{fmt}"
        used_names.add(target_name)
        target = out_dir / target_name
        _http_download(url, token, target)
        written += 1
        print(f"Downloaded: {target}")

    print(f"Done. Exported {written} files to {out_dir}.")
    return 0


def cmd_dump(args: argparse.Namespace) -> int:
    token = _require_env("FIGMA_TOKEN")
    file_key = _require_env("FIGMA_FILE_KEY")
    ids = (args.ids or []) + (read_ids_file(args.ids_file) if args.ids_file else [])
    if not ids:
        raise SystemExit("Provide --ids and/or --ids-file.")

    data = figma_nodes(file_key, ids, token)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote: {out}")
    return 0


def cmd_assets(args: argparse.Namespace) -> int:
    token = _require_env("FIGMA_TOKEN")
    file_key = _require_env("FIGMA_FILE_KEY")
    ids = (args.ids or []) + (read_ids_file(args.ids_file) if args.ids_file else [])
    if not ids:
        raise SystemExit("Provide --ids and/or --ids-file.")
    root_ids = [normalize_node_id(i) for i in ids]

    data = figma_nodes(file_key, root_ids, token)
    exportables: list[Exportable] = []
    for node_id, entry in (data.get("nodes") or {}).items():
        doc = (entry or {}).get("document") or {}
        _collect_exportables(doc, exportables)

    out_root = Path(args.out)
    icons_dir = out_root / "icons"
    images_dir = out_root / "images"
    brand_dir = out_root / "brand"
    icons_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)
    brand_dir.mkdir(parents=True, exist_ok=True)

    manifest: list[dict[str, Any]] = []

    # Split by format preference: SVG goes to icons/, raster goes to images/
    for fmt in args.formats:
        ids_for_fmt = [e.node_id for e in exportables if fmt in e.formats or not e.formats]
        if not ids_for_fmt:
            continue
        urls = export_images(file_key, ids_for_fmt, token, fmt=fmt, scale=args.scale)
        for e in exportables:
            if e.node_id not in urls:
                continue
            url = urls[e.node_id]
            base = _kebab(e.name)
            subdir = icons_dir if fmt == "svg" else images_dir
            suffix = "" if args.scale == 1 else f"@{args.scale}x"
            target = subdir / f"{base}{suffix}.{fmt}"
            _http_download(url, token, target)
            manifest.append(
                {
                    "id": e.node_id,
                    "name": e.name,
                    "format": fmt,
                    "scale": args.scale,
                    "path": str(target),
                }
            )
            print(f"Downloaded: {target}")

    (out_root / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote manifest: {out_root / 'manifest.json'}")
    return 0

def cmd_imagefills(args: argparse.Namespace) -> int:
    token = _require_env("FIGMA_TOKEN")
    file_key = _require_env("FIGMA_FILE_KEY")
    data = figma_image_fills(file_key, token)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote: {out}")
    return 0


def _extract_fills_map(payload: dict[str, Any]) -> dict[str, str]:
    # API responses vary by version; support common shapes
    if isinstance(payload.get("meta"), dict) and isinstance(payload["meta"].get("images"), dict):
        return payload["meta"]["images"]
    if isinstance(payload.get("images"), dict):
        return payload["images"]
    return {}


def cmd_download_imagefills(args: argparse.Namespace) -> int:
    token = _require_env("FIGMA_TOKEN")
    fills_payload = json.loads(Path(args.fills).read_text(encoding="utf-8"))
    fills_map = _extract_fills_map(fills_payload)
    if not fills_map:
        raise SystemExit("No image fill URLs found in fills payload.")

    plan = json.loads(Path(args.plan).read_text(encoding="utf-8"))
    assets = (plan.get("assets") or {}).get("plan") or []
    if not assets:
        raise SystemExit("No assets plan found in metrics JSON. Run scripts/figma_analyze.py first.")

    written = 0
    for a in assets:
        ref = a.get("imageRef")
        url = fills_map.get(ref)
        if not url:
            continue
        target = Path(a["suggested"]["path"])
        _http_download(url, token, target)
        written += 1
        print(f"Downloaded: {target}")

    print(f"Done. Downloaded {written} image fills.")
    return 0


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    p_dump = sub.add_parser("dump", help="Dump node JSON from Figma API.")
    p_dump.add_argument("--ids", nargs="+", help="Node IDs (140:4885 or 140-4885).")
    p_dump.add_argument("--ids-file", help="Path to newline-separated node IDs.")
    p_dump.add_argument("--out", default="design/figma-nodes.json", help="Output JSON path.")
    p_dump.set_defaults(func=cmd_dump)

    p_assets = sub.add_parser("assets", help="Download exportable assets under nodes.")
    p_assets.add_argument("--ids", nargs="+", help="Root node IDs to scan.")
    p_assets.add_argument("--ids-file", help="Path to newline-separated node IDs.")
    p_assets.add_argument("--out", default="static/assets", help="Output directory.")
    p_assets.add_argument("--formats", nargs="+", default=["svg", "png"], help="Formats to download.")
    p_assets.add_argument("--scale", type=int, default=2, choices=[1, 2, 3], help="Raster scale.")
    p_assets.set_defaults(func=cmd_assets)

    p_fills = sub.add_parser("imagefills", help="Fetch image fill URLs (imageRef -> URL).")
    p_fills.add_argument("--out", default="design/figma-imagefills.json", help="Output JSON path.")
    p_fills.set_defaults(func=cmd_imagefills)

    p_dl = sub.add_parser("download-imagefills", help="Download image fills to paths from metrics plan.")
    p_dl.add_argument("--fills", default="design/figma-imagefills.json", help="JSON from imagefills command.")
    p_dl.add_argument("--plan", default="design/figma-metrics.json", help="Metrics JSON with assets.plan.")
    p_dl.set_defaults(func=cmd_download_imagefills)

    p_export = sub.add_parser("export", help="Export nodes via images endpoint (svg/png/...).")
    p_export.add_argument("--format", required=True, help="svg/png/jpg/webp/pdf")
    p_export.add_argument("--scale", type=int, default=2, choices=[1, 2, 3], help="Raster scale (ignored for svg).")
    p_export.add_argument("--ids", nargs="+", help="Node IDs to export.")
    p_export.add_argument("--ids-file", help="Path to newline-separated node IDs.")
    p_export.add_argument("--out", required=True, help="Output directory.")
    p_export.set_defaults(func=cmd_export)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))


