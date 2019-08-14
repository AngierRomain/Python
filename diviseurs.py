from math import *
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

#si la  somme des diviseurs de n est égal à 2*n alors le nombre
#est parfait sinon il est pas parfait
def parfait(n):
    if(sommeDiviseurs(n)==2*n):
        return True
    else:
        return False

def amicaux(a,b):
    nba = sommediviseurs(a)-a #calcul de nba
    nbb = sommediviseurs(b)-b #calcul de nbb
    if nba == b and nbb == a: #condition si nba = b et nbb = a:
        return True
    else:
        return False
def pgcdEuclide(a,b):
    #   a   b   r
    #   35  15  5
    #   15  5   0
    #   5   0
    while b!=0: #tant que b non nul
        r=a%b #le restte de a par b
        a=b #a prend la valeur de b
        b=r #b prend la valeur du reste
    return a # retourner a

def init(n):
    L=[] #initialisation liste
    for i in range (0,n+1): #pour i allant de 0 à n:
        L=L+[i] #dans L je mets [i]
    return L
    #init(100) renvoie [0,1,2,3,4,5,6,7,..,100]
    #init (20) renvoie [0,1,2,3,4,5,6,7,..,20]
    #Crible d'Ératosthène

def barrerMultiplesDe2(n):
    L=init(n)
    #Ecrire le programme qui permet de remplacer les multiples de 2 par des 0
    for i in range(3,n+1):
        if i%2==0:
            L[i]=0
    return L
        












    
