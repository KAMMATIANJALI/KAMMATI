import numpy as np
import matplotlib.pyplot as plt
p=float(input("enter the passband peak"))
s=float(input("enter the stopband peak"))
q=float(input("enter the passband freq"))
r=float(input("enter the stopband freq"))
T=np.arange(0,1000,10)
m=p*p
l=s*s
m=p*p
print(l)
print(m)
n=float((1/l)-1)
o=float((1/m)-1)
w=np.log10(n/o)
b=float(np.log10(r/q))
A=float(w/b)
Z=float(0.5*A)
print(Z)
c=float(1/(2*Z))
d=float(o/c)
print(d)
D=float(q/d)
print(D)
e=float(2*Z)
f=(1/(1+(T/D)**e))
g=(f**0.5)
plt.plot(T,g)
plt.show()

##H(s)##
