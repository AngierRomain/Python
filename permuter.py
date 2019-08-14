def permuter(a,b):
    c=a
    a=b
    b=c
    return a,b

def permuter2(a,b):
    a,b = b,a
    #échange les valeurs de a et de b
    return a,b
    
