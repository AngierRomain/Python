#ecrire une fonction premier qui prend en argument un entier n et
#qui renvoie True si n est premier sinon False.
from math import sqrt
def nbPremier(n):
    for i in range(2,int(sqrt(n))): #n-1
        if n%i==0:
            return False
    return True

#utiliser sqrt(n)
#tests
# 1597 = true 1601 = true 51 = false

def nbreDeDeux(n):
    #on veut récupérer le nombre de facteurs 2 contenus dans
    #la décomposition de n
    cpt=0
    while n%2 == 0:
        n=n/2
        cpt=cpt+1
    return cpt

def diviseurs(n):
    T=[]#Initialisation
    for i in range(1,n+1):
        if (n%i==0):
            T=T+[i]
    return T
        
def sommeDiviseurs(n):
    T=diviseurs(n)
    return sum(T)
#>>> diviseurs(6)
#[1, 2, 3, 6]
#>>> sommeDiviseurs(6)
#12
#>>> 

#Pour parcourir une liste on peut faire:
# for i in range(0,4):
        # print(T[i])


