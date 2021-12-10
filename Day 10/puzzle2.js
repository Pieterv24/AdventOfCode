const fs = require('fs');
const readline = require('readline');

const inputFile = 'input.txt';
const sampleFile = 'sampleInput.txt';

const openChars = ['(', '[', '{', '<'];
const closeChars = [')', ']', '}', '>']

/**
 * 
 * @param {String} chars 
 * @param {Array} openingChar 
 * @returns {Boolean} Char is either legal or not
 */
function checkIllegalClosure(chars, openStack = []) {
    // Stop if no chars remain
    if (chars.length <= 0) {
        return false;
    }
    // Preliminary sanity check
    if (openStack.length === 0 && closeChars.includes(chars[0])) {
        return true;
    }
    const currentChar = chars[0];
    const isOpening = openChars.includes(currentChar);

    if (isOpening) {
        return checkIllegalClosure(chars.slice(1), [...openStack, currentChar]);
    } else {
        if (openChars.indexOf(openStack[openStack.length - 1]) === closeChars.indexOf(currentChar)) {
            return checkIllegalClosure(chars.slice(1), openStack.slice(0, -1));
        } else {
            return true;
        }
    }
}

/**
 * 
 * @param {String} chars 
 * @param {Array} openStack Stack of unclosed openChars
 * @returns {Array} Returns Stack of unclosed openChars
 */
function findUnclosedChars(chars, openStack = []) {
    // Stop if no chars remain
    if (chars.length <= 0) {
        return openStack;
    }

    const currentChar = chars[0];
    const isOpening = openChars.includes(currentChar);

    if (isOpening) {
        return findUnclosedChars(chars.slice(1), [...openStack, currentChar]);
    } else {
        return findUnclosedChars(chars.slice(1), openStack.slice(0, -1));
    }
}

function findCompletionString(chars) {
    const unclosedChars = findUnclosedChars(chars);
    
    const completionString = [];

    while (unclosedChars.length > 0) {
        completionString.push(closeChars[openChars.indexOf(unclosedChars.pop())])
    }

    return completionString;
}

async function processLineByLine() {
    const args = process.argv.slice(2);
    const fileStream = fs.createReadStream(args.includes('sample') ? sampleFile : inputFile);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    /**
     * Score starts at 0, and for each char it is 5x score value + value of the char
     * ): 1 point.
     * ]: 2 points.
     * }: 3 points.
     * >: 4 points.
     * 
     * The winner is the middle score
     */
    const scoreArray = [')', ']', '}', '>'];
    let scoreBoard = [];

    for await (const line of rl) {
        // Skip lines with illegal closure
        if (checkIllegalClosure(line)) {
            continue;
        }

        const completionString = findCompletionString(line);
        scoreBoard.push(completionString.reduce((pv, cv) => (pv * 5) + (scoreArray.indexOf(cv) + 1)  , 0));
    }

    scoreBoard.sort((a, b) => a - b);
    console.log(`The winning score is: ${scoreBoard.at(Math.ceil(scoreBoard.length/2) - 1)}`);
}

processLineByLine();