#!/usr/bin/env python3
"""
Анализ 440px страниц в дизайн-файлах.
Сравнение с production/ как шаблоном для идентификации блоков, требующих правок.
"""

import json
import os
from pathlib import Path
from collections import defaultdict

DESIGN_DIR = Path(r"c:\Users\KiGi\PycharmProjects\ADSmart — копия\design")

# Найденные 440-файлы
FILES_440 = [
    "production-440-metrics.json",
    "production-440-nodes.json",
    "print-440-6863-metrics.json",
    "print-440-6863-nodes.json",
    "print-440-6863-hero.json",
    "telegram-440-metrics.json",
    "telegram-440-nodes.json",
]

def load_json(filepath):
    """Загрузить JSON файл."""
    if not filepath or not filepath.exists():
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Ошибка при чтении {filepath.name if filepath else 'None'}: {e}")
        return None

def extract_pages_from_metrics(metrics):
    """Извлечь pages и blocks из metrics.json."""
    if not metrics:
        return []
    
    pages = metrics.get("pages", [])
    result = []
    for page in pages:
        # блоки могут быть либо strings, либо dicts с 'name'
        blocks = page.get("blocks", [])
        block_names = []
        for block in blocks:
            if isinstance(block, dict):
                block_names.append(block.get("name", "?"))
            else:
                block_names.append(str(block))
        
        page_info = {
            "node_id": page.get("node_id"),
            "name": page.get("name", "Unknown"),
            "size": page.get("size", {}),
            "breakpoints": page.get("breakpoints", []),
            "blocks": block_names,
            "components_count": len(page.get("components", {}).get("instances", []))
        }
        result.append(page_info)
    return result

def extract_blocks_from_nodes(nodes_data):
    """Извлечь document info и children (блоки) из nodes.json."""
    if not nodes_data or "nodes" not in nodes_data:
        return {}
    
    result = {}
    for node_id, node_content in nodes_data["nodes"].items():
        doc = node_content.get("document", {})
        page_name = doc.get("name", node_id)
        page_size = doc.get("absoluteBoundingBox", {})
        children_names = [child.get("name") for child in doc.get("children", [])]
        
        result[node_id] = {
            "name": page_name,
            "size": page_size,
            "blocks": children_names,
            "blocks_count": len(children_names),
            "document": doc
        }
    return result

def analyze_file_pair(metrics_file, nodes_file):
    """Анализ пары metrics + nodes файлов для одной страницы."""
    metrics_data = load_json(metrics_file)
    nodes_data = load_json(nodes_file)
    
    metrics_pages = extract_pages_from_metrics(metrics_data) if metrics_data else []
    nodes_pages = extract_blocks_from_nodes(nodes_data) if nodes_data else {}
    
    info = {
        "metrics_pages": metrics_pages,
        "nodes_pages": nodes_pages,
        "file_pair": (metrics_file.name if metrics_file else None, 
                      nodes_file.name if nodes_file else None)
    }
    return info

