def triBulle(T):
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        for i in range(0, len(tableau) - passage):
            if tableau[i] > tableau[i + 1]:
                permutation = True
                # On echange les deux elements
                tableau[i], tableau[i + 1] = \
                tableau[i + 1],tableau[i]
    return tableau  
