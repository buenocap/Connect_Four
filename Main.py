import string
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
            if self.board[x][pos_y] == 0 :
                self.board[x][pos_y] = player
                return x,pos_y,player
            else:
                pass
        print(full_msg)
        return 0,0,0

    def checkboard(self,pos_x,pos_y,player):
        counter = 0
        win_msg = "Player {player} has won the game!\n".format(player = player)
        # Check left
        for y in range(0,7):
            if self.board[pos_x][pos_y] == player and pos_y >= 0:
                pos_y -= 1
                counter += 1
            elif counter == 4:
                print(win_msg)
                self.game_status = True
                return
            else:
                counter = 0
                pos_y += y
                break
        # Check right
        for y in range(0,6):
            if self.board[pos_x][pos_y] == player and pos_y <= 6:
                pos_y += 1
                counter += 1
            elif counter == 4:
                print(win_msg)
                self.game_status = True
                return
            else:
                counter = 0
                pos_y -= y
                break

        # Check up
        # Check down
        # Check diagonal right
        # Check diagonal left
        return
    
    def player_turn(self,player):
        try:
            while True:
                selection = int(input("Select a column (1-7):\n"))
                if selection < 1 or selection > 7:
                    print("Selection is out of bound please try again.")
                else:
                    break
        except ValueError:
            print("Invalid try again.")
            while True:
                selection = int(input("Select a column (1-7):\n"))
                break
        x,y,user_token = self.place_chip(selection-1,player)
        print(self.board)
        return x,y,user_token

    def computer_turn(self):
        pass

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

#Start Game - Initial Board
print(game.board)
#Game loop
while game.game_status != True:
    pos_x,pos_y,player_token = game.player_turn(player.token)
    game.checkboard(pos_x,pos_y,player_token)
