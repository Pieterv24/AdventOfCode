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
    let aim = 0;

    for await (const line of rl) {
        const match = line.match(dirReg);
        const direction = match[1];
        const value = parseInt(match[2]);

        switch(direction) {
            case 'up':
                aim -= value;
                break;
            case 'down':
                aim += value;
                break;
            case 'forward':
                distance += value;
                depth += aim * value;
                console.log(`Moving ${value} forward`);
                console.log(`Moving ${aim} * ${value} = ${aim * value} in depth`);
                break;
        }
        console.log(`Position is now: { Distance: ${distance}, Depth: ${depth}, Aim: ${aim}}`)
    }

    console.log(`You've traveled ${distance} units and are on a depth of ${depth} units`);
    console.log(`Multiplying this gives: ${distance * depth}`)
}

processLineByLine();