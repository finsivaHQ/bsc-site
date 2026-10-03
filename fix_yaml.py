import os
import glob
import re

for filepath in glob.glob('src/content/blog/*.md'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if content.startswith('\nfaqs:') or content.startswith('faqs:'):
        # The file was corrupted by the bad patch script.
        # It looks like:
        # \nfaqs:... \n---\ntitle: ... \n\nfaqs: ... \n---
        # Let's completely extract just the standard frontmatter lines
        
        # find the title: description: etc block
        match = re.search(r'(title:.*?)(\nfaqs:)', content, re.DOTALL)
        if match:
            core_yaml = match.group(1)
            # The second faq block
            faq_block = match.group(2) + content[match.end(2):].split('---')[0]
            
            # Reconstruct the file safely
            rest_of_file = content.split('---')[-1] # Everything after the last ---
            
            clean_content = f"---\n{core_yaml}{faq_block}---\n{rest_of_file}"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(clean_content)
            print(f"Fixed {filepath}")
