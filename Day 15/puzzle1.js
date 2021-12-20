const fs = require('fs');
const path = require('path/posix');
const readline = require('readline');

const inputFile = 'input.txt';
const sampleFile = 'sampleInput.txt';

/**
 * 
 * @param {[][]} grid 
 * @param {[[]]} path 
 */
function getPossiblePaths(grid, path) {
    const [x, y] = path[path.length - 1];
    
    if (!(x < grid[y].length && x >= 0 && y < grid.length && y >= 0)) {
        throw new Error('position is out of range of grid');
    }
    const possibleCoords = [[x, y+1], [x, y-1], [x-1, y], [x+1, y]]
        .filter(coord => 
            coord[0] >= 0 
            && coord[1] >= 0 
            && coord[0] < grid[y].length 
            && coord[1] < grid.length
            && !path.map(e => e.join(',')).includes(coord.join(','))
        );
    
    return possibleCoords
}

/**
 * 
 * @param {[[]]} grid 
 * @param {[[]]} path 
 */
function getPathRiskScore(grid, path) {
    let riskScore = 0;
    path.forEach((position, index) => {
        if (index > 0) {
            const [x, y] = position;
            riskScore += grid[y][x];
        }
    });
    return riskScore;
}

function getLowestPath(paths) {
    let lowestScore = {index: -1, path: { score: Number.MAX_VALUE}}
    paths.forEach((path, index) => lowestScore = path.score < lowestScore.path.score ? {index, path} : lowestScore);
    return lowestScore;
}

async function processLineByLine() {
    const args = process.argv.slice(2);
    const fileStream = fs.createReadStream(args.includes('sample') ? sampleFile : inputFile);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    const startPoint = [0, 0];
    const grid = [];

    for await (const line of rl) {
        grid.push(line.split('').map(e => parseInt(e)));
    }

    const endPoint = [grid[0].length - 1, grid.length - 1];

    let paths = [];
    paths.push({
        path: [startPoint]
    });

    while(true) {
        // Grade all paths
        paths = paths.map(path => {
            if (!path.score)
                return {...path, score: getPathRiskScore(grid, path.path)}
            return path;
        });

        const {index, path} = getLowestPath(paths);
        console.log(`Lowest path: ${JSON.stringify(path)}, on index: ${index}`);
        const nextPaths = getPossiblePaths(grid, path.path);

        // Create new path for lowest possible paths
        paths.splice(index);
        nextPaths.forEach(nextPath => {
            const newPath = [...path.path, nextPath];
            paths.push({
                path: newPath,
                score: getPathRiskScore(grid, newPath)
            })
        });

        // check if end is reached
        const endReached = paths.reduce((pv, cv) => pv || cv.path[cv.path.length - 1].join(',') === endPoint.join(','), false);
        if (endReached) {
            console.log("End is reached");
            break;
        }
    }
}

processLineByLine();