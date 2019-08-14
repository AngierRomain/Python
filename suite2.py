def suite2(n):
    #initialisation
    w = 1
    for i in range(n):
        w = 2*w+1
    return w

def suite3(n):
    w = 5
    cpt = 0
    while(cpt < n):
        w = 2*w+1
        cpt = cpt +1
    return w
        
