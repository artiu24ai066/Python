import random
def is_valid(board):
    for i in range(len(board)):        # loop checks all pairs of queens (not attacking each other diagonally)
        for j in range(i + 1, len(board)):
            if abs(board[i] - board[j]) == abs(i - j):   # board[i] represents column position of the queen in row i
                return False      # Two queens are on the same diagonal if abs(col1 - col2) == abs(row1 - row2)
    return True

def print_board(board):
    for i in range(len(board)):
        row = ['.'] * len(board)
        row[board[i]] = 'Q'
        print(' '.join(row))
    print()

def find_random_solution():
    attempts = 0
    while True:
        board = list(range(8))
        random.shuffle(board)       # checking diagonal conflicts because rows/columns are unique
        attempts += 1
        if is_valid(board):
            print(f"Found a solution in {attempts} attempts:")
            print_board(board)
            return board

find_random_solution()
