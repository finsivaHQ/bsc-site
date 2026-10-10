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
        if in_redirects:
            if line.strip() == '},' or line.strip() == '}':
                in_redirects = False
                continue
            if ':' in line and 'destination' in line:
                source = line.split(':')[0].strip().strip("'")
                dest_match = re.search(r"destination:\s*'([^']+)'", line)
                if dest_match:
                    dest = dest_match.group(1)
                    f.write(f'{source} {dest} 301\n')
                    if not source.endswith('/'):
                        f.write(f'{source}/ {dest} 301\n')

print('Done.')
