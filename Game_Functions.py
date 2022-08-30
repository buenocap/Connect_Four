import numpy as np
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
            if pos_y >= 0 and self.board[pos_x][pos_y] == player:
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
        for y in range(0,7):
            if pos_y <= 6 and self.board[pos_x][pos_y] == player:
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
        for x in range(0,6):
            if pos_x >= 0 and self.board[pos_x][pos_y] == player:
                pos_x -= 1
                counter +=1
            elif counter == 4:
                print(win_msg)
                self.game_status = True
                return
            else:
                counter = 0
                pos_x += x
                break
        # Check down
        for x in range(0,6):
            if pos_x < 6 and self.board[pos_x][pos_y] == player:
                pos_x += 1
                counter += 1
            elif counter == 4:
                print(win_msg)
                self.game_status = True
                return
            else:
                counter = 0
                pos_x -= x
                break
        # Check upper diagonal (right)
        temp1 = pos_x
        temp2 = pos_y
        while True:
            if pos_x >= 0 and pos_y < 7 and self.board[pos_x][pos_y] == player:
                counter += 1
                pos_x -= 1
                pos_y += 1
            elif counter == 4:
                print(win_msg)
                self.game_status = True
                return
            else:
                counter = 0
                pos_x = temp1
                pos_y = temp2
                break
        #Check lower diagonal (right)
        while True:
            if pos_x < 6 and pos_y >=0 and self.board[pos_x][pos_y] == player:
                counter += 1
                pos_x += 1
                pos_y -= 1
            elif counter == 4:
                print(win_msg)
                self.game_status = True
                return
            else:
                counter = 0
                pos_x = temp1
                pos_y = temp2
                break

        # Check upper diagonal (left)
        while True:
            if pos_x >= 0 and pos_y >= 0 and self.board[pos_x][pos_y] ==  player:
                counter += 1
                pos_x -= 1
                pos_y -= 1
            elif counter == 4:
                print(win_msg)
                self.game_status = True
                return
            else:
                counter = 0
                pos_x = temp1
                pos_y = temp2
                break
        # Check lower diagonal (left)
        while True:
            if pos_x < 6 and pos_y < 7 and self.board[pos_x][pos_y]:
                counter += 1
                pos_x += 1
                pos_y += 1
            elif counter == 4:
                print(win_msg)
                self.game_status = False
                return
            else:
                counter = 0
                pos_x = temp1
                pos_y = temp2
                break
        
        #Check for any empty spots if full game has ended in a tie
        if 0 not in self.board:
            print("Game has ended in a tie!\nNo more moves can be made.\n")
            self.game_status = True

        return
    
    def player_turn(self,player):
        try:
            while True:
                selection = int(input("\nPlayer {zero} select a column (1-7):\n".format(zero = player)))
                if selection < 1 or selection > 7:
                    print("\nSelection is out of bound please try again.\n")
                    print(self.board)
                else:
                    break
        except ValueError:
            print("Invalid try again.")
            while True:
                selection = int(input("\nPlayer {zero} select a column (1-7):\n".format(zero = player)))
                break
        x,y,user_token = self.place_chip(selection-1,player)
        print(self.board)
        return x,y,user_token

    def computer_turn(self):
        #Implementation space for A.I
        pass

    # Game Variables
    board = create_board()