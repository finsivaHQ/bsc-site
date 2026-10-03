import os
import glob
import re

astro_padding_clean = """
<section class='bg-surface border border-hairline rounded-2xl p-6 sm:p-8 mt-10'>
<h2>The Physical and Emotional Reality of Sizing Frustrations</h2>
<p>Let's be incredibly honest for a moment. If you are reading this, you have likely spent years dealing with painful, frustrating, and exhausting sizing issues. The apparel industry has normalized discomfort. We have been conditioned to believe that red marks, deep shoulder grooves, and the urge to unhook your garment the second you get home are simply "normal" parts of life.</p>
<p>They are not normal. They are the direct result of archaic manufacturing standards.</p>
<p>When you wear a garment that does not properly anchor to your ribcage, the entire biomechanical load shifts to your shoulders and neck. This isn't just an aesthetic issue; it is a profound ergonomic failure. A band that rides up your back forces you to unconsciously hunch your shoulders forward to relieve the tension. Over years, this micro-postural adjustment leads to chronic neck pain, tension headaches, and deep fatigue in the trapezius muscles.</p>
<p>Furthermore, the psychological toll is immense. Countless individuals step into fitting rooms only to be told they are a size that feels completely wrong, or worse, that their true size simply "doesn't exist." This gaslighting by the retail industry forces millions to wear the wrong size, leading to body dysmorphia and a feeling that their body is somehow "wrong." Your body is not wrong. The math used by modern fast-fashion brands is wrong.</p>
<h3>Why The "+4 Method" Failed Us</h3>
<p>Historically, before the invention of modern stretch fabrics like elastane and spandex, garments were made of rigid cotton. To allow individuals to breathe, tailors instructed them to add 4 or 5 inches to their actual underbust measurement.</p>
<p>Today, fabrics stretch dynamically. Yet, brands continue to teach the "+4 method." Why? Because by adding 4 inches to your band size and shrinking your cup size, brands can force a massive variety of body types into a highly restricted, cheap-to-manufacture matrix of 32A to 38DD. It is a financial decision, not an ergonomic one.</p>
<p>When you discover your mathematically correct size—anchoring the band firmly against the ribcage wall to bear 80% of the load—the relief is instantaneous. The shoulder straps no longer dig in. The underwires no longer sit on sensitive breast tissue. The center gore tacks perfectly flat against the sternum.</p>
<p>We encourage you to trust the math, measure accurately, and demand garments that respect the actual physics of your body.</p>
</section>
"""

for filepath in glob.glob('src/pages/fit-guide/*.astro'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip the corrupted section out completely by looking for the start of it
    if "<section class='bg-surface border border-hairline rounded-2xl p-6 sm:p-8 mt-10'>" in content:
        parts = content.split("<section class='bg-surface border border-hairline rounded-2xl p-6 sm:p-8 mt-10'>")
        # Keep everything before the FIRST occurrence
        clean_base = parts[0]
        # Then append the closing tag (either </main> or </Layout> whichever was at the bottom)
        if '</main>' in content:
            new_content = clean_base + astro_padding_clean + "\n</main>\n</Layout>"
        else:
            new_content = clean_base + astro_padding_clean + "\n</Layout>"
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
