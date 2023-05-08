def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-") 
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == player and board[i+1] == player and board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True
    # No win
    return False

def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    winner = None

    while not winner:
        print_board(board)
        print("It's " + current_player + "'s turn.")
        move = input("Enter the position (0-8) where you want to place your " + current_player + ": ")
        move = int(move)
        if board[move] == " ":
            board[move] = current_player
            if check_win(board, current_player):
                winner = current_player
            elif " " not in board:
                winner = "tie"
            else:
                current_player = "O" if current_player == "X" else "X"

    print_board(board)
    if winner == "tie":
        print("It's a tie!")
    else:
        print(winner + " wins!")
print(tic_tac_toe())