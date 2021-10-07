import math as m
x1 = int(input('x1='))
x2 = int(input('x2='))
d = int(input('d='))
r = int(input('R='))
x=x1
while x<=x2:
    if x <= -r:
        y=r
    elif x > -r and x < r:
        y=(r - m.sqrt(r * r - x * x))
    elif x >= r and x <= 6:
        y=(r + ((-3 - r) / (6 - r) * (x - r)))
    else:
        y=x+9
    print('x='+str(x)+'    y='+str(y))
    x+=d