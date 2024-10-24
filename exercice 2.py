from math import *

# Demande à l'utilisateur de saisir
a = int(input("Saisir un nombre de photocopies: "))

def prix(n):
    if n <= 50 and n>0:
        return 0.15 * n
    elif n >= 51:
        return 0.10 * n
    else:
        return "c'est pas possible"
resultat = prix(a)
print("Le prix des photocopies est:", resultat)
