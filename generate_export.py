#!/usr/bin/env python3
"""
Generate exportable Python dict with all fixed CSS files
"""

import re
import json
from pathlib import Path

def fix_clamp_formula(content):
    """Convert clamp(Apx, Bvw, Cpx) → clamp(Apx, calc(X * 100vw / 440), new_Cpx)"""
    pattern = r'clamp\((\d+)px,\s*(\d+(?:\.\d+)?vw),\s*(\d+)px\)'
    
    def replacer(match):
        a = match.group(1)
        b = float(match.group(2).rstrip('vw'))
        c = int(match.group(3))
        x = round(b * 440 / 100)
        new_c = c * 2
        return f'clamp({a}px, calc({x} * 100vw / 440), {new_c}px)'
    
    return re.sub(pattern, replacer, content)


def main():
    base_path = Path(r"c:\Users\KiGi\PycharmProjects\ADSmart — копия\static\css\pages")
    
    files = [
        "radio-mobile-lock.css",
        "transport-mobile-lock.css",
        "billboards-mobile-lock.css",
        "stops-mobile-lock.css",
        "elevators-mobile-lock.css"
    ]
    
    fixed_files = {}
    
    for filename in files:
        filepath = base_path / filename
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        fixed_content = fix_clamp_formula(content)
        fixed_files[str(filepath)] = fixed_content
    
    # Export as Python code
    output_file = Path(r"c:\Users\KiGi\PycharmProjects\ADSmart — копия\fixed_clamp_files.py")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('"""Fixed clamp() formulas for all 5 mobile-lock CSS files"""\n\n')
        f.write('fixed_files = {\n')
        for filepath, content in fixed_files.items():
            # Escape special characters properly
            escaped_content = content.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")
            f.write(f"    r'{filepath}': r'{escaped_content}',\n")
        f.write('}\n\n')
        f.write('# Usage:\n')
        f.write('# for filepath, content in fixed_files.items():\n')
        f.write('#     with open(filepath, "w", encoding="utf-8") as f:\n')
        f.write('#         f.write(content)\n')
    
    print(f"✓ Exported to {output_file}")
    
    # Also print sample conversions
    print("\n" + "="*80)
    print("SAMPLE CONVERSIONS:")
    print("="*80)
    
    samples = [
        "clamp(48px, 12vw, 72px)",
        "clamp(16px, 4.5vw, 24px)",
        "clamp(32px, 8vw, 44px)",
        "clamp(20px, 5.5vw, 28px)",
    ]
    
    for sample in samples:
        fixed = fix_clamp_formula(sample)
        print(f"  {sample:35} → {fixed}")
    
    print("\n" + "="*80)
    print("WRITE FIXED FILES (Python snippet):")
    print("="*80 + "\n")
    print("""
from fixed_clamp_files import fixed_files

for filepath, content in fixed_files.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Written {filepath}")
""")


if __name__ == "__main__":
    main()
