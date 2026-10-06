import os
import glob

def fix_colors(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    new_content = content.replace('bg-primary text-white', 'bg-primary text-on-primary')
    new_content = new_content.replace('bg-ink text-white', 'bg-ink text-canvas')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

for root, dirs, files in os.walk('src'):
    for file in files:
        if file.endswith('.astro') or file.endswith('.md') or file.endswith('.tsx') or file.endswith('.js'):
            fix_colors(os.path.join(root, file))
