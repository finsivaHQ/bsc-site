const fs = require('fs');
const path = require('path');

const files = [
  'bra-size-chart.astro',
  'bra-size-converter.astro',
  'eu-bra-size-guide.astro',
  'uk-bra-size-guide.astro'
];

const faqs = {
  'bra-size-chart.astro': [
    { q: "How do I read an international bra size chart?", a: "Locate your snug underbust measurement in either inches or centimeters on the band matrix row. This reveals your equivalent band size across regions (e.g. 34 in US/UK = 75 in EU = 90 in FR = 12 in AU). Next, locate your bust-to-band delta in the cup matrix to find your regional cup letter. Taking the time to cross-reference both matrices ensures you account for brand-specific sizing nuances, ultimately preventing the discomfort of wires digging into your ribs or cups gaping at the top." },
    { q: "Why do Asian bra sizes (Japan, Hong Kong, Korea, Singapore) use metric band numbers?", a: "Asian bra sizing systems (such as Japan JIS L 4006 and South Korea KS K 9404) follow metric EN 13402 specifications, using underbust centimeters for band numbers (65, 70, 75, 80) and 2.5 cm cup delta increments. This metric approach is often considered more precise than imperial inches, providing a tighter, more customized fit that accommodates narrower ribcages frequently found in Asian demographics." },
    { q: "Why do my bra sizes differ so much between US and UK brands?", a: "The primary difference lies in cup volume progression. While US brands use single letters or inconsistent multi-D systems (like DDD or G), UK brands follow a strict double-letter progression (DD, E, F, FF, G). This means a US 'H' cup is significantly smaller than a UK 'H' cup, leading to massive fit issues if you don't convert properly." },
    { q: "How do I know if the bra size chart is accurate for my body type?", a: "Bra size charts provide a statistical baseline, but breast root width, projection, and tissue density play massive roles in how a bra fits. If you have narrow roots and projected tissue, you might need a deeper cup than the chart suggests. Always use charts as a starting point and adjust based on how the underwire encapsulates your breast tissue." },
    { q: "What should I do if my measurements put me between two band sizes?", a: "If you measure between band sizes (e.g., exactly 31 inches), consider your ribcage padding and the brand's stretch profile. Those with less natural padding around the ribs often prefer sizing up for comfort to prevent the band from digging painfully into the skin, while those with more squish might prefer the tighter band for superior support." },
    { q: "Does the size chart account for sister sizing?", a: "Standard size charts map direct conversions, but sister sizing (e.g., 34C to 36B) is crucial when navigating international brands that run firm or loose. If an EU brand's band feels excruciatingly tight, you must sister size up in the band and down in the cup to maintain the exact same cup volume while relieving rib pressure." },
    { q: "How often should I re-measure myself against the bra size chart?", a: "Your breast size and ribcage circumference fluctuate due to hormonal shifts, weight changes, aging, and pregnancy. We recommend consulting the bra size chart every six months. Wearing a bra that fit you perfectly three years ago is a common recipe for shoulder grooves, neck tension, and inadequate support today." },
    { q: "Why do French (FR) and EU sizes have different band numbers if they are both metric?", a: "French bra sizing adds a +15 cm offset to the standard EU metric band number. So an EU 75 band is labeled as a FR 90. The physical garment is identical in length; the difference is purely historical and categorical, which causes immense confusion for shoppers buying imported European lingerie." }
  ],
  'bra-size-converter.astro': [
    { q: "How do I convert my bra size between US and UK sizing?", a: "For band sizes, US and UK numbers are 100% identical (30, 32, 34, 36, 38). For cup sizes, US and UK match up to D cup. For cups larger than D, UK uses double-letter progression (DD, E, F, FF, G, GG) while US uses single letters or multi-D notation (DD, DDD, G, H, I)." },
    { q: "How do I convert a US/UK bra band size to European (EU) sizing?", a: "To convert a US/UK inch band to EU metric band, multiply the inch band by 2.54 and round to the nearest multiple of 5 cm (e.g. 30 in = 65 EU, 32 in = 70 EU, 34 in = 75 EU, 36 in = 80 EU, 38 in = 85 EU)." },
    { q: "Is the cup size conversion the same for all European brands?", a: "No. While the EU EN 13402 standard dictates 2 cm cup increments, French, Belgian, and Spanish brands use the same cup letters but offset their bands by +15. Furthermore, Polish brands often use UK-style cup progressions mixed with EU band sizing, requiring careful brand-specific conversion." },
    { q: "Why does my converted size still not fit perfectly?", a: "Converting sizes mathematically doesn't account for shape mismatch. A UK balcony bra might expect full-on-bottom breasts, while a US molded cup might expect tall roots. If the converted size gives you quad-boob or gaping, you have a shape mismatch, not necessarily a size conversion error." },
    { q: "What is the Australian (AU) equivalent of a US 34 band?", a: "An AU bra band corresponds to Australian dress sizes. A US/UK 34 band generally converts to an AU 12. A 32 is an AU 10, a 36 is an AU 14, and so on. The cup letters generally follow UK sizing progressions, making it a hybrid system." },
    { q: "How does the converter handle half-sizes or fluctuating measurements?", a: "Converters use absolute math, but bodies are fluid. If you fluctuate between a C and D cup, convert both sizes. When buying internationally, always check the retailer's return policy, as a converted 'D' cup in Japan runs significantly smaller than a US 'D'." },
    { q: "Can I use this converter for sports bras and bralettes?", a: "Sports bras often use Alpha sizing (S, M, L), which is notoriously difficult to convert accurately for larger busts. For encapsulation sports bras that use band/cup sizing (like Panache Sport), this converter works perfectly. For compression bralettes, you must refer to the specific brand's sizing chart." },
    { q: "Does the converter work for nursing and maternity bras?", a: "Yes, the conversion math remains the same. However, maternity bands often have more hooks and stretch to accommodate expanding ribcages. We recommend converting your current measurements, not your pre-pregnancy size, to ensure the wire doesn't rest on sensitive breast tissue." }
  ],
  'eu-bra-size-guide.astro': [
    { q: "How does European (EU) EN 13402 bra sizing differ from US/UK sizing?", a: "European (EU) sizing follows the metric EN 13402 standard. Band numbers represent underbust measurements in centimeters rounded to the nearest multiple of 5 (e.g. 75, 80, 85). Unlike US/UK sizing which uses 1-inch (2.54 cm) cup increments, EU cup progressions use 2 cm (0.78 inch) increments per letter step." },
    { q: "Why is a French (FR) bra band 15 cm higher than an EU band?", a: "French (FR), Belgian (BE), and Spanish (ES) brands add a 15 cm numerical offset to the standard EU band number (e.g. an EU 75 band is labeled FR 90; EU 80 is FR 95). The physical garment dimensions and cup letters are 100% identical—only the tag label number differs." },
    { q: "Do EU brands use double letters like DD or FF?", a: "Generally, no. Standard EU sizing strictly uses single letters (A, B, C, D, E, F, G). An EU 'E' cup is equivalent to a UK 'DD' or US 'DD/DDD'. This single-letter progression can cause extreme confusion for those used to British sizing." },
    { q: "How do I measure myself for an EU bra size?", a: "Measure your snug underbust in centimeters and round to the nearest 5 (e.g., 73cm becomes 75). Measure your full overbust in centimeters. Subtract the underbust from the overbust. A 12-14cm difference is an A cup, 14-16cm is a B cup, and so on in 2cm increments." },
    { q: "Are Italian bra sizes the same as EU sizes?", a: "No, Italian sizing is unique. Brands like Intimissimi use Roman numerals for bands (I, II, III, IV) corresponding to 65, 70, 75, 80 EU. Their cup sizing often matches EU standards, but the band numbering system requires a specific conversion chart." },
    { q: "Why do EU bras feel tighter in the band than US bras?", a: "US sizing historically added 4 inches to the underbust measurement to determine the band size (the '+4 method'). EU sizing measures the underbust directly in centimeters. This direct measurement often results in a firmer, more supportive band fit that US buyers aren't accustomed to." },
    { q: "Is Japanese sizing identical to EU sizing?", a: "Japanese (JP) sizing uses the same metric band numbers (65, 70, 75) as EU sizing. However, JP cups use 2.5cm increments (closer to 1 inch) rather than the EU 2cm increment. Also, JP bras are often heavily padded, leading many to size up 1-2 cup volumes compared to their EU size." },
    { q: "What are the best EU lingerie brands for large busts?", a: "While UK brands dominate the full-bust market, Polish brands (which fall under the EU umbrella geographically but have unique sizing quirks) like Ewa Michalak and Comexim are legendary for their projection, narrow wires, and incredible support for larger busts." }
  ],
  'uk-bra-size-guide.astro': [
    { q: "Why is UK bra sizing considered the global benchmark for fuller busts?", a: "UK lingerie brands standardized double-letter cup progressions (DD, E, F, FF, G, GG) to provide precise 1-inch volume steps up to a 17-inch bust delta. In contrast, US brands use inconsistent multi-D naming schemes that lack uniformity above a D cup." },
    { q: "Is a UK G cup the same size as a US G cup?", a: "No! A UK G cup represents a 9-inch difference between bust and underbust (the 9th cup size). A US G cup represents a 7-inch difference (the 7th cup size). Therefore, a UK G cup is TWO full cup volumes LARGER than a US G cup." },
    { q: "Do UK bands use the +4 measurement method?", a: "Modern UK fit experts strongly discourage the outdated +4 method. Your UK band size should roughly equal your snug underbust measurement in inches. If you measure 32 inches, your UK band is 32. Adding inches creates a loose band that forces the shoulder straps to carry the weight." },
    { q: "What does a UK 'FF' cup actually mean?", a: "The 'FF' cup simply represents an 8-inch difference between your underbust and overbust. It is one inch larger than an 'F' cup and one inch smaller than a 'G' cup. The double letters are just place markers for absolute inch deltas." },
    { q: "Why do my UK bras have such firm bands?", a: "UK full-bust brands engineer their bras so that 80% of the breast weight is supported by the band, not the straps. This requires firm power-mesh fabrics that don't stretch excessively, preventing the excruciating shoulder pain and neck tension common with flimsier bras." },
    { q: "How do I know if I'm buying a UK or US brand?", a: "Check the size tag. If you see double letters beyond DD (like FF, GG, HH), it is definitively a UK sized bra. Brands like Panache, Freya, Elomi, Fantasie, and Curvy Kate all use UK sizing, even when sold in US stores." },
    { q: "Can I use UK sizing for sports bras?", a: "Absolutely. UK brands like Panache produce some of the world's highest-rated encapsulation sports bras. Using precise UK band and cup sizing provides significantly better bounce reduction than generic S/M/L sports bras." },
    { q: "What is 'projection' in UK bras?", a: "UK bras often feature multi-part seamed cups (balconette styles) that allow breast tissue to project forward rather than being flattened against the chest. This structural depth is crucial for larger breasts, offering lift and separation without the 'uniboob' effect." }
  ]
};

