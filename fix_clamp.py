#!/usr/bin/env python3
"""
Fix clamp() formulas in mobile-lock CSS files.
Converts: clamp(Apx, Bvw, Cpx) → clamp(Apx, calc(X * 100vw / 440), new_Cpx)
Where: X = round(B * 440 / 100), new_Cpx = C * 2
"""

import re
from pathlib import Path

def fix_clamp_formula(content):
    """
    Converts clamp(Apx, Bvw, Cpx) to clamp(Apx, calc(X * 100vw / 440), new_Cpx)
    """
    # Pattern to match clamp(Apx, Bvw, Cpx)
    pattern = r'clamp\((\d+)px,\s*(\d+(?:\.\d+)?vw),\s*(\d+)px\)'
    
    def replacer(match):
        a = match.group(1)  # min value in px
        b = float(match.group(2).rstrip('vw'))  # vw percentage as float
        c = int(match.group(3))  # max value in px
        
        # Calculate X = round(B * 440 / 100)
        x = round(b * 440 / 100)
        # Calculate new max = C * 2
        new_c = c * 2
        
        return f'clamp({a}px, calc({x} * 100vw / 440), {new_c}px)'
    
    return re.sub(pattern, replacer, content)


def process_files():
    """Process all 5 mobile-lock CSS files"""
    base_path = Path(r"c:\Users\KiGi\PycharmProjects\ADSmart — копия\static\css\pages")
    
    files = [
        "radio-mobile-lock.css",
        "transport-mobile-lock.css",
        "billboards-mobile-lock.css",
        "stops-mobile-lock.css",
        "elevators-mobile-lock.css"
    ]
    
    results = {}
    
    for filename in files:
        filepath = base_path / filename
        print(f"Processing {filename}...")
        
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count matches before
        matches = re.findall(r'clamp\(\d+px,\s*\d+(?:\.\d+)?vw,\s*\d+px\)', content)
        print(f"  Found {len(matches)} clamp(px, vw, px) patterns")
        
        # Fix formulas
        fixed_content = fix_clamp_formula(content)
        
        # Count matches after
        remaining = re.findall(r'clamp\(\d+px,\s*\d+(?:\.\d+)?vw,\s*\d+px\)', fixed_content)
        print(f"  Remaining: {len(remaining)} clamp(px, vw, px) patterns")
        
        results[str(filepath)] = fixed_content
        print(f"  ✓ Fixed\n")
    
    return results


if __name__ == "__main__":
    fixed_files = process_files()
    
    # Print as Python dict for easy import/writing
    print("\n" + "="*80)
    print("RESULTS DICT (ready to import):")
    print("="*80 + "\n")
    
    # Create a simplified dict for display
    output_dict = {}
    for filepath, content in fixed_files.items():
        # Show first 500 chars of each file
        output_dict[filepath] = f"[{len(content)} chars] - Fixed content ready"
    
    print(output_dict)
    print(f"\nTotal files processed: {len(fixed_files)}")
    
    # Also print the actual dict for writing to files
    print("\n" + "="*80)
    print("PYTHON DICT (to write files):")
    print("="*80 + "\n")
    
    import pprint
    # Don't print full content, just structure
    print("fixed_files = {")
    for filepath in fixed_files.keys():
        print(f"    r'{filepath}': '...content...',")
    print("}")
    
    # Return the dict for further use
    print("\n✓ All files processed successfully!")
    print(f"✓ Total files: {len(fixed_files)}")
