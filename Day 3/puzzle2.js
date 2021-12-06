const fs = require('fs');
const readline = require('readline');

function getCountForPos(inputArray, position) {
    let count = 0;
    for (const byte of inputArray) {
        // Walk through bytes, and register counts in array.
        // If counter in array is negative, the most common is 0
        // If positive, the most common is 1
        // The least common can be determined by taking the opposite of the most common
        const bit = parseInt(byte[position]);

        if (bit == 0) {
            count -= 1;
        } else if (bit == 1) {
            count += 1;
        }
    }
    return count;
}

function filterArray(inputArray, position, requiredValue) {
    return  inputArray.filter((value) => value[position] === requiredValue);
}

async function processLineByLine() {
    const fileStream = fs.createReadStream('input.txt');

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    const initialArray = [];

    for await (const line of rl) {
        initialArray.push(line);
    }

    let genArray = [...initialArray];
    let genPosition = 0;
    do {
        genArray = filterArray(genArray, genPosition, getCountForPos(genArray, genPosition) >= 0 ? '1' : '0' );
        console.log(`${genArray.length} Genrerator Entries left`)
        genPosition++;
    } while (genArray.length > 1);

    let scrubArray = [...initialArray];
    let scrubPosition = 0;
    do {
        scrubArray = filterArray(scrubArray, scrubPosition, getCountForPos(scrubArray, scrubPosition) >= 0 ? '0' : '1' );
        console.log(`${scrubArray.length} Scrubber Entries left`)
        scrubPosition++;
    } while (scrubArray.length > 1);

    console.log(genArray[0]);
    console.log(scrubArray[0]);

    const decimalGenerator = parseInt(genArray[0], 2);
    const decimalScrub = parseInt(scrubArray[0], 2);

    console.log(`Generator rating is ${decimalGenerator}`);
    console.log(`Scrubber rating is ${decimalScrub}`);
    console.log(`The awnser is: ${decimalGenerator * decimalScrub}`);
}

processLineByLine();