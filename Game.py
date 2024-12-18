import  os

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

            self.move_cat() # move cat using BFS 

            if (self.rat_pos == self.cat_pos): # if cat eat the rat
                self.grid[self.rat_pos[0]][self.rat_pos[1]] = 'X'
                self.display(True)
                print("Game Over :(")
                break
            
            if (self.rat_pos == self.exit):
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
                print(self.grid[i][j], end=' ')
            print()



    def is_valid(self,pos): # position is valid or not
        return pos[0] >= 0 and pos[0] < self.grid_high and pos[1] >= 0 and pos[1] < self.grid_width and self.grid[pos[0]][pos[1]] != '#'
    


    def move_rat(self): # move the rat
        print("Enter the direction to move the rat(up 'U' ,down 'D' ,left 'L',right 'R') : ", end='')
        inp = input()
        new_pos = self.rat_pos
        if (inp == 'up' or inp == 'U'):
            new_pos = (self.rat_pos[0]-1,self.rat_pos[1])
        elif (inp == 'down' or inp == 'D'):
            new_pos = (self.rat_pos[0]+1,self.rat_pos[1])
        elif (inp == 'left' or inp == 'L'):
            new_pos = (self.rat_pos[0],self.rat_pos[1]-1)
        elif (inp == 'right' or inp == 'R'):
            new_pos = (self.rat_pos[0],self.rat_pos[1]+1)
        else:
            return
        if (not self.is_valid(new_pos)):
            return
        
        self.grid[self.rat_pos[0]][self.rat_pos[1]] = '-'
        self.rat_pos = new_pos
        self.grid[self.rat_pos[0]][self.rat_pos[1]] = 'J'
        return
    


    def find_path(self,start,end): # BFS Search Algorithm
        visited = [[False for i in range(self.grid_width)] for j in range(self.grid_high)]
        queue = []
        queue.append(start)
        visited[start[0]][start[1]] = True
        parent = {}
        while queue:
            node = queue.pop(0)
            if (node == end):
                break
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dir in directions:
                new_pos = (node[0]+dir[0],node[1]+dir[1])
                if (self.is_valid(new_pos) and not visited[new_pos[0]][new_pos[1]]):
                    queue.append(new_pos)
                    visited[new_pos[0]][new_pos[1]] = True
                    parent[new_pos] = node
                    
        path = []

        while end != start:
            path.append(end)
            end = parent[end]
        path.append(start)
        path.reverse()

        return path



    def move_cat(self):
        if (self.cat_pos == self.exit):
            return
        
        new_pos = self.cat_pos

        path_to_rat = self.find_path(self.cat_pos,self.rat_pos)
        path_to_exit = self.find_path(self.cat_pos,self.exit)

        to_rat = len(path_to_rat)
        to_exit = len(path_to_exit)

        if (to_rat <= 3):
            self.grid[self.cat_pos[0]][self.cat_pos[1]] = '-'
            self.cat_pos = self.rat_pos
            self.grid[self.cat_pos[0]][self.cat_pos[1]] = 'T'
            return
        
        if (to_rat < to_exit):
            new_pos = path_to_rat[1]
        else:
            new_pos = path_to_exit[1]

        self.grid[self.cat_pos[0]][self.cat_pos[1]] = '-'
        self.cat_pos = new_pos
        self.grid[self.cat_pos[0]][self.cat_pos[1]] = 'T'
        return

