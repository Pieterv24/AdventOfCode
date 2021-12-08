const fs = require('fs');
const readline = require('readline');

const inputFile = 'sampleInput.txt';

/**
 * 6 segments: 0, 6, 9 (differentiating segments: )
 * 2 segments: 1
 * 5 segments: 2, 3, 5 (differentiating segments: )
 * 4 segments: 4
 * 3 segments: 7
 * 7 segments: 8
 */
const segments = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

async function processLineByLine() {
    const fileStream = fs.createReadStream(inputFile);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    for await (const line of rl) {
        
    }
}

processLineByLine();