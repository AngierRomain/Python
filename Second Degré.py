#Résoudre une équation du second degré
from math import sqrt
def secondDeg(a,b,c):
    D=b**2-4*a*c
    if D > 0:
        print("Deux solutions ",(-b+sqrt(D))/(2*a),"et",(-b-sqrt(D))/(2*a))
    elif D==0:
        print("Une solution", -b/2*a)
    else:
        print("Aucune solution")
        
        
    
    
