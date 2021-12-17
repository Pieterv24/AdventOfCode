const fs = require('fs');
const readline = require('readline');

const inputFile = 'input.txt';
const sampleFile = 'sampleInput.txt';

/**
 * 
 * @param {Array} template 
 * @param {Object} rules 
 * @returns 
 */
function addStep(pairCounter, rules) {
    const newPairCounter = {...pairCounter};
    // Reset counts
    Object.keys(newPairCounter).forEach(pair => newPairCounter[pair] = 0);

    Object.keys(pairCounter).forEach(pair => {
        const newPairs = rules[pair];
        const currentCount = pairCounter[pair];

        newPairs.forEach(newPair => newPairCounter[newPair] += currentCount)
    });

    return newPairCounter;
}

async function processLineByLine() {
    const args = process.argv.slice(2);
    const fileStream = fs.createReadStream(args.includes('sample') ? sampleFile : inputFile);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let template = [];
    let rules = {};

    for await (const line of rl) {
        if (line.includes('->')) {
            const rule = line.split(' -> ');
            const newPairs = [rule[0][0] + rule[1], rule[1] + rule[0][1]]
            rules[rule[0]] = newPairs;
        } else if (line.length > 1) {
            template = line;
        }
    }

    console.log(template);
    console.log(rules);
    
    const steps = 40;
    let currentPolymer = {};
    // Add Pair counters
    Object.keys(rules).forEach(pair => currentPolymer[pair] = 0);
    
    const templatePairs = template.split('').map((e, i) => i < template.length - 1 ? e + template[i+1] : undefined).filter(e => e !== undefined);
    templatePairs.forEach(pair => currentPolymer[pair]++);

    for (let i = 0; i < steps; i++) {
        currentPolymer = addStep(currentPolymer, rules);
        console.log(currentPolymer);
    }

    const countOccurences = {};
    Object.keys(currentPolymer).forEach((pair, index) => {
        if (!countOccurences[pair[0]]) {
            countOccurences[pair[0]] = 0;
        }
        countOccurences[pair[0]] += currentPolymer[pair];
        if (index == Object.keys(currentPolymer).length - 1) {
            if (!countOccurences[pair[1]]) {
                countOccurences[pair[1]] = 0;
            }
            countOccurences[pair[1]] += currentPolymer[pair];
        }
    });
    // Add 1 count for last polymer node
    countOccurences[template[template.length - 1]] += 1;

    const highest = Math.max(...Object.values(countOccurences));
    const lowest = Math.min(...Object.values(countOccurences));

    console.log(`The answer is: ${highest - lowest}`);
}

processLineByLine();

