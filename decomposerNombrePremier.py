from math import sqrt
def premier(n):
    if(n==0 or n==1):
        return False
    for i in range(2,int(sqrt(n))+1):
                if(n%i==0):
                   return False
    return True

def decomposer(n):
    L=[] #pour réccupérer la liste des diviseurs premiers
    i=2
    while(n!=1):
        if(n%i==0 and premier(i)==True): #je calcule le reste (// = quotient entier)
            L=L+[i]
            n=(n//i)
        else:
            i=i+1
    return L

def pgcd(a,b):
    L1=decomposer(a)
    L2=decomposer(b)
    while a%b != 0 : 
      a, b = b, a%b
    return b


    
