import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter m value:"))
h=[]
for n in range(0,m-1):
	x=1
	h=np.append(h,x)
plt.stem(h)
plt.title("rectangular window")
plt.ylabel("----->w")
plt.xlabel("----->n")
plt.show()


