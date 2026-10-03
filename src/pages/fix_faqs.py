import json
import re

files = [
    r'd:\TOOLS WEB TOOLS\bsc calculator site\src\pages\bra-size-chart.astro',
    r'd:\TOOLS WEB TOOLS\bsc calculator site\src\pages\bra-size-converter.astro',
    r'd:\TOOLS WEB TOOLS\bsc calculator site\src\pages\eu-bra-size-guide.astro',
    r'd:\TOOLS WEB TOOLS\bsc calculator site\src\pages\uk-bra-size-guide.astro'
]

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

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    faq_addition_str = ',\n    ' + ',\n    '.join([json.dumps(faq) for faq in faq_additions])
    
    if len(re.findall(r'Why do my bra straps keep falling down', content)) == 0:
        # replace the last element's closing brace and the end of the array
        # look for "    }\n  ]\n};"
        new_content = content.replace('    }\n  ]\n};', '    }' + faq_addition_str + '\n  ]\n};')
        if new_content == content:
            # Maybe windows line endings?
            new_content = content.replace('    }\r\n  ]\r\n};', '    }' + faq_addition_str + '\r\n  ]\r\n};')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
