#!/usr/bin/env python3
"""
Analyze `design/figma-nodes.json` (Figma API /files/:key/nodes dump) and generate:
- docs/figma-spec-generated.md (page map, tokens, components hints, assets list)
- design/figma-metrics.json (raw aggregates)

This does NOT guess numeric values. All values come from the JSON dump.
Role-mapping for colors is inferred from usage context (frames/text) and should be verified in Figma.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, DefaultDict, Iterable


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def rgba_to_hex(rgba: dict[str, Any]) -> str:
    r = int(round(clamp01(float(rgba.get("r", 0))) * 255))
    g = int(round(clamp01(float(rgba.get("g", 0))) * 255))
    b = int(round(clamp01(float(rgba.get("b", 0))) * 255))
    a = clamp01(float(rgba.get("a", 1)))
    if a >= 0.999:
        return f"#{r:02x}{g:02x}{b:02x}"
    return f"rgba({r},{g},{b},{a:.3f})"


def round_px(v: Any) -> int:
    try:
        return int(round(float(v)))
    except Exception:
        return 0


def kebab(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "asset"


@dataclass(frozen=True)
class TextStyle:
    font_family: str
    font_size: float
    font_weight: int
    line_height: str  # px or %
    letter_spacing: str  # px or %


def _line_height(style: dict[str, Any]) -> str:
    lh = style.get("lineHeightPx")
    if lh is not None:
        return f"{float(lh):g}px"
    lhp = style.get("lineHeightPercent")
    if lhp is not None:
        return f"{float(lhp):g}%"
    lhpfs = style.get("lineHeightPercentFontSize")
    if lhpfs is not None:
        return f"{float(lhpfs):g}%"
    return "normal"


def _letter_spacing(style: dict[str, Any]) -> str:
    ls = style.get("letterSpacing")
    if not isinstance(ls, dict):
        return "0"
    if ls.get("unit") == "PERCENT":
        return f"{float(ls.get('value', 0)):g}%"
    return f"{float(ls.get('value', 0)):g}px"


def walk(node: dict[str, Any], path: tuple[str, ...], visit) -> None:
    visit(node, path)
    for child in node.get("children") or []:
        walk(child, path + (str(child.get("name", "")),), visit)


def load_dump(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_root_frame(doc: dict[str, Any]) -> bool:
    return doc.get("type") == "FRAME" and doc.get("children") is not None


def is_text(node: dict[str, Any]) -> bool:
    return node.get("type") == "TEXT"


def is_autolayout_frame(node: dict[str, Any]) -> bool:
    return node.get("type") == "FRAME" and node.get("layoutMode") in {"HORIZONTAL", "VERTICAL"}


def analyze(dump: dict[str, Any]) -> dict[str, Any]:
    pages = []
    color_counter: Counter[str] = Counter()
    color_context: DefaultDict[str, Counter[str]] = defaultdict(Counter)
    text_counter: Counter[tuple] = Counter()
    spacing_counter: Counter[int] = Counter()
    radius_counter: Counter[int] = Counter()
    shadow_counter: Counter[str] = Counter()
    image_refs: DefaultDict[str, list[dict[str, Any]]] = defaultdict(list)
    frame_widths: Counter[int] = Counter()
    instance_counter: Counter[tuple[str, str]] = Counter()  # (name, componentId)

    for node_id, entry in (dump.get("nodes") or {}).items():
        doc = (entry or {}).get("document") or {}
        if not is_root_frame(doc):
            continue

        name = str(doc.get("name", "")).strip()
        bbox = doc.get("absoluteBoundingBox") or {}
        w = round_px(bbox.get("width"))
        h = round_px(bbox.get("height"))
        frame_widths[w] += 1

        blocks = []
        for ch in doc.get("children") or []:
            blocks.append({"name": ch.get("name"), "type": ch.get("type")})

        # Traverse to collect tokens/assets
        def visit(n: dict[str, Any], p: tuple[str, ...]) -> None:
            n_type = n.get("type")

            if n_type == "INSTANCE":
                instance_counter[(str(n.get("name", "")), str(n.get("componentId", "")))] += 1

            # Colors: solid fills/strokes
            for fill in n.get("fills") or []:
                if isinstance(fill, dict) and fill.get("type") == "SOLID" and fill.get("color"):
                    c = rgba_to_hex(fill["color"])
                    color_counter[c] += 1
                    color_context[c][str(n_type)] += 1
            for stroke in n.get("strokes") or []:
                if isinstance(stroke, dict) and stroke.get("type") == "SOLID" and stroke.get("color"):
                    c = rgba_to_hex(stroke["color"])
                    color_counter[c] += 1
                    color_context[c][f"{n_type}:stroke"] += 1

            # Text styles
            if is_text(n):
                style = n.get("style") or {}
                ts = TextStyle(
                    font_family=str(style.get("fontFamily", "")).strip(),
                    font_size=float(style.get("fontSize") or 0),
                    font_weight=int(style.get("fontWeight") or 0),
                    line_height=_line_height(style),
                    letter_spacing=_letter_spacing(style),
                )
                text_counter[(ts.font_family, ts.font_size, ts.font_weight, ts.line_height, ts.letter_spacing)] += 1

                # Text color also can appear in fills

            # Spacing scale: autolayout paddings + itemSpacing
            if is_autolayout_frame(n):
                for k in ("paddingLeft", "paddingRight", "paddingTop", "paddingBottom", "itemSpacing"):
                    if k in n:
                        spacing_counter[round_px(n.get(k))] += 1

            # Radius
            cr = n.get("cornerRadius")
            if cr is not None:
                radius_counter[round_px(cr)] += 1
            rcr = n.get("rectangleCornerRadii")
            if isinstance(rcr, list) and rcr:
                for v in rcr:
                    radius_counter[round_px(v)] += 1

            # Shadows
            for eff in n.get("effects") or []:
                if not isinstance(eff, dict):
                    continue
                if eff.get("type") in {"DROP_SHADOW", "INNER_SHADOW"} and eff.get("color"):
                    c = rgba_to_hex(eff["color"])
                    off = eff.get("offset") or {}
                    blur = eff.get("radius")
                    spread = eff.get("spread")
                    key = f"{eff.get('type')} {round_px(off.get('x'))} {round_px(off.get('y'))} {round_px(blur)} {round_px(spread)} {c}"
                    shadow_counter[key] += 1

            # Image fills
            for fill in n.get("fills") or []:
                if isinstance(fill, dict) and fill.get("type") == "IMAGE" and fill.get("imageRef"):
                    bbox = n.get("absoluteBoundingBox") or {}
                    image_refs[str(fill["imageRef"])].append(
                        {
                            "page": name,
                            "node_id": n.get("id"),
                            "node_name": n.get("name"),
                            "path": " / ".join([x for x in p if x]),
                            "w": round_px(bbox.get("width")),
                            "h": round_px(bbox.get("height")),
                            "scaleMode": fill.get("scaleMode"),
                        }
                    )

        walk(doc, (name,), visit)

        pages.append(
            {
                "node_id": node_id,
                "name": name,
                "size": {"w": w, "h": h},
                "blocks": blocks,
            }
        )

    # Prepare summaries
    top_colors = [{"value": c, "count": n, "by_type": dict(color_context[c].most_common(5))} for c, n in color_counter.most_common(40)]

    text_styles = []
    for (ff, fs, fw, lh, ls), n in text_counter.most_common(60):
        text_styles.append(
            {
                "fontFamily": ff,
                "fontSize": fs,
                "fontWeight": fw,
                "lineHeight": lh,
                "letterSpacing": ls,
                "count": n,
            }
        )

    spacings = [{"px": k, "count": v} for k, v in spacing_counter.most_common(40) if k != 0]
    radii = [{"px": k, "count": v} for k, v in radius_counter.most_common(30) if k != 0]
    shadows = [{"value": k, "count": v} for k, v in shadow_counter.most_common(30)]
    widths = [{"px": k, "count": v} for k, v in frame_widths.most_common()]

    instances = [
        {"name": n, "componentId": cid, "count": c}
        for (n, cid), c in instance_counter.most_common(80)
    ]

    # Build assets plan from imageRefs (deterministic naming based on layer name + imageRef prefix)
    assets_plan = []
    for ref, uses in image_refs.items():
        name_counts = Counter([str(u.get("node_name", "")) for u in uses])
        best_name = name_counts.most_common(1)[0][0] if name_counts else "image"
        ref_short = str(ref)[:8]
        base = f"{kebab(best_name)}-{ref_short}"
        assets_plan.append(
            {
                "imageRef": ref,
                "suggested": {
                    "path": f"static/assets/images/{base}.png",
                    "name": f"{base}.png",
                },
                "usages": uses,
            }
        )
    assets_plan.sort(key=lambda x: x["suggested"]["name"])

    return {
        "pages": sorted(pages, key=lambda x: x["node_id"]),
        "breakpoints": {"frame_widths": widths},
        "tokens": {
            "colors_top": top_colors,
            "text_styles": text_styles,
            "spacing": spacings,
            "radii": radii,
            "shadows": shadows,
        },
        "assets": {
            "image_refs_count": len(image_refs),
            "image_refs": image_refs,  # dict: imageRef -> list[usage]
            "plan": assets_plan,
        },
        "components": {
            "instances": instances,
        },
    }


def md_escape(s: str) -> str:
    return (s or "").replace("|", "\\|")


def render_md(report: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("## Figma → Django Templates + чистый CSS — сгенерированная спецификация")
    lines.append("")
    lines.append("Источник: `design/figma-nodes.json` (Figma API nodes dump).")
    lines.append("Все числовые значения ниже взяты из JSON; роли/семантика (bg/surface/primary) требуют верификации по стилям/Dev Mode.")
    lines.append("")

    # A) Pages map
    lines.append("### A) Карта страниц (по frames)")
    lines.append("")
    for p in report["pages"]:
        lines.append(f"- **{md_escape(p['name'])}** (`{p['node_id']}`) — {p['size']['w']}×{p['size']['h']}")
        if p["blocks"]:
            lines.append("  - **Блоки верхнего уровня**:")
            for b in p["blocks"][:20]:
                lines.append(
                    f"    - `{md_escape(str(b.get('name')))}` ({md_escape(str(b.get('type')))})"
                )
            if len(p["blocks"]) > 20:
                lines.append(f"    - … и ещё {len(p['blocks'])-20}")
        lines.append("")

    # Breakpoints
    lines.append("### Breakpoints / форматы")
    lines.append("")
    lines.append("| Frame width (px) | Count |")
    lines.append("|---:|---:|")
    for w in report["breakpoints"]["frame_widths"]:
        lines.append(f"| {w['px']} | {w['count']} |")
    lines.append("")

    # B) Tokens
    lines.append("### B) Tokens (сырые данные из макета)")
    lines.append("")
    lines.append("#### Colors (top 40 по частоте)")
    lines.append("| Color | Count | Where (top) |")
    lines.append("|---|---:|---|")
    for c in report["tokens"]["colors_top"]:
        where = ", ".join([f"{k}:{v}" for k, v in (c.get("by_type") or {}).items()])
        lines.append(f"| `{c['value']}` | {c['count']} | {md_escape(where)} |")
    lines.append("")

    lines.append("#### Typography (уникальные TEXT стили)")
    lines.append("| font-family | size | weight | line-height | letter-spacing | count |")
    lines.append("|---|---:|---:|---|---|---:|")
    for t in report["tokens"]["text_styles"]:
        lines.append(
            f"| `{md_escape(t['fontFamily'])}` | {t['fontSize']:g} | {t['fontWeight']} | `{t['lineHeight']}` | `{t['letterSpacing']}` | {t['count']} |"
        )
    lines.append("")

    lines.append("#### Spacing (Auto-layout paddings / gaps)")
    lines.append("| px | count |")
    lines.append("|---:|---:|")
    for s in report["tokens"]["spacing"]:
        lines.append(f"| {s['px']} | {s['count']} |")
    lines.append("")

    lines.append("#### Radius")
    lines.append("| px | count |")
    lines.append("|---:|---:|")
    for r in report["tokens"]["radii"]:
        lines.append(f"| {r['px']} | {r['count']} |")
    lines.append("")

    lines.append("#### Shadows / effects (top)")
    for sh in report["tokens"]["shadows"]:
        lines.append(f"- `{sh['value']}` × {sh['count']}")
    lines.append("")

    # C) Components (instances)
    lines.append("### C) Компоненты (INSTANCE из макета)")
    lines.append("")
    lines.append("| Instance name | componentId | count |")
    lines.append("|---|---|---:|")
    for it in report.get("components", {}).get("instances", [])[:30]:
        lines.append(
            f"| `{md_escape(it['name'])}` | `{md_escape(it['componentId'])}` | {it['count']} |"
        )
    lines.append("")

    # D) Build table (page -> instances)
    lines.append("### D) Таблица сборки (page → компоненты → данные)")
    lines.append("")
    lines.append("| Page (node) | Template | Components (top-level instances) | Data (mocks) |")
    lines.append("|---|---|---|---|")
    for p in report["pages"]:
        instance_blocks = [b["name"] for b in p["blocks"] if b.get("type") == "INSTANCE"][:6]
        comps = ", ".join([f"`{md_escape(str(x))}`" for x in instance_blocks]) or "—"
        slug = kebab(p["name"])
        lines.append(f"| `{md_escape(p['name'])}` | `templates/pages/{slug}.html` | {comps} | TBD |")
    lines.append("")

    # E) Assets
    lines.append("### E) Ассеты (image fills по imageRef)")
    lines.append("")
    lines.append(f"Найдено imageRef: **{report['assets']['image_refs_count']}**")
    lines.append("")
    lines.append("| Suggested path | format | density | imageRef | Where used (sample) |")
    lines.append("|---|---|---:|---|---|")
    for a in report["assets"].get("plan", [])[:120]:
        uses = a.get("usages") or []
        sample = uses[0] if uses else {}
        usage = f"{sample.get('page')} · {sample.get('path')} · {sample.get('w')}×{sample.get('h')}"
        # Recommendation: raster exports as PNG/WebP; keep 2x by default
        lines.append(
            f"| `{a['suggested']['path']}` | `png` | 2x | `{a['imageRef']}` | {md_escape(usage)} |"
        )
    if len(report["assets"].get("plan", [])) > 120:
        lines.append(f"| … | … | … | … | … (ещё {len(report['assets']['plan'])-120}) |")
    lines.append("")
    lines.append("Примечание: это **image fills** (raster) по `imageRef`. Для скачивания нужен endpoint Figma API \"get image fills\" (URL по `imageRef`).")
    lines.append("")

    return "\n".join(lines)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", default="design/figma-nodes.json")
    ap.add_argument("--out-md", default="docs/figma-spec-generated.md")
    ap.add_argument("--out-json", default="design/figma-metrics.json")
    args = ap.parse_args(argv)

    dump = load_dump(Path(args.in_path))
    report = analyze(dump)

    Path(args.out_json).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    Path(args.out_md).write_text(render_md(report), encoding="utf-8")
    print(f"Wrote: {args.out_md}")
    print(f"Wrote: {args.out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv[1:]))


