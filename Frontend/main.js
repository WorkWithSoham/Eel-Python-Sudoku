var unsolved_Sudoku;
var solved_Sudoku;

// Request Python to generate Sudoku Puzzle for the user
function puzzle_generator() {
    const difficulty = document.getElementById('difficulty').value
    eel.generate(difficulty)(function (res) {
        unsolved_Sudoku = res;
        eel.solve(res)(function (sres) {
            // console.log(sres)
            if(sres === false){
                puzzle_generator();
            } else{
                solved_Sudoku = sres;
                fill_values(unsolved_Sudoku);
            }
        })
    })
}

// Auto Solve the puzzle for the user
function solve_puzzle() {
    fill_values(solved_Sudoku);
}

// Assigning the required values to the required cell
function fill_values(puzzle) {
    for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {
            id = 'cell-' + String((i * 9 + j));
            if (puzzle[i][j] == 0){
                document.getElementById(id).value = "";
                document.getElementById(id).disabled = false;
                document.getElementById(id).style.backgroundColor = '#FFFFFF'
            } else {
                document.getElementById(id).value = puzzle[i][j];
                document.getElementById(id).disabled = true;
                document.getElementById(id).style.backgroundColor = '#aca9a9'
            }
            
        }
    }
}

function check_puzzle(){
    var count = 0;
    for (var i = 0; i < 9; i++){
        for (var j = 0; j < 9; j++){
            id = 'cell-' + String((i * 9 + j));
            var value = document.getElementById(id).value
            console.log(value)
            if (value == solved_Sudoku[i][j]){
                document.getElementById(id).style.backgroundColor = '#54f176'
            } else {
                if (value){
                    document.getElementById(id).style.backgroundColor = '#f05151'
                } else{
                    document.getElementById(id).style.backgroundColor = '#FFFFFF'
                }
                count += 1
            }
        }
    }
    if (!count){
        alert('Congratulations! You have solved the Sudoku!')
    }
}

function reset_puzzle(){
    fill_values(unsolved_Sudoku);
}