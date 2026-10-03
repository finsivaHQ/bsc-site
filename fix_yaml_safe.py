import os
import glob
import re

for filepath in glob.glob('src/content/blog/*.md'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if content.startswith('faqs:\n') or content.startswith('\nfaqs:\n'):
        # Clean it up. 
        # Structure is:
        # faqs: ... 
        # ---
        # title: ...
        # faqs: ...
        # ---
        
        # Split by ---
        parts = content.split('---')
        
        # parts[0] is the stray faqs block at the start
        # parts[1] is the actual core yaml (which has the second faqs block)
        # parts[2:] is the massive markdown body (which might contain --- inside it)
        
        core_yaml = parts[1].strip()
        body = "---".join(parts[2:]).strip()
        
        clean_content = f"---\n{core_yaml}\n---\n\n{body}\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(clean_content)
        print(f"Properly fixed {filepath}")
