const fs = require('fs');
const readline = require('readline');

const boardSize = 5;

function checkForWinningBoard(rows) {
    for (const row of rows) {
        if (row.reduce((pv, cv) => pv && (cv === 'X'), true)) {
            console.log('win found')
            console.log(row);
            return true;
        }
    }
}

function checkForWinningBoards(boards) {
    for (const board of boards) {
        const checkCount = board.reduce((pv, cv) => pv + cv.reduce((pv2, cv2) => cv2 === 'X' ? pv2 + 1 : pv2, 0), 0);
        // Sanity check, this board can't have bingo
        if (checkCount < 5) {
            continue;
        }

        // Rotate board, so check is easier
        const rotatedBoard = board[0].map((val, index) => board.map(row => row[index]).reverse());

        // Find winning row/col
        if (checkForWinningBoard(board) || checkForWinningBoard(rotatedBoard)) {
            return board;
        }
    }
}

async function processLineByLine() {
    const fileStream = fs.createReadStream('input.txt');

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    const gameObject = {
        numbers: [],
        boards: []
    };
    let boardBuffer = [];

    for await (const line of rl) {
        if (gameObject.numbers.length === 0) {
            gameObject.numbers = line.split(',').map(e => parseInt(e));
        } else if (line === '' && boardBuffer.length > 0) {
            gameObject.boards.push(boardBuffer);
            boardBuffer = [];
        } else if (line !== '') {
            const boardLineArray = line.trim().replaceAll('  ', ' ').split(' ').map(e => parseInt(e));
            boardBuffer.push(boardLineArray)
        }
    }

    if (boardBuffer.length > 0) {
        gameObject.boards.push(boardBuffer);
    }

    // Play for each number
    for (const number of gameObject.numbers) {
        const playedBoards = gameObject.boards.map(board => {
            return board.map(row => {
                return row.map(boardNumber => number === boardNumber ? 'X' : boardNumber);
            });
        });
        gameObject.boards = playedBoards;
        
        const winningBoard = checkForWinningBoards(playedBoards);
        if (winningBoard) {
            console.log(`We've found a winner with number: ${number}`)
            console.log(winningBoard);
            const boardSum = winningBoard.reduce((pr, cr) => pr + cr.reduce((pv, cv) => cv !== 'X' ? pv + cv : pv, 0)  ,0);

            console.log(`The solution is: ${boardSum} * ${number} = ${boardSum * number}`)
            break;
        }
    }
}

processLineByLine();