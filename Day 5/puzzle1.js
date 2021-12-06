const fs = require('fs');
const readline = require('readline');

const gridSize = 10;

function calcLinePoints(x1,y1,x2,y2) {
    console.log(`[${x1},${y1}], [${x2},${y2}]`);
    const linePoints = [];

    if (x1 !== x2 && y1 !== y2) {
        console.log('diagnals can be ignores');
        return linePoints;
    }

    const delta_x = x2 - x1;
    const delta_y = y2 - y1;
    console.log(`delta_x: ${delta_x} | delta_y: ${delta_y}`);

    // Since only accounting for horizontal or vertical, the amount of points can be calculated
    // Based on the one that is 0, because there always is one
    const points = delta_x === 0 ? Math.abs(delta_y) : Math.abs(delta_x);
    console.log(`Theres: ${points} points`);
    
    // Calc movement for each point
    const interval_x = delta_x / points;
    const interval_y = delta_y / points;
    console.log(`For each point x moves: ${interval_x}`);
    console.log(`For each point y moves: ${interval_y}`)

    linePoints.push([x1,y1]);
    for (let i = 1; i < points + 1; i++) {
        const point = [x1 + (interval_x * i), y1 + (interval_y * 1)];
        linePoints.push(point);
    }

    console.log(linePoints);
}

async function processLineByLine() {
    const fileStream = fs.createReadStream('sampleInput.txt');

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    const grid = [...Array(gridSize)].map(e => Array(gridSize));
    const readRegex = /(\d+),(\d+) -> (\d+),(\d+)/
    for await (const line of rl) {
        const match = line.match(readRegex);
        const x1 = parseInt(match[1]);
        const y1 = parseInt(match[2]);
        const x2 = parseInt(match[3]);
        const y2 = parseInt(match[4]);

        calcLinePoints(x1,y1,x2,y2);
    }
}

processLineByLine();