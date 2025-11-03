N = 8

def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def print_solution(board):
    for row in board:
        print(row)

def solve_knight():
    board = [[-1 for _ in range(N)] for _ in range(N)]
    moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
    moves_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    if not solve_util(0, 0, 1, board, moves_x, moves_y):
        print("No solution exists")
    else:
        print("Knight's Tour Path:")
        print_solution(board)

def solve_util(x, y, movei, board, moves_x, moves_y):
    if movei == N * N:
        return True
    for k in range(8):
        next_x, next_y = x + moves_x[k], y + moves_y[k]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = movei
            if solve_util(next_x, next_y, movei + 1, board, moves_x, moves_y):
                return True
            board[next_x][next_y] = -1
    return False

solve_knight()
