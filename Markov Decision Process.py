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
actlist = {UP:1, DOWN:2, LEFT:3, RIGHT:4}
'''Reward Function'''
reward = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]] 
reward[-1][-1] = 1
reward[-2][-2] = -1
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
            return (-1,-1,0.8),(-1,-1,0.1),(-1,-1,0.1)
        elif(actions == DOWN):
            return (-1,-1,0.8),(-1,-1,0.1),(-1,-1,0.1)
        elif(actions == LEFT):
            return (-1,-1,0.8),(-1,-1,0.1),(-1,-1,0.1)
        elif(actions == RIGHT):
            return (-1,-1,0.8),(-1,-1,0.1),(-1,-1,0.1)
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
            return (-2,-2,0.8),(-2,-2,0.1),(-2,-2,0.1)
        elif(actions == DOWN):
            return (-2,-2,0.8),(-2,-2,0.1),(-2,-2,0.1)
        elif(actions == LEFT):
            return (-2,-2,0.8),(-2,-2,0.1),(-2,-2,0.1)
        elif(actions == RIGHT):
            return (-2,-2,0.8),(-2,-2,0.1),(-2,-2,0.1)      
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
                U1[i][j] = max(sum(p*(R(k,l)+gamma*U[k][l]) for (k,l,p) in T(i,j,a)) for a in actlist)
                print(i,j,U1[i][j],U[i][j],reward[i][j])
                delta = max(delta, abs(U1[i][j] - U[i][j]))
        break
        if delta <= epsilon*(1 - gamma)/gamma:
            return U
            
            
                #
                #U1[i][j] = max(sum(p*(R(k,l)+gamma*U[k][l]) for (k,l,p) in T(i,j,a)) for a in actlist)
                #print(i,j,U1[i][j])
                    #q_value = sum(p * (R(k,l) + gamma * U[k][l]) for (k,l,p) in T(i,j,a))
                    #print(q_value)
                    #(k1,l1,p1), (k2,l2,p2), (k3,l3,p3) = T(i,j,a)
                    #q_value = p1 * (R(k1,l1) + gamma * U[k1][l1]) + p2 * (R(k2,l2) + gamma * U[k2][l2]) + p3 * (R(k3,l3) + gamma * U[k3][l3])
                    #print(q_value)
                    #sum(p*U[k][l])
                    
                    #U1[i][j] = max(U[i][j],q_value)
                      
                    #U[i][j] = max(q_value)
                    #
                    
                    #U1[i][j] = R[i][j] + gamma * max(sum(p*U[i][j] for (k,l,p) in T(i, j, a)))

print(value_iteration())

'''
 U=U1.copy()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for a in actlist:
                for (k,l,p) in T(i,j,a):
                    print(i,j,a,k,l,p)
                    '''