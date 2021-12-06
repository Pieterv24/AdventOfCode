const fs = require('fs');
const readline = require('readline');

async function processLineByLine() {
    const fileStream = fs.createReadStream('input.txt');

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    const dirReg = /(\w+) (\d+)/;

    let depth = 0;
    let distance = 0;

    for await (const line of rl) {
        const match = line.match(dirReg);
        const direction = match[1];
        const value = parseInt(match[2]);

        switch(direction) {
            case 'up':
                depth -= value;
                break;
            case 'down':
                depth += value;
                break;
            case 'forward':
                distance += value;
                break;
        }
    }

    console.log(`You've traveled ${distance} units and are on a depth of ${depth} units`);
    console.log(`Multiplying this gives: ${distance * depth}`)
}

processLineByLine();