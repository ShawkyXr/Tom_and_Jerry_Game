from time import sleep
import os



class Game:

    def __init__(self,h,w,cat,rat,exit,obs):
        self.grid_high = h
        self.grid_width = w
        self.grid = [['-' for i in range(self.grid_width)] for j in range(self.grid_high)]
        self.cat_pos = cat
        self.rat_pos = rat
        self.exit = exit
        self.obstacles = obs

    def start(self):
        self.build()
        self.display(False)
        self.play()

    def build(self):

        self.grid[self.cat_pos[0]][self.cat_pos[1]] = 'T'
        self.grid[self.rat_pos[0]][self.rat_pos[1]] = 'J'
        self.grid[self.exit[0]][self.exit[1]] = 'E'

        for obstacle in self.obstacles:
            self.grid[obstacle[0]][obstacle[1]] = '#' 

    def play(self):
        while True:

            self.move_rat()

            self.move_cat()

            if (self.rat_pos == self.cat_pos):
                self.grid[self.rat_pos[0]][self.rat_pos[1]] = 'X'
                self.display(True)
                print("Game Over :(")
                break
            
            if (self.rat_pos == self.exit):
                print("WOW! You Won")
                break
                
            self.display(True)



    def clear_terminal(self,k):
        if os.name == 'nt':
            os.system('cls')  # For Windows
        else:
            for _ in range(k):
                print("\033[F\033[K", end='')  



    def display(self,clear):
        if (clear):
            self.clear_terminal(self.grid_high+1)
        for i in range(self.grid_high):
            for j in range(self.grid_width):
                print(self.grid[i][j], end=' ')
            print()

    def is_valid(self,pos):
        return pos[0] >= 0 and pos[0] < self.grid_high and pos[1] >= 0 and pos[1] < self.grid_width and self.grid[pos[0]][pos[1]] != '#'
    

    def move_rat(self):
        print("Enter the direction to move the rat(up,down,left,right) : ", end='')
        inp = input()
        new_pos = self.rat_pos
        if (inp == 'up'):
            new_pos = (self.rat_pos[0]-1,self.rat_pos[1])
        elif (inp == 'down'):
            new_pos = (self.rat_pos[0]+1,self.rat_pos[1])
        elif (inp == 'left'):
            new_pos = (self.rat_pos[0],self.rat_pos[1]-1)
        elif (inp == 'right'):
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


if __name__ == "__main__":
    Easy = Game(5,5,(2,0),(1,3),(4,4),[(2,2),(2,4)])
    Mediam = Game(5,5,(2,0),(1,3),(4,4),[(2,2),(2,4)])
    Hard = Game(5,5,(2,0),(1,3),(4,4),[(2,2),(2,4)])
    Easy.start()