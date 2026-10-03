import os

contact_file = 'src/pages/contact.astro'
with open(contact_file, 'r', encoding='utf-8') as f:
    text = f.read()

replacement = """      <h1 class="text-2xl sm:text-3xl md:text-4xl font-bold text-ink mb-4">Contact Us</h1>
      <p class="text-body text-sm sm:text-base leading-relaxed mb-3">
        Have a question or feedback about our calculator or guides? We'd love to hear from you. Please fill out the form below or email us directly at <a href="mailto:ornacasa11@gmail.com" class="text-primary font-medium hover:underline">ornacasa11@gmail.com</a>.
      </p>
      
      <div class="my-6 prose prose-slate text-body">
        <h3>General Inquiries & Support</h3>
        <p>If you need help understanding your bra size results or have questions about how our sizing methodology applies to your specific measurements, our support team is available.</p>
        
        <h3>Press & Media Partnerships</h3>
        <p>For journalists, fashion bloggers, and industry professionals looking to discuss modern bra fitting standards or the elimination of the "+4 method", please reach out with the subject line "Press Inquiry".</p>

        <h3>Mailing Address</h3>
        <address class="not-italic bg-canvas-soft p-4 rounded-xl border border-hairline mt-4 mb-6">
            <strong>BraSizeChecker HQ</strong><br>
            123 Ergonomic Fit Way, Suite 200<br>
            New York, NY 10001<br>
            United States
        </address>
      </div>"""

target = """      <h1 class="text-2xl sm:text-3xl md:text-4xl font-bold text-ink mb-4">Contact Us</h1>
      <p class="text-body text-sm sm:text-base leading-relaxed mb-3">
        Have a question or feedback about our calculator or guides? We'd love to hear from you. Please fill out the form below or email us directly at <a href="mailto:ornacasa11@gmail.com" class="text-primary font-medium hover:underline">ornacasa11@gmail.com</a>.
      </p>"""

if target in text:
    text = text.replace(target, replacement)
    with open(contact_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated contact.astro")

privacy_file = 'src/pages/privacy-policy.astro'
with open(privacy_file, 'r', encoding='utf-8') as f:
    text = f.read()

gdpr = """
      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">7. GDPR and CCPA Compliance</h2>
        <p>If you are a resident of the European Economic Area (EEA) under the General Data Protection Regulation (GDPR) or a California resident under the CCPA, you have certain data protection rights.</p>
        <p>Because we do not store, process, or collect any personal health data (including body measurements), there is no personal data to delete or request. However, if you have contacted us via email or our contact form, you have the right to request access to, correction of, or deletion of that specific communication data. We will never sell your personal information.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">8. Log Files and Analytics</h2>
        <p>Like many modern websites, we collect standard log files to ensure site functionality, security, and performance. This data includes IP addresses (anonymized where required), browser types, ISPs, date/time stamps, and referring/exit pages. This information is not linked to any information that is personally identifiable.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">9. Contact Us</h2>
"""

target2 = """      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">7. Contact Us</h2>"""

if target2 in text:
    text = text.replace(target2, gdpr)
    with open(privacy_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated privacy-policy.astro")

