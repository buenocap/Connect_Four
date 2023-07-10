"""

Connect Four

Pedro Bueno Castaneda

This file provides all functionality needed to properly run the game in the user's terminal.

"""

import numpy as np
import random


#Initialize a profile for the player

class player:

    def __init__(self,token,turn=0,score=0):
        self.token = token;
        self.turn = turn;
        self.score = score;
        self.name = "Player " + str(token);
    
    def get_token(self):
        return self.token;

    def set_token(self, x):
        self.token = x;
        
    def get_turn(self):
        return self.turn;

    def set_turn(self, x):
        self.turn = x;
        
    def get_score(self):
        return self.score;

    def set_score(self, x):
        self.score = x;

#Initialize a profile for the computer
class computer:

    def __init__(self,token,turn=0,score=0):
        self.token = token;
        self.turn = turn;
        self.score = score;
        self.name = "Computer " + str(token);

    def get_token(self):
        return self.token;

    def set_token(self, x):
        self.token = x;
        
    def get_turn(self):
        return self.turn;

    def set_turn(self, x):
        self.turn = x;
        
    def get_score(self):
        return self.score;

    def set_score(self, x):
        self.score = x;
        
    # Creating AI to play the game
    def random_placement(self,game):
        game_board_length = len(game.game_board);
        placement = random.randrange(0,6);
        for row in reversed(range(-1,game_board_length)):
                if row == -1:
                    game.display_board();
                    print("Row selected is full making another selection!");
                    self.random_placement(game);
                if(game.game_board[row][placement] == 0):
                    game.game_board[row][placement] = self.token;
                    print("\n{name} selected column {col}".format(name = self.name, col=placement+1));
                    game.display_board();
                    game_status = game.check_win(row,placement,self.token);
                    return 0
    
    def minimax(self):
        return 0;

#Initalize a profile for the game
class Tic_Tac_Toe:

    def __init__(self,game_over = True, game_board =[]):
        self.game_status = game_over;
        self.game_board = game_board;
        self.game_capacity = True;
        
    def get_game_status(self):
        return self.game_status;

    def create_board(self):
        game_board = np.zeros((6,7));
        self.game_board = game_board;
        return game_board;

    def display_board(self):
        print("\n 1  2  3  4  5  6  7");
        print(" ---------------------");
        for x in self.game_board:
            print(x)
        return 0;
    
    def is_full(self):
        if 0 not in self.game_board:
            self.game_capacity = False;
        return True;

# Allow the player to place a token on the game board
    def place_token(self,token):
        game_board_length = len(self.game_board);
        placement = int(input("Player {token} please enter number 1-7: ".format(token=token)))-1;

        if(placement > -1 and placement < 7):
            for row in reversed(range(-1,game_board_length)):
                if row == -1:
                    self.display_board();
                    print("Row selected is full make another selection!");
                    self.place_token(token);
                if(self.game_board[row][placement] == 0):
                    self.game_board[row][placement] = token;
                    self.display_board();
                    game_status = self.check_win(row,placement,token);
                    return 0
        
    def check_win(self, row, column, player):
        tracker = 0;
        original_column_value = column;
        original_row_value = row;

        #Checking left win condition
        while(column > -1):
            
            if(self.game_board[row][column] == player):
                tracker +=1;
            else:                                                               # We want the program to check for a continuious connected player tokens, if we don't break it will continue looping and counting off all instances of player                                               # Reset tracker value to zero to avoid miscount
                break;
                
            if(tracker == 4):
                print("Player {player} has won the match!\n".format(player = player));
                self.game_status = False;
                return 0;    
            column -=1;
        
        tracker = 0;
        column = original_column_value;                                         # Reset column to it's original value to avoid error
        
        #Check right win condition
        while(column < 7):
            
            if(self.game_board[row][column] == player):
                tracker +=1;
            else:
                break;
            
            if(tracker == 4):
                print("Player {player} has won the match!\n".format(player=player));
                self.game_status = False;
                return 0;
            column +=1;
         
        tracker = 0;   
        column = original_column_value;        
        
        #Check down win conition
        while(row < 6):
            
            if(self.game_board[row][column] == player):
                tracker +=1;
            else:
                break;
            
            if(tracker == 4):
                print("Player {player} has won the match!\n".format(player=player));
                self.game_status = False;
                return 0;
            row +=1;
        
        tracker = 0;
        row = original_row_value;
        
        #Check left diagonal
        while(row < 6 and column > -1):
            
            if(self.game_board[row][column] == player):
                tracker +=1;
            else:
                break;
            
            if(tracker == 4):
                print("Player {player} has won the match!\n".format(player=player));
                self.game_status = False;
                return 0;
            
            row +=1;
            column -=1;
        
        tracker = 0;  
        row = original_row_value;
        column = original_column_value;

        #Check right diagonal
        while(row > -1 and column > 7):
            
            if(self.game_board[row][column] == player):
                tracker +=1;
            else:
                break;
            
            if(tracker == 4):
                print("Player {player} has won the match!\n".format(player=player));
                self.game_status = False;
                return 0;
            
            print("checking [{row}][{column}]".format(row=row,column=column));
            row -=1;
            column +=1;

        return 0;