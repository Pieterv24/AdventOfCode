const fs = require('fs');
const readline = require('readline');

const inputFile = 'input.txt';

async function processLineByLine() {
    const fileStream = fs.createReadStream(inputFile);

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let totalCount = 0;

    for await (const line of rl) {
        const testCases = line.split('|')[0].trim().split(' ').map(digit => digit.split('').sort());
        const digits = line.split('|')[1].trim().split(' ').map(digit => digit.split('').sort().join(''));

        const results = {
            1: testCases.filter(digit => digit.length === 2)[0],
            4: testCases.filter(digit => digit.length === 4)[0],
            7: testCases.filter(digit => digit.length === 3)[0],
            8: testCases.filter(digit => digit.length === 7)[0]
        }

        let fiveSeg = testCases.filter(digit => digit.length === 5);
        let sixSeg = testCases.filter(digit => digit.length === 6);

        // Segment A is known since it's the one not in 7 that does not occur in 1
        const segmentA = results[7].filter(segment => !results[1].includes(segment))[0];

        // One of the 6 segment displays lacks one of the entries in one, this is 6
        results[6] = sixSeg.filter(digit => digit.reduce((pv, cv) => results[1].includes(cv) ? pv + 1 : pv, 0) === 1)[0];
        // Remove digit from list
        sixSeg.splice(sixSeg.indexOf(results[6]), 1);

        // Four and segment A leave only 1 segment unknown for 9 and 2 for 0
        results[9] = sixSeg.filter(digit => digit.filter(segment => !results[4].includes(segment) && segment !== segmentA).length === 1)[0];
        results[0] = sixSeg.filter(digit => digit.filter(segment => !results[4].includes(segment) && segment !== segmentA).length === 2)[0];

        // Three has both segments from one, while the others only have one
        results[3] = fiveSeg.filter(digit => digit.reduce((pv, cv) => results[1].includes(cv) ? pv + 1 : pv, 0) === 2)[0];
        // Remove digit from list
        fiveSeg.splice(fiveSeg.indexOf(results[3]), 1);

        // Five has one segment different than six, while 2 has 2 different segments
        results[5] = fiveSeg.filter(digit => results[6].filter(segment => !digit.includes(segment)).length === 1)[0];
        results[2] = fiveSeg.filter(digit => results[6].filter(segment => !digit.includes(segment)).length === 2)[0];

        let digitEntry = '';
        for (const digit of digits) {
            for(const knownDigit of Object.keys(results)) {
                if (digit === results[knownDigit].join('')) {
                    digitEntry += knownDigit;
                    continue;
                }
            }
        }

        console.log(digitEntry);

        totalCount += parseInt(digitEntry);
    }

    console.log(`The answer is: ${totalCount}`);
}

processLineByLine();