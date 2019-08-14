def pgcdDiff(a,b): #algorithme de la différence
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
