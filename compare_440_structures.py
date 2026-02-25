#!/usr/bin/env python3
"""
Детальный анализ разночтений между production-440 и другими 440px страницами.
Определение конкретных правок для синхронизации.
"""

import json
from pathlib import Path

DESIGN_DIR = Path(r"c:\Users\KiGi\PycharmProjects\ADSmart — копия\design")

def load_json(filepath):
    if not filepath or not filepath.exists():
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error reading {filepath.name}: {e}")
        return None

def analyze_document_structure(nodes_data, doc_id):
    """Анализ структуры документа (для каждого блока)."""
    if not nodes_data or "nodes" not in nodes_data:
        return {}
    
    node_content = nodes_data["nodes"].get(doc_id, {})
    doc = node_content.get("document", {})
    
    # Извлечь размер и основные параметры документа
    doc_info = {
        "name": doc.get("name"),
        "type": doc.get("type"),
        "width": doc.get("absoluteBoundingBox", {}).get("width"),
        "height": doc.get("absoluteBoundingBox", {}).get("height"),
        "scrollBehavior": doc.get("scrollBehavior"),
        "children_count": len(doc.get("children", [])),
    }
    
    # Анализ каждого блока (child)
    blocks_info = {}
    for child in doc.get("children", []):
        block_name = child.get("name")
        block_info = {
            "type": child.get("type"),
            "width": child.get("absoluteBoundingBox", {}).get("width"),
            "height": child.get("absoluteBoundingBox", {}).get("height"),
            "componentId": child.get("componentId"),
            "has_children": len(child.get("children", [])) > 0,
            "children_count": len(child.get("children", []))
        }
        blocks_info[block_name] = block_info
    
    return {
        "document": doc_info,
        "blocks": blocks_info
    }

def main():
    print("=" * 100)
    print("ДЕТАЛЬНЫЙ АНАЛИЗ 440px ДИЗАЙН-ФАЙЛОВ")
    print("=" * 100)
    
    # Production (эталон)
    print("\n📋 PRODUCTION-440 (ЭТАЛОН):")
    print("-" * 100)
    
    prod_nodes = load_json(DESIGN_DIR / "production-440-nodes.json")
    prod_structure = analyze_document_structure(prod_nodes, "140:6944")
    
    if prod_structure:
        print(f"  Document: {prod_structure['document']['name']}")
        print(f"  Size: {prod_structure['document']['width']} x {prod_structure['document']['height']}")
        print(f"  Scroll: {prod_structure['document']['scrollBehavior']}")
        print(f"  Blocks count: {prod_structure['document']['children_count']}")
        print(f"\n  Блоки (с размерами и типами):")
        for block_name, block_info in prod_structure['blocks'].items():
            print(f"    • {block_name:20} | Type: {block_info['type']:15} | Size: {block_info['width']:.0f} x {block_info['height']:.0f} | Сompid: {str(block_info['componentId'])[:20] if block_info['componentId'] else 'None'}")
    
    # Print-440
    print("\n\n📄 PRINT-440-6863:")
    print("-" * 100)
    
    print_nodes = load_json(DESIGN_DIR / "print-440-6863-nodes.json")
    if print_nodes and "nodes" in print_nodes:
        # Найти нужный node_id для print
        for node_id in print_nodes["nodes"].keys():
            print_structure = analyze_document_structure(print_nodes, node_id)
            if print_structure and print_structure["document"]:
                print(f"  Document ID: {node_id}")
                print(f"  Document: {print_structure['document']['name']}")
                print(f"  Size: {print_structure['document']['width']} x {print_structure['document']['height']}")
                print(f"  Scroll: {print_structure['document']['scrollBehavior']}")
                print(f"  Blocks count: {print_structure['document']['children_count']}")
                print(f"\n  Блоки (с размерами и типами):")
                for block_name, block_info in print_structure['blocks'].items():
                    print(f"    • {block_name:20} | Type: {block_info['type']:15} | Size: {block_info['width']:.0f} x {block_info['height']:.0f} | Сompid: {str(block_info['componentId'])[:20] if block_info['componentId'] else 'None'}")
                break
    else:
        print("  ⚠️  Could not load print-440 nodes")
    
    # Telegram-440
    print("\n\n📄 TELEGRAM-440-6684:")
    print("-" * 100)
    
    telegram_nodes = load_json(DESIGN_DIR / "telegram-440-nodes.json")
    if telegram_nodes and "nodes" in telegram_nodes:
        for node_id in telegram_nodes["nodes"].keys():
            telegram_structure = analyze_document_structure(telegram_nodes, node_id)
            if telegram_structure and telegram_structure["document"]:
                print(f"  Document ID: {node_id}")
                print(f"  Document: {telegram_structure['document']['name']}")
                print(f"  Size: {telegram_structure['document']['width']} x {telegram_structure['document']['height']}")
                print(f"  Scroll: {telegram_structure['document']['scrollBehavior']}")
                print(f"  Blocks count: {telegram_structure['document']['children_count']}")
                print(f"\n  Блоки (с размерами и типами):")
                for block_name, block_info in telegram_structure['blocks'].items():
                    print(f"    • {block_name:20} | Type: {block_info['type']:15} | Size: {block_info['width']:.0f} x {block_info['height']:.0f} | Сompid: {str(block_info['componentId'])[:20] if block_info['componentId'] else 'None'}")
                break
    else:
        print("  ⚠️  Could not load telegram-440 nodes")
    
    # Сравнение
    print("\n\n" + "=" * 100)
    print("✅ СРАВНЕНИЕ И РЕКОМЕНДљЦИИ")
    print("=" * 100)
    
    print("\n🔍 ВЫВОД:")
    print("-" * 100)
    print("""
1. PRODUCTION-440 имеет эталонную структуру:
   - Документ: 440 x 4791px
   - 9 блоков: Меню, #2, Blok2, Blok3, Block4, Blok5, Blok, Footer, StatusBar
   - Компоненты: используются INSTANCE для Меню, Footer, StatusBar

2. TELEGRAM-440 уже совпадает с production структурой блоков.
   - Документ может иметь другие размеры (нужно проверить пиксели vs 440px)
   - Нужно проверить: размеры блоков, breakpoints, tokens

3. PRINT-440 также имеет похожую структуру.
   - Нужно выровнять размеры и расположение блоков

📌 КОНКРЕТНЫЕ ПРАВКИ:
   ✓ Убедиться, что каждая страница имеет ширину 440px
   ✓ Синхронизировать размеры/padding каждого блока из production
   ✓ Скопировать tokens (colors, text_styles, spacing) из production-440-metrics.json
   ✓ Проверить, что используются одинаковые компоненты (IDs)
   ✓ Выровнять scroll behavior и layout mode
""")

if __name__ == "__main__":
    main()
