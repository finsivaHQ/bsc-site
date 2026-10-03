import os
import re

filepath = 'src/pages/size/[size].astro'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

faq_schema = """
// 6-PILLAR E-E-A-T FAQ SCHEMA FOR DYNAMIC SIZE PAGES
const faqSchema = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": `Is the ${band}${cup.name} bra size considered big or small?`,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": `Cup size is entirely relative to band size. A ${band}${cup.name} holds exactly the same volume of breast tissue as a ${sisterDown ? sisterDown.band + sisterDown.cup.name : 'smaller band'} and a ${sisterUp ? sisterUp.band + sisterUp.cup.name : 'larger band'}. Therefore, a ${cup.name} cup on a ${band} band looks very different physically than it does on other bands.`
      }
    },
    {
      "@type": "Question",
      "name": `Why does my ${band}${cup.name} bra hurt my shoulders?`,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": `If your shoulders hurt, it is highly likely your ${band} band is actually too loose, or the ${cup.name} cups are too small. When the band fails to carry 80% of the bust weight securely against the ribcage, all that mechanical load transfers to your shoulder straps, digging into your trapezius muscles.`
      }
    },
    {
      "@type": "Question",
      "name": `What does a ${cup.diff}-inch overbust difference actually mean?`,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": `In modern bra sizing math, every 1-inch difference between your ribcage and the fullest part of your bust equals one cup letter. Because you measure ${band} inches underbust and ${overbust} inches overbust, the ${cup.diff}-inch mathematical delta places you precisely in the ${cup.name} cup bracket.`
      }
    },
    {
      "@type": "Question",
      "name": `Are US and UK sizes the same for a ${band}${cup.name}?`,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": `For a ${band}${cup.name} in the UK system, the exact US equivalent is a ${band}${cup.us}. While bands remain identical, US manufacturers scale their cup letters completely differently after a D cup.`
      }
    },
    {
      "@type": "Question",
      "name": `Can I wear a sister size instead of a ${band}${cup.name}?`,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": `Yes. If a ${band}${cup.name} fits perfectly in the cups but the band feels suffocatingly tight around your ribs, you should sister-size UP to a ${sisterUp ? sisterUp.band + sisterUp.cup.name : 'larger band size'}. If the cups fit but the band rides up your back, sister-size DOWN to a ${sisterDown ? sisterDown.band + sisterDown.cup.name : 'smaller band size'}.`
      }
    },
    {
      "@type": "Question",
      "name": `How do I know if my ${band}${cup.name} fits correctly?`,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": `In a properly fitted ${band}${cup.name}, the center wire gore must rest completely flat against your sternum. The underwire must encapsulate all breast tissue without sitting on top of it laterally, and the band should sit parallel to the floor without riding up your spine.`
      }
    }
  ]
};
"""

