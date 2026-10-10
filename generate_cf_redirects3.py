import re
import os

with open('astro.config.mjs', 'r', encoding='utf-8') as f:
    lines = f.readlines()

os.makedirs('public', exist_ok=True)
with open('public/_redirects', 'w', encoding='utf-8') as f:
    in_redirects = False
    for line in lines:
        if 'redirects: {' in line:
            in_redirects = True
            continue
        if in_redirects and '}' in line and not 'status: 301' in line: # crude end of block
            if line.strip() == '},':
                in_redirects = False
                continue
        if in_redirects and 'destination' in line:
            parts = line.split(': {')
            if len(parts) == 2:
                source = parts[0].strip().strip("'")
                dest_match = re.search(r"destination:\s*'([^']+)'", parts[1])
                if dest_match:
                    dest = dest_match.group(1)
                    f.write(f'{source} {dest} 301\n')
print('Done.')
