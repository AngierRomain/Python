def pgcd(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre  a et b"""
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)
 
# tests:
print pgcd(56,42) # =>  affiche 14
