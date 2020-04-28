import numpy as np

a = np.arange(2,25,2)
b=a.reshape(3,4)
c=a.reshape(4,3)
d=a.reshape(2,6)

b=b.ravel()
c=c.ravel()
d=d.ravel()
print(a)
print(b)
print(c)
print(d)