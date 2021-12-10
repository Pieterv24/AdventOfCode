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

    const heightMap = [];

    for await (const line of rl) {
        heightMap.push(line.split('').map(value => parseInt(value)));
    }

    const lowPoints = [];
    console.log(heightMap);
    for (let y = 0; y < heightMap.length; y++) {
        for (let x = 0; x < heightMap[y].length; x++) {
            const locationValue = heightMap[y][x];
            if (locationValue === 9) {
                continue;
            }
            console.log(`Checking for ${x}, ${y}`)
            const adjacentCoords = [[x, y+1], [x, y-1], [x-1, y], [x+1, y]].filter(coord => coord[0] >= 0 && coord[1] >= 0 && coord[0] < heightMap[y].length && coord[1] < heightMap.length);
            console.log(adjacentCoords);
            if (adjacentCoords.reduce((pv, cv) => pv && locationValue < heightMap[cv[1]][cv[0]], true)) {
                lowPoints.push(locationValue);
            }
        }
    }

    const awnser = lowPoints.map(point => point + 1).reduce((pv, cv) => pv + cv, 0);

    console.log(`The awnser is: ${awnser}`);
}

processLineByLine();