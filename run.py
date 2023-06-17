
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "X"
winner = None
game_is_running = True
line = "-----"

#printing the game board

def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(line)
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(line)
    print(board[6] + "|" + board[7] + "|" + board[8])

print_board(board)