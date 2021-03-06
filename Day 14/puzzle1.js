const fs = require('fs');
const readline = require('readline');

const inputFile = 'input.txt';
const sampleFile = 'sampleInput.txt';

function addStep(template, rules) {
    let polymer = '';

    for (let i = 0; i < template.length - 1; i++) {
        const pair = template.slice(i, i+2);
        polymer += `${pair[0]}${rules[pair]}`
    }

    return polymer + template[template.length-1];
}

async function processLineByLine() {
    const args = process.argv.slice(2);
    const fileStream = fs.createReadStream(args.includes('sample') ? sampleFile : inputFile);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let template = '';
    let rules = {};

    for await (const line of rl) {
        if (line.includes('->')) {
            const rule = line.split(' -> ');
            rules[rule[0]] = rule[1];
        } else if (line.length > 1) {
            template = line;
        }
    }

    console.log(template);
    console.log(rules);
    
    const steps = 10;
    let currentPolymer = template;
    for (let i = 0; i < steps; i++) {
        currentPolymer = addStep(currentPolymer, rules);
        console.log(currentPolymer);
    }

    // const elementCount = currentPolymer.split('').reduce((pv, cv) => pv.get(cv) ? pv.set(cv, pv.get(cv) + 1) : pv.set(cv, 1), new Map());
    const elementCount = currentPolymer.split('').reduce((pv, cv) => (pv[cv] ? pv[cv]++ : pv[cv] = 1, pv), {});
    const highest = Math.max(...Object.values(elementCount));
    const lowest = Math.min(...Object.values(elementCount));

    console.log(`The answer is: ${highest - lowest}`);
}

processLineByLine();