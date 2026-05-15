def isValidSudoku(board):
    """
    The function determines the correctness of the Sudoku.
    :param board: game table
    """
    for row in board:
        seen = set()
        for ch in row:
            if ch != ".":
                if ch in seen:
                    return False
                seen.add(ch)

    for col in range(9):
        seen = set()
        for row in range(9):
            ch = board[row][col]
            if ch != ".":
                if ch in seen:
                    return False
                seen.add(ch)

    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            seen = set()
            for row in range(block_row, block_row + 3):
                for col in range(block_col, block_col + 3):
                    ch = board[row][col]
                    if ch != ".":
                        if ch in seen:
                            return False
                        seen.add(ch)

    return True

board = [
    ["5", "3", ".", "7", ".", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(isValidSudoku(board))

