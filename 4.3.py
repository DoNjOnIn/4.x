a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
x1 = int(input('x1='))
x2 = int(input('x2='))
d = int(input('d='))
for x in range(x1,x2,d):
    if x<5 and c!=0:
        f=-a*x*x-b
    elif x>5 and c==0:
        f=(x-a)/x
    else:
        f=-x/c
    print('x='+ str(x)+'f='+str(f))