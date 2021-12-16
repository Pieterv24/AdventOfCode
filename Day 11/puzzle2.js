const fs = require('fs');

const inputFile = 'input.txt';
const sampleFile = 'sampleInput.txt';

function getFileContent() {
    const args = process.argv.slice(2);
    return fs.readFileSync(args.includes('sample') ? sampleFile : inputFile).toString();
}

function createGrid(input) {
    return input.split('\n').map(row => row.split('').map(value => parseInt(value)));
}

function printGrid(grid) {
    grid.map(row => console.log(row.map(val => val > 9 ? '\x1b[34m' + 0 + '\x1b[0m' : val).join('')));
}

function increaseAllCells(grid) {
    const newGrid = [...grid.map(row => [...row])];

    return newGrid.map(row => row.map(value => value+1));
}

function getFlashingOctoPi(grid) {
    const flashingOctopi = [];

    grid.map((row, y) => row.map((value, x) => value > 9 ? flashingOctopi.push([parseInt(x), parseInt(y)]) : ''));

    return flashingOctopi;
}

function areAllFlashing(grid) {
    return grid.reduce((pv, cv) => pv && cv.reduce((ppv, ccv) => ppv && ccv > 9, true), true);
}

function stepGrid(grid, step = 1) {
    let flashes = new Set();

    let newGrid = increaseAllCells(grid);
    let flashingOctopi = getFlashingOctoPi(newGrid)
    
    while(flashingOctopi.length > 0) {
        flashingOctopi.map(value => flashes.add(value.join(',')));
        for (const coord of flashingOctopi) {
            const x = coord[0];
            const y = coord[1];
            const moves = [-1, 0, 1];
            moves.forEach(dy => moves.forEach(dx => {
                if (
                    !(dx === 0 && dy === 0) 
                    && (dx + x >= 0 && dx + x < newGrid[0].length) 
                    && (dy + y >= 0 && dy + y < newGrid.length)
                ) {
                    newGrid[dy+y][dx+x] = newGrid[dy+y][dx+x] + 1;
                }
            }));
        }

        flashingOctopi = getFlashingOctoPi(newGrid).filter(value => !flashes.has(value.join(',')));
    }

    console.log(`----------------------Iteration--------------------------`)
    printGrid(newGrid);

    const allFlashing = areAllFlashing(newGrid);

    newGrid = newGrid.map(row => row.map(val => val > 9 ? 0 : val));

    return allFlashing ? step : stepGrid(newGrid, ++step);
}

const input = getFileContent();
const grid = createGrid(input);
console.log('------------------start grid ---------------------------')
printGrid(grid);

// console.log(grid);
console.log(stepGrid(grid))