import pandas as pd 
import matplotlib.pyplot as plt

zamowienia = pd.read_csv('zamowienia.csv', header=0, delimiter=';')
ilosc=zamowienia.groupby(['Sprzedawca']).count()
ilosc=ilosc['idZamowienia']
wykres=ilosc.plot.bar()
plt.show()