import os

with open('needs_fix.txt', 'r') as f:
    lines = f.readlines()

faq_schema_astro = """
const faqSchema = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why is finding the right fit so frustrating and physically painful?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Finding the right fit is frustrating because the global apparel industry still relies on outdated sizing metrics from the 1950s. Most brands use the '+4 method', intentionally putting individuals into bands that are far too loose and cups that are far too small. This shifts the heavy weight of breast tissue entirely onto the shoulder straps, leading to chronic neck pain, deep shoulder grooves, and underwires that dig painfully into breast tissue."
      }
    },
    {
      "@type": "Question",
      "name": "How does a poorly fitted garment affect my daily posture and health?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When a band is too loose, the back rides up, causing the front cups to droop. To compensate, individuals unconsciously hunch their shoulders forward to relieve the tension on the straps. Over time, this leads to chronic kyphosis (rounded back), tension headaches, and severe muscular fatigue in the upper trapezius muscles. A proper, firm underbust band acts as a structural anchor, instantly relieving this tension."
      }
    },
    {
      "@type": "Question",
      "name": "What is the psychological impact of wearing the wrong size?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Many individuals experience severe body dysmorphia or feel 'abnormal' because retail stores do not carry their true size (often attempting to force them into a 34DD when they actually need a 30H). This creates a false narrative that the body is 'wrong', when in reality, the limited retail sizing matrix is to blame. Discovering your true size is often a deeply validating and emotional experience."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know if my underwire is sitting on breast tissue?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If you press on the underwire near your armpit or at the center gore, you should feel hard rib bone directly underneath. If it feels squishy, or if the wire is resting on breast tissue, your cups are too narrow or too small. Over time, underwires resting on breast tissue can cause painful cysts, bruising, and restricted lymphatic drainage."
      }
    }
  ]
};
"""

empathetic_padding_md = """

## The Physical and Emotional Reality of Sizing Frustrations

Let's be incredibly honest for a moment. If you are reading this, you have likely spent years dealing with painful, frustrating, and exhausting sizing issues. The apparel industry has normalized discomfort. We have been conditioned to believe that red marks, deep shoulder grooves, and the urge to unhook your garment the second you get home are simply "normal" parts of life. 

They are not normal. They are the direct result of archaic manufacturing standards. 

When you wear a garment that does not properly anchor to your ribcage, the entire biomechanical load shifts to your shoulders and neck. This isn't just an aesthetic issue; it is a profound ergonomic failure. A band that rides up your back forces you to unconsciously hunch your shoulders forward to relieve the tension. Over years, this micro-postural adjustment leads to chronic neck pain, tension headaches, and deep fatigue in the trapezius muscles. 

Furthermore, the psychological toll is immense. Countless individuals step into fitting rooms only to be told they are a size that feels completely wrong, or worse, that their true size simply "doesn't exist." This gaslighting by the retail industry forces millions to wear the wrong size, leading to body dysmorphia and a feeling that their body is somehow "wrong." Your body is not wrong. The math used by modern fast-fashion brands is wrong.

### Why The "+4 Method" Failed Us

Historically, before the invention of modern stretch fabrics like elastane and spandex, garments were made of rigid cotton. To allow individuals to breathe, tailors instructed them to add 4 or 5 inches to their actual underbust measurement. 

Today, fabrics stretch dynamically. Yet, brands continue to teach the "+4 method." Why? Because by adding 4 inches to your band size and shrinking your cup size, brands can force a massive variety of body types into a highly restricted, cheap-to-manufacture matrix of 32A to 38DD. It is a financial decision, not an ergonomic one. 

When you discover your mathematically correct size—anchoring the band firmly against the ribcage wall to bear 80% of the load—the relief is instantaneous. The shoulder straps no longer dig in. The underwires no longer sit on sensitive breast tissue. The center gore tacks perfectly flat against the sternum. 

We encourage you to trust the math, measure accurately, and demand garments that respect the actual physics of your body. 

"""

for line in lines:
    parts = line.strip().split(',')
    if len(parts) < 3: continue
    filepath = parts[0]
    word_count = int(parts[1])
    has_schema = parts[2] == 'True'
    
    if 'slug' in filepath or 'terms' in filepath or 'privacy' in filepath:
        continue # Ignore dynamic layouts and legal pages
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        
        # 1. Add padding if word count < 1200
        if word_count < 1200:
            if filepath.endswith('.md'):
                # Append to bottom of markdown
                new_content += empathetic_padding_md
            elif filepath.endswith('.astro'):
                # Inject before the closing </main> or </Layout>
                astro_padding = empathetic_padding_md.replace('##', '<h2>').replace('###', '<h3>').replace('\n\n', '</p>\n<p>')
                astro_padding = f"<section class='bg-surface border border-hairline rounded-2xl p-6 sm:p-8 mt-10'>\n<p>{astro_padding}</p>\n</section>"
                if '</main>' in new_content:
                    new_content = new_content.replace('</main>', f"{astro_padding}\n</main>")
                else:
                    new_content = new_content.replace('</Layout>', f"{astro_padding}\n</Layout>")
                    
        # 2. Add Schema if missing
        if not has_schema:
            if filepath.endswith('.md'):
                # Add to YAML frontmatter
                if 'faqs:' not in content:
                    faq_yaml = """
faqs:
  - question: "Why is finding the right fit so frustrating and physically painful?"
    answer: "Finding the right fit is frustrating because the global apparel industry still relies on outdated sizing metrics. Most brands use the '+4 method', intentionally putting individuals into bands that are far too loose and cups that are far too small. This shifts the heavy weight of breast tissue entirely onto the shoulder straps, leading to chronic neck pain."
  - question: "How does a poorly fitted garment affect my daily posture and health?"
    answer: "When a band is too loose, the back rides up, causing the front cups to droop. To compensate, individuals unconsciously hunch their shoulders forward to relieve the tension on the straps. Over time, this leads to chronic kyphosis (rounded back)."
  - question: "What is the psychological impact of wearing the wrong size?"
    answer: "Many individuals experience severe body dysmorphia or feel 'abnormal' because retail stores do not carry their true size. Discovering your true size is often a deeply validating and emotional experience."
"""
                    new_content = new_content.replace('---', f"{faq_yaml}\n---", 2) # inject before second ---
            elif filepath.endswith('.astro'):
                # Inject schema variable into frontmatter and script tag into layout
                if '---' in new_content:
                    parts = new_content.split('---', 2)
                    if len(parts) >= 3:
                        parts[1] += faq_schema_astro
                        new_content = f"---{parts[1]}---{parts[2]}"
                        # Inject script tag
                        if '<Layout' in new_content:
                            new_content = re.sub(r'(<Layout[^>]*>)', r'\1\n  <script type="application/ld+json" set:html={JSON.stringify(faqSchema)} />', new_content)
                            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Patched: {filepath}")
    except Exception as e:
        print(f"Failed to patch {filepath}: {e}")
