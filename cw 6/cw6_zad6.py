import numpy as np 
n1="jacek"
n2="place"
n3="oleje"
m1 = np.array(list(n1))
m2 = np.array(list(n2))
m3 = np.diag(list(n3))
m3[:,0]=m1
m3[0:1]=m2
print(m3)