const longTextA = `
<div class="prose max-w-none text-body leading-relaxed mb-8">
  <p class="mb-6">
    We understand the profound exhaustion that comes with trying to find a bra that actually fits. It’s a deeply frustrating cycle: measuring yourself, ordering what you believe is the correct size, waiting for the package to arrive, and then feeling a crushing sense of defeat when the band is suffocatingly tight, or the cups gap loosely at the top. You are not alone in this struggle. Millions of women endure excruciating shoulder pain, deep red grooves dug into their skin, and wires that violently poke the delicate breast tissue near the armpits. These are not signs that your body is wrong; they are glaring indicators that the global lingerie industry’s sizing standards are chaotic, inconsistent, and incredibly difficult to navigate without a master guide.
  </p>
  <p class="mb-6">
    The pain of an ill-fitting bra goes far beyond mere physical discomfort. It alters your posture, pulling your shoulders forward to compensate for the lack of support. It affects your wardrobe choices, making you avoid certain fabrics or necklines because you constantly have to adjust your straps or pull the band down in the back. When you are wearing a bra that truly fits, it should feel like a second skin—a supportive embrace that lifts the breast tissue from the bottom, anchoring firmly around your ribcage so that your shoulders bear almost none of the weight. This level of comfort is not a myth; it is entirely achievable when you arm yourself with the knowledge of how international sizing systems interact.
  </p>
  <p class="mb-6">
    Whether you are navigating the bewildering multi-D systems of American manufacturers, the precise and highly regarded double-letter progressions of British brands, or the metric-based centimeter standards of the European Union, understanding these conversions is your absolute best defense against bad fits. A US 'H' cup is vastly different from a UK 'H' cup—in fact, mixing these up can result in a bra that is several volumes too small, causing the dreaded "quad-boob" effect where breast tissue aggressively spills over the top edge of the cup. 
  </p>
  <p class="mb-6">
    To alleviate these pervasive issues, we have engineered this comprehensive, interactive guide. By cross-referencing your measurements against international standards, you can confidently shop across borders. Before you dive into the conversion matrices, we strongly recommend visiting our <a href="/how-to-measure/" class="text-primary underline font-semibold">How to Measure Guide</a> to ensure your baseline numbers are entirely accurate, or consulting our <a href="/fit-guide/" class="text-primary underline font-semibold">Comprehensive Fit Guide</a> to diagnose any specific fit issues you are currently experiencing. Your comfort is paramount, and finding the perfect fit is an investment in your daily well-being and physical health.
  </p>
</div>
`;

