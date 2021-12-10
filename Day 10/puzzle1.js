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
 * @returns 
 */
function checkIllegalClosure(chars, openStack = []) {
    // Stop if no chars remain
    if (chars.length <= 0) {
        return '';
    }
    // Preliminary sanity check
    if (openStack.length === 0 && closeChars.includes(chars[0])) {
        return chars[0];
    }
    const currentChar = chars[0];
    const isOpening = openChars.includes(currentChar);

    if (isOpening) {
        return checkIllegalClosure(chars.slice(1), [...openStack, currentChar]);
    } else {
        if (openChars.indexOf(openStack[openStack.length - 1]) === closeChars.indexOf(currentChar)) {
            return checkIllegalClosure(chars.slice(1), openStack.slice(0, -1));
        } else {
            return currentChar;
        }
    }
}

async function processLineByLine() {
    const args = process.argv.slice(2);
    const fileStream = fs.createReadStream(args.includes('sample') ? sampleFile : inputFile);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    // ): 3 points.
    // ]: 57 points.
    // }: 1197 points.
    // >: 25137 points.
    let score = 0;

    for await (const line of rl) {
        const illegalChar = checkIllegalClosure(line);

        switch(illegalChar) {
            case ')':
                score += 3;
                break;
            case ']':
                score += 57;
                break;
            case '}':
                score += 1197;
                break;
            case '>':
                score += 25137;
                break;
        }
    }

    console.log(`The Score is: ${score}`)
}

processLineByLine();