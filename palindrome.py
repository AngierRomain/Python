def palindrome(mot):
    a = int(len(mot)/2)
    for i in range(0,a):
        if mot[i] != mot[len(mot)-i-1]:
            return False
        return True

#battlepoint.io

def palindrome2(mot):
    for i in range(len(mot)):
        if mot[i] != mot[-1-i]: # -1 -i pour symétrique
            return False
        return True

def crypter(lettre,cle):
    nbre=ord(lettre)-65
    nbre=nbre+cle
    nbre=nbre%26
    return chr(nbre-65)


def cesar(mot,cle):
    newmot=''
    for i in range(len(mot)): #Boucle qui parcourt le mot
        newmot = newmot + crypter(mot[i], -cle) #Concaténation de newmot et de la clé
    return newmot

#def decrypter:
    

