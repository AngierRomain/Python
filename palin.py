def palindrome2(mot):
    for i in range(int(len(mot)/2)):
        if mot[i]!=mot[-1-i]:
            return False
    return True
def crypter(lettre,cle):
    nbre=ord(lettre)-65
    nbre=nbre+cle
    nbre=nbre%26
    return chr(nbre+65)
def cesar(mot,cle):
    newmot="" #initialisation 
    for i in range(len(mot)): #Boucle qui parcourt le mot 
        newmot = newmot + crypter(mot[i],cle) #Concaténation de newmot et de la lettre cryptée
    return newmot

    
cesar("BTS",5) renvoie 'GYX'
