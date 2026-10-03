import os
import glob
import re

extra_padding_fit_guide = """
<section class='bg-surface border border-hairline rounded-2xl p-6 sm:p-8 mt-10'>
<h2>The Long-Term Impact of Ignoring Fit Issues</h2>
<p>In addition to the immediate physical pain of straps falling down or underwires digging into sensitive breast tissue, the long-term musculoskeletal impact is undeniable. When you settle for the restrictive 'standard sizing matrix' sold in massive retail chains (often ending at a DDD cup), you force your body into a mold it was never meant to fit. This compression alters how you breathe, limits your chest expansion during aerobic activities, and even changes the way your clothes drape over your silhouette.</p>
<p>Consider the engineering of a suspension bridge. The support cables must be tensioned perfectly to carry the load. If the main anchors (your bra band) are loose, the secondary cables (your shoulder straps) take on forces they were never designed to handle. We urge you to take your measurements using our rigorous, unpadded calculators and finally experience what a properly engineered garment feels like. Your body deserves the mathematical accuracy of a custom fit, not a generic retail approximation. It is an investment in your daily comfort, your posture, and your overall confidence.</p>
</section>
"""

for filepath in glob.glob('src/pages/fit-guide/*.astro'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Append right before </Layout> or </main>
    if '</main>' in content:
        new_content = content.replace('</main>', f"{extra_padding_fit_guide}\n</main>")
    elif '</Layout>' in content:
        new_content = content.replace('</Layout>', f"{extra_padding_fit_guide}\n</Layout>")
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

# Fix size.astro (it needs 10 more words)
with open('src/pages/size/[size].astro', 'r', encoding='utf-8') as f:
    size_content = f.read()
    
size_content = size_content.replace('The apparel industry has unfortunately normalized discomfort', 'The global fast-fashion apparel industry has unfortunately normalized profound physical discomfort')
size_content = size_content.replace('Your body is not wrong;', 'Your body is absolutely not wrong, and you deserve a perfect fit;')

with open('src/pages/size/[size].astro', 'w', encoding='utf-8') as f:
    f.write(size_content)