dynamic_padding = """
      <!-- 6-PILLAR HIGH-RICH CONTENT EXPANSION -->
      <section class="mt-12 space-y-8 bg-surface border border-hairline rounded-3xl p-6 md:p-10 shadow-sm">
        <h2 class="text-2xl md:text-3xl font-black text-ink">The Physical Reality of the {band}{cup.name} Bra Size</h2>
        
        <p class="text-body leading-relaxed">
          Let's be incredibly honest for a moment. If you've just discovered through our calculator that you are a <strong>{band}{cup.name}</strong>, you might be experiencing a bit of "sticker shock"—especially if retail stores have spent years trying to force you into a vastly different size. The apparel industry has unfortunately normalized discomfort, leading millions of individuals to believe that deep shoulder grooves, red marks, and the desperate urge to unhook their garment at the end of the day are simply normal parts of life. They are not.
        </p>

        <p class="text-body leading-relaxed">
          When you wear a {band}{cup.name}, it is because the specific three-dimensional geometry of your chest requires a precise mathematical container. The <strong>{band}-inch underbust band</strong> is engineered to act as a structural anchor. In a properly fitted {band}{cup.name}, this snug band wraps horizontally around the ribcage and utilizes friction to carry 80% of the weight of your breast tissue. 
        </p>

        <h3 class="text-xl font-bold text-ink mt-6">Why Your Shoulders Hurt (And How the {band}{cup.name} Fixes It)</h3>
        
        <p class="text-body leading-relaxed">
          Consider the engineering of a suspension bridge. The heavy structural load must be supported by thick, tensioned base cables. In your body, your underbust band is that primary base cable. If you have been wearing a band larger than {band}, that primary anchor is completely useless. It rides up your back, effectively transferring 100% of the heavy, cantilevered load of your bust directly onto your delicate shoulder straps. 
        </p>
        
        <p class="text-body leading-relaxed">
          This isn't just an aesthetic inconvenience. Over years, this micro-postural adjustment leads to chronic kyphosis (rounded shoulders), severe tension headaches, and deep fatigue in the upper trapezius muscles. By securing a true <strong>{band} band</strong>, you relieve your neck and shoulders of this immense burden.
        </p>

        <h3 class="text-xl font-bold text-ink mt-6">Decoding the {cup.diff}-inch Difference of the {cup.name} Cup</h3>

        <p class="text-body leading-relaxed">
          The letter "{cup.name}" is not an arbitrary label indicating "large" or "small." It is a strict mathematical variable. It simply denotes that the circumference of the fullest part of your bust (<strong>{overbust} inches</strong>) is exactly <strong>{cup.diff} inches larger</strong> than your ribcage. 
        </p>

        <p class="text-body leading-relaxed">
          This relative volume means a {cup.name} cup looks entirely different depending on the band it is attached to. The volume of breast tissue in a {band}{cup.name} is identical to the volume in a {sisterDown ? sisterDown.band + sisterDown.cup.name : 'smaller sister size'} and a {sisterUp ? sisterUp.band + sisterUp.cup.name : 'larger sister size'}. If the {band}{cup.name} cups encapsulate your tissue perfectly without spillage (quad-boob) or gaping, but the band feels suffocating, you should sister-size to the {sisterUp ? sisterUp.band + sisterUp.cup.name : 'larger band'}. If the band is loose and riding up, sister-size down to the {sisterDown ? sisterDown.band + sisterDown.cup.name : 'smaller band'}.
        </p>

        <div class="p-6 bg-primary/5 border border-primary/20 rounded-2xl my-8">
          <h4 class="font-bold text-primary mb-2">The Center Gore Check</h4>
          <p class="text-sm text-body">
            When evaluating a {band}{cup.name} underwired bra, pay absolute attention to the "center gore" (the fabric between the cups). It must tack completely flat against your sternum bone. If it floats away from your chest wall, or if the underwire sits on top of soft breast tissue laterally near your armpits, the {cup.name} cups are too small for your true volume. 
          </p>
        </div>

        <p class="text-body leading-relaxed">
          We encourage you to trust the math. Discovering your true size is a deeply validating, emotional experience. You no longer have to squeeze your body into the cheap, restricted sizing matrix of fast-fashion retailers. Your body is not wrong; the limited retail math is wrong. Embrace the tailored, ergonomic support of the {band}{cup.name}.
        </p>
      </section>

      <!-- FAQ SECTION -->
      <section class="mt-12 space-y-6">
        <h2 class="text-2xl font-bold text-ink">Frequently Asked Questions about Size {band}{cup.name}</h2>
        <div class="space-y-4">
          {faqSchema.mainEntity.map(item => (
            <details class="bg-surface border border-hairline rounded-2xl p-5 cursor-pointer group shadow-sm hover:border-primary/40 transition-colors">
              <summary class="font-bold text-ink flex justify-between items-center list-none text-sm md:text-base">
                <span>{item.name}</span>
                <span class="text-primary group-open:rotate-180 transition-transform">&darr;</span>
              </summary>
              <p class="mt-4 text-body text-sm leading-relaxed">{item.acceptedAnswer.text}</p>
            </details>
          ))}
        </div>
      </section>
"""


# 1. Inject schema right before --- in frontmatter
if 'const title = ' in content and 'faqSchema' not in content:
    content = content.replace('const title = ', f"{faq_schema}\nconst title = ")
    
# 2. Inject LD+JSON script into layout
if '<Layout' in content and 'ld+json' not in content:
    content = re.sub(r'(<Layout[^>]*>)', r'\1\n  <script type="application/ld+json" set:html={JSON.stringify(faqSchema)} />', content)
    
# 3. Inject Dynamic Padding right before closing </main>
if '</main>' in content and 'The Physical Reality' not in content:
    content = content.replace('</main>', f"{dynamic_padding}\n  </main>")
    
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

