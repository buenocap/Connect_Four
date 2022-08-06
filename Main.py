import numpy as np
# Game Board Class Initialization
class Tic_Tac_Toe:
    def __init__(self,game_over = False, turn = 0):
        self.game_status = game_over
        self.game_turn = turn

    # Game Methods:
    def create_board():
        game_board = np.zeros((6,7))
        return game_board
    def place_chip(self,pos_y,player):
        full_column = "Column is full please make another selection!\n"
        for x in reversed(range(0,6)):
            if self.board[x][pos_y] == 0:
                self.board[x][pos_y] = player
                return
            else:
                pass
        return full_column
    def checkboard(self):
        pass

    # Game Variables
    board = create_board()

# Create Board
game = Tic_Tac_Toe()
while game.game_status != True:
    selection = int(input("Enter a row:\n"))
    game.place_chip(selection,1)
    print(game.board)