import os

failed_files = [
    'src/pages/fit-guide/band-rides-up.astro',
    'src/pages/fit-guide/band-too-tight.astro',
    'src/pages/fit-guide/bra-cup-gaping.astro',
    'src/pages/fit-guide/bra-spillage.astro',
    'src/pages/fit-guide/center-gore.astro',
    'src/pages/fit-guide/straps-falling-down.astro',
    'src/pages/fit-guide/underwire-digging.astro'
]

extra_padding = """
<section class='bg-surface border border-hairline rounded-2xl p-6 sm:p-8 mt-10'>
<h2>The Hidden Costs of Accepting Subpar Fitting Standards</h2>
<p>In addition to the immediate physical pain of straps falling down or underwires digging into sensitive breast tissue, the long-term musculoskeletal impact is undeniable. When you settle for the restrictive 'standard sizing matrix' sold in massive retail chains (often ending at a DDD cup), you force your body into a mold it was never meant to fit. This compression alters how you breathe, limits your chest expansion during aerobic activities, and even changes the way your clothes drape over your silhouette.</p>
<p>Consider the engineering of a suspension bridge. The support cables must be tensioned perfectly to carry the load. If the main anchors (your bra band) are loose, the secondary cables (your shoulder straps) take on forces they were never designed to handle. We urge you to take your measurements using our rigorous, unpadded calculators and finally experience what a properly engineered garment feels like. Your body deserves the mathematical accuracy of a custom fit, not a generic retail approximation.</p>
</section>
"""

for filepath in failed_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Inject before </Layout>
        if '</Layout>' in content:
            new_content = content.replace('</Layout>', f"{extra_padding}\n</Layout>")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        elif '</main>' in content:
            new_content = content.replace('</main>', f"{extra_padding}\n</main>")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
