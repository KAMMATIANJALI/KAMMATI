import matplotlib.pyplot as plt;
import numpy as np;
fs=int(input("enter sample frequency:"));
f1=int(input("enter first wave frequency:"));
n=int(input("enter number of samples:"));
x=np.arange(n);
a=np.cos(2*np.pi*f1/fs*x);
plt.subplot(311);
plt.plot(x,a);
plt.xlabel("samples(n)");
plt.ylabel("amplitude(v)");
plt.show();
 
