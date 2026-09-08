const fs = require('fs');
const path = require('path');

const distDir = path.join(__dirname, '../dist');
const API_KEY = '919b9e2f83484d43abea1fdc52f2a2a3';
const HOST = 'brasizechecker.com';
const KEY_LOCATION = `https://${HOST}/${API_KEY}.txt`;

async function submitIndexNow() {
  try {
    const urlList = [];
    
    function walk(dir) {
      const files = fs.readdirSync(dir);
      for (const file of files) {
        const filepath = path.join(dir, file);
        if (fs.statSync(filepath).isDirectory()) {
          walk(filepath);
        } else if (filepath.endsWith('.html')) {
          let relativePath = path.relative(distDir, filepath).replace(/\\/g, '/');
          
          if (relativePath === 'index.html') {
            urlList.push(`https://${HOST}/`);
            continue;
          }
          
          if (relativePath.endsWith('index.html')) {
            relativePath = relativePath.slice(0, -10);
          }
          
          urlList.push(`https://${HOST}/${relativePath}`);
        }
      }
    }
    
    if (fs.existsSync(distDir)) {
      walk(distDir);
    } else {
      console.log('No dist directory found. Make sure to build first.');
      return;
    }

    console.log(`Found ${urlList.length} URLs. Submitting to IndexNow...`);

    const payload = {
      host: HOST,
      key: API_KEY,
      keyLocation: KEY_LOCATION,
      urlList: urlList
    };

    const response = await fetch('https://www.bing.com/indexnow', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      },
      body: JSON.stringify(payload)
    });

    if (response.ok || response.status === 200 || response.status === 202) {
      console.log(`[${HOST}] Successfully submitted to IndexNow. Status:`, response.status);
    } else {
      console.error(`[${HOST}] Failed to submit. Status:`, response.status);
      const text = await response.text();
      console.error('Response:', text);
    }

  } catch (error) {
    console.error(`[${HOST}] Error submitting to IndexNow:`, error);
  }
}

submitIndexNow();
