def fibonacci(n):
        tab =[]
        for I in range(50):
            n=0
            n1=n-1
            n2=n+1
            n=n1+n2
            return(tab[n])
tab = []
tab.append(50)
print(tab)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Afficher les 10 premiers termes
for i in range(10):
    print(fibonacci(i))




        
                
                

