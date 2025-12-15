# import packages used
import numpy as np

def solve_VFI(par):
    Cstar = np.zeros([par.W+1])
    
    # Parameters for VFI
    max_iter = par.max_iter   # maximum number of iterations
    delta = 1000 #difference between V_next and V_now
    tol = par.tol #convergence tol. level
    it = 0  #iteration counter 
    V_now = np.zeros([par.W+1]) #arbitrary starting values
    
    while (max_iter>= it and tol<delta):
        it = it+1
        V_next = V_now.copy()
        for w in range(par.W+1):
            #Fill in
            c = np.arange(w+1)  #(w+1) vector of possible consumption choices given cake size w
            V_next_c = V_next[w - c ]  #(w+1) vector of value next period given consumption c
            V_guess = np.sqrt(c)+par.beta*V_next_c #(w+1) vector of possible values next period
            V_now[w] = np.amax(V_guess) #Find the maximum value
            Cstar[w] = np.argmax(V_guess) #Find the corresponding consumption
            ## fill in end ##
            
        delta = np.amax(np.abs(V_now - V_next))
    
    class sol: pass
    sol.C = Cstar
    sol.V = V_now
    sol.it = it

    return sol