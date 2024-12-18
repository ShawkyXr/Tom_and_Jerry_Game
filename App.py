import Game

from Game import Game


if __name__ == "__main__":
    
    leave = False

    while leave == False:
        level = input("Select the level of the game (Easy '0' , Medium '1' , Hard '2') : ")
        try:
            ver = int(level)
            if ver >= 0 and ver <= 2:
                if ver == 0:
                    Easy = Game(5,5,(2,0),(1,3),(4,4),[(2,2),(2,4)],ver)
                    Easy.start()
                elif ver == 1:
                    Medium = Game(5,5,(2,0),(1,3),(4,4),[(2,2),(2,4)],ver)
                    Medium.start()
                else:
                    Hard = Game(5,5,(2,0),(1,3),(4,4),[(2,2),(2,4)],ver)
                    Hard.start()
                again = input("Do you want to play again? (Y/N) : ")
                if again == 'N' or again == 'n':
                    leave = True
            else:
                print("Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")
            level = input("Select the level of the game (Easy '0' , Medium '1' , Hard '2') : ")

    