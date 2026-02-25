#!/usr/bin/env python3
"""
Автоматическое применение правок для выравнивания 440px страниц по шаблону production.

Правки:
1. telegram-440-nodes.json: Blok5 ширина 439 → 440
2. print-440-nodes.json: добавить недостающий Blok3 блок из production
3. Синхронизировать metrics tokens
"""

import json
import copy
from pathlib import Path
from datetime import datetime

DESIGN_DIR = Path(r"c:\Users\KiGi\PycharmProjects\ADSmart — копия\design")

def load_json(filepath):
    """Загрузить JSON."""
    if not filepath.exists():
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data, backup=True):
    """Сохранить JSON с бэкапом."""
    if backup and filepath.exists():
        backup_path = filepath.with_suffix(f".backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json")
        with open(filepath, 'r', encoding='utf-8') as f:
            backup_data = f.read()
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(backup_data)
        print(f"  📦 Backup: {backup_path.name}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  ✅ Saved: {filepath.name}")

def fix_telegram_440_blok5():
    """Исправить width Blok5 с 439 на 440."""
    print("\n🔧 Fix 1: TELEGRAM-440 Blok5 width (439 → 440)")
    print("-" * 60)
    
    filepath = DESIGN_DIR / "telegram-440-nodes.json"
    data = load_json(filepath)
    
    if not data or "nodes" not in data:
        print("  ❌ Could not load telegram-440-nodes.json")
        return False
    
    # Find and fix Blok5
    for node_id, node_content in data["nodes"].items():
        doc = node_content.get("document", {})
        for i, child in enumerate(doc.get("children", [])):
            if child.get("name") == "Blok5" and child.get("absoluteBoundingBox", {}).get("width") == 439:
                print(f"  Found Blok5 with width=439 in node {node_id}")
                data["nodes"][node_id]["document"]["children"][i]["absoluteBoundingBox"]["width"] = 440
                print(f"  ✓ Changed width to 440")
                save_json(filepath, data)
                return True
    
    print("  ⚠️  Could not find Blok5 with width=439")
    return False

def find_blok3_in_production():
    """Найти и извлечь Blok3 из production-440-nodes.json."""
    print("\n🔍 Extracting Blok3 from Production")
    print("-" * 60)
    
    filepath = DESIGN_DIR / "production-440-nodes.json"
    data = load_json(filepath)
    
    if not data or "nodes" not in data:
        print("  ❌ Could not load production-440-nodes.json")
        return None
    
    for node_id, node_content in data["nodes"].items():
        doc = node_content.get("document", {})
        for child in doc.get("children", []):
            if child.get("name") == "Blok3":
                print(f"  ✓ Found Blok3 in production (node {node_id})")
                return copy.deepcopy(child)
    
    print("  ❌ Could not find Blok3 in production")
    return None

def fix_print_440_add_blok3():
    """Добавить Blok3 в print-440-6863-nodes.json между Blok2 и Blok5."""
    print("\n🔧 Fix 2: PRINT-440-6863 Add missing Blok3")
    print("-" * 60)
    
    filepath = DESIGN_DIR / "print-440-6863-nodes.json"
    data = load_json(filepath)
    
    if not data or "nodes" not in data:
        print("  ❌ Could not load print-440-nodes.json")
        return False
    
    # Extract Blok3 from production
    blok3_template = find_blok3_in_production()
    if not blok3_template:
        print("  ❌ Could not get Blok3 template from production")
        return False
    
    # Find print document
    for node_id, node_content in data["nodes"].items():
        doc = node_content.get("document", {})
        children = doc.get("children", [])
        
        # Find Blok2 position
        blok2_idx = None
        blok5_idx = None
        for i, child in enumerate(children):
            if child.get("name") == "Blok2":
                blok2_idx = i
            elif child.get("name") == "Blok5":
                blok5_idx = i
        
        if blok2_idx is not None and blok5_idx is not None:
            if blok5_idx == blok2_idx + 1:
                # Blok3 is missing, insert it
                blok3_copy = copy.deepcopy(blok3_template)
                # Adjust position: after Blok2, before Blok5
                children.insert(blok2_idx + 1, blok3_copy)
                data["nodes"][node_id]["document"]["children"] = children
                print(f"  ✓ Inserted Blok3 at position {blok2_idx + 1}")
                save_json(filepath, data)
                return True
            else:
                print(f"  ℹ️  Blok3 already exists or layout is different (Blok2={blok2_idx}, Blok5={blok5_idx})")
                return False
    
    print(f"  ❌ Could not find Blok2/Blok5 in print-440-6863")
    return False

def sync_metrics_tokens():
    """Синхронизировать tokens из production-440-metrics в другие metrics."""
    print("\n🔧 Fix 3: SYNC Metrics Tokens")
    print("-" * 60)
    
    prod_metrics_file = DESIGN_DIR / "production-440-metrics.json"
    prod_metrics = load_json(prod_metrics_file)
    
    if not prod_metrics or "tokens" not in prod_metrics:
        print("  ❌ Could not load tokens from production")
        return False
    
    prod_tokens = prod_metrics.get("tokens", {})
    
    # Попробовать синхронизировать print metrics (если есть)
    print_metrics_file = DESIGN_DIR / "print-440-6863-metrics.json"
    if print_metrics_file.exists():
        print_metrics = load_json(print_metrics_file)
        if print_metrics:
            print_metrics["tokens"] = copy.deepcopy(prod_tokens)
            save_json(print_metrics_file, print_metrics)
            print(f"  ✓ Updated print-440-6863-metrics.json tokens")
    else:
        print(f"  ⓘ print-440-6863-metrics.json not found (skipped)")
    
    # Telegram metrics
    telegram_metrics_file = DESIGN_DIR / "telegram-440-metrics.json"
    if telegram_metrics_file.exists():
        telegram_metrics = load_json(telegram_metrics_file)
        if telegram_metrics:
            telegram_metrics["tokens"] = copy.deepcopy(prod_tokens)
            save_json(telegram_metrics_file, telegram_metrics)
            print(f"  ✓ Updated telegram-440-metrics.json tokens")
    else:
        print(f"  ⓘ telegram-440-metrics.json not found (skipped)")
    
    return True

def main():
    print("=" * 80)
    print("ПРИМЕНЕНИЕ ПРАВОК К 440px ДИЗАЙН-ФАЙЛАМ")
    print("=" * 80)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Design dir: {DESIGN_DIR}\n")
    
    results = {
        "telegram_fix": fix_telegram_440_blok5(),
        "print_fix": fix_print_440_add_blok3(),
        "metrics_sync": sync_metrics_tokens(),
    }
    
    print("\n" + "=" * 80)
    print("РЕЗУЛЬТАТЫ")
    print("=" * 80)
    print(f"✓ Telegram Blok5 width fix: {'SUCCESS' if results['telegram_fix'] else 'FAILED/SKIPPED'}")
    print(f"✓ Print add Blok3 fix: {'SUCCESS' if results['print_fix'] else 'FAILED/SKIPPED'}")
    print(f"✓ Metrics tokens sync: {'SUCCESS' if results['metrics_sync'] else 'FAILED/SKIPPED'}")
    
    if all(results.values()):
        print("\n✅ ВСЕ ПРАВКИ ПРИМЕНЕНЫ УСПЕШНО!")
    else:
        print("\n⚠️  Некоторые правки скипнуты или не удались")
    
    print("\nБэкапы сохранены с суффиксом -backup-YYYYMMDD-HHMMSS.json")

if __name__ == "__main__":
    main()
