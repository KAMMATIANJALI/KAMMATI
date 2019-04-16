from scipy import *
import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
from dftfun import dft
n=int(input("enter number of samples for x1[n]:"))
x1=[]
N=int(input("enter order of dft:"))
print("enter samples of x1[n]:")
for i in range(0,n-1):
	x=int(input())
	x1=np.append(x1,x)
print("x1[n]=",x1)
X1=dft(x1,N)
print("X1[n]=",X1)
print("enter samples for x2[n]:")
x2=[]
for i in range(0,n-1):
	z=int(input())
	x2=np.append(x2,z)
print("x2[n]=",x2)
X2=dft(x2,N)
print("X2[n]=",X2)
y=[]
y=X1[i]*X2[i]
print("circular convolution is y=X1[n]*X2[n]=",y)
