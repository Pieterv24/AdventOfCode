const fs = require('fs');
const readline = require('readline');

async function processLineByLine() {
    const fileStream = fs.createReadStream('input.txt');

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    const countArray = [];

    for await (const line of rl) {
        // Walk through bytes, and register counts in array.
        // If counter in array is negative, the most common is 0
        // If positive, the most common is 1
        // The least common can be determined by taking the opposite of the most common
        for (let i = 0; i < line.length; i++) {
            const bit = parseInt(line[i]);

            // Init on 0 if no entry is there yet
            if (!countArray[i]) {
                countArray[i] = 0;
            }

            if (bit == 0) {
                countArray[i] -= 1;
            } else if (bit == 1) {
                countArray[i] += 1;
            }
        }
    }

    // Get most common bits from gamma
    let gammaValue = '';
    let epsilonValue = '';
    for (const bit of countArray) {
        gammaValue += bit > 0 ? '1' : '0';
        epsilonValue += bit < 0 ? '1' : '0';
    }

    console.log(countArray);
    console.log(gammaValue);
    console.log(epsilonValue);

    const decimalGamma = parseInt(gammaValue, 2);
    const decimalEpsilon = parseInt(epsilonValue, 2);

    console.log(`Gamma value is ${decimalGamma}`);
    console.log(`Epsilon value is ${decimalEpsilon}`);
    console.log(`Power consumption is ${decimalGamma * decimalEpsilon}`);
}

processLineByLine();