const fs = require('fs');
const readline = require('readline');

async function processLineByLine() {
    const fileStream = fs.createReadStream('input.txt');

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let entriesRead = 0;
    let counter = 0;
    let previous = Number.MAX_VALUE;
    for await (const line of rl) {
        const lineNumber = parseInt(line);
        const isGreater = lineNumber > previous;

        // console.log(`${line} is ${isGreater ? 'greater' : 'less'} than ${previous}`);
        if (lineNumber == previous) {
            console.log(`${lineNumber} and ${previous} are equal`)
        }

        previous = lineNumber;
        counter += isGreater ? 1 : 0;
        entriesRead++;
    }
    console.log(`Total instances is: ${counter}`)
    console.log(`${entriesRead} entries were read`)
}

processLineByLine();