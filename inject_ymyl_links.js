const fs = require('fs');
const path = require('path');

const directoryPath = path.join(__dirname, 'src', 'content', 'blog');
const referenceText = `\n\n## Medical & Ergonomic References\n\nFor further reading on the impact of proper breast support on posture, back pain, and overall health, we recommend consulting these authoritative medical resources:\n*   [NHS Guide to Back Pain and Posture](https://www.nhs.uk/conditions/back-pain/)\n*   [Mayo Clinic: Breast Health Basics](https://www.mayoclinic.org/healthy-lifestyle/womens-health/basics/breast-health/hlv-20049411)\n*   [National Institutes of Health (NIH): Ergonomics and Musculoskeletal Health](https://www.nih.gov/)\n\n`;

fs.readdir(directoryPath, function (err, files) {
    if (err) {
        return console.log('Unable to scan directory: ' + err);
    } 

    files.forEach(function (file) {
        if (file.endsWith('.md')) {
            const filePath = path.join(directoryPath, file);
            let content = fs.readFileSync(filePath, 'utf8');

            const hasExternalLink = /http[s]?:\/\/(?!brasizechecker\.com|localhost|.*github)/.test(content);
            const hasRefs = content.includes('Medical & Ergonomic References');

            if (!hasExternalLink && !hasRefs) {
                // Insert right before "## Stop Guessing" CTA or before "## Frequently Asked Questions" if CTA doesn't exist
                if (content.includes('## Stop Guessing')) {
                    content = content.replace('## Stop Guessing', referenceText + '## Stop Guessing');
                } else if (content.includes('## Frequently Asked')) {
                    content = content.replace('## Frequently Asked', referenceText + '## Frequently Asked');
                } else {
                    content += referenceText;
                }

                fs.writeFileSync(filePath, content, 'utf8');
                console.log(`Injected authoritative YMYL external links into: ${file}`);
            }
        }
    });
});
