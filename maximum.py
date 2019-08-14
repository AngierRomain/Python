def maximum(T):
    #maximum([4,7,2,9]) renvoie 9
    Max = T[0]
    for i in range (0,len(T)):
        if T[i]> Max:
            Max = T[i]
    return Max
         
                    
