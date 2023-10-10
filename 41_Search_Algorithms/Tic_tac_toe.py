"""
References: https://github.com/GeorgeSeif/Tic-Tac-Toe-AI
"""

import math

EMPTY = " "
COMPUTER_X = "X"
PLAYER_O = "O"
INFINITY = math.inf


# Function to check if a player has won
def check_winner(board, player):

    # Check valid combination in diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    # Check valid combination in rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check valid combination in columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    return False


# Function to check if the game is over
def is_game_over(board):
    if check_winner(board, COMPUTER_X) or check_winner(board, PLAYER_O):
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


# Function to get the available moves
def get_available_moves(board):
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                moves.append((row, col))
    return moves


# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, COMPUTER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    elif is_game_over(board):
        return 0

    if maximizing_player:
        max_eval = -INFINITY
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = COMPUTER_X
            eval_ = minimax(board, depth + 1, alpha, beta, False)
            board[row][col] = EMPTY
            max_eval = max(max_eval, eval_)
            alpha = max(alpha, eval_)
            if beta <= alpha:
                break

        return max_eval
    else:
        min_eval = INFINITY
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = PLAYER_O
            eval_ = minimax(board, depth + 1, alpha, beta, True)
            board[row][col] = EMPTY
            min_eval = min(min_eval, eval_)
            beta = min(beta, eval_)
            if beta <= alpha:
                break
        return min_eval


# Function for computer to make a move using the minimax algorithm
def make_move(board):
    best_eval = -INFINITY
    best_move = None
    for move in get_available_moves(board):
        row, col = move
        board[row][col] = COMPUTER_X
        eval_ = minimax(board, 0, -INFINITY, INFINITY, False)
        board[row][col] = EMPTY
        if eval_ > best_eval:
            best_eval = eval_
            best_move = move
    row, col = best_move
    board[row][col] = COMPUTER_X


# print the tic-tac-toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("----------")


# Function to play the game
def start_game():
    print("Welcome to Tic-Tac-Toe using Minimax with Alpha Beta Pruning!")

    board = [[EMPTY] * 3 for _ in range(3)]
    current_player = COMPUTER_X

    while not is_game_over(board):
        if current_player == COMPUTER_X:
            make_move(board)
            current_player = PLAYER_O
        else:
            print_board(board)
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1
            if board[row][col] != EMPTY:
                print("Invalid spot. Please try again.")
                continue
            board[row][col] = PLAYER_O
            current_player = COMPUTER_X

    print_board(board)
    if check_winner(board, COMPUTER_X):
        print("X wins!")
    elif check_winner(board, PLAYER_O):
        print("O wins!")
    else:
        print("Draw!")


start_game()
