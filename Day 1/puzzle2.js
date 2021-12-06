const fs = require('fs');
const readline = require('readline');

async function processLineByLine() {
    const fileStream = fs.createReadStream('input.txt');

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let entriesRead = 0;
    let counter = 0;
    let windows = [];
    let previousSum = Number.MAX_VALUE;
    for await (const line of rl) {
        const lineNumber = parseInt(line);
        
        // Start new window
        windows.push([lineNumber]);

        // Push second number to previous window
        if (windows.length > 1) {
            windows[windows.length - 2].push(lineNumber)
        }

        // push last number to window and process the complete window
        if (windows.length > 2) {
            windows[windows.length - 3].push(lineNumber)

            const completedWindow = windows[windows.length - 3];

            // Remove unneeded data from memory
            windows = windows.slice(1, windows.length);

            const windowSum = completedWindow.reduce((a, b) => a + b, 0);
            console.log(`${completedWindow} = ${windowSum}`);

            const isGreater = windowSum > previousSum;
            console.log(`${windowSum} is ${isGreater ? 'greater' : 'less'} than ${previousSum}`)
            previousSum = windowSum;
            counter += isGreater ? 1 : 0;
            console.log(`Counter goes to: ${counter}`)
        }
    }

    console.log(`${counter} instances were counted`)
}

processLineByLine();