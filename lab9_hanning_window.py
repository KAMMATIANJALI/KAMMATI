import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter m value:"))
h=[]
for n in range(0,m-1):
	x=0.5-0.5*np.cos(2*np.pi*n/(m-1))
	h=np.append(h,x)
plt.plot(h)
plt.title("hanning window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.show()
