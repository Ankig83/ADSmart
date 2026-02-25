#!/usr/bin/env python3
"""
Apply all clamp() fixes to the 5 CSS files
"""

import re
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
    
    files_info = [
        ("radio-mobile-lock.css", 28),
        ("transport-mobile-lock.css", 50),
        ("billboards-mobile-lock.css", 47),
        ("stops-mobile-lock.css", 49),
        ("elevators-mobile-lock.css", 41),
    ]
    
    print("Writing fixed CSS files...\n")
    print("="*80)
    
    total_fixed = 0
    
    for filename, expected_count in files_info:
        filepath = base_path / filename
        
        # Read
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix
        fixed_content = fix_clamp_formula(content)
        
        # Verify
        matches_before = len(re.findall(r'clamp\(\d+px,\s*\d+(?:\.\d+)?vw,\s*\d+px\)', content))
        matches_after = len(re.findall(r'clamp\(\d+px,\s*\d+(?:\.\d+)?vw,\s*\d+px\)', fixed_content))
        
        # Write
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        total_fixed += matches_before
        
        print(f"✓ {filename}")
        print(f"  Patterns fixed: {matches_before} (expected {expected_count})")
        print(f"  Remaining: {matches_after}")
        print(f"  File size: {len(fixed_content):,} bytes\n")
    
    print("="*80)
    print(f"✓ ALL DONE!")
    print(f"✓ Total patterns converted: {total_fixed}")
    print(f"✓ Files updated in place")


if __name__ == "__main__":
    main()
