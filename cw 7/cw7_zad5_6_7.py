import numpy as np 
m1 = np.arange(6).reshape(2,3)
a = np.sin(m1)
m2 = np.arange(1,7).reshape(2,3)
b = np.cos(m2)

print(a+b)