def main():
    """Главная функция анализа."""
    print("=" * 80)
    print("АНАЛИЗ 440px СТРАНИЦ")
    print("=" * 80)
    
    # Анализ PRODUCTION (эталон)
    print("\n📋 PRODUCTION-440 (ЭТАЛОН):")
    print("-" * 80)
    production_metrics = DESIGN_DIR / "production-440-metrics.json"
    production_nodes = DESIGN_DIR / "production-440-nodes.json"
    
    production_info = analyze_file_pair(production_metrics, production_nodes)
    
    if production_info["metrics_pages"]:
        prod_page = production_info["metrics_pages"][0]
        print(f"  Page ID: {prod_page['node_id']}")
        print(f"  Name: {prod_page['name']}")
        print(f"  Size: {prod_page['size']}")
        print(f"  Breakpoints: {prod_page['breakpoints']}")
        print(f"  Blocks (из metrics): {prod_page['blocks']}")
        print(f"  Components count: {prod_page['components_count']}")
    
    if production_info["nodes_pages"]:
        for node_id, nodes_page in production_info["nodes_pages"].items():
            print(f"  Blocks (из nodes): {nodes_page['blocks']}")
    
    # Анализ других 440 страниц
    pages_info = {}
    
    print("\n📄 ДРУГИЕ 440px СТРАНИЦЫ:")
    print("-" * 80)
    
    # Print-440
    print("\n  🔹 PRINT-440-6863:")
    print_metrics = DESIGN_DIR / "print-440-6863-metrics.json"
    print_nodes = DESIGN_DIR / "print-440-6863-nodes.json"
    
    if print_metrics.exists():
        print_info = analyze_file_pair(print_metrics, print_nodes)
        pages_info["print-440"] = print_info
        
        if print_info["metrics_pages"]:
            page = print_info["metrics_pages"][0]
            print(f"     Name: {page['name']}")
            print(f"     Size: {page['size']}")
            print(f"     Blocks: {page['blocks']}")
            print(f"     Components: {page['components_count']}")
        
        if print_info["nodes_pages"]:
            for node_id, nodes_page in print_info["nodes_pages"].items():
                print(f"     Nodes blocks: {nodes_page['blocks'][:5]}...")
    else:
        print("     ⚠️  Metrics файл не найден")
    
    # Telegram-440
    print("\n  🔹 TELEGRAM-440:")
    telegram_metrics = DESIGN_DIR / "telegram-440-metrics.json"
    telegram_nodes = DESIGN_DIR / "telegram-440-nodes.json"
    
    if telegram_metrics.exists():
        telegram_info = analyze_file_pair(telegram_metrics, telegram_nodes)
        pages_info["telegram-440"] = telegram_info
        
        if telegram_info["metrics_pages"]:
            page = telegram_info["metrics_pages"][0]
            print(f"     Name: {page['name']}")
            print(f"     Size: {page['size']}")
            print(f"     Blocks: {page['blocks']}")
            print(f"     Components: {page['components_count']}")
        
        if telegram_info["nodes_pages"]:
            for node_id, nodes_page in telegram_info["nodes_pages"].items():
                print(f"     Nodes blocks: {nodes_page['blocks'][:5]}...")
    else:
        print("     ⚠️  Metrics файл не найден, ищу в nodes...")
        telegram_info = analyze_file_pair(None, telegram_nodes)
        pages_info["telegram-440"] = telegram_info
        
        if telegram_info["nodes_pages"]:
            for node_id, nodes_page in telegram_info["nodes_pages"].items():
                print(f"     Name: {nodes_page['name']}")
                print(f"     Blocks: {nodes_page['blocks'][:5]}...")
    
    # Сравнение структуры
    print("\n" + "=" * 80)
    print("✅ ВЫВОД: СТРУКТУРА БЛОКОВ")
    print("=" * 80)
    
    prod_blocks = None
    if production_info["metrics_pages"]:
        prod_blocks = set(production_info["metrics_pages"][0]["blocks"])
    if not prod_blocks and production_info["nodes_pages"]:
        for node_id, page in production_info["nodes_pages"].items():
            prod_blocks = set(page["blocks"])
            break
    
    if prod_blocks:
        print(f"\nProduction блоки (эталон): {sorted(prod_blocks)}")
        
        for page_name, page_info in pages_info.items():
            if page_info["metrics_pages"]:
                other_blocks = set(page_info["metrics_pages"][0]["blocks"])
            elif page_info["nodes_pages"]:
                other_blocks = set(list(page_info["nodes_pages"].values())[0]["blocks"])
            else:
                other_blocks = set()
            
            if other_blocks:
                print(f"\n{page_name} блоки: {sorted(other_blocks)}")
                if other_blocks == prod_blocks:
                    print(f"  ✓ ИДЕНТИЧНЫ production")
                else:
                    missing = prod_blocks - other_blocks
                    extra = other_blocks - prod_blocks
                    if missing:
                        print(f"  ⚠️  Отсутствуют: {missing}")
                    if extra:
                        print(f"  ⚠️  Лишние: {extra}")

if __name__ == "__main__":
    main()
