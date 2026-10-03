import json
import re

files = [
    r'd:\TOOLS WEB TOOLS\bsc calculator site\src\pages\bra-size-chart.astro',
    r'd:\TOOLS WEB TOOLS\bsc calculator site\src\pages\bra-size-converter.astro',
    r'd:\TOOLS WEB TOOLS\bsc calculator site\src\pages\eu-bra-size-guide.astro',
    r'd:\TOOLS WEB TOOLS\bsc calculator site\src\pages\uk-bra-size-guide.astro'
]

empathy_text_pre = """
      <p class="text-base sm:text-lg text-body leading-relaxed max-w-3xl mb-6">
        For years, women have silently endured the physical and emotional toll of wearing the wrong bra size. The pinching, the digging underwires, the straps that perpetually slip down your shoulders, and that inescapable feeling of restriction—it is a frustration that transcends borders. If you have ever felt a burning ache in your shoulders after a long day at work, or found deep red indentations along your ribcage the moment you take your bra off, you are intimately familiar with the struggle. This isn't just about fashion; it is about your daily comfort, your posture, and your overall well-being. Finding a bra that truly fits shouldn't feel like deciphering an ancient, unsolvable puzzle, yet the chaotic landscape of international sizing often makes it seem exactly like that.
      </p>
      <p class="text-base sm:text-lg text-body leading-relaxed max-w-3xl mb-6">
        We understand the exhaustion of ordering what you think is your size, only to have it arrive and fit completely differently from the bra you bought just weeks prior. You might be a 34DD in a US brand, but suddenly find yourself spilling out of a French 90E, or swimming in a UK 34E. It’s enough to make anyone want to give up and settle for "good enough." But you deserve better than "good enough." You deserve a garment that supports you seamlessly, distributing weight evenly across your torso rather than placing the entire burden on your delicate shoulder muscles. A well-fitted bra can alleviate chronic back pain, improve your posture, and give you the confidence to move freely throughout your day without constantly adjusting your undergarments.
      </p>
      <p class="text-base sm:text-lg text-body leading-relaxed max-w-3xl mb-6">
        This is why we have meticulously compiled this comprehensive guide and sizing matrix. We believe that knowledge is power, and by demystifying the complex world of international bra sizing, we aim to empower you to make informed, confident choices. Whether you are shopping for a delicate lace bralette from a boutique in Paris, a highly structured sports bra from the UK, or a comfortable everyday t-shirt bra from an American retailer, understanding how your measurements translate across different regional standards is the key to unlocking true comfort. 
      </p>
      <p class="text-base sm:text-lg text-body leading-relaxed max-w-3xl mb-6">
        Before diving into the charts and converters, it is absolutely crucial that you start with accurate baseline measurements. If you haven't measured yourself recently—and by recently, we mean within the last six months—we strongly encourage you to visit our comprehensive <a href="/how-to-measure/" class="text-primary hover:underline">How to Measure Guide</a>. Our bodies are dynamic and constantly evolving; factors such as weight fluctuation, hormonal changes, pregnancy, and simple aging can all impact your breast tissue and ribcage dimensions. Relying on a measurement taken three years ago is a guaranteed recipe for a poor fit. Once you have your current, precise measurements in both inches and centimeters, you can use the tools provided here to seamlessly translate your size across any global standard. For a deeper understanding of how a bra should actually sit on your body, check out our <a href="/fit-guide/" class="text-primary hover:underline">Ultimate Fit Guide</a>.
      </p>
"""

