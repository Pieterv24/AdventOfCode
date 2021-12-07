const fs = require('fs');

const inputFile = 'input.txt';

const growthDays = 256;
const maxSpawnTime = 8;

function createInitialMap(numbers) {
    const initialMap = {};
    for (let i = 0; i <= maxSpawnTime; i++) {
        initialMap[i] = 0;
    }
    numbers.map(value => {
        initialMap[value]++;
    });
    return initialMap;
}

// Read file, split on , and map all values to numbers before adding them to the initial map
let stateMap =  createInitialMap(fs.readFileSync(inputFile).toString().split(',').map(value => parseInt(value)));

console.log(stateMap);
console.log(`Initial state: ${JSON.stringify(stateMap)}`);
for (let i = 0; i < growthDays; i++) {
    const newMap = createInitialMap([]);
    for (const key of Object.keys(stateMap)) {
        if (parseInt(key) - 1 < 0) {
            newMap[8] += stateMap[key];
            newMap[6] += stateMap[key];
            continue;
        }
        newMap[parseInt(key) - 1] += stateMap[key];
    }
    stateMap = {...newMap};
    console.log(`After day ${i+1}: ${JSON.stringify(stateMap)}`);
}
const count = Object.keys(stateMap).reduce((pv, cv) => pv + stateMap[cv], 0)
console.log(`After ${growthDays}, there are ${count} fish`);