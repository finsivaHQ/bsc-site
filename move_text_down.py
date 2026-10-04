import re
import glob

def refactor_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the <header> block
    match = re.search(r'(<header.*?>)(.*?)(</header>)', content, re.DOTALL)
    if not match: return
    
    header_open = match.group(1)
    header_body = match.group(2)
    header_close = match.group(3)
    
    # We want to extract all <p> tags from the header that are NOT the first <p> tag.
    # The first <p> tag is usually the subtitle "Select your known bra size..."
    p_tags = list(re.finditer(r'<p.*?</p>', header_body, re.DOTALL))
    
    if len(p_tags) <= 1:
        return # Nothing to move
        
    # The first p tag stays
    first_p_end = p_tags[0].end()
    
    # Everything after the first p tag inside the header goes to the bottom
    text_to_move = header_body[first_p_end:].strip()
    
    # Create the new header
    new_header_body = header_body[:first_p_end].strip()
    new_header = f"{header_open}\n    {new_header_body}\n  {header_close}"
    
    # Create the article block to insert below the calculator
    article_block = f"\n  <article class='mt-12 space-y-6'>\n    {text_to_move}\n  </article>\n"
    
    # Replace the old header with the new header
    new_content = content[:match.start()] + new_header + content[match.end():]
    
    # Now, insert the article block right before the FAQ section if it exists, or before </main>
    if '<!-- FAQ Section -->' in new_content:
        new_content = new_content.replace('<!-- FAQ Section -->', f"{article_block}\n    <!-- FAQ Section -->")
    else:
        new_content = new_content.replace('</main>', f"{article_block}\n  </main>")
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Refactored {filepath}")

for file in ['bra-size-converter.astro', 'bra-size-chart.astro', 'sister-size-calculator.astro']:
    refactor_page(f"d:/TOOLS WEB TOOLS/bsc calculator site/src/pages/{file}")
    
