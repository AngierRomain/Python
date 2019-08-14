def miroir(M): #M est une matrice
    for i in range(len(M)): #je parcours les lignes
        for j in range(len(M[0])//2): #je parcours les colonnes jusqu'à la moitié
            M[i][j],M[i][len(M[0])-j-1] = M[i][len(M[0])-j-1],M[i][j]
    return M

def afficher(M):
    for i in range(len(M)):
        print(M[i])

def init(n):
    return [[randint(0,1) for i in range(n)]for j in range(n)]
