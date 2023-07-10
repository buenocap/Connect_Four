import game_functions
import time

def PvP(game):

    player_one = game_functions.player(1);
    player_two = game_functions.player(2);
    game.create_board();
    game.display_board();
    while(game.game_status):
        game.is_full();
        game.place_token(player_one.get_token());
        if(game.game_status == False or game.game_capacity == False):
            break;
        game.is_full();
        game.place_token(player_two.get_token());
    return 0;


def PvC(game):
    print("Player Vs Computer");
    player_one = game_functions.player(1);
    player_two = game_functions.computer(2);
    game.create_board();
    game.display_board();
    while(game.game_status):
        game.place_token(player_one.get_token());
        if(game.game_status == False):
            break;
        player_two.random_placement(game);
    return 0;

def CvC(game):
    print("\nComputer Vs Computer");
    computer_one = game_functions.computer(1);
    computer_two = game_functions.computer(2);
    game.create_board();
    game.display_board();
    while(game.game_status):
        computer_one.random_placement(game);
        if(game.game_status == False):
            break;
        time.sleep(2);
        computer_two.random_placement(game);
        time.sleep(2);
    return 0;