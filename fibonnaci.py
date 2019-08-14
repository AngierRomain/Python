def fibI(n): #itérative
    u=1
    v=1
    cpt=2
    while cpt <=n:
        w = u+v
        u = v
        v = w
        cpt = cpt+1
    return w
#1,1,2,3,5,8,13

def fibR(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibR(n-1) + fibR(n-2)
    
