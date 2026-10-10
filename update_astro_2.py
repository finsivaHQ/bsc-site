import re

with open('astro.config.mjs', 'r', encoding='utf-8') as f:
    content = f.read()

new_redirects = """    '/blog/comprehensive-global-bra-size-comparison/': { status: 301, destination: '/bra-size-converter/' },
    '/blog/how-to-fit-someone-for-a-bra-professional-guide/': { status: 301, destination: '/how-to-measure/' },
    '/blog/measuring-cup-size-inches-vs-centimeters/': { status: 301, destination: '/how-to-measure/' },
    '/blog/how-to-tell-if-your-bra-is-too-small-signs/': { status: 301, destination: '/fit-guide/' },
    '/blog/convert-french-italian-bra-sizes-to-us-uk/': { status: 301, destination: '/eu-bra-size-guide/' },
"""

content = content.replace("redirects: {", "redirects: {\n" + new_redirects)

with open('astro.config.mjs', 'w', encoding='utf-8') as f:
    f.write(content)
