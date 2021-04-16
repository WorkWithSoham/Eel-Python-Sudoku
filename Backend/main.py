import eel # pip install eel
import Sudoku_generator
import Sudoku_solver

eel.init('Frontend')

@eel.expose
def generate(diff):
    '''
        Takes in the number of clues in the Sudoku and returns the Sudoku Puzzle
    '''
    
    SudokuPuzzle = Sudoku_generator.generateSudoku(int(diff))
    return SudokuPuzzle

@eel.expose
def solve(SudokuPuzzle):
    '''
        Takes the unsolved Sudoku and returns the solved one
    '''
    if not Sudoku_solver.solveSudoku(SudokuPuzzle):
        return False

    return SudokuPuzzle

# Change 'brave' to the browser installed in your machine.
# E.g
# 'chrome' => Google Chrome => Default
# 'edge' => Microsoft Edge

# Define all the require functions above the start method
eel.start('index.html')
