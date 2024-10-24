from math import *
def interval(n):
    if n >= 0 :
        c = 1 + sqrt(n)
    else :
        c = (n-1)**2
    return(interval(c))
print(interval(99))

