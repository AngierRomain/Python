def afficher(M):
    for i in range(len(M)):
        print(M[i])

def init():
    return [[0 for i in range(8)]for j in range(8)]

def tour(lig, col):
    M = init()
    for i in range(len(M)):
        M[i][col] = 1
        M[lig][i] = 1
    M[lig][col] = 2
    return M

def fou(lig, col):
    M = init()
    for i in range(len(M)):
        for j in range(len(M)):
            if i+j == col+lig or i-j == lig-col:
                M[i][j] = 1
    M[lig][col]=3
    return M

def dedans(i,j):
    res=True
    if i<0 or i>7 or j<0 or j>7:
        res=False
    return res

def cavalier(lig, col):
    M = init()
    M[lig][col] = 2
    for i in range(-2, 2):
        for j in range(-2,2):
            if dedans(lig+i,col+j) == True:
                M[lig-2][col-1]=1
                M[lig+2][col-1]=1
                M[lig-2][col+1]=1
                M[lig+2][col+1]=1
                M[lig-1][col+2]=1
                M[lig+1][col+2]=1
                M[lig-1][col-2]=1
                M[lig+1][col-2]=1
    
