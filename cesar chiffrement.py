def cesar(mot): #mot à crypter
    Alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_mot="" #mot crypté
    for i in range(len(mot)):
        nb = ord(mot[i])
        nb = nb+3
        nb = nb % 26
        new_mot = new_mot + Alphabet[chr(65)]
        
        
