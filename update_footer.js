const fs = require('fs');

const file = 'src/components/Footer.astro';
let content = fs.readFileSync(file, 'utf8');

const target = '<li><a href="/bra-size-converter/" class="text-xs sm:text-sm font-medium text-body hover:text-primary transition-colors">Size Converter</a></li>';
const replacement = `<li><a href="/bra-size-converter/" class="text-xs sm:text-sm font-medium text-body hover:text-primary transition-colors">Size Converter</a></li>
        <li><a href="/size/" class="text-xs sm:text-sm font-medium text-body hover:text-primary transition-colors">Visual Size Database</a></li>`;

content = content.replace(target, replacement);

fs.writeFileSync(file, content, 'utf8');
console.log('Footer updated successfully.');
