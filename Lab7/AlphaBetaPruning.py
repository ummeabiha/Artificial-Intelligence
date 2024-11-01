import math
board = [[' ' for _ in range(3)] for _ in range(3)]
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True
def check_winner(board):
    lines = board + [[board[i][j] for i in range(3)] for j in range(3)] + [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
    if ['X'] * 3 in lines:
        return 'X'
    elif ['O'] * 3 in lines:
        return 'O'
    return None
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return 1  
    elif winner == 'O':
        return -1 
    elif is_board_full(board):
        return 0 
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move
def play_game():
    while True:
        print_board(board)
        if check_winner(board) or is_board_full(board):
            break
        row, col = map(int, input("Enter row and column (0-2): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Cell already taken, try again.")
            continue
        if check_winner(board) or is_board_full(board):
            break
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'X'
            print("AI played at:", move)
    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie!")
play_game()
