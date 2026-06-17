# Function to check whether placing a queen at (row, col) is safe
def is_safe(board, row, col, n):

    # Check if any queen is already placed in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if any queen is on the same diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    # Position is safe for placing the queen
    return True


# Recursive function that solves the N-Queen problem using backtracking
def solve_n_queen(board, row, n):

    # If all queens are placed successfully, print the solution
    if row == n:
        print_solution(board, n)
        return True

    # Try placing the queen in each column of the current row
    for col in range(n):

        # Check whether the current position is safe
        if is_safe(board, row, col, n):

            # Place the queen
            board[row] = col

            # Recursively place queens in the next row
            if solve_n_queen(board, row + 1, n):
                return True

    # No valid position found in this row
    return False


# Function to display the chessboard with queens
def print_solution(board, n):

    # Traverse each row
    for i in range(n):

        # Traverse each column
        for j in range(n):

            # Print Q where a queen is placed
            if board[i] == j:
                print("Q", end=" ")

            # Print . for empty spaces
            else:
                print(".", end=" ")

        print()


# Size of the chessboard (8x8)
n = 8

# Initialize the board with -1 (no queen placed)
board = [-1] * n

# Start solving from the first row
solve_n_queen(board, 0, n)