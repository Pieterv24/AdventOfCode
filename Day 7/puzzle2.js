const fs = require('fs');

const inputFile = 'input.txt';

const crabArray = fs.readFileSync(inputFile).toString().split(',').map(value => parseInt(value));

let lowestFuel = Number.MAX_VALUE;
for (let i = 0; i < Math.max(...crabArray); i++) {
    let totalFuel = 0;
    crabArray.map(value => {
        const moves = Math.abs(i - value);
        totalFuel += (moves*(moves+1))/2
    });

    lowestFuel = totalFuel < lowestFuel ? totalFuel : lowestFuel;
}

console.log(lowestFuel);