const longTextB = `
<div class="prose max-w-none text-body leading-relaxed mt-12 mb-8">
  <h2 class="text-2xl font-bold text-ink mb-6">Mastering the Nuances of Bra Fit and Sizing</h2>
  <p class="mb-6">
    Once you have identified your converted size using the tools above, it is crucial to recognize that the number and letter on the tag are only the beginning of your journey toward true comfort. The shape of your breast tissue—whether you are full on top, full on bottom, have wide roots, or narrow roots—will drastically dictate how a specific brand or style fits your body. For instance, a UK balconette bra with deep projection might fit flawlessly in a 34F, but a molded seamless t-shirt bra in the exact same size might gap significantly because the foam cannot conform to your natural shape. This is a common source of immense frustration. You haven't chosen the wrong size; you have simply encountered a shape mismatch.
  </p>
  <p class="mb-6">
    We hear incredible stories of relief from people who finally drop the outdated "+4 measurement method" and embrace their true band size. For decades, outdated sizing guides told women to add 4 inches to their underbust measurement to find their band size. This catastrophic advice results in bands that are far too loose, forcing the shoulder straps to carry the heavy burden of breast tissue. When the straps dig into your shoulders, causing tension headaches and deep indentations, the solution is almost always a smaller, firmer band and a larger cup volume. Your band must act as a strong, horizontal anchor around your ribcage, sitting perfectly parallel to the floor.
  </p>
  <p class="mb-6">
    Furthermore, sister sizing is an essential concept to master when dealing with international brands. Because different manufacturers use different elastic tensions—some brands run notoriously tight, while others are incredibly stretchy—you must know how to adjust your size while maintaining the same cup volume. If a 34G is suffocating your ribs, you do not want a 36G, which would increase the cup volume. Instead, you sister size to a 36FF. This intricate dance of sizing is what separates a lifetime of discomfort from the blissful realization that a bra can be both deeply supportive and entirely painless.
  </p>
  <p class="mb-6">
    We deeply empathize with the anxiety of ordering lingerie online, especially from overseas brands. The fear of wasting money on non-returnable items is entirely valid. By meticulously using the charts and calculators we provide, and cross-referencing with our <a href="/fit-guide/" class="text-primary underline font-semibold">Fit Guide</a>, you drastically reduce this risk. Always remember that your body is not the problem. The chaotic lack of standardization in the garment industry is the problem, and you now have the tools to conquer it.
  </p>
</div>
`;

