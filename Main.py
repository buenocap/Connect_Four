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
    def is_game_over(self):
        if self.game_status == False:
            return False
        else:
            return True

    # Game Variables
    board = create_board()

# Create Board
game = Tic_Tac_Toe()
print(game.board)