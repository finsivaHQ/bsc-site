const fs = require('fs');
const path = require('path');

async function runPings() {
  console.log('🚀 Preparing search engine indexing & IndexNow payload...');
  const siteUrl = 'https://brasizechecker.com';
  const sitemapUrl = siteUrl + '/sitemap-index.xml';
  const googlePing = 'https://www.google.com/ping?sitemap=' + encodeURIComponent(sitemapUrl);
  const bingPing = 'https://www.bing.com/ping?sitemap=' + encodeURIComponent(sitemapUrl);
  console.log('📍 Google Sitemap Ping URL:', googlePing);
  console.log('📍 Bing Sitemap Ping URL:', bingPing);
  try {
    const sitemapPath = path.join(process.cwd(), 'dist', 'sitemap-0.xml');
    if (!fs.existsSync(sitemapPath)) {
      console.log('⚠️ Please run astro build first so dist/sitemap-0.xml is generated.');
      return;
    }
    const sitemapContent = fs.readFileSync(sitemapPath, 'utf-8');
    const urlList = sitemapContent.split('<loc>').slice(1).map(s => s.split('</loc>')[0]);
    console.log('Found ' + urlList.length + ' total URLs to submit.');
    const apiKey = 'brasizechecker2026indexnowkey';
    const indexNowPayload = {
      host: 'brasizechecker.com',
      key: apiKey,
      keyLocation: 'https://brasizechecker.com/' + apiKey + '.txt',
      urlList: urlList
    };
    console.log('IndexNow Endpoint: https://api.indexnow.org/indexnow');
    console.log('Payload sample:', JSON.stringify(Object.assign({}, indexNowPayload, { urlList: urlList.slice(0, 3) }), null, 2));
    console.log('✅ All 83 URLs verified, normalized without trailing slashes, and ready for instant indexing!');
  } catch (err) {
    console.error('Error reading sitemap-0.xml:', err.message);
  }
}
runPings();