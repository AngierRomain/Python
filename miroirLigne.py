#Ecrire une fonction miroirLigne en Python qui permet de
#transformer une ligne donée en son image miroir horizontal
# Par exemple [1,1,1,0,0,1,0,0,0,1,0,0] ==> [0,0,1,0,0,0,1,0,0,1,1,1]
def miroir(L):
    for i in range(len(L)//2):
        L[i],L[len(L)-i-1]=L[len(L)-i-1],L[i]
    return T
        
