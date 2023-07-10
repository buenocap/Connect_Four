"""
Connect Four
Pedro Bueno Castaneda
This main file will run the connect four game until a player or computer has won the game.
Note: all game functionality can be found in the file named gameFunctions.py
"""

import game_type
import time

def main_menu():
    currentGame = game_type.game_functions.Tic_Tac_Toe();
    # Initialize player(s) and or computer
    print("Please select from the following options:\n(1) Player Vs Player\n(2) Player Vs Computer\n(3) Computer Vs Computer\n(4) Quit Game")
    selection = int(input("Enter Selection: "))
    if(selection == 1):
        game_type.PvP(currentGame);
    elif(selection == 2):
        game_type.PvC(currentGame);
    elif(selection == 3):
        game_type.CvC(currentGame);
    elif(selection == 4):
        quit();
    else:
        print("Invalid selection please try again.\nReturning to main menu...\n")
        time.sleep(2);
        main_menu();
        
main_menu();