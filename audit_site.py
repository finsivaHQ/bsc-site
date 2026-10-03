import os
import re

directories = ['src/pages', 'src/pages/guides', 'src/content/blog']
ignore_files = ['404.astro', '500.astro', 'index.astro']

report = []

for d in directories:
    if not os.path.exists(d):
        continue
    for root, _, files in os.walk(d):
        if 'size' in root: continue # skip dynamic db files as discussed
        for file in files:
            if file in ignore_files: continue
            if file.endswith('.astro') or file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # word count
                text_only = re.sub(r'<[^>]+>', ' ', content)
                words = [w for w in text_only.split() if re.match(r'\w', w)]
                word_count = len(words)
                
                # Check Pillar 6: JSON-LD Schema
                has_schema = 'application/ld+json' in content or 'faqSchema' in content or 'JSON-LD' in content or 'faq' in content.lower()
                
                # Status
                status = "PASS" if word_count >= 1200 and has_schema else "FAIL"
                
                report.append(f"{file:<45} | Words: {word_count:<5} | Schema: {str(has_schema):<5} | Status: {status}")

print("=== FINAL SITE AUDIT REPORT ===")
print(f"{'Filename':<45} | {'Words':<5} | {'Schema':<5} | {'Status'}")
print("-" * 75)
for r in report:
    print(r)
