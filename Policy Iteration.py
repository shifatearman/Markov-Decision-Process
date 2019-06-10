import random
import numpy
import copy
#a = random.choice(actlist)
'''States'''
grid = [[0, 0, 0, +1],
        [0, "W", 0, -1],
        [0, 0, 0, 0]]
'''Actions'''
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
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
gamma = float(input("Enter discount: "))
'''Convergence Factor'''
epsilon = 0.001
'''Living Reward'''
lr = float(input("Enter living reward: "))
print("\n")


'''Policy Iteration'''
def policy_evaluation(pi, U, k = 20):
    for f in range(k):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                U[i][j] =  lr + R(i,j) + gamma * max(sum(p*(U[k][l]) for (k,l,p) in T(i,j,a)) for a in actlist)
    return U
def argmax(i,j,U):
    if(i == 1 and j ==1):
        return None
    elif(i == 0 and j == 3):
        return None
    elif(i == 1 and j == 3):
        return None
    best = actlist[0]
    best_score = expected_utility(actlist[0],i,j,U)
    for a in actlist:
        expected_score = expected_utility(a,i,j,U)
        if expected_score > best_score:
            best = a 
            best_score = expected_score
    return best  
def expected_utility(a,i,j,U):
    return sum(p*U[k][l] for (k,l,p) in T(i,j,a))
def policy_iteration():
    U = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]] 
    pi = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]] 
    for i in range(len(pi)):
        for j in range(len(pi[i])):
            pi[i][j] = random.choice(actlist)
    print(pi)
    while True:
        # Policy Evaluation
        U = policy_evaluation(pi,U) 
        unchanged = True
        # Policy Extraction
        for i in range(len(grid)):
            for j in range(len(grid[i])): 
                a = argmax(i,j,U)
                # Policy Improvement
                if(a != pi[i][j]):
                    pi[i][j] = a
                    unchanged = False
        if unchanged:
            return pi
policy = policy_iteration()
'''
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(policy[i][j],end = ' ')
    print("\n")
'''

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if(policy[i][j] == 0):
            print("UP",' ')
        elif(policy[i][j] == 1):
            print("DOWN",' ')
        elif(policy[i][j] == 2):
            print("LEFT",' ')
        elif(policy[i][j] == 3):
            print("RIGHT",' ')
        elif(policy[i][j] == None):
            print(None,' ')
    print("\n")
