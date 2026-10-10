const fs = require('fs');
const content = fs.readFileSync('astro.config.mjs', 'utf8');

// Match the entire redirects object
// We will look for lines matching: 'source': { ... destination: 'dest' }
const lines = content.split('\n');
const redirects = [];
let currentSource = '';

for (const line of lines) {
  // Check for source URL line, e.g., '/blogs/hong-kong/': {
  const sourceMatch = line.match(/^\s*'([^']+)'\s*:\s*\{/);
  if (sourceMatch) {
    currentSource = sourceMatch[1];
  }
  
  // Check for destination line, e.g., destination: '/countries/hong-kong/'
  const destMatch = line.match(/destination:\s*'([^']+)'/);
  if (destMatch && currentSource) {
    redirects.push(currentSource + ' ' + destMatch[1] + ' 301');
    currentSource = ''; // reset
  }
}

if (redirects.length > 0) {
  if (!fs.existsSync('public')) {
    fs.mkdirSync('public');
  }
  fs.writeFileSync('public/_redirects', redirects.join('\n') + '\n');
  console.log('Successfully generated public/_redirects with ' + redirects.length + ' rules.');
} else {
  console.log('No redirects found.');
}
