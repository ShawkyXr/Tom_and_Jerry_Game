import random
import Game
import os
from Maps import view_maps

from Game import Game

if __name__ == "__main__":
    
    leave = False

    while leave == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        # view maps
        view = input("Do you want to view the maps? (Y/N) : ")
        map
        if view == 'Y' or view == 'y':
            view_maps()
            map = input("Select the map of the game (1 or 2) : ")
        else:
            map = random.randint(1,2)
        level = input("Select the level of the game (Easy '0' , Medium '1' , Hard '2') : ")
        # chek  if the input is valid
        if(int(level) < 0 or int(level) > 2):
            while(int(level) < 0 or int(level) > 2):
                print("Please enter a valid number")
                level = input("Select the level of the game (Easy '0' , Medium '1' , Hard '2') : ")
                os.system('cls' if os.name == 'nt' else 'clear')   
        if int(map) == 2:
            Easy = Game(20,25,(18,2),(18,13),(3,5), [(0,1),(0,2),(1,11),(1,16),(2,11),(2,16),(3,11),(3,14),(3,15),(3,16),(3,17),(3,18),(3,19),(4,5),(4,11),(4,14),(5,5),(5,11),(5,14),(6,5),(6,11),(6,14),(6,16),(6,17),(6,18),(6,19),(6,20),(6,21),(6,22),(6,23),(6,24),(7,5),(7,11),(8,5),(8,11),(9,5),(9,11),(10,2),(10,3),(10,4),(10,5),(10,11),(11,11),(11,12),(11,13),(11,14),(12,15),(13,15),(14,1),(14,2),(14,3),(14,4),(14,5),(14,6),(14,7),(14,8),(14,22),(15,8),(15,9),(15,14),(15,15),(15,16),(15,22),(16,8),(16,14),(16,22),(17,0),(17,1),(17,2),(17,3),(17,4),(17,5),(17,6),(17,8),(17,10),(17,11),(17,22),(18,8),(18,10),(18,12),(18,22),(19,12),(19,22)] ,int(level))
        else:
            Easy = Game(5,5,(2,0),(1,3),(4,4),[(2,2),(2,4)], int(level))
        Easy.start()
        again = input("Do you want to play again? (Y/N) : ")
        if again == 'N' or again == 'n':
            leave = True
        elif again == 'Y' or again == 'y':
            leave = False
        else:
            print("Please enter a valid input")
