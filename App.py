import random
import Game
import os
import Maps
from Game import Game

if __name__ == "__main__":
    
    leave = False

    while leave == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Tom and Jerry Game")
        level = input("Select the level of the game (Easy '0' , Medium '1' , Hard '2') : ")
        os.system('cls' if os.name == 'nt' else 'clear') 
        # chek  if the input is valid
        while level != '0' and level != '1' and level != '2':
            level = input("Please enter a valid input : ")
            os.system('cls' if os.name == 'nt' else 'clear')
        # generate the map
        map_height , map_width , map_exit , map_rat , map_cat , map_obstacles = Maps.generate_map(int(level))
        game = Game(map_height , map_width , map_exit , map_rat , map_cat , map_obstacles , int(level))
        game.start()
        again = input("Do you want to play again? (Y/N) : ")
        if again == 'N' or again == 'n':
            leave = True
        elif again == 'Y' or again == 'y':
            leave = False
        else:
            print("Please enter a valid input")
