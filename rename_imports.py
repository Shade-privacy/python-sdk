import os
import re
from pathlib import Path

def update_file_content(filepath):
    """Update import statements in a Python file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update import statements
    # Pattern 1: from veil_privacy import
    content = re.sub(
        r'from\s+shade_privacy(\.\w+)?\s+import',
        lambda m: f'from veil_privacy{m.group(1) or ""} import',
        content
    )
    
    # Pattern 2: import veil_privacy
    content = re.sub(
        r'import\s+shade_privacy(\.\w+)?',
        lambda m: f'import veil_privacy{m.group(1) or ""}',
        content
    )
    
    # Pattern 3: veil_privacy.something
    content = re.sub(
        r'\bshade_privacy\.',
        'veil_privacy.',
        content
    )
    
    # Pattern 4: 'veil_privacy' in strings (optional)
    content = re.sub(
        r"'veil_privacy'",
        "'veil_privacy'",
        content
    )
    
    content = re.sub(
        r'"veil_privacy"',
        '"veil_privacy"',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Process all Python files
for root, dirs, files in os.walk('.'):
    # Skip hidden directories and __pycache__
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
    
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            print(f"Updating: {filepath}")
            update_file_content(filepath)

print("Import updates completed!")
