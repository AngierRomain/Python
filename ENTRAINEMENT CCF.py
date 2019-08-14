from random import randint
def afficher(M):
    for i in range(len(M)):
        print M[i]

def init(n): #matrice carrée d'ordre n remplie aléatoirement de 0 et de 1
    return[[ randint(0, 1) for i in range(n)] for j in range(n)]

    #TEST
    #afficher(init(3))
    #[1, 0, 0]
    #[0, 1, 0]
    #[1, 1, 1]


def init2(n,m): #matrice rectangulaire à n lignes m colonnes remplie aléatoirement de 0 et de 1
    return[[randint(0,1) for i in range(m)] for j in range(n)]

    #TEST
    #afficher(init2(3,5))
    #[0, 0, 0, 0, 1]
    #[1, 0, 1, 0, 0]
    #[0, 0, 0, 1, 0]

def alig(L): #prend en argument une liste L aléatoirement remplie de 0 et de 1
             #et renvoie True si L est remplie uniquement de 1 sinon False
    for i in range(len(L)):
        if L[i]==0:
            return False
    return True

def alig2(L): #Avec une autre syntaxe
    for i in L:
        if L[i]==0:
            return False
    return True

def alignement(n):
    M=init(n)
    afficher(M)
    cpt=0
    for i in range(len(M)):
        if alig(M[i]) == True:
            cpt +=1
    return cpt
    #TEST
#for i in range (3):

    # alignement(3)
    #	
    #[0, 0, 1]
    #[1, 0, 1]
    #[0, 1, 0]
    #0
    #[0, 1, 1]
    #[1, 1, 0]
    #[1, 0, 1]
    #0
    #[0, 1, 1]
    #[1, 0, 0]
    #[0, 0, 0]
    #0

##Ecire une fonction alignement qui prend en argument un entier n
##et qui renvoie le nombre de lignes complètes de la matrice carrée d'ordre n.
        
