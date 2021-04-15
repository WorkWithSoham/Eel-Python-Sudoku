import random

def generateSudoku(no_clues):
    SudokuPuzzle = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for j in range(9):
            SudokuPuzzle[i][j] = 0

    # The range here is the amount of numbers in the grid
    for i in range(no_clues):
        # choose random numbers
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        # if taken or not valid reroll
        while(not checkValid(SudokuPuzzle, row, col, num) or SudokuPuzzle[row][col] != 0):
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        SudokuPuzzle[row][col] = num

    return SudokuPuzzle

def printPuzzle(SudokuPuzzle):
    # Electron.js can be fed this array to produce a SudokuPuzzle GUI
    for grid in SudokuPuzzle:
        print(grid)

    # Printable grid in the python terminal
    # TableTB = "|--------------------------------|"
    # TableMD = "|----------+----------+----------|"
    # print(TableTB)
    # for x in range(9):
    #     for y in range(9):
    #         if ((x == 3 or x == 6) and y == 0):
    #             print(TableMD)
    #         if (y == 0 or y == 3 or y== 6):
    #             print("|", end=" ")
    #         print(" " + str(SudokuPuzzle[x][y] if SudokuPuzzle[x][y] else "_"), end=" ")
    #         if (y == 8):
    #             print("|")
    # print(TableTB)

def checkValid(SudokuPuzzle, row, col, num):
    # check if in row
    valid = True
    # check row and collumn
    for x in range(9):
        if (SudokuPuzzle[x][col] == num):
            valid = False
    for y in range(9):
        if (SudokuPuzzle[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            # check if section is valid
            if(SudokuPuzzle[rowsection*3 + x][colsection*3 + y] == num):
                valid = False
    return valid

if __name__ == '__main__':
    SudokuPuzzle = generateSudoku(3)
    print(SudokuPuzzle)