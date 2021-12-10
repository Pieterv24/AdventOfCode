const fs = require('fs');
const readline = require('readline');

const inputFile = 'input.txt';
const sampleFile = 'sampleInput.txt';

async function processLineByLine() {
    const args = process.argv.slice(2);
    const fileStream = fs.createReadStream(args.includes('sample') ? sampleFile : inputFile);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    for await (const line of rl) {
        
    }
}

processLineByLine();