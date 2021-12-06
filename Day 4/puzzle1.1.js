const fs = require('fs');
const readline = require('readline');

const boardSize = 5;

function checkForWinningBoards(boards) {
    for (const boardIndex in boards) {
        const board = boards[boardIndex];
        if (board.length !== boardSize * boardSize) {
            console.error("something is fucky")
        }
        
        const checkCount = board.reduce((pv, cv) => cv === 'X' ? pv + 1 : pv, 0)

        if (checkCount <= 5) {
            continue;
        }

        for (let row = 0; row < boardSize; row++) {
            const rowSlice = board.slice(row * boardSize, row * boardSize + boardSize);
            if (rowSlice.reduce((pv, cv) => pv && (cv === 'X'), true)) {
                console.log('row found')
                console.log(rowSlice);
                return {board, index: boardIndex};
            }
        }

        for (let col = 0; col < boardSize; col++) {
            let i = 0;
            const colSlice = board.filter((value, index) => {
                if (index === (i * boardSize + col)) {
                    i++;
                    return true;
                }
                return false
            });
            
            if (colSlice.reduce((pv, cv) => pv && (cv === 'X'), true)) {
                console.log('col found')
                console.log(colSlice)
                return {board, index: boardIndex};
            }
        }
        break;
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
        boards: [],
        playedBoards: []
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
            boardBuffer = [...boardBuffer, ...boardLineArray];
        }
    }

    gameObject.playedBoards = [...gameObject.boards]
    for (let i = 0; i < gameObject.numbers.length; i++) {
        gameObject.playedBoards = gameObject.playedBoards.map(board => {
            return board.map(number => {
                if (number === gameObject.numbers[i]) {
                    return 'X'
                }
                return number;
            });
        });

        const winningBoard = checkForWinningBoards(gameObject.playedBoards);
        if (winningBoard) {
            console.log(winningBoard);
            console.log(gameObject.boards[winningBoard.index])
            break;
        }
    }
}

processLineByLine();