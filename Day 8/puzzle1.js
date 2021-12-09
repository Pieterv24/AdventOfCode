const fs = require('fs');
const readline = require('readline');

const inputFile = 'input.txt';

async function processLineByLine() {
    const fileStream = fs.createReadStream(inputFile);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let counter = 0;

    for await (const line of rl) {
        const digits = line.split('|')[1].trim().split(' ');

        // Filter array to only contain the needed values
        const filteredDigits = digits.filter(dg => dg.length === 2 || dg.length === 3 || dg.length === 4 || dg.length === 7);

        counter += filteredDigits.length;
    }

    console.log(counter);
}

processLineByLine();