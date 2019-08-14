def afficher(A=[[1,3,5],[2,4,6],[7,8,0]]): #afficher A sous forme de matrice
    #A=[[1,3,5],[2,4,6],[7,8,0]]
    for i in range(len(A)): #len(A) pour une matrice indique le nombre de ligne
        print(A[i])


#créer une liste de taille n remplie de 0, ainsi init[5] renvoie [0,0,0,0,0]
def init1(n):
    A=[]
    for i in range(n):
        A += [0] # T=T+[] # On concatène des listes de [0]
    return A

def init2(n):
    return [0 for i in range(n)]


#créer une liste de taille n remplie de 0 ou 1
#de manière aléatoire,ainsi init3(5) renvoie [0,1,0,0,1]
from random import randint
def init3(n):
    return [randint(0,1) for i in range(n)]


#créer une matrice carrée d'ordre n remplie de 0
def init4(n):
    return [[0 for ligne in range(n)] for colonne in range(n)]

def diag2(n):
    A=init1(n) #initialisation
    for i in range(n): #je remplis la diagonale secondaire
        A[i][n-1-i]=1 #la somme des indices qui se trouvent sur la
                      # diagonale secondaire vaut n-1
    return A 
    
#def initialisation(n):



#créer une matrice carrée d'ordre n remplie de nombres aléatoires
#compris entre 0 et 20, puis l'afficher
