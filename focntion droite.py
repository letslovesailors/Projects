def droite(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1)
    p=y1-m*x1
    return [m,p]

print(droite(-1,3,3,1))
