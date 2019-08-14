def esttriee(T):
    for i in range(len(T)-1): #sert à parcourir le tableau T
        if T[i]>T[i+1]: #Si deux éléments sont rangés dans l'ordre contraire
            return False #cela signifie que la liste n'est pas triée
        return True
