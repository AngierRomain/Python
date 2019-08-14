def afficher(M):
    for i in range(len(M)):
        print(M[i])

def init(n):
    return [[0 for i in range(n)]for i in range(n)]

def pascal(n):
    M=init(n)
    for i in range(len(M)): #remplit la première colonne de 1
        M[i][0]=1
    return M

def pascal2(n):
    M=pascal(n)
    for i in range(1,n): #deuxieme colonne
        for j in range(n):
            M[i][j]= M[i-1][j-1]+ M[i-1][j]
    return M

def sommeLignes(n):#renvoie la somme des coefficients des lignes du triangle de pascal
    #sommeLignes(4) renvoie [1, 2, 4, 8]
    M=pascal(n)
    L=[0 for i in range(n)] #initialisation
    for i in range(n): #je parcours toutes les lignes de M[0] à M[n-1]
        for j in range(n): #je parcours la liste M[i]
            L[i]=L[i]+M[i][j] #je calcule la somme L[i]
    return L

def binairePascal(n):
    M=pascal(n)
    for i in range(n):
        for j in range(n):
            if M[i][j]%2 == 0:
                M[i][j] = 0
            else:
                M[i][j]= 1
    return M
        
def factorielleIterative(n): #1*2*3*..*n
    p=1
    for i in range(1,n+1):
        p=p*i
    return p

def factorielleRecursive(n):
    if n==0:
        return 1
    else:
        return n*factorielleRecursive(n-1)
#factorielleRecursive(5)    5*4*3*2*1
#120

def fibonnacciIterative(n):
    u=1
    v=1
    cpt=2
    while cpt <= n:
        w = u+v
        u = v
        v = w
        cpt = cpt+1
    return w












    
