import os

terms_file = 'src/pages/terms-conditions.astro'
with open(terms_file, 'r', encoding='utf-8') as f:
    text = f.read()

replacement = """      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">4. Limitation of Liability and Medical Disclaimer</h2>
        <p>BraSizeChecker.com is provided "as is" without any warranties, express or implied. We are not liable for any direct or indirect damages resulting from your use of the site, including but not limited to purchasing improperly fitting garments. Furthermore, our measurement guidelines are non-medical. If you experience breast pain, discomfort, or dermatological issues, please consult a healthcare professional. We do not offer medical advice.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">5. Intellectual Property Rights</h2>
        <p>The Service and its original content, features, proprietary algorithms, and user interface are and will remain the exclusive property of BraSizeChecker.com. Our site is protected by copyright, trademark, and other laws. You may not scrape, reproduce, or commercially exploit our calculator tools without written permission.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">6. External Links</h2>
        <p>Our website may contain links to third-party web sites or services (such as retailers) that are not owned or controlled by us. We assume no responsibility for the content, privacy policies, or practices of any third party web sites or services.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">7. Contact Us</h2>"""

target = """      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">4. Limitation of Liability</h2>
        <p>BraSizeChecker.com is provided "as is" without any warranties. We are not liable for any direct or indirect damages resulting from your use of the site.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">5. Contact Us</h2>"""

if target in text:
    text = text.replace(target, replacement)
    with open(terms_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated terms-conditions.astro")
