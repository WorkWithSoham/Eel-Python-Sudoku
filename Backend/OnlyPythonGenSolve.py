import Sudoku_generator
import Sudoku_solver

def printPuzzle(string, SudokuPuzzle):
    print(string)
    for grid in SudokuPuzzle:
        print(grid)
    print("\n\n")

if __name__ == '__main__':
    loop = True
    while loop:
        Difficulty = int(input("Enter difficulty level from 1 to 5, with 5 being most difficult: "))
        if 0 < Difficulty < 6:
            loop = False

    diff = {
        1: 35,
        2: 30,
        3: 25,
        4: 20,
        5: 17,
    }

    SudokuPuzzle = Sudoku_generator.generateSudoku(diff[Difficulty])
    printPuzzle('The Puzzle', SudokuPuzzle)

    # Sudoku_solver.solveSudoku(SudokuPuzzle)
    # printPuzzle('The Solution', SudokuPuzzle)

    SudokuPuzzle = Sudoku_solver.ReturnableSudoku(SudokuPuzzle)
    printPuzzle('The Solution', SudokuPuzzle)

