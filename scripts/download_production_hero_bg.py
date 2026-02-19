#!/usr/bin/env python3
"""
Download the correct Production hero background from Figma (Производство рекламы).
Saves to static/assets/images/production-hero-bg.png

Requires: FIGMA_TOKEN in .env
Run: python scripts/download_production_hero_bg.py
"""
import json
import os
import urllib.request
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

IMAGE_REF = "073cb30e1d28cb97063329832b0c7b268491dbee"
OUT_PATH = BASE_DIR / "static" / "assets" / "images" / "production-hero-bg.png"


def main():
    token = os.getenv("FIGMA_TOKEN", "").strip()
    if not token:
        print("Error: Set FIGMA_TOKEN in .env")
        return 1

    fills_path = BASE_DIR / "design" / "figma-imagefills.json"
    if not fills_path.exists():
        print("Error: Run 'python scripts/figma_export.py imagefills' first")
        return 1

    data = json.loads(fills_path.read_text(encoding="utf-8"))
    images = (data.get("meta") or {}).get("images") or data.get("images") or {}
    url = images.get(IMAGE_REF)
    if not url:
        print("Error: Image ref not found in figma-imagefills.json")
        return 1

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"X-Figma-Token": token})
    with urllib.request.urlopen(req) as resp:
        OUT_PATH.write_bytes(resp.read())
    print(f"Downloaded: {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
