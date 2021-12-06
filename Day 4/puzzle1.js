const fs = require('fs');

const boardSize = 5;

function createBoard(boardArray) {
    const board = [...Array(boardSize)].map(e => Array(boardSize));

    for(let i = 0; i < boardArray; i++) {
        const y = i % 5;
        const x = i - (y * 5);

        board[x][y] = boardArray[i];
    }

    return board;
}

/**
 * 
 * @param {String} input 
 */
function createGameObject(input) {
    const gameArray = input.split('\n\n');
    const gameObject = {
        numbers: [],
        boards: []
    }

    for (let i = 0; i < gameArray.length; i++) {
        if (i == 0) {
            gameObject.numbers = gameArray[i].split(',');
        }
        else {
            const boardArray = gameArray[i].replace('\n', ' ')
            console.log(boardArray.split(' '))
            // console.log(boardArray)
            gameObject.boards.push(createBoard(gameArray[i]));
        }
    }

    return gameObject;
}

fs.readFile('input.txt', 'utf-8', (err, data) => {
    if (err) {
        console.log(err);
        return;
    }
    const gameObject = createGameObject(data);
    // console.log(JSON.stringify(gameObject));
});
