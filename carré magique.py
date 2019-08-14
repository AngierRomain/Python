def afficher(M): #Carré magique voir fiche
    for i in range(len(M)):
        print(M[i])
def init(n):
    return[[0 for i in range(n)]for j in range(n)]
def Magic(M):
    i=0
    j=(5-1)//2
    k=1
    M[i][j]=1
    while(k < 25):
        
