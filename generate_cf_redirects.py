import re
import os

with open('astro.config.mjs', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the missing comma
content = content.replace(
    "'/blog/bra-fitting-guide-how-it-should-fit': { status: 301, destination: '/fit-guide/' }\n\n    '/blog/bra-size-chart-with-pictures-explained'",
    "'/blog/bra-fitting-guide-how-it-should-fit': { status: 301, destination: '/fit-guide/' },\n\n    '/blog/bra-size-chart-with-pictures-explained'"
)

with open('astro.config.mjs', 'w', encoding='utf-8') as f:
    f.write(content)

# Extract redirects to public/_redirects
redirects_match = re.search(r'redirects:\s*\{([^}]+)\}', content)
if redirects_match:
    os.makedirs('public', exist_ok=True)
    with open('public/_redirects', 'w', encoding='utf-8') as f:
        lines = redirects_match.group(1).split('\n')
        for line in lines:
            if ':' in line and 'destination' in line:
                source = line.split(':')[0].strip().strip("'")
                dest_match = re.search(r"destination:\s*'([^']+)'", line)
                if dest_match:
                    dest = dest_match.group(1)
                    f.write(f"{source} {dest} 301\n")
    print('Generated public/_redirects successfully.')
else:
    print('Failed to parse redirects.')
