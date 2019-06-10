delta = 0
#delta = max(delta, abs(U1[i] - U[i]))
        #if delta <= epsilon*(1 - gamma)/gamma:
         #   return U    
         
         
         if(i == 0 and a == L):
        return i
    elif(i == 0 and a == R):
        return i
    elif(i == 5 and a == L):
        return i
    elif(i == 5 and a == R):
        return i
    elif(i == 1 or i == 2 or i == 3 or i == 4 and a == L):
        return i-1
    elif(i == 1 or i == 2 or i == 3 or i == 4 and a == R):
        return i+1
    
    
    
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
    
'''
def best_policy(U):
    pi = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pi[i][j] = numpy.argmax(actlist, key = lambda a: expected_utility(a, i, j, U))
    return pi
'''

'''
policy = best_policy(v)
'''

'''
def best_policy(U):
    pi = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pi[i][j] = numpy.argmax(actlist, key = lambda a: expected_utility(a, i, j, U))
    return pi
'''

'''
policy = best_policy(v)
'''