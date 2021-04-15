var unsolved_Sudoku;
var solved_Sudoku;

// Request Python to generate Sudoku Puzzle for the user
function puzzle_generator() {
    const difficulty = document.getElementById('difficulty').value
    eel.generate(difficulty)(function (res) {
        unsolved_Sudoku = res;
        fill_values(unsolved_Sudoku);
    })
}

// Auto Solve the puzzle for the user
function solve_puzzle() {
    eel.solve(unsolved_Sudoku)(function (res) {
        console.log(res);
        if(!res){
            alert("Oops, the given puzzle was unsolvable!")
        } else{
            solved_Sudoku = res;
            fill_values(solved_Sudoku);
        }
    })
}

// Assigning the required values to the required cell
function fill_values(puzzle) {
    for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {
            id = 'cell-' + String((i * 9 + j));
            document.getElementById(id).value = puzzle[i][j];
        }
    }
}