def afficher(M):
    for i in range(len(M)):
        print(M[i])
        
def sommeLig(M, i): # M[i][0] + M [i][1] + M[i][2] + ... + M[i][n-1] # avec n = len(M)
    n = len(M)
    s = 0 #initialisation
    for i in range(n): #on parcourt toutes les lignes de M[0] à M[n-1]
        for j in range(n): #on parcourt la liste M[i]
            s=s+M[i][j] #on calcule la somme 
    return s 
                    
def sommeCol(M,j): # M[0][j] + M[1][j] + M[2][j]+ ... M[n-1][j] # avec n = len(M)
    n = len(M)
    s = 0 #initialisation
    for i in range(n): #on parcourt toutes les colonnes de M[0] à M[n-1]
        for j in range(n): #on parcourt la liste M[i]
            s=s+M[j][i] #on calcule la somme 
    return s

def sommeDiag1(M): #M[0][0] + M[1][1] + M[2][2] + ... + M[n-1][n-1]
    s = 0 #initialisation
    for i in range(len(M)): 
            s=s+M[i][i]
    return s

def sommeDiag2(M): #...
    n = len(M)
    s = 0 #initialisation
    for i in range(n): #on parcourt toutes les lignes de M[0] à M[n-1]
            s=s+M[i][n-1-i]
    return s
    
#M=[[1,2,3],[4,5,6],[7,8,9]]
def magic(M): #renvoie True si M est un carré magique, False sinon
    afficher(M) #On affiche la matrice
    if(sommeDiag1(M) != sommeDiag2(M)):
        return False
    else:
        for i in range(len(M)):
            if(sommeLig(M,i) != sommeDiag1(M)):
               return False
    else:
        
        
    

    