empathy_text_post = """
      <section class="bg-surface border border-hairline rounded-2xl p-6 sm:p-8 mt-10">
        <h2 class="text-xl sm:text-2xl font-bold text-ink mb-4">The Physical Impact of a Poorly Fitted Bra</h2>
        <p class="mb-4">
          It is a startling reality that the majority of women are currently wearing the wrong bra size. The consequences of this go far beyond mere aesthetics. A poorly fitted bra can lead to a cascade of physical ailments that many women accept as a normal part of life, completely unaware that their undergarments are the root cause. When a band is too loose, it fails to provide the necessary support, forcing the shoulder straps to carry the weight of the breasts. Over time, this constant downward pressure can lead to deep grooving in the shoulders, chronic neck tension, and persistent upper back pain. It can even contribute to poor posture, as the body instinctively hunches forward to relieve the strain.
        </p>
        <p class="mb-4">
          Conversely, a band that is excessively tight restricts breathing, causes painful friction against the skin, and can even impede healthy circulation. The underwires, which are designed to sit flush against the ribcage and encapsulate the breast tissue, can become instruments of torture if the cup size is incorrect. Cups that are too small force the underwires to sit on top of the delicate breast tissue, causing painful bruising, digging, and the dreaded "quad-boob" effect. Cups that are too large fail to provide adequate containment, leading to uncomfortable shifting and chafing throughout the day.
        </p>
        <p class="mb-4">
          By taking the time to understand your true size and how it translates across different brands and regions, you are investing in your own health and comfort. You are saying no to the normalized pain of a poorly fitted bra and demanding undergarments that work with your body, not against it. We know that the journey to finding the perfect fit can be frustrating, involving trial and error, multiple returns, and moments of exasperation. But we assure you, the moment you put on a bra that fits perfectly—a bra that feels like a second skin, supporting you effortlessly and painlessly—it will all be worth it. If you are still unsure about your size or experiencing persistent fit issues, our <a href="/fit-guide/" class="text-primary hover:underline">Fit Guide</a> offers detailed troubleshooting advice to help you pinpoint exactly where your current bras are failing you.
        </p>
        <p class="mb-4">
          Remember, your bra size is just a number and a letter—a starting point, a tool to help you navigate the vast and often confusing world of lingerie. It does not define you, and it certainly shouldn't dictate your comfort. Embrace the process, be patient with yourself, and don't hesitate to utilize all the resources we have provided, from our precise <a href="/how-to-measure/" class="text-primary hover:underline">measurement instructions</a> to our dynamic converters and comprehensive charts. True comfort is achievable, and it starts with understanding the unique needs of your own body.
        </p>
      </section>
"""

faq_additions = [
    {
      "@type": "Question",
      "name": "Why do my bra straps keep falling down even when tightened?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Straps constantly slipping off your shoulders is a classic sign that your bra band is too large. When the band is too loose, the straps are set too far apart for your frame and cannot maintain tension. We recommend checking your underbust measurement with our <a href='/how-to-measure/'>How to Measure Guide</a> to ensure you're in the right band size."
      }
    },
    {
      "@type": "Question",
      "name": "What causes the underwire to dig into my ribs or armpits?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Underwire digging is usually caused by wearing a cup size that is too small or a band that is too tight. If the cups are too small, the wire sits on breast tissue instead of your ribcage. If the band is too tight, it pulls the wires uncomfortably hard against your body. Review our <a href='/fit-guide/'>Fit Guide</a> for more details."
      }
    },
    {
      "@type": "Question",
      "name": "How often should I measure my bra size?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You should measure your bra size every 6 months, or whenever you experience significant weight changes, hormonal shifts, or pregnancy. Breast tissue changes naturally over time, and a size that fit perfectly a year ago may no longer provide the necessary support."
      }
    },
    {
      "@type": "Question",
      "name": "What does 'sister sizing' mean and how do I use it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sister sizes are bra sizes that hold the same cup volume but have different band sizes. If you go up a band size, you must go down a cup letter to maintain the same volume (e.g., a 34C holds the same volume as a 36B). This is incredibly helpful when a specific brand runs tight or loose."
      }
    },
    {
      "@type": "Question",
      "name": "Why do bras from different brands fit differently even if they are the same size?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Different brands use different fit models and grading rules. Additionally, international sizing standards vary wildly. A US 34G is vastly different from a UK 34G. Always cross-reference the brand's country of origin using our converter tools before purchasing."
      }
    },
    {
      "@type": "Question",
      "name": "Can wearing the wrong bra size cause back pain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. If your bra band is too loose, your shoulder straps bear the weight of your breasts, leading to neck, shoulder, and back pain. The band should provide 80% of the support, not the straps."
      }
    }
]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add FAQs
    try:
        faq_start = content.find('const faqSchema = {')
        faq_end = content.find('};\n---', faq_start) + 1
        
        # we can just use string replacement to insert the new FAQs before the last ]
        import json
        faq_addition_str = ',\n    ' + ',\n    '.join([json.dumps(faq) for faq in faq_additions])
        new_content = content[:faq_end].replace('    }\n  ]\n};', '    }' + faq_addition_str + '\n  ]\n};') + content[faq_end:]
    except Exception as e:
        print(f'Error processing FAQs in {filepath}: {e}')
        new_content = content
        
    # Find the header section to append empathy text
    header_end = new_content.find('</header>')
    if header_end != -1:
        new_content = new_content[:header_end] + '\n' + empathy_text_pre + '\n' + new_content[header_end:]
        
    # Find the Educational Sections to prepend the post empathy text
    ed_start = new_content.find('<!-- Educational Sections -->')
    if ed_start != -1:
        # insert right after the opening div of educational sections
        div_start = new_content.find('<div', ed_start)
        div_end = new_content.find('>', div_start) + 1
        new_content = new_content[:div_end] + '\n' + empathy_text_post + '\n' + new_content[div_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

for file in files:
    process_file(file)

print('All 4 files processed.')
