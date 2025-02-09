import  os
from colorama import Fore, Style

class Game:

    def __init__(self,h,w,cat,rat,exit,obs,level): # instialize the game
        self.level = level
        self.grid_high = h
        self.grid_width = w
        self.grid = [['-' for i in range(self.grid_width)] for j in range(self.grid_high)]
        self.cat_pos = cat
        self.rat_pos = rat
        self.exit = exit
        self.obstacles = obs

    def start(self): # start the game
        print ("Welcome to Tom and Jerry Game")

        if (self.level==0):
            print("Easy Mode")
        elif (self.level==1):
            print("Medium Mode")
        else:
            print("Hard Mode")

        self.build()
        self.display(False)
        self.play()


    # build the game grid
    def build(self):

        self.grid[self.cat_pos[0]][self.cat_pos[1]] = 'T'
        self.grid[self.rat_pos[0]][self.rat_pos[1]] = 'J'
        self.grid[self.exit[0]][self.exit[1]] = 'E'

        for obstacle in self.obstacles:
            self.grid[obstacle[0]][obstacle[1]] = '#' 


    # play the game
    def play(self):

        while True:

            self.move_rat() # take moves from player

            self.move_cat() 

            if (self.rat_pos == self.cat_pos): # if cat eat the rat
                self.grid[self.rat_pos[0]][self.rat_pos[1]] = 'X'
                self.display(True)
                print("Game Over :(")
                break
            
            if (self.rat_pos == self.exit):
                self.grid[self.rat_pos[0]][self.rat_pos[1]] = '-'
                self.grid[self.exit[0]][self.exit[1]] = 'W'
                self.display(True)
                print("WOW! You Won")
                break
                
            self.display(True)


    # to be dynamic in terminal
    def clear_terminal(self,k):
        if os.name == 'nt':
            os.system('cls')  # For Windows
        else:
            for _ in range(k):
                print("\033[F\033[K", end='')  



    def display(self,clear): # display the game grid
        if (clear):
            self.clear_terminal(self.grid_high+1)
        for i in range(self.grid_high):
            for j in range(self.grid_width):
                cell = self.grid[i][j]
                if (cell == 'J' or cell == 'W'):
                    print (Style.BRIGHT + Fore.LIGHTGREEN_EX + cell + Style.RESET_ALL, end=' ')
                elif (cell == 'T' or cell == 'X'):
                    print (Style.BRIGHT + Fore.LIGHTRED_EX + cell + Style.RESET_ALL, end=' ')
                elif (cell == 'E'):
                    print (Style.BRIGHT + Fore.LIGHTBLUE_EX + cell + Style.RESET_ALL, end=' ')
                elif (cell == '#'):
                    print (Style.BRIGHT + Fore.YELLOW + cell + Style.RESET_ALL, end=' ')
                else:
                    print (cell, end=' ')
            print()



    def is_valid(self,pos): # position is valid or not
        return pos[0] >= 0 and pos[0] < self.grid_high and pos[1] >= 0 and pos[1] < self.grid_width and self.grid[pos[0]][pos[1]] != '#'
    


    def move_rat(self): # move the rat
        print("Enter the direction to move the rat(up 'U' ,down 'D' ,left 'L',right 'R') : ", end='')
        inp = input()
        new_pos = self.rat_pos
        if (inp == 'up' or inp == 'U' or inp == 'u'):
            new_pos = (self.rat_pos[0]-1,self.rat_pos[1])
        elif (inp == 'down' or inp == 'D' or inp == 'd'):
            new_pos = (self.rat_pos[0]+1,self.rat_pos[1])
        elif (inp == 'left' or inp == 'L' or inp == 'l'):
            new_pos = (self.rat_pos[0],self.rat_pos[1]-1)
        elif (inp == 'right' or inp == 'R' or inp == 'r'):
            new_pos = (self.rat_pos[0],self.rat_pos[1]+1)
        else:
            return
        if (not self.is_valid(new_pos)):
            return
        
        self.grid[self.rat_pos[0]][self.rat_pos[1]] = '-'
        self.rat_pos = new_pos
        self.grid[self.rat_pos[0]][self.rat_pos[1]] = 'J'
        return
    


    def find_path(self,start,end): # A* Search Algorithm
        def h(pos):
            return abs(pos[0]-end[0]) + abs(pos[1]-end[1])
        
        def g(pos):
            return abs(pos[0]-start[0]) + abs(pos[1]-start[1])
        
        
        def is_valid(pos):
            return pos[0] >= 0 and pos[0] < self.grid_high and pos[1] >= 0 and pos[1] < self.grid_width and self.grid[pos[0]][pos[1]] != '#'
        
        def get_neighbours(pos):
            neighbours = []
            for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_pos = (pos[0]+i,pos[1]+j)
                if (is_valid(new_pos)):
                    neighbours.append(new_pos)
            return neighbours
        
        open_list = [start]
        closed_list = []
        came_from = {}
        g_score = {start:0}
        f_score = {start:h(start)}

        while open_list:
            current = min(open_list,key=lambda x:f_score[x])
            if (current == end):
                path = []
                while current in came_from:
                    path.insert(0,current)
                    current = came_from[current]
                return path

            open_list.remove(current)
            closed_list.append(current)

            for neighbour in get_neighbours(current):
                if neighbour in closed_list:
                    continue
                tentative_g_score = g_score[current] + 1
                if neighbour not in open_list:
                    open_list.append(neighbour)
                elif tentative_g_score >= g_score[neighbour]:
                    continue
                
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = g_score[neighbour] + h(neighbour)

        return []


    def move_cat(self):
        if (self.cat_pos == self.exit):
            return
        
        new_pos = self.cat_pos

        path_to_rat = self.find_path(self.cat_pos,self.rat_pos)
        path_to_exit = self.find_path(self.cat_pos,self.exit)

        to_rat = len(path_to_rat)
        to_exit = len(path_to_exit)
        
        if (to_rat < 2):
            new_pos = self.rat_pos
            self.grid[self.cat_pos[0]][self.cat_pos[1]] = '-'
            self.cat_pos = new_pos
            self.grid[self.cat_pos[0]][self.cat_pos[1]] = 'T'
            return

            
        if (to_rat < to_exit):
            new_pos = path_to_rat[1]
        else:
            if (len(path_to_exit) <= 1):
                new_pos = self.exit
                return
            new_pos = path_to_exit[1]

        self.grid[self.cat_pos[0]][self.cat_pos[1]] = '-'
        self.cat_pos = new_pos
        self.grid[self.cat_pos[0]][self.cat_pos[1]] = 'T'
        return