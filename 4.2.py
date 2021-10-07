import math as m
x=int(input('x1='))
x2=int(input('x2='))
d=int(input('d='))
for i in range(x,x2,d):
    d1 = i * i * m.sin(i / 2)
    if i <= -5:
        y = d1 + m.atan(m.e ** i)
    elif i > -5 and i <= 0:
        y = d1 + 1 + i ** 3 / 4
    else:
        y = d1 + m.log10(i) - i / 5
    print('x='+str(i)+'    y='+ str(y))