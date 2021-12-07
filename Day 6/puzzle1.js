const fs = require('fs');

const inputFile = 'input.txt';

const growthDays = 80;

let state = fs.readFileSync(inputFile).toString().split(',');
state = state.map(value => parseInt(value));

console.log(`Initial state: ${JSON.stringify(state)}`);
for (let i = 0; i < growthDays; i++) {
    const newFish = [];
    const updatedFish = state.map(angler => {
        if (angler - 1 < 0) {
            newFish.push(8);
            return 6; 
        }
        return angler - 1;
    });
    state = [...updatedFish, ...newFish];
    console.log(`After day ${i+1}: ${JSON.stringify(state)}`);
}
console.log(`After ${growthDays}, there are ${state.length} fish`);