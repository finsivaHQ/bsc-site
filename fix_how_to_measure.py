import re

with open('src/pages/how-to-measure.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the header block
match = re.search(r'(<header.*?>)(.*?)(</header>)', content, re.DOTALL)
header_open = match.group(1)
header_body = match.group(2)
header_close = match.group(3)

# Inside header_body, there is a <div class="prose...
div_match = re.search(r'(<div class="prose.*?>)(.*?)(</div>)', header_body, re.DOTALL)
div_open = div_match.group(1)
div_body = div_match.group(2)
div_close = div_match.group(3)

# Inside div_body, there are multiple <p> tags. We want to keep the first one in the header.
p_tags = list(re.finditer(r'<p.*?</p>', div_body, re.DOTALL))
first_p_end = p_tags[0].end()

kept_div_body = div_body[:first_p_end]
moved_div_body = div_body[first_p_end:]

new_header_body = header_body[:div_match.start()] + div_open + kept_div_body + div_close + header_body[div_match.end():]
new_header = header_open + new_header_body + header_close

article_block = f'\n  <article class="mt-12 space-y-6">\n    {div_open}\n      {moved_div_body.strip()}\n    {div_close}\n  </article>\n'

new_content = content[:match.start()] + new_header + content[match.end():]
new_content = new_content.replace('<!-- FAQ Section -->', article_block + '    <!-- FAQ Section -->')

with open('src/pages/how-to-measure.astro', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Successfully moved text in how-to-measure.astro")
