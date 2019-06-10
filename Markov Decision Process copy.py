import random
import numpy
import copy
#a = random.choice(actlist)
'''States'''
grid = [[0, 0, 0, +1],
        [0, "W", 0, -1],
        [0, 0, 0, 0]]
'''Actions'''
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
actlist = [UP, DOWN, LEFT, RIGHT]
'''Reward Function'''
reward = [[0, 0, 0, 1],
          [0, 0, 0, -1],
          [0, 0, 0, 0]] 
def R(i, j):  
    return reward[i][j]
'''Transition Function'''            
def T(i,j,actions):
    if(i == 0 and j == 0):
        if(actions == UP):
            return (i,i,0.8),(i,i,0.1),(i,j+1,0.1)
        elif(actions == DOWN):
            return (i+1,j,0.8),(i,j,0.1),(i,j+1,0.1)
        elif(actions == LEFT):
            return (i,j,0.8),(i,j,0.1),(i+1,j,0.1)
        elif(actions == RIGHT):
            return (i,j+1,0.8),(i,i,0.1),(i+1,j,0.1)
    elif (i == 0 and j == 1):
        if(actions == UP):
            return (i,i,0.8),(i,j-1,0.1),(i,j+1,0.1)
        elif(actions == DOWN):
            return (i,j,0.8),(i,j-1,0.1),(i,j+1,0.1)
        elif(actions == LEFT):
            return (i,j-1,0.8),(i,j,0.1),(i,j,0.1)
        elif(actions == RIGHT):
            return (i,j+1,0.8),(i,j,0.1),(i,j,0.1)
    elif(i == 0 and j == 2):
        if(actions == UP):
            return (i,j,0.8),(i,j-1,0.1),(i,j+1,0.1)
        elif(actions == DOWN):
            return(i+1,j,0.8),(i,j-1,0.1),(i,j+1,0.1)
        elif(actions == LEFT):
            return (i,j-1,0.8),(i,j,0.1),(i+1,j,0.1)
        elif(actions == RIGHT):
            return (i,j+1,0.8),(i,j,0.1),(i+1,j,0.1)
    elif(i == 0 and j == 3):
        if(actions == UP):
            return (i,j,0),(i,j,0),(i,j,0)
        elif(actions == DOWN):
            return (i,j,0),(i,j,0),(i,j,0)   
        elif(actions == LEFT):
            return (i,j,0),(i,j,0),(i,j,0)   
        elif(actions == RIGHT):
            return (i,j,0),(i,j,0),(i,j,0)
    # 2nd row
    elif (i == 1 and j == 0):
        if(actions == UP):
            return (i-1,j,0.8),(i,j,0.1),(i,j,0.1)
        elif(actions == DOWN):
            return (i+1,j,0.8),(i,j,0.1),(i,j,0.1)
        elif(actions == LEFT):
            return (i,j,0.8),(i-1,j,0.1),(i+1,j,0.1)
        elif(actions == RIGHT):
            return (i,j,0.8),(i-1,j,0.1),(i+1,j,0.1)
    elif(i == 1 and j ==1):
        if(actions == UP):
            return (i,j,0.8),(i,j,0.1),(i,j,0.1)
        elif(actions == DOWN):
            return (i,j,0.8),(i,j,0.1),(i,j,0.1)
        elif(actions == LEFT):
            return (i,j,0.8),(i,j,0.1),(i,j,0.1)
        elif(actions == RIGHT):
            return (i,j,0.8),(i,j,0.1),(i,j,0.1)
    elif (i == 1 and j == 2):
        if(actions == UP):
            return (i-1,j,0.8),(i,j,0.1),(i,j+1,0.1)
        elif(actions == DOWN):
            return (i+1,j,0.8),(i,j,0.1),(i,j+1,0.1)
        elif(actions == LEFT):
            return (i,j,0.8),(i-1,j,0.1),(i+1,j,0.1)
        elif(actions == RIGHT):
            return (i,j+1,0.8),(i-1,j,0.1),(i+1,j,0.1)
    elif(i == 1 and j == 3):
        if(actions == UP):
            return (i,j,0),(i,j,0),(i,j,0)   
        elif(actions == DOWN):
            return (i,j,0),(i,j,0),(i,j,0)   
        elif(actions == LEFT):
            return (i,j,0),(i,j,0),(i,j,0)
        elif(actions == RIGHT):
            return (i,j,0),(i,j,0),(i,j,0)   
    # 3rd row
    elif(i == 2 and j == 0):
        if(actions == UP):
            return (i-1,j,0.8),(i,j,0.1),(i,j+1,0.1)
        elif(actions == DOWN):
            return (i,j,0.8),(i,j,0.1),(i,j+1,0.1)
        elif(actions == LEFT):
            return (i,j,0.8),(i-1,j,0.1),(i,j,0.1)
        elif(actions == RIGHT):
            return (i,j+1,0.8),(i-1,j,0.1),(i,j,0.1)
    elif (i == 2 and j == 1):
        if(actions == UP):
            return (i,j,0.8),(i,j-1,0.1),(i,j+1,0.1)
        elif(actions == DOWN):
            return (i,j,0.8),(i,j-1,0.1),(i,j+1,0.1)
        elif(actions == LEFT):
            return (i,j-1,0.8),(i,j,0.1),(i,j,0.1)
        elif(actions == RIGHT):
            return (i,j+1,0.8),(i,j,0.1),(i,j,0.1)
    elif(i == 2 and j == 2):
        if(actions == UP):
            return (i-1,j,0.8),(i,j-1,0.1),(i,j+1,0.1)
        elif(actions == DOWN):
            return (i,j,0.8),(i,j-1,0.1),(i,j+1,0.1)
        elif(actions == LEFT):
            return (i,j-1,0.8),(i-1,j,0.1),(i,j,0.1)
        elif(actions == RIGHT):
            return (i,j+1,0.8),(i-1,j,0.1),(i,j,0.1)
    elif(i == 2 and j == 3):
        if(actions == UP):
            return (i-1,j,0.8),(i,j-1,0.1),(i,j,0.1)
        elif(actions == DOWN):
            return (i,j,0.8),(i,j-1,0.1),(i,j,0.1)
        elif(actions == LEFT):
            return (i,j-1,0.8),(i-1,j,0.1),(i,j,0.1)
        elif(actions == RIGHT):
            return (i,j,0.8),(i-1,j,0.1),(i,j,0.1)            
         
'''Discount'''
gamma = 0.9
epsilon = 0.001
'''Value Iteration'''
def value_iteration():
    U1 = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]] 
    while True:
        U=copy.deepcopy(U1)
        delta = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                U1[i][j] = R(i,j) + gamma * max(sum(p*(U[k][l]) for (k,l,p) in T(i,j,a)) for a in actlist)
                delta = max(delta, abs(U1[i][j] - U[i][j]))
        if delta <= epsilon*(1 - gamma)/gamma:
            return U    
v = value_iteration()
print("\n")
for i in range(len(v)):
    for j in range(len(v[i])):
        print(v[i][j],end='   ')
    print("\n")