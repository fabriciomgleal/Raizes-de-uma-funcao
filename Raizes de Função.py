#import numpy as npi
#fx = [1/3,1/2,0,0]
#raizes = npi.roots(fx)
#print(raizes)
#teste#
list = []
x=-1000.0
while x < 10.0:
    fx = x**2+2
    if fx != round(0.0):
        x = x+1
        continue
    elif fx == round(0.0):
        list.append(x)
        x = x+1
        continue
print(list)