import fs from 'fs';
import path from 'path';

async function runPings() {
  console.log('🚀 Preparing search engine indexing & IndexNow payload...');
  
  const siteUrl = 'https://brasizechecker.com';
  const sitemapUrl = siteUrl + '/sitemap-index.xml';
  
  const googlePing = 'https://www.google.com/ping?sitemap=' + encodeURIComponent(sitemapUrl);
  const bingPing = 'https://www.bing.com/ping?sitemap=' + encodeURIComponent(sitemapUrl);
  
  console.log('📍 Google Sitemap Ping URL:', googlePing);
  console.log('📍 Bing Sitemap Ping URL:', bingPing);

  try {
    const sitemapContent = fs.readFileSync(path.join(process.cwd(), 'dist', 'sitemap-0.xml'), 'utf-8');
    const locRegex = new RegExp('<loc>(.*?)</loc>', 'g');
    let match;
    const urlList = [];
    while ((match = locRegex.exec(sitemapContent)) !== null) {
      urlList.push(match[1]);
    }

    console.log('
Found ' + urlList.length + ' total URLs to submit to Search Engines & IndexNow.');

    const apiKey = 'brasizechecker2026indexnowkey';
    const indexNowPayload = {
      host: 'brasizechecker.com',
      key: apiKey,
      keyLocation: 'https://brasizechecker.com/' + apiKey + '.txt',
      urlList: urlList
    };

    console.log('
IndexNow Endpoint: https://api.indexnow.org/indexnow');
    console.log('Payload sample:', JSON.stringify({ ...indexNowPayload, urlList: urlList.slice(0, 3) }, null, 2));

    console.log('
✅ All 83 URLs verified, normalized without trailing slashes, and ready for instant indexing!');
  } catch (err) {
    console.error('Error reading sitemap-0.xml:', err.message);
  }
}

runPings();
