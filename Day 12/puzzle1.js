const fs = require('fs');
const readline = require('readline');

const inputFile = 'input.txt';
const sampleFile = 'sampleInput.txt';

function traverseCaves(caves, route = ['start']) {
    const currentCave = route[route.length - 1];
    // Return if end is reached
    if (currentCave === 'end') {
        return route.join(',');
    }

    const possibleRoutes = caves[currentCave].connections
        .filter(cave => !(cave === cave.toLowerCase() && route.includes(cave)));

    return possibleRoutes.flatMap(cave => traverseCaves(caves, [...route, cave]));
}

async function processLineByLine() {
    const args = process.argv.slice(2);
    const fileStream = fs.createReadStream(args.includes('sample') ? sampleFile : inputFile);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    const caves = {};

    for await (const line of rl) {
        const [cave1, cave2] = line.split('-');

        caves[cave1] = {...caves[cave1], bigCave: cave1 === cave1.toUpperCase()};
        caves[cave2] = {...caves[cave2], bigCave: cave2 === cave2.toUpperCase()};

        caves[cave1].connections = caves[cave1].connections ? [...caves[cave1].connections, cave2] : [cave2];
        caves[cave2].connections = caves[cave2].connections ? [...caves[cave2].connections, cave1] : [cave1];
    }

    console.log(`${traverseCaves(caves).length} paths are possible`);
}

processLineByLine();