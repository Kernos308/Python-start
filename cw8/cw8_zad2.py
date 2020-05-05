import numpy as np 
import pandas as pd 
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
arkusz = pd.read_excel(xlsx,'Arkusz1')

#2a)
print(arkusz[arkusz['Liczba']>1000])

#2b)
print(arkusz[arkusz['Imie']=='JACEK'])

#2c)
print((arkusz.groupby(['Rok']).agg({'Liczba':['sum']})).sum())

#2d)
suma=arkusz[((arkusz.Rok >=2000) & (arkusz.Rok<=2005))]
print(suma.groupby(['Rok']).agg({'Liczba':['sum']}))

#2e)
print(arkusz.groupby(['Plec']).agg({'Liczba':['sum']}))

#2f)
imie = arkusz.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0)
print(imie)

#2g)
np=arkusz.groupby(['Plec','Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending = False).iloc[[0,1]]
print(np)