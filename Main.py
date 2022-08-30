import os
import Player
import COM
from Game_Functions import Tic_Tac_Toe

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

#Game loop
answer = "y"
while answer == "y":
    #Start Game - Initial Board
    print("\n",game.board)
    while game.game_status != True:
        pos_x,pos_y,player_token = game.player_turn(player.token)
        game.checkboard(pos_x,pos_y,player_token)
        if game.game_status == True:
            break
        pos_x,pos_y,comp_token = game.player_turn(computer.token)
        game.checkboard(pos_x,pos_y,comp_token)
    answer = input("\nWould you like to play again?\n")
    if answer == "y":
        # Reset board and status of game
        game.board.fill(0)
        game.game_status = False
        os.system('clear')
        print("\n")
        continue
    else:
        os.system('clear')
        print("\nThank you for playing!\n")
        exit()