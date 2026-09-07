const fs = require('fs');
const path = require('path');
function walk(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(function(file) {
    file = dir + '/' + file;
    const stat = fs.statSync(file);
    if (stat && stat.isDirectory()) { 
      results = results.concat(walk(file));
    } else if (file.endsWith('.astro') || file.endsWith('.md')) {
      results.push(file);
    }
  });
  return results;
}
const files = walk('./src');
const routes = ['bra-size-chart', 'how-to-measure', 'fit-guide', 'blog', 'about', 'contact', 'bra-size-converter', 'eu-bra-size-guide', 'uk-bra-size-guide', 'sister-size-calculator', 'methodology', 'terms-conditions', 'privacy-policy'];
const regex = new RegExp('href=\"/(' + routes.join('|') + ')\"', 'g');
let changed = 0;
files.forEach(f => {
  const content = fs.readFileSync(f, 'utf8');
  if (regex.test(content)) {
    const newContent = content.replace(regex, 'href=\"/$1/\"');
    fs.writeFileSync(f, newContent);
    changed++;
  }
});
console.log('Fixed ' + changed + ' files');
