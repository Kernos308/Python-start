import pandas as pd 
z = pd.read_csv('zamowienia.csv', header=0, delimiter=';')


#3a)
unikalne=z['Sprzedawca'].unique()
print(unikalne)

#3b)
maxx=z.sort_values('Utarg', ascending = False).iloc[[0,1,2,3,4]]
print(maxx['Utarg'])

#3c)
ilosc=z.groupby(['Sprzedawca']).count()
print(ilosc['idZamowienia'])

#3d)
suma=z.groupby(['Kraj']).count()
print(suma['idZamowienia'])

#3e)
suma2 = z[(z['Data zamowienia'] >= '2005-01-01') & (z['Data zamowienia'] <= '2005-12-31') & (z['Kraj']=='Polska')].groupby(['Kraj']).count()
print(suma2['idZamowienia'])

#3)
srednia = z[(z['Data zamowienia'] >= '2004-01-01') & (z['Data zamowienia'] <= '2004-12-31')].mean()
print(srednia['Utarg'])

#3g)
rok24 = z[(z['Data zamowienia'] >= '2004-01-01') & (z['Data zamowienia'] <= '2004-12-31')]
rok25 = z[(z['Data zamowienia'] >= '2005-01-01') & (z['Data zamowienia'] <= '2005-12-31')]
rok24.to_csv('zamowienia_2004.csv', header=None)
rok25.to_csv('zamowienia_2005.csv', header=None)