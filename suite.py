from math import sqrt

def suite(n):
    #Initialisation
    #i = 0
    u = 1
    for i in range(n):
        u = sqrt(1+u)
    return u
        


        
