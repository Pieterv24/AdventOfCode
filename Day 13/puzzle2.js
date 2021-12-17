const fs = require('fs');
const readline = require('readline');

const inputFile = 'input.txt';
const sampleFile = 'sampleInput.txt';

class Grid {
    constructor(...values) {
        this.xGridSize = 1;
        this.yGridSize = 1;

        this.grid = [['.']];

        if (values.length > 0) {
            values.map(coord => this.addToGrid(coord, '#'));
        }
    }

    addToGrid(coord, value) {
        const x = coord[0];
        const y = coord[1];

        // Expand grid if dot is outside of it
        if (x >= this.xGridSize || y >= this.yGridSize) {
            this.__expandGrid(x >= this.xGridSize ? x + 1 : this.xGridSize, y >= this.yGridSize ? y + 1 : this.yGridSize);
        }

        this.grid[y][x] = value;
    }

    __expandGrid(xSize, ySize) {
        // Sanity check
        if (xSize < this.xGridSize || ySize < this.yGridSize) {
            throw new Error('You cannot shrink the grid');
        }
        this.xGridSize = xSize;
        this.yGridSize = ySize;

        const newGrid = [...Array(ySize)].map(row => Array(xSize).fill('.'));

        this.grid.map((row, y) => row.map((value, x) => newGrid[y][x] = value));

        this.grid = newGrid;
    }

    foldGrid(direction, location) {
        const newGrid = [...Array(direction === 'y' ? location : this.yGridSize)]
            .map(e => Array(direction === 'x' ? location : this.xGridSize).fill('.'));

        if (direction === 'y') {
            for (let y = 0; y < location; y++) {
                for (let x = 0; x < this.xGridSize; x++) {
                    const stillSide = this.grid[y][x];
                    const foldSide = this.grid[this.yGridSize - y - 1][x];

                    newGrid[y][x] = stillSide === '#' || foldSide === '#' ? '#' : '.';
                }
            }
            this.yGridSize = location;
        }
        if (direction === 'x') {
            for (let y = 0; y < this.yGridSize; y++) {
                for (let x = 0; x < location; x++) {
                    const stillSide = this.grid[y][x];
                    const foldSide = this.grid[y][this.xGridSize - x - 1];

                    newGrid[y][x] = stillSide === '#' || foldSide === '#' ? '#' : '.';
                }
            }
            this.xGridSize = location;
        }

        this.grid = newGrid;
    }

    countDots() {
        return this.grid.reduce((pv, cv) => pv + cv.reduce((ppv, ccv) => ccv === '#' ? ++ppv : ppv, 0), 0);
    }

    toString() {
        let outputString = '';
        this.grid.map(row => outputString += row.join('') + '\n');

        return outputString;
    }
}

async function processLineByLine() {
    const args = process.argv.slice(2);
    const fileStream = fs.createReadStream(args.includes('sample') ? sampleFile : inputFile);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let paper = new Grid();
    const foldInstructions = [];

    for await (const line of rl) {
        if (line.includes('fold along')) {
            foldInstructions.push(line.split(' ')[2].split('='));
        } else if (line.length > 1) {
            paper.addToGrid(line.split(',').map(val => parseInt(val)), '#');
        }
    }

    console.log(paper.toString());
    console.log(`The paper has a size of ${paper.xGridSize}, ${paper.yGridSize}`);
    for (const instruction of foldInstructions) {
        console.log(`Folding along ${instruction[0]} axis`);

        paper.foldGrid(instruction[0], parseInt(instruction[1]));
        console.log(paper.toString());
    }

    console.log(`After folding, ${paper.countDots()} dots are visible`);
}

processLineByLine();