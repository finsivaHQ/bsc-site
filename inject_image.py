import re

with open('src/pages/bra-size-chart.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Update title and H1 to include the keywords
content = content.replace(
    'title="Bra Size Chart — US, UK, EU, AU, JP, IN, HK, South Korea, SG & International Conversion Guide | BraSizeChecker"',
    'title="Visual Bra Size Chart with Pictures & International Conversion Guide | BraSizeChecker"'
)
content = content.replace(
    'Master Bra Size Chart: US, UK, EU, AU, JP, IN & International Matrix',
    'Visual Bra Size Chart with Pictures: Master International Matrix'
)

# Insert the image and a small paragraph right after the intro header
image_html = '''
        <figure class="my-10 w-full rounded-2xl overflow-hidden border border-hairline shadow-sm">
          <img 
            src="/img/bra-cup-fit-guide.jpg" 
            alt="Visual bra size chart with pictures showing realistic cup size comparisons" 
            class="w-full h-auto object-cover"
          />
          <figcaption class="p-4 bg-canvas-soft text-sm text-mute text-center border-t border-hairline">
            A visual representation of how different cup sizes look relative to band sizes.
          </figcaption>
        </figure>
'''

# Find the end of the <header> tag to insert the image
content = content.replace('      </header>', image_html + '\n      </header>')

with open('src/pages/bra-size-chart.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated bra-size-chart.astro with images and keywords.")