files.forEach(file => {
  const filePath = path.join('src', 'pages', file);
  if (!fs.existsSync(filePath)) {
    console.log('File not found:', filePath);
    return;
  }
  let content = fs.readFileSync(filePath, 'utf-8');

  const faqData = faqs[file];
  const faqJson = JSON.stringify(faqData.map(f => ({
    "@type": "Question",
    "name": f.q,
    "acceptedAnswer": {
      "@type": "Answer",
      "text": f.a
    }
  })), null, 4);

  const newFaqStr = "const faqSchema = {\n  \"@context\": \"https://schema.org\",\n  \"@type\": \"FAQPage\",\n  \"mainEntity\": " + faqJson + "\n};\n---";
  
  content = content.replace(/const faqSchema = \{[\s\S]*?\n\};\n---/, newFaqStr);

  // Insert longTextA after the <header> tag closes
  content = content.replace(/(<\/header>)/, "$1\n\n    <!-- E-E-A-T Intro Expansion -->\n    " + longTextA);

  // Insert longTextB before the Educational Sections
  content = content.replace(/(<!-- Educational Sections -->)/, "<!-- E-E-A-T Outro Expansion -->\n    " + longTextB + "\n\n    $1");

  fs.writeFileSync(filePath, content);
  console.log('Processed', file);
});
