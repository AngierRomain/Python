def afficher(M): #M est une matrice
    #sous forme d'un tableau
    for i in range(len(M)):
        print(M[i])
        
def init(n):
    #renvoie une matrice carrée d'ordre n nulle
    return[[0 for i in range(n)] for j in range(n)]
    
def identite(n):
    #renvoie la matrice carrée identité d'ordre n
    M=init(n) #initialisation
    for i in range(n): #je remplis la diagonale 
        M[i][i]=1
    return M

def cadre(n):
    #renvoie la matrice nulle, remplie de 1 sur les 4 bords.
    M=init(n)
    for i in range(n):
        M[0][i]=1 #je remplis la première ligne
        M[i][0]=1 #                       colonne
        M[n-1][i]=1 #            dernière ligne
        M[i][n-1]=1 #                     colonne
    return M

def croix(n):
    #renvoie la matrice nulle avec des 1 sur les deux diagonales
    M=init(n) #initialisation
    for i in range(n): #je remplis la diagonale 
        M[i][i]=1
        M[-i-1][i]=1
    return M


    
def sommeDiag(M):
  res=0
  for i in range(len(M)):
     res = res + M[i][i] 
  return res
