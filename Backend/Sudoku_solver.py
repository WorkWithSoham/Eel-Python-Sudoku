def findNextEmpty(SudokuPuzzle):

    for row in range(9):
        for col in range(9):
            if SudokuPuzzle[row][col] == 0:
                return row, col

    return None, None

def checkValid(SudokuPuzzle, row, col, guess):

    # check the validity of the guess for the row
    if guess in SudokuPuzzle[row]:
        return False

    if guess in [SudokuPuzzle[i][col] for i in range(9)]:
        return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if SudokuPuzzle[r][c] == guess:
                return False

    return True

def solveSudoku(SudokuPuzzle):
    # Backtracking Technique

    row, col = findNextEmpty(SudokuPuzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        if checkValid(SudokuPuzzle, row, col, guess):
            SudokuPuzzle[row][col] = guess

            if solveSudoku(SudokuPuzzle):
                return True

        SudokuPuzzle[row][col] = 0

    return False

def ReturnableSudoku(SudokuPuzzle):
    '''
        Returns the newly filled sudoku puzzle
    '''
    solveSudoku(SudokuPuzzle)
    print(solveSudoku(SudokuPuzzle))
    return SudokuPuzzle
