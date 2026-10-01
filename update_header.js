const fs = require('fs');

const file = 'src/components/Header.astro';
let content = fs.readFileSync(file, 'utf8');

const desktopNavTarget = '<a href="/bra-size-chart/" class="nav-link text-sm text-body hover:text-primary transition-colors font-medium relative py-2">';
const desktopNavReplacement = `<a href="/size/" class="nav-link text-sm text-body hover:text-primary transition-colors font-medium relative py-2">
        Size Database
        <span class="active-indicator hidden absolute bottom-0 left-0 w-full h-[2px] bg-accent rounded-full"></span>
      </a>
      <a href="/bra-size-chart/" class="nav-link text-sm text-body hover:text-primary transition-colors font-medium relative py-2">`;

content = content.replace(desktopNavTarget, desktopNavReplacement);

const mobileNavTarget = '<a href="/bra-size-chart/" class="mobile-nav-link text-base font-semibold text-ink hover:text-primary py-2.5 px-3 rounded-lg hover:bg-canvas-soft-2 transition-colors">';
const mobileNavReplacement = `<a href="/size/" class="mobile-nav-link text-base font-semibold text-ink hover:text-primary py-2.5 px-3 rounded-lg hover:bg-canvas-soft-2 transition-colors">
        Size Database
      </a>
      <a href="/bra-size-chart/" class="mobile-nav-link text-base font-semibold text-ink hover:text-primary py-2.5 px-3 rounded-lg hover:bg-canvas-soft-2 transition-colors">`;

content = content.replace(mobileNavTarget, mobileNavReplacement);

fs.writeFileSync(file, content, 'utf8');
console.log('Header updated successfully.');
