const fs = require('fs');
const readline = require('readline');

function checkForWinningBoard(rows) {
    for (const row of rows) {
        if (row.reduce((pv, cv) => pv && (cv === 'X'), true)) {
            return true;
        }
    }
}

function checkForWinningBoards(boards) {
    const winningBoards = [];
    for (const boardIndex in boards) {
        const board = boards[boardIndex];
        const checkCount = board.reduce((pv, cv) => pv + cv.reduce((pv2, cv2) => cv2 === 'X' ? pv2 + 1 : pv2, 0), 0);
        // Sanity check, this board can't have bingo
        if (checkCount < 5) {
            continue;
        }

        // Rotate board, so check is easier
        const rotatedBoard = board[0].map((val, index) => board.map(row => row[index]).reverse());

        // Find winning row/col
        if (checkForWinningBoard(board) || checkForWinningBoard(rotatedBoard)) {
            winningBoards.push({board, index: boardIndex});
        }
    }

    if (winningBoards.length > 1) {
        // Sort so removal doesn't fuck stuff up
        return winningBoards.sort((a, b) => b.index - a.index);
    }
    return winningBoards;
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

    let winCounter = 0;
    const gameBoards = gameObject.boards.length;
    // Play for each number
    for (const number of gameObject.numbers) {
        const playedBoards = gameObject.boards.map(board => {
            return board.map(row => {
                return row.map(boardNumber => number === boardNumber ? 'X' : boardNumber);
            });
        });
        gameObject.boards = playedBoards;
        
        const winningBoards = checkForWinningBoards(playedBoards);
        if (winningBoards.length > 0) {
            winCounter += winningBoards.length;

            // Remove all winning boards
            winningBoards.map(winningBoard => gameObject.boards.splice(winningBoard.index, 1));

            if (winCounter === gameBoards) {
                console.log(`We've found the last winner with number: ${number}`)
                console.log(winningBoards[0]);
                const boardSum = winningBoards[0].board.reduce((pr, cr) => pr + cr.reduce((pv, cv) => cv !== 'X' ? pv + cv : pv, 0)  ,0);
    
                console.log(`The solution is: ${boardSum} * ${number} = ${boardSum * number}`)
                break;
            }
        }
    }
}

processLineByLine();