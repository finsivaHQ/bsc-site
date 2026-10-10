const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// 1. Get all deleted .astro files from git history
const gitOutput = execSync('git log --diff-filter=D --summary', { encoding: 'utf-8' });
const deletedFiles = gitOutput.split('\n')
  .filter(line => line.includes('delete mode') && line.includes('.astro') && line.includes('src/pages/'))
  .map(line => {
    const match = line.match(/src\/pages\/(.+)\.astro/);
    if (match) return `/${match[1]}/`.replace(/\/index\/$/, '/');
    return null;
  })
  .filter(Boolean);

const deletedPages = [...new Set(deletedFiles)];

// 2. Read existing redirects
let existingRedirectsRaw = fs.readFileSync('public/_redirects', 'utf8');
if (existingRedirectsRaw.includes('# Auto-generated redirects')) {
  existingRedirectsRaw = existingRedirectsRaw.split('# Auto-generated redirects')[0];
  fs.writeFileSync('public/_redirects', existingRedirectsRaw);
}

const existingRedirectsList = existingRedirectsRaw.split('\n').filter(line => line.trim() && !line.startsWith('#')).map(line => line.split(' ')[0]);

// 3. Mapping logic (custom for bsc calculator site)
function mapToAlive(url) {
  // Only 1 deleted page: pakistan-income-tax-calculator
  // Let's redirect it to the homepage since this seems to be a single/multi calculator site
  return '/';
}

function pageExists(urlPath) {
  const cleanPath = urlPath.replace(/^\//, '').replace(/\/$/, '');
  if (cleanPath === '') return true; 
  if (cleanPath.includes('[')) return true;

  const exactFile = path.join('src/pages', cleanPath + '.astro');
  const indexFile = path.join('src/pages', cleanPath, 'index.astro');
  
  return fs.existsSync(exactFile) || fs.existsSync(indexFile);
}

let newRedirects = '\n# Auto-generated redirects for historically deleted pages\n';
let addedCount = 0;

for (const oldUrl of deletedPages) {
  if (oldUrl.includes('[')) continue;

  if (!existingRedirectsList.includes(oldUrl)) {
    if (!pageExists(oldUrl)) {
      const newUrl = mapToAlive(oldUrl);
      newRedirects += `${oldUrl} ${newUrl} 301\n`;
      addedCount++;
    }
  }
}

if (addedCount > 0) {
  fs.appendFileSync('public/_redirects', newRedirects);
  console.log(`Added ${addedCount} new redirects to public/_redirects`);
} else {
  console.log('No new redirects needed.');
}
