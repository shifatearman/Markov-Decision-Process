import copy
'''States'''
board = [0,0,0,0,0,0]
'''Actions'''
L = 0
R = 1
actionlist = [L,R]
'''Transition Function'''
def T(i,a):
    if(i == 0):
        if(a == 0):
            return (i)
        elif(a == 1):
            return (i)
    elif(i == 1):
        if(a == 0):
            return (i-1) 
        elif(a == 1):
            return (i+1)
    elif(i == 2):
        if(a == 0):
            return (i-1) 
        elif(a == 1):
            return (i+1)
    elif(i == 3):
        if(a == 0):
            return (i-1) 
        elif(a == 1):
            return (i+1)
    elif(i == 4):
        if(a == 0):
            return (i-1) 
        elif(a == 1):
            return (i+1)
    elif(i == 5):
        if(a == 0):
            return (i)
        elif(a == 1):
            return (i)
'''Reward Function'''
reward = [1,0,0,0,0,5]
def R(f):
    return reward[f]
'''Discount'''
gamma = 0.5
'''Converging Factor'''
epsilon = 0.001


def value_iteration():
    Q1 = [ [0, 0],
           [0, 0],
           [0, 0],
           [0, 0],
           [0, 0],
           [0, 0]]
    while True:
        Q=copy.deepcopy(Q1)
        for i in range(6):
            for a in actionlist:
                Q1[i][a] = reward[T(i,a)] + gamma * 1 * Q[T(i,a)][a]
                print(Q1[i][a])
        
           

            
    
v = value_iteration()
