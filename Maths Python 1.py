from math import *
def Divis(n):
    if n%11==0:
        C="Ce nombre est divisible par 11"
    else:
        C="Ce nombre n'est pas divisible par 11"
    return C

print(Divis(120))



def RacCarre(x):
    if x>=0:
        f=1+sqrt(x)
    else:
        f=(x-1)**2
    return f

print(RacCarre(2))


def Prix(a):
    if a<0:
        b="Veuillez rentrer un nombre supérieur à 0"
    elif a<=50:
        b=a*0.15
    else:
        b=50*0.15+(a-50)*0.10
    return b

print(Prix(45))









