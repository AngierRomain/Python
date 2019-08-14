from random import randint

def devinette ():

    nbAlea = randint(1,100) # Tirage au sort du nombre aléatoire
    nb =0 # Initialisation de la variable nb

    while (nb != nbAlea): # tourne en boucle tant que l'utilisateur ne trouve pas le bon nombre
        nb = int(input("saisir un nombre entre 1 et 100: "))
        if (nb<nbAlea): 
            print("Le nombre est plus grand")
        elif (nb>nbAlea):
            print("Le nombre est plus petit")
        else : 
            print("Bravo, le nombre est bien ",nb) # Affiche un message "Bravo !" ainsi que le nombre
# test
##saisir un nombre entre 1 et 100: 50
##Le nombre est plus petit
##saisir un nombre entre 1 et 100: 25
##Le nombre est plus petit
##saisir un nombre entre 1 et 100: 10
##Le nombre est plus grand
##saisir un nombre entre 1 et 100: 20
##Le nombre est plus petit
##saisir un nombre entre 1 et 100: 15
##Le nombre est plus grand
##saisir un nombre entre 1 et 100: 18
##Le nombre est plus petit
##saisir un nombre entre 1 et 100: 16
##Le nombre est plus grand
##saisir un nombre entre 1 et 100: 17
Bravo, le nombre est bien  17
