from random import random
Macierz=[[round(random()*1000) for y in range(1+4*x,5+4*x)] for x in range(4)]
print(Macierz)
przekatnaMacierzy=[Macierz[x][x]for x in range(4)]
print(przekatnaMacierzy)