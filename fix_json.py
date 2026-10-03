import os
import re

astro_dir = 'src/pages'

for root, _, files in os.walk(astro_dir):
    for file in files:
        if file.endswith('.astro'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple regex to fix missing commas between JSON objects in mainEntity array
            # Looks for `} \s* {` and replaces with `}, {`
            fixed_content = re.sub(r'\}\s*\{', '},\n    {', content)
            
            # Also fix `} \s* ]` -> `} ]` if any trailing commas exist, etc. (not strictly necessary for JSON in JS but good practice)
            
            if content != fixed_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                print(f"Fixed missing commas in {filepath}")
