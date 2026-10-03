import os

base_path = r"d:\TOOLS WEB TOOLS\bsc calculator site\src\pages"
privacy = """---
import Layout from '../layouts/Layout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import Breadcrumbs from '../components/Breadcrumbs.astro';
---

<Layout 
  title="Privacy Policy — 100% Local Measurement Privacy | BraSizeChecker"
  description="Read our privacy policy. BraSizeChecker processes all body measurements 100% locally inside your browser with zero data collection or tracking."
>
  <Header />
  <main class="flex-1 w-full max-w-3xl mx-auto px-4 sm:px-6 py-8 sm:py-12 md:py-16">
    <Breadcrumbs items={[{ label: 'Privacy Policy' }]} />

    <h1 class="text-2xl sm:text-3xl md:text-4xl font-bold text-ink mb-6">Privacy Policy</h1>
    <div class="prose prose-slate max-w-none text-body space-y-6 leading-relaxed text-sm sm:text-base">
      <p class="text-xs text-mute font-mono uppercase tracking-wider">Last updated: October 2026</p>
      
      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">1. Introduction and Core Philosophy</h2>
        <p>
          Welcome to BraSizeChecker.com. We respect your privacy and are committed to maintaining full transparency regarding data processing. This Privacy Policy explains exactly how our calculator operates and how information is handled when you visit our website.
        </p>
        <p>
          Unlike many online retail stores that force you to create an account to save your sizes for marketing purposes, we believe your physical dimensions are deeply personal and highly sensitive. Our platform is engineered to never see or store your bodily data.
        </p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">2. Body Measurement Privacy (Local Processing)</h2>
        <p>
          Your body measurements (bust, underbust, leaning, lying, etc.) are processed <strong>100% locally</strong> inside your browser's JavaScript engine. 
        </p>
        <ul class="list-disc pl-5 sm:pl-6 space-y-2 mt-2">
          <li>Measurements are <strong>never</strong> transmitted over network requests or sent to remote servers.</li>
          <li>Measurements are <strong>never</strong> stored in databases, cookies, `localStorage`, or `sessionStorage`.</li>
          <li>Measurements are <strong>never</strong> included in query parameters or analytics events.</li>
          <li>Once you close or refresh your browser tab, your entered measurements vanish from memory entirely.</li>
        </ul>
        <p>This means that in the event of a theoretical server breach, your measurements cannot be stolen, because they simply do not exist on our servers.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">3. No Account Required</h2>
        <p>
          BraSizeChecker.com is open to all users without registration. We do not require users to create an account, log in, or provide a name, email address, or personal profile to use the sizing tool. We do not want your email address unless you are specifically reaching out to our support team for assistance.
        </p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">4. Contact Form Submissions</h2>
        <p>
          If you choose to submit an inquiry through our <a href="/contact/" class="text-primary font-medium hover:underline">Contact Us</a> page, you voluntarily provide your email address and message contents. 
        </p>
        <p class="mt-2">
          Contact form submissions are securely processed via Formspree solely for the purpose of responding to your inquiry. Formspree handles form data in accordance with strict privacy standards. We will never add your email to a marketing newsletter without explicit consent, and we will never sell your contact information.
        </p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">5. Browser Storage & Cookies</h2>
        <p>
          We do not use tracking or advertising cookies. The only item saved in your browser's local storage (`localStorage`) is your preferred color theme (`light` or `dark`), which allows the website to preserve your visual theme choice across visits. This is purely a functional mechanism and contains no personal data.
        </p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">6. Third-Party Links & Services</h2>
        <p>
          Our website contains no third-party tracking scripts or advertising networks on sizing pages. If external links are provided (such as links to bra retailers or educational forums like Reddit's A Bra That Fits), we encourage you to review the privacy policies of any third-party websites you visit, as we have no control over their tracking mechanisms.
        </p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">7. GDPR, CCPA, and Global Privacy Compliance</h2>
        <p>If you are a resident of the European Economic Area (EEA) under the General Data Protection Regulation (GDPR), a California resident under the CCPA, or a citizen of another jurisdiction with strict data laws, you have specific data protection rights.</p>
        <p>Because we explicitly do not store, process, or collect any personal health data (including body measurements), there is no personal data database to query. However, if you have contacted us via email or our contact form, you maintain the right to request access to, correction of, or deletion of that specific communication data. We strictly adhere to the principle of data minimization.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">8. Log Files and Analytics</h2>
        <p>Like many modern websites, we collect standard log files to ensure site functionality, security, and performance. This anonymous data includes IP addresses (anonymized where required by law), browser types, ISPs, date/time stamps, and referring/exit pages. This information is critical for defending against cyber attacks and is not linked to any information that is personally identifiable.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">9. Children's Privacy</h2>
        <p>Our tools are designed for adult users. We do not knowingly collect personal information from individuals under the age of 13. If we become aware that a child under 13 has provided us with personal information (such as via an email), we will take steps to delete such information immediately.</p>
      </section>

      <section>
        <h2 class="text-lg sm:text-xl font-bold text-ink mb-3">10. Contact Us</h2>
        <p>
          If you have any questions, feedback, or data deletion requests regarding this Privacy Policy, please email us directly at <a href="mailto:ornacasa11@gmail.com" class="text-primary font-medium hover:underline">ornacasa11@gmail.com</a>.
        </p>
      </section>
    </div>
  </main>
  <Footer />
</Layout>
"""

with open(os.path.join(base_path, 'privacy-policy.astro'), "w", encoding="utf-8") as f:
    f.write(privacy)
print("Expanded bsc privacy")
