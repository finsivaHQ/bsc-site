import os

base_path = r"d:\TOOLS WEB TOOLS\bsc calculator site\src\pages"

def write_page(filename, content):
    path = os.path.join(base_path, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

about = """---
import Layout from '../layouts/Layout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import Breadcrumbs from '../components/Breadcrumbs.astro';

const orgSchema = {
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "BraSizeChecker",
  "url": "https://brasizechecker.com",
  "logo": "https://brasizechecker.com/apple-touch-icon.png",
  "description": "Independent ergonomic fitting laboratory and digital calculator platform providing modern direct underbust bra size verification.",
  "knowsAbout": ["Bra Fitting", "Anthropometric Measurement", "Textile Elasticity", "Breast Health Ergonomics"],
  "publishingPrinciples": "https://brasizechecker.com/methodology"
};
---

<Layout 
  title="About Us — Independent Ergonomic Bra Sizing & E-E-A-T Standards | BraSizeChecker"
  description="Learn about BraSizeChecker: our independent sizing methodology, modern direct underbust calculation principles, and browser privacy commitments."
  canonical="https://brasizechecker.com/about"
>
  <script type="application/ld+json" set:html={JSON.stringify(orgSchema)} />

  <Header />
  <main class="flex-1 w-full max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 md:py-16">
    <Breadcrumbs items={[{ label: 'About Us' }]} />
    
    <header class="mb-10 text-center sm:text-left">
      <span class="inline-block py-1 px-3 rounded-full bg-canvas-soft-2 border border-hairline text-xs font-semibold uppercase tracking-widest text-primary mb-3">
        E-E-A-T & Transparency Notice
      </span>
      <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold text-ink tracking-tight mb-4">
        About BraSizeChecker: Independent Ergonomics & Fit Science
      </h1>
      <div class="flex items-center gap-3 text-xs text-mute mb-4">
        <span>By BraSizeChecker BSC Team</span>
        <span>&bull;</span>
        <time datetime="2026-10-02">Updated October 2026</time>
      </div>
      <p class="text-base sm:text-lg text-body leading-relaxed max-w-3xl">
        BraSizeChecker is a 100% independent digital sizing reference hub. We empower individuals around the globe to discover their true, comfortable bra size from home using modern anthropometric principles, discarding the outdated and painful sizing methods pushed by historical retailers.
      </p>
    </header>

    <div class="space-y-10 text-body leading-relaxed text-sm sm:text-base">
      <!-- Section 1: Our Mission & The Problem We Solve -->
      <section class="bg-surface border border-hairline rounded-2xl p-6 sm:p-8">
        <h2 class="text-xl sm:text-2xl font-bold text-ink mb-4">1. Our Mission: Eliminating the Outdated "+4" Method</h2>
        <p class="mb-4">
          For over half a century, the retail lingerie industry relied on the obsolete <strong>"+4 method"</strong>—instructing customers to add 4 or 5 inches to their measured underbust (e.g., measuring a 30-inch underbust and being told to wear a 34 band). This antiquated rule originated in the 1950s when bras lacked stretchable elastane, were manufactured from stiff cotton, and sizing matrices were severely limited.
        </p>
        <p class="mb-4">
          In modern times, applying the +4 method forces many individuals into loose 34 or 36 bands paired with undersized A or B cups. The consequences of this are severe: shoulder strap grooving, neck and back pain, poor weight distribution, the band constantly riding up the back, and general daily discomfort. It fundamentally misunderstands garment engineering, as 80% of breast tissue support should come from a firm, flush underband, not the shoulder straps.
        </p>
        <p>
          BraSizeChecker was built to replace outdated retail charts with a <strong>modern direct underbust algorithm</strong>. Our tool anchors structural support firmly against the ribcage wall where it naturally belongs. By calculating your true underbust and overbust differential, we aim to solve the chronic issue of ill-fitting foundation garments that affect millions globally.
        </p>
      </section>

      <!-- Section 2: Editorial Independence & Commercial Integrity -->
      <section class="bg-surface border border-hairline rounded-2xl p-6 sm:p-8">
        <h2 class="text-xl sm:text-2xl font-bold text-ink mb-4">2. 100% Independent & Brand-Neutral Principles</h2>
        <p class="mb-4">
          The core issue with retail sizing charts is commercial conflict of interest. Brands often push users into their limited size range (e.g., 32A to 38DD) rather than admitting the customer needs a size they do not manufacture (like a 28G). 
        </p>
        <p class="mb-4">
          BraSizeChecker is completely independent. We are not owned, operated, funded, or influenced by any lingerie manufacturer, brand, or retail department store. We tell you the mathematical truth of your measurements, regardless of whether it's a difficult size to find in a standard mall.
        </p>

        <div class="grid sm:grid-cols-3 gap-4 my-6">
          <div class="p-4 bg-canvas-soft-2/70 border border-hairline rounded-xl text-center">
            <span class="text-primary font-bold text-lg block mb-1">Zero Paid Bias</span>
            <p class="text-xs text-body">We accept zero paid brand placements or biased product rankings. Our algorithms are mathematically rigid.</p>
          </div>
          <div class="p-4 bg-canvas-soft-2/70 border border-hairline rounded-xl text-center">
            <span class="text-primary font-bold text-lg block mb-1">Mathematical Accuracy</span>
            <p class="text-xs text-body">All conversion matrices rely on verified international standards (EN 13402, UK BS) and real textile mechanics.</p>
          </div>
          <div class="p-4 bg-canvas-soft-2/70 border border-hairline rounded-xl text-center">
            <span class="text-primary font-bold text-lg block mb-1">Privacy First</span>
            <p class="text-xs text-body">Calculations execute locally in JS; no personal measurement data is saved or transmitted anywhere.</p>
          </div>
        </div>
      </section>

      <!-- Section 3: Editorial Standards & Sizing Methodology -->
      <section class="bg-surface border border-hairline rounded-2xl p-6 sm:p-8">
        <h2 class="text-xl sm:text-2xl font-bold text-ink mb-4">3. E-E-A-T & Editorial Standards</h2>
        <p class="mb-4">
          Our fitting advice and diagnostic documentation are created by our BSC Team using established apparel sizing standards and deep community fit research. We adhere strictly to Google's E-E-A-T guidelines (Experience, Expertise, Authoritativeness, Trustworthiness) by ensuring our educational guides are scientifically robust.
        </p>
        <p class="mb-4">
          We do not just output a number; we provide diagnostic guides on how a garment *should* feel. We discuss tissue migration, breast root width, projection, and the realities of modern elastane degradation over time.
        </p>

        <div class="space-y-4 mb-6">
          <div class="p-4 bg-canvas-soft-2/70 border border-hairline rounded-xl">
            <h3 class="font-bold text-ink text-sm mb-1">Technical Fit Standards</h3>
            <p class="text-xs sm:text-sm text-body">
              We reference standard international sizing tables and cup volume grading across diverse anatomical profiles (shallow, projected, asymmetrical, and wide-set roots). We understand that two people with the same measurements may need different styles.
            </p>
          </div>

          <div class="p-4 bg-canvas-soft-2/70 border border-hairline rounded-xl">
            <h3 class="font-bold text-ink text-sm mb-1">Garment Fit Analysis</h3>
            <p class="text-xs sm:text-sm text-body">
              We analyze fabric elasticity characteristics and international sizing conversions (US vs UK vs EU) to provide practical brand-by-brand sizing guidance and Sister Size conversions.
            </p>
          </div>
        </div>
      </section>

      <!-- Section 4: Privacy & Client-Side Processing Commitments -->
      <section class="bg-surface border border-hairline rounded-2xl p-6 sm:p-8">
        <h2 class="text-xl sm:text-2xl font-bold text-ink mb-4">4. Strict User Privacy Standards</h2>
        <p class="mb-4">
          Your personal body measurements are deeply private. BraSizeChecker processes all underbust and overbust measurement data <strong>entirely inside your local web browser</strong> using JavaScript. We do not track, log, transmit, or store body measurements on external servers. You are completely anonymous.
        </p>

        <div class="flex flex-wrap gap-3 text-xs font-bold">
          <a href="/methodology/" class="px-5 py-2.5 bg-primary text-white rounded-xl hover:bg-primary-hover transition-colors shadow-2xs">Read Technical Methodology &rarr;</a>
          <a href="/privacy-policy/" class="px-5 py-2.5 bg-surface border border-hairline text-ink rounded-xl hover:bg-canvas-soft-2 transition-colors">Privacy Policy &rarr;</a>
          <a href="/contact/" class="px-5 py-2.5 bg-surface border border-hairline text-ink rounded-xl hover:bg-canvas-soft-2 transition-colors">Contact Advisory Team &rarr;</a>
        </div>
      </section>
    </div>
  </main>
  <Footer />
</Layout>
"""

terms = """---
import Layout from '../layouts/Layout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import Breadcrumbs from '../components/Breadcrumbs.astro';
---

<Layout 
  title="Terms & Conditions — Website Terms of Use | BraSizeChecker"
  description="Review the terms and conditions for using BraSizeChecker.com sizing calculators, conversion charts, and fit guides."
>
  <Header />
  <main class="flex-1 w-full max-w-3xl mx-auto px-4 sm:px-6 py-8 sm:py-12 md:py-16">
    <Breadcrumbs items={[{ label: 'Terms & Conditions' }]} />

    <h1 class="text-2xl sm:text-3xl md:text-4xl font-bold text-ink mb-6">Terms & Conditions</h1>
    <div class="prose prose-slate max-w-none text-body space-y-6 leading-relaxed text-sm sm:text-base">
      <p class="text-xs text-mute font-mono uppercase tracking-wider">Last updated: October 2026</p>
      
      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">1. Agreement to Terms</h2>
        <p>By accessing or using BraSizeChecker.com, you agree to be bound by these Terms and Conditions. If you do not agree to all of these terms, please do not use our website or its embedded calculators. These Terms apply to all visitors, users, and automated crawlers that access the Service.</p>
        <p>We reserve the right to modify these Terms at any time. We will provide notice of any significant changes by updating the "Last updated" date at the top of this page. Your continued use of the site following any changes signifies your acceptance of the revised Terms.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">2. Sizing Disclaimer & Educational Purpose</h2>
        <p>Our sizing recommendations, output by our algorithms, are intended for educational and guidance purposes only. Fit can vary dramatically by brand, style, pattern grading, and individual anatomical preference (such as breast root width, projection, and tissue density). We do not guarantee a perfect fit from our recommendations, and our calculators should be treated strictly as a starting baseline.</p>
        <p>A mathematical algorithm cannot account for the elasticity of a specific garment's fabric or the unique geometry of the human body. Users must apply their own judgment and utilize physical fitting tests (like the "scoop and swoop" method) to verify fit.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">3. Limitation of Liability and Medical Disclaimer</h2>
        <p>BraSizeChecker.com is provided "as is" and "as available" without any warranties, express or implied. We are not liable for any direct, indirect, incidental, or consequential damages resulting from your use of the site, including but not limited to the financial cost of purchasing improperly fitting garments based on our algorithms.</p>
        <p><strong>Crucial Medical Disclaimer:</strong> Our measurement guidelines are strictly non-medical. Improperly fitting undergarments can cause skin irritation, shoulder pain, or restrict breathing, but our site cannot diagnose or treat any physical ailments. If you experience chronic breast pain, dermatological issues, or back pain, please consult a licensed healthcare professional. We do not offer medical advice, and our content should never substitute for a doctor's diagnosis.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">4. Intellectual Property Rights</h2>
        <p>The Service and its original content, features, proprietary algorithms, conversion matrices, and user interface are and will remain the exclusive property of BraSizeChecker.com. Our site is protected by copyright, trademark, and other intellectual property laws.</p>
        <p>You may not scrape, reproduce, reverse-engineer, or commercially exploit our calculator tools or educational guides without express written permission. Automated data harvesting of our sizing matrices is strictly forbidden.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">5. User Conduct</h2>
        <p>When using our site, you agree to not use the service for any unlawful purpose. You must not attempt to compromise the security of the site, inject malicious code into our contact forms, or intentionally overload our servers with automated requests.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">6. External Links and Third Parties</h2>
        <p>Our website may contain links to third-party web sites, brands, or retail services that are not owned or controlled by us. We assume no responsibility for the content, privacy policies, sizing charts, or practices of any third-party web sites or services. Clicking on a link to a retailer does not constitute an endorsement of their specific sizing methodology.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">7. Contact Us</h2>
        <p>For any legal inquiries, questions about these terms, or requests for permission to use our intellectual property, please contact us at <a href="mailto:ornacasa11@gmail.com" class="text-primary font-medium hover:underline">ornacasa11@gmail.com</a>.</p>
      </section>
    </div>
  </main>
  <Footer />
</Layout>
"""

write_page("about.astro", about)
write_page("terms-conditions.astro", terms)
print("Expanded bsc calculator site about and terms")
