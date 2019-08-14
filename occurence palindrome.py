def occurence(mot,lettre):# occurence (bonjour,0) renvoie 2
    
    occurence=0
    n=len(mot)
    for i in range(n): # occurence(maths,z) renvoie 0
        
        if(mot[i] == lettre):
            occurence += 1
    return occurence

 # palindrome(radar) renvoie True
 # palindrome(maths) renvoie False          

def palindrome(mot):
