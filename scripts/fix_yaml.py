#!/usr/bin/env python3
import os
import re

# Directory containing publications
PUBLICATION_DIR = '/Users/lingfeng/Documents/AAA_sutd_work/tump-lab.github.io-main/content/publication'

def fix_yaml_abstract(file_path):
    """Fix YAML abstract formatting in a publication index.md file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if abstract needs fixing (doesn't have | and has content on same line)
    # Pattern: abstract: <text> (without |)
    pattern = r'^abstract: ([^\|\n].+)$'
    
    match = re.search(pattern, content, re.MULTILINE)
    if match:
        abstract_text = match.group(1).strip()
        
        # Only fix if the abstract is not empty and doesn't start with |
        if abstract_text and not abstract_text.startswith('|'):
            # Replace with proper YAML format
            new_abstract = f'abstract: |\n  {abstract_text}'
            content = re.sub(pattern, new_abstract, content, flags=re.MULTILINE)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
    
    return False

def main():
    fixed_count = 0
    
    # Walk through all publication directories
    for root, dirs, files in os.walk(PUBLICATION_DIR):
        if 'index.md' in files:
            file_path = os.path.join(root, 'index.md')
            if fix_yaml_abstract(file_path):
                print(f"Fixed: {file_path}")
                fixed_count += 1
    
    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == "__main__":
    main()
