import numpy as np
import matplotlib.pyplot as plt
h=[]
for n in range(0,31):
	x=np.sin(np.pi/4*n)/(np.pi*n)
	h=np.append(h,x)
plt.stem(h)
plt.title("input signal")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.show()
