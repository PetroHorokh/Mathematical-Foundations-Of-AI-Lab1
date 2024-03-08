def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):

            board[i][col] = 'Q'

            if solve_n_queens(board, col + 1, n):
                return True

            board[i][col] = '0'

    return False


def backtracking(n):
    board = [[0 for j in range(n)] for i in range(n)]

    solve_n_queens(board, 0, n)

    print("\nBacktracking algorithm solution: ")
    for row in board:
        print(row)
