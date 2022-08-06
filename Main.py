import numpy as np
import Player
import COM
# Game Board Class Initialization
class Tic_Tac_Toe:
    def __init__(self,game_over = False):
        self.game_status = game_over

    # Game Methods:
    def create_board():
        game_board = np.zeros((6,7))
        return game_board
    def place_chip(self,pos_y,player):
        full_column = "Column is full please make another selection!\n"
        for pos_x in reversed(range(0,6)):
            if self.board[pos_x][pos_y] == 0:
                self.board[pos_x][pos_y] = player
                return pos_x,pos_y
            else:
                pass
        return full_column
    def checkboard(self,pos_x,pos_y):
        # Check left
        # Check right
        # Check up
        # Check down
        # Check diagonal right
        # Check diagonal left
        pass

    # Game Variables
    board = create_board()

# Create Board
game = Tic_Tac_Toe()
while game.game_status != True:
    selection = int(input("Enter a row:\n"))
    game.place_chip(selection,1)
    print(game.board)