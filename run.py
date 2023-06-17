import random 

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

#take player input
def player_input(board):
    your_input = int(input("choose a number between 1 and 9: \n"))
    if board[your_input-1] == "-":
        board[your_input-1] = current_player
    else:
        print("the spot was already played!!")

#We check if we have three similar symbols in a row, horizontally, vertically, or diagonally.
#we check horizontally: 3 possibilities
def check_horizontally(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

#we check vertically: 3 possibilities
def check_vertically(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True
        
#we check diagonally: 2 possibilities
def check_diagonally(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

#we check if we have a winner
def check_the_winner(board):
    global game_is_running
    if check_horizontally(board) or check_vertically(board) or check_diagonally(board):
        print_board(board)
        print(f"The winner is {winner}!")
        game_is_running = False

#switch bettween players function
def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


#we check if the game ends in a draw
def check_if_draw(board):
    global game_is_running
    if "-" not in board:
        print_board(board)
        print("The game ends in a draw!")
        game_is_running = False


while game_is_running:
    print_board(board)
    player_input(board)
    check_the_winner(board)
    check_if_draw(board)
    change_player()