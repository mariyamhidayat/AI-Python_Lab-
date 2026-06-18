board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):  # range(start, end, step) and i takes values 0, 3, 6
        print(board[i], board[i+1], board[i+2])
    print()

def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    
    for i, j, k in wins:
        if b[i] == b[j] == b[k] and b[i] != " ":
            return b[i]
    return None

def is_full(b):
    # Check if there are no empty spaces left on the board
    return " " not in b

# Minimax function
# This function gives the AI its decision-making ability
def minimax(b, is_max):
    winner = check_winner(b)  # First check if someone has won
    
    if winner == "X":
        return 1  # AI gets +1 score (GOOD)
    elif winner == "O":
        return -1  # AI gets -1 score (BAD)
    elif is_full(b):
        return 0  # Draw

    if is_max:  # AI (X)
        best = -999
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, False)
                b[i] = " "  # Undo move (backtracking)
                best = max(best, score)
        return best
    else:  # Human (O)
        best = 999
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, True)
                b[i] = " "  # Undo move (backtracking)
                best = min(best, score)
        return best

# AI move
def best_move():
    best_score = -999
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            
            # Call Minimax to evaluate how good this move is
            score = minimax(board, False)
            
            # Undo the move so the board returns to its original state
            board[i] = " "
            
            if score > best_score:
                best_score = score
                move = i

    board[move] = "X"

# Simple game loop
while True:
    print_board()

    # Human move
    pos = int(input("Enter position (0-8): "))
    if board[pos] == " ":
        board[pos] = "O"

    if check_winner(board):
        print_board()
        print("Winner:", check_winner(board))
        break

    # AI move
    best_move()

    if check_winner(board):
        print_board()
        print("Winner:", check_winner(board))
        break

    if is_full(board):
        print_board()
        print("Draw!")
        break