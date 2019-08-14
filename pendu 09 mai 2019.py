def chercherLettre(mot, lettre):
    for i in range(len(mot)):
        if lettre == mot[i]:
            return True
        return False
##>>> chercherLettre("bonjour","b")
##True
##>>> chercherLettre("bonjour","p")
##False
##>>>         
def positionLettre(mot,lettre):
    L=[]
    for i in range(len(mot)):
        if lettre == mot[i]:
            L=L+[i]
    return L
##>>> positionLettre("bonjour","o")
##[1, 4]
##>>> positionLettre("bonjour","j")
##[3]
##>>> 
def pendu():
    secret = input("Le Joueur 1 saisit un mot a deviner: ")
    #Au moment de la saisie ne pas oublier les doubles cotes

    nbErreurs=0 #Compteur du nombre d'erreurs commises
    nbTrouvees=0 #Compteur du nombre de lettres trouvées par le joueur 2
    while nbErreurs < 10 and len(secret) >= nbTrouvees:
        lettre=input("Le Joueur 2 saisit une lettre: ")
    print lettre
