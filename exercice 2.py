from math import *

# Demande à l'utilisateur de saisir
a = int(input("Saisir un nombre de photocopies: "))

def prix(n):
    if n <= 50:
        return 0.15 * n
    elif n >= 51:
        return 0.10 * n  
resultat = prix(a)
print("Le prix des photocopies est:", resultat)
