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
        full_msg = "Column is full plese make another selection!\n"
        for x in reversed(range(0,len(self.board))):
            if self.board[x][pos_y] == 0:
                self.board[x][pos_y] = player
                return x,pos_y,player
            else:
                pass
        print(full_msg)
        return 0,0,0

    def checkboard(self,pos_x,pos_y,player):
        counter = 0
        # Check left
        # Check right
        # Check up
        # Check down
        # Check diagonal right
        # Check diagonal left
        return

    # Game Variables
    board = create_board()

# Create Board
game = Tic_Tac_Toe()

# Create Player and Computer
token = input("Would you like to go first or second?\n").lower()
if token == 'first':
    player = Player.Player(1)
    computer = COM.Computer(2)
else:
    player = Player.Player(2)
    computer = COM.Computer(1)

#Start Game
while game.game_status != True:
    try:
        selection = int(input("Enter a row:\n"))
    except ValueError:
        print("invalid entry")

    x,y,user_token = game.place_chip(selection,1)
    print(game.board)