const fs = require('fs');
const readline = require('readline');

const inputFile = 'input.txt';
const sampleFile = 'sampleInput.txt';

function findHigherPoints(heightMap, location) {
    const x = location[0];
    const y = location[1];
    const currentValue = heightMap[y][x];

    const higherPoints = [];
    const adjacentCoords = [[x, y+1], [x, y-1], [x-1, y], [x+1, y]].filter(coord => coord[0] >= 0 && coord[1] >= 0 && coord[0] < heightMap[y].length && coord[1] < heightMap.length);

    adjacentCoords.filter(value => 
        heightMap[value[1]][value[0]] !== 9 && heightMap[value[1]][value[0]] > currentValue)
        .map(value => higherPoints.push(value));

    if (higherPoints.length > 0) {
        return [location, ...higherPoints, ...higherPoints.flatMap(point => findHigherPoints(heightMap, point))];
    } else {
        return [];
    }
}

function findBasin(heightMap, coord) {
    const basin = findHigherPoints(heightMap, coord);
    // Remove duplicates
    return [...new Set(basin.map(coord => coord.join(',')))].map(coord => coord.split(',').map(value => parseInt(value)));
}

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
    for (let y = 0; y < heightMap.length; y++) {
        for (let x = 0; x < heightMap[y].length; x++) {
            const locationValue = heightMap[y][x];
            if (locationValue === 9) {
                continue;
            }
            // console.log(`Checking for ${x}, ${y}`)
            const adjacentCoords = [[x, y+1], [x, y-1], [x-1, y], [x+1, y]].filter(coord => coord[0] >= 0 && coord[1] >= 0 && coord[0] < heightMap[y].length && coord[1] < heightMap.length);
            // console.log(adjacentCoords);
            if (adjacentCoords.reduce((pv, cv) => pv && locationValue < heightMap[cv[1]][cv[0]], true)) {
                lowPoints.push([x, y]);
            }
        }
    }

    // After gettign the low points, get the basins
    const basins = lowPoints.map(point => findBasin(heightMap,  point));
    console.log(basins.sort((a, b) => b.length - a.length).slice(0, 3).reduce((pv, cv) => pv * cv.length, 1));
}

processLineByLine();