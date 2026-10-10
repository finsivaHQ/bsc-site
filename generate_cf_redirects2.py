import re
import os

with open('astro.config.mjs', 'r', encoding='utf-8') as f:
    content = f.read()

redirects_match = re.search(r'redirects:\s*\{([^}]+)\}', content)
if redirects_match:
    lines = redirects_match.group(1).splitlines()
    with open('public/_redirects', 'w', encoding='utf-8') as f:
        for line in lines:
            if ':' in line and 'destination' in line:
                source = line.split(':')[0].strip().strip("'")
                dest_match = re.search(r"destination:\s*'([^']+)'", line)
                if dest_match:
                    dest = dest_match.group(1)
                    f.write(f'{source} {dest} 301\n')
    print('Done.')
