import numpy as np 
import matplotlib.pylab as plt

x = np.arange(0, 4*np.pi, 0.01)
y = np.cos(x)
plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
plt.savefig('GraficaCoseno.png')