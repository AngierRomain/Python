def afficher(M):
    for i in range(len(M)):
        print(M[i])
def init(n):
    return[[0 for i in range(n)]for j in range(n)]
def diag2(n):
    M=init(n)
    for i in  range(n):
        M[i][n-1-i] = 1
    afficher(M)
