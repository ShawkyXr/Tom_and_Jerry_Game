import random

def manhattan_distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def generate_map(map_level):
    # Generate a map
    

    if map_level == 0:
        map_width = random.randint(5,10)
        map_height = random.randint(5,10)
        map_exit = (random.randint(0,map_height-1),random.randint(0,map_width-1))
        while True:
            map_rat = (random.randint(0,map_height-1),random.randint(0,map_width-1))
            if map_rat != map_exit:
                break
        
        while True:
            map_cat = (random.randint(0,map_height-1),random.randint(0,map_width-1))
            if map_cat != map_exit and map_cat != map_rat and manhattan_distance(map_cat,map_rat) > 2 and manhattan_distance(map_rat,map_exit) < manhattan_distance(map_cat,map_exit):
                break
        
        map_obstacles = []
        for i in range(random.randint(1,3)):
            while True:
                obstacle = (random.randint(0,map_height-1),random.randint(0,map_width-1))
                if obstacle != map_exit and obstacle != map_rat and obstacle != map_cat and obstacle not in map_obstacles:
                    map_obstacles.append(obstacle)
                    break
        
    elif map_level == 1:
        map_width = random.randint(10,15)
        map_height = random.randint(10,15)
        map_exit = (random.randint(0,map_height-1),random.randint(0,map_width-1))
        while True:
            map_rat = (random.randint(0,map_height-1),random.randint(0,map_width-1))
            if map_rat != map_exit:
                break
        
        while True:
            map_cat = (random.randint(0,map_height-1),random.randint(0,map_width-1))
            if map_cat != map_exit and map_cat != map_rat and manhattan_distance(map_cat,map_rat) > 3 and manhattan_distance(map_rat,map_exit) < manhattan_distance(map_cat,map_exit):
                break
        
        map_obstacles = []
        for i in range(random.randint(3,6)):
            while True:
                obstacle = (random.randint(0,map_height-1),random.randint(0,map_width-1))
                if obstacle != map_exit and obstacle != map_rat and obstacle != map_cat and obstacle not in map_obstacles:
                    map_obstacles.append(obstacle)
                    break
        
    else:
        map_width = random.randint(15,20)
        map_height = random.randint(15,20)
        map_exit = (random.randint(0,map_height-1),random.randint(0,map_width-1))
        while True:
            map_rat = (random.randint(0,map_height-1),random.randint(0,map_width-1))
            if map_rat != map_exit:
                break
        
        while True:
            map_cat = (random.randint(0,map_height-1),random.randint(0,map_width-1))
            if map_cat != map_exit and map_cat != map_rat and manhattan_distance(map_cat,map_rat) > 4 and manhattan_distance(map_rat,map_exit) < manhattan_distance(map_cat,map_exit):
                break
        
        map_obstacles = []
        for i in range(random.randint(6,10)):
            while True:
                obstacle = (random.randint(0,map_height-1),random.randint(0,map_width-1))
                if obstacle != map_exit and obstacle != map_rat and obstacle != map_cat and obstacle not in map_obstacles:
                    map_obstacles.append(obstacle)
                    break
        
    return map_height,map_width,map_cat,map_rat,map_exit,map_obstacles
