#U1[i][j] = max(sum(p*(R(k,l)+gamma*U[k][l]) for (k,l,p) in T(i,j,a)) for a in actlist)
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
