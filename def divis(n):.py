def divis(n):
    if n%11== 0:
        C="Ce nombre est divisible par 11"
    else:
        C="Ce nombre n'est pas divisible par 11"
    return C

p=int(input("saisir un nombre entier"))
print(divis(p))
