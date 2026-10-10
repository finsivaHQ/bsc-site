with open('astro.config.mjs', 'r', encoding='utf-8') as f:
    content = f.read()

new_redirects = """    '/blog/ultimate-international-bra-size-converter-guide/': { status: 301, destination: '/bra-size-converter/' },
    '/blog/sister-sizes-explained/': { status: 301, destination: '/sister-size-calculator/' },
    '/blog/complete-sister-bra-size-chart-every-band-size/': { status: 301, destination: '/sister-size-calculator/' },
    '/blog/complete-guide-to-uk-sister-sizes/': { status: 301, destination: '/sister-size-calculator/' },
    '/blog/visual-bra-size-chart-with-pictures/': { status: 301, destination: '/bra-size-chart/' },
    '/blog/ultimate-boob-size-chart-guide/': { status: 301, destination: '/bra-size-chart/' },
    '/blog/a-bra-that-fits-calculator-guide/': { status: 301, destination: '/' },
    '/blog/are-bra-size-calculators-accurate/': { status: 301, destination: '/' },
    '/blog/troubleshooting-fit-bra-band-too-tight/': { status: 301, destination: '/fit-guide/band-too-tight/' },
    '/blog/bra-center-gore-not-laying-flat/': { status: 301, destination: '/fit-guide/center-gore/' },
    '/blog/fixing-cup-spillage-boobs-falling-out/': { status: 301, destination: '/fit-guide/bra-spillage/' },
    '/blog/underwire-sitting-on-breast-tissue-visual-guide/': { status: 301, destination: '/fit-guide/underwire-digging/' },
    '/blog/decoding-bra-measurements-band-vs-cup/': { status: 301, destination: '/how-to-measure/' },
    '/blog/determining-bra-cup-size-mathematics/': { status: 301, destination: '/guides/how-cup-sizes-work/' },
"""

content = content.replace("redirects: {", "redirects: {\n" + new_redirects)

with open('astro.config.mjs', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected redirects into BSC")
