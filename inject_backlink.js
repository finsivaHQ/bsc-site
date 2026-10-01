const fs = require('fs');

const file = 'src/content/blog/sister-sizing-weight-loss-gain-34c-36b.md';
let content = fs.readFileSync(file, 'utf8');

// Find the target sentence
const target = 'If you\'ve recently experienced weight fluctuations—whether from dieting, a new fitness routine, or pregnancy';
const replacement = 'If you\'ve recently experienced weight fluctuations—whether from dieting, using a [calorie calculator](https://caloriecalculatorfree.com/) to manage your daily intake, a new fitness routine, or pregnancy';

if (content.includes(target)) {
    content = content.replace(target, replacement);
    fs.writeFileSync(file, content, 'utf8');
    console.log('Backlink inserted successfully.');
} else {
    // try a regex approach in case of hidden encoding quirks
    const regex = /whether from dieting, a new fitness routine, or pregnancy/i;
    if (regex.test(content)) {
        content = content.replace(regex, 'whether from dieting, using a [calorie calculator](https://caloriecalculatorfree.com/) to manage your daily intake, a new fitness routine, or pregnancy');
        fs.writeFileSync(file, content, 'utf8');
        console.log('Backlink inserted successfully via regex.');
    } else {
        console.log('Could not find the target string in the file.');
    }
}
