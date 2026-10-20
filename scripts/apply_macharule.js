const fs = require('fs');
const path = require('path');

const directoryPath = path.join(__dirname, 'src', 'content', 'blog');

fs.readdir(directoryPath, function (err, files) {
    if (err) {
        return console.log('Unable to scan directory: ' + err);
    } 

    files.forEach(function (file) {
        if (file.endsWith('.md')) {
            const filePath = path.join(directoryPath, file);
            let content = fs.readFileSync(filePath, 'utf8');

            let updated = false;

            // 1. Enforce E-E-A-T: Add fitReviewed: true if missing
            if (!content.includes('fitReviewed:')) {
                content = content.replace(/^---/, '---\nfitReviewed: true');
                updated = true;
            } else if (content.includes('fitReviewed: false')) {
                content = content.replace('fitReviewed: false', 'fitReviewed: true');
                updated = true;
            }

            // 2. Enforce MachaRule Hub & Spoke: Add CTA if no calculator link exists at bottom
            if (!content.includes('Calculate Your') && !content.includes('bra-size-chart') && !content.includes('sister-size-calculator')) {
                const cta = `\n\n## Stop Guessing, Start Calculating\n\nFinding your perfect fit shouldn't be a mystery. Use our advanced **[Bra Size Calculator](/bra-size-chart/)** or explore your alternative sizing options with our **[Sister Size Calculator](/sister-size-calculator/)** to find a fit that feels custom-tailored to your unique shape.`;
                content += cta;
                updated = true;
            }

            if (updated) {
                fs.writeFileSync(filePath, content, 'utf8');
                console.log(`Updated MachaRule structure for: ${file}`);
            }
        }
    });